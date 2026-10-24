# MekoFd Release Notes

| **Current version** | **4.0.0**                      |
| ------------------- | ------------------------------ |
| **Suite release**   | NavySim 2026.1, in development |

## [4.0.0] - Unreleased

Version 4.0.0 introduces a modern Windows application, expanded ship handling, geographic navigation displays and a more detailed Yavuz-class visual model.

### Infrastructure

- Modernizes the application for Windows x64 with .NET 10 and Stride / Direct3D 11 graphics.
- Improves startup with model caching, visible loading progress and cancellation.
- Retains standalone operation alongside optional federation connectivity.

### Environment

- Makes **Boston Harbor** the default operating area, with NOAA land/seabed terrain, harbour buildings and piers aligned with the navigation chart.
- Adds a spectral sea with **Sea State 0–9**, editable significant wave height, peak period and wave direction, and Bretschneider/JONSWAP selection.
- Applies reference wind speed when a sea-state preset is selected. A separate wind-speed update overrides that preset value; independent wind changes leave the selected sea state intact.
- Improves bow waves, stern wash, propeller jets, foam and spray. Nearby moving contacts also produce visible wakes.
- Refines underwater visibility, sky/sea reflections, distant horizons, shoreline appearance and explicit fog.
- Adds **3D ENC buoys within 2 NM**, with chart-derived colours, shapes and light sequences, and wave-driven motion at their chart positions.
- Adds separate underway and harbour lighting programs, automatic day/night switching, navigation/anchor/alongside combinations, and **DARKEN SHIP / NORMAL LIGHTS** controls.

### Hydrodynamics & Maneuvering

- Introduces coupled surge, sway, roll and yaw handling, with reduced heave and pitch responses to waves.
- Uses a directionally stable MEKO-sized training profile based on a comparable combatant hull. This remains a training approximation rather than a model calibrated to Yavuz sea trials.
- Models port and starboard CPP shafts independently, including RPM, pitch, torque, power availability and differential-thrust turning.
- Refines rudder response during headway, neutral-pitch coasting, reverse-pitch braking and established sternway. A STOP engine order does not remove rudder authority while water is still flowing past the rudders.
- Keeps CPP shaft rotation positive during powered astern operation and retains passive windmilling after declutching.
- Adds configurable connected-neutral or declutched STOP behaviour and crash-stop demand profiles, with finite pitch/RPM response and machinery limits.
- Separates ahead and astern pitch/RPM programs and provides an optional docking-training program for finer low-order astern control.
- Improves heading acquisition with turn, check-swing and capture phases, including consistent turn direction for a 180° course change.
- Preserves independent machinery failures and recovery: a failed shaft does not disable the healthy shaft.

### Navigation & Collision Handling

- Integrates NOAA Boston Harbor ENC into a **chart-first ATD**, alongside a live OOW view and permanent TRD/ATD navigation.
- Adds a chart library for importing extracted **S-57** packages, selecting an active chart and restoring Boston. Chart and 3D buoy positions remain aligned.
- Adds **LIGHT / DARK / AUTO** chart appearance and a separate **DEPTHS ON / OFF** control for sounding numbers.
- Adds **Inspect chart** for buoys, lights, soundings, depth areas and quays, with source-cell and feature information. Inspection is separate from pin placement.
- Shows independent **PIN** and **CURSOR** true bearings, ranges from own ship and geographic coordinates. Pinned positions remain fixed as the ship moves or the display zooms.
- Adds **Safety Contour** and **Safety Depth**, showing requested and applied contours separately, with clear feedback when chart coverage is unavailable.
- Adds a configurable shallow-water look-ahead watch, Navigation Officer warnings, a charted assessment corridor and a marker for the first predicted shallow contact. These are advisory aids, not grounding prevention or tide/squat/under-keel-clearance calculations.
- Preserves trail history across centers and zoom changes. Selecting NONE hides the trail while recording continues; FULL restores the retained history.
- Refines **TRD** as a navigation-radar display with a rotating sweep, scan-lit coast/contact echoes, range rings, bearing scale and heading line. GREEN, AMBER and MULTI palettes and selectable echo persistence are available.
- Adds rotary **EBL / VRM** controls with mouse-wheel and drag adjustment, stepped radar ranges and corner readouts for measurements and selected contacts.
- Adds hull-to-hull clearance and closing/opening reports, alongside close-contact and CPA/TCPA warnings.
- Adds the **Black Falcon Berth 7** training area with an aligned quay, fenders, bollards and ladders, plus a matching berthing scenario.
- Prevents local ship interpenetration with hull contact response while allowing tangential sliding and backing clear. Fixes head-on overlap between two independently controlled ships.
- Adds fixed-quay and compliant-fender contact. General terrain collision, damage and mooring-line dynamics are not included.
- The chart and radar displays are training aids; no ECDIS or ARPA certification is claimed.

