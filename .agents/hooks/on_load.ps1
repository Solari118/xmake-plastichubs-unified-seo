$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$required = @(
  'AGENTS.md',
  'project.yaml',
  'skills/manufacturing-content-pipeline/SKILL.md',
  'workflows/article-pipeline.yaml',
  'policies/context-isolation.md',
  'scripts/validate_project.py'
)
$missing = @($required | Where-Object { -not (Test-Path -LiteralPath (Join-Path $root $_)) })
if ($missing.Count) {
  Write-Output ('BLOCKED: missing canonical project files: ' + ($missing -join ', '))
  exit 1
}
Write-Output 'OK: canonical manufacturing content pipeline is present.'
Write-Output 'Route: artifact-aware Plan -> Info -> Audit -> B2B Image -> Final Output.'

