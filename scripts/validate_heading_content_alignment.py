"""Hard-gate an independent per-H2 heading-to-content semantic audit."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import tempfile
from pathlib import Path
from typing import Any


ENTRY_FIELDS = (
    "heading", "reader_question", "heading_meaning",
    "first_paragraph_evidence_excerpt", "section_evidence_excerpt",
    "section_summary", "reference_sources", "reference_structure_pattern",
    "verdict", "defect_origin", "required_route",
)


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().casefold()


def word_count(text: str) -> int:
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'-]*", text))


def parse_h2_sections(text: str) -> list[tuple[str, str, str]]:
    matches = list(re.finditer(r"(?m)^## (?!#)(.+?)\s*$", text))
    sections: list[tuple[str, str, str]] = []
    for index, match in enumerate(matches):
        body_start = match.end()
        body_end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        body = text[body_start:body_end].strip()
        paragraphs = [
            block.strip()
            for block in re.split(r"\n\s*\n", body)
            if block.strip() and not block.lstrip().startswith(("### ", "|", "-", "*"))
        ]
        first_paragraph = paragraphs[0] if paragraphs else body
        sections.append((match.group(1).strip(), body, first_paragraph))
    return sections


def validate(article: Path, audit: dict[str, Any]) -> tuple[str, list[str]]:
    errors: list[str] = []
    article_text = article.read_text(encoding="utf-8")
    article_hash = hashlib.sha256(article.read_bytes()).hexdigest()
    if audit.get("reviewer_stage") != "Audit":
        errors.append("reviewer_stage must be Audit; a writer self-check cannot satisfy this gate")
    if audit.get("article_sha256") != article_hash:
        errors.append("article_sha256 does not match the audited article")
    sections = parse_h2_sections(article_text)
    records = audit.get("sections")
    if not isinstance(records, list):
        return "FAIL", errors + ["sections must be an array"]
    if len(records) != len(sections):
        errors.append(
            f"section count mismatch: article has {len(sections)} H2 sections, audit has {len(records)}"
        )
    for index, (heading, body, first_paragraph) in enumerate(sections):
        if index >= len(records) or not isinstance(records[index], dict):
            errors.append(f"H2 {index + 1} has no complete audit record")
            continue
        record = records[index]
        for field in ENTRY_FIELDS:
            value = record.get(field)
            if value is None or value == "" or value == []:
                errors.append(f"H2 {index + 1} missing {field}")
        for field, minimum in (
            ("reader_question", 5),
            ("heading_meaning", 6),
            ("first_paragraph_evidence_excerpt", 8),
            ("section_evidence_excerpt", 6),
            ("section_summary", 8),
            ("reference_structure_pattern", 5),
        ):
            if word_count(str(record.get(field, ""))) < minimum:
                errors.append(f"H2 {index + 1} {field} is too thin for an auditable semantic decision")
        sources = record.get("reference_sources")
        if not isinstance(sources, list) or not sources or any(
            not str(source).startswith(("https://", "http://")) for source in sources
        ):
            errors.append(f"H2 {index + 1} reference_sources must contain Top-10 HTTP(S) URLs")
        if record.get("heading") != heading:
            errors.append(
                f"H2 {index + 1} heading mismatch: article={heading!r}, audit={record.get('heading')!r}"
            )
        first_excerpt = normalize(str(record.get("first_paragraph_evidence_excerpt", "")))
        section_excerpt = normalize(str(record.get("section_evidence_excerpt", "")))
        if first_excerpt and first_excerpt not in normalize(first_paragraph):
            errors.append(f"H2 {index + 1} first-paragraph evidence is not present in the first paragraph")
        if section_excerpt and section_excerpt not in normalize(body):
            errors.append(f"H2 {index + 1} section evidence is not present in the section body")
        verdict = record.get("verdict")
        origin = record.get("defect_origin")
        route = record.get("required_route")
        if verdict != "PASS":
            errors.append(f"H2 {index + 1} semantic alignment verdict is not PASS")
        if verdict == "PASS" and (origin != "none" or route != "none"):
            errors.append(f"H2 {index + 1} PASS requires defect_origin=none and required_route=none")
        if verdict == "FAIL" and origin == "info" and route != "Info -> Audit":
            errors.append(f"H2 {index + 1} Info defect must route Info -> Audit")
        if verdict == "FAIL" and origin == "plan" and route != "Plan -> Info -> Audit":
            errors.append(f"H2 {index + 1} Plan defect must route Plan -> Info -> Audit")
    if audit.get("overall_verdict") != ("PASS" if not errors else "FAIL"):
        errors.append("overall_verdict is inconsistent with section evidence")
    return ("PASS", []) if not errors else ("FAIL", errors)


def self_test() -> int:
    article_text = """# Test

## When CNC machining fits an acrylic part

CNC machining fits acrylic parts that need accurate features on several faces without dedicated tooling.

The process can combine bores, pockets, threads, and engraving while retaining specified stock material.
"""
    with tempfile.TemporaryDirectory() as temporary:
        article = Path(temporary) / "article.md"
        article.write_text(article_text, encoding="utf-8")
        article_hash = hashlib.sha256(article.read_bytes()).hexdigest()
        good = {
            "article_path": "article.md",
            "article_sha256": article_hash,
            "reviewer_stage": "Audit",
            "overall_verdict": "PASS",
            "sections": [{
                "heading": "When CNC machining fits an acrylic part",
                "reader_question": "When does CNC machining fit an acrylic part?",
                "heading_meaning": "The section must state practical process suitability conditions.",
                "first_paragraph_evidence_excerpt": "CNC machining fits acrylic parts that need accurate features on several faces without dedicated tooling.",
                "section_evidence_excerpt": "The process can combine bores, pockets, threads, and engraving while retaining specified stock material.",
                "section_summary": "The section answers process fit and names the supported feature scope.",
                "reference_sources": ["https://example.com/top-ten-guide"],
                "reference_structure_pattern": "Direct suitability answer followed by bounded process detail.",
                "verdict": "PASS",
                "defect_origin": "none",
                "required_route": "none",
            }],
        }
        good_status, good_errors = validate(article, good)
        thin = json.loads(json.dumps(good))
        thin["sections"][0]["section_evidence_excerpt"] = "The process"
        thin_status, _ = validate(article, thin)
        wrong_stage = json.loads(json.dumps(good))
        wrong_stage["reviewer_stage"] = "Info"
        wrong_stage_status, _ = validate(article, wrong_stage)
    if (good_status, good_errors) != ("PASS", []) or thin_status != "FAIL" or wrong_stage_status != "FAIL":
        print(json.dumps({
            "good": [good_status, good_errors],
            "thin": thin_status,
            "wrong_stage": wrong_stage_status,
        }, indent=2))
        return 1
    print("PASS: H2 alignment evidence, minimum depth, URL provenance, hash, and Audit-stage gates")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("article", nargs="?", type=Path)
    parser.add_argument("audit", nargs="?", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        return self_test()
    if args.article is None or args.audit is None:
        parser.error("article and audit are required unless --self-test is used")
    data = json.loads(args.audit.read_text(encoding="utf-8"))
    status, errors = validate(args.article, data)
    print(json.dumps({"section_alignment_gate_status": status, "errors": errors}, indent=2))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
