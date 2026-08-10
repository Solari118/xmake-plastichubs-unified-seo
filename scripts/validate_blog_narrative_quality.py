"""Validate Blog tone, FAQ interruption control, and H2 scope against the Plan."""

from __future__ import annotations

import argparse
import json
import re
import tempfile
from copy import deepcopy
from pathlib import Path
from typing import Any


FORBIDDEN_TONE_TERMS = (
    "delve", "embark", "craft", "crafting", "unlock", "discover", "utilize",
    "utilizing", "dive deep", "unveil", "harness", "elucidate", "enlightening",
    "esteemed", "game-changer", "skyrocket", "revolutionize", "disruptive",
    "groundbreaking", "cutting-edge", "remarkable", "powerful", "world-class",
    "real-world", "shed light", "imagine", "realm", "abyss", "tapestry",
    "illuminate", "glimpse into", "navigating", "landscape", "stark",
    "testament", "bustling", "opened up", "ever-evolving", "you're not alone",
    "in a world where", "it remains to be seen", "pivotal", "intricate",
    "hence", "furthermore", "however", "moreover", "in summary",
    "in conclusion", "in closing",
)
NARROW_NEGATIVE_CONTRAST = re.compile(
    r"\b(?:is|are)\s+not\s+the\s+same\s+as\b|\bnot\s+the\s+same\s+as\b",
    re.IGNORECASE,
)


