#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
required=(
  "AGENTS.md"
  "project.yaml"
  "agents/unified-seo-pipeline.md"
  "skills/unified-seo-pipeline/SKILL.md"
  "skills/b2b-seo-topic-map-builder/SKILL.md"
  "skills/manufacturing-blog-writer/SKILL.md"
  "skills/seo-geo-content-auditor/SKILL.md"
  "skills/b2b-machining-image-generator/SKILL.md"
  "config/article-schedule.yaml"
)
missing=()
for file in "${required[@]}"; do
  [[ -f "$ROOT/$file" ]] || missing+=("$file")
done
if (( ${#missing[@]} )); then
  echo "BLOCKED: missing unified project files: ${missing[*]}"
  exit 1
fi
echo "OK: unified SEO pipeline files are present."
echo "Approval gate: only agent-proposed keywords pause the chain."
echo "Scheduler: contract loaded; external automation remains disabled until explicitly configured."
