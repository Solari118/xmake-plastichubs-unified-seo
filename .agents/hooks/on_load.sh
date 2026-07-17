#!/usr/bin/env sh
set -eu
root="$(CDPATH= cd -- "$(dirname -- "$0")/../.." && pwd)"
for rel in AGENTS.md project.yaml skills/manufacturing-content-pipeline/SKILL.md workflows/article-pipeline.yaml policies/context-isolation.md scripts/validate_project.py; do
  test -e "$root/$rel" || { echo "BLOCKED: missing $rel"; exit 1; }
done
echo "OK: canonical manufacturing content pipeline is present."

