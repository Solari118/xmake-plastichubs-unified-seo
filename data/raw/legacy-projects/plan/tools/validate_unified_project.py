"""Validate the local unified SEO project without modifying it."""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "AGENTS.md",
    "project.yaml",
    "codex-project.yaml",
    "agents/unified-seo-pipeline.md",
    "skills/unified-seo-pipeline/SKILL.md",
    "skills/b2b-seo-topic-map-builder/SKILL.md",
    "skills/manufacturing-blog-writer/SKILL.md",
    "skills/seo-geo-content-auditor/SKILL.md",
    "skills/b2b-machining-image-generator/SKILL.md",
    "skills/xmake-plastichubs-website-ops/SKILL.md",
    "config/article-schedule.yaml",
    "config/live-seo-data-source.yaml",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    missing = [path for path in REQUIRED if not (ROOT / path).is_file()]
    if missing:
        print("BLOCKED: missing files")
        for path in missing:
            print(f"- {path}")
        return 1

    project_text = (ROOT / "project.yaml").read_text(encoding="utf-8")
    router_text = (ROOT / "agents/unified-seo-pipeline.md").read_text(encoding="utf-8")
    skill_text = (ROOT / "skills/unified-seo-pipeline/SKILL.md").read_text(encoding="utf-8")
    live_source_text = (ROOT / "config/live-seo-data-source.yaml").read_text(encoding="utf-8")
    checks = {
        "default_router": "default: \"unified-seo-pipeline\"" in project_text,
        "full_route": all(token in router_text for token in ["Plan", "Info", "Audit", "B2B Asset", "Website Ops/Word"]),
        "keyword_pause": "WAITING_FOR_KEYWORD_APPROVAL" in skill_text,
        "user_keyword_bypass": "KEYWORD_USER_SUPPLIED" in skill_text,
        "image_skill": (ROOT / "skills/b2b-machining-image-generator/agents/openai.yaml").is_file(),
        "live_data_contract": "LIVE_DATA_STATUS" in skill_text and "authenticated_browser" in live_source_text,
    }
    failed = [name for name, passed in checks.items() if not passed]
    print(f"Root: {ROOT}")
    print(f"Required files: {len(REQUIRED)}")
    print(f"Required SHA sample: {sha256(ROOT / 'skills/unified-seo-pipeline/SKILL.md')}")
    for name, passed in checks.items():
        print(f"{name}: {'PASS' if passed else 'FAIL'}")
    if failed:
        print("STATUS: BLOCKED")
        return 1
    print("STATUS: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
