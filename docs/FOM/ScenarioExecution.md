# Scenario distribution and event mapping

ExMFd uses **NavySim FDD 5.1.0**, from the full SimGe 0.5.4 export `SourceCode/20261018211031`, including TaskOrd.InitialHeading. C2SIM is the saved format; execution uses native NavySim classes without a supplemental NavyScenario module.

| Function | FOM element | Mapping |
|---|---|---|
| General information | Scenario OC | ScenarioTitle, ScenarioVersion, ScenarioDescription, ScenarioStartTime, DLLCLat, DLLCLong, ReportInterval. Origin derives from the first vessel; reporting defaults to one minute. |
| Ship assignment | HF Communication.TaskOrd | FederateId targets the discovered object-instance handle. ShipName, HullNo, CallSign, Nation, Latitude, Longitude assign identity/initial position; optional InitialHeading supplies true degrees clockwise from north (Float / HLAfloat32BE). |
| Begin | BeginToPlay | One broadcast on Run. |
| Weather | Environment OC | SeaState enum, WindSpeed in knots, WindDirection true FROM degrees. |
| Man overboard | HF InjectionMessage.ManOverboard | EventId, TargetObjectId, Description; Side enum Port/Starboard; inherited headers. |
| Engine failure | HF InjectionMessage.EngineFailure | Common fields; EngineGroup Port/Starboard/Both and positive finite DurationSeconds. |
| Rudder failure | HF InjectionMessage.RudderFailure | Common fields and positive finite DurationSeconds. |
| Radio failure | HF InjectionMessage.RadioFailure | Common fields; RadioChannel HF/UHF/Both and positive finite DurationSeconds. |
| Observation | HF Communication.ShipStatusReport | Position, Course, Velocity in knots and message timestamp. |

**Initial true heading is placement, not a course-control order.** ExMFd sends grid heading plus grid-north offset, normalized to [0,360). Position and heading apply only before Begin, regardless of callback order. Explicit 000 is valid; omission retains orientation. The receiver updates solver yaw as well as posture and disables course control, while preserving speed, shaft state, EOT and manual rudder. After Begin, assignments cannot change position/heading. Authored speed is reference only. Updated peers require FDD 5.1.0 in a newly created federation; the contract of an existing 5.0.0 federation is not upgraded by changing a local file.

## Injection parameters

[Full typed contract](TypedEventInjection.md). The base InjectionMessage is an inheritance container, with no direct send/subscription. Concrete child subscriptions retain child identity and parameters. All four reuse one HF region and inherit FrequencySpectrum without redeclaration.

EventId is canonical UUID text; TargetObjectId is the current ship object-instance handle, resolved from scenario allocation and discovery. To/Cc are display headers, not authoritative fault targeting. Duration is HLAfloat64BE in seconds; no decimal-minute conversion or Parameter1/Parameter2 fallback remains. Enum values and finite positive durations are validated before changing ship state.

The ship expires failures locally. Manager recovery rows mean expected expiry only; there is no recovery interaction. Scheduled and instant MOB have an explicit Port/Starboard selection and a description. They produce a report, not a physical person, objective or manoeuvre. Predefined packages cover weather/failures and, with NavySim supplement 1.1.0, ManOverboard. The 1.0.0 package contract remains supported.

## Clock and evidence

ExMFd owns its event schedule. Quiet intervals and Pause/Resume/Stop/Disconnect send no clock or execution-status commands. Ships retain their clocks, physics and OOW. Initial UTC is configuration.

The FOM has an EventId correlation field but no application receipt or event-ID deduplication. ExMFd records **RTI accepted**, not **Applied**. CommandId is carried as EventId for injections; RunId and schedule time remain local journal context. Explicit retry after an uncertain send can duplicate effects.

Local accepted sends enter AAR as Sent; remote callbacks enter as Received. The collector resolves inherited and child fields and respects HF/UHF subscriptions, without adding global parent subscriptions. This evidence does not imply delivery to the target ship.

EnviFd is optional. Weather uses supplied-field semantics; SS resets reference wind and explicit wind in the same patch wins. Multiple controllers have no ownership arbitration.

[Current import and runtime evidence](../../../Implementation/Library/NFL/SimGeSync/20261018211031/validation.json) · [ExMFd architecture](../ExMFd/Architecture.md) · [Manual](../ExMFd/UserManual.md).