def parse_sections(text: str) -> list[dict[str, Any]]:
    matches = list(re.finditer(r"(?m)^## (?!#)(.+?)\s*$", text))
    sections: list[dict[str, Any]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        body = text[match.end():end]
        sections.append({
            "heading": match.group(1).strip(),
            "h3_count": len(re.findall(r"(?m)^### (?!#).+?\s*$", body)),
        })
    return sections


def tone_hits(text: str) -> list[str]:
    hits: list[str] = []
    for term in FORBIDDEN_TONE_TERMS:
        pattern = rf"(?<![A-Za-z]){re.escape(term)}(?![A-Za-z])"
        if re.search(pattern, text, re.IGNORECASE):
            hits.append(term)
    return hits


def validate(article: Path, plan: dict[str, Any]) -> dict[str, Any]:
    text = article.read_text(encoding="utf-8")
    sections = parse_sections(text)
    section_map = plan.get("SECTION_REFERENCE_MAP")
    errors: list[str] = []

    hits = tone_hits(text)
    if hits:
        errors.append(f"forbidden tone terms found: {', '.join(hits)}")

    if not isinstance(section_map, list) or len(section_map) != len(sections):
        errors.append("article H2 count cannot be reconciled with SECTION_REFERENCE_MAP")
        section_map = []

    for index, article_section in enumerate(sections):
        if index >= len(section_map) or not isinstance(section_map[index], dict):
            continue
        planned = section_map[index]
        kind = str(planned.get("section_kind", "")).strip()
        scope_mode = str(planned.get("heading_scope_mode", "")).strip()
        heading = article_section["heading"]
        h3_count = article_section["h3_count"]
        if kind == "core" and h3_count >= 3:
            if scope_mode not in {"multi-topic-umbrella", "comparison"}:
                errors.append(
                    f"H2 {index + 1} contains {h3_count} H3 topics but lacks a broad heading scope mode"
                )
            if NARROW_NEGATIVE_CONTRAST.search(heading):
                errors.append(
                    f"H2 {index + 1} uses a narrow negative comparison over {h3_count} H3 topics"
                )

    kinds = [
        str(section.get("section_kind", "")).strip()
        for section in section_map if isinstance(section, dict)
    ]
    if kinds.count("faq") != 1:
        errors.append("SECTION_REFERENCE_MAP must contain exactly one FAQ for narrative-flow validation")
    else:
        faq_index = kinds.index("faq")
        core_after = [
            str(section.get("planned_heading", "")).strip()
            for section in section_map[faq_index + 1:]
            if isinstance(section, dict) and section.get("section_kind") == "core"
        ]
        faq = plan.get("FAQ_PLAN")
        if not isinstance(faq, dict):
            errors.append("FAQ_PLAN is missing")
        else:
            if faq.get("substantive_sections_after_faq") != core_after:
                errors.append(
                    "FAQ_PLAN does not declare the actual core sections placed after FAQ"
                )
            if core_after and faq.get("allow_substantive_sections_after_faq") is not True:
                errors.append("FAQ interrupts the core narrative without an approved placement exception")
            if not core_after and faq.get("allow_substantive_sections_after_faq") is not False:
                errors.append(
                    "FAQ placement flag must be false when no substantive section follows FAQ"
                )
            if len(str(faq.get("placement_rationale", "")).split()) < 8:
                errors.append("FAQ placement rationale is too thin for flow review")

    return {
        "status": "PASS" if not errors else "FAIL",
        "forbidden_tone_hits": hits,
        "h2_count": len(sections),
        "errors": errors,
    }


def self_test() -> int:
    from validate_plan_gate import sample

    article_text = """# Manufacturing Process Guide

## What the process is and when it fits

This process fits plastic parts that need controlled features without dedicated tooling.

## How the process works

The supplier prepares stock, runs the operation, and inspects the part.

## Questions Buyers Ask Before Choosing This Route

### When is the process a poor fit?

It is a poor fit when the required evidence conflicts with the process.

### Which inputs affect the quote most?

CAD, material, quantity, tolerance, and finish affect the quote.

### What should be verified?

Verify material, dimensions, finish, and inspection.

## Review Your Plastic Part With PlasticHubs

Send PlasticHubs the CAD file and drawing for review.
"""
    with tempfile.TemporaryDirectory() as temporary:
        article = Path(temporary) / "article.md"
        article.write_text(article_text, encoding="utf-8")
        good_plan = sample(False)
        good = validate(article, good_plan)

        article.write_text(article_text.replace(
            "This process fits", "However, this process fits"
        ), encoding="utf-8")
        bad_tone = validate(article, good_plan)

        article.write_text(article_text, encoding="utf-8")
        bad_flow_plan = deepcopy(good_plan)
        moved = bad_flow_plan["SECTION_REFERENCE_MAP"].pop(1)
        bad_flow_plan["SECTION_REFERENCE_MAP"].insert(3, moved)
        bad_flow_plan["FAQ_PLAN"]["substantive_sections_after_faq"] = []
        bad_flow_plan["FAQ_PLAN"]["allow_substantive_sections_after_faq"] = False
        bad_flow = validate(article, bad_flow_plan)

        narrow_text = article_text.replace(
            "## What the process is and when it fits\n\n"
            "This process fits plastic parts that need controlled features without dedicated tooling.",
            "## A molded texture is not the same as a coating\n\n"
            "Secondary finishing can include several routes.\n\n"
            "### Polishing\n\nPolishing changes gloss.\n\n"
            "### Blasting\n\nBlasting changes texture.\n\n"
            "### Printing\n\nPrinting adds graphics."
        )
        article.write_text(narrow_text, encoding="utf-8")
        bad_scope_plan = deepcopy(good_plan)
        bad_scope_plan["SECTION_REFERENCE_MAP"][0]["heading_scope_mode"] = "comparison"
        bad_scope = validate(article, bad_scope_plan)

    passed = (
        good["status"] == "PASS"
        and bad_tone["status"] == "FAIL"
        and bad_flow["status"] == "FAIL"
        and bad_scope["status"] == "FAIL"
    )
    if not passed:
        print(json.dumps({
            "good": good,
            "bad_tone": bad_tone,
            "bad_flow": bad_flow,
            "bad_scope": bad_scope,
        }, indent=2))
        return 1
    print("PASS: tone, FAQ interruption, and multi-topic H2 scope gates")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plan", nargs="?", type=Path)
    parser.add_argument("article", nargs="?", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        return self_test()
    if args.plan is None or args.article is None:
        parser.error("plan and article are required unless --self-test is used")
    plan = json.loads(args.plan.read_text(encoding="utf-8"))
    result = validate(args.article, plan)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
