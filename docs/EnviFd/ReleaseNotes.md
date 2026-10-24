# EnviFd Release Notes

## Shared Boston regional default

Initial Environment FileName and DLLC now come from the shared geographic catalog: `boston-harbor`, 42.315°N / 71.025°W. This avoids a first publication resetting MekoFd to 0°/0°. Explicit Scenario terrain/origin overrides and generated encoding remain supported. [Regional terrain](../Maritime/Shared/RegionalTerrain.md).

## Scenario manager interoperability

EnviFd remains an optional independent meteorology station/external editor. ExMFd publishes scenario weather through base Environment OC. No custom NavyScenario module, command handler or application receipt endpoint is required. Normal Scenario/Begin receivers and local clocks remain. Generated base source is unchanged; version remains 5.0.0.

## SimGe user export integrated — 2026-10-18 04:01:30

Imported the user-generated `nstmss/SourceCode/20261018040130` FDD, generated sources and API guides. Application-owned managers/entities remain intact. FDD 5.0.0 is coordinated with NFL/MEKO/ExMFd; Envi retains Environment and WeatherReport responsibilities without injection subscriptions. Shared FDDs match; obsolete imported SOM copies absent from this export are removed. Build, import verification and current local/live application checks validate the actual user output.

## Standard sea and wind presets — 2026-10-17

Sea Control now offers SS0–SS9 with shared Hs/Tp and ANEP reference wind at 19.5 m. Wind can be overridden independently; selecting another SS restores reference wind. Removed individual Wave controls/state. Regenerated fifteen-field Environment and typed weather-report contracts match Meko/NFL 4.0.0. All-code live exchange, WPF and lifecycle/advisory tests pass.

