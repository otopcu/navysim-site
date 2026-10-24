# MekoFd User Manual screenshot sources

Captured **2026-10-12** from the real C# / Stride application and local ship/terrain assets. These images replace historical C++ screenshots in the [current user manual](Maritime/MekoFd/UserManual.md).

- Source revision: NavySim `92ce79788a9059a15afcee143955537c860bd0d7`, plus the current Hawaii material modernization and the screenshot-fixture-only `ALL MEKO` → `ALL` correction in `MessageVerification.cs`.
- The original set was recaptured from the same final build after the terrain/fixture changes; About and the three navigation views were subsequently refreshed; two non-skid deck close-ups were added from their respective 4.0.0 builds below. The addressing correction changes sample text, not delivery behavior.
- Build: Release / `net10.0-windows`; final application build succeeded with 0 warnings and 0 errors.
- Images are complete window/render captures. Wizard/About use the actual WinForms controls; runtime views use Stride output. No UI was painted over the images.
- All captures are offline except `fora-connected.png`, which uses a separately launched local Fora server on FP 25164 / HTTP 27112 and a unique federation. The application joined, rendered 120 frames, resigned, destroyed its federation and disconnected. The isolated server was then stopped.
- Offline contacts/messages/failures are demonstration data. The edited KNOX wizard example is offline.
- Existing historical images are retained for other documents; the new manual uses only this folder.

## Build fingerprint

These hashes identify the original capture build, except for the subsequent About/navigation refreshes documented below.

| File | SHA-256 |
|---|---|
| MekoFd.App.exe | `aea513c4366de2e30df1a8dfe3bb43d1cc1f55cc72fa604340b7452ff73068fb` |
| MekoFd.App.dll | `2154ecebc2105c6382951b5e932a39999cb7fb9f445d6d2069627ca260afc81c` |
| MessageVerification.cs | `79f1d239b3dcdf857a7cc2e1011e41473db2cf79bb4a8859d0738ad1a4bafec0` |
| MekoFd.Rendering.Stride.dll | `12037791e4c6fde203155c005ac293aceee2bd75295129a799e14f5d6c0dd27f` |
| coastal-scrub.png | `08d5d90fa89784dfbbef0fae3e7af27fbf71a7d0276f9c9cc52508ce44529b6a` |

## About refresh — 4.0.0

Captured from the actual WinForms dialog after the version update. Build and assembly metadata checks passed; the displayed version is 4.0.0. Other images retain their original capture provenance.

| File | SHA-256 |
|---|---|
| MekoFd.App.exe | `794145f755a2a702701ebeeb1e6e0e03aee101a0c2d5d96f62acc989d5d3dcd7` |
| MekoFd.App.dll | `a01d2877e7dbcf07ddae442b5c76f1a5236fdd0d63b9b1e278762181e1eced7c` |

## Navigation refresh — own-ship center

The three navigation images are actual Stride captures from the updated 4.0.0 Release build. Nine radar/mast cases completed 270 frames and clean exit, including the new startup position and moving own ship. All 59 local parity groups passed. The ATD image shows the relocated ship; TRD and zoom/pin use controlled origin-based fixtures. Other images retain their recorded provenance.

| File | SHA-256 |
|---|---|
| MekoFd.App.exe | `794145f755a2a702701ebeeb1e6e0e03aee101a0c2d5d96f62acc989d5d3dcd7` |
| MekoFd.App.dll | `f0c716566629c60c47d0380e741b9644048a8ab5c5bcdc48c888b196b87af4e4` |
| MekoFd.Rendering.Stride.dll | `21e998ee703e96c738803e0bfc11f3e7d1dc8d26390200662aedc36507ec1722` |
| MekoFd.Simulation.dll | `4d40155241c94b8582e1b681e1b9b11a0fbfe6529c84007464cd55cbe9525e07` |

## Non-skid deck close-ups — 4.0.0

Two additional actual Stride captures document the new walking/flight-deck coating. The Release build passed; all 60 parity groups and 18 ship views / 540 frames passed, including distance, sunset and night. Sixteen comparison views were captured before the change. The screenshots are controlled offline views of the original MEKO geometry. Coating source references are recorded in `Implementation/FdApps/MekoFd/CSharp/src/MekoFd.Rendering.Stride/Resources/Ship/SOURCES.md`.

