# KnoxFd user manual

Start `Implementation/FdApps/KnoxFd/Code/src/KnoxFd.App/bin/Release/net10.0-windows/KnoxFd.App.exe`, or use `Code/Run.ps1 -Offline`. Open `Code/KnoxFd.slnx` and select `KnoxFd.App` for development. `Code/Build.ps1 -Offline` builds the shared maritime solution.

The default vessel is **TCG Akdeniz F257**, using the adapted existing Knox model and its national flag. Sea/weather controls, radar, messages, camera controls and other common panels work through the same host as MekoFd; see the [common operator controls](../MekoFd/UserManual.md).

Seven OOW presets are available. The current Knox visual has no approved walking surface or articulated weapon/shaft bindings, so MEKO-specific equipment/locations are not offered as Knox equipment. Knox own ship is offline-only under the current federation adapter. Maneuvering uses an inherited, unvalidated reference; the model is not a calibrated representation of Knox machinery or handling. See [shared architecture](../Shared/Modules.md).

[Vessel architecture](Architecture.md) documents the Akdeniz livery and current module capabilities.

[Known issues and capability limits](Maritime/KnoxFd/Known%20Issues.md) · [Release notes](Release%20Notes.md).
