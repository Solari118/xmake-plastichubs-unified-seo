"""Validate unified project structure, routing, contracts, mirrors, adapters, and preservation evidence."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_ROOT = [
    "AGENTS.md", "project.yaml", "codex-project.yaml", "README.md", "LICENSE", "CHANGELOG.md",
    "agents", "skills", "tools", "workflows", "prompts", "schemas", "memory", "knowledge", "config",
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
    ("performance-review", "seo-content-performance-review"),
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
        skill_path = ROOT / "skills" / skill / "SKILL.md"
        if not skill_path.exists():
            failures.append(f"missing skill: {skill}")
        else:
            skill_text = skill_path.read_text(encoding="utf-8")
            frontmatter = re.match(r"^---\r?\n(.*?)\r?\n---", skill_text, re.DOTALL)
            if not frontmatter:
                failures.append(f"missing or invalid skill frontmatter: {skill}")
            elif not re.search(rf"(?m)^name:\s*{re.escape(skill)}\s*$", frontmatter.group(1)):
                failures.append(f"skill frontmatter name mismatch: {skill}")
            elif not re.search(r"(?m)^description:\s*\S", frontmatter.group(1)):
                failures.append(f"skill description missing: {skill}")
    workflow = (ROOT / "workflows" / "article-pipeline.yaml").read_text(encoding="utf-8")
    order = [workflow.find(f"  - {stage}\n") for stage, _ in STAGES]
    if any(index < 0 for index in order) or order != sorted(order):
        failures.append("canonical route order is missing or incorrect")
    required_contract = {
        "PRIMARY_SERVICE:",
        "CROSS_SERVICE_LINK_PLAN:",
        "TOP_TEN_SERP_RESULTS:",
        "TOP_TEN_COMPLETENESS_STATUS:",
        "SERP_INTENT_DISTRIBUTION:",
        "DOMINANT_SERP_INTENT:",
        "SERP_AUDIENCE_DISTRIBUTION:",
        "DOMINANT_AUDIENCE:",
        "SERP_FORMAT_DISTRIBUTION:",
        "DOMINANT_CONTENT_FORMAT:",
        "SELECTED_PRIMARY_INTENT:",
        "SELECTED_CONTENT_FORMAT:",
        "ANGLE_ALIGNMENT_STATUS:",
        "USER_INTENT_APPROVAL:",
        "PLAN_GATE_STATUS:",
        "PRIMARY_STRUCTURE_REFERENCE:",
        "STRUCTURE_ADAPTATION_MAP:",
        "STYLE_PROFILE:",
        "ARTICLE_ARCHETYPE:",
        "INTERNAL_LINK_DEPLOYMENT:",
        "COMPETITOR_PAGE_STRENGTH:",
    }
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
    required_schemas = [
        "task-envelope.schema.json",
        "plan-brief.schema.json",
        "article-bundle.schema.json",
        "audit-report.schema.json",
        "final-package.schema.json",
        "route-state.schema.json",
        "performance-review.schema.json",
        "visual-brief.schema.json",
    ]
    for schema_name in required_schemas:
        schema_path = ROOT / "schemas" / schema_name
        if not schema_path.exists():
            failures.append(f"missing schema: {schema_name}")
            continue
        try:
            json.loads(schema_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            failures.append(f"invalid JSON schema {schema_name}: {exc}")
    plan_schema = json.loads((ROOT / "schemas" / "plan-brief.schema.json").read_text(encoding="utf-8"))
    top_ten = plan_schema["properties"].get("TOP_TEN_SERP_RESULTS", {})
    if top_ten.get("minItems") != 10 or top_ten.get("maxItems") != 10:
        failures.append("Plan schema does not require exactly ten SERP records")
    result_required = set(top_ten.get("items", {}).get("required", []))
    for field in [
        "primary_intent", "primary_audience", "content_format", "outline",
        "opening_mode", "pacing", "style_profile", "evidence_form",
        "commercial_intensity", "cta_position", "strengths", "gaps",
        "ranking_hypotheses",
    ]:
        if field not in result_required:
            failures.append(f"Plan schema SERP record missing required field: {field}")
    route_schema = json.loads((ROOT / "schemas" / "route-state.schema.json").read_text(encoding="utf-8"))
    terminal_states = route_schema["properties"]["terminal_state"].get("enum", [])
    if "WAITING_FOR_INTENT_APPROVAL" not in terminal_states:
        failures.append("route state missing WAITING_FOR_INTENT_APPROVAL")
    if "intent_or_format_approval_required: WAITING_FOR_INTENT_APPROVAL" not in workflow:
        failures.append("workflow missing intent/format approval transition")
    if not (ROOT / "scripts" / "validate_plan_gate.py").exists():
        failures.append("missing deterministic Plan gate validator")
    visual_schema = json.loads((ROOT / "schemas" / "visual-brief.schema.json").read_text(encoding="utf-8"))
    if visual_schema["properties"]["assets"].get("minItems", 0) < 3:
        failures.append("visual brief does not require at least three article images")
    final_schema = json.loads((ROOT / "schemas" / "final-package.schema.json").read_text(encoding="utf-8"))
    if final_schema["properties"].get("visual_asset_manifest", {}).get("minItems", 0) < 3:
        failures.append("final package does not require at least three article images")
    output_skill = (ROOT / "skills" / "xmake-plastichubs-website-ops" / "SKILL.md").read_text(encoding="utf-8")
    if "#5B9BD5" not in output_skill:
        failures.append("light-blue internal-link output rule missing")
    private_files = [
        ROOT / "config" / "private-resource-sources.yaml",
        ROOT / "policies" / "private-resource-policy.md",
        ROOT / "scripts" / "sync_private_resources.ps1",
        ROOT / "scripts" / "assert_private_packaging_scope.ps1",
    ]
    for private_file in private_files:
        if not private_file.exists():
            failures.append(f"missing private-resource control: {private_file.relative_to(ROOT)}")
    private_policy = (ROOT / "policies" / "private-resource-policy.md").read_text(encoding="utf-8")
    for required_text in [
        "Local project copies are allowed",
        "replace every visible `APEX`, `TIGER`",
        "must not be pixel-identical",
        "Every packaging request requires a fresh question",
    ]:
        if required_text not in private_policy:
            failures.append(f"private-resource policy rule missing: {required_text}")
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
