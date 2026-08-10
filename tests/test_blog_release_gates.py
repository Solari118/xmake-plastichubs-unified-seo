from __future__ import annotations

import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate_final_blog_release import validate_release  # noqa: E402
from validate_plan_gate import sample, validate as validate_plan  # noqa: E402


ARTICLE = """# Manufacturing Process Guide

## What the process is and when it fits

This process fits plastic parts that need controlled features without dedicated production tooling.

The section defines the process and states the practical fit boundary for a buyer.

## How the process works

The supplier reviews the model, prepares stock, runs the operation, and inspects the resulting part.

Setup, operation, and inspection appear in production order so the workflow remains easy to follow.

## Questions Buyers Ask Before Choosing This Route

### When is the process a poor fit?

It is a poor fit when geometry, material behavior, or required production evidence conflicts with the process.

### Which inputs affect the quote most?

CAD, drawing, material, quantity, tolerance, and finish data define the manufacturing and inspection work.

### What should be verified before production?

The buyer should verify material, critical dimensions, finish zones, and the agreed inspection method.

## Review Your Plastic Part With PlasticHubs

Send PlasticHubs your CAD file, drawing, material, quantity, tolerance, and finish requirements for a process review.

Use the [PlasticHubs engineering contact](https://plastichubs.com/contact-us/) to receive manufacturability feedback and a clear next step.
"""


class BlogReleaseGateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.plan_path = self.root / "plan.json"
        self.article_path = self.root / "article.md"
        self.audit_path = self.root / "section-audit.json"
        self.change_path = self.root / "heading-change.json"
        self.peer_path = self.root / "peer.md"
        self.plan = sample(False)
        self.article_path.write_text(ARTICLE, encoding="utf-8")
        self.plan_path.write_text(json.dumps(self.plan), encoding="utf-8")
        self.change_path.write_text(json.dumps({"changes": []}), encoding="utf-8")
        self.peer_path.write_text(
            "# Peer\n\n## Cost drivers\n\nMaterial and setup determine cost.\n\n"
            "## Inspection evidence\n\nAcceptance records close the article.\n",
            encoding="utf-8",
        )
        first_paragraphs = [
            "This process fits plastic parts that need controlled features without dedicated production tooling.",
            "The supplier reviews the model, prepares stock, runs the operation, and inspects the resulting part.",
            "It is a poor fit when geometry, material behavior, or required production evidence conflicts with the process.",
            "Send PlasticHubs your CAD file, drawing, material, quantity, tolerance, and finish requirements for a process review.",
        ]
        section_excerpts = [
            "The section defines the process and states the practical fit boundary for a buyer.",
            "Setup, operation, and inspection appear in production order so the workflow remains easy to follow.",
            "The buyer should verify material, critical dimensions, finish zones, and the agreed inspection method.",
            "Use the [PlasticHubs engineering contact](https://plastichubs.com/contact-us/) to receive manufacturability feedback and a clear next step.",
        ]
        headings = [item["planned_heading"] for item in self.plan["SECTION_REFERENCE_MAP"]]
        audit = {
            "article_path": "article.md",
            "article_sha256": hashlib.sha256(self.article_path.read_bytes()).hexdigest(),
            "reviewer_stage": "Audit",
            "overall_verdict": "PASS",
            "sections": [],
        }
        for heading, first, excerpt in zip(headings, first_paragraphs, section_excerpts):
            audit["sections"].append({
                "heading": heading,
                "reader_question": "What reader question does this section answer directly?",
                "heading_meaning": "The section must fulfill the exact reader-facing heading promise.",
                "first_paragraph_evidence_excerpt": first,
                "section_evidence_excerpt": excerpt,
                "section_summary": "The section provides a direct answer and bounded supporting detail.",
                "reference_sources": ["https://example1.com/guide"],
                "reference_structure_pattern": "Direct answer followed by concise supporting evidence.",
                "verdict": "PASS",
                "defect_origin": "none",
                "required_route": "none",
            })
        self.audit_path.write_text(json.dumps(audit), encoding="utf-8")

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def test_complete_release_gate_passes(self) -> None:
        result = validate_release(
            self.plan_path,
            self.article_path,
            self.audit_path,
            "PlasticHubs",
            [self.peer_path],
            self.change_path,
        )
        self.assertEqual(result["final_blog_release_gate"], "PASS", result)

    def test_missing_cta_section_in_plan_is_blocked(self) -> None:
        broken = sample(False)
        broken["SECTION_REFERENCE_MAP"] = [
            item for item in broken["SECTION_REFERENCE_MAP"] if item["section_kind"] != "cta"
        ]
        status, errors = validate_plan(broken)
        self.assertEqual(status, "BLOCKED")
        self.assertTrue(any("CTA section" in error for error in errors))

    def test_forbidden_tone_term_blocks_release(self) -> None:
        changed = ARTICLE.replace("This process fits", "However, this process fits")
        self.article_path.write_text(changed, encoding="utf-8")
        audit = json.loads(self.audit_path.read_text(encoding="utf-8"))
        audit["article_sha256"] = hashlib.sha256(self.article_path.read_bytes()).hexdigest()
        audit["sections"][0]["first_paragraph_evidence_excerpt"] = (
            "However, this process fits plastic parts that need controlled features without dedicated production tooling."
        )
        self.audit_path.write_text(json.dumps(audit), encoding="utf-8")
        result = validate_release(
            self.plan_path, self.article_path, self.audit_path, "PlasticHubs",
            [self.peer_path], self.change_path,
        )
        self.assertEqual(result["narrative_quality_gate"], "FAIL", result)
        self.assertEqual(result["final_blog_release_gate"], "FAIL", result)

    def test_unapproved_core_section_after_faq_blocks_release(self) -> None:
        broken = sample(False)
        moved = broken["SECTION_REFERENCE_MAP"].pop(1)
        broken["SECTION_REFERENCE_MAP"].insert(3, moved)
        for index, section in enumerate(broken["SECTION_REFERENCE_MAP"], start=1):
            section["sequence_index"] = index
        broken["FAQ_PLAN"]["allow_substantive_sections_after_faq"] = False
        broken["FAQ_PLAN"]["substantive_sections_after_faq"] = []
        self.plan_path.write_text(json.dumps(broken), encoding="utf-8")
        result = validate_release(
            self.plan_path, self.article_path, self.audit_path, "PlasticHubs",
            [self.peer_path], self.change_path,
        )
        self.assertEqual(result["narrative_quality_gate"], "FAIL", result)
        self.assertEqual(result["final_blog_release_gate"], "FAIL", result)

    def test_narrow_comparison_heading_over_many_h3_topics_blocks_release(self) -> None:
        changed = ARTICLE.replace(
            "## What the process is and when it fits",
            "## A molded texture is not the same as a coating",
        ).replace(
            "The section defines the process and states the practical fit boundary for a buyer.",
            "The section defines the process and states the practical fit boundary for a buyer.\n\n"
            "### Polishing\n\nPolishing changes gloss.\n\n"
            "### Blasting\n\nBlasting changes texture.\n\n"
            "### Printing\n\nPrinting adds graphics.",
        )
        self.article_path.write_text(changed, encoding="utf-8")
        plan = sample(False)
        plan["SECTION_REFERENCE_MAP"][0]["planned_heading"] = (
            "A molded texture is not the same as a coating"
        )
        plan["SECTION_REFERENCE_MAP"][0]["heading_scope_mode"] = "comparison"
        self.plan_path.write_text(json.dumps(plan), encoding="utf-8")
        audit = json.loads(self.audit_path.read_text(encoding="utf-8"))
        audit["article_sha256"] = hashlib.sha256(self.article_path.read_bytes()).hexdigest()
        audit["sections"][0]["heading"] = "A molded texture is not the same as a coating"
        self.audit_path.write_text(json.dumps(audit), encoding="utf-8")
        result = validate_release(
            self.plan_path, self.article_path, self.audit_path, "PlasticHubs",
            [self.peer_path], self.change_path,
        )
        self.assertEqual(result["narrative_quality_gate"], "FAIL", result)
        self.assertEqual(result["final_blog_release_gate"], "FAIL", result)


if __name__ == "__main__":
    unittest.main()
