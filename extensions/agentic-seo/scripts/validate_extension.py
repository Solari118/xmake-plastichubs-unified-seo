#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

SKILLS = [
    "seo-data-foundation",
    "seo-opportunity-orchestrator",
    "seo-technical-preflight",
    "seo-run-health-check",
    "seo-learning-governor",
]
AGENTS = [
    "seo-data-agent.md",
    "seo-opportunity-orchestrator.md",
    "seo-technical-preflight-agent.md",
    "seo-health-check-agent.md",
    "seo-learning-governor-agent.md",
]
SCHEMAS = [
    "source-manifest.schema.json",
    "proposal.schema.json",
    "action-queue.schema.json",
    "run-receipt.schema.json",
    "learning-change-proposal.schema.json",
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", required=True)
    args = parser.parse_args()
    root = Path(args.project_root).resolve()
    extension = root / "extensions" / "agentic-seo"
    errors = []
    warnings = []

    config = extension / "extension.yaml"
    if not config.is_file():
        errors.append(f"missing {config}")
    elif yaml is None:
        warnings.append("PyYAML unavailable; extension.yaml parse skipped")
    else:
        yaml.safe_load(config.read_text(encoding="utf-8"))

    for schema_name in SCHEMAS:
        schema_path = extension / "schemas" / schema_name
        if not schema_path.is_file():
            errors.append(f"missing {schema_path}")
        else:
            json.loads(schema_path.read_text(encoding="utf-8"))

    for agent in AGENTS:
        if not (root / "agents" / agent).is_file():
            errors.append(f"missing agent {agent}")

    for skill in SKILLS:
        canonical = root / "skills" / skill
        if not (canonical / "SKILL.md").is_file():
            errors.append(f"missing skill {skill}")
            continue
        canonical_files = {
            path.relative_to(canonical): path.read_bytes()
            for path in canonical.rglob("*") if path.is_file()
        }
        for mirror_name in (".agents", ".codex"):
            mirror = root / mirror_name / "skills" / skill
            if not mirror.is_dir():
                errors.append(f"missing mirror {mirror}")
                continue
            mirror_files = {
                path.relative_to(mirror): path.read_bytes()
                for path in mirror.rglob("*") if path.is_file()
            }
            if canonical_files != mirror_files:
                errors.append(f"mirror mismatch {mirror}")

    if errors:
        print("BLOCKED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PASS_STRUCTURAL")
    for warning in warnings:
        print(f"WARNING: {warning}")
    print("LIVE_RUNTIME_NOT_TESTED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
