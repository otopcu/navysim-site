# ExMFd Release Notes

> Source: *Implementation/FdApps/ExMFd/Docs/RN ExMFd.docx*
>
> Exercise Manager Federate (formerly Exercise Planner Federate, ExPFd). See also: [ExMFd Installation Manual](InstallationManual.md) · [ExMFd User Manual](UserManual.md) · [NavySim Release Notes](../ReleaseNotes.md) · [Known Issues](Known%20Issues.md) · [Roadmap](Roadmap.md)

| | |
|---|---|
| **Current version** | 4.0.0 (unreleased) |
| **Source document date** | January 31, 2016 |
| **Originally developed by** | Okan TOPÇU (okantopcu@gmail.com) |

## Contents

- [Version summary](#version-summary)
- [Version history](#version-history)

## Version summary

| Version | Latest change | NSTMSS release | Platform / RTI layer | By |
|---|---|---|---|---|
| 4.0.0 | 18.10.2026 | 2026.1 | .NET 10 / WPF / Fora / C2SIM | Okan TOPÇU |
| 3.0.1 | 31.01.2016 | — | VS 2015 Community, Windows 10, WPF | Okan TOPÇU |
| 3.0.0 | 24.08.2015 | — | Renamed ExPFd → ExMFd | Okan TOPÇU |
| 2.1.0 | 18.08.2009 | 5.2 (v2) | Generic RTI layer | Okan TOPÇU |
| 2.0.0 | 01.05.2009 | 5.1 (v2.x) | VS 2008 Pro, Windows Vista, NFL, Portico 0.8 | Okan TOPÇU |
| 1.0.3 | 20.08.2006 | 5.0 / 5.0.1 (v1.0.x) | — | Okan TOPÇU |
| 1.0.2 | 05.03.2006 | — | — | Okan TOPÇU |
| 1.0.1 | 05.02.2006 | — | VS .NET 2005 | Okan TOPÇU |
| 1.0.0 | 27.08.2005 | — | — | Okan TOPÇU |

## Version history

## [4.0.0] — Unreleased

### Infrastructure and FOM integration

- Modern .NET 10 WPF application/runtime, active-monitor startup, FDD browsing and NFL/Fora lifecycle.
- C2SIM validation; base Scenario OC, HF TaskOrd, BeginToPlay, Environment OC and HF typed ManOverboard/EngineFailure/RudderFailure/RadioFailure mapping from user export `20261018040130` (FDD 5.0.0).
- Retired custom NavyScenario channel and participant handlers to archive. Generated SimGe base sources remain unchanged.
- FDD 5.1.0 TaskOrd.InitialHeading fixes missing scenario heading: sends grid heading plus grid-north offset, applies it to posture and solver yaw before Begin, and preserves speed, shaft state, EOT and manual rudder. Omission keeps the existing heading; late assignments cannot reorient a running ship. Initial placement does not enable autopilot. Focused checks, 27 offline checks and 12 isolated real-RTI checks passed. [Evidence](../../../Implementation/Library/NFL/SimGeSync/20261018-initial-heading/validation.json).

- Imported ExMFdSom DTOs, SOM handles and codecs; retains the application-owned NFL/Fora lifecycle. Local accepted sends and remote received callbacks have distinct AAR Direction; typed child parameters are collected under HF/UHF filters.
- All three application builds, 25 offline checks, WPF rendering and 12 live groups passed with and without optional EnviFd. [Evidence](../../../Implementation/Library/NFL/SimGeSync/20261018040130/runtime-validation.json).

### Tactical communications — OSE

- Verified 28 offline acceptance checks, formatted/compact WPF browsing and 12 real-RTI groups with and without EnviFd; all five TMS families / eight concrete types were observed. [Evidence](../../../Implementation/Library/NFL/Validation/tms-20261018/validation.json).

- Restores the legacy OSE identity and a dedicated Comms Center: All/Inbox/Sent, type/full-field search, newer/older browsing, shared FM/TO/CC/SBJ/DTG signal formatting, original-field inspection and full-signal copy. All retained records are browsable beyond AAR's latest 1,000 rows; stable selection and revision-gated refresh preserve reading position.
- Separates the bounded connection TMS archive from scenario/AAR counters. Scenario loads and disconnect preserve it; a successful new RTI connection resets it. Environment object updates remain in AAR. Accepted sends and local callbacks retain distinct evidence labels.
- Sends TaskOrd and typed events with tactical FM OSE while retaining the configured RTI name. TaskOrd TO identifies the ship/current participant and CC is OTC; object-target semantics remain intact. No additional FDD schema change.
- Extracts Federation Architecture §2.5 into [TMS architecture](../Architecture/TacticalMessagingSystem.md), preserving legacy source/figures and distinguishing current typed/HF behavior. Adds the shared formatter in NFL.

### Exercise workspace

- Extracted reusable presentation resources and monitor-aware frame insets into Library/DesktopUI; Sen now uses the same design. Existing ExMFd window and typed-injection UI checks pass after extraction.

- Six workflow pages: RTI connection, Scenario information, Distribution & role casting, Execution, Event injection and AAR; independent Comms Center navigation.
- Unified all section tabs under one application-wide modern style: Scenario Information, Scheduled/Instant Event Injection and Execution Monitoring/Traffic log/Evidence. Consistent active accent, hover and keyboard focus; page content retains its own typography.
- Modernized action buttons with consistent rounded primary/secondary/subtle/stop variants, folder icon for Open scenario, hover/press feedback, keyboard focus and disabled states. Caption/navigation semantics are retained.
- Modernized dropdown fields/options and all data tables, including the scenario picker: flat headers, alternating rows, blue selection/focus, visible sort direction and retained column resizing. Dropdown selection, Escape and arrow-key navigation are verified.
- Integrated window controls into the application header and removed the separate Windows title bar. Native header dragging, double-click/system menu and edge resizing remain; monitor/DPI-aware maximized insets prevent clipping and taskbar overlap. Custom Close retains RTI cleanup.
- Separate readiness, Distribute & assign and Run; read-only source documents and explicit allocation states.
- Reference/elapsed/wall clocks, scalable timeline, ship monitoring, message details and RTI evidence.
- Buffered copyable log and changed-field notifications avoid idle flashing.
- Workspace navigation now shows stable colour, icon and text statuses for RTI connection, scenario loading, distribution, execution, event dispatch and AAR availability. Selected-page highlighting is independent. Partial failures remain amber; disconnect, reload and New run refresh readiness from current evidence.

### Scenario briefing

- Replaced the flat Scenario Information text with five EnviFd-style tabs: Briefing, Units, Environment, Event plan and Source files.
- Added summary cards, structured metadata, selectable ship details, marine coordinate formatting, a true-FROM wind compass and explicit preset/override labels.
- Added an authored event timeline/table with description inspection and structured briefing copy. Selection survives idle refresh; compact and empty states are handled.
- Initial state and authored motion remain distinct from live telemetry and OOW-controlled motion. Source XML remains read-only.

### Event scheduling

- Local automatic injection; no periodic clock or remote pause/stop/reset.
- Separate Scheduled and Instant event tabs: read-only authored schedule/parameter inspection, immediate runtime injection, preview, inline validation and recent instant history.
- Type-specific dropdowns shared with Sen: MOB Port/Starboard, engine Port/Starboard/Both, radio HF/UHF/Both; rudder has no component selector. Unrelated inputs are hidden.
- Scheduled MOB authoring and optional failure descriptions use the additive NavySim profile 1.1.0; existing 1.0.0 packages remain readable. Overlap checks and ship-local fault expiry are retained.
- Typed HLAfloat64BE DurationSeconds carries fractional-second failures without minute conversion. Ship-local expiry is independent; recovery rows mean expected expiry.
- Optional independent EnviFd; supplied-field weather updates and explicit wind precedence.
- RTI acceptance remains distinct from application confirmation. No remote receipts/deduplication are claimed.

### Collection and AAR

- Weather Change now appears in message statistics and recorded-message details after RTI accepts an Environment update. Initial, scheduled and instant weather broadcasts are counted once each, with patch fields, units and command/run correlation; WeatherReport remains separate. Failed sends and cache replays are excluded.

- Actual messages, cumulative counts and HF ship observations at the one-minute Scenario interval.
- Five review tables with JSON, XLSX, CSV, HTML and Print / PDF; bounded memory and Disconnect retention.
- Two-ship isolated Fora acceptance with and without EnviFd verifies OOW preservation, native assignment/events, local expiry, telemetry and independent Stop/Disconnect.

## [3.0.1] - 2016-01-31

**31.01.2016** — *Okan TOPÇU*
- Compiled with MS VS 2015 Community Edition.
- Compatible with Windows 10.
- WPF GUI.

---

## [3.0.0] - 2015-08-24

**24.08.2015**
- Name change: Exercise Planner Federate (ExPFd) → ExMFd.

---

## [2.1.0] - 2009-08-18

**18.08.2009**
- Generic RTI layer is adapted.

---

## [2.0.0] - 2009-05-01

**01.05.2009**
- Report viewer code is refined.

**12.05.2008**
- ExPFd is adapted to the NFL.

**02.04.2008**
- RTI methods are compatible with Portico 0.8.

**20.12.2007**
- Compiled on Windows Vista Home Premium.
- Compiled with MS Visual Studio 2008 Pro.

---

## [1.0.3] - 2006-08-20

**20.08.2006**
- Combo boxes are re-implemented as read-only.

---

## [1.0.2] - 2006-03-05

**05.03.2006**
- RTI tick rate setting is implemented.
- OTC info section of the scenario is added.
- XML scenario parser is implemented.

---

## [1.0.1] - 2006-02-05

**05.02.2006**
- RTI Scenario Start Time attribute data type changed to `DateTime`.

**04.11.2005**
- TMS report is implemented.
- Ship-Based Positions and Scenario Information reports are implemented.
- Compiled with MS Visual Studio .NET 2005 (previously RC-1).
- Splash screen is implemented.
- About dialog is implemented.
- Scenario Information UI is redesigned.

---

## [1.0.0] - 2005-08-27

**27.08.2005**
- RTI interface for the Weather Report interaction is implemented.

**20.08.2005**
- TMS regions are implemented.
- Radio Failure event is implemented.

**26.07.2005**
- HTML Help file (`Release Notes.chm`) integration is done.

**23.07.2005**
- RTI interface for the Start-To-Play interaction is implemented.
- Wait cursor is implemented.

**21.07.2005**
- Monitor tab UI is implemented.

**16.07.2005**
- RTI interface for event injection is implemented.
- Event Injection UI is implemented.

**12.07.2005**
- Formation Message subscription is completed.

**07.07.2005**
- Automatic casting (scenario distribution) is completed.

**05.07.2005**
- User interface is implemented.
- RTI federation management, declaration management and object management interfaces are implemented.

---

*Modification DTG: 2026-10-18 (UTC+03:00)*


*Updated: 2026-10-18 (Europe/Istanbul).*