### UI Controls

- Refreshes the startup wizard, control centers, full-screen/resolution controls and digital simulation clock, with sharper text and consistent navigation shortcuts.
- Adds a sliding left control console and an independent **Status Messages** drawer on the right, closed by default. Closing either drawer expands the main view.
- Makes **F8** hide both side panels and restore their previous states without losing the selected center, measurements or message drafts.
- Adds a default-open **INSTRUMENTS** bar. Closing it expands the main view and leaves a translucent, read-only strip of engine orders and ordered/actual rudder angles.
- Replaces the lower EOT buttons with horizontal detented levers: **STARBOARD green above PORT red**, with independent drag and mouse-wheel control.
- Adds a bridge-style rudder display with separate **ORDER** and **ACTUAL** indications, red port/green starboard sectors, 5° manual steps through **±35°**, and MIDSHIPS.
- Integrates heading-focused **Helm Control** into the left SCC panel, with a heading tape, course entry, **Steady on course** and **Steady as she goes**.
- Keeps **OOW EYE** true look bearing visible at the upper-left of the main view across centers.
- Adds a modern Settings popup for sound, visuals, weather, ship lights, RTI connection and automatic follow-up. **Sound is off by default.**
- Adds startup working-area selection with separate ENC, terrain and harbour readiness indicators. Areas without a 3D package can continue with chart and sea.
- Adds **F9 / Mission** for briefings, orders and readiness information, and **F10 / Weather** for wind, sea state, wave conditions, clouds, fog and environmental time.
- Adds All/System/RTI/Ship message filters, full message details and filtered text copying.
- Shows ship reports above the instruments for **3 seconds**, with priority handling and queued messages, even when the Status Messages drawer is closed.

### Observer & Camera Controls

- Adds eight Yavuz observer locations, including the bridge interior, with a standing eye position and full ship-motion following.
- Supports right-mouse look from fixed observer locations across all centers while preserving the observer's position.
- Adds **FREE FLIGHT** with mouse look, WASD/QE movement, speed boost and wheel-based near/far movement.
- Provides **FOLLOW SHIP**, **FRAME SHIP** and **RETURN STATION** controls.
- Adds bounded **WALK** on the quarterdeck, forecastle and bridge, with movement along deck slopes and around equipment.
- Adds a ship-specific station illustration with viewpoint callouts, walking areas and the current observer position.

### Communications & Crew Reports

- Adds a **Helmsman** that engages on explicit heading orders and releases immediately when the user takes manual rudder control. Reports identify acquisition, unavailable steering, low inflow and failure to converge on the ordered course.
- Improves Message Center editing, archive browsing, Unicode input, scrolling, draft retention and protection against duplicate sends.
- Shows distinct outgoing-message states: **QUEUED**, **RTI ACCEPTED**, **SEND SKIPPED**, **NOT SENT** and **RESULT UNKNOWN**. RTI acceptance does not mean recipient acknowledgement or reading.
- Adds role-specific reports from the Navigation Officer, CIC Officer, Chief Engineer, Communications Officer and Meteorology Officer.
- Reports contacts, clearance and closing rates, headway/sternway, machinery orders, failures/repairs, communication outcomes and effective weather changes, with reduced repetition.
- Adds **PA Ship Stations** calls for Navigation and Manoeuvring routines, with English announcements and retained text reports. Sound OFF cancels speech without removing the text.

