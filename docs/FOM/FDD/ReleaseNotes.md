# NavySim FDD Release Notes

> Sources: *Documentation/Archieve/FED/releasenotes_FED.doc* (HLA 1.3 FED files), the `modelIdentification` of each `NavySim.xml`, and the [NFL Release Notes](../../NFL/ReleaseNotes.md) (versions 3.1.0–3.1.1).
>
> See also: [NavySim FOM](../Fom.md) · [NavySim Release Notes](../../ReleaseNotes.md) · [RID Release Notes](../RID/ReleaseNotes.md)

| | |
|---|---|
| **Deployed version** | 5.1.0, the `modelIdentification/version` of [`Implementation/Library/NFL/Code/NavySim.xml`](../../../../Implementation/Library/NFL/Code/NavySim.xml) |
| **Standard** | IEEE 1516-2025 |
| **Suite release** | NavySim 2026.1 (in development) |
| **Originally developed by** | Okan TOPÇU (otopcu@gmail.com) |

The federation object model of NavySim has been delivered in two forms. Up to NavySim 6.0 it was an HLA 1.3 **FED** file (`nstmss.fed`); since the move to .NET 10 and Fora it is an IEEE 1516 **FDD** (FOM Document Data), `NavySim.xml`, shipped by NFL. The FDD is a part of the suite with its own version, raised as described in [FOM Version](../../Architecture/01.1-VersionControl.md#114-fom-version).

The base contract editing source is the SimGe `nstmss` project (`NavySim.fap` / `Fom/NavySimOM.fom`). `NavySim`, `MekoFdSom`, `EnviFdSom` and the new `ExMFdSom` are the four source modules; their source and imported version is 5.1.0. The deployed/imported contract comparison is documented in [FOM source and deployed contract](../Fom.md#source-and-deployed-contract).

## 5.1.0 — initial scenario heading

- Adds optional `Communication.TaskOrd.InitialHeading`, type Float / HLAfloat32BE: true degrees clockwise from north, [0,360). ExMFd sends authored grid heading plus grid-north offset. This is pre-Begin placement, not autopilot or a speed/engine order. Omission preserves heading; assignments after Begin cannot reorient a running ship.

### Generated application synchronization

- Full user-generated SimGe 0.5.4 export `SourceCode/20261018211031` is deployed to MEKO, EnviFd and ExMFd: 48 generated C# files, API guides and per-application SHA-256 provenance; 40 manual C# files preserved. It supersedes the earlier baseline plus incremental InitialHeading generation.
- The FDD remains **5.1.0**. Wire/type layouts, sharing, dimensions and ordered records agree with the existing 5.1.0 contract. Totals are 8 object classes, 13 interaction classes, 45 declared attributes, 35 declared parameters and 56 types.
- Four runtime source Fom copies and three application Release output copies match the exported module. All six exported XML documents pass FDD/DIF schema validation. Snapshot SHA-256: `8FB6AD20774EA6C245267E815919238F8FF3E2A50390CC52011ACC8812020DB8`.
- Three applications build with zero errors; focused MEKO heading/injection regressions, 63 NFL, 43 EnviFd, 28 ExMFd offline checks and 12 live RTI groups pass, including OSE tactical traffic with and without optional EnviFd. [Import and runtime validation](../../../../Implementation/Library/NFL/SimGeSync/20261018211031/validation.json).

## 5.0.0 — typed injection and coordinated application import

- Replaces generic InjectionMessage EventType/Parameter1/Parameter2 with ManOverboard, EngineFailure, RudderFailure and RadioFailure children, plus common EventId/TargetObjectId/Description.
- Adds ShipSideEnum, EngineGroupEnum, RadioChannelEnum and positive finite DurationSecondsFloat64; removes EmergencyEventEnum. Source totals: 13 interaction classes, 45 attributes, 34 parameters and 56 type/basic definitions.
- Adds ExMFdSom with native repository/FAM links. MEKO receives concrete events on one shared HF region; ExMFd publishes/subscribes to those events. Dimensions are inherited without repetition on the injection branch.
- ExMFd retains MOB side, per-event correlation, target and finite seconds. AAR distinguishes local Sent records from Received callbacks; collection respects the SOM HF/UHF regions. [Runtime evidence](../../../../Implementation/Library/NFL/SimGeSync/20261018040130/runtime-validation.json).

[Detailed contract and handoff](../TypedEventInjection.md) · [NETN/RPR roadmap](../Roadmap.md).

## Scenario execution mapping

ExMFd uses Scenario, TaskOrd (including initial-heading placement), BeginToPlay and Environment plus the four typed InjectionMessage children in FDD 5.1.0. No supplemental NavyScenario module is joined. Course/speed remain under OOW control; the FOM provides no application acknowledgement. [Mapping and evidence semantics](../ScenarioExecution.md).

## FDD history (IEEE 1516)

| Version | Date | Standard | Changes |
|---|---|---|---|
| 5.1.0 | 2026-10-18 | IEEE 1516-2025 | Optional pre-Begin TaskOrd.InitialHeading; full 20261018211031 application import, source/SOM/runtime synchronization and live RTI acceptance. |
| 5.0.0 | 2026-10-18 | IEEE 1516-2025 | Typed injection children and ExMFdSom; coordinated 20261018040130 import into NFL/MEKO/EnviFd/ExMFd. 13 interaction classes, 45 attributes, 34 parameters, 56 types. |
| 4.0.0 | 2026-10-17 | IEEE 1516-2025 | Expands SeaStateEnum to SS0–SS9 and types WeatherReport.SeaState with it; removes 24 Wave1…Wave4 Environment attributes. Active model: 45 attributes, 29 parameters and 53 type/basic definitions; Meko subscribes to 11 Environment fields, Envi publishes 15. |
| 3.1.1 | 2026-10-11 | IEEE 1516-2025 | `Int32` and `UInt32` simple data types added (`HLAinteger32BE`, `HLAunsignedInteger32BE`); eleven member references use them. Four-byte wire layouts and enum representations are unchanged. 53 data type definitions. Shipped with NFL 3.1.1; unchanged in NFL 3.1.2. |
| 3.1.0 | 2026-10-11 | IEEE 1516-2025 | All 69 attributes and 29 parameters have explicit types: four Environment GIS fields, seven Helicopter attributes and federation location text completed from archived producer and consumer code (see [FOM](../Fom.md#completed-legacy-fields-and-source-evidence)). Shipped with NFL 3.1.0. |
| 0.4.8 | 2026-09-17 | IEEE 1516-2025 | Migrated from the legacy HLA 1.3 `nstmss.fed` used by MekoFd. Shared creation FDD of NFL 3.0.0 (.NET 10 / Fora); class and member names and data layouts come from the modern MekoFd. `HLAinteractionRoot` is HLAreliable / TimeStamp, as the Fora server's standard MIM requires. |
| v1.3 | 2013-12-02 | IEEE 1516-2010 | `NavySim.xml` of the .NET Framework NFL (RACoN), created with SimGe. |

## FED history (HLA 1.3)

FED files are kept under `Documentation/Archieve/FED/`.

| Version | Date | Changes |
|---|---|---|
| 2.0.7 | — | *(no entries recorded)* |
| 2.0.6 | 04.04.2008 | Wave attributes and cloud density attribute added to the Environment object class (integration with Canku's thesis). Compatible with Portico 0.8. Compatible with DMSO RTI 1.3 NGv6. |
| 2.0.5 | 02.04.2008 | Compatible with Portico 0.8. Not tested with DMSO RTI 1.3 NGv6. |
| 2.0.4 | 24.03.2006 | Main release for NSTMSS 5.0. `ScenarioFileName` attribute deleted. |
| 2.0.3 | 18.09.2005 | `DLLCLat` and `DLLCLong` attributes added to the Environment class. |
| — | 21.08.2005 | `ScenarioBeginTime` attribute added. Weather Report interaction enhanced. Event Injection interaction class enhanced. TaskOrd interaction class enhanced. Scenario class added. `STG_Scenario` class removed. |
| — | 04.09.2004 | Main release for NSTMSS 4.1. Sea State attribute added to the Environment object class. LLC and URC attributes removed. Helicopter object class added. |
| 2.0.2 | 06.10.2003 | Main release for NSTMSS 4.0. |
| 2.0.1 | 30.10.2002 | Main release for NSTMSS 3.0. |
| — | 18.09.2002 | Position and Heading attributes combined into Posture. |
| — | 19.08.2001 | Working with NSTMSS 2 (which includes Hasan's thesis). |
| 2.0 | 04.05.2000 | Developed for NSTMSS 1.1 (KnoxFd 4.4, OTCFd 3.1, EnviFd 1.1). |
| 1.1 | — | — |

> Note: Rows marked “—” have no version number in the source document.

---

*Copyright © 1999–2026 Okan Topçu.*

*Modification DTG: 2026-10-18 (UTC+03:00)*
