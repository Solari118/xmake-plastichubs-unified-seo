"""Validate SERP access, Top-10 completeness, and explicit route approvals."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


RESULT_FIELDS = (
    "position", "title", "url", "domain", "content_type", "record_type",
    "primary_intent", "primary_audience", "content_format", "outline",
    "title_alignment", "heading_hierarchy", "narrative_sequence",
    "opening_mode", "intent_resolution_point", "section_length_pattern",
    "list_table_placement", "pacing", "style_profile", "complexity_load",
    "english_naturalness", "ai_pattern_risks", "evidence_form",
    "commercial_intensity", "cta_position", "strengths", "gaps",
    "ranking_hypotheses",
)
PROPOSAL_FIELDS = (
    "reason", "expected_gain", "ranking_risk", "audience_effect", "measurement_plan",
)
EDITORIAL_TYPES = {
    "editorial-blog", "knowledge-guide", "technical-article",
    "tutorial-article", "comparison-article",
}
SHAPE_FIELDS = (
    "opening_length_and_stance", "intent_resolution_point", "title_alignment",
    "heading_hierarchy", "section_count_or_range", "section_length_pattern",
    "narrative_sequence", "heading_grammar", "paragraph_cadence", "evidence_density",
    "list_and_table_behavior", "faq_placement_and_form", "cta_placement_and_form",
    "ending_form", "complexity_load", "english_naturalness_and_ai_risk",
)
RHYTHM_FIELDS = (
    "primary_controller", "secondary_contributions", "rhythm_rationale",
    "anti_convergence_guard",
)
FAQ_FIELDS = (
    "heading", "question_count", "question_sources", "placement",
    "questions", "duplication_guard", "allow_substantive_sections_after_faq",
    "substantive_sections_after_faq", "placement_rationale",
    "placement_reference_urls",
)
CTA_FIELDS = (
    "heading_or_callout", "placement", "action", "destination_url",
    "input_request", "reader_value", "same_brand_url_status", "variation_note",
)
SECTION_REFERENCE_FIELDS = (
    "planned_heading", "section_kind", "sequence_index", "sequence_reason",
    "heading_scope_mode", "reference_result_positions",
    "reference_urls", "reference_heading_patterns", "reference_information_order",
    "reader_question", "first_paragraph_answer_requirement", "body_scope",
    "excluded_scope", "adaptation_note", "originality_guard",
)
BRAND_DOMAINS = {
    "XMAKE": "xmake.com",
    "PlasticHubs": "plastichubs.com",
}


def nonempty(value: Any) -> bool:
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, dict)):
        return bool(value)
    return value is not None


def distribution(rows: list[dict[str, Any]], field: str) -> dict[str, int]:
    return dict(Counter(str(row.get(field, "")).strip() for row in rows))


def validate_blog_contract(data: dict[str, Any], errors: list[str]) -> None:
    for field, required_fields in (
        ("REFERENCE_SHAPE_FINGERPRINT", SHAPE_FIELDS),
        ("ARTICLE_RHYTHM_ROUTE", RHYTHM_FIELDS),
    ):
        value = data.get(field)
        if not isinstance(value, dict):
            errors.append(f"{field} must be a complete object")
            continue
        for required in required_fields:
            if not nonempty(value.get(required)):
                errors.append(f"{field} missing {required}")

    section_map = data.get("SECTION_REFERENCE_MAP")
    if not isinstance(section_map, list) or len(section_map) < 3:
        errors.append("SECTION_REFERENCE_MAP must contain at least three planned public H2 sections")
    else:
        top_ten = data.get("TOP_TEN_SERP_RESULTS")
        top_urls = {
            str(row.get("url", "")).strip()
            for row in top_ten
            if isinstance(row, dict)
        } if isinstance(top_ten, list) else set()
        headings: list[str] = []
        section_kinds: set[str] = set()
        for index, section in enumerate(section_map, start=1):
            if not isinstance(section, dict):
                errors.append(f"SECTION_REFERENCE_MAP item {index} must be an object")
                continue
            for field in SECTION_REFERENCE_FIELDS:
                if field == "excluded_scope":
                    if not isinstance(section.get(field), list):
                        errors.append(f"SECTION_REFERENCE_MAP item {index} {field} must be an array")
                elif not nonempty(section.get(field)):
                    errors.append(f"SECTION_REFERENCE_MAP item {index} missing {field}")
            heading = str(section.get("planned_heading", "")).strip()
            if heading:
                headings.append(heading.casefold())
            section_kind = str(section.get("section_kind", "")).strip().lower()
            section_kinds.add(section_kind)
            if section.get("sequence_index") != index:
                errors.append(
                    f"SECTION_REFERENCE_MAP item {index} sequence_index must equal its 1-based position"
                )
            if len(str(section.get("sequence_reason", "")).split()) < 5:
                errors.append(
                    f"SECTION_REFERENCE_MAP item {index} sequence_reason is too thin"
                )
            scope_mode = str(section.get("heading_scope_mode", "")).strip()
            allowed_scope_modes = {
                "core": {"single-topic", "comparison", "multi-topic-umbrella"},
                "faq": {"faq"},
                "cta": {"cta"},
            }
            if scope_mode not in allowed_scope_modes.get(section_kind, set()):
                errors.append(
                    f"SECTION_REFERENCE_MAP item {index} heading_scope_mode is incompatible with section_kind"
                )
            positions = section.get("reference_result_positions")
            if not isinstance(positions, list) or not positions or any(
                not isinstance(position, int) or not 1 <= position <= 10
                for position in positions
            ):
                errors.append(
                    f"SECTION_REFERENCE_MAP item {index} reference_result_positions must use Top-10 positions 1-10"
                )
            urls = section.get("reference_urls")
            if not isinstance(urls, list) or not urls:
                errors.append(f"SECTION_REFERENCE_MAP item {index} reference_urls must be non-empty")
            else:
                for url in urls:
                    if str(url).strip() not in top_urls:
                        errors.append(
                            f"SECTION_REFERENCE_MAP item {index} reference URL is not in TOP_TEN_SERP_RESULTS: {url}"
                        )
        if len(headings) != len(set(headings)):
            errors.append("SECTION_REFERENCE_MAP planned_heading values must be unique")
        if "faq" not in section_kinds:
            errors.append("SECTION_REFERENCE_MAP must contain a FAQ section")
        if "cta" not in section_kinds:
            errors.append("SECTION_REFERENCE_MAP must contain a CTA section")
        faq_headings = [
            str(section.get("planned_heading", "")).strip()
            for section in section_map
            if isinstance(section, dict) and section.get("section_kind") == "faq"
        ]
        planned_faq_heading = str(data.get("FAQ_PLAN", {}).get("heading", "")).strip()
        if planned_faq_heading and faq_headings != [planned_faq_heading]:
            errors.append("SECTION_REFERENCE_MAP FAQ heading must match FAQ_PLAN heading")
        cta_headings = [
            str(section.get("planned_heading", "")).strip()
            for section in section_map
            if isinstance(section, dict) and section.get("section_kind") == "cta"
        ]
        planned_cta_heading = str(data.get("CTA", {}).get("heading_or_callout", "")).strip()
        if planned_cta_heading and cta_headings != [planned_cta_heading]:
            errors.append("SECTION_REFERENCE_MAP CTA heading must match CTA heading_or_callout")

    mandatory = data.get("MANDATORY_MODULES")
    normalized = {
        str(item).strip().lower()
        for item in mandatory
    } if isinstance(mandatory, list) else set()
    if "faq" not in normalized:
        errors.append("MANDATORY_MODULES must contain FAQ")
    if "cta" not in normalized:
        errors.append("MANDATORY_MODULES must contain CTA")

    omitted = data.get("MODULES_TO_OMIT")
    omitted_normalized = {
        str(item).strip().lower()
        for item in omitted
    } if isinstance(omitted, list) else set()
    if "faq" in omitted_normalized or "cta" in omitted_normalized:
        errors.append("MODULES_TO_OMIT must not contain FAQ or CTA")

    faq = data.get("FAQ_PLAN")
    if not isinstance(faq, dict):
        errors.append("FAQ_PLAN must be a complete object")
    else:
        for field in FAQ_FIELDS:
            if field == "substantive_sections_after_faq":
                if not isinstance(faq.get(field), list):
                    errors.append(f"FAQ_PLAN {field} must be an array")
            elif field == "allow_substantive_sections_after_faq":
                if not isinstance(faq.get(field), bool):
                    errors.append(f"FAQ_PLAN {field} must be boolean")
            elif not nonempty(faq.get(field)):
                errors.append(f"FAQ_PLAN missing {field}")
        questions = faq.get("questions")
        count = faq.get("question_count")
        if not isinstance(questions, list) or not 3 <= len(questions) <= 6:
            errors.append("FAQ_PLAN questions must contain 3 to 6 questions")
        if not isinstance(count, int) or not 3 <= count <= 6:
            errors.append("FAQ_PLAN question_count must be between 3 and 6")
        elif isinstance(questions, list) and count != len(questions):
            errors.append("FAQ_PLAN question_count must match questions length")
        if isinstance(section_map, list):
            faq_indexes = [
                index for index, section in enumerate(section_map)
                if isinstance(section, dict) and section.get("section_kind") == "faq"
            ]
            if len(faq_indexes) == 1:
                faq_index = faq_indexes[0]
                actual_after = [
                    str(section.get("planned_heading", "")).strip()
                    for section in section_map[faq_index + 1:]
                    if isinstance(section, dict) and section.get("section_kind") == "core"
                ]
                declared_after = faq.get("substantive_sections_after_faq")
                if declared_after != actual_after:
                    errors.append(
                        "FAQ_PLAN substantive_sections_after_faq must match core sections placed after FAQ"
                    )
                if actual_after and faq.get("allow_substantive_sections_after_faq") is not True:
                    errors.append(
                        "core sections after FAQ require allow_substantive_sections_after_faq=true"
                    )
                if not actual_after and faq.get("allow_substantive_sections_after_faq") is not False:
                    errors.append(
                        "allow_substantive_sections_after_faq must be false when no core section follows FAQ"
                    )
        if len(str(faq.get("placement_rationale", "")).split()) < 8:
            errors.append("FAQ_PLAN placement_rationale is too thin")
        placement_urls = faq.get("placement_reference_urls")
        top_urls = {
            str(row.get("url", "")).strip()
            for row in data.get("TOP_TEN_SERP_RESULTS", [])
            if isinstance(row, dict)
        }
        if not isinstance(placement_urls, list) or not placement_urls:
            errors.append("FAQ_PLAN placement_reference_urls must be non-empty")
        elif any(str(url).strip() not in top_urls for url in placement_urls):
            errors.append("FAQ_PLAN placement_reference_urls must belong to TOP_TEN_SERP_RESULTS")

    cta = data.get("CTA")
    if not isinstance(cta, dict):
        errors.append("CTA must be a complete object")
    else:
        for field in CTA_FIELDS:
            if not nonempty(cta.get(field)):
                errors.append(f"CTA missing {field}")
        url = str(cta.get("destination_url", "")).strip()
        host = (urlparse(url).hostname or "").lower()
        expected_domain = BRAND_DOMAINS.get(str(data.get("BRAND", "")))
        if not url.startswith(("https://", "http://")):
            errors.append("CTA destination_url must be absolute")
        elif not expected_domain or not (
            host == expected_domain or host.endswith(f".{expected_domain}")
        ):
            errors.append("CTA destination_url must use the selected brand domain")
        if cta.get("same_brand_url_status") != "verified":
            errors.append("CTA same_brand_url_status must be verified")


def validate(data: dict[str, Any]) -> tuple[str, list[str]]:
    errors: list[str] = []
    access_status = data.get("SERP_ACCESS_STATUS")
    browser_status = data.get("USER_BROWSER_VERIFICATION_STATUS")
    downgrade_status = data.get("BEST_EFFORT_DOWNGRADE_APPROVAL")
    benchmark_status = data.get("SERP_BENCHMARK_STATUS")

    if access_status == "google-verification-required":
        if browser_status != "pending":
            errors.append("Google verification requires USER_BROWSER_VERIFICATION_STATUS=pending")
        if benchmark_status != "Blocked":
            errors.append("Google verification challenge requires SERP_BENCHMARK_STATUS=Blocked until resolved or downgrade-approved")
        if data.get("PLAN_GATE_STATUS") != "WAITING_FOR_USER_BROWSER_VERIFICATION":
            errors.append("Google verification challenge requires PLAN_GATE_STATUS=WAITING_FOR_USER_BROWSER_VERIFICATION")
        return ("BLOCKED", errors) if errors else ("WAITING_FOR_USER_BROWSER_VERIFICATION", [])

    if access_status == "tool-permission-required":
        if benchmark_status != "Blocked":
            errors.append("Tool permission block requires SERP_BENCHMARK_STATUS=Blocked")
        if data.get("PLAN_GATE_STATUS") != "WAITING_FOR_TOOL_PERMISSION":
            errors.append("Tool permission block requires PLAN_GATE_STATUS=WAITING_FOR_TOOL_PERMISSION")
        return ("BLOCKED", errors) if errors else ("WAITING_FOR_TOOL_PERMISSION", [])

    if access_status == "blocked":
        return "BLOCKED", ["SERP_ACCESS_STATUS is blocked"]

    if access_status == "exact-positions-verified":
        if benchmark_status != "Validated":
            errors.append("exact-positions-verified requires SERP_BENCHMARK_STATUS=Validated")
        if browser_status not in {"not-required", "completed"}:
            errors.append("exact positions require browser verification to be not-required or completed")
        if downgrade_status != "not-required":
            errors.append("exact positions require BEST_EFFORT_DOWNGRADE_APPROVAL=not-required")
    elif access_status == "best-effort-approved":
        if benchmark_status != "Best-effort":
            errors.append("best-effort-approved requires SERP_BENCHMARK_STATUS=Best-effort")
        if downgrade_status != "approved":
            errors.append("Best-effort requires explicit BEST_EFFORT_DOWNGRADE_APPROVAL=approved")
        if not nonempty(data.get("BEST_EFFORT_DOWNGRADE_APPROVAL_EVIDENCE")):
            errors.append("Best-effort requires explicit downgrade approval evidence")
    else:
        errors.append("SERP_ACCESS_STATUS is missing or invalid")

    rows = data.get("TOP_TEN_SERP_RESULTS")
    if not isinstance(rows, list) or len(rows) != 10:
        return "BLOCKED", ["TOP_TEN_SERP_RESULTS must contain exactly 10 analyzed editorial/blog records"]

    positions: list[int] = []
    for index, row in enumerate(rows, start=1):
        if not isinstance(row, dict):
            errors.append(f"result {index} must be an object")
            continue
        for field in RESULT_FIELDS:
            if not nonempty(row.get(field)):
                errors.append(f"result {index} missing {field}")
        if row.get("content_type") not in EDITORIAL_TYPES:
            errors.append(f"result {index} is not an allowed editorial/blog content_type")
        if row.get("record_type") == "substitute" and not nonempty(row.get("substitution_reason")):
            errors.append(f"result {index} substitute requires substitution_reason")
        if not str(row.get("url", "")).startswith(("https://", "http://")):
            errors.append(f"result {index} URL must be absolute")
        if isinstance(row.get("position"), int):
            positions.append(row["position"])
    if len(positions) != len(set(positions)):
        errors.append("SERP positions must be unique")

    actual_intents = distribution(rows, "primary_intent")
    actual_audiences = distribution(rows, "primary_audience")
    actual_formats = distribution(rows, "content_format")
    declared = (
        ("SERP_INTENT_DISTRIBUTION", actual_intents),
        ("SERP_AUDIENCE_DISTRIBUTION", actual_audiences),
        ("SERP_FORMAT_DISTRIBUTION", actual_formats),
    )
    for field, actual in declared:
        if data.get(field) != actual:
            errors.append(f"{field} does not match the ten per-page records")

    dominant_checks = (
        ("DOMINANT_SERP_INTENT", actual_intents),
        ("DOMINANT_AUDIENCE", actual_audiences),
        ("DOMINANT_CONTENT_FORMAT", actual_formats),
    )
    for field, actual in dominant_checks:
        value = data.get(field)
        if not actual or value not in actual or actual[value] != max(actual.values()):
            errors.append(f"{field} is not a highest-count classification")

    validate_blog_contract(data, errors)

    if data.get("TOP_TEN_COMPLETENESS_STATUS") != "complete":
        errors.append("TOP_TEN_COMPLETENESS_STATUS must be complete before Info")
    if benchmark_status == "Blocked":
        return "BLOCKED", errors or ["SERP_BENCHMARK_STATUS is Blocked"]

    intent_changed = data.get("SELECTED_PRIMARY_INTENT") != data.get("DOMINANT_SERP_INTENT")
    format_changed = data.get("SELECTED_CONTENT_FORMAT") != data.get("DOMINANT_CONTENT_FORMAT")
    is_alternative = intent_changed or format_changed

    if is_alternative:
        proposal = data.get("INTENT_CHANGE_PROPOSAL")
        if not isinstance(proposal, dict):
            errors.append("alternative intent/format requires INTENT_CHANGE_PROPOSAL")
        else:
            for field in PROPOSAL_FIELDS:
                if not nonempty(proposal.get(field)):
                    errors.append(f"INTENT_CHANGE_PROPOSAL missing {field}")
        if data.get("USER_INTENT_APPROVAL") == "approved":
            if data.get("ANGLE_ALIGNMENT_STATUS") != "alternative-approved":
                errors.append("approved alternative requires ANGLE_ALIGNMENT_STATUS=alternative-approved")
            if not nonempty(data.get("USER_INTENT_APPROVAL_EVIDENCE")):
                errors.append("approved alternative requires explicit USER_INTENT_APPROVAL_EVIDENCE")
            expected_status = "PASS"
        else:
            if data.get("ANGLE_ALIGNMENT_STATUS") != "approval-required":
                errors.append("unapproved alternative requires ANGLE_ALIGNMENT_STATUS=approval-required")
            if data.get("USER_INTENT_APPROVAL") != "pending":
                errors.append("unapproved alternative requires USER_INTENT_APPROVAL=pending")
            expected_status = "WAITING_FOR_INTENT_APPROVAL"
    else:
        if data.get("ANGLE_ALIGNMENT_STATUS") != "aligned":
            errors.append("SERP-aligned route requires ANGLE_ALIGNMENT_STATUS=aligned")
        if data.get("USER_INTENT_APPROVAL") != "not-required":
            errors.append("SERP-aligned route requires USER_INTENT_APPROVAL=not-required")
        expected_status = "PASS"

    if data.get("PLAN_GATE_STATUS") != expected_status:
        errors.append(f"PLAN_GATE_STATUS must be {expected_status}")
    if errors:
        return "BLOCKED", errors
    return expected_status, []


def receipt(data: dict[str, Any], status: str, errors: list[str]) -> dict[str, Any]:
    return {
        "plan_gate_status": status,
        "top_ten_record_count": len(data.get("TOP_TEN_SERP_RESULTS", []))
        if isinstance(data.get("TOP_TEN_SERP_RESULTS"), list) else 0,
        "top_ten_completeness_status": data.get("TOP_TEN_COMPLETENESS_STATUS"),
        "serp_benchmark_status": data.get("SERP_BENCHMARK_STATUS"),
        "serp_access_status": data.get("SERP_ACCESS_STATUS"),
        "user_browser_verification_status": data.get("USER_BROWSER_VERIFICATION_STATUS"),
        "best_effort_downgrade_approval": data.get("BEST_EFFORT_DOWNGRADE_APPROVAL"),
        "best_effort_downgrade_approval_evidence": data.get("BEST_EFFORT_DOWNGRADE_APPROVAL_EVIDENCE"),
        "intent_distribution": data.get("SERP_INTENT_DISTRIBUTION"),
        "dominant_serp_intent": data.get("DOMINANT_SERP_INTENT"),
        "selected_primary_intent": data.get("SELECTED_PRIMARY_INTENT"),
        "audience_distribution": data.get("SERP_AUDIENCE_DISTRIBUTION"),
        "dominant_audience": data.get("DOMINANT_AUDIENCE"),
        "format_distribution": data.get("SERP_FORMAT_DISTRIBUTION"),
        "dominant_content_format": data.get("DOMINANT_CONTENT_FORMAT"),
        "selected_content_format": data.get("SELECTED_CONTENT_FORMAT"),
        "angle_alignment_status": data.get("ANGLE_ALIGNMENT_STATUS"),
        "user_intent_approval": data.get("USER_INTENT_APPROVAL"),
        "faq_gate": "PASS" if isinstance(data.get("FAQ_PLAN"), dict) else "FAIL",
        "cta_gate": "PASS" if isinstance(data.get("CTA"), dict) else "FAIL",
        "section_reference_count": len(data.get("SECTION_REFERENCE_MAP", []))
        if isinstance(data.get("SECTION_REFERENCE_MAP"), list) else 0,
        "errors": errors,
    }


def sample(alternative: bool, approved: bool = False) -> dict[str, Any]:
    rows = []
    for position in range(1, 11):
        rows.append({
            "position": position,
            "title": f"Guide {position}",
            "url": f"https://example{position}.com/guide",
            "domain": f"example{position}.com",
            "content_type": "knowledge-guide",
            "record_type": "observed",
            "primary_intent": "mixed-informational-commercial",
            "primary_audience": "prospective manufacturing buyer",
            "content_format": "introductory-guide",
            "outline": ["definition", "process", "applications"],
            "title_alignment": "core sections directly answer the title promise",
            "heading_hierarchy": "one H1, task-led H2s, selective dependent H3s",
            "narrative_sequence": ["definition", "fit", "process", "applications", "next step"],
            "opening_mode": "definition",
            "intent_resolution_point": "first paragraph",
            "section_length_pattern": "short opening, longer core sections, concise ending",
            "list_table_placement": "one comparison list in the middle when useful",
            "pacing": "broad and accessible",
            "style_profile": "plain commercial education",
            "complexity_load": "buyer-friendly with defined technical terms",
            "english_naturalness": "plain editorial English",
            "ai_pattern_risks": "repeated symmetric sections and generic transitions",
            "evidence_form": "process explanation",
            "commercial_intensity": "moderate",
            "cta_position": "closing",
            "strengths": ["clear introduction"],
            "gaps": ["limited differentiation"],
            "ranking_hypotheses": ["intent alignment may contribute"],
        })
    data: dict[str, Any] = {
        "BRAND": "PlasticHubs",
        "SERP_BENCHMARK_STATUS": "Validated",
        "SERP_ACCESS_STATUS": "exact-positions-verified",
        "USER_BROWSER_VERIFICATION_STATUS": "not-required",
        "BEST_EFFORT_DOWNGRADE_APPROVAL": "not-required",
        "BEST_EFFORT_DOWNGRADE_APPROVAL_EVIDENCE": "",
        "TOP_TEN_SERP_RESULTS": rows,
        "TOP_TEN_COMPLETENESS_STATUS": "complete",
        "SERP_INTENT_DISTRIBUTION": {"mixed-informational-commercial": 10},
        "DOMINANT_SERP_INTENT": "mixed-informational-commercial",
        "SERP_AUDIENCE_DISTRIBUTION": {"prospective manufacturing buyer": 10},
        "DOMINANT_AUDIENCE": "prospective manufacturing buyer",
        "SERP_FORMAT_DISTRIBUTION": {"introductory-guide": 10},
        "DOMINANT_CONTENT_FORMAT": "introductory-guide",
        "SELECTED_PRIMARY_INTENT": "technical-troubleshooting" if alternative else "mixed-informational-commercial",
        "SELECTED_CONTENT_FORMAT": "failure-investigation" if alternative else "introductory-guide",
        "SELECTED_CONTENT_ANGLE": "failure diagnosis" if alternative else "plain buyer guide",
        "REFERENCE_SHAPE_FINGERPRINT": {
            "opening_length_and_stance": "two short buyer-facing paragraphs",
            "intent_resolution_point": "primary answer appears in the first paragraph",
            "title_alignment": "each core H2 resolves one promise implied by the title",
            "heading_hierarchy": "one H1, buyer-task H2s, and H3s only for dependent questions",
            "section_count_or_range": "five to seven H2 sections",
            "section_length_pattern": "short opening, two long core sections, concise close",
            "narrative_sequence": "definition, fit boundaries, process choice, verification, next step",
            "heading_grammar": "plain noun and question headings",
            "paragraph_cadence": "mixed two-to-four sentence paragraphs",
            "evidence_density": "one practical distinction per core section",
            "list_and_table_behavior": "one list when it shortens comparison work",
            "faq_placement_and_form": "three concise questions after the core answer",
            "cta_placement_and_form": "topic-specific closing callout",
            "ending_form": "action-led next step",
            "complexity_load": "plain buyer language with technical terms defined in place",
            "english_naturalness_and_ai_risk": "natural editorial English; avoid repeated labels and symmetric modules",
        },
        "ARTICLE_RHYTHM_ROUTE": {
            "primary_controller": "SERP result 1 controls the dominant rhythm",
            "secondary_contributions": ["SERP result 3 contributes one comparison module"],
            "rhythm_rationale": "matches the dominant buyer-guide intent",
            "anti_convergence_guard": "do not reuse explanation-caution-supplier-input sequencing",
        },
        "SECTION_REFERENCE_MAP": [
            {
                "planned_heading": "What the process is and when it fits",
                "section_kind": "core",
                "sequence_index": 1,
                "sequence_reason": "Resolve the definition and fit decision before process detail.",
                "heading_scope_mode": "single-topic",
                "reference_result_positions": [1],
                "reference_urls": ["https://example1.com/guide"],
                "reference_heading_patterns": ["plain definition followed by a fit decision"],
                "reference_information_order": ["definition", "fit boundary"],
                "reader_question": "What is this process, and is it suitable for my part?",
                "first_paragraph_answer_requirement": "Define the process and state its main fit condition immediately.",
                "body_scope": ["definition", "fit conditions"],
                "excluded_scope": ["detailed defect diagnosis"],
                "adaptation_note": "Use the reference's accessible order with original examples.",
                "originality_guard": "Do not copy the reference heading or prose.",
            },
            {
                "planned_heading": "How the process works",
                "section_kind": "core",
                "sequence_index": 2,
                "sequence_reason": "Explain the operating sequence after establishing process fit.",
                "heading_scope_mode": "single-topic",
                "reference_result_positions": [1, 3],
                "reference_urls": ["https://example1.com/guide", "https://example3.com/guide"],
                "reference_heading_patterns": ["stepwise process explanation"],
                "reference_information_order": ["setup", "operation", "result"],
                "reader_question": "How does the process turn stock into a finished part?",
                "first_paragraph_answer_requirement": "Summarize the process sequence before adding detail.",
                "body_scope": ["setup", "operation", "result"],
                "excluded_scope": ["supplier-selection checklist"],
                "adaptation_note": "Combine the primary sequence with one bounded explanatory pattern.",
                "originality_guard": "Use original sequencing language and examples.",
            },
            {
                "planned_heading": "Questions Buyers Ask Before Choosing This Route",
                "section_kind": "faq",
                "sequence_index": 3,
                "sequence_reason": "Resolve remaining buyer objections after the complete core narrative.",
                "heading_scope_mode": "faq",
                "reference_result_positions": [1],
                "reference_urls": ["https://example1.com/guide"],
                "reference_heading_patterns": ["compact end-of-guide FAQ"],
                "reference_information_order": ["unresolved boundary questions"],
                "reader_question": "What practical questions remain before choosing the process?",
                "first_paragraph_answer_requirement": "Answer the first unresolved buyer question directly.",
                "body_scope": ["three non-duplicate buyer questions"],
                "excluded_scope": ["repeating the body verbatim"],
                "adaptation_note": "Use the reference FAQ position but query-specific questions.",
                "originality_guard": "Do not copy question wording.",
            },
            {
                "planned_heading": "Review Your Plastic Part With PlasticHubs",
                "section_kind": "cta",
                "sequence_index": 4,
                "sequence_reason": "Close with a selected-brand action after buyer questions are resolved.",
                "heading_scope_mode": "cta",
                "reference_result_positions": [1],
                "reference_urls": ["https://example1.com/guide"],
                "reference_heading_patterns": ["action-led closing next step"],
                "reference_information_order": ["action", "inputs", "reader value"],
                "reader_question": "What should the buyer send for a process review?",
                "first_paragraph_answer_requirement": "Name the selected-brand action and required inputs.",
                "body_scope": ["brand action", "inputs", "direct URL", "reader value"],
                "excluded_scope": ["generic contact sentence"],
                "adaptation_note": "Use the reference CTA position with a topic-specific action.",
                "originality_guard": "Write original CTA wording.",
            },
        ],
        "MANDATORY_MODULES": ["FAQ", "CTA"],
        "OPTIONAL_MODULES": ["comparison list"],
        "MODULES_TO_OMIT": ["RFQ table"],
        "FAQ_PLAN": {
            "heading": "Questions Buyers Ask Before Choosing This Route",
            "question_count": 3,
            "question_sources": ["Top-10 gap analysis", "buyer objections"],
            "placement": "after the last core decision section",
            "questions": [
                "When is this process a poor fit?",
                "Which inputs affect the quote most?",
                "What should be verified before production?",
            ],
            "duplication_guard": "each answer adds a new boundary not repeated in the body",
            "allow_substantive_sections_after_faq": False,
            "substantive_sections_after_faq": [],
            "placement_rationale": "The FAQ resolves remaining objections only after every core decision section is complete.",
            "placement_reference_urls": ["https://example1.com/guide"],
        },
        "CTA": {
            "heading_or_callout": "Review Your Plastic Part With PlasticHubs",
            "placement": "after the FAQ",
            "action": "submit the project for process-fit review",
            "destination_url": "https://plastichubs.com/contact-us/",
            "input_request": "CAD, material, quantity, tolerance, and finish",
            "reader_value": "receive a manufacturability and quoting review",
            "same_brand_url_status": "verified",
            "variation_note": "use a review CTA rather than the recent quote-request ending",
        },
        "INTENT_CHANGE_PROPOSAL": {
            "reason": "differentiate from broad guides",
            "expected_gain": "stronger defect coverage",
            "ranking_risk": "may under-serve the dominant beginner intent",
            "audience_effect": "narrows the audience toward engineers",
            "measurement_plan": "compare GSC query coverage and CTR after publication",
        } if alternative else None,
    }
    if alternative and approved:
        data.update({
            "ANGLE_ALIGNMENT_STATUS": "alternative-approved",
            "USER_INTENT_APPROVAL": "approved",
            "USER_INTENT_APPROVAL_EVIDENCE": "User explicitly approved the alternative angle in the current task.",
            "PLAN_GATE_STATUS": "PASS",
        })
    elif alternative:
        data.update({
            "ANGLE_ALIGNMENT_STATUS": "approval-required",
            "USER_INTENT_APPROVAL": "pending",
            "USER_INTENT_APPROVAL_EVIDENCE": "",
            "PLAN_GATE_STATUS": "WAITING_FOR_INTENT_APPROVAL",
        })
    else:
        data.update({
            "ANGLE_ALIGNMENT_STATUS": "aligned",
            "USER_INTENT_APPROVAL": "not-required",
            "USER_INTENT_APPROVAL_EVIDENCE": "",
            "PLAN_GATE_STATUS": "PASS",
        })
    return data


def self_test() -> int:
    aligned_sample = sample(False)
    aligned_status, aligned_errors = validate(aligned_sample)
    pending_status, pending_errors = validate(sample(True))
    approved_status, approved_errors = validate(sample(True, approved=True))
    incomplete = sample(False)
    incomplete["TOP_TEN_SERP_RESULTS"].pop()
    incomplete_status, _ = validate(incomplete)
    missing_faq = sample(False)
    missing_faq["MANDATORY_MODULES"] = ["CTA"]
    missing_faq_status, _ = validate(missing_faq)
    missing_cta = sample(False)
    del missing_cta["CTA"]
    missing_cta_status, _ = validate(missing_cta)
    missing_section_map = sample(False)
    del missing_section_map["SECTION_REFERENCE_MAP"]
    missing_section_map_status, _ = validate(missing_section_map)
    foreign_reference = sample(False)
    foreign_reference["SECTION_REFERENCE_MAP"][0]["reference_urls"] = ["https://outside.example/guide"]
    foreign_reference_status, _ = validate(foreign_reference)
    verification_wait = sample(False)
    verification_wait.update({
        "SERP_BENCHMARK_STATUS": "Blocked",
        "SERP_ACCESS_STATUS": "google-verification-required",
        "USER_BROWSER_VERIFICATION_STATUS": "pending",
        "BEST_EFFORT_DOWNGRADE_APPROVAL": "pending",
        "PLAN_GATE_STATUS": "WAITING_FOR_USER_BROWSER_VERIFICATION",
    })
    verification_status, verification_errors = validate(verification_wait)
    permission_wait = sample(False)
    permission_wait.update({
        "SERP_BENCHMARK_STATUS": "Blocked",
        "SERP_ACCESS_STATUS": "tool-permission-required",
        "USER_BROWSER_VERIFICATION_STATUS": "not-required",
        "BEST_EFFORT_DOWNGRADE_APPROVAL": "pending",
        "PLAN_GATE_STATUS": "WAITING_FOR_TOOL_PERMISSION",
    })
    permission_status, permission_errors = validate(permission_wait)
    unapproved_best_effort = sample(False)
    unapproved_best_effort.update({
        "SERP_BENCHMARK_STATUS": "Best-effort",
        "SERP_ACCESS_STATUS": "best-effort-approved",
        "BEST_EFFORT_DOWNGRADE_APPROVAL": "pending",
    })
    unapproved_best_effort_status, _ = validate(unapproved_best_effort)
    approved_best_effort = sample(False)
    approved_best_effort.update({
        "SERP_BENCHMARK_STATUS": "Best-effort",
        "SERP_ACCESS_STATUS": "best-effort-approved",
        "BEST_EFFORT_DOWNGRADE_APPROVAL": "approved",
        "BEST_EFFORT_DOWNGRADE_APPROVAL_EVIDENCE": "User explicitly approved Best-effort downgrade in the current task.",
    })
    approved_best_effort_status, approved_best_effort_errors = validate(approved_best_effort)
    if (
        (aligned_status, aligned_errors) != ("PASS", [])
        or (pending_status, pending_errors) != ("WAITING_FOR_INTENT_APPROVAL", [])
        or (approved_status, approved_errors) != ("PASS", [])
        or incomplete_status != "BLOCKED"
        or missing_faq_status != "BLOCKED"
        or missing_cta_status != "BLOCKED"
        or missing_section_map_status != "BLOCKED"
        or foreign_reference_status != "BLOCKED"
        or (verification_status, verification_errors) != ("WAITING_FOR_USER_BROWSER_VERIFICATION", [])
        or (permission_status, permission_errors) != ("WAITING_FOR_TOOL_PERMISSION", [])
        or unapproved_best_effort_status != "BLOCKED"
        or (approved_best_effort_status, approved_best_effort_errors) != ("PASS", [])
        or receipt(aligned_sample, aligned_status, aligned_errors).get("top_ten_record_count") != 10
    ):
        print(json.dumps({
            "aligned": [aligned_status, aligned_errors],
            "pending": [pending_status, pending_errors],
            "approved": [approved_status, approved_errors],
            "incomplete": incomplete_status,
            "missing_faq": missing_faq_status,
            "missing_cta": missing_cta_status,
            "missing_section_map": missing_section_map_status,
            "foreign_reference": foreign_reference_status,
            "verification_wait": [verification_status, verification_errors],
            "permission_wait": [permission_status, permission_errors],
            "unapproved_best_effort": unapproved_best_effort_status,
            "approved_best_effort": [approved_best_effort_status, approved_best_effort_errors],
        }, ensure_ascii=False, indent=2))
        return 1
    print("PASS: browser verification, tool permission, Best-effort approval, intent, Top-10, section-reference, FAQ, and CTA gates")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("brief", nargs="?", type=Path)
    parser.add_argument("--receipt", type=Path, help="Write a compact machine-readable gate receipt")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        return self_test()
    if args.brief is None:
        parser.error("brief is required unless --self-test is used")
    data = json.loads(args.brief.read_text(encoding="utf-8"))
    status, errors = validate(data)
    result = receipt(data, status, errors)
    if args.receipt:
        args.receipt.parent.mkdir(parents=True, exist_ok=True)
        args.receipt.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    exit_codes = {
        "PASS": 0,
        "WAITING_FOR_INTENT_APPROVAL": 3,
        "WAITING_FOR_USER_BROWSER_VERIFICATION": 4,
        "WAITING_FOR_TOOL_PERMISSION": 5,
    }
    return exit_codes.get(status, 1)


if __name__ == "__main__":
    raise SystemExit(main())