### Ship Models & Rendering

- Adds a more detailed Yavuz-class model with refined freeboard, hull silhouette, bridge wings, working wells, ship's boats, anchors, launchers, radars and underwater appendages.
- Refines forebody flare and foremast yards, platforms, mast-head fittings and antenna detail from photographic references.
- Improves funnel geometry, hangar fittings, aft director supports, service equipment, stern safety nets and open lower working-deck apertures.
- Improves hull/upperworks paint separation and matte deck finish, reducing visible texture repetition while retaining flight-deck markings and ship identity artwork.
- Improves bridge-glass reflections at different viewing angles while preserving clear OOW visibility by day and night.
- Animates the two own-ship propellers from their independent shaft RPM, including CPP astern and passive windmilling. Visual blade pitch remains fixed.
- Adds twelve national flag textures with startup/assignment selection and apparent-wind-driven cloth motion.
- Adds Standard/High visual quality, smoother thin fittings and distance transitions, and more stable doors, markings and equipment surfaces. Corrects visible shadow bands on the hull.
- Retains the legacy ship appearance as an alternative. Detailed geometry and fittings remain photographic approximations rather than surveyed naval drawings.

### Federation & Interoperability

- Integrates with the NavySim federation through Fora, including scenario assignments, contacts, weather and tactical messages.
- Supports background connection, cancellation, disconnection and reconnection. Failed connections or transport loss preserve local ship operation.
- Uses ship identity as the default federate name and provides duplicate-name feedback.
- Receives initial identity, position and true heading through task orders before exercise start. Late or repeated assignments do not relocate an already running ship, and assignment alone does not engage course hold.
- Receives targeted **Man Overboard**, **Engine Failure**, **Rudder Failure** and **Radio Failure** injections with the applicable side, machinery group or channel.
- Receives Sea State 0–9 and independent weather changes from the exercise environment, with explicit wind updates taking precedence over preset wind values.
- Keeps the ship's simulation clock and machinery independent of the Exercise Manager's pause, stop or disconnection.

---

## [3.0.0] - 2008-09-28

**By:** Okan TOPÃ‡U

**28.09.2008**
- Compiled with MS DirectX SDK (August 2008).
- The type of the TOA and TOD scenario elements is changed to `DateTime`.

**22.09.2008**
- `NFL::Types::SLatLong` is integrated.
- `NFL::Utilities::FederateClock` is integrated.
- Integration of `NFL::Types::SeaState`, `Fog`, `FederateStates` and `FrigateClasses` is done.

**20.12.2007**
- Compiled on Windows XP Pro SP2.
- Compiled with MS Visual Studio 2008 Pro SP1.
- Compiled with MS DirectX SDK (November 2007).

---

## [2.2.1] - 2006-11-11

**By:** Canku Alp CALARGUN â€” Canku's thesis

**11.11.2006**
- Implementation of the wave model.
- Implementation of the wave shading model.
- Implementation of the ship's wake model.
- Implementation of cloud simulation.
- Implementation of the 4-DOF hydrodynamic model.

---

## [2.2.0] - 2006-09-12

**By:** Okan TOPÃ‡U

**12.09.2006**
- Ship view with minimal displays is implemented.

**10.09.2006**
- Classes are redesigned and implemented.
- DirectInput is used for keyboard and mouse events.

**30.08.2006**
- About dialog is implemented.
- `cout` calls are replaced with `Console::WriteLine` calls.

---

## [2.1.2] - 2006-08-19

**By:** Okan TOPÃ‡U

**19.08.2006**
- MekoFd became generic so that it can also act as KnoxFd.
- Start-up configuration wizard is implemented.

