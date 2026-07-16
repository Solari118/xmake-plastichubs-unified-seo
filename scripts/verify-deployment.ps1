[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$RepoRoot = [IO.Path]::GetFullPath((Split-Path -Parent $PSScriptRoot))

$required = @(
  'AGENTS.md',
  'project.yaml',
  'codex-project.yaml',
  'manifest.json',
  'agents\unified-seo-pipeline.md',
  'skills\unified-seo-pipeline\SKILL.md',
  'skills\b2b-seo-topic-map-builder\SKILL.md',
  'skills\manufacturing-blog-writer\SKILL.md',
  'skills\seo-geo-content-auditor\SKILL.md',
  'skills\b2b-machining-image-generator\SKILL.md',
  'skills\xmake-plastichubs-website-ops\SKILL.md',
  'integrated-assets\b2b-machining-image-generator\SKILL.md',
  'data\plastichubs\keywords\PlasticHubs_SEMrush_All_Keywords_Classified_2026-07-10.xlsx',
  'hooks\on_load.ps1',
  'tools\sync_unified_project.ps1',
  'tools\validate_unified_project.py',
  'scripts\install.ps1'
)

foreach ($relative in $required) {
  if (-not (Test-Path -LiteralPath (Join-Path $RepoRoot $relative) -PathType Leaf)) {
    throw "Required deployment file is missing: $relative"
  }
}

$forbidden = Get-ChildItem -LiteralPath $RepoRoot -Recurse -File -Force | Where-Object {
  $_.FullName -notmatch '[\\/]\.git[\\/]' -and (
    $_.Name -match '^(\.env($|\.)|id_rsa|id_ed25519)$' -or
    $_.Extension -match '^\.(pfx|pem|key)$'
  )
}
if ($forbidden) {
  throw "Credential-like files found: $($forbidden.FullName -join ', ')"
}

$largeFiles = Get-ChildItem -LiteralPath $RepoRoot -Recurse -File -Force | Where-Object {
  $_.FullName -notmatch '[\\/]\.git[\\/]' -and $_.Length -gt 95MB
}
if ($largeFiles) {
  throw "Files larger than 95 MB cannot be pushed safely: $($largeFiles.FullName -join ', ')"
}

$rg = Get-Command rg -ErrorAction SilentlyContinue
if ($rg) {
  $patterns = '(github_pat_[A-Za-z0-9_]+|ghp_[A-Za-z0-9]+|sk-[A-Za-z0-9_-]{16,}|BEGIN (RSA |OPENSSH |EC )?PRIVATE KEY)'
  $secretMatches = @(& $rg.Source -l -i --hidden --glob '!**/.git/**' $patterns $RepoRoot)
  $scanExitCode = $LASTEXITCODE
  if ($secretMatches) { throw "Potential credential material detected: $($secretMatches -join ', ')" }
  if ($scanExitCode -gt 1) { throw "Secret scan failed with exit code $scanExitCode" }
}

$checksumPath = Join-Path $RepoRoot 'checksums.sha256'
if (Test-Path -LiteralPath $checksumPath) {
  foreach ($line in Get-Content -LiteralPath $checksumPath) {
    if ($line -notmatch '^([a-f0-9]{64})  (.+)$') { throw "Malformed checksum line: $line" }
    $file = Join-Path $RepoRoot $matches[2]
    if (-not (Test-Path -LiteralPath $file)) { throw "Checksum target missing: $($matches[2])" }
    $actual = (Get-FileHash -LiteralPath $file -Algorithm SHA256).Hash.ToLowerInvariant()
    if ($actual -ne $matches[1]) { throw "Checksum mismatch: $($matches[2])" }
  }
}

$python = Get-Command python.exe -All -ErrorAction SilentlyContinue |
  Where-Object { $_.Source -notmatch '[\\/]WindowsApps[\\/]' } |
  Select-Object -First 1
if (-not $python) {
  $python = Get-Command python3.exe -All -ErrorAction SilentlyContinue |
    Where-Object { $_.Source -notmatch '[\\/]WindowsApps[\\/]' } |
    Select-Object -First 1
}
if ($python) {
  & $python.Source (Join-Path $RepoRoot 'tools\validate_unified_project.py')
  if ($LASTEXITCODE -ne 0) { throw 'Unified project validator failed.' }
} else {
  Write-Warning 'Python was not found; deterministic project validator was skipped.'
}

$files = Get-ChildItem -LiteralPath $RepoRoot -Recurse -File -Force | Where-Object {
  $_.FullName -notmatch '[\\/]\.git[\\/]'
}
Write-Output "Deployment verification passed. Files: $($files.Count)"
