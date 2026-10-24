## EnviFd

Environment Federate (EnviFd) — see its [release notes](EnviFd/ReleaseNotes.md).

- If EnviFd joins after the scenario has started, the Scenario BeginToPlay interaction is not received (to be fixed in ExPFd).
- If EnviFd joins after the scenario has started, the federate's current time starts at the scenario start time; it should be synchronized to the scenario's current time (to be fixed in ExPFd).
