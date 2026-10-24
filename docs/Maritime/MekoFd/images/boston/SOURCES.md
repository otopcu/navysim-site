# Boston runtime captures

Actual Stride/Direct3D11 MekoFd Debug output, 18 October 2026, AMD Radeon 890M. `--offline --no-dialog --verify-boston` drew 100 frames across harbor, shore, island, measured seabed and ATD cases. Calm water was used for terrain inspection. No replacement UI or painted terrain is present.

Terrain: NOAA NCEI CUDEM MA_NH_ME 2021v1, reduced to a 25 m visual grid. Retained metadata, hashes and reference heights: `Implementation/Library/Geography/Regions/boston-harbor`. Land cover is generic, not aerial photography. Building/port assets and terrain grounding are not claimed. See [regional architecture](../../../Shared/RegionalTerrain.md).

## Harbor structure captures — 18 October 2026

`skyline-structures.png`, `fish-pier-structures.png` and `atd-structures.png` are unedited native Release Stride/D3D11 application captures from `--offline --no-dialog --verify-boston-harbor`. The AMD Radeon 890M run completed 100 frames across five reviewed views. `structures-map.png` is the actual shared Mapsui chart render with US5MA12M and US5MA11M applied updates plus the same normalized building/pier footprints. Its attribution is City of Boston GIS / NOAA / © OpenStreetMap contributors, ODbL: https://www.openstreetmap.org/copyright . The screenshots are visual observations, not surveyed geometry/photographic facade claims. See the shared HarborStructures architecture and the retained source manifests.
