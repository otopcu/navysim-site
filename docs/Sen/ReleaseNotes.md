# Sen Release Notes

**Current version: 3.0.0 (NavySim 2026.1, unreleased).** Scenario Manager continues former GSEd; version comes from Implementation/Tools/Sen/Version.props. .NET 10 / C# 14 / Windows WPF.

[Manual](UserManual.md) · [Architecture](Architecture.md) · [Install](InstallationManual.md) · [Known issues](Known%20Issues.md) · [Suite](../ReleaseNotes.md).

## [3.0.0] — Unreleased

### Infrastructure

- SDK-style .NET 10 app and UI-independent Management library, grouped under Tools/Sen; common scenario code under Library/Scenarios. Stable SDK 10.0.4xx, no RTI dependency.
- Removed active NSDL/.sprj typed DataSets, Windows Forms timeline and legacy import scaffolding. Historical code/fixtures are archived outside Code; [old NSDL architecture](Architecture/LegacyNSDL.md) is preserved.

### Scenario authoring

- Adds a Black Falcon Berth 7 MEKO berthing template, bundled C2SIM package and detailed-map shortcut. Shares the berth/initial-position definition with MekoFd's 3D and collision surface. Calm SS1 exercise retains OOW control of machinery and heading; authored heading/speed are references. [Berth model](../Maritime/Shared/BlackFalconBerthing.md).

- Editable C2SIM metadata/UTC time, vessel UUID/allocation/identity/position/heading/speed, SS/wind and timed weather/failure/Man-overboard events. Blank wind preserves preset intent; explicit zero is retained.
- Pinned upstream 1.0.1 XSD and separate NavySim profiles 1.0.0 / 1.1.0; full source/field validation, persistent UUIDs, unsupported-content rejection and read-only XML preview.
- Validated open/save, dedicated two-file package folders, staged writes with ordinary-error rollback, failed-open preservation and unsaved-change prompts.

### UI and validation

- Adopted ExMFd presentation across the designer, table editor and Open/Save dialogs: rounded buttons, unified tabs, dropdowns, text fields, selection and table headers. Resources and monitor-aware window handling now live in Library/DesktopUI.
- Integrated minimize/maximize/restore/close into the application header; retained native dragging, double-click and resizing. Saved/unsaved badges reflect document state. Editable cells, keyboard selection and unsaved-change protection remain active.
- Passed 24 existing Sen checks, focused native-window/dropdown/dialog/table checks and ExMFd window/injection regressions. [Evidence](../../../Implementation/Library/DesktopUI/Validation/sen-modern-ui-20261018.json).

- Associated supporting-data files with the entry filename (`Hawaii.xml` / `Hawaii.NavySim.xml`); entry renames update both names and the XML reference. Legacy navysim.xml packages load and upgrade on save. Supporting-data selection produces a clear ENTRY diagnostic.
- Added a project browser for Open, with folder navigation and supporting-data files excluded from the list.

- Default Open / Save as uses the Windows Documents known folder plus `Scenario Projects`, respecting OneDrive redirection without a Scenarios subfolder. Save as accepts a project folder and XML entry filename; reopening and subsequent saves retain that filename. Renaming an existing entry first validates the two-file package and continues to protect unrelated folder contents.

- First Save / Save as now accept a scenario name and destination, with an automatically suggested package folder. The title is persisted in Metadata; cancel and failed saves retain the current document name/location. Existing package replacement is confirmed.

- Start maximized on the monitor containing the mouse pointer, with native monitor placement rather than virtual-desktop centering.
- Startup/New now use the shared Boston Harbor authoring workspace: stationary TCG Yavuz allocated to `MekoFd`, 30 minutes, SS3 and no events. Fresh UUIDs and a validated packaged example are included. The Hawaii example remains explicit; existing projects retain their positions. MekoFd now includes the matching measured NOAA CUDEM land/seabed package and shared geographic frame.
- Extends the offline Boston map with NOAA US5MA11M inner-harbor coverage and .001/.002 updates, plus the same municipal building/OSM pier polygons used by MekoFd 3D. Preserves source IDs, height estimates and visible attribution; includes source/license notices in output/publish. The tile57 single-cell comparison adapter explicitly rejects composite overlays.

- Connected the classic three-pane designer to real C2SIM authoring: project tree/toolbox, scenario cards and contextual Properties, Open/Save/Save as/Validate, copyable feedback and unsaved-change prompts. This is now the default UI; the earlier table form remains available with `--editor`.
- Added a shared event-type dropdown with relevant parameters only: MOB Port/Starboard, engine groups, radio channels and rudder duration. Scheduled MOB and failure descriptions round-trip through the additive profile 1.1.0.
- Added typed weather/component/target selectors, persistent UUID targets through vessel renames, unique identities for mixed-class additions and guarded removal of referenced ships. Invalid numeric buffers persist across selection changes and prevent save.
- Event Timeline scales actual elapsed times and failure durations against scenario duration, with stable explicit sorting. XML Preview generates the validated two-file package and invalidates stale output after edits. Sandbox uses the shared Library/Geography foundation: real bundled NOAA ENC / OSM geography, optional online OSM/OpenSeaMap, pan/zoom, picking and single-use initial-position placement. Inspector values, dirty state, UUIDs and C2SIM persistence remain synchronized. Removed active dummy data and fake chart geometry. [Designer guide](../../../Implementation/Tools/Sen/Code/DesignerPreview.md).
- Twenty-four Sen checks cover authoring/save/reopen, Unicode/UUID/nulls, save/open failure safety, actual WPF interactions, hidden invalid fields, timeline scaling and semantic schedule rejection. [Working UI captures](../../../Implementation/Tools/Sen/Design/Designer/README.md). Prior shared parser/coordinator and real-RTI execution evidence remains in the [migration snapshot](../../../Implementation/Library/Scenarios/Validation/c2sim-migration-20261018.json).
- Routes/condition authoring, full C2SIM task interchange and automatic NSDL conversion remain outside this release profile.

## Historical GSEd releases

Historical source: *RN GSEd.docx* and *READMEEEE.txt*; source document date August 22, 2013. Entries below describe those releases, not new 3.0.0 functionality.

## [2.1.0] - 2010-01-04

**04.01.2010** — *Okan TOPÇU*
- Compiled on Windows 7.
- Compiled with MS Visual Studio 2010 Beta 2.

---

## [2.0.0] - 2007-12-20

**20.12.2007**
- Compiled on Windows Vista Ultimate.
- Compiled with MS Visual Studio 2008 Pro.

---

## [1.0.1] - 2006-09-23

**23.09.2006**
- Compiled on Windows Vista Ultimate RC1.

**10.07.2006**
- XML View tab is implemented.

**14.05.2006**
- Event Target and OTC Ship combo box bug is fixed.

---

## [1.0.0] - 2006-03-26

**26.03.2006**
- Toolstrip menu is implemented.

**20.03.2006**
- Adding and deleting ships and events in the scenario is implemented.
- Static scenario elements (e.g., metadata) are created automatically for new scenario files.
- "Save As" dialog is implemented.
- 32×32 and 64×64 icon library is created.

**18.03.2006**
- Scenario properties panel functionality is implemented.
- Open/Save functionality is implemented.
- Basic user interface is implemented.

---

*Modification DTG: 2026-10-18 (UTC+03:00)*


*Updated: 2026-10-18 (Europe/Istanbul).*
