# Sen Known Issues — 3.0.0

- Supports the documented NavySim C2SIM profile, not every XSD-valid C2SIM construct. Unsupported content is rejected explicitly.
- The Sandbox supports NOAA ENC / OSM / OpenSeaMap placement, but map viewport/layer preferences are not persisted and portrayal is simplified. Placement does not check depth or safe water. Boston is the new authoring default; MekoFd includes measured Boston terrain; coverage is 12.8 × 12.8 km with 25 m visual mesh, generic land cover and no terrain collision/grounding. Timeline bars are edited through Properties, without drag rescheduling. Organization/OTC cards from the dummy are outside the current profile.
- No terrain loading, route/condition/objective authoring, multi-document project system, recent-file list or automatic legacy converter.
- Saving uses staging plus rollback for ordinary errors; it is not durable crash recovery. Use dedicated two-file folders and external backups.
- Package validation cannot establish live participant capability or vessel calibration. ExMFd preflight currently supports one MEKO200 per participant; Knox own-ship remains separate work.

Former empty-form, NSDL DataSet and uneditable timeline limitations no longer describe active Sen. See [architecture](Architecture.md), [manual](UserManual.md) and [validation](../../../Implementation/Library/Scenarios/Validation/c2sim-migration-20261018.json).
