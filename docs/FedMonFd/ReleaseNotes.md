# FedMonFd Release Notes

> Source: *Implementation/FdApps/FedMonFd/Docs/RN FedMonFd.docx*
>
> Federation Monitor Federate. See also: [FedMonFd Installation Manual](InstallationManual.md) · [FedMonFd User Manual](FedMonFd/UserManual.md) · [NavySim Release Notes](../ReleaseNotes.md) · [Known Bugs](../Known%20Bugs.md#fedmonfd) · [Roadmap](../Roadmap.md#fedmonfd)

| | |
|---|---|
| **Current version** | 3.0.0 (set in `Implementation/FdApps/FedMonFd/Version.props`) |
| **Source document date** | October 2, 2012 |
| **Developed by** | Okan TOPÇU (otopcu@ceng.metu.edu.tr / otopcu@tsk.mil.tr) |

> FedMonFd 1.0.0 (2005) is a new federate written from scratch. It has no versioning link to the earlier federation monitor federate (FedMonFd v2.0 of NSTMSS 1.2–2.0, see the [NavySim Release Notes](../ReleaseNotes.md)); only some RTI code was reused.

## Contents

- [Version summary](#version-summary)
- [Version history](#version-history)

## Version summary

| Version | Latest change | NSTMSS release       | Platform                       |
| ------- | ------------- | -------------------- | ------------------------------ |
| 3.0.0   | 20261016      | 2026.1               | .NET 10, WPF, Fora, NFL 3.1.2  |
| 2.0.0   | 27.09.2008    | 5.1 / 5.2 (v2.x)     | VS 2008 Pro SP1, Windows Vista |
| 1.1.0   | 18.02.2006    | 5.0 / 5.0.1 (v1.1.x) | Microsoft Reports, `/clr`      |
| 1.0.0   | 29.01.2006    | —                    | VS .NET 2005                   |

## Version history

## [3.0.0] - Unreleased

**By:** Okan TOPÇU

Ported from C++/CLI (Windows Forms, HLA 1.3, DMSO RTI 1.3-NG 6) to .NET 10 WPF over Fora.Client 20261004.0.0 (IEEE 1516-2025), with the layered structure of EnviFd: `SimulationLayer`, `PresentationLayer`, `FedMonFdUI-Wpf` and `tests/FedMonFd.Tests`. See `Implementation/FdApps/FedMonFd/Code/README.md`.

### Infrastructure

- Uses the HLA 4 MIM: `HLAmanager.HLAfederation`/`HLAfederate` for Federation and Federate Status, and the six `HLArequest…`/eight `HLAreport…` interactions for the RTI data. Report values are decoded from the binary IEEE 1516.2 types instead of HLA 1.3 comma-separated strings; class, attribute and transportation names are resolved through the RTI.
- RTI calls run outside the callbacks on one work queue; the tick timer only applies queued changes to the screen.
- MVVM with CommunityToolkit.Mvvm: `MainViewModel` replaces the `CUIControl` presenter; the window only provides dialogs, printing and layout.
- Removed: DMSO RTI / Portico dependency, `RTI.rid`, `nstmss.fed`, the RTI_DataSet XSD and the Visual Studio setup project (the legacy sources remain in `Code/`).

### Federation Control

- Command bar (Connect/Disconnect, Refresh F5, Auto-refresh switch, Report menu, Messages) replaces the three control tabs; Fora address, federation, FDD and refresh rates are in a collapsible Connection / Settings panel.
- Fora Address field added; the FDD (default: the shared `NavySim.xml`) replaces the FED file. If the name FedMonFd is in use, FedMonFd joins with an RTI-assigned name.
- The last connection, refresh rates, view options and window layout are remembered (`%LOCALAPPDATA%\NavySim\FedMonFd\settings.json`). Browse opens in the FDD folder.

### Federation and Federate Status

- Federation Status is shown as a card (FOM modules, RTI version, MIM, saves).
- Master–detail view: a federate list with state badge and counters; the selected federate shows what it publishes, subscribes to and its traffic. "All federates" keeps the RTI data tables, with search and grouping by federate.
- Federate Status also shows type, time management, logical time and the update/reflection/interaction/object counters of each federate.

### P/S Status, Traffic and Network Status

- **P/S Matrix** (the P/S Status tab planned since 2.0): classes and attributes × federates with P, S or P+S; subscriptions without a publisher and publications without a subscriber are flagged, taking class hierarchy into account. A class row says how many attributes lack a publisher and how many lack a subscriber. MOM classes can be hidden.
- **Traffic**: messages per second from the change of the MOM counters, per federate and per interaction class, with sparklines of the last 60 samples. The RTI sends the federate counters itself every 2 s (`HLAsetTiming`, 1–60 s, can be switched off) instead of FedMonFd requesting them: evenly spaced, finer samples and fewer requests. FedMonFd stops the periodic updates when it disconnects.
- **P/S Diagrams**: class-based and federate-based Publish/Subscribe diagrams in the notation of *Distributed Simulation*, Chapter 2 (classes as boxes with their attributes or parameters from the FDD, federates as ellipses, P/S arrows labelled `P(*)`, `S(Callsign,Position)`, `PS(*)`), drawn from the live publications and subscriptions; hover highlights the members of an arrow, click switches between class and federate diagrams; copy, save as PNG or export all.
- **Run-time P/S changes**: a light P/S refresh every 5 s (only publications and subscriptions) and, for federates with service reporting on, an immediate request after each Publish/Subscribe/Unpublish/Unsubscribe call. A federate's P/S rows are replaced at once when its new set is complete (no half-received state). Changes are logged (`P/S change: …`) and marked in the P/S diagrams for a minute (NEW, CHANGED, REMOVED).
- **Network** (Network Status): federates and the data flows between them as a diagram; hover for the classes, click a federate to open its details.

### RTI Services Usage

- **Services** tab (open since 2.0): switches the MOM Service Reporting Switch of a federate on and off (`HLAsetSwitches`) and counts its `HLAreportServiceInvocation` reports: calls, calls per second, failures, last exception and arguments per federate and service, and reports lost according to their serial numbers. FedMonFd switches reporting off again when it disconnects.
- Both reports get a *Measured Service Invocations* part, so the RTI Services Usage reports are filled from measurements instead of the RTI data tables only.

### Reports

- Microsoft Reports (RDLC) is replaced by a WPF document with the same two report types; it can be printed (PDF through a PDF printer) and saved as HTML or CSV (Excel). Monitor data are kept after resign, so reports can still be generated; a new join clears them.

### System Messages

- Collapsible message log at the bottom with time stamp and level (info, warning, error) in colour, warning/error counts and a warnings-only filter.
- One summary line per refresh ("16 reports received from 2 of 2 federate(s)") instead of a line per report; a P/S check line when unmatched publications or subscriptions change.

### Validation

- 68 local and 50 live checks against Fora.Rti.Server 20261004.0.0 (`Code/tools/Test-Live.ps1`); the WPF views were checked by hand with EnviFd and MekoFd.

---

## [2.0.0] - 2008-09-27

**By:** Okan TOPÇU

**27.09.2008**
- Compiled with MS Visual Studio 2008 Pro SP1.

**20.12.2007**
- Compiled with MS Visual Studio 2008 Pro.

**16.02.2007**
- Compiled on Windows Vista Ultimate.

---

## [1.1.0] - 2006-02-18

**18.02.2006**
- Reporting library changed from Crystal Reports to Microsoft Reports.
- RTI tick rate and RTI data monitor rate settings are implemented.
- FedMonFd database is removed; data is now kept in a DataSet.
- Code rewritten for the `/clr` switch instead of `/clr:oldSyntax` (written as "/clr-old" in the source), for future compatibility.

---

## [1.0.0] - 2006-01-29

**29.01.2006**
- Compiled with MS Visual Studio .NET 2005.

**25.07.2005**
- Federation and federate status displays are changed.
- Automatic update request for federation and federate status is implemented.
- Wait cursor for time-bounded function calls is implemented.
- HTML Help file (`Release Notes.chm`) integration is done.

**01.03.2005**
- About dialog box is implemented.

**27.02.2005**
- Federation status display is implemented.

**17.02.2005**
- Federate-based and service-based usage reporting is implemented.

**13.02.2005**
- Database functionality is implemented.

**10.02.2005**
- Monitoring and data-on-demand (RTI Services Table) services are implemented.

**23.01.2005**
- Development of a new Federation Monitor Federate starts from scratch. It has no versioning link to the old federation monitor federate; some old RTI code is reused.

---

*Modification DTG: 2026-10-16 11:40 (UTC+03:00)*
