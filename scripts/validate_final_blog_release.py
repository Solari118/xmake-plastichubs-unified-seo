"""Run the complete machine gate required before Blog Final Output."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from validate_blog_conversion_modules import validate as validate_conversion
from validate_blog_corpus_similarity import validate as validate_corpus
from validate_blog_narrative_quality import validate as validate_narrative_quality
from validate_heading_content_alignment import parse_h2_sections, validate as validate_alignment
from validate_plan_gate import validate as validate_plan


def nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate_heading_contract(
    plan: dict[str, Any],
    article: Path,
    alignment: dict[str, Any],
    heading_change_record: dict[str, Any] | None,
) -> list[str]:
    errors: list[str] = []
    section_map = plan.get("SECTION_REFERENCE_MAP")
    if not isinstance(section_map, list):
        return ["Plan SECTION_REFERENCE_MAP is missing"]
    actual_headings = [heading for heading, _, _ in parse_h2_sections(article.read_text(encoding="utf-8"))]
    planned_headings = [str(section.get("planned_heading", "")).strip() for section in section_map]
    changes = heading_change_record.get("changes", []) if isinstance(heading_change_record, dict) else []
    if not isinstance(changes, list):
        return ["HEADING_CHANGE_RECORD changes must be an array"]
    change_map: dict[str, str] = {}
    for index, change in enumerate(changes, start=1):
        if not isinstance(change, dict):
            errors.append(f"heading change {index} must be an object")
            continue
        for field in ("old_heading", "new_heading", "reason", "reader_question", "body_change"):
            if not nonempty(change.get(field)):
                errors.append(f"heading change {index} missing {field}")
        if change.get("first_paragraph_matches_new_heading") is not True:
            errors.append(f"heading change {index} lacks first-paragraph confirmation")
        old = str(change.get("old_heading", "")).strip()
        new = str(change.get("new_heading", "")).strip()
        if old:
            change_map[old] = new
    expected_headings = [change_map.get(heading, heading) for heading in planned_headings]
    if expected_headings != actual_headings:
        errors.append(
            "article H2 sequence does not match SECTION_REFERENCE_MAP plus approved HEADING_CHANGE_RECORD"
        )
    audit_sections = alignment.get("sections")
    if isinstance(audit_sections, list) and len(audit_sections) == len(section_map):
        for index, (planned, audited) in enumerate(zip(section_map, audit_sections), start=1):
            planned_urls = set(planned.get("reference_urls", [])) if isinstance(planned, dict) else set()
            audited_urls = set(audited.get("reference_sources", [])) if isinstance(audited, dict) else set()
            if not planned_urls.intersection(audited_urls):
                errors.append(f"H2 {index} Audit reference does not match its Plan Top-10 section source")
    else:
        errors.append("Audit section count cannot be reconciled with SECTION_REFERENCE_MAP")
    return errors


def validate_release(
    plan_path: Path,
    article_path: Path,
    alignment_path: Path,
    brand: str,
    corpus_paths: list[Path],
    heading_change_path: Path | None,
) -> dict[str, Any]:
    plan = json.loads(plan_path.read_text(encoding="utf-8"))
    alignment = json.loads(alignment_path.read_text(encoding="utf-8"))
    heading_change = (
        json.loads(heading_change_path.read_text(encoding="utf-8"))
        if heading_change_path else None
    )
    plan_status, plan_errors = validate_plan(plan)
    alignment_status, alignment_errors = validate_alignment(article_path, alignment)
    conversion = validate_conversion(article_path.read_text(encoding="utf-8"), brand)
    narrative_quality = validate_narrative_quality(article_path, plan)
    corpus_articles = [article_path] + [path for path in corpus_paths if path.resolve() != article_path.resolve()]
    corpus = validate_corpus(corpus_articles) if len(corpus_articles) >= 2 else {
        "status": "FAIL",
        "failed_pair_count": 0,
        "error": "at least one recent same-brand comparison article is required",
    }
    heading_errors = validate_heading_contract(
        plan, article_path, alignment, heading_change
    )
    errors = (
        [f"Plan: {error}" for error in plan_errors]
        + [f"Alignment: {error}" for error in alignment_errors]
        + [f"Heading contract: {error}" for error in heading_errors]
        + [f"Conversion: {error}" for error in conversion.get("errors", [])]
        + [f"Narrative quality: {error}" for error in narrative_quality.get("errors", [])]
    )
    if plan_status != "PASS" and not plan_errors:
        errors.append(f"Plan gate status is {plan_status}, not PASS")
    if corpus.get("status") != "PASS":
        errors.append("Corpus similarity gate did not pass")
    status = "PASS" if (
        plan_status == "PASS"
        and alignment_status == "PASS"
        and conversion.get("status") == "PASS"
        and narrative_quality.get("status") == "PASS"
        and corpus.get("status") == "PASS"
        and not heading_errors
    ) else "FAIL"
    return {
        "final_blog_release_gate": status,
        "plan_gate": plan_status,
        "section_alignment_gate": alignment_status,
        "heading_contract_gate": "PASS" if not heading_errors else "FAIL",
        "conversion_gate": conversion.get("status"),
        "narrative_quality_gate": narrative_quality.get("status"),
        "corpus_gate": corpus.get("status"),
        "corpus_failed_pair_count": corpus.get("failed_pair_count"),
        "errors": errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plan", type=Path)
    parser.add_argument("article", type=Path)
    parser.add_argument("section_audit", type=Path)
    parser.add_argument("--brand", required=True, choices=["XMAKE", "PlasticHubs"])
    parser.add_argument("--corpus", nargs="+", required=True, type=Path)
    parser.add_argument("--heading-change-record", type=Path)
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()
    result = validate_release(
        args.plan,
        args.article,
        args.section_audit,
        args.brand,
        args.corpus,
        args.heading_change_record,
    )
    if args.receipt:
        args.receipt.parent.mkdir(parents=True, exist_ok=True)
        args.receipt.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["final_blog_release_gate"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
