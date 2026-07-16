param(
  [string]$Root = (Split-Path -Parent $PSScriptRoot)
)

$ErrorActionPreference = 'Stop'
$targets = @('.agents', '.codex')

foreach ($target in $targets) {
  $base = Join-Path $Root $target
  New-Item -ItemType Directory -Force `
    (Join-Path $base 'agents'),
    (Join-Path $base 'skills'),
    (Join-Path $base 'data'),
    (Join-Path $base 'hooks'),
    (Join-Path $base 'config') | Out-Null

  Copy-Item -Recurse -Force (Join-Path $Root 'skills\*') (Join-Path $base 'skills')
  Copy-Item -Force (Join-Path $Root 'agents\*') (Join-Path $base 'agents')
  Copy-Item -Recurse -Force (Join-Path $Root 'data\*') (Join-Path $base 'data')
  Copy-Item -Force (Join-Path $Root 'hooks\*') (Join-Path $base 'hooks')
  Copy-Item -Force (Join-Path $Root 'config\*') (Join-Path $base 'config')
}

Copy-Item -Force (Join-Path $Root 'project.yaml') (Join-Path $Root '.codex\project.yaml')
Copy-Item -Force (Join-Path $Root 'codex-project.yaml') (Join-Path $Root '.codex\codex-project.yaml')
Copy-Item -Force (Join-Path $Root 'README.md') (Join-Path $Root '.codex\project.md')

Write-Output 'Unified project mirrors synchronized: .agents and .codex'
