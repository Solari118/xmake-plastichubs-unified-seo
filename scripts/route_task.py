"""Deterministic route planner for the unified manufacturing content project."""

from __future__ import annotations

import argparse
import json


FULL = ["plan", "info", "audit", "b2b-image", "final-output"]


def route(
    entry: str,
    mode: str,
    detected: str,
    audit_defect: str = "none",
    wechat_reference: bool = False,
    plan_gate: str = "pass",
) -> list[str]:
    def auxiliary(stages: list[str]) -> list[str]:
        if wechat_reference and mode not in {"standalone_image", "performance_review"}:
            return ["wechat-research", *stages]
        return stages

    if mode == "standalone_image":
        return ["b2b-image"]
    if mode == "performance_review" or detected == "published_article":
        return ["performance-review"]
    if mode == "phase_only":
        mapping = {"article": "audit", "canonical": "plan"}
        return auxiliary([mapping.get(entry, entry)])

    starts = {
        "none": 0,
        "topic": 0,
        "plan_brief": 1,
        "article": 2,
        "audited_article": 3,
        "article_with_assets": 4,
    }
    start = starts[detected]
    stages = FULL[start:]
    if detected == "article" and audit_defect == "info":
        stages = ["audit", "info", "audit", "b2b-image", "final-output"]
    elif detected == "article" and audit_defect == "plan":
        stages = ["audit", "plan", "info", "audit", "b2b-image", "final-output"]
    elif detected == "article" and audit_defect == "user":
        stages = ["audit", "BLOCKED"]
    if "plan" in stages and plan_gate != "pass":
        plan_index = stages.index("plan")
        terminals = {
            "intent_approval_required": "WAITING_FOR_INTENT_APPROVAL",
            "browser_verification_required": "WAITING_FOR_USER_BROWSER_VERIFICATION",
            "tool_permission_required": "WAITING_FOR_TOOL_PERMISSION",
            "best_effort_approval_required": "WAITING_FOR_USER_BROWSER_VERIFICATION",
        }
        terminal = terminals.get(plan_gate, "BLOCKED")
        stages = [*stages[:plan_index + 1], terminal]
    return auxiliary(stages)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--entry", choices=["canonical", "plan", "info", "audit", "b2b-image", "final-output", "performance-review", "article"], default="canonical")
    parser.add_argument("--mode", choices=["full_pipeline", "phase_only", "standalone_image", "performance_review"], default="full_pipeline")
    parser.add_argument("--detected", choices=["none", "topic", "plan_brief", "article", "audited_article", "article_with_assets", "published_article"], default="none")
    parser.add_argument("--audit-defect", choices=["none", "info", "plan", "user"], default="none")
    parser.add_argument(
        "--plan-gate",
        choices=[
            "pass", "intent_approval_required", "browser_verification_required",
            "tool_permission_required", "best_effort_approval_required", "blocked",
        ],
        default="pass",
    )
    parser.add_argument("--wechat-reference", action="store_true")
    args = parser.parse_args()
    print(json.dumps({"entry": args.entry, "mode": args.mode, "detected": args.detected, "wechat_reference": args.wechat_reference, "plan_gate": args.plan_gate, "stages": route(args.entry, args.mode, args.detected, args.audit_defect, args.wechat_reference, args.plan_gate)}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
