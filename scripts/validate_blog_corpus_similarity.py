"""Detect repeated semantic and structural article shapes across a Blog corpus."""

from __future__ import annotations

import argparse
import json
import math
import re
import tempfile
from itertools import combinations
from pathlib import Path


def cosine(left: list[float], right: list[float]) -> float:
    size = max(len(left), len(right))
    a = left + [0.0] * (size - len(left))
    b = right + [0.0] * (size - len(right))
    dot = sum(x * y for x, y in zip(a, b))
    denom = math.sqrt(sum(x * x for x in a) * sum(y * y for y in b))
    return dot / denom if denom else 0.0


def role(heading: str) -> str:
    value = heading.lower()
    patterns = [
        ("faq", r"\bfaq\b|frequently asked|questions .* ask"),
        (
            "action",
            r"\bplastichubs\b|\bxmake\b|^(?:ask|request|send|review|contact|upload|"
            r"talk|discuss|evaluate|check|submit|get)\b",
        ),
        ("specification", r"\bspecif|\binspect|\baccept|\btolerance"),
        ("selection", r"^start with\b|^match\b|\bchoose\b|\bwhich\b|\bwhen should\b|\bright process|\bright material|\bdecision\b"),
        ("finish", r"\bfinish|\btexture|\bpolish|\bSPI\b|\bVDI\b"),
        ("comparison", r"\bcompare|\bversus\b|\bvs\.?\b|\bor\b|\bdifference"),
        ("risk-control", r"\brisk|\bstress|\bdefect|\bfail|\bcontrol|\bmatters"),
        ("cost", r"\bcost|\bprice|\blead time"),
        ("design", r"\bdesign|\bgeometry|\btool access"),
        ("process", r"\bmachin|\bprint|\bmold|\bcast|\bprocess|\bmanufactur|\bways to make\b|\bproduction\b"),
        ("orientation", r"^what\b|^why\b|^understanding\b|^guide\b"),
    ]
    for label, pattern in patterns:
        if re.search(pattern, value, re.I):
            return label
    return "other"


