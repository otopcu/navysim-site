# ExMFd Installation Manual — 4.0.0

Windows x64 and .NET 10 Windows Desktop runtime are required. Build with the suite .NET 10 SDK and restored Fora.Client packages. A compatible Fora RTI is required for federation operations.

From Implementation:

```powershell
dotnet build FdApps/ExMFd/Code/ExMFd.slnx -c Release -m:1 -nr:false
dotnet publish FdApps/ExMFd/Code/src/ExMFd.App -c Release -o FdApps/ExMFd/Code/artifacts/publish
```

Deploy the entire output directory, including `Fom/NavySim.xml`. Schemas are embedded. Use a fresh output directory when replacing an old build; the retired NavySim.Scenario.xml is not required or joined.

Browse the FDD path in RTI connection. XML content is sent to the RTI; the server does not read the client-local path. Use matching federation names and unique federate names. Scenario SystemName must match each ship's producing federate name.

Execution uses Scenario OC, HF TaskOrd, BeginToPlay, Environment OC and HF InjectionMessage. EnviFd is optional. No extra JSON protocol, supplemental FOM module or legacy RACoN/RTI DLL is required.

[Manual](UserManual.md) · [Architecture](Architecture.md) · [Historical instructions](History/InstallationManual.md).
