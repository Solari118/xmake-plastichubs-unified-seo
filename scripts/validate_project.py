"""Validate unified project structure, routing, contracts, mirrors, adapters, and preservation evidence."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_ROOT = [
    "AGENTS.md", "project.yaml", "codex-project.yaml", "README.md", "LICENSE", "CHANGELOG.md",
    "agents", "skills", "tools", "workflows", "prompts", "schemas", "memory", "knowledge",
    "data/raw", "data/processed", "data/fixtures", "templates", "scripts", "examples", "docs",
    "tests", "evals", "observability", "policies", "deployments", ".codex", ".agents", ".github",
    ".gitignore", ".env.example", "Dockerfile", "requirements.lock"
]
STAGES = [
    ("plan", "b2b-seo-topic-map-builder"),
    ("info", "manufacturing-blog-writer"),
    ("audit", "seo-geo-content-auditor"),
    ("b2b-image", "b2b-machining-image-generator"),
    ("final-output", "xmake-plastichubs-website-ops"),
]
LEGACY = {
    "plan": Path(r"C:\Users\Lostk\Documents\文章规划提示词-Plan"),
    "info": Path(r"C:\Users\Lostk\Documents\文章撰写提示词-Info"),
    "audit": Path(r"C:\Users\Lostk\Documents\文章优化提示词2.0-Aduit"),
    "b2b-image": Path(r"C:\Users\Lostk\Documents\B2B机加工生图"),
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--skip-legacy-adapters",
        action="store_true",
        help="Skip workstation-specific legacy adapter checks in portable CI environments",
    )
    args = parser.parse_args()
    failures = []
    for rel in REQUIRED_ROOT:
        if not (ROOT / rel).exists():
            failures.append(f"missing root resource: {rel}")
    for stage, skill in STAGES:
        if not (ROOT / "agents" / f"{stage}.md").exists():
            failures.append(f"missing agent: {stage}")
        if not (ROOT / "skills" / skill / "SKILL.md").exists():
            failures.append(f"missing skill: {skill}")
    workflow = (ROOT / "workflows" / "article-pipeline.yaml").read_text(encoding="utf-8")
    order = [workflow.find(f"  - {stage}\n") for stage, _ in STAGES]
    if any(index < 0 for index in order) or order != sorted(order):
        failures.append("canonical route order is missing or incorrect")
    required_contract = {"PRIMARY_SERVICE:", "CROSS_SERVICE_LINK_PLAN:"}
    contracts = [
        ROOT / "skills" / "b2b-seo-topic-map-builder" / "references" / "content-brief-contract.md",
        ROOT / "skills" / "manufacturing-blog-writer" / "references" / "content-brief-contract.md",
        ROOT / "skills" / "seo-geo-content-auditor" / "references" / "content-brief-contract.md",
    ]
    for contract in contracts:
        text = contract.read_text(encoding="utf-8")
        for field in required_contract:
            if field not in text:
                failures.append(f"contract field {field} missing from {contract.relative_to(ROOT)}")
    for mirror_name in [".agents", ".codex"]:
        for _, skill in STAGES:
            source = ROOT / "skills" / skill / "SKILL.md"
            mirror = ROOT / mirror_name / "skills" / skill / "SKILL.md"
            if not mirror.exists() or sha(source) != sha(mirror):
                failures.append(f"mirror mismatch: {mirror_name}/skills/{skill}/SKILL.md")
    if not args.skip_legacy_adapters:
        for name, legacy in LEGACY.items():
            adapter = legacy / "AGENTS.md"
            backup = legacy / "AGENTS.legacy.md"
            if not adapter.exists() or "CANONICAL_UNIFIED_PROJECT" not in adapter.read_text(encoding="utf-8"):
                failures.append(f"legacy adapter missing: {name}")
            if not backup.exists():
                failures.append(f"legacy AGENTS backup missing: {name}")
            pointer = legacy / "UNIFIED_PROJECT_POINTER.yaml"
            if not pointer.exists() or str(ROOT) not in pointer.read_text(encoding="utf-8"):
                failures.append(f"legacy project pointer missing or wrong: {name}")
            for discovery in [".agents", ".codex"]:
                skill_adapter = legacy / discovery / "skills" / "manufacturing-content-pipeline" / "SKILL.md"
                if not skill_adapter.exists() or "CANONICAL_UNIFIED_PROJECT" not in skill_adapter.read_text(encoding="utf-8"):
                    failures.append(f"legacy discovery adapter missing: {name}/{discovery}")
    inventory = ROOT / "data" / "processed" / "source-capability-inventory.json"
    if not inventory.exists():
        failures.append("capability inventory not generated")
    else:
        summary = json.loads(inventory.read_text(encoding="utf-8"))["summary"]
        if summary["missing_or_changed"]:
            failures.append(f"capability inventory has {summary['missing_or_changed']} missing or changed files")
    forbidden_auto_load = "data/raw/legacy-projects"
    if forbidden_auto_load not in (ROOT / "policies" / "context-isolation.md").read_text(encoding="utf-8"):
        failures.append("legacy snapshot isolation rule missing")
    if failures:
        print("FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("PASS: unified project structure, route, contracts, mirrors, adapters, and preservation evidence")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
