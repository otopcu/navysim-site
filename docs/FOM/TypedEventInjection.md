# Typed event injection

**Deployed contract: NavySim 5.1.0.** Typed injection was introduced in 5.0.0 and remains unchanged in the full SimGe 0.5.4 export `SourceCode/20261018211031`, integrated into NFL, MEKO, EnviFd and ExMFd. SimGe source, exported wire layouts and application FOM copies agree. [FDD release notes](FDD/ReleaseNotes.md) · [FOM roadmap](Roadmap.md).

## Hierarchy and responsibility

```text
HLAinteractionRoot.Communication.InjectionMessage
├── ManOverboard
├── EngineFailure
├── RudderFailure
└── RadioFailure
```

Send concrete children. `InjectionMessage` is an inheritance container with `Neither` sharing in the source FOM/SOMs. The former `EventType`, `Parameter1`, `Parameter2` and `EmergencyEventEnum` are removed. This is a breaking wire-contract change, requiring coordinated export/import and application changes.

Events change the addressed ship's simulated situation. They do not prescribe an automatic manoeuvre or transfer ownership of its clock, heading, speed, engines or rudder to ExMFd.

## Common parameters

The existing Communication headers `Fm`, `To`, `Cc`, `Subject` and `TimeStamp` remain inherited with their existing types. Header `TimeStamp` is UTC DateTime; it is separate from the optional HLA logical timestamp used by a send service.

| Parameter declared on InjectionMessage | Type | Meaning |
|---|---|---|
| EventId | HLAunicodeString | Required canonical UUID text; preserve across scenario execution, dispatch and AAR for correlation |
| TargetObjectId | UInt32 | Required nonzero RTI object-instance handle of the ship in the current federation execution |
| Description | HLAunicodeString | Operator-facing explanation; may be empty |

`TargetObjectId` is authoritative. It uses the same object-instance namespace as the default TaskOrd.FederateId mapping, not an owner federate handle. The dispatcher must resolve a persistent scenario vessel UUID to a currently discovered ship instance. Handles must be resolved again after a new federation execution; human-readable To/Cc headers do not substitute for that resolution.

UUID text uses the `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx` format. It is an application correlation field, not the NETN fixed 16-byte UUID wire type. EventId does not introduce acknowledgement, retries, deduplication or exactly-once execution by itself.

## Child parameters and encodings

| Child | Own parameters | Valid values |
|---|---|---|
| ManOverboard | Side: ShipSideEnum | Port=0, Starboard=1; relative to the target ship facing the bow |
| EngineFailure | EngineGroup: EngineGroupEnum; DurationSeconds: DurationSecondsFloat64 | Port=0, Starboard=1, Both=2; machinery groups, not individual diesels |
| RudderFailure | DurationSeconds: DurationSecondsFloat64 | Target ship rudder-control failure |
| RadioFailure | RadioChannel: RadioChannelEnum; DurationSeconds: DurationSecondsFloat64 | HF=0, UHF=1, Both=2 |

The three enums use HLAinteger32BE. DurationSecondsFloat64 uses HLAfloat64BE, units seconds: a finite value strictly greater than zero. Zero, negative values, NaN and infinity are invalid; no implicit infinite duration exists. Recovery uses the receiving ship's local timer from event application. Pausing, stopping or disconnecting ExMFd does not implicitly freeze or clear a ship failure.

Normal HLAunicodeString encoding applies to text and UInt32 uses HLAunsignedInteger32BE. Existing non-injection record layouts and enum values remain unchanged.

## HF routing and inheritance

All injection children inherit `FrequencySpectrum` from Communication through InjectionMessage. Neither InjectionMessage nor its children redeclare the dimension. One named HF region `[3,30)` is reused by all four bindings in each application's behavior model; no separate physical HF region per child is required.

An ancestor subscription covers descendant traffic, but receives it at the nearest subscribed superclass and only with parameters available there. Thus a subscription only to InjectionMessage would lose child identity and `Side`, `EngineGroup`, `RadioChannel` and `DurationSeconds`. To receive the complete typed payload, subscribe to the four concrete children. This follows the checked Fora implementation of IEEE 1516.1 sections 5.10/6.1.7 (`CandidateReceivedClass` and `ParametersAt`), also covered by its existing `AnInteraction_IsReceivedAtTheSubscribedSuperclass_WithItsParametersOnly` test. The test was inspected, not rerun as part of this source edit.

