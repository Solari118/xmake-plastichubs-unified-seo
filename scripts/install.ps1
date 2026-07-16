[CmdletBinding(SupportsShouldProcess = $true)]
param(
  [string]$ProjectsDestination = (Join-Path ([Environment]::GetFolderPath('MyDocuments')) 'CodexProjects'),
  [switch]$SkipGlobalSkills
)

$ErrorActionPreference = 'Stop'
$RepoRoot = [IO.Path]::GetFullPath((Split-Path -Parent $PSScriptRoot))
$ProjectName = 'xmake-plastichubs-unified-seo'
$Destination = Join-Path $ProjectsDestination $ProjectName
$CodexHome = Join-Path ([Environment]::GetFolderPath('UserProfile')) '.codex'
$BackupRoot = Join-Path $CodexHome ("deployment-backups\" + [DateTime]::UtcNow.ToString('yyyyMMddHHmmss'))

& (Join-Path $PSScriptRoot 'verify-deployment.ps1')

function Backup-Path {
  param([Parameter(Mandatory)][string]$Path)
  if (-not (Test-Path -LiteralPath $Path)) { return }
  $relativeName = ($Path -replace '[:\\/]', '_').Trim('_')
  $backup = Join-Path $BackupRoot $relativeName
  if ($PSCmdlet.ShouldProcess($Path, "Back up to $backup")) {
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $backup) | Out-Null
    Copy-Item -LiteralPath $Path -Destination $backup -Recurse -Force
  }
}

New-Item -ItemType Directory -Force -Path $ProjectsDestination, $CodexHome | Out-Null
$samePath = $RepoRoot.TrimEnd('\\') -ieq $Destination.TrimEnd('\\')
if (-not $samePath) {
  Backup-Path -Path $Destination
  if ($PSCmdlet.ShouldProcess($Destination, 'Install unified project')) {
    if (Test-Path -LiteralPath $Destination) { Remove-Item -LiteralPath $Destination -Recurse -Force }
    New-Item -ItemType Directory -Force -Path $Destination | Out-Null
    $exclude = @('.git', 'outputs', 'rendered_plastic_cnc_revised', 'rendered_plastic_cnc_revised_v2')
    Get-ChildItem -LiteralPath $RepoRoot -Force | Where-Object { $_.Name -notin $exclude } | ForEach-Object {
      Copy-Item -LiteralPath $_.FullName -Destination $Destination -Recurse -Force
    }
  }
}

$InstalledRoot = if ($samePath) { $RepoRoot } else { $Destination }
& (Join-Path $InstalledRoot 'tools\sync_unified_project.ps1') -Root $InstalledRoot

if (-not $SkipGlobalSkills) {
  $skillsRoot = Join-Path $InstalledRoot 'skills'
  foreach ($skill in Get-ChildItem -LiteralPath $skillsRoot -Directory) {
    if (-not (Test-Path -LiteralPath (Join-Path $skill.FullName 'SKILL.md'))) { continue }
    $skillDestination = Join-Path $CodexHome ("skills\" + $skill.Name)
    Backup-Path -Path $skillDestination
    if ($PSCmdlet.ShouldProcess($skillDestination, "Install skill $($skill.Name)")) {
      if (Test-Path -LiteralPath $skillDestination) { Remove-Item -LiteralPath $skillDestination -Recurse -Force }
      New-Item -ItemType Directory -Force -Path (Split-Path -Parent $skillDestination) | Out-Null
      Copy-Item -LiteralPath $skill.FullName -Destination $skillDestination -Recurse -Force
    }
  }
}

New-Item -ItemType Directory -Force -Path (Join-Path $InstalledRoot 'outputs') | Out-Null
Write-Output "Installation complete: $InstalledRoot"
Write-Output "Conflicting local content was backed up under: $BackupRoot"
Write-Output 'Open the installed project folder in Codex Desktop and reload the project.'
