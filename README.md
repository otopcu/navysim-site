<!-- Generated content — do not edit this repository directly. -->

# navysim-site (generated)

This repository is **generated and published automatically** from the NavySim documentation.
Do not edit files here by hand — changes will be overwritten on the next publish.

- **Source of truth:** `Documentation/NavySimWiki` and `Documentation/site` in the NavySim repository.
- **Public pages:** Home (`index.md`), Components and What's New are authored in `NavySimWiki/Web/` and published at the documentation root with the same filenames.
- **Selected wiki pages:** `site/pages.txt` lists which wiki pages are published; images they reference are copied with them. Links to unpublished pages or source files become plain text at build time (`hooks/links.py`).
- **Site configuration:** `Documentation/site/` contains `mkdocs.yml`, the link hook, the deployment workflow (`deploy.yml`, installed as `.github/workflows/deploy.yml`) and this README.
- **Publish:** run `Documentation/site/publish-site.ps1` in the NavySim repository.
- **Live site:** https://otopcu.github.io/navysim-site/
