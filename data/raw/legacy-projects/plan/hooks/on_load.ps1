$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
$required = @(
  'AGENTS.md',
  'project.yaml',
  'agents/unified-seo-pipeline.md',
  'skills/unified-seo-pipeline/SKILL.md',
  'skills/b2b-seo-topic-map-builder/SKILL.md',
  'skills/manufacturing-blog-writer/SKILL.md',
  'skills/seo-geo-content-auditor/SKILL.md',
  'skills/b2b-machining-image-generator/SKILL.md',
  'config/article-schedule.yaml'
)
$missing = @($required | Where-Object { -not (Test-Path (Join-Path $root $_)) })
if ($missing.Count -gt 0) {
  Write-Output ('BLOCKED: missing unified project files: ' + ($missing -join ', '))
  exit 1
}
Write-Output 'OK: unified SEO pipeline files are present.'
Write-Output 'Approval gate: only agent-proposed keywords pause the chain.'
Write-Output 'Scheduler: contract loaded; external automation remains disabled until explicitly configured.'
