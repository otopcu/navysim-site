# NavySim FOM

This page documents the base contract from the active SimGe project `C:/Users/okant/OneDrive/Documents/Simulation Projects/nstmss`, selected by `NavySim.fap` → `Fom/NavySimOM.fom`. The current XML modules are `Fom/NavySim.xml`, `Fom/MekoFdSom.xml`, `Fom/EnviFdSom.xml` and `Fom/ExMFdSom.xml`; `.sfom` files hold their module identities. Behavior/DDM policy is in `Behavior/*.sfbm`, and application-to-module links are in `Fam/NavySim.sfam`.

The tables below are derived from those XML modules, not from old prose inventories or archived FED files. The current definitions contain **8 object classes, 13 interaction classes, 45 declared attributes, 35 declared parameters and 56 data-type definitions**. Inherited members are counted once at their declaring class.

## Fom Version

[FDD Release Notes](FDD/ReleaseNotes.md).

## Source and deployed contract

The source and coordinated NFL, MEKO, EnviFd and ExMFd runtime contracts are **5.1.0**. The current full import is the user-generated SimGe 0.5.4 export `nstmss/SourceCode/20261018211031`, including optional TaskOrd.InitialHeading and the four typed injection children. This export replaces the earlier baseline plus incremental heading generation. Its wire/type layout agrees with the previously deployed 5.1.0 contract; generation timestamps and declaration ordering do not create another FDD version. [Import manifest](../../../Implementation/Library/NFL/SimGeSync/20261018211031/import.json) · [Validation](../../../Implementation/Library/NFL/SimGeSync/20261018211031/validation.json).

| Module | Type | Module ID | Source / imported version |
|---|---|---|---|
| NavySim | FOM | 3a973572-0775-4c28-a6a0-c6dbbf871bcb | 5.1.0 |
| MekoFdSom | SOM | a8997201-6e51-4d74-a753-ce8e16f21589 | 5.1.0 |
| EnviFdSom | SOM | 18c1f043-3f7c-44ac-a1a7-2eaf58609135 | 5.1.0 |
| ExMFdSom | SOM | 860e990a-c3a2-4877-964f-620e91ee1a7b | 5.1.0 |

Existing module and behavior identities are preserved; the new ExMFdSom identity is linked from the native repository/FAM.

### Generated export and application imports

| Application | Imported generated C# files | Application-owned C# files retained | Namespace isolation |
|---|---|---|---|
| MekoFd | 17 | 18 | NavySim.MekoGenerated |
| EnviFd | 14 | 9 | NavySim.EnviGenerated |
| ExMFd | 17 | 13 | NavySim.ExmGenerated |

All **48** generated C# files and the three generated API guides come from `20261018211031`. Namespace isolation is the only C# import transformation. The **40** retained manual C# files include application-owned federates, managers, entity extensions and runtime adapters; they are not counted as generated scaffolds. Each application's `Generated/provenance.json` records source/import hashes and preserved manual-source hashes. There is no mixed baseline/incremental generated set in the current import. Envi's SOM omits injection DTOs because it neither publishes nor subscribes to injection events; its complete FDD still carries the shared hierarchy.

All six exported XML documents pass their matching IEEE 1516-2025 FDD/DIF schemas and agree with the previous deployed wire/type layout. The three root creation FDDs are byte-identical to one another; the three `Fom/NavySim.xml` source modules are byte-identical to one another. Runtime source copies in NFL, MEKO, EnviFd and ExMFd, and all three application Release output copies, match the exported Fom snapshot. ExMFd's build uses the central NFL copy. Root creation FDD versus Fom snapshot byte equality is not claimed because metadata/ordering differ.

The deployed Fom snapshot SHA-256 is `8FB6AD20774EA6C245267E815919238F8FF3E2A50390CC52011ACC8812020DB8`.

All three applications build in Release with zero errors. Focused MEKO initial-heading and typed-injection tests, **63 NFL**, **43 EnviFd**, **28 ExMFd offline** checks and **12 live RTI acceptance groups** passed. Live coverage includes two MEKO adapters with ExMFd, both with and without optional EnviFd, all four typed events, local recovery, independent ship clocks, and OSE tactical traffic covering eight concrete message types. These are application-model/adapter live tests; interactive bridge, Debug outputs and published-installation validation are outside this evidence. Existing build warnings remain. [Current runtime evidence](../../../Implementation/Library/NFL/SimGeSync/20261018211031/validation.json).

## Scenario execution mapping

[Scenario execution](ScenarioExecution.md) documents the deployed native Scenario/TaskOrd/BeginToPlay/Environment/typed-injection mapping. No additional NavySim.Scenario module is used. Version 5.0.0 changes the injection branch as described below; course/speed remain under OOW control.

