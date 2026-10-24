# Sen Installation Manual — 3.0.0

Windows x64 with the .NET 10 Windows Desktop runtime is required. Building uses the stable .NET 10.0.4xx SDK selected by the suite. No RTI or legacy NSDL schema installation is needed.

From Implementation:

```powershell
dotnet build Tools/Sen/Code/Sen.slnx -c Release -m:1 -nr:false
dotnet publish Tools/Sen/Code/Sen/Sen.csproj -c Release -o Tools/Sen/Code/artifacts/publish
```

Run Sen.exe from the full publish directory. Keep all DLLs/runtime files together. Validation schemas are embedded in NavySim.Scenarios.dll; the current working directory does not supply schemas. There is no installer or file association registration.

The suite solution lists Sen and Management under Tools/Sen, and shared parsing under Library/Scenarios. [Source instructions](../../../Implementation/Tools/Sen/Code/README.md) · [Acceptance](../../../Implementation/Library/Scenarios/Validation/c2sim-migration-20261018.json).
