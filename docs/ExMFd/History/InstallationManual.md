# ExMFd Installation Manual

> Source: *Implementation/FdApps/ExMFd/Docs/ExMFd Installation and User Manual.docx* (Section 1)
>
> See also: [ExMFd User Manual](ExMFd/UserManual.md) · [ExMFd Release Notes](ReleaseNotes.md) · [Development Environment Configuration](../DevelopmentEnvironmentConfiguration.md)

## Contents

- [1. Pre-installation](#1-pre-installation)
- [2. Installation](#2-installation)
- [3. Troubleshooting](#3-troubleshooting)
- [References](#references)

## 1. Pre-installation

### Hardware and software prerequisites

**Table 1. ExMFd hardware and software requirements**

| Component | Configuration |
|---|---|
| RAM | ExMFd uses 53 MB RAM |
| Hard disk space | ExMFd uses 12 MB hard disk space |
| Others | CD-ROM drive for installation |
| Operating system | Microsoft Windows XP Service Pack 2 |
| Runtime environment | Microsoft .NET 2.0 |
| HLA library | DMSO RTI 1.3 NG 6 |

> Installation requires **local administrator rights**.
>
> The [release notes](ReleaseNotes.md#known-bugs) list a known issue: setup requires the **MS Visual J# .NET redistributable package 2.0**.

## 2. Installation

Run `setup.exe`. The installer checks whether ExMFd is already installed:

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