## Object class hierarchy

```text
HLAobjectRoot
├── Frigate
│   ├── Meko
│   └── Knox
├── OTC
├── Environment
├── Scenario
└── Helicopter
```

Attributes belong to their declaring class and are inherited. `Meko` and `Knox` inherit the four Frigate fields and the root deletion privilege. A FOM `PublishSubscribe` capability does not establish an application's actual P/S. There is no separate Vessel class in this FDD.

## Attribute table

### HLAobjectRoot

Class sharing: `Neither`.

| Attribute | Data type | Update / condition | Ownership | FOM sharing | Transport / order |
|---|---|---|---|---|---|
| `HLAprivilegeToDeleteObject` | `HLAtoken` | Static / NA | DivestAcquire | PublishSubscribe | HLAreliable / TimeStamp |

### HLAobjectRoot.Frigate

Class sharing: `PublishSubscribe`.

| Attribute | Data type | Update / condition | Ownership | FOM sharing | Transport / order |
|---|---|---|---|---|---|
| `Velocity` | `Float` | Static / NA | NoTransfer | PublishSubscribe | HLAreliable / Receive |
| `Posture` | `PostureType` | Static / NA | NoTransfer | PublishSubscribe | HLAreliable / Receive |
| `Name` | `HLAunicodeString` | Static / NA | NoTransfer | PublishSubscribe | HLAreliable / Receive |
| `Class` | `FrigateClassEnum` | Static / NA | NoTransfer | PublishSubscribe | HLAreliable / Receive |

### HLAobjectRoot.Frigate.Meko

Class sharing: `PublishSubscribe`.

No directly declared attributes; inherited fields retain their parent declarations.

### HLAobjectRoot.Frigate.Knox

Class sharing: `PublishSubscribe`.

No directly declared attributes; inherited fields retain their parent declarations.

### HLAobjectRoot.OTC

Class sharing: `PublishSubscribe`.

| Attribute | Data type | Update / condition | Ownership | FOM sharing | Transport / order |
|---|---|---|---|---|---|
| `OTCRank` | `HLAunicodeString` | Static / NA | NoTransfer | PublishSubscribe | HLAreliable / Receive |
| `OTCName` | `HLAunicodeString` | Static / NA | NoTransfer | PublishSubscribe | HLAreliable / Receive |

### HLAobjectRoot.Environment

Class sharing: `PublishSubscribe`.

| Attribute | Data type | Update / condition | Ownership | FOM sharing | Transport / order |
|---|---|---|---|---|---|
| `Harbor` | `HarborArray` | Static / NA | NoTransfer | PublishSubscribe | HLAbestEffort / Receive |
| `Lighthouse` | `LighthouseArray` | Static / NA | NoTransfer | PublishSubscribe | HLAbestEffort / Receive |
| `GisDbSizes` | `GisDbSizesType` | Static / NA | NoTransfer | PublishSubscribe | HLAreliable / Receive |
| `AnchoringPlace` | `AnchoringPlaceArray` | Static / NA | NoTransfer | PublishSubscribe | HLAbestEffort / Receive |
| `WindSpeed` | `Float` | Conditional / User | NoTransfer | PublishSubscribe | HLAreliable / Receive |
| `WindDirection` | `Float` | Conditional / User | NoTransfer | PublishSubscribe | HLAreliable / Receive |
| `SeaState` | `SeaStateEnum` | Conditional / User | NoTransfer | PublishSubscribe | HLAreliable / Receive |
| `CloudDensity` | `CloudDensityEnum` | Static / NA | NoTransfer | PublishSubscribe | HLAreliable / Receive |
| `FarFogRange` | `Float` | Conditional / User | NoTransfer | PublishSubscribe | HLAreliable / Receive |
| `NearFogRange` | `Float` | Conditional / User | NoTransfer | PublishSubscribe | HLAreliable / Receive |
| `FogType` | `FogTypeEnum` | Conditional / User | NoTransfer | PublishSubscribe | HLAreliable / Receive |
| `TOD` | `Float` | Conditional / User | NoTransfer | PublishSubscribe | HLAreliable / Receive |
| `FileName` | `HLAunicodeString` | Static / NA | NoTransfer | PublishSubscribe | HLAreliable / Receive |
| `DLLCLat` | `ClatLong` | Static / NA | NoTransfer | PublishSubscribe | HLAreliable / Receive |
| `DLLCLong` | `ClatLong` | Static / NA | NoTransfer | PublishSubscribe | HLAreliable / Receive |

### HLAobjectRoot.Scenario

Class sharing: `PublishSubscribe`.

