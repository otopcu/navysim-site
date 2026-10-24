### What's New

NavySim **2026.1** is in development. It moves the suite from the NSTMSS-era toolchain (DMSO RTI 1.3-NG, OpenGL Performer, .NET Framework) to **.NET 10**, the **Fora** IEEE 1516-2025 (HLA 4) client and the **Stride** 3D engine.

- **New ship-handling federates.** MekoFd 4.0.0 is a C# / Stride / Fora rewrite of the MEKO-class frigate simulator. KnoxFd resumes its original lineage as 5.0.0 on the same shared maritime runtime.
- **Shared maritime runtime.** Sea and wind, hydrodynamics, controllable-pitch propulsion, ENC chart navigation, navigation radar and bridge consoles are shared by both ship federates.
- **C2SIM scenarios.** Sen 3.0.0 authors C2SIM packages with typed scheduled events. ExMFd 4.0.0 executes them, separates authored inspection from instant injection, shows workspace progress and produces after-action review statistics.
- **Modernized federates.** EnviFd 5.0.0 and FedMonFd 3.0.0 run on .NET 10 and Fora. FedMonFd monitors the federation live through the HLA Management Object Model (MOM).
- **Federation model.** FOM / FDD 5.1.0 adds typed event injection and an initial true heading for pre-Begin scenario placement.
- **Versioning.** The suite has a calendar version (`2026.1`), and every component has its own semantic version.

See [Components](Components.md) for every component version and the [Release Notes](ReleaseNotes.md) for details.