**11.08.2006**
- C3D and CUI type classes are simplified by combining the derived types into one class.
- Bug fixed: *"The artillery of all the frigates in the scene graph are controlled at the same time"* â€” fixed by cloning the Meko polygon set.
- The scene graph array structure is replaced with pointers connected to the track list.
- TSS track list is re-implemented as a `BindingList` structure.
- Bug fixed: *"Chimney smoke still exists after ship is resigned from federation"*.

**05.03.2006**
- Compiled with SGI OpenGL Performer 3.2.2.

---

## [2.1.1] - 2006-02-11

**By:** Okan TOPÃ‡U

**11.02.2006**
- NSTMSSComponents `CScenario` class is implemented.
- `CFrigate` abstract class is removed from the code.

**02.11.2005**
- Compiled with MS Visual Studio .NET 2005.
- Splash screen is implemented.

---

## [2.1.0] - 2005-10-07

**By:** Okan TOPÃ‡U

**07.10.2005**
- Most of the classes are re-implemented as MS Managed C++ classes.
- Status messages list is re-implemented using a `BindingList` data structure.
- Emergency event injection timers are enhanced.

**24.09.2005**
- Compiled with SGI OpenGL Performer 3.2.1.
- Scenario file and DLLC updates are implemented.

**27.08.2005**
- Weather Report interface is implemented.
- Compiled with MS Visual Studio .NET 2005 Beta 2.
- Radio failure event response is implemented.

**21.07.2005**
- RTI interface for ship status reporting is implemented.

**16.07.2005**
- RTI interface for event injection is implemented.
- Injection response functionality for rudder malfunction is implemented.

**15.07.2005**
- Scenario settings are implemented (i.e., ship name and posture are set).

**06.07.2005**
- RTI interface for TaskOrd is implemented.
- A few attribute-update bugs are fixed (e.g., the class attribute was sent all the time; now it is sent only when it is set).

**23.01.2005**
- Ship's smoke (from chimneys) is implemented.

**20.01.2005**
- Simple collision detection (intersection testing) and response routines are implemented.
- Maximum screen width and height capability is checked before setting the application resolution.
- Settings tab functionality (environment controls) and About tab are implemented.
- CTI and status interface tabs are redeveloped as `.flt` files.
- Compiled with SGI OpenGL Performer 3.2.

---

## [2.0.1] - 2005-08-23

**23.08.2005** â€” *AslÄ± KILIÃ‡*
- Implementation of the world coordinate system.
- Implementation of the body coordinate system.

**06.09.2004** â€” *Okan TOPÃ‡U*
- SeaState attribute of the HLA Environment object class is received via the RTI.
- Sea state, TOD and fog status are redesigned and implemented.
- Some ATD functionality is implemented (tracing, UI viewports, mouse coordinate orientation, scrolling and zooming).
- Imitation of the roll and pitch effect (sea state) is implemented.
- The distance travelled by the ship is calculated.
- Turret controls (up/down and right/left) for the 5/54 and Sea Zeniths are implemented.
- New OOW transportation positions (6 and 7) are added.
- Changeable viewport interface tabs are redeveloped as `.flt` files.
- Compiled with SGI Performer 3.1.1.
- OOW eye bearing (true) is printed on the CTI screen.
- Exception handling for memory exhaustion is added using `assert` functions.
- Status-message display UI is enhanced (up-page and down-page icons added).
- Status-message viewport classes are implemented.
- Status messages are implemented using a doubly-linked list.

---

## [2.0] - 2003-10-04

*Main release for NSTMSS 4.0*

**By:** Okan TOPÃ‡U

**Platform:** Windows 2000/XP Pro Â· SGI OpenGL Performer 3.0.2 Â· DMSO RTI-NG 1.3v6 Â· MS Visual Studio .NET

**06.06.2004**
- Message history capability is implemented.
- The doubly-linked list is redesigned as generic.