| Attribute | Data type | Update / condition | Ownership | FOM sharing | Transport / order |
|---|---|---|---|---|---|
| `DLLCLong` | `ClatLong` | Static / NA | NoTransfer | PublishSubscribe | HLAreliable / Receive |
| `DLLCLat` | `ClatLong` | Static / NA | NoTransfer | PublishSubscribe | HLAreliable / Receive |
| `TerrainFileName` | `HLAunicodeString` | Static / NA | NoTransfer | PublishSubscribe | HLAreliable / Receive |
| `ScenarioLocation` | `HLAunicodeString` | Static / NA | NoTransfer | PublishSubscribe | HLAreliable / Receive |
| `WeatherReportBroadcastInterval` | `Int32` | Static / NA | NoTransfer | PublishSubscribe | HLAreliable / Receive |
| `ReportInterval` | `Int32` | Static / NA | NoTransfer | PublishSubscribe | HLAreliable / Receive |
| `STGName` | `HLAunicodeString` | Static / NA | NoTransfer | PublishSubscribe | HLAreliable / Receive |
| `OrderDescription` | `HLAunicodeString` | Static / NA | NoTransfer | PublishSubscribe | HLAreliable / Receive |
| `ArrivalLocation` | `HLAunicodeString` | Static / NA | NoTransfer | PublishSubscribe | HLAreliable / Receive |
| `TOA` | `DateTime` | Static / NA | NoTransfer | PublishSubscribe | HLAreliable / Receive |
| `DepartureLocation` | `HLAunicodeString` | Static / NA | NoTransfer | PublishSubscribe | HLAreliable / Receive |
| `TOD` | `DateTime` | Static / NA | NoTransfer | PublishSubscribe | HLAreliable / Receive |
| `ScenarioStartTime` | `DateTime` | Static / NA | NoTransfer | PublishSubscribe | HLAreliable / Receive |
| `ScenarioDescription` | `HLAunicodeString` | Static / NA | NoTransfer | PublishSubscribe | HLAreliable / Receive |
| `ScenarioVersion` | `HLAunicodeString` | Static / NA | NoTransfer | PublishSubscribe | HLAreliable / Receive |
| `ScenarioTitle` | `HLAunicodeString` | Static / NA | NoTransfer | PublishSubscribe | HLAreliable / Receive |

### HLAobjectRoot.Helicopter

Class sharing: `PublishSubscribe`.

| Attribute | Data type | Update / condition | Ownership | FOM sharing | Transport / order |
|---|---|---|---|---|---|
| `Status` | `HelicopterStatusEnum` | Static / NA | NoTransfer | PublishSubscribe | HLAbestEffort / Receive |
| `Quaternion` | `QuaternionRateType` | Static / NA | NoTransfer | PublishSubscribe | HLAbestEffort / Receive |
| `Orientation` | `HelicopterOrientationType` | Static / NA | NoTransfer | PublishSubscribe | HLAbestEffort / Receive |
| `Altitude` | `Double` | Static / NA | NoTransfer | PublishSubscribe | HLAbestEffort / Receive |
| `Speed` | `Double` | Static / NA | NoTransfer | PublishSubscribe | HLAbestEffort / Receive |
| `Position` | `HelicopterPositionType` | Static / NA | NoTransfer | PublishSubscribe | HLAbestEffort / Receive |
| `Name` | `HLAunicodeString` | Static / NA | NoTransfer | PublishSubscribe | HLAbestEffort / Receive |

`Environment` now has **15** declared attributes. Wave1…Wave4 fields are absent. Four GIS/navigation-aid fields remain part of the FOM but are outside Meko's eleven-field Environment subscription.

## Interaction class hierarchy

```text
HLAinteractionRoot
├── BeginToPlay
├── Communication
│   ├── InjectionMessage
│   │   ├── ManOverboard
│   │   ├── EngineFailure
│   │   ├── RudderFailure
│   │   └── RadioFailure
│   ├── TaskOrd
│   ├── WeatherReport
│   ├── FormationMessage
│   └── ShipStatusReport
└── Federation_Location_Message
```

The root uses HLAreliable / TimeStamp. `Communication` contributes five inherited parameters; subscribing to a child does not require a direct Communication-parent subscription.

### HLAinteractionRoot

FOM sharing: `Neither`; transport/order: `HLAreliable` / `TimeStamp`; local dimensions: none locally declared; effective dimensions: none.

No directly declared parameters.

### HLAinteractionRoot.BeginToPlay

FOM sharing: `PublishSubscribe`; transport/order: `HLAreliable` / `TimeStamp`; local dimensions: none locally declared; effective dimensions: none.

No directly declared parameters.

### HLAinteractionRoot.Communication

