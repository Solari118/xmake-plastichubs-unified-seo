#!/usr/bin/env python3
import argparse
from pathlib import Path

SKILLS = ["seo-backlink-intelligence", "seo-link-outreach"]
AGENTS = ["seo-backlink-intelligence-agent.md", "seo-link-outreach-agent.md"]


def file_map(root):
    return {p.relative_to(root): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", required=True)
    args = parser.parse_args()
    root = Path(args.project_root).resolve()
    errors = []
    config = root / "extensions" / "link-building" / "extension.yaml"
    if not config.is_file() or "status: installed_inactive" not in config.read_text(encoding="utf-8"):
        errors.append("link extension must remain installed_inactive")
    for agent in AGENTS:
        if not (root / "agents" / agent).is_file():
            errors.append(f"missing {agent}")
    for skill in SKILLS:
        source = root / "skills" / skill
        if not (source / "SKILL.md").is_file():
            errors.append(f"missing {skill}")
            continue
        for mirror_name in (".agents", ".codex"):
            mirror = root / mirror_name / "skills" / skill
            if not mirror.is_dir() or file_map(source) != file_map(mirror):
                errors.append(f"mirror mismatch {mirror}")
    if errors:
        print("FAIL")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print("PASS_INSTALLED_INACTIVE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

