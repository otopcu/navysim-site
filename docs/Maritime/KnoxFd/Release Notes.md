# KnoxFd Release Notes

| | |
|---|---|
| **Current version** | **5.0.0**, modern C# / shared maritime runtime |
| **Suite release** | NavySim 2026.1, in development |
| **Original final version** | 4.5, last updated 18.01.2002 |

## Contents

- [5.0.0](#500)
- [Legacy release history](#legacy-release-history)
- [Historical known bugs](#historical-known-bugs)
- [Current known issues](Maritime/KnoxFd/Known%20Issues.md)

## [5.0.0] - Unreleased

### Infrastructure

- Resumes the original KnoxFd lineage as **5.0.0**, with the component version defined in `Implementation/FdApps/KnoxFd/Version.props`.

- Adds `KnoxFd.App` as a separate executable composition root over the shared maritime host, with Knox build/run/package entry points.
- `KnoxFd.Vessel` owns Akdeniz identity, visual-profile selection, hull/ensign/exhaust metadata, seven OOW poses and declared capabilities. The executable registers the available modules; common sea, controls, UI and rendering are reused.

### Ship Model & Rendering

- Adds TCG Akdeniz **F257** artwork on the existing coarse Knox geometry, corrected normals, matte paint/decks, new UV subdivisions and startup preview. Attribution/rebuild instructions are retained. Baked F257 does not follow later hull-number edits; unrelated DCS normal/mantlet maps are not reused.
- Adapts the downloaded Freddie Akdeniz DCS hull/grey paint artwork to the original NavySim Knox geometry. Paint-boundary subdivisions preserve hierarchy, bounds and total surface area; source FLT and physical shape remain unchanged. Sea/weather controls and national flags use the common host.

### UI Controls

- Adds a default-open **INSTRUMENTS** toggle. Closing expands the 3D/ENC/radar workspace and leaves translucent read-only engine orders plus ordered/actual rudder angles; narrow views use two rows and faults retain LOCKED. Session choice survives center/Settings/F8 changes, commands cannot leak through the overlay, and reports stay above it. Retains digital speed/course/coordinate layout with sharper displayed-size dynamic text. Both builds, focused regressions and 26 native MEKO cases pass. [Behavior and validation](../Shared/InstrumentStrip.md).

- Adds the shared **bridge-arc rudder** to the existing lower status strip: red port/green starboard sectors, outlined ORDER diamond, separate physical ACTUAL needle/readout and MANUAL/HELMSMAN/LOCKED status. The lower gripped rail retains fifteen 5° stops, adds hovered-wheel detents and MIDSHIPS with guarded manual takeover. EOT, navigation and OOW areas are preserved. Focused tests, both Release builds and 15 native MEKO cases pass. [Operation and validation](../Shared/EotConsole.md#bridge-arc-rudder).

- Moves **OOW EYE** true look bearing from the lower status strip to the upper-left main view across all centers. Retains a compact NAV/F8 indication, follows drawers, avoids the clock at narrow sizes and wraps rounded north correctly. All-center layout/value tests and 25 actual center/F8 captures pass. [Shared behavior](../Shared/EotConsole.md#persistent-oow-eye-bearing).

- Replaces the shared lower EOT button rows with compact horizontal levers: **STARBOARD green above PORT red**, prominent STOP, drag preview with one command on release, and independent hovered-rail wheel detents. Retains the existing rudder/navigation strip, F8 and machinery authority. Focused regressions, both builds, ten native review cases and physical mouse checks pass. [Operation and validation](../Shared/EotConsole.md).

- Adds shared scan-held TRD contacts, sweep-lit mapped coast, GREEN/AMBER/MULTI palettes, SHORT/MEDIUM/LONG persistence and four corner instruments (range/rings, echo controls, cursor, selected-echo age/measurements). Source returns remain synthetic. MEKO native review: 22 cases / 3,960 frames; shared scan/layout/input tests and both builds pass. [Details](../Shared/NavigationRadar.md#scan-echoes-colour-and-corner-instruments).

- Reuses the shared **ATD console**: seven-step rotary/rail chart span, independent PIN/CURSOR readout cards, true bearing/NM/WGS84 presentation and header CLEAR. OOW, EOT and Inspect/Safety are preserved. Shared input/format/layout tests and MEKO native captures document the change. [Details](../Shared/AtdConsole.md).

- Reuses the shared **TRD Twin Encoder** console: independent EBL/VRM rotary controls with wheel and captured dragging, a nine-stop range rail, retained upper-left live OOW and fixed lower EOT/rudder. The shared input/layout tests cover wrap, limits, range/VRM preservation and cancellation; the actual native captures were recorded with MEKO. [Controls and evidence](../Shared/NavigationRadar.md#twin-encoder-console).
- Fixes ATD span and TRD EBL/VRM circular dragging: relative multi-turn rotation, centre scrubbing, immediate reversal at bounded stops, persistent focus rings, Tab/arrow adjustment and capture precedence over OOW/other controls. [Input validation](../../../../Implementation/Library/Maritime/Validation/rotary-input-20261024/README.md).

### Validation

- Retains the livery's Release build, profile/render-quality checks, wizard verification, unchanged hierarchy/bounds/surface-area checks and actual port/starboard/quarter/top/sea captures.
- The modular delivery also records a real Knox Debug scene, fresh publish/startup checks and **14 Knox sea-state cases / 840 frames**. These are numerical/UI/rendering and packaging checks, not real-vessel handling calibration.

[Architecture](Architecture.md) · [Known issues and capability limits](Maritime/KnoxFd/Known%20Issues.md) · [User manual](Maritime/KnoxFd/UserManual.md) · [Shared modules](../Shared/Modules.md).

[Livery attribution and regeneration](../../../../Implementation/Library/Maritime/Assets/ships/knox-akdeniz-v1/Attribution.md) · [Livery evidence](../../../../Implementation/FdApps/MekoFd/Docs/Validation/knox-akdeniz-20261017.json) · [Modular validation](../../../../Implementation/Library/Maritime/Docs/Validation/modularity-20261017.json).

---

## Legacy Release History

This history is transcribed from the original **FRIGATE (TYPE=KNOX) FEDERATE [KNOXFd]** notes supplied by Okan TOPÇU. That document identifies **4.5**, last updated **18.01.2002**, as the final version of the original implementation. The modern C# application resumes the KnoxFd lineage as **5.0.0**.

**Originally developed by:** Okan TOPÇU ([otopcu@ceng.metu.edu.tr](mailto:otopcu@ceng.metu.edu.tr), historical contact).

| Legacy version | Recorded date | Changes | By |
|---|---|---|---|
| **4.5** | 18.01.2002 | Original notice: **“KNOXFd is not supported and developed anymore. This is the final version.”** This notice applies to the original implementation. | Okan TOPÇU |
| **4.5** | 2001 | Main release for NSTMSS2; runs on RH Linux 7.1 with RTI-NG 1.3rel3.1. | Okan TOPÇU |
| **4.41** | 03.09.2001 | Main release for NSTMSS1.3 and NSTMSS 3.0. | Okan TOPÇU |
| **4.4** | 26.02.2000 | Main release for NSTMSS1.1 (Okan's thesis). Code enhanced to follow the NSTMSS FOM class structure; distinguishes KNOX and MEKO frigates. | Okan TOPÇU |
| **4.31** | 13.10.2000 | Main release for NSTMSS1.2 (Hasan's thesis). Adds time management and event injections. | Hasan Basri AKIRMAK |
| **4.3** | 15.12.1999 | IRIX main release for NSTMSS1.1 (Okan's thesis). Enhances radar functionality and calculates bearing/distance for the selected echo. | Okan TOPÇU |
| **4.2** | 05.11.1999 | Adds CommunicationSpace. | Okan TOPÇU |
| **4.1** | 31.10.1999 | Adds `setUpdateFlags()` to fix a bug. | Okan TOPÇU |
| **4.0** | 30.10.1999 | Implements the dead-reckoning algorithm. | Okan TOPÇU |
| **3.6** | 29.10.1999 | Starts extracting the sound system; records RTI system-call bug fixes and adds the Channel Selection GUI. | Okan TOPÇU |
| **3.5** | 27.10.1999 | Fixes scene-creation and too-many-lights bugs. | Okan TOPÇU |
| **3.4** | 26.10.1999 | Separates the radar scene so time and fog changes no longer affect it. | Okan TOPÇU |
| **3.3** | 26.10.1999 | Implements TOD and fog. | Okan TOPÇU |
| **3.2** | 23.10.1999 | Reads the environment-file name from the environment. | Okan TOPÇU |
| **3.1** | 21.10.1999 | Starts extracting the message-mode changer from the main loop. | Okan TOPÇU |
| **3.0** | 19.10.1999 | Implements the `sGUI` class hierarchy. | Okan TOPÇU |
| **2.1** | 18.10.1999 | Encapsulates all RTI-related code in `rtiAmb_class`. | Okan TOPÇU |

Version labels, dates and NSTMSS release associations are retained as supplied, including their original ordering.

## Historical Known Bugs

The original notes list:

- Many compiler warnings.
- Bearing and distance do not become zero when there is no contact.

These are reports for the original implementation, not confirmed defects in 5.0.0. Current capability limits are maintained separately in [Known Issues](Maritime/KnoxFd/Known%20Issues.md).