FOM sharing: `PublishSubscribe`; transport/order: `HLAreliable` / `TimeStamp`; local dimensions: FrequencySpectrum; effective dimensions: FrequencySpectrum.

| Parameter | Data type |
|---|---|
| `TimeStamp` | `DateTime` |
| `Subject` | `HLAunicodeString` |
| `Cc` | `HLAunicodeString` |
| `To` | `HLAunicodeString` |
| `Fm` | `HLAunicodeString` |

### HLAinteractionRoot.Communication.InjectionMessage

FOM sharing: `Neither` (inheritance container); transport/order: `HLAreliable` / `TimeStamp`. FrequencySpectrum is inherited from Communication without a local dimension declaration.

Inherited parameters: `TimeStamp`, `Subject`, `Cc`, `To`, `Fm`.

| Parameter | Data type |
|---|---|
| EventId | HLAunicodeString |
| TargetObjectId | UInt32 |
| Description | HLAunicodeString |

| Concrete child | FOM sharing | Own parameters |
|---|---|---|
| ManOverboard | PublishSubscribe | Side: ShipSideEnum |
| EngineFailure | PublishSubscribe | EngineGroup: EngineGroupEnum; DurationSeconds: DurationSecondsFloat64 |
| RudderFailure | PublishSubscribe | DurationSeconds: DurationSecondsFloat64 |
| RadioFailure | PublishSubscribe | RadioChannel: RadioChannelEnum; DurationSeconds: DurationSecondsFloat64 |

Children inherit common parameters and dimensions. [Targeting, validation, local failure expiry and HF subscription semantics](TypedEventInjection.md). The generic EventType/Parameter1/Parameter2 and EmergencyEventEnum no longer exist in source 5.0.0.

### HLAinteractionRoot.Communication.TaskOrd

FOM sharing: `PublishSubscribe`; transport/order: `HLAreliable` / `TimeStamp`; local dimensions: FrequencySpectrum; effective dimensions: FrequencySpectrum.

Inherited parameters: `TimeStamp`, `Subject`, `Cc`, `To`, `Fm`.

| Parameter | Data type |
|---|---|
| `Nation` | `HLAunicodeString` |
| `Longitude` | `ClatLong` |
| `Latitude` | `ClatLong` |
| `HullNo` | `HLAunicodeString` |
| `CallSign` | `HLAunicodeString` |
| `ShipName` | `HLAunicodeString` |
| `FederateId` | `UInt32` |
| `InitialHeading` | `Float` (HLAfloat32BE) |

InitialHeading is optional true degrees clockwise from north, [0,360), used for placement before Begin only. Explicit 000 is north; omission keeps current orientation. It does not set speed or enable autopilot. [Execution mapping](ScenarioExecution.md).

### HLAinteractionRoot.Communication.WeatherReport

FOM sharing: `PublishSubscribe`; transport/order: `HLAreliable` / `TimeStamp`; local dimensions: none locally declared; effective dimensions: FrequencySpectrum.

Inherited parameters: `TimeStamp`, `Subject`, `Cc`, `To`, `Fm`.

| Parameter | Data type |
|---|---|
| `FreeText` | `HLAunicodeString` |
| `WindSpeed` | `HLAunicodeString` |
| `WindDirection` | `HLAunicodeString` |
| `FogStatus` | `HLAunicodeString` |
| `SeaState` | `SeaStateEnum` |

### HLAinteractionRoot.Communication.FormationMessage

FOM sharing: `PublishSubscribe`; transport/order: `HLAreliable` / `TimeStamp`; local dimensions: FrequencySpectrum; effective dimensions: FrequencySpectrum.

Inherited parameters: `TimeStamp`, `Subject`, `Cc`, `To`, `Fm`.

| Parameter | Data type |
|---|---|
| `BodyLine3` | `HLAunicodeString` |
| `BodyLine2` | `HLAunicodeString` |
| `BodyLine1` | `HLAunicodeString` |

### HLAinteractionRoot.Communication.ShipStatusReport

FOM sharing: `PublishSubscribe`; transport/order: `HLAreliable` / `TimeStamp`; local dimensions: FrequencySpectrum; effective dimensions: FrequencySpectrum.

Inherited parameters: `TimeStamp`, `Subject`, `Cc`, `To`, `Fm`.

| Parameter | Data type |
|---|---|
| `Course` | `Float` |
| `Velocity` | `Float` |
| `Longitude` | `ClatLong` |
| `Latitude` | `ClatLong` |

### HLAinteractionRoot.Federation_Location_Message

FOM sharing: `PublishSubscribe`; transport/order: `HLAreliable` / `TimeStamp`; local dimensions: FrequencySpectrum; effective dimensions: FrequencySpectrum.

| Parameter | Data type |
|---|---|
| `Federation_Location_Name` | `HLAunicodeString` |

