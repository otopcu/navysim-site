# ExMFd Known Issues — 4.0.0

- Supports the NavySim C2SIM profile, not every C2SIM task/server. NSDL/DataSet loading is archived.
- Live acceptance covers one MEKO per allocated federate. Knox discovery alone does not establish own-ship support. Routes, STG/OTC and conditional objectives are outside the profile.
- The FOM has no application receipt or event-ID deduplication. RTI acceptance is not confirmed application. Multi-target distribution is not atomic; explicit retry can duplicate an uncertain send.
- Scheduling is local, not HLA time management. Network delay affects event arrival; no globally synchronized physical history is promised.
- Course/speed are deliberately not distributed. OOW retains manoeuvring. New run does not reset motion or reposition already-begun ships.
- Failures expire on ship-local time while ExMFd is paused/absent. Recovery rows mean expected expiry, not confirmed repair; no recovery interaction is invented.
- EnviFd is optional. Multiple weather publishers use last-received supplied-field semantics without controller arbitration.
- Man-overboard with explicit Port/Starboard is an HF received message, not a person model or recovery objective.
- Reports/journal are memory-only until export. Loading another package clears collection; normal Disconnect retains the last report.
- At most 100,000 messages/positions are retained and 1,000 shown. Counters remain cumulative; exports cover retained rows.
- Ship reporting defaults to one minute after Begin on its own clock. HF failure suppresses reports.
- PDF uses an installed Windows PDF printer. Historical templates and continuous database logging are not restored.
- Cross-UTM-zone operation, vessel calibration and clean-machine deployment require separate validation.

[Manual](UserManual.md) · [Architecture](Architecture.md) · [Release notes](ReleaseNotes.md).
