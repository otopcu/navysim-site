# NavySim RID Release Notes

> Source: *Documentation/Archieve/RID/releasenotes_RID.doc*
>
> See also: [NavySim Release Notes](../../ReleaseNotes.md) · [FDD Release Notes](../FDD/ReleaseNotes.md)

| | |
|---|---|
| **Legacy version** | 1.0 (`Documentation/Archieve/RID/RTI.rid`) |
| **Originally developed by** | Okan TOPÇU (otopcu@gmail.com) |

The RID (RTI Initialization Data) file configures the DMSO RTI 1.3-NG; copies of it are kept beside the federate code (`Implementation/FdApps/<federate>/Code/RTI.rid`).

## Current RTI configuration

The modern Fora applications do not load this DMSO RID. Connection address, federation/FDD selection and local refresh settings belong to application configuration; SimGe records model/application links in its FAP/FAM/behavior files. No new RID revision was introduced by the SeaState/Wave migration. [Current FDD contract](../FDD/ReleaseNotes.md) · [Fora monitor integration](../../FedMonFd/ReleaseNotes.md).

## Version history

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2003 | Main release for NSTMSS 4.0. |
| — | 2000 | Routing space added. |

> Note: Rows marked “—” have no version number in the source document.

---

*Copyright © 1999–2026 Okan Topçu.*

*Modification DTG: 2026-10-17 22:25 (UTC+03:00)*