WeatherReport.SeaState is **SeaStateEnum**, not text. FogStatus, WindDirection, WindSpeed and FreeText remain formatted Unicode strings; matching Environment names do not imply matching wire types. WeatherReport has no local dimensions element and inherits FrequencySpectrum from Communication; the XML does not repeat that dimension on the child.

## Wire data types

The XML contains 20 basic representations, 11 simple types, 9 enumerations, 8 arrays and 8 fixed records; no variant records. The tables preserve record-field order and enum numeric values. Class/member declaration order has no corresponding field-packing meaning.

### Basic representations

| Name | Size, bits | Endian |
|---|---|---|
| `HLAinteger16BE` | 16 | Big |
| `HLAinteger32BE` | 32 | Big |
| `HLAinteger64BE` | 64 | Big |
| `HLAunsignedInteger16BE` | 16 | Big |
| `HLAunsignedInteger32BE` | 32 | Big |
| `HLAunsignedInteger64BE` | 64 | Big |
| `HLAfloat32BE` | 32 | Big |
| `HLAfloat64BE` | 64 | Big |
| `HLAoctetPairBE` | 16 | Big |
| `HLAinteger16LE` | 16 | Little |
| `HLAinteger32LE` | 32 | Little |
| `HLAinteger64LE` | 64 | Little |
| `HLAunsignedInteger8` | 8 | Little |
| `HLAunsignedInteger16LE` | 16 | Little |
| `HLAunsignedInteger32LE` | 32 | Little |
| `HLAunsignedInteger64LE` | 64 | Little |
| `HLAfloat32LE` | 32 | Little |
| `HLAfloat64LE` | 64 | Little |
| `HLAoctetPairLE` | 16 | Little |
| `HLAoctet` | 8 | Big |

### Simple types

| Name | Representation | Units |
|---|---|---|
| `HLAASCIIchar` | `HLAoctet` | NA |
| `HLAunicodeChar` | `HLAoctetPairBE` | NA |
| `HLAbyte` | `HLAoctet` | NA |
| `HLAinteger64Time` | `HLAinteger64BE` | NA |
| `HLAfloat64Time` | `HLAfloat64BE` | NA |
| `Float` | `HLAfloat32BE` | NA |
| `DateTime` | `HLAinteger64BE` | 100 nanoseconds since 0001-01-01T00:00:00Z |
| `Double` | `HLAfloat64BE` | NA |
| `Int32` | `HLAinteger32BE` | NA |
| `UInt32` | `HLAunsignedInteger32BE` | NA |
| `DurationSecondsFloat64` | `HLAfloat64BE` | s; positive finite duration |

### Enumerations

| Enumeration | Representation | Values |
|---|---|---|
| `HLAboolean` | `HLAinteger32BE` | HLAfalse=0, HLAtrue=1 |
| `FogTypeEnum` | `HLAinteger32BE` | NOFOG=0, LINEAR=1, EXP=2, EXP2=3, SPLINE=4 |
| `SeaStateEnum` | `HLAinteger32BE` | SS0=0, SS1=1, SS2=2, SS3=3, SS4=4, SS5=5, SS6=6, SS7=7, SS8=8, SS9=9 |
| `FrigateClassEnum` | `HLAinteger32BE` | FRIG_KNOX=0, FRIG_MEKO=1 |
| `CloudDensityEnum` | `HLAinteger32BE` | CLOUD0=0, CLOUD1=1, CLOUD2=2, CLOUD3=3 |
| `ShipSideEnum` | `HLAinteger32BE` | Port=0, Starboard=1 |
| `EngineGroupEnum` | `HLAinteger32BE` | Port=0, Starboard=1, Both=2 |
| `RadioChannelEnum` | `HLAinteger32BE` | HF=0, UHF=1, Both=2 |
| `HelicopterStatusEnum` | `HLAinteger32BE` | AIRBORNE=1, ON_DECK=2 |

### Arrays

| Type | Element | Cardinality | Encoding |
|---|---|---|---|
| `HLAASCIIstring` | `HLAASCIIchar` | Dynamic | `HLAvariableArray` |
| `HLAunicodeString` | `HLAunicodeChar` | Dynamic | `HLAvariableArray` |
| `HLAopaqueData` | `HLAbyte` | Dynamic | `HLAvariableArray` |
| `HLAtoken` | `HLAbyte` | 0 | `HLAfixedArray` |
| `AnchoringPlaceArray` | `AnchoringPlaceRecord` | Dynamic | `HLAvariableArray` |
| `LighthouseArray` | `LighthouseRecord` | Dynamic | `HLAvariableArray` |
| `HarborArray` | `HarborRecord` | Dynamic | `HLAvariableArray` |
| `GisDbSizesType` | `Int32` | 3 | `HLAfixedArray` |