| File | SHA-256 |
|---|---|
| MekoFd.App.exe | `794145f755a2a702701ebeeb1e6e0e03aee101a0c2d5d96f62acc989d5d3dcd7` |
| MekoFd.App.dll | `84b9f03b609fe127117049cda203044cd2f57ae74ea949c0b8b780ce18f46314` |
| MekoFd.Rendering.Stride.dll | `035bb51cd5bb76001322223dea5bfd47a9d36d181731f623abe89f067bb708f4` |
| MekoFd.AssetPipeline.dll | `e22a1b37854740a05bd524579f188beaffaa6b22948e0e6d892bfa2d98a2aa3e` |

## Capture modes and checks

| Group | Successful result |
|---|---|
| Wizard / About | Configuration and About captures saved |
| Overview | Rendered 120 frames |
| Settings | Rendered 220 frames |
| Radar | Original set: 210 frames; navigation refresh: nine cases / 270 frames |
| CIC | Rendered 360 frames |
| Transportation | Rendered 360 frames |
| Messages | Rendered 270 frames |
| EOT | Rendered 90 frames |
| Island terrain | Rendered 150 frames |
| Connected Fora | Rendered 120 frames; client Info diagnostics and successful RTI cleanup verified |

## Image manifest

Times below are source-file timestamps in local time. Capture flags are developer verification options, not ordinary exercise launch instructions.

