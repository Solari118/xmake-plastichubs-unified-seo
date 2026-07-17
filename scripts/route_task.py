"""Deterministic route planner for the unified manufacturing content project."""

from __future__ import annotations

import argparse
import json


FULL = ["plan", "info", "audit", "b2b-image", "final-output"]


def route(entry: str, mode: str, detected: str, audit_defect: str = "none") -> list[str]:
    if mode == "standalone_image":
        return ["b2b-image"]
    if mode == "phase_only":
        mapping = {"article": "audit", "canonical": "plan"}
        return [mapping.get(entry, entry)]

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
    return stages


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--entry", choices=["canonical", "plan", "info", "audit", "b2b-image", "article"], default="canonical")
    parser.add_argument("--mode", choices=["full_pipeline", "phase_only", "standalone_image"], default="full_pipeline")
    parser.add_argument("--detected", choices=["none", "topic", "plan_brief", "article", "audited_article", "article_with_assets"], default="none")
    parser.add_argument("--audit-defect", choices=["none", "info", "plan", "user"], default="none")
    args = parser.parse_args()
    print(json.dumps({"entry": args.entry, "mode": args.mode, "detected": args.detected, "stages": route(args.entry, args.mode, args.detected, args.audit_defect)}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