### Fixed records

| Type | Encoding | Fields in wire order |
|---|---|---|
| `ClatLong` | `HLAfixedRecord` | Degree:Float, Polar:HLAunicodeChar |
| `PostureType` | `HLAfixedRecord` | X:Float, Y:Float, Z:Float, Heading:Float, Pitch:Float, Roll:Float |
| `AnchoringPlaceRecord` | `HLAfixedRecord` | Id:Int32, X:Float, Y:Float, Depth:Int32, Distance:Int32 |
| `LighthouseRecord` | `HLAfixedRecord` | Id:Int32, Type:Int32, Height:Float, Distance:Float, X:Float, Y:Float |
| `HarborRecord` | `HLAfixedRecord` | Id:Int32, Capacity:Int32, X:Float, Y:Float |
| `HelicopterPositionType` | `HLAfixedRecord` | X:Double, Y:Double, Z:Double |
| `HelicopterOrientationType` | `HLAfixedRecord` | Psi:Double, Theta:Double, Phi:Double |
| `QuaternionRateType` | `HLAfixedRecord` | Q0:Double, Q1:Double, Q2:Double, Q3:Double |

### Application encoding and units

- Unicode strings use a four-byte big-endian UTF-16 code-unit count and UTF-16BE characters, without a NUL terminator. Enum and Int32/UInt32 values are four-byte big endian.
- DateTime is UTC .NET ticks in HLAinteger64BE, not DateTime.ToBinary(), Unix time or RTI logical time. Local values are converted to UTC; unspecified time requires an explicit source time zone.
- Frigate.Velocity is **m/s**: the maritime adapter publishes `ShipSnapshot.Speed` from the m/s hydrodynamic state. ShipStatusReport.Velocity is **knots**, populated from `SpeedKnots`. Course is degrees; it is distinct from the legacy-negative Posture.Heading convention. The previous documentation's blanket “both speeds are knots” statement is superseded.
- ScenarioStartTime, Scenario.TOD and TOA are DateTime values; Environment.TOD is a Float hour. ReportInterval is Int32 in minutes in the Meko scheduler; zero disables automatic reports.
- Wind speed is sustained knots at 19.5 m in the current application contract. Wave and wind directions are FROM; the spectrum's Hs/Tp/seed/phase are not FOM fields.
- TaskOrd.FederateId is UInt32; the default Meko task identity is its own object-instance handle. The explicit federate-identity option is a separate policy, not an interchangeable handle space.
- Helicopter Position/Orientation retain Double fields. Quaternion is a four-Double **Qdot/rate** record, not a unit orientation quaternion. GIS fixed/variable arrays retain their declared record/index order.

## Sea-state and wind update semantics

SeaStateEnum SS0–SS9 is shared by Environment.SeaState and WeatherReport.SeaState. A selected/received Environment SeaState restores the ANEP wave/wind reference preset. An explicit WindSpeed in that same reflection overrides preset wind; across separate updates the later update wins. WindDirection is independently editable. Envi sends SeaState/WindSpeed for a preset and WindDirection/WindSpeed for an independent wind edit. WeatherReport remains informational and does not replace authoritative Environment updates. Custom Hs/Tp, spectrum, wave direction and phase remain local; no Wave1…Wave4 fallback exists.

[Physical preset meanings](../Maritime/Shared/SeaConditions.md) · [Federation precedence and current limits](../Maritime/Shared/SeaConditionsFederation.md).

## MekoFd publication and subscription

Source: the active `MekoFdSom.xml`, `Behavior/MekoFd.sfbm`, [FederationLink.cs](../../../Implementation/Library/Maritime/Code/src/NavySim.Hla.Fora/FederationLink.cs) and [FddContract.cs](../../../Implementation/Library/Maritime/Code/src/NavySim.Hla.Fora/FddContract.cs). P = Publish, S = Subscribe, P/S = both, — = neither.

| Object scope | Meko P/S | Fields |
|---|---|---|
| Frigate.Meko | P/S | Inherited Class, Name, Posture, Velocity |
| Frigate.Knox | S | Inherited Class, Name, Posture, Velocity |
| Scenario | S | All 16 declared fields |
| Environment | S | WindSpeed, WindDirection, SeaState, CloudDensity, FarFogRange, NearFogRange, FogType, TOD, FileName, DLLCLat, DLLCLong |
| Environment GIS/navigation aids | — | AnchoringPlace, GisDbSizes, Lighthouse, Harbor |
| OTC, Helicopter, root deletion privilege | — | Not consumed by the application adapter |

