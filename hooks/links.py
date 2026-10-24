"""MkDocs hook: keep wiki links that point outside the published site from breaking the build.

NavySimWiki pages link to source files, solutions and wiki pages that are not
published (see pages.txt). On the site such a link would be a 404, so this hook
turns it into plain text (or drops the image) before MkDocs validates links.
Links inside fenced or inline code are left untouched.
"""

from __future__ import annotations

import posixpath
import re
from urllib.parse import unquote

_FENCE = re.compile(r"^(\s*)(`{3,}|~{3,})")
_INLINE_CODE = re.compile(r"(`+)(?:(?!\1).)+?\1")
# [text](target "title") and ![alt](target)
_LINK = re.compile(r"(!?)\[((?:[^\[\]]|\[[^\[\]]*\])*)\]\(\s*<?([^)\s>]+)>?(\s+\"[^\"]*\")?\s*\)")
_EXTERNAL = re.compile(r"^(?:[a-z][a-z0-9+.-]*:|#|//)", re.IGNORECASE)

_published: set[str] = set()


def on_files(files, config):
    _published.clear()
    for f in files:
        _published.add(f.src_uri)
    return files


def _resolve(page_uri: str, target: str) -> str | None:
    path = unquote(target.split("#", 1)[0].split("?", 1)[0])
    if not path:
        return None
    if path.startswith("/"):
        resolved = path.lstrip("/")
    else:
        resolved = posixpath.normpath(posixpath.join(posixpath.dirname(page_uri), path))
    return resolved


def _exists(resolved: str) -> bool:
    if resolved.startswith(".."):
        return False
    if resolved in _published:
        return True
    # Directory links resolve to their index or README page.
    base = resolved.rstrip("/")
    return any(f"{base}/{name}" in _published for name in ("index.md", "README.md"))


def _rewrite_line(line: str, page_uri: str) -> str:
    def replace(m: re.Match) -> str:
        bang, text, target, _title = m.groups()
        if _EXTERNAL.match(target):
            return m.group(0)
        resolved = _resolve(page_uri, target)
        if resolved is None or _exists(resolved):
            return m.group(0)
        return "" if bang else text

    # Leave links that start inside an inline code span alone; link text may itself contain code.
    code = [(cm.start(), cm.end()) for cm in _INLINE_CODE.finditer(line)]

    def guarded(m: re.Match) -> str:
        if any(start <= m.start() < end for start, end in code):
            return m.group(0)
        return replace(m)

    return _LINK.sub(guarded, line)


def on_page_markdown(markdown, page, config, files):
    out, fence = [], None
    for line in markdown.split("\n"):
        m = _FENCE.match(line)
        if fence:
            if m and m.group(2)[0] == fence[0] and len(m.group(2)) >= len(fence):
                fence = None
            out.append(line)
            continue
        if m:
            fence = m.group(2)
            out.append(line)
            continue
        out.append(_rewrite_line(line, page.file.src_uri))
    return "\n".join(out)