def section_data(markdown: str) -> tuple[list[str], list[int]]:
    matches = list(re.finditer(r"(?m)^##\s+(.+?)\s*$", markdown))
    headings: list[str] = []
    counts: list[int] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(markdown)
        headings.append(match.group(1).strip())
        counts.append(len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'-]*", markdown[match.end():end])))
    return headings, counts


def normalize_counts(counts: list[int]) -> list[float]:
    total = sum(counts)
    return [value / total for value in counts] if total else []


def cadence(markdown: str) -> list[float]:
    histogram = [0.0, 0.0, 0.0, 0.0]
    for block in re.split(r"\n\s*\n", markdown):
        stripped = block.strip()
        if (
            not stripped
            or stripped.startswith("#")
            or stripped.startswith(("-", "*", "|", "!["))
        ):
            continue
        sentences = len(re.findall(r"[.!?](?:\s|$)", stripped))
        histogram[min(max(sentences, 1), 4) - 1] += 1
    total = sum(histogram)
    return [value / total for value in histogram] if total else histogram


def structured_line_density(markdown: str) -> float:
    lines = [line for line in markdown.splitlines() if line.strip()]
    if not lines:
        return 0.0
    structured = sum(
        bool(re.match(r"\s*(?:[-*]\s|\d+\.\s|\|)", line))
        for line in lines
    )
    return structured / len(lines)


def fingerprint(path: Path) -> dict[str, object]:
    markdown = path.read_text(encoding="utf-8")
    headings, counts = section_data(markdown)
    roles = [role(heading) for heading in headings]
    return {
        "path": str(path),
        "h2_count": len(headings),
        "roles": roles,
        "first_role": roles[0] if roles else "missing",
        "last_role": roles[-1] if roles else "missing",
        "section_proportions": normalize_counts(counts),
        "paragraph_cadence": cadence(markdown),
        "structured_line_density": structured_line_density(markdown),
    }


def compare(left: dict[str, object], right: dict[str, object]) -> dict[str, object]:
    count_delta = abs(int(left["h2_count"]) - int(right["h2_count"]))
    count_similarity = 1.0 if count_delta == 0 else 0.7 if count_delta == 1 else 0.0
    section_similarity = cosine(
        list(left["section_proportions"]), list(right["section_proportions"])
    )
    cadence_similarity = cosine(
        list(left["paragraph_cadence"]), list(right["paragraph_cadence"])
    )
    edge_role_similarity = (
        (0.5 if left["first_role"] == right["first_role"] else 0.0)
        + (0.5 if left["last_role"] == right["last_role"] else 0.0)
    )
    density_similarity = max(
        0.0,
        1.0 - abs(
            float(left["structured_line_density"]) - float(right["structured_line_density"])
        ) / 0.15,
    )
    score = (
        0.25 * count_similarity
        + 0.30 * section_similarity
        + 0.20 * cadence_similarity
        + 0.15 * edge_role_similarity
        + 0.10 * density_similarity
    )
    reasons = []
    if count_delta <= 1:
        reasons.append("same or near-identical H2 count")
    if section_similarity >= 0.90:
        reasons.append("near-identical section-length distribution")
    if cadence_similarity >= 0.93:
        reasons.append("near-identical paragraph cadence")
    if left["first_role"] == right["first_role"]:
        reasons.append("same opening section role")
    if left["last_role"] == right["last_role"]:
        reasons.append("same ending section role")
    if density_similarity >= 0.90:
        reasons.append("near-identical list/table density")
    status = "FAIL" if score >= 0.72 and len(reasons) >= 3 else "PASS"
    return {
        "left": left["path"],
        "right": right["path"],
        "score": round(score, 3),
        "status": status,
        "reasons": reasons,
        "metrics": {
            "h2_count_delta": count_delta,
            "section_proportion_cosine": round(section_similarity, 3),
            "paragraph_cadence_cosine": round(cadence_similarity, 3),
            "edge_role_similarity": round(edge_role_similarity, 3),
            "list_table_density_similarity": round(density_similarity, 3),
        },
    }


def validate(paths: list[Path]) -> dict[str, object]:
    fingerprints = [fingerprint(path) for path in paths]
    pairs = [compare(left, right) for left, right in combinations(fingerprints, 2)]
    failures = [pair for pair in pairs if pair["status"] == "FAIL"]
    return {
        "status": "FAIL" if failures else "PASS",
        "article_count": len(paths),
        "failed_pair_count": len(failures),
        "fingerprints": fingerprints,
        "pairs": pairs,
        "rule": "literal difference cannot override semantic/shape similarity",
    }


def self_test() -> int:
    root = Path(__file__).resolve().parents[1]
    current = [
        root / "data/processed/runs/ph-week-20260727-three-articles/final"
        / "acrylic-cnc-machining/acrylic-cnc-machining.v3.md",
        root / "data/processed/runs/ph-week-20260727-three-articles/final"
        / "plastic-surface-finish-types/plastic-surface-finish-types.v3.md",
        root / "data/processed/runs/ph-week-20260727-three-articles/final"
        / "small-batch-plastic-manufacturing/small-batch-plastic-manufacturing.v3.md",
    ]
    role_cases = {
        "Start with the decision your batch must support": "selection",
        "Four ways to make a small plastic batch": "process",
        "Cost changes when the design is still changing": "cost",
        "Ask PlasticHubs to compare the process routes": "action",
        "Finishing options for machined acrylic parts": "finish",
        "Review plastic finish samples with PlasticHubs before approval": "action",
    }
    role_errors = {
        heading: {"expected": expected, "actual": role(heading)}
        for heading, expected in role_cases.items()
        if role(heading) != expected
    }
    duplicate_a = """# Process Route A

## How the process works

Material is prepared, processed, and inspected in sequence.

## Choose the route for the part

Geometry, material, and quantity define the selection.

## Cost changes with setup

Setup and tooling move cost between early and repeated units.

## Frequently asked questions

### What affects fit?

Geometry and material affect fit.

### What affects cost?

Setup and quantity affect cost.

### What needs inspection?

Dimensions and finish need inspection.

## Ask PlasticHubs to review the part

Send the model and drawing for review.
"""
    duplicate_b = """# Manufacturing Route B

## How production operates

Stock is prepared, processed, and checked in sequence.

## Select the method for the component

Shape, resin, and batch size define the selection.

## Cost depends on preparation

Preparation and tools move cost between early and repeated units.

## Questions buyers often ask

### What affects suitability?

Shape and resin affect suitability.

### What affects price?

Preparation and quantity affect price.

### What needs verification?

Dimensions and appearance need verification.

## Request a PlasticHubs part review

Send the CAD file and drawing for review.
"""
    diverse_c = """# Plastic Finish Specification

## Separate molded texture from secondary finishing

Mold texture originates in tooling, while secondary finishing changes an individual part.

### Mold texture

Tooling transfers texture during molding.

### Secondary finishing

Polishing or coating changes the molded part.

## Write the acceptance requirement

Define gloss, color, viewing conditions, and protected functional zones.

| Requirement | Inspection |
|---|---|
| Gloss | Approved sample |
| Color | Controlled lighting |

## Frequently asked questions about finish control

### Can one part use two finishes?

Yes, when zones and boundaries are defined.

### Does texture hide defects?

Not every defect is hidden by texture.

### Is a sample enough?

The sample also needs documented viewing conditions.

## Review finish samples with PlasticHubs

Send the material, process, finish zones, and acceptance method for review.
"""
    with tempfile.TemporaryDirectory() as temporary:
        fixture_root = Path(temporary)
        duplicate_a_path = fixture_root / "duplicate-a.md"
        duplicate_b_path = fixture_root / "duplicate-b.md"
        diverse_path = fixture_root / "diverse.md"
        duplicate_a_path.write_text(duplicate_a, encoding="utf-8")
        duplicate_b_path.write_text(duplicate_b, encoding="utf-8")
        diverse_path.write_text(diverse_c, encoding="utf-8")
        duplicate_result = validate([duplicate_a_path, duplicate_b_path])
        diverse_result = validate([duplicate_a_path, diverse_path])
    legacy_result = validate(current) if all(path.exists() for path in current) else None
    result = {
        "role_errors": role_errors,
        "portable_duplicate_status": duplicate_result["status"],
        "portable_diverse_status": diverse_result["status"],
        "legacy_fixture_status": legacy_result["status"] if legacy_result else "NOT_AVAILABLE",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    passed = (
        not role_errors
        and duplicate_result["status"] == "FAIL"
        and diverse_result["status"] == "PASS"
        and (legacy_result is None or legacy_result["status"] == "FAIL")
    )
    return 0 if passed else 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("articles", nargs="*", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        return self_test()
    if len(args.articles) < 2:
        parser.error("at least two article paths are required")
    result = validate(args.articles)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
