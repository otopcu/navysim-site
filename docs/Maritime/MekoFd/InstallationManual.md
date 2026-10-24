# MekoFd installation

Current application: **4.0.0**, Windows x64, C# / .NET 10, Stride / Direct3D 11 and Fora. [User manual](Maritime/MekoFd/UserManual.md) · [Build/package guide](../../../Implementation/FdApps/MekoFd/Code/README.md) · [Release notes](ReleaseNotes.md).

## Runtime requirements

- Windows x64 with a working Direct3D 11 graphics driver.
- .NET 10 Desktop Runtime for a framework-dependent delivery.
- Visual C++ x64 runtime for the bundled native model importer.
- A writable package/cache location and available local assets.
- Fora RTI only when participating in a federation; standalone use is supported.

The current local acceptance package is not yet a clean-machine deployment certification. Hardware/device/DPI coverage and sustained-operation validation remain [open](Maritime/Shared/Validation.md#acceptance-work-still-open).

## Packaged application

Extract the complete delivery to a writable directory. Keep `App`, `Assets` and `Code/artifacts/native-importer` together; do not copy only the executable. First startup prepares local model/shader caches.

```powershell
./Start.ps1 -Offline
./Start.ps1 -Rti localhost:15164 -Federation NSTMSS
```

Select ship/identity/environment in startup configuration. RTI connection is optional and can be made later in F6 Settings. The default Yavuz profile is visual revision 20; the explicit `legacy` profile remains a supported rollback selection.

## Source checkout

Open `Implementation/FdApps/MekoFd/Code/MekoFd.slnx`. A stable .NET 10.0.4xx **SDK**, not only the runtime, is required for compilation and Stride asset building. `global.json` selects it. If missing, use the project-local SDK installer from `Code`, then build normally:

```powershell
./tools/Install-DotNetSdk.ps1
./Build.ps1 -Offline -Locked -Configuration Debug
```

The bootstrap verifies the official archive and uses ignored project-local artifacts; it does not replace the system SDK or PATH. See the [build guide](../../../Implementation/FdApps/MekoFd/Code/README.md) for dependency/bootstrap/package options.

## Troubleshooting

| Symptom | Action |
|---|---|
| No compatible MSBuild during asset build | Check the selected stable SDK from `Code`; run the local SDK installer if needed. Keep normal asset compilation enabled. |
| RTI connection fails | Run standalone or check the server, endpoint, federation and FDD in F6. |
| Federate name already in use | Choose a unique federate name in F6; ship display name is a separate value. |
| Missing model/importer/runtime | Restore the complete package layout and required runtimes; inspect the application log. |
| Startup is slow | The loading window reports preparation stages; first-launch caches can take longer. |

`MekoFd.log` is next to the application and is replaced on startup. Preserve relevant logs before restarting when investigating a failure.