**04.10.2003**
- Classes are redesigned and re-implemented.

---

## [1.2] - 2002-10-31

*Main release for NSTMSS 3.0*

**Release date:** 31.10.2002

**Platform:** Linux RH 7.3 Â· SGI OpenGL Performer 2.5.2 Â· DMSO RTI-NG 1.3v6

**23.10.2002**
- Radar functionality is implemented. The radar tracks other ships.

**19.09.2002**
- Singly-linked list is implemented for the TSS ghost paradigm.

**14.09.2002**
- Command-line interface is implemented.

**12.09.2002**
- Simple hydrodynamic model is implemented.

**14.07.2002**
- Fully OpenGL-integrated GUI is implemented.

**12.05.2002**
- `Meko.flt` polygon model improvements.

---

## [1.1] - 2001

*Main release for NSTMSS 2*

**Release date:** 2001

- Runs on RH Linux 7.1 with RTI-NG 1.3rel3.1.

---

## [1.01] - 2001-09-03

*Main release for NSTMSS 1.3*

**Release date:** 03.09.2001

**27.08.2001**
- Message Center UI enhancements:
  - The writing column is now marked with a shadowed rectangle, so the user can see where she/he will write.
  - The shadow moves with the TAB key or a mouse click.
- Minor code optimization to remove compiler warnings.

**26.08.2001**
- Enhancements to the `msgView.cpp` geometric polygons (position and size of the message rectangle changed).
- The Message Center automatically fills the "FM" header with its ship name; the user cannot modify it.

**25.08.2001**
- Message center frustum changed to ORTHO instead of an FOV frustum.
- Messages are rendered with OpenGL calls instead of Performer `pfDrawMessage` calls.

**23.08.2001**
- OOD positioning for the right and left sides is implemented; the OOD can now tele-transport to both sides.
- F-keys are re-assigned to tele-transport the OOD.

---

## [1.0] - 2000-01-15

**15.01.2000**
- The KNOX code is almost entirely reused in the MEKO code.

## Version summary

| Version | Latest recorded change | NSTMSS release | Platform | By |
|---|---|---|---|---|
| 4.0.0 | Unreleased | 2026.1 | C# 14, .NET 10, Windows x64, Stride / Direct3D 11, SimGe-generated Fora | Okan TOPÇU |
| 3.0.0 | 28.09.2008 | 5.1 / 5.2 | Windows XP Pro SP2, VS 2008 SP1, DirectX SDK (Aug 2008) | Okan TOPÇU |
| 2.2.1 | 11.11.2006 | 5.0.1 | | Canku Alp CALARGUN |
| 2.2.0 | 12.09.2006 | 5.0 (v2.2.x) | | Okan TOPÇU |
| 2.1.2 | 19.08.2006 | — | OpenGL Performer 3.2.2 | Okan TOPÇU |
| 2.1.1 | 11.02.2006 | — | VS .NET 2005 | Okan TOPÇU |
| 2.1.0 | 07.10.2005 | — | OpenGL Performer 3.2 / 3.2.1 | Okan TOPÇU |
| 2.0.1 | 23.08.2005 | 4.2 | OpenGL Performer 3.1.1 | Aslı KILIÇ, Okan TOPÇU |
| 2.0 | 04.10.2003 | 4.0 | Windows 2000/XP, Performer 3.0.2, DMSO RTI-NG 1.3v6, VS .NET | Okan TOPÇU |
| 1.2 | 31.10.2002 | 3.0 | Linux RH 7.3, Performer 2.5.2, DMSO RTI-NG 1.3v6 | Okan TOPÇU |
| 1.1 | 2001 | 2.0 | RH Linux 7.1, RTI-NG 1.3rel3.1 | Okan TOPÇU |
| 1.01 | 03.09.2001 | 1.3 | — | Okan TOPÇU |
| 1.0 | 15.01.2000 | 1.1 | — | Okan TOPÇU |

The version summary retains the historical NSTMSS release associations.