The Frigate parent is an inheritance container in the SOM; its inherited attribute declarations support the child class bindings. Current own-ship publication is **MEKO only**. Knox contacts are subscribed; choosing the local Knox vessel does not switch this SOM to publish Knox. [Knox capability limits](../Maritime/KnoxFd/Known%20Issues.md).

| Interaction | SOM sharing | Behavior region |
|---|---|---|
| BeginToPlay | Subscribe | Global/default |
| Communication.InjectionMessage | Neither | Inheritance container |
| InjectionMessage.ManOverboard / EngineFailure / RudderFailure / RadioFailure | Subscribe each | Shared HF |
| Communication.TaskOrd | Subscribe | HF |
| Communication.WeatherReport | Subscribe | HF |
| Communication.FormationMessage | PublishSubscribe | UHF |
| Communication.ShipStatusReport | Publish | HF |

## EnviFd publication and subscription

| Scope | Envi P/S | Fields |
|---|---|---|
| Environment | P | All 15 current attributes, including four GIS/navigation-aid fields |
| Scenario | S | DLLCLong, DLLCLat, TerrainFileName, ScenarioLocation, WeatherReportBroadcastInterval, ScenarioStartTime, ScenarioDescription, ScenarioVersion, ScenarioTitle |
| Other object fields | — | No frigate, helicopter, OTC or deletion-privilege publication |

| Interaction | SOM sharing | Behavior region |
|---|---|---|
| BeginToPlay | Subscribe | Global/default |
| Communication.WeatherReport | Publish | HF |

Envi's autonomous Environment declaration is advisory-driven and releases on delete. The .sfbm strategy describes generation/lifecycle policy; it does not add a new FOM attribute. BeginToPlay is global; weather transmission is the typed HF child interaction.

## ExMFd publication and subscription

