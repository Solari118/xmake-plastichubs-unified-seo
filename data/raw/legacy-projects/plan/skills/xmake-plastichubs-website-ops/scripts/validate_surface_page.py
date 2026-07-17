#!/usr/bin/env python3
"""Validate Xmake surface-finishing Markdown review drafts."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


REQUIRED_PATTERNS = {
    "meta_title": r"(?im)^\s*(?:meta title|Meta Title)\s*[：:]",
    "meta_description": r"(?im)^\s*(?:meta description|Meta Description)\s*[：:]",
    "h1": r"(?im)^#\s+(?:H1\s*[：:]\s*)?\S+",
    "primary_keyword": r"(?im)^\s*Primary Keyword\s*[：:]",
    "secondary_keywords": r"(?im)^\s*Secondary Keywords\s*[：:]",
    "search_intent": r"(?im)^\s*Search Intent\s*[：:]",
    "cta": r"(?im)^#{1,2}\s+.*(?:CTA|Get (?:an )?Instant Quote|Request a Quote|获取报价)",
    "internal_links": r"(?im)^#{1,3}\s+.*(?:Suggested Internal Links|建议内部链接)",
    "verification_notes": r"(?im)^#{1,3}\s+.*(?:Human Verification Notes|人工核验说明)",
}

CONFIDENTIAL_PATTERNS = {
    "named_upstream_provider": r"(?i)\bPlastichubs/xmake\b",
    "partner_factory_disclosure": r"(?i)\bpartner factor(?:y|ies)\b|合作工厂|供应商名称",
}


def validate(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    warnings: list[str] = []

    for name, pattern in REQUIRED_PATTERNS.items():
        if not re.search(pattern, text):
            errors.append(f"missing_required_field:{name}")

    if re.search(r"(?i)<\s*/?\s*(?:div|section|table|span)\b", text):
        errors.append("raw_html_layout_tag")

    for name, pattern in CONFIDENTIAL_PATTERNS.items():
        if re.search(pattern, text):
            errors.append(f"confidential_public_disclosure:{name}")

    if not re.search(r"[\u4e00-\u9fff]", text):
        errors.append("missing_chinese_review_content")
    if not re.search(r"(?i)\b(?:the|and|for|with|service|process)\b", text):
        errors.append("missing_english_review_content")

    if re.search(r"(?i)\b(?:global leader|world-class|best quality|lowest cost|fastest delivery|perfect surface finish)\b", text):
        warnings.append("unsupported_superlative_or_absolute")

    return {
        "path": str(path.resolve()),
        "valid": not errors,
        "errors": errors,
        "warnings": warnings,
        "url_required": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pages", nargs="+", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    results = [validate(page) for page in args.pages]
    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        for result in results:
            status = "PASS" if result["valid"] else "FAIL"
            print(f"{status} {result['path']}")
            for error in result["errors"]:
                print(f"  ERROR {error}")
            for warning in result["warnings"]:
                print(f"  WARN  {warning}")
    return 0 if all(result["valid"] for result in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