| Image | Size | Capture time | Mode | SHA-256 |
|---|---|---|---|---|
| [overview.png](overview.png) | 1024×768 | 2026-10-12T21:19:54 | `--offline --no-dialog --frames 120 --capture` | `8bae19f58399cdc5ae51135c5187d2e749ed0d6418235686b1652136a31afbe3` |
| [configuration-ship.png](configuration-ship.png) | 916×643 | 2026-10-12T21:19:46 | `--offline --no-dialog --verify-ui` | `cf6479e2f46a5c16518ff13b298fe6a5d6d20a8b6a9dd053a53e1894851b3238` |
| [configuration-environment.png](configuration-environment.png) | 916×643 | 2026-10-12T21:19:46 | `--offline --no-dialog --verify-ui` | `ed20a41213db7749c75da111ed751366a2aa194f7dc85d4b1052b1cfb6d4e12a` |
| [configuration-review.png](configuration-review.png) | 916×643 | 2026-10-12T21:19:46 | `--offline --no-dialog --verify-ui` | `f4ebd8a5dadfcba92dfcbcb596352f7a2b1e9d9c9d5b27736635f5b2bac10f50` |
| [instruments-underway.png](instruments-underway.png) | 1024×768 | 2026-10-12T21:21:03 | `--offline --no-dialog --verify-eot` | `aa484af4e7f3e9df78ed68aebbf2c791c05a9dce9c3ac10f781f5a2f88f0856d` |
| [view-displays-only.png](view-displays-only.png) | 1024×768 | 2026-10-12T21:21:04 | `--offline --no-dialog --verify-eot` | `5b8fa6bee0d634afacc76954f0877b29bcfdd0a3b0be9391c138e6b7e99e0904` |
| [ship-controls-locked.png](ship-controls-locked.png) | 1024×768 | 2026-10-12T21:21:04 | `--offline --no-dialog --verify-eot` | `1de5432cb22bcf359c9f44b0d71ff7799bf4f6c5634ac036e5f0996453bfdd54` |
| [messages-archive.png](messages-archive.png) | 1024×768 | 2026-10-12T21:20:52 | `--offline --no-dialog --verify-messages` | `a89dbed9c7565a0d03ecb7d6ae9dc1ecab190babcf4cb3dff8cb445a8b04627e` |
| [messages-compose.png](messages-compose.png) | 1024×768 | 2026-10-12T21:20:52 | `--offline --no-dialog --verify-messages` | `05e209e35348b7f5a706395d76bb2b01f9cca0784f2788e780315f2ed3dd9d99` |
| [messages-uhf-offline.png](messages-uhf-offline.png) | 1024×768 | 2026-10-12T21:20:53 | `--offline --no-dialog --verify-messages` | `d5b69de3473fce4bbf2ca5e253c10f70fc60d257b7efa87534b3c26d8a059353` |
| [navigation-trd.png](navigation-trd.png) | 1024×768 | 2026-10-12T21:40:15 | `--offline --no-dialog --verify-radar` (trd-on.png; own-ship center) | `6719d3acbe62bc6201599e9ffe3c7b382313564ae24d9394c007df22e0f48bbf` |
| [navigation-atd.png](navigation-atd.png) | 1024×768 | 2026-10-12T21:40:19 | `--offline --no-dialog --verify-radar` (atd-relocated.png; own-ship center) | `a9b06aecb902871b6f274160665b0183c3a8135657822986c1370ff41a811dc2` |
| [navigation-pin.png](navigation-pin.png) | 1024×768 | 2026-10-12T21:40:17 | `--offline --no-dialog --verify-radar` (atd-zoom-pin.png; own-ship center) | `f5c51fa5eca2faea388ebba6cc029b36e321bf718d337754b5d9f902e7d63b56` |
| [combat-asuw.png](combat-asuw.png) | 1024×768 | 2026-10-12T21:20:26 | `--offline --no-dialog --verify-cic` | `f951d4df5e471b27f9292825dc0dfaf94418d8d55b82a72327f07f6f218024d0` |
| [combat-aaw.png](combat-aaw.png) | 1024×768 | 2026-10-12T21:20:28 | `--offline --no-dialog --verify-cic` | `813bb7a3acc7e3109bc31acac24e17b22c973fb5cd3614b09e581b9e904df3a3` |
| [combat-asw.png](combat-asw.png) | 1024×768 | 2026-10-12T21:20:27 | `--offline --no-dialog --verify-cic` | `c3d12c1460983acb8a96285634f27518ff8b8939fb1d4773f5ce660b24d81172` |
| [transportation-quarterdeck.png](transportation-quarterdeck.png) | 1024×768 | 2026-10-12T21:20:40 | `--offline --no-dialog --verify-transportation` | `91392756e199f13159eef5366c5790648afa1d31ab6de5572b7818f6b9059038` |
| [transportation-code.png](transportation-code.png) | 1024×768 | 2026-10-12T21:20:42 | `--offline --no-dialog --verify-transportation` | `f70ae34b0fad98ed5b723accf9373f8d2d172b395399af5f8551b82f658bff9f` |
| [settings.png](settings.png) | 1024×768 | 2026-10-12T21:20:02 | `--offline --no-dialog --verify-settings` | `b17f6786e1b14302dcf79d038ed4dba59d5e4c7feb5cb03cd0047c2bd3d7e808` |
| [settings-640.png](settings-640.png) | 640×480 | 2026-10-12T21:20:02 | `--offline --no-dialog --verify-settings` | `8145766d3d6088927a242819812f6bc5a18f0dad744786dbec37cfff1f334641` |
| [about.png](about.png) | 483×305 | 2026-10-12T21:35:54 | `--offline --no-dialog --verify-ui` (4.0.0 refresh) | `418b7331184153e4f6e8fda8d1f7bba927266bded1582281a838826c5fe6bfa2` |
| [view-ahead.png](view-ahead.png) | 1024×768 | 2026-10-12T21:20:43 | `--offline --no-dialog --verify-transportation` | `652a3a78b1eeec30a747b74055b9fcf640223b24010531686eae7e43df7a1a9a` |
| [fora-connected.png](fora-connected.png) | 1024×768 | 2026-10-12T21:21:23 | `--no-dialog --frames 120 --rti localhost:25164 --federation MekoManual-<unique> --capture` | `c60292b0e846b37ea2670251fe15788b26aa0d29c95e104dfc41666ad70b7600` |
| [island-vegetation.png](island-vegetation.png) | 1024×768 | 2026-10-12T21:21:12 | `--offline --no-dialog --verify-terrain` | `2c164d7824a769a708c7c05436030b225dc1c47e56f4a60acb4dd76cad0435c4` |
| [ship-nonskid-close.png](ship-nonskid-close.png) | 1024×768 | 2026-10-12T21:52:21 | `--offline --no-dialog --verify-ship-materials` (nonskid-close.png; non-skid) | `f230517d9c590e5d8ee6d35f9720c7a8fdf49343284716cce5f7b850de6319f5` |
| [ship-flight-nonskid-close.png](ship-flight-nonskid-close.png) | 1024×768 | 2026-10-12T21:52:22 | `--offline --no-dialog --verify-ship-materials` (flight-nonskid-close.png; non-skid) | `8fa5efbae8ed1fdf409b5238378498f7668ae98c4954caebb0f69de2d64b4e1e` |
