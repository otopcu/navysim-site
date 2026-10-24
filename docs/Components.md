# Components

NavySim 2026.1 is a suite release. It has a calendar version (`YYYY.N`), and every component carries its own semantic version. The table below follows the [Release Notes](ReleaseNotes.md).

## Federate applications

| Component | Version | Role | Documentation |
|---|---|---|---|
| **MekoFd** | 4.0.0 | MEKO-class frigate ship-handling simulator (C# / Stride / Fora) | [User Manual](Maritime/MekoFd/UserManual.md) · [Installation](Maritime/MekoFd/InstallationManual.md) · [Release Notes](Maritime/MekoFd/ReleaseNotes.md) · [Known Issues](Maritime/MekoFd/Known%20Issues.md) |
| **KnoxFd** | 5.0.0 | Knox-class frigate on the shared maritime runtime; offline | [User Manual](Maritime/KnoxFd/UserManual.md) · [Release Notes](Maritime/KnoxFd/Release%20Notes.md) · [Known Issues](Maritime/KnoxFd/Known%20Issues.md) |
| **ExMFd** | 4.0.0 | Exercise manager: C2SIM execution, typed events, workspace status and after-action review | [User Manual](ExMFd/UserManual.md) · [Installation](ExMFd/InstallationManual.md) · [Release Notes](ExMFd/ReleaseNotes.md) · [Known Issues](ExMFd/Known%20Issues.md) |
| **EnviFd** | 5.0.0 | Environment controller: time of day, wind, fog and cloud (.NET 10 / Fora) | [User Manual](EnviFd/UserManual.md) · [Installation](EnviFd/InstallationManual.md) · [Release Notes](EnviFd/ReleaseNotes.md) · [Known Issues](EnviFd/Known%20Issues.md) |
| **FedMonFd** | 3.0.0 | Federation monitor with live MOM monitoring (WPF / Fora) | [User Manual](FedMonFd/UserManual.md) · [Installation](FedMonFd/InstallationManual.md) · [Release Notes](FedMonFd/ReleaseNotes.md) · [Known Issues](FedMonFd/Known%20Issues.md) |
| **TacPicFd** | 1.0.0 | Tactical-display prototype; unchanged in 2026.1 | [User Manual](TacPicFd/UserManual.md) · [Installation](TacPicFd/InstallationManual.md) · [Release Notes](TacPicFd/ReleaseNotes.md) · [Known Issues](TacPicFd/Known%20Issues.md) |

## Tools

| Component | Version | Role | Documentation |
|---|---|---|---|
| **Sen** | 3.0.0 | Scenario Manager: C2SIM authoring with typed scheduled events | [User Manual](Sen/UserManual.md) · [Installation](Sen/InstallationManual.md) · [Release Notes](Sen/ReleaseNotes.md) · [Known Issues](Sen/Known%20Issues.md) |

## Libraries and federation model

| Component | Version | Role | Documentation |
|---|---|---|---|
| **NavySim Foundation Library (NFL)** | 3.1.2 | Shared federate foundation (.NET 10 / Fora; typed contracts) | [Release Notes](NFL/ReleaseNotes.md) · [Known Issues](NFL/Known%20Issues.md) |
| **Shared Maritime** | 1.0.0 | Shared sea, simulation and rendering runtime for the ship federates | — |
| **Environment Model** | 4.0.0 | Common sea-state and wind presets | — |
| **FOM** (`NavySim.xml`) | 5.1.0 | Federation Object Model: typed injection and initial heading | [FOM](FOM/Fom.md) · [FDD Release Notes](FOM/FDD/ReleaseNotes.md) · [Scenario Execution](FOM/ScenarioExecution.md) · [Typed Event Injection](FOM/TypedEventInjection.md) |

## Legacy installation

The suite-level [Installation Manual](InstallationManual.md) and [Development Environment Configuration](DevelopmentEnvironmentConfiguration.md) describe the NSTMSS-era setup (DMSO RTI 1.3-NG). Use the component installation pages above for the current .NET 10 applications.