ExMFdSom publishes Scenario/Environment and BeginToPlay; subscribes to Meko/Knox telemetry; publishes/subscribes to TaskOrd and the four typed injection children on HF; subscribes to FormationMessage on UHF and ShipStatusReport/WeatherReport on HF. Other classes, including Communication and InjectionMessage bases, have no direct P/S. [Detailed source roles and AAR semantics](TypedEventInjection.md#exmfdsom).

## Dimensions and radio behavior

FrequencySpectrum has upperBound **1,000,000**. Meko defines AllFrequencySpectrum [0,1000000], HF [3,30] and UHF [300,3000]; its eight radio uses bind only HF/UHF, including four concrete injection subscriptions. Envi defines HF and binds WeatherReport sending to it. These are model routing coordinates; the XML does not establish a physical-frequency unit. Do not infer a different dimensional encoding from an HF/UHF label.

Parameters and dimensions inherited from Communication do not create a parent subscription. Direct Communication-parent subscription in the global region would change the intended filtering. WeatherReport and the injection hierarchy inherit their parent dimension; adding a redundant local declaration is unnecessary. An ancestor subscription receives only the parameters available at that ancestor. Concrete injection subscriptions retain the child identity and typed fields; all four reuse the same HF region.

## SimGe application and behavior links

| Application | SOM | Behavior ID | Multiplicity |
|---|---|---|---|
| MekoFd | MekoFdSom | 1539eda8-e228-4853-84a0-f850d79f1e83 | 1..* |
| EnviFd | EnviFdSom | c16dd8bb-6391-44c8-8930-cef370d2cf46 | 1..1 |
| FedMonFd | — | 49bc9f7f-08f7-4377-b779-b30d0b7a441e | 1..1 |
| TacPicFd | — | c827387b-334d-4973-827d-6155a4e4b439 | 1..1 |
| ExMFd | ExMFdSom | 27a438bc-6091-48d7-8779-868c8983ef14 | 1..1 |

The FAM execution name is `NavySim`; runtime connection names remain configurable. FedMonFd's current monitor uses the standard MIM through its hand-written Fora adapter, not a new NavySim SOM. ExMFdSom defines the active 5.1.0 role; ExMFd uses its generated SOM/DTOs/encoders with the application-owned NFL/Fora session. TacPicFd FAM membership alone does not prove application integration. Knox currently has no FAM/SOM own-ship entry.

FAM free-text notes still mention the old 35/39 Environment counts and a Knox publication swap. Those comments are not the current declarations: the XML SOMs specify 11/15 fields and the runtime rejects own-Knox publication. This documentation uses the actual modules/behavior files and current adapters rather than copying those old notes.

## Completed legacy fields and source evidence

The audit used archived NSTMSS implementation files under `C:/OkPer/Projects/NSTMSS/Versions/Code/`. The following evidence establishes data shapes; modern HLA encodings deliberately replace native C++ ABI copies and NUL-terminated strings. No untyped fields remain.

| Field | Completed type | Legacy evidence |
|---|---|---|
| Environment.AnchoringPlace | AnchoringPlaceArray | `_nstmss_hakan/EnviFd/types.h:28-35`, `EnviFd20Doc.cpp:598-617`: packed logical list of id, xpos, ypos, depth, distance. |
| Environment.Lighthouse | LighthouseArray | `types.h:36-44`, `EnviFd20Doc.cpp:619-639`: id, type, height, distance, xpos, ypos. |
| Environment.Harbor | HarborArray | `types.h:45-51`, `EnviFd20Doc.cpp:641-659`: id, capacity, xpos, ypos. |
| Environment.GisDbSizes | GisDbSizesType | `EnviFd20Doc.h:126` declares int[3]; `HeliFd/src/yengecHLA.cpp:917-924` reads three ints. |
| Helicopter.Name | HLAunicodeString | `HeliFd/src/yengecHLA.cpp:1062-1075`: callsign char text with strlen+1. |
| Helicopter.Position | HelicopterPositionType | `HeliFd/include/fdm_defs.h:82-87`: three doubles; producer :1078-1100 and consumer :781-787. |
| Helicopter.Speed | Double | Producer :1102-1112 and consumer :789-794 use double. |
| Helicopter.Altitude | Double | Consumer :796-802 casts double; the producer block :1114-1123 is disabled in this snapshot. |
| Helicopter.Orientation | HelicopterOrientationType | `fdm_defs.h:88-93`: ePsi/eTheta/ePhi doubles; consumer :804-811, disabled producer :1125-1146. |
| Helicopter.Quaternion | QuaternionRateType | `fdm_defs.h:94-100`, producer :1148-1175 and consumer :812-817 identify quaternion_rate / Qdot, four doubles. |
| Helicopter.Status | HelicopterStatusEnum | `fdm_defs.h:76`: AIRBORNE=1, ON_DECK=2; producer :1177-1184, consumer :819-823. |
| Federation_Location_Message.Federation_Location_Name | HLAunicodeString | `nstmss 2.0/OSEFd2.0/src/RTIAmb.cpp:674`: text sent with strlen+1; `nstmss 1.2/OSEFd1.0/RTIAmb.cpp:663` corroborates it. |

HeliFd paths above refer to `Federates/Heli - VS2003/HeliFd/`; the same structures and decoders are present in `NSTMSS/nstmss 4.1/HeliFd/` and `nstmss 4.2/HeliFd/`. HeliFd uses `yengecfdm.h:143` -> `fdm_defs.h`, whose position is double-based; the separate generic Envi `types.h` float position is not substituted. Archived producer blocks contain disabled conversions and temporary-copy bugs; those defects are not copied into NFL. Altitude and Orientation have source-backed types even though that producer snapshot disables their updates.

The completed GIS/helicopter/location fields retain Neither sharing in MekoFdSom because the current MekoFd controller does not consume them. NFL now exposes all seven helicopter attributes and FederationLocationMessage, and NflWireCodec supports every completed layout. Resolving a typed handle does not constitute publication or subscription.

## Validation and synchronization

The current `20261018211031` import validates six exported XML documents, generated-source hashes, namespace transformations and preserved manual-source hashes. The deployed 5.1.0 model has **8 object classes, 13 interaction classes, 45 declared attributes, 35 declared parameters and 56 data-type definitions**. Ordered record layouts, enum values, inherited dimensions and sharing declarations agree with the existing 5.1.0 contract. SeaStateEnum covers 0–9; retired Wave fields and generic injection parameters remain absent.

[Current import and runtime validation](../../../Implementation/Library/NFL/SimGeSync/20261018211031/validation.json) · [Import manifest](../../../Implementation/Library/NFL/SimGeSync/20261018211031/import.json) · [Typed-event handoff](TypedEventInjection.md#generation-and-integration-handoff). The earlier [initial-heading audit](../../../Implementation/Library/NFL/SimGeSync/20261018-initial-heading/validation.json) records the introduction of the extra parameter; its incremental generated set is superseded by this full user export. Earlier 5.0.0 typed-injection evidence is [retained](../../../Implementation/Library/NFL/SimGeSync/20261018040130/runtime-validation.json).

For future changes, edit the active SimGe project, validate native model composition and XML schema, regenerate, and use each application's import workflow. Review generated diffs, preserve application-owned scaffolds and module/behavior IDs, verify deployed copies and P/S/codecs, then update these tables and [FDD Release Notes](FDD/ReleaseNotes.md). An unused `.fom` repository or a stale FAM note must not replace the `NavySim.fap`-selected source. XML type agreement does not make archived native C++ packets byte-compatible; legacy peers need a conversion adapter.
