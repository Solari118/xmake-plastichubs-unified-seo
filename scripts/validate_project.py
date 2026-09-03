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
AUXILIARY_SKILLS = [
    "seo-data-foundation",
    "seo-opportunity-orchestrator",
    "seo-technical-preflight",
    "seo-run-health-check",
    "seo-learning-governor",
]
AUXILIARY_AGENTS = [
    "seo-data-agent.md",
    "seo-opportunity-orchestrator.md",
    "seo-technical-preflight-agent.md",
    "seo-health-check-agent.md",
    "seo-learning-governor-agent.md",
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
    for skill in AUXILIARY_SKILLS:
        if not (ROOT / "skills" / skill / "SKILL.md").exists():
            failures.append(f"missing auxiliary skill: {skill}")
    for agent in AUXILIARY_AGENTS:
        if not (ROOT / "agents" / agent).exists():
            failures.append(f"missing auxiliary agent: {agent}")
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
        "SERP_ACCESS_STATUS:",
        "USER_BROWSER_VERIFICATION_STATUS:",
        "BEST_EFFORT_DOWNGRADE_APPROVAL:",
        "BEST_EFFORT_DOWNGRADE_APPROVAL_EVIDENCE:",
        "PLAN_GATE_STATUS:",
        "PRIMARY_STRUCTURE_REFERENCE:",
        "STRUCTURE_ADAPTATION_MAP:",
        "STYLE_PROFILE:",
        "REFERENCE_SHAPE_FINGERPRINT:",
        "ARTICLE_RHYTHM_ROUTE:",
        "SECTION_REFERENCE_MAP:",
        "ARTICLE_ARCHETYPE:",
        "FAQ_PLAN:",
        "CTA:",
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
        "section-alignment-audit.schema.json",
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
    for field in [
        "SERP_ACCESS_STATUS", "USER_BROWSER_VERIFICATION_STATUS",
        "BEST_EFFORT_DOWNGRADE_APPROVAL", "BEST_EFFORT_DOWNGRADE_APPROVAL_EVIDENCE",
        "REFERENCE_SHAPE_FINGERPRINT", "ARTICLE_RHYTHM_ROUTE", "SECTION_REFERENCE_MAP",
        "FAQ_PLAN", "CTA",
    ]:
        if field not in plan_schema.get("required", []):
            failures.append(f"Plan schema missing required field: {field}")
    top_ten = plan_schema["properties"].get("TOP_TEN_SERP_RESULTS", {})
    if top_ten.get("minItems") != 10 or top_ten.get("maxItems") != 10:
        failures.append("Plan schema does not require exactly ten SERP records")
    result_required = set(top_ten.get("items", {}).get("required", []))
    for field in [
        "primary_intent", "primary_audience", "content_format", "outline",
        "title_alignment", "heading_hierarchy", "narrative_sequence",
        "opening_mode", "intent_resolution_point", "section_length_pattern",
        "list_table_placement", "pacing", "style_profile", "complexity_load",
        "english_naturalness", "ai_pattern_risks", "evidence_form",
        "commercial_intensity", "cta_position", "strengths", "gaps",
        "ranking_hypotheses",
    ]:
        if field not in result_required:
            failures.append(f"Plan schema SERP record missing required field: {field}")
    section_required = set(
        plan_schema["properties"]["SECTION_REFERENCE_MAP"]["items"].get("required", [])
    )
    for field in ("sequence_index", "sequence_reason", "heading_scope_mode"):
        if field not in section_required:
            failures.append(f"Plan schema section map missing required field: {field}")
    faq_required = set(plan_schema["properties"]["FAQ_PLAN"].get("required", []))
    for field in (
        "allow_substantive_sections_after_faq",
        "substantive_sections_after_faq",
        "placement_rationale",
        "placement_reference_urls",
    ):
        if field not in faq_required:
            failures.append(f"Plan schema FAQ plan missing required field: {field}")
    route_schema = json.loads((ROOT / "schemas" / "route-state.schema.json").read_text(encoding="utf-8"))
    terminal_states = route_schema["properties"]["terminal_state"].get("enum", [])
    for terminal_state in [
        "WAITING_FOR_INTENT_APPROVAL",
        "WAITING_FOR_USER_BROWSER_VERIFICATION",
        "WAITING_FOR_TOOL_PERMISSION",
        "WAITING_FOR_FRESH_DATA",
        "WAITING_FOR_LIVE_CHANGE_APPROVAL",
        "WAITING_FOR_GOVERNANCE_APPROVAL",
    ]:
        if terminal_state not in terminal_states:
            failures.append(f"route state missing {terminal_state}")
    if "intent_or_format_approval_required: WAITING_FOR_INTENT_APPROVAL" not in workflow:
        failures.append("workflow missing intent/format approval transition")
    if "google_verification_required: WAITING_FOR_USER_BROWSER_VERIFICATION" not in workflow:
        failures.append("workflow missing Google browser-verification transition")
    if "tool_or_sandbox_permission_required: WAITING_FOR_TOOL_PERMISSION" not in workflow:
        failures.append("workflow missing tool-permission transition")
    if not (ROOT / "scripts" / "validate_plan_gate.py").exists():
        failures.append("missing deterministic Plan gate validator")
    if not (ROOT / "scripts" / "validate_blog_conversion_modules.py").exists():
        failures.append("missing deterministic Blog FAQ/CTA gate validator")
    if not (ROOT / "scripts" / "validate_blog_corpus_similarity.py").exists():
        failures.append("missing deterministic semantic/shape corpus validator")
    if not (ROOT / "scripts" / "validate_blog_narrative_quality.py").exists():
        failures.append("missing deterministic Blog tone, flow, and H2-scope validator")
    if not (ROOT / "scripts" / "validate_heading_content_alignment.py").exists():
        failures.append("missing deterministic H2-to-content alignment gate")
    if not (ROOT / "scripts" / "validate_final_blog_release.py").exists():
        failures.append("missing unified Final Blog release gate")
    legacy_serp = (
        ROOT / "skills" / "b2b-seo-topic-map-builder" / "references" / "serp-top-five-workflow.md"
    ).read_text(encoding="utf-8")
    for required_text in (
        "Legacy Compatibility Only",
        "Do not use this file for active planning",
        "exact Google Top-10 workflow",
    ):
        if required_text not in legacy_serp:
            failures.append(f"legacy Top-5 redirect missing safeguard: {required_text}")
    if "Capture the first five" in legacy_serp or "Use `Best-effort` when" in legacy_serp:
        failures.append("legacy Top-5 file still contains executable obsolete instructions")
    for required_text in [
        "scripts/validate_heading_content_alignment.py",
        "scripts/validate_blog_narrative_quality.py",
        "section-alignment-audit",
    ]:
        if required_text not in workflow:
            failures.append(f"workflow missing H2 alignment control: {required_text}")
    visual_schema = json.loads((ROOT / "schemas" / "visual-brief.schema.json").read_text(encoding="utf-8"))
    if visual_schema["properties"]["assets"].get("minItems", 0) < 3:
        failures.append("visual brief does not require at least three article images")
    final_schema = json.loads((ROOT / "schemas" / "final-package.schema.json").read_text(encoding="utf-8"))
    if final_schema["properties"].get("visual_asset_manifest", {}).get("minItems", 0) < 3:
        failures.append("final package does not require at least three article images")
    if final_schema["properties"].get("section_alignment_gate_status", {}).get("const") != "PASS":
        failures.append("final package does not hard-require a passing H2 alignment gate")
    if final_schema["properties"].get("narrative_quality_gate_status", {}).get("const") != "PASS":
        failures.append("final package does not hard-require a passing narrative-quality gate")
    final_release = (ROOT / "scripts" / "validate_final_blog_release.py").read_text(encoding="utf-8")
    for required_text in ("validate_blog_narrative_quality", "narrative_quality_gate"):
        if required_text not in final_release:
            failures.append(f"unified release gate missing narrative-quality binding: {required_text}")
    if final_schema["properties"].get("release_gate_status", {}).get("const") != "PASS":
        failures.append("final package does not hard-require the unified release gate")
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
        for skill in [item[1] for item in STAGES] + AUXILIARY_SKILLS:
            source = ROOT / "skills" / skill / "SKILL.md"
            mirror = ROOT / mirror_name / "skills" / skill / "SKILL.md"
            if not mirror.exists() or sha(source) != sha(mirror):
                failures.append(f"mirror mismatch: {mirror_name}/skills/{skill}/SKILL.md")
    extension = ROOT / "extensions" / "agentic-seo" / "extension.yaml"
    if not extension.exists() or "status: active" not in extension.read_text(encoding="utf-8"):
        failures.append("agentic SEO extension is not active")
    link_extension = ROOT / "extensions" / "link-building" / "extension.yaml"
    if not link_extension.exists() or "status: installed_inactive" not in link_extension.read_text(encoding="utf-8"):
        failures.append("link-building extension must remain installed_inactive")
    project_text = (ROOT / "project.yaml").read_text(encoding="utf-8")
    for required_text in [
        "slack:",
        "google_sheets:",
        "warning_non_blocking",
        "WAITING_FOR_GOVERNANCE_APPROVAL",
    ]:
        if required_text not in project_text:
            failures.append(f"project governance/output rule missing: {required_text}")
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
