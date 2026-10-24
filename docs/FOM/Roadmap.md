# FOM evolution roadmap

**Decision: 18 October 2026.** Deliver typed NavySim event injection first. Evaluate NETN and RPR integration in a separate later change; neither family is adopted by the current source edit. [Suite roadmap](../Roadmap.md) · [Current FOM](Fom.md).

## Immediate delivery: typed injection

| Work | Status / acceptance |
|---|---|
| NavySim 5.0.0 typed injection hierarchy, enums and semantics | Imported; schema/semantic and live application checks passed; [contract](TypedEventInjection.md) |
| MekoFdSom/EnviFdSom update and new ExMFdSom | Imported; FAM/repository identities, generated role declarations and HF/UHF links validated |
| Generated FDD and application code | Complete: user export 20261018040130, SimGe 0.5.4 |
| NFL/application import and typed runtime dispatch | Complete: NFL and all three applications use 5.0.0 |
| End-to-end acceptance | Passed: 12 live groups with/without EnviFd, concrete payloads, targets, local recovery, AAR/remote collection and independent clocks |

The coordinated source import is complete. [Export/import and runtime evidence](../../../Implementation/Library/NFL/SimGeSync/20261018040130/runtime-validation.json). Clean-machine deployment and broader training acceptance remain separate work.

## Deferred: NETN alignment

Review baseline: local `Simulation Projects/NETN/Fom` modules inspected for this design. The local NETN-SMC module declares version 1.0 dated 2023-11-20 and belongs to the local NETN FOM v4 set. These are pinned local evidence, not a claim about the newest upstream release.

| Candidate | NavySim use to evaluate | Open design work |
|---|---|---|
| NETN-BASE identity and timing | Persistent entity UUID, interaction UniqueId and SendTime | Map scenario UUIDs and session-local RTI handles; define epoch and units |
| NETN-SMC SMC_EntityControl | Entity-addressed exercise actions | Evaluate a separate extension for NavySim faults/man-overboard; local modules contain no direct equivalents |
| SupportedActions and SMC_Response | Advertise supported actions and report action processing | Define supported-action IDs, correlation, rejection, timeout and retry semantics; RTI acceptance alone is insufficient |
| NETN-ETR DamageStatusReport | Report resulting damage/state | Distinguish a reported state from an injected fault command |
| NETN-LOG Repair task | Deliberate recovery/task workflows | Distinguish repair tasks from immediate fault clearing and local timed expiry |

Keep upstream modules unchanged; place NavySim extensions in separately versioned modules. Select only needed dependencies. Preserve the ship federate's ownership of manoeuvring and its local simulation clock.

## Deferred: RPR alignment

The inspected local RPR-Physical_v3.0 definitions include BaseEntity/PhysicalEntity state, ExtendedDamageStatus, PropulsionSystemsData and Platform damage/mobility state. Evaluate their suitability for entity taxonomy, spatial/velocity exchange and observed damage/propulsion status. These state structures are not an automatic replacement for exercise-injection commands.

Define coordinate frames, orientation convention, velocity semantics, units, stable identity and appearance/damage mappings before replacing the current Frigate model. Retain an explicit adapter for existing NavySim applications during any transition.

## Evaluation gates

1. Pin exact NETN/RPR distributions, module versions, source URLs, license notices and hashes; inventory transitive dependencies and the required IEEE standard profile.
2. Produce a field-by-field mapping from C2SIM/NavySim identity, scenario/task/event and vessel state to the selected modules. Document gaps and extension ownership.
3. Decide UUID/RTI-handle resolution, action capability discovery, responses and fault lifecycle. Do not infer delivery, application acknowledgement or deduplication from a correlation field.
4. Build one isolated adapter/prototype with unchanged upstream XML and explicitly versioned extensions. Validate composition, codecs, sharing and DDM semantics.
5. Test cross-implementation exchange and failure cases before committing to a breaking cutover. Record acceptance evidence and update FDD release notes.
