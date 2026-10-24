# MekoFd Known Issues

Current application: **4.0.0 / C# / Stride / Fora**. This page collects unresolved issues and current capability limits. See the [release notes](ReleaseNotes.md#400) for delivered functionality.

## Tracked issues

| ID | Detailed issue |
|---|---|
| HYD-002 | [Vessel-specific parameter and response calibration](Architecture/OpenIssues.md#hyd-002) |
| HYD-007 | [Uncalibrated reverse propulsion and resistance](Architecture/OpenIssues.md#hyd-007) |
| HYD-008 | Resolved for the default training envelope; [retained v7 diagnosis](../Shared/HullCouplingStability.md) and [current acceptance](../Shared/Decisions/ADR-002-Franceschi-Training-Profile.md) |
| COL-002 | [Coordinated physical contact under sparse updates and WAN conditions](../Shared/OpenIssues.md#col-002) |
| ACC-001 | [Deployment, GPU/DPI coverage and sustained-operation acceptance](../Shared/OpenIssues.md#acc-001) |

## Known Limitations

- Working-area readiness validates installed local packages. Only Boston has an authored regional terrain/harbour association; imported ENC starts with an extent-centre reference and explicit chart/sea mode until a scene is registered. Extent centre is not a verified navigable position. The ATD identity card uses source coverage and compilation scale, not full S-52 cell selection. [Scope](../Shared/WorkingAreas.md).

- The shared chart library imports extracted unencrypted S-57 with metre depths and contiguous supplied updates (up to 512 distinct cells). It does not download/check the current publisher catalog, accept S-63, combine separately selected packages or generate a new regional 3D terrain/collision scene. Boston remains the bundled fallback; supported ENC buoys follow an external chart. [Data and 3D boundaries](../Shared/ChartLibrary.md).

- Chart Safety includes continuous straight-motion swept-hull look-ahead and Navigation Officer Ship warnings, including unknown/no-deeper states. It does not calculate tide/squat/live UKC, predict turns/braking, perform full route or isolated-danger checks, or establish measured grounding risk. Conservative overlapping-cell checks, estimated hull margin, full conditional portrayal, large-portfolio performance and persisted safety/appearance settings remain open. [Look-ahead limits](../Shared/ChartLookAhead.md#limits-and-next-work).

- The look-ahead overlay is the latest 1 Hz straight-motion hull sweep, with one representative first-contact marker. Simultaneous contacts are not exhaustively marked; the visual corridor and margin are not surveyed clearance or intended-route geometry. OFF, stale/mismatched contexts and preparation suppress it; clipped contacts require zooming out. [Display behavior](../Shared/ChartLookAhead.md#atd-corridor-and-first-contact-marker).
- ENC LIGHT/DARK/AUTO are simplified training palettes. AUTO uses fixed local simulation hours rather than sunrise/sunset; full S-52 day/dusk/night portrayal and persisted chart-appearance preferences remain open.

- The default v8 is a stable MEKO-sized training surrogate based on Franceschi5415M appended hull data, not real Yavuz trial calibration. The reference reconstruction uses declared supplemental control models and a straightening factor identified from 10/10 zigzag data. [ADR-002](../Shared/Decisions/ADR-002-Franceschi-Training-Profile.md).
- Reverse resistance/installation and real stopping distances remain uncalibrated. [Three-order diagnostics](../Shared/AsternOrders.md) find no numerical/limit violation but retain synthetic sternway equilibria of -6.960/-14.088/-22.529 kn. The FULL ramp softens braking; the estimated reverse machinery program and symmetric hull drag still need an explicit calibration basis. The source-based forward hull replacement does not supply measured MEKO sternway performance or shallow-water/near-quay forces; no artificial astern speed cap is imposed.
- The positive neutral-flow mode belongs to the retained `previous` v7. Current v8 passes 20 sampled calm-water neutral/powered stability conditions from 0 to 27 kn and finite turn-decay checks; this does not prove every loading/environment/governor operating condition.
- The [neutral CPP, braking and sternway flow closures](../Shared/RudderFlowRegimes.md) are implemented and numerically tested but use estimated wake/loss/suction parameters. Unsteady propeller side forces/yaw, reverse stall and near-quay inflow remain unresolved; similar-vessel experiments do not establish Yavuz handling accuracy.
- Heave/pitch are reduced responses; there is no fully coupled 6-DOF seakeeping, validated wind/current/shallow-water force model, CFD wake feedback or measured four-quadrant propeller model. Seabed, light installation, spray and cloth are bounded visual approximations; no NATO lighting certification is claimed.
- Ship contact is a local guard against externally authoritative tracks, without damage or a shared momentum-conserving impact solver. WAN delay/loss, dense contacts and uniform physical correction bounds remain unestablished.
- Radar display scales are equipment-family references, not measured detection performance. CIC ASW remains informational and weapon firing is unavailable. Advisory officer reports are training aids. Helmsman alone executes explicit heading orders through the existing bounded controller; it provides no autonomous route, collision avoidance or berthing. Its warning thresholds are heuristics. Physical heading acquisition is tested ahead in calm water; sternway and severe-environment acceptance remain open.
- RTI acceptance confirms the local send request, not recipient delivery or reading. No recipient/read acknowledgment, automatic replay or persistent message/watch archive is added. A consolidated active-alarm/acknowledgment panel remains open work.
- The current 12-cell Boston portfolio contains four topmarks without associated 3D topmark rendering and three colocated periodic buoy pairs without calendar-based selection. The chart footprint extends beyond the existing CUDEM terrain; no terrain regeneration is implied. [Source limits](../Shared/BostonEncData.md#remaining-source-limitations).
- ENC buoy coordinates, colour/shape codes and supported light sequences are source-derived, but dimensions and fine geometry are estimated. Seasonal replacements, topmarks absent from the package, mooring/collision physics and measured light visibility remain outside the delivered layer. [3D buoy limits](../Shared/EncBuoys.md#dimensions-and-remaining-limits).
- Clean-machine installation, broader GPU/DPI/device coverage, long-duration operation and sustained multi-contact/network resource recovery remain acceptance work.

[Shared open work](../Shared/OpenIssues.md) · [MEKO profile gaps](Architecture/OpenIssues.md).