> Source: *Implementation/FdApps/EnviFd/Docs/RN EnviFd.docx*
>
> Environment Controller Federate. See also: [EnviFd Installation Manual](InstallationManual.md) · [EnviFd User Manual](UserManual.md) · [EnviFd Architecture](Architecture.md) · [NavySim Release Notes](../ReleaseNotes.md) · [Known Bugs](../Known%20Bugs.md#envifd) · [Roadmap](../Roadmap.md#envifd)

| | |
|---|---|
| **Current version** | 5.0.0 (set in `Implementation/FdApps/EnviFd/Version.props`) |
| **Suite release** | NavySim 2026.1 (in development) |
| **Developed by** | Okan TOPÇU (okantopcu@gmail.com) |

## Contents

- [Version summary](#version-summary)
- [Version history](#version-history)

## Version summary

- **2026-10-12 — Shared generated runtime:** Discovery deferral/guards, client log/error forwarding and startup readiness move to SimGe bases with manual overrides. Domain/UI behavior remains. Incremental manual source reduction: 6 lines including comments/blanks. Three-app 60-case live default/override probe and existing Envi/Meko pairing, WPF close/reconnect and Meko transport-loss checks pass.

- **2026-10-12 — Declared Environment lifecycle:** Generated runtime now registers the model-declared Environment with AdvisoryDriven timing, tracks the entity and resets declaration state on reconnect. Manual registration callback/state removed; runtime UI values remain a single hook. Default Stop Registration retains the object, with manual registration/deletion policy overrides available. Manager reduced by 15 source lines; 12 new live lifecycle, 31 advisory, 22 interoperability and 22 WPF checks pass. Version remains 5.0.0.

| Version | Latest change | NSTMSS release | Platform / RTI layer                                         |
| ------- | ------------- | -------------- | ------------------------------------------------------------ |
| 5.0.0   | 2026          | 2026.1         | .NET 10, Fora, NFL 3.1.2                                     |
| 4.0.2   | —             | —              | VS Enterprise 2017, Windows 10 Pro, RACoN 0.0.1.7, NFL 2.0.2 |
| 4.0.1   | 01.02.2016    | —              | —                                                            |
| 4.0.0   | 24.09.2015    | —              | VS 2015 Community, Windows 10 Pro, RACoN 0.0.1.7             |
| 3.1.0   | 28.07.2011    | 5.2            | VS 2010 Ultimate, Windows 7, RACoN 0.0.0.4                   |
| 3.0.0   | 01.05.2009    | 5.1            | VS .NET 2008, Windows Vista, WPF, Portico 0.8                |
| 2.1.2   | 11.11.2006    | 5.0.1          | —                                                            |
| 2.1.1   | 11.02.2006    | 5.0 (v2.1.x)   | VS .NET 2005                                                 |
| 2.1.0   | 25.08.2005    | —              | —                                                            |
| 2.0.1   | 23.08.2005    | 4.2            | —                                                            |
| 2.0     | 13.06.2005    | 4.1            | VS .NET 2005 Beta 2                                          |
| 1.22    | 30.10.2002    | 3.0            | Windows, RTI-NG                                              |
| 1.3     | 18.08.2001    | 2.0            | —                                                            |
| 1.2     | 2000          | 1.2            | —                                                            |
| 1.11    | 31.10.1999    | 1.1            | Windows                                                      |
| 1.1     | —             | —              | IRIX with Performer                                          |

> The *NSTMSS release* column comes from the "Main release for NSTMSS x" remarks here and the federate versions in the [NavySim Release Notes](../ReleaseNotes.md).

## Version history

## [5.0.0] - Unreleased

**By:** Okan TOPÇU

Ported from .NET Framework 4.6 (WPF, RACoN 0.0.1.7, native RTI) to .NET 10 WPF over Fora.Client 20261004.0.0 (IEEE 1516-2025) with a SimGe-generated runtime in `SimulationLayer/Generated`. Includes the .NET 10 move first numbered 4.1.0, which was not released.

### Infrastructure

- **Target platform and architecture:** Targets .NET 10 (`net10.0-windows`) and C# 14. Modernized into a layered solution structure: `SimulationLayer`, `PresentationLayer`, `EnviFdUI-Wpf`, and shared test assemblies (`tests/EnviFd.Tests`, `tests/EnviFd.Wpf.Tests`).
- **Fora RTI integration:** Migrated from RACoN and native DMSO/OpenRTI DLLs to modern Fora (`Fora.Client 20261004.0.0`, IEEE 1516-2025). NFL 3.1.2 is decoupled from federate execution and supplies only UI/MVVM/clock and fog/wind/wave helpers.
- **Generated runtime:** Uses SimGe-generated backend (`SimulationLayer/Generated`): machine-owned codecs, SOM definitions, advisory hook routing and wire pumping. Application code maintains typed scaffolds (`SimulationManager : SimulationManagerBase` and `EnviFd : EnviFdBase`).
- **Ambassador boundary:** Production `EnviAmbassadorBase` is removed from production code and converted to internal test support (`tests/Shared`) linked into test assemblies.
- **Session lifecycle and resilience:** Reconnect preserves manager, UI controls, settings and Environment state while establishing a fresh ambassador, Fora client, SOM and Environment identity. Startup failure/retry, HF regions and Scenario discovery remain isolated per session. Safe close completes resign and disposal before window teardown without dispatcher exceptions.
- **Cleaned legacy components:** Removed redundant `StartUp.cs` (WPF entry point generated by `App.xaml`), `RTI.rid`, unused PresentationLayer resource designer/files/logo copy, unused resource manager/text validator, `MainSimulationLoop`, empty register/unregister methods, and legacy `CSimulationManager`/`CEnviFd` facade classes.

### FOM Module

- **Coordinated NavySim FOM:** Packages and loads `Fom/NavySim.xml` by default (coordinated with FOM 3.1.1 / 4.0.0 across NFL and MekoFd) and transmits its content directly to Fora on startup.
- **SOM capability declarations:** Publishes 15 typed Environment attributes (aligned with Meko/NFL 4.0.0; legacy `Wave1`–`Wave4` attributes removed), subscribes to nine Scenario attributes (`ScenarioTitle`, `ScenarioVersion`, `ScenarioLocation`, `ScenarioStartTime`, `WeatherReportBroadcastInterval`, `DLLCLat`, `DLLCLong`, `TerrainFileName`, `ScenarioDescription`), and subscribes to `BeginToPlay`. Neither payload fields and inactive leaf classes are omitted from P/S.
- **Weather report publication:** Publishes `WeatherReport` interaction through the HF [3, 30) MHz region with typed SeaState enum (SS0–SS9) and formatted weather observation fields.
- **Advisory relevance routing:** ObjectClass, Attribute, and Interaction Relevance advisories are active (Attribute Scope remains OFF). Publication helpers suppress inactive fields and silent updates when no subscribers are present, while On flushes latest values. Calls with no active relevant payload return `false` and emit no wire traffic.

### Environment Simulation

- **Standard sea and wind presets:** Implements standard WMO Sea State 0–9 (SS0–SS9) with shared ANEP reference significant wave height (`Hs`), peak period (`Tp`), and mean wind speed (knots at 19.5 m) via `NavySim.EnvironmentModel`.
- **Decoupled wind controls:** Wind speed and direction can be overridden independently while retaining the selected Sea State; selecting a new Sea State resets wind to the reference value.
- **Advisory-driven lifecycle:** Object registration waits for `StartRegistration`; initialization completes without waiting for a subscriber. Field On flushes current UI values (including edits made while automatic updates were disabled); field Off suppresses affected fields. Explicit value responses select requested fields and check ownership through the generated provider independently of relevance.
- **Weather report timing:** Scenario `BeginToPlay` starts periodic weather report broadcasts governed by `WeatherReportBroadcastInterval`. Dynamic interval updates adjust the timer, and setting interval to zero disables periodic transmission. Manual send remains available.

### User Interface

- **WPF MVVM presentation:** WPF GUI modernized under `EnviFdApp` with clean MVVM structure and presenter (`MainVM`, `CUIControl`, `MainWindow`). Window title and About dialog display Version 5.0.0 (`EnviFdApp v.5.0.0`).
- **Sea state & wind controls:** Sea Control tab updated to standard SS0–SS9 combo box and independent wind numeric controls. Obsolete individual wave tabs and controls are removed.
- **Fora Messages panel:** Connects the generated `RtiLogged` event to the Fora Messages panel at Verbose level. Delivers client logs on the presentation thread (including failed startup and cleanup while the tick timer is stopped); scrolls automatically to the latest entry; reconnect does not duplicate log entries.

### Validation

- **Automated test suite:** Comprehensive unit, smoke, and live WPF tests in `tests/EnviFd.Tests` and `tests/EnviFd.Wpf.Tests`.
- **MekoFd interoperability:** Verified paired execution, live RTI data exchange, and 600 frames rendered in Stride. Subscriber joining/leaving and graceful exit of MekoFd preserve EnviFd connection.
- **Advisory policy verification:** Passes 89 distinct policy checks (delayed registration, 35/36-field unions, partial Off, zero traffic after last Off, subscriber rejoin, and full reconnect) and 51 cross-application policy checks.
- **Build and publish:** Clean builds in Release (0 errors, 0 warnings) and Debug configurations, verifying published WPF runtime and assembly versioning (5.0.0.0).
- **Validation records:**
  - [Publication integration evidence](../../../Implementation/Library/NFL/SimGeSync/20261012-publication-integration/validation.json)
  - [Advisory step 1 integration evidence](../../../Implementation/Library/NFL/SimGeSync/20261012-advisory-step1-integration/validation.json)
  - [Advisory policy validation](../../../Implementation/FdApps/EnviFd/Modernization/advisory-policy-20261012/validation.json)
  - [Cleanup validation](../../../Implementation/FdApps/EnviFd/Modernization/cleanup-20261012/validation.json)
  - [EnviFd build guide](../../../Implementation/FdApps/EnviFd/Code/README.md)

---
## [4.0.2]

**By:** Okan TOPÇU
- Compatible with RACoN 0.0.1.7.
- Compatible with NFL 2.0.2.
- Compiled with MS Visual Studio Enterprise 2017 on Windows 10 Pro.

---

## [4.0.1] - 2016-02-01

**01.02.2016**
- HLA class functionality for `ScenarioOC`, `BeginToPlayIC` and `EnviOC` is implemented.
- About box is implemented.

---

## [4.0.0] - 2015-09-24

**24.09.2015**
- Compiled with MS Visual Studio 2015 Community on Windows 10 Pro.
- Compatible with RACoN 0.0.1.7.

---

## [3.1.0] - 2011-07-28

**28.07.2011**
- A PresentationLayer (interface class and controller) is built to support multiple GUIs: one for WPF and one for Windows Forms.

**24.07.2011**
- Adapted to RACoN 0.0.0.4.
- The Passive View pattern is implemented.
- A few UI changes.

**19.12.2010**
- Compiled with MS Visual Studio 2010 Ultimate on Windows 7 Ultimate.

**15.08.2009 — major architecture enhancements**
- Generic RTI layer and simulation layer are implemented.

---

## [3.0.0] - 2009-05-01

**01.05.2009**
- Report viewer code is refined.

**22.09.2008**
- `NFL.Objects.CFog` is adapted.

**10.05.2008**
- Presentation layer based on MS Windows Presentation Foundation (WPF) is implemented.
- New user interface based on expanders is implemented.

**30.04.2008**
- EnviFd is re-architected according to the Model-View-Controller design pattern.
- Wave status displays and controls are added (integration with Canku's thesis).

**02.04.2008**
- RTI methods are compatible with Portico 0.8.

**20.12.2007**
- Compiled with MS Visual Studio .NET 2008.

**16.02.2007**
- Compiled on Windows Vista Ultimate.

---

## [2.1.2] - 2006-11-11

**11.11.2006** — *Can Alp CALARGUN*
- Wave properties are controlled by EnviFd and changes are sent via the RTI.

---

## [2.1.1] - 2006-02-11

**11.02.2006** — *Okan TOPÇU*
- Scheduled weather report broadcast is implemented.
- NSTMSSComponents Scenario class is adapted.
- Compiled with MS Visual Studio .NET 2005 (previously RC-1).
- About dialog is implemented.

---

## [2.1.0] - 2005-08-25

**25.08.2005**
- `updateXXX()` calls are implemented.
- Terrain information is no longer sent via EnviFd.
- Subscription to the Scenario and BeginToPlay classes is implemented.
- Weather Report interface is implemented.
- Wind Status interface is implemented.
- Weather Status Monitor is implemented.

---

## [2.0.1] - 2005-08-23

**23.08.2005** — *Aslı KILIÇ*
- Terrain information is sent via the RTI.

---

## [2.0] - 2005-06-13

*Main release for NSTMSS 4.1*

**13.06.2005** — *Okan TOPÇU*
- Compiled with MS Visual Studio .NET 2005 Beta 2.

**29.01.2005**
- "End of line character" bug is removed.

**04.09.2004**
- New GUI implemented as a Visual Studio Managed C++ .NET application.
- Instant (automatic) and manual update modes are implemented.
- Sea State attribute is implemented.

**30.08.2004**
- Version changed to 1.22 (formerly 2.0).

**06.10.2003 — Main release for NSTMSS 4.0**
- Win2000 · MS Visual Studio .NET 2003 · DMSO RTI NG 1.3v6

> Entries are listed in the same order as in the source table.

---

## [1.22] - 2002-10-30

*Main release for NSTMSS 3.0*

**30.10.2002**

**17.08.2001**
- EnviFd is adapted to work with RTI-NG v3.1.
- MS Windows implementation.
- Upgraded from 1.1, not from 1.11.
- Release notes re-formatted as HTML and `.doc` files.

---

## [1.3] - 2001-08-18

*Main release for NSTMSS 2.0*

**18.08.2001**
- `PrintUsage()` function is deployed.
- EnviFd is adapted to Hasan's thesis (combination of 1.2 and 1.11).

---

## [1.2] - 2000

*Main release for NSTMSS 1.2 (Hasan's thesis)*

**2000**
- EnviFd now waits for TASKORD from OSEFd to extract the environment file name.

**09.1999 — Demo release for NSTMSS 1.1**
- Demo version for Okan's thesis.
- The main simulation loop ticks automatically; keyboard events are caught with Performer libraries.

---

## [1.11] - 1999-10-31

*Main release for NSTMSS 1.1*

**31.10.1999** — *Hasan Basri AKIRMAK*
- Subscription to the OTC object is implemented for late-joining OTCFds. Windows implementation.

---

## [1.1]

*Okan TOPÇU* — IRIX with Performer.

---

*Modification DTG: 2026-10-18 (UTC+03:00)*
