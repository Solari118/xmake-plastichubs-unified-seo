"""Validate mandatory FAQ and visible CTA modules in a final English Blog draft."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


BRAND_DOMAINS = {
    "XMAKE": "xmake.com",
    "PlasticHubs": "plastichubs.com",
}
ACTION_WORDS = {
    "get", "request", "start", "send", "upload", "talk", "contact", "review",
    "quote", "compare", "specify", "plan", "discuss", "evaluate", "check",
}
INPUT_PATTERN = re.compile(
    r"\b(CAD|drawing|material|grade|quantity|volume|tolerance|finish|application|"
    r"deadline|file|specification|requirement|part data)\b",
    re.IGNORECASE,
)
VALUE_PATTERN = re.compile(
    r"\b(review|quote|recommend|feedback|check|assess|confirm|identify|compare|"
    r"manufacturability|process fit|next step|cost|lead time|risk)\b",
    re.IGNORECASE,
)


def sections(markdown: str) -> list[dict[str, str | int]]:
    matches = list(re.finditer(r"(?m)^(#{2,3})\s+(.+?)\s*$", markdown))
    result: list[dict[str, str | int]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(markdown)
        result.append({
            "level": len(match.group(1)),
            "heading": match.group(2).strip(),
            "body": markdown[match.end():end].strip(),
            "start": match.start(),
            "end": end,
        })
    return result


def word_count(text: str) -> int:
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'-]*", text))


def validate(markdown: str, brand: str) -> dict[str, object]:
    errors: list[str] = []
    parsed = sections(markdown)

    faq_index = next((
        index for index, section in enumerate(parsed)
        if re.search(r"\bFAQ\b|frequently asked questions|questions .* ask", str(section["heading"]), re.I)
    ), None)
    faq_count = 0
    faq_heading = None
    if faq_index is None:
        errors.append("missing visible FAQ section")
    else:
        faq_heading = str(parsed[faq_index]["heading"])
        faq_level = int(parsed[faq_index]["level"])
        questions = []
        for section in parsed[faq_index + 1:]:
            if int(section["level"]) <= faq_level:
                break
            heading = str(section["heading"]).strip()
            if heading.endswith("?"):
                questions.append(section)
        faq_count = len(questions)
        if not 3 <= faq_count <= 6:
            errors.append("FAQ must contain 3 to 6 visible question headings")
        for question in questions:
            if word_count(str(question["body"])) < 12:
                errors.append(f"FAQ answer is too thin: {question['heading']}")

    cta_candidates = []
    for section in parsed:
        heading = str(section["heading"])
        heading_words = set(re.findall(r"[a-z]+", heading.lower()))
        if heading_words & ACTION_WORDS:
            cta_candidates.append(section)
    cta = next((
        section for section in cta_candidates
        if brand.lower() in (str(section["heading"]) + " " + str(section["body"])).lower()
    ), None)
    cta_heading = None
    if cta is None:
        errors.append("missing visible action-led CTA heading or callout")
    else:
        cta_heading = str(cta["heading"])
        cta_text = f"{cta['heading']} {cta['body']}"
        if cta_heading.lower().strip() in {"contact us", "get a quote", "request a quote"}:
            errors.append("CTA heading is generic rather than topic-specific")
        expected_domain = BRAND_DOMAINS[brand]
        if not re.search(rf"https?://(?:www\.)?{re.escape(expected_domain)}(?:/|\b)", cta_text, re.I):
            errors.append("CTA lacks a direct same-brand URL")
        if not INPUT_PATTERN.search(cta_text):
            errors.append("CTA lacks useful project-input guidance")
        if not VALUE_PATTERN.search(cta_text):
            errors.append("CTA lacks a concrete reader value or next-step result")
        if re.fullmatch(
            r".{0,40}contact us for more information[.!]?",
            re.sub(r"\s+", " ", cta_text).strip(),
            re.I,
        ):
            errors.append("generic contact sentence does not satisfy the CTA gate")

    return {
        "status": "PASS" if not errors else "FAIL",
        "brand": brand,
        "faq_heading": faq_heading,
        "faq_question_count": faq_count,
        "cta_heading": cta_heading,
        "errors": errors,
    }


def self_test() -> int:
    good = """# Acrylic CNC Machining

## Questions Buyers Ask Before Machining Acrylic

### Can acrylic hold tight tolerances?

It can hold useful tolerances when geometry, stock condition, workholding, and inspection temperature are defined before machining begins.

### Should the edges be polished after machining?

Polishing depends on optical requirements, edge geometry, and dimensional priorities because each polishing method changes the surface differently.

### What information improves an acrylic machining quote?

Material grade, CAD data, drawings, quantities, tolerances, cosmetic zones, and required finish help establish the correct process route.

## Review Your Acrylic Part Before Releasing It

Send PlasticHubs your CAD file, drawing, material grade, quantity, tolerance, and finish requirements. [Request a process-fit review](https://plastichubs.com/contact-us/) to identify manufacturability risks and receive a usable next step.
"""
    missing_faq = """# Article

## Review Your Acrylic Part

Send PlasticHubs CAD, material, quantity, and tolerance data for a [process-fit review](https://plastichubs.com/contact-us/).
"""
    generic_cta = """# Article

## Frequently Asked Questions

### Question one?

This answer contains enough useful words to explain a meaningful manufacturing decision and its important boundary.

### Question two?

This answer contains enough useful words to explain a meaningful manufacturing decision and its important boundary.

### Question three?

This answer contains enough useful words to explain a meaningful manufacturing decision and its important boundary.

## Contact Us

Contact us for more information.
"""
    results = {
        "good": validate(good, "PlasticHubs"),
        "missing_faq": validate(missing_faq, "PlasticHubs"),
        "generic_cta": validate(generic_cta, "PlasticHubs"),
    }
    if (
        results["good"]["status"] != "PASS"
        or results["missing_faq"]["status"] != "FAIL"
        or results["generic_cta"]["status"] != "FAIL"
    ):
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return 1
    print("PASS: mandatory FAQ and visible topic-specific CTA gate")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("article", nargs="?", type=Path)
    parser.add_argument("--brand", choices=sorted(BRAND_DOMAINS))
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        return self_test()
    if args.article is None or args.brand is None:
        parser.error("article and --brand are required unless --self-test is used")
    result = validate(args.article.read_text(encoding="utf-8"), args.brand)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
