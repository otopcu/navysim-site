# NavySim Release Notes

| **Current version** | 2026.1 (in development); last release 6.0 |
| ------------------- | ----------------------------------------- |

NavySim was formerly known as **NSTMSS** (Naval Surface Tactical Maneuvering Simulation System, pronounced *"NiSTMiSS"*). Versions up to 5.2 were released under the NSTMSS name. From 2026.1 on, a suite release has a calendar version (`YYYY.N`) and lists the version of every component it contains; see [Version Control](Architecture/01.1-VersionControl.md).

## Version history

## [2026.1] - Unreleased

### Components

| Component                                             | Version | Changes                                         | Release notes                               |
| ----------------------------------------------------- | ------- | ----------------------------------------------- | ------------------------------------------- |
| **Federate Applications**                             |         |                                                 |                                             |
| EnviFd                                                | 5.0.0   | .NET 10 / Fora environment controls.            | [Notes](EnviFd/ReleaseNotes.md)             |
| MekoFd                                                | 4.0.0   | C# / Stride / Fora rewrite.                     | [Notes](Maritime/MekoFd/ReleaseNotes.md)    |
| KnoxFd                                                | 5.0.0   | Modern C# / Akdeniz model; offline.             | [Notes](Maritime/KnoxFd/Release%20Notes.md) |
| ExMFd | 4.0.0 | C2SIM execution, typed events, workspace status and AAR. | [Notes](ExMFd/ReleaseNotes.md) |
| FedMonFd                                              | 3.0.0   | WPF / Fora; live MOM monitoring.                | [Notes](FedMonFd/ReleaseNotes.md)           |
| TacPicFd                                              | 1.0.0   | Existing tactical-display prototype; unchanged. | [Notes](TacPicFd/ReleaseNotes.md)           |
| **Tools**                                             |         |                                                 |                                             |
| [Sen](../../Implementation/Tools/Sen/Code/Sen.slnx) | 3.0.0 | C2SIM authoring with typed scheduled events. | [Notes](Sen/ReleaseNotes.md) |
| **Libraries**                                         |         |                                                 |                                             |
| NavySim Foundation Library (NFL)                      | 3.1.2   | .NET 10 / Fora; typed contracts.                | [Notes](NFL/ReleaseNotes.md)                |
| [Shared Maritime](Maritime/Shared/Modules.md)         | 1.0.0   | Shared sea, simulation and rendering.           | —                                           |
| [Environment Model](Maritime/Shared/SeaConditions.md) | 4.0.0   | Common sea-state and wind presets.              | —                                           |
| [Scenarios](../../Implementation/Library/Scenarios/README.md) | 1.0.0 | C2SIM profiles, authoring and execution. | [Plan/evidence](Roadmap.md#c2sim-scenario-infrastructure) |
| [Desktop UI](../../Implementation/Library/DesktopUI/README.md) | 0.1.0 | Shared WPF controls and window frame. | [Notes](Sen/ReleaseNotes.md) |
| **Federation Model**                                  |         |                                                 |                                             |
| FOM (`NavySim.xml`)                                   | 5.1.0 | Typed injection and initial heading.                       | [Notes](FOM/FDD/ReleaseNotes.md)            |

### Platform

Current .NET 10 configuration; legacy components retain their documented toolchains.

| Item | Version / Configuration |
|---|---|
| IDE | Visual Studio 18.12.12308.306 (Insiders) |
| Runtime Platform | .NET 10 / C# 14; stable SDK 10.0.4xx |
| OS | Windows 11 Pro x64; reference build 26300 |
| RTI | Fora RTI / Fora.Client 20261004.0.0; IEEE 1516-2025 (HLA 4) |
| Graphics | Stride 4.3.0.2507 / Direct3D 11; WPF for EnviFd, FedMonFd, ExMFd and Sen |
| FDD Version | **5.1.0** — [FDD Release Notes](FOM/FDD/ReleaseNotes.md) |

### Suite

- **Configuration management** — The suite is a local Git repository whose root is the `NavySim` folder; `Private`, `Resources`, build output and the snapshot copies made before the repository stay outside it.
- **Versioning** — The suite has a calendar version (`2026.1`); every component has its own semantic version in the `Version.props` of its folder, and the FOM in its `modelIdentification`. See [Version Control](Architecture/01.1-VersionControl.md).
- **Build** — `Implementation/NavySim.slnx` builds the .NET 10 components (NFL, EnviFd, FedMonFd, ExMFd, MekoFd, KnoxFd, Sen and shared modules) together; every binary carries the Git commit it was built from in its informational version.
- **Scenario and exercise workflow** — Sen authors typed scheduled events, including side-bearing ManOverboard; ExMFd separates authored inspection from instant injection, shows workspace progress and includes accepted weather updates in AAR statistics. NavySim supplement 1.1.0 is additive; the C2SIM baseline is unchanged. FDD 5.1.0 adds initial true heading for pre-Begin scenario placement; speed and machinery remain under OOW control. See [Sen notes](Sen/ReleaseNotes.md), [ExMFd notes](ExMFd/ReleaseNotes.md) and [acceptance scope](../../Implementation/Library/Scenarios/Validation/exm-typed-ui-20261018.json).
- **Documentation** — Version Control has its own page; the FOM, FDD and RID pages are under `FOM/`; every release note ends with its modification DTG.

---

## [6.0]

*NavySim*

**By:** Okan TOPÇU

**Remarks**
- Name change: NSTMSS → NavySim.
- Based on NSTMSS 5.2.

---

## [5.2] - 2010

**By:** Okan TOPÇU

**Federates**
- Meko Federate (MekoFd) 3
- Environment Federate (EnviFd) 3
- Federation Monitor Federate (FedMonFd) 2
- Exercise Planner Federate (ExPFd) 2

**Supporting tools**
- Sen 1 (scenario construction tool for NSTMSS)

**Supporting libraries**
- NSTMSS Foundation Library (NFL)

**Platforms**
- IDE: MS Visual Studio .NET 2010
- Runtime platform: .NET Framework 4.0
- OS: MS Windows 7
- RTI: DMSO RTI-NG-1.3v6
- Graphics: SGI OpenGL Performer 3.2.2, DirectX 9.0c
- FED: 3
- RID: 1

**Documentation:** NSTMSS Technical Report

**Remarks**
- GSEd is replaced by a new scenario construction tool: Sen 1.
- Major FED change (scenario object model).
- Minor OS change (MS Windows 7).
- IDE change (MS VS2010).

---

## [5.1] - 2007

**By:** Okan TOPÇU

**Federates**
- Meko Federate (MekoFd) v3.x
- Environment Federate (EnviFd) v3.x
- Federation Monitor Federate (FedMonFd) v2.x
- Exercise Planner Federate (ExPFd) v2.x
- Tactical Picture Federate (TacPicFd) v1.0.design

**Supporting tools**
- Graphical Scenario Editor (GSEd) v2.x for NSTMSS

**Supporting libraries**
- NSTMSS Foundation Library (NFL) v1.0.0

**Platforms**
- IDE: MS Visual Studio .NET 2008 SP1
- Runtime platform: .NET Framework 3.5 SP1
- OS: MS Windows Vista
- RTI: DMSO RTI-NG-1.3v6
- Graphics: SGI OpenGL Performer 3.2.2, DirectX 9.0c
- FED: 2.0.6
- RID: 1.0

**Documentation:** NSTMSS Technical Report

**Remarks**
- Helicopter Federate (HeliFd) v1.0.alpha is not supported anymore.
- MS Windows Vista ready.

---

## [5.0.1] - 2006-08-21

**By:** Canku CALARGUN

**Federates**
- Meko Federate (MekoFd) v2.2.1
- Environment Federate (EnviFd) v2.1.2
- Federation Monitor Federate (FedMonFd) v1.1.x
- Exercise Planner Federate (ExPFd) v1.0.x
- Helicopter Federate (HeliFd) v1.0.alpha
- Tactical Picture Federate (TacPicFd) v1.0.design

**Supporting tools**
- Graphical Scenario Editor (GSEd) v1.0.1 for NSTMSS

**Platforms**
- IDE: MS Visual Studio .NET 2005
- OS: MS Windows XP Professional SP2
- RTI: DMSO RTI-NG-1.3v6
- Graphics: SGI OpenGL Performer 3.2.2, DirectX 9.0c
- FED: 2.0.4
- RID: 1.0

**Documentation:** Canku's MS Thesis

**What is new?**
- 4-DOF hydrodynamic model
- Wave models
- Ship wakes
- Controlling the waves using EnviFd
- Simple cloud simulation
- Wave shading simulation

---

## [5.0] - 2006-08-21

**By:** Okan TOPÇU

**Federates**
- Meko Federate (MekoFd) v2.2.x
- Environment Federate (EnviFd) v2.1.x
- Federation Monitor Federate (FedMonFd) v1.1.x
- Exercise Planner Federate (ExPFd) v1.0.x
- Helicopter Federate (HeliFd) v1.0.alpha
- Tactical Picture Federate (TacPicFd) v1.0.design

**Supporting tools**
- Graphical Scenario Editor (GSEd) v1.0.1 for NSTMSS

**Platforms**
- IDE: MS Visual Studio .NET 2005
- OS: MS Windows XP Professional SP2
- RTI: DMSO RTI-NG-1.3v6
- Graphics: SGI OpenGL Performer 3.2.2, DirectX 9.0c
- FED: 2.0.4
- RID: 1.0

**Documentation:** NSTMSS Technical Report

**Remarks**
- OTCFd is not supported anymore.

---

## [4.2] - 2005-08-23

**By:** Aslı KILIÇ

**Federates**
- Meko Federate (MekoFd) v2.0.1
- Environment Federate (EnviFd) v2.0.1
- Helicopter Federate (HeliFd) v1.0 Alpha (in development)
- Officer in Tactical Command Federate (OTCFd) v4.0

**Platforms**
- IDE: Visual Studio .NET 2003
- OS: Windows XP
- RTI: RTI-NG-1.3v6
- Graphics: Performer 3.1.1
- FED: 2.0.2
- RID: 1.0

**Documentation:** Aslı KILIÇ's Master Thesis

**Remarks**
- Aslı KILIÇ's MS Thesis.

---

## [4.1] - 2004-08-30

**By:** Okan TOPÇU

**Remarks**
- **Not released.**
- Used for Aslı's MS thesis study.

---

## [4.0] - 2003-10-06

*Windows version*

**By:** Okan TOPÇU

**Federates**
- MekoFd v2.0 (Win2K, RTI-NG-1.3v6, Performer 3.0.2)
- OTCFd v4.0 (Win2K, RTI-NG-1.3v6, Performer 3.0.2)
- EnviFd v1.3 (Win2K, RTI-NG-1.3v6)

**Platforms**
- IDE: Visual Studio .NET 2003
- OS: Win2K
- RTI: RTI-NG-1.3v6
- Graphics: Performer 3.0.2
- FED: 2.0.1
- RID: 1.0

**Documentation:** NSTMSS Technical Report

**Remarks**
- Windows version.
- KnoxFd is not ported and is not supported anymore.

---

## [3.0] - 2002-10-31

*Linux version*

**By:** Okan TOPÇU

OSEFd and FedMonFd are extracted from the NSTMSS release. Many bugs are fixed in MekoFd and OTCFd.

**Federates**
- MekoFd v1.2 (RH7.3, RTI-NG-1.3v6, Performer 2.5.2)
- KnoxFd v4.41 (RH7.3, RTI-NG-1.3v6, Performer 2.5.2)
- OTCFd v3.22 (RH7.3, RTI-NG-1.3v6, Performer 2.5.2)
- EnviFd v1.2 (Win2K, RTI-NG-1.3v6)

**Platforms**
- IDE: KDevelop
- OS: RedHat 7.3 and Win2K
- RTI: RTI-NG-1.3v6
- Graphics: Performer 2.5.2
- FED: 2.0.1
- RID: 1.0

**Documentation:** None

**Remarks**
- Linux version.

---

## [2.0] - 2001-12-15

**By:** Okan TOPÇU

Okan's thesis and Hasan's thesis are combined, and Hasan's RTI code is ported to RTI-NG.

**Federates**
- KnoxFd v4.5 (RH 7.1 + RTI-NG-1.3r3.2)
- OTCFd v3.3 (RH 7.1 + RTI-NG-1.3r3.2)
- MekoFd v1.1 (RH 7.1 + RTI-NG-1.3r3.2)
- EnviFd v2.0 (Win2000 + RTI-NG-1.3r3.1)
- OSEFd v2.0 (Win2000 + RTI-NG-1.3r3.1)
- FedMonFd v2.0 (Win2000 + RTI-NG-1.3r3.1)

**Platforms**
- IDE: KDevelop
- RTI: RTI-NG-1.3r3.1/3.2
- FED: 2.0

**Documentation:** NSTMSS Technical Report

---

## [1.3] - 2001-09-03

**By:** Okan TOPÇU

NSTMSS Linux version of Okan's thesis. The simulation entity group is ported to RH7.1 and the RTI is ported to the NG version.

**Federates**
- KnoxFd v4.41 (RH 7.1)
- OTCFd v3.21 (RH 7.1)
- MekoFd v1.01 (RH 7.1)
- EnviFd v1.2 (Win2000)

**Platforms**
- RTI: RTI-NG-1.3r3.1/3.2
- FED: 2.0

**Documentation:** None

---

## [YENGEC] - 2001-08-23

**By:** Hakan SAVAŞAN

Hakan's thesis study adds a helicopter federate: Yengec. The federation is called Yengec.

**Federates**
- KnoxFd (modified version of v4.3)
- EnviFd (new Windows version)
- Yengec v1.0

**Platforms**
- RTI: RTI 1.3r6

**Documentation:** Hasan's Thesis *(as stated in the source document)*

---

## [1.2] - 2000-02-26

**By:** Hasan Basri AKIRMAK

Hasan's thesis study adds two more federates: FedMonFd and OSEFd. It also implements time management schemes for NSTMSS.

**Federates**
- KnoxFd v4.31 (IRIX 6.3 + RTI 1.3v6)
- OTCFd v3.11 (IRIX 6.3 + RTI 1.3v6)
- EnviFd v1.11 (NT 4.0 + RTI 1.3v6)
- OSEFd v1.0 (NT 4.0 + RTI 1.3v6)
- FedMonFd v2.0 (NT 4.0 + RTI 1.3v6)

**Platforms**
- RTI: RTI 1.3r6

**Documentation:** Hasan's Thesis

---

## [1.1] - 2000-01

**By:** Okan TOPÇU

- MekoFd v1.0 is implemented and added to NSTMSS.
- RTI: RTI v1.3r6
- Documentation: None

---

## [1.0] - 1999-09

*IRIX version*

**By:** Okan TOPÇU

Okan's thesis study covers the first release of the NSTMSS federation.

**Federates**
- KnoxFd v4.3 (IRIX 6.3 + RTI 1.3r6)
- OTCFd v3.1 (IRIX 6.3 + RTI 1.3r6)
- EnviFd v1.1 (NT 4.0 + RTI 1.3r6)

**Platforms**
- RTI: RTI 1.3r6

**Documentation:** Okan's Thesis

---

*Copyright © 1999–2026 Okan Topçu.*

*Modification DTG: 2026-10-18 (UTC+03:00)*