| Application | InjectionMessage base | Each concrete child | Region |
|---|---|---|---|
| MekoFdSom | Neither | Subscribe | Shared HF |
| ExMFdSom | Neither | PublishSubscribe | Shared HF |
| EnviFdSom | Neither | Neither | No injection binding |

ExMFd publishes scenario/manual injections and subscribes for collection of injections from other participants. Its own sends must be recorded locally for AAR; an RTI subscription does not provide a self-echo guarantee. RTI send acceptance remains distinct from application execution.

## ExMFdSom

The new standalone SOM contains the same complete class/type tree as NavySim, with application-specific sharing. It is registered in NavySimOM.fom and linked to the existing ExMFd application and behavior identity in NavySim.sfam.

| Scope | ExMFd source sharing | Routing |
|---|---|---|
| Scenario, Environment | Publish | Object updates |
| Frigate.Meko, Frigate.Knox | Subscribe | Discovery/telemetry; inherited four Frigate fields |
| BeginToPlay | Publish | Default/global region |
| TaskOrd | PublishSubscribe | HF |
| Four typed injection children | PublishSubscribe | HF |
| FormationMessage | Subscribe | UHF |
| ShipStatusReport, WeatherReport | Subscribe | HF |
| Other classes | Neither | No direct binding |

These source roles are implemented by the imported runtime: MEKO receives typed children, Envi retains its Environment/report role, and ExMFd sends and collects the concrete events. ExMFd uses generated DTOs, SOM handles and encoders with its application-owned NFL/Fora lifecycle; MEKO and Envi use their generated manager bases. Existing module IDs, ExMFd behavior ID and other FAM application links are preserved.

## Generation and integration handoff

The current handoff is complete: the full SimGe 0.5.4 export `20261018211031` is imported for all three applications. All 48 generated C# sources are replaced with namespace isolation only; 40 application-owned C# files are retained. Per-application provenance records this export and its source/import hashes. This replaces the former baseline plus incremental InitialHeading generated set without changing the existing 5.1.0 wire contract. NFL descriptors/codecs and MEKO controller hooks now use the typed children. No generic EventType/Parameter1/Parameter2 runtime fallback remains.

Sen authors scheduled ManOverboard in the additive NavySim supplement 1.1.0; ExMFd also offers instant runtime injection. Both explicitly select Port or Starboard and preserve side, description and event UUID through dispatch and AAR. Their type-aware dropdowns share the same allowed choices. Man-overboard creates a received report, not a physical person, recovery objective or automatic manoeuvre. Existing profile 1.0.0 packages remain supported; this adds no FDD parameters or wire-version change.

ExMFd records successful local sends as **Sent**, independently of any RTI echo. Remote callbacks are **Received** and retain child-specific fields through recursive parameter resolution. The collector uses SOM HF/UHF subscriptions; it adds no global Communication or InjectionMessage-base subscription. EventId is visible in AAR but does not establish application acknowledgement/deduplication.

Verification passed: six FDD/DIF XML schemas and wire/type projections; all generated import hashes; seven identical source/Release Fom snapshots; focused MEKO initial-heading, targeting, enum, duration and expiry regressions; **63 NFL**, **43 EnviFd**, **28 ExMFd offline** checks; and **12 real-RTI groups**, with and without optional EnviFd. Live groups cover all four event kinds, engine/radio selections, ship-local expiry while the manager is paused, local AAR and remote collection. OSE tactical traffic includes all eight concrete message types. Three Release application builds have zero errors. [Current evidence](../../../Implementation/Library/NFL/SimGeSync/20261018211031/validation.json). Earlier [5.0.0 import/WPF evidence](../../../Implementation/Library/NFL/SimGeSync/20261018040130/runtime-validation.json) remains historical; it is not the deployed generated baseline.

For future regeneration, use the matching application import tool and Verify mode, preserve application scaffolds, coordinate all affected FDDs and repeat the relevant acceptance checks. Old generic-injection peers are not wire-compatible with this revision.
