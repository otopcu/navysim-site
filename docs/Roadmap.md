# NavySim Roadmap

> Historical backlog source: *NavySim Development Plan.docx*. The active C2SIM scenario migration plan below was agreed on 17 October 2026. Delivered features are tracked in the [Release Notes](ReleaseNotes.md).

**Legend:** **TP** = Term Project · **MS** = MS Thesis

## Contents

- [C2SIM scenario infrastructure](#c2sim-scenario-infrastructure)
- [Shared geography and Boston](#shared-geography-and-boston)
- [FOM evolution](#fom-evolution)
- [Scheduled milestones](#scheduled-milestones)
- [Backlog](#backlog)
- [To do by part](#to-do-by-part)
- [Notes](#notes)

## C2SIM scenario infrastructure

**Decision (2026-10-17):** Replace the active NSDL scenario path with C2SIM-based scenario packages authored by **Sen** and executed by **ExMFd**. Keep NavyFOM/Fora as the federation interface. This is a staged migration; schema validation alone does not establish live federation interoperability or complete C2SIM conformance.

### Baseline and ownership

- Pin the published Core + SMX + LOX composite schema **1.0.1**, its source and SHA-256. Preserve the upstream XSD unchanged. Do not silently substitute CWIX trial schemas or confuse editor/server releases with the standard version.
- Use C2SIM for vessel identity, initial state, scenario time and system/entity allocation where supported.
- Use a separately versioned, schema-validated **NavySim supplement**, referenced through C2SIM `InitializationDataFile`, for local environment and execution semantics absent from the baseline. This is application-specific supplemental data, not an already standardized maritime extension.
- Document coordinates, heading reference, units, wind conventions, time origin, identity mapping and unsupported content. Introduce an ontology-based C2SIM extension if interchange requirements later justify one.
- Put reusable parsing, validation and scenario models in a UI/RTI-independent shared library used by Sen and ExMFd. Keep federation transport in an adapter.
- Follow GSD for scenario objectives, initial conditions, course of events and termination criteria. GSD is guidance, not an executable file format.

### Delivery stages and acceptance gates

All six stages are delivered for **NavySim scenario profile 1.0.0**. This does not include later map/route/condition authoring or full C2SIM conformance.

| Stage | Delivered result | Acceptance | Status |
|---|---|---|---|
| 1. Contract and sample | Unchanged pinned C2SIM 1.0.1 XSD, supplemental schema, 37-field NSDL inventory and two-MEKO package | XSD, semantic, units, references and unsupported-content checks | Complete |
| 2. Shared library | Immutable package parser, editable draft, validated save and source/field diagnostics | 55 package/timeline groups plus Sen/coordinator round trips and invalid-input safety | Complete |
| 3. End-to-end slice | Two MEKO applications over real Fora with and without EnviFd, native assignment/weather/failure | Eight native-FOM groups verify received state, OOW preservation, local expiry, telemetry and independent Stop/Disconnect | Complete |
| 4. ExMFd | .NET 10 runtime/WPF, discovered object allocation, native FOM mapping and local event clock | Separate distribution/run, RTI dispatch evidence, six workspaces and AAR; no application receipt/deduplication claim | Complete |
| 5. Sen | Editable metadata/time/weather, ship state/allocation and event grids; validation/open/save/XML preview | Eight Sen checks including author/save/reopen without XML editing and WPF rendering | Complete |
| 6. Cutover/docs | Active NSDL/DataSet paths archived, modern builds/publish, manuals/architecture/releases updated | Reproducible acceptance manifest and retained historical sources | Complete |

### First executable scenario

1. Two surface vessels with UUIDs, explicit system allocation, starting geodetic positions, heading reference and speed in m/s retained as source values; runtime assignment applies position only and OOW controls manoeuvring.
2. Initial sea state and wind. Applying sea state sets the preset wind; an explicit wind speed in the same update wins. A later sea-state update resets it again unless explicitly overridden.
3. A wind change at a defined elapsed simulation time.
4. A finite port-engine failure addressed by vessel UUID, followed by recovery.
5. A defined scenario end time and observable completion state.

The accepted live sample uses two MEKO200 participants. A parsed Knox representation is not proof of live Knox own-ship capability.

### Validation and progress rules

- Check schema integrity, XSD validity, semantic validity, supported feature coverage and runtime capability separately.
- Exercise load/save round trips, invalid inputs, duplicate references, boundary values and deterministic timing with focused offline tests.
- Test sea-state/wind precedence explicitly. Do not introduce a second sea-state preset table into the scenario library.
- Do not use wall-clock sleeps to test event scheduling. Test an injected/controlled simulation clock.
- Verify current NavyFOM limitations before promising initial course/speed transfer, pause/resume or application acknowledgments; extend contracts deliberately where needed.
- Reject unsupported execution semantics instead of silently dropping them. Keep parsed metadata distinct from implemented runtime behavior.
- Update stage status with evidence as work lands. A validated package does not mean Sen authoring or ExMFd integration has shipped.

### Implementation evidence (2026-10-18)

- [Complete acceptance manifest](../../Implementation/Library/Scenarios/Validation/c2sim-migration-20261018.json): build, package/timeline, Sen, coordinator, existing-domain and real-RTI evidence. Live tests use actual application models/adapters headlessly; WPF editors are rendered separately.
- [Shared contract and APIs](../../Implementation/Library/Scenarios/README.md), [two-MEKO package](../../Implementation/Library/Scenarios/Samples/two-meko-training/initialization.xml), [reproducible validation script](../../Implementation/Library/Scenarios/Code/tools/Validate-Scenarios.ps1).
- [Sen architecture/manual](Sen/Architecture.md), [ExMFd architecture/manual](ExMFd/Architecture.md), [Native NavySim execution mapping](FOM/ScenarioExecution.md).
- Common layout is **FdApps / Library / Tools**; suite projects resolve. Helpers/Shared common sources now live under Library. MEKO/Knox-specific modules stay with their applications.
- Coordinated source/runtime FDD is 5.0.0 after the user-generated 20261018040130 import; typed injection has passed live acceptance. Execution uses existing Scenario/TaskOrd/BeginToPlay/Environment/InjectionMessage elements. The custom channel is archived. RTI acceptance does not confirm application; no exactly-once or receipt guarantee is inferred.
- Future scope: map/routes, conditions/objectives, terrain/organization, richer weather and additional own-ship types. Durable crash recovery and HLA logical-time management are separate designs. No full C2SIM certification is claimed.

### References

- [C2SIM standard, SISO-STD-019-2020](https://cdn.ymaws.com/www.sisostandards.org/resource/resmgr/standards_products/siso-std-019-2020_c2sim.pdf)
- [C2SIM implementation guide, SISO-GUIDE-010-2020](https://cdn.ymaws.com/www.sisostandards.org/resource/resmgr/guidance_products_/siso-guide-010-2020_c2sim.pdf)
- [GSD, SISO-GUIDE-006-2018](https://cdn.ymaws.com/www.sisostandards.org/resource/resmgr/guidance_products_/siso-guide-006-2018_gsd.pdf)
- [Published C2SIM 1.0.1 artifacts](https://github.com/OpenC2SIM/C2SIMArtifacts/releases/tag/v1.0.1)
- [OpenC2SIM schemas and implementation tools](https://github.com/OpenC2SIM/OpenC2SIM.github.io)

## Shared geography and Boston

**18 October 2026:** The Library/Geography foundation and real Sen map placement are delivered using NOAA ENC plus OSM/OpenSeaMap. Boston Harbor is now the Sen and MekoFd default; the measured NOAA CUDEM land/seabed package and common geographic frame are integrated and GPU-checked. [Architecture and source assessment](Architecture/Geography.md).

Boston harbor LOD1 building/pier footprints and the shared inner-harbor map overlay are delivered; source/height estimates and offline rebuild evidence are retained.

Next: refine near-shore detail/LOD and authored harbor appearance, spatial/tidal water references and measured grounding behavior; integrate TacPic contact/symbology overlays and Meko ENC navigation frames. The initial Boston terrain/frame switch is validated; detailed facades, harbor engineering structures and collision/grounding remain separate work. O-charts Türkiye is a deferred licensed option, not a required dependency or a plain S-57 source.

## FOM evolution

[FOM roadmap](FOM/Roadmap.md): typed NavySim 5.0.0 injection and ExMFdSom are imported from user export 20261018040130 and live-tested. Separately evaluate NETN-SMC/BASE for entity-addressed actions, capabilities and responses, and RPR for vessel/entity, damage and propulsion state. Exact distributions, dependency subsets, identity/units mapping and interoperability tests precede adoption. NETN/RPR are deferred; current runtime uses FDD 5.0.0.

## Scheduled milestones

| Time frame | Items |
|---|---|
| May 2008 | NSTMSS Foundation Library (NFL) (a.k.a. NSTMSS Components) · Re-architecting EnviFd · Adapting ExPFd to use the NFL |
| Sep 2008 | Integration of Canku's thesis: wave models, wave shading simulation, ship wakes, simple cloud simulation, 4-DOF hydrodynamic model, controlling the waves using EnviFd |
| Nov 2008 | GPL license updated to GNU GPL v3 |
| Aug 2011 | Generic RTI-layer implementation (RACoN) · Integrating RACoN into ExPFd — new name: **ExCFd** |
| Sep 2011 | Re-architecting EnviFd |
| Oct 2026 | NavySim under a local Git repository · suite solution `Implementation/NavySim.slnx` · calendar versions for the suite (first: **2026.1**), SemVer per part in `Version.props` — see [Version Control](Architecture/01.1-VersionControl.md) |

## Backlog

Items without a time frame in the development plan, grouped by theme. The order within each group follows the source document.

### Scenario and object model

- Extend the delivered [C2SIM profile](#c2sim-scenario-infrastructure) with map/routes, conditional objectives and further platform/environment semantics when required.
- Evaluate NETN and RPR module subsets and explicit NavySim mappings through the [FOM roadmap](FOM/Roadmap.md).
- IEEE compatibility

### RTI layer (RACoN)

- Integrating RACoN into FedMonFd

### Graphics and virtual environment

- Renewing the graphical infrastructure of the virtual ship — transition from OpenGL Performer to one of: (1) XNA Game Studio, (2) Delta3D, (3) NVIDIA SceniX, (4) OpenSceneGraph
- Environmental and atmospheric effects integrated with ship hydrodynamics (simulation + graphics):
  - Time-of-day sky dome: sun and moon positions and appearance changing over time, lighting of the virtual environment, sky dome shaped by cloud cover (cloudy/clear weather, cloud and sun movement)
  - Atmospheric effects: rain, snow, layered fog, wind effect (fog is already implemented; wind can be shown graphically, e.g. a waving flag)
- Sea state + water depth + bow bubbles + realistic sea surface (simulation + graphics)
- (TP) Lights — running lights, man-overboard lights, etc.
- Adding Turkish motifs to NSTMSS
- 3D Model Distributor Federate (MDFd) for unknown object geometry

### Ship models and hydrodynamics

- (TP) Adapting MİLGEM to NSTMSS
  - Creating the 3D model
  - Adapting the federate coordinate system
  - Adapting the hydrodynamics model
- 6-DOF hydrodynamic model (Sinan's thesis)
- Advanced collision detection and collision response, with ship deformation after collision (simulation + VR + graphics)

### Sensors, C2 and weapons

- (TP) Classical generic navigation radar — could be a separate federate
- Air radar modeling
- (TP) TacPicFd implementation (simulation + C2)
- Fire control system — firing, CIC simulation (simulation + C2)

### Communication

- TMS improvements: flexible interface, multiple *to* and *cc* addressing, address grouping, DDM regions
  - (MS) Tactical voice message interface — voice over HLA (simulation + network, simulation + C2)
- Semi-formatted FormMsg implementation (simulation + C2)
- (TP) Navigation sound communication system — 3D external sound system; whistle communication among ships using 3D sound
- Visual communication system among virtual ships in a naval virtual environment:
  - Flag communication: (1) automatic flag hoisting — the user enters the message as text and the ship hoists the flags; (2) manual flag hoisting — a flag locker is shown and the user selects and hoists the flags (possibly a separate federate)
  - Semaphore communication
  - (TP) Flashing light (signal lamp) communication

### User interaction and training

- (TP) Voice commands for ship control
- (TP) 3D virtual officer — voice reports (later also shown on a status display)
- Overhaul of the user interface, e.g. 3D control panels (simulation + VR)
- (TP) Animated man overboard
  - A real figure falls into the sea
  - The person in the water is animated (e.g. waving)
  - The ship's radar takes a fix on the man overboard; a signal flare (rocket) is fired
- Development of an after-action review tool (simulation + C2)
- (MS) Intelligent agents in the virtual environment (simulation + AI)

### Engineering and deployment

- 64-bit programming
- Obfuscation — protect executables against reverse engineering
- Support for non-admin users: store settings under `HKEY_CURRENT_USER/Software/NSTMSS/MekoFd/…`
- Microsoft Application Verifier


---

*Updated: 2026-10-18 (Europe/Istanbul)*
