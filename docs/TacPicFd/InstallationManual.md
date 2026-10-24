# TacPicFd Installation Manual

> Source: *Implementation/FdApps/TacPicFd/Docs/TacPicFd Installation and User Manual.docx* (Section 1)
>
> See also: [TacPicFd User Manual](TacPicFd/UserManual.md) · [TacPicFd Release Notes](ReleaseNotes.md) · [Development Environment Configuration](../DevelopmentEnvironmentConfiguration.md)

## Contents

- [1. Pre-installation](#1-pre-installation)
- [2. Installation](#2-installation)
- [3. Troubleshooting](#3-troubleshooting)
- [References](#references)

## 1. Pre-installation

### Hardware and software prerequisites

**Table 1. TacPicFd hardware and software requirements**

| Component | Configuration |
|---|---|
| RAM | *(not specified in the source)* |
| Hard disk space | *(not specified in the source)* |
| Others | CD-ROM drive for installation |
| Operating system | Microsoft Windows Vista SP1 |
| Runtime environment | Microsoft .NET 3.5 |
| HLA library | DMSO RTI 1.3 NG 6 |

> Installation requires **local administrator rights**.

## 2. Installation

Run `setup.exe`. The installer checks whether TacPicFd is already installed:

- If the **current** version is detected, the installer asks whether to **remove** or **repair** it.
- If a **previous** version is detected, the installer uninstalls it.

Then follow the installer screens.

> The source says "follow the screens shown below", but no installer screenshots are included.

## 3. Troubleshooting

### Missing DLL: `LibRTI-NG.dll` not found

- Install DMSO RTI.
- Configure the RTI environment variables as described in [1].

## References

1. Topçu, O., *NSTMSS Development Environment Configuration Manual*, November 17, 2004. — see [Development Environment Configuration](../DevelopmentEnvironmentConfiguration.md) for the latest version.
