$ErrorActionPreference = 'Stop'
& (Join-Path (Split-Path -Parent (Split-Path -Parent $PSScriptRoot)) '.agents\hooks\on_load.ps1')

