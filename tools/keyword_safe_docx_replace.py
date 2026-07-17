from __future__ import annotations

import json
from pathlib import Path

from docx import Document


INPUT = Path(
    r"C:\Users\Lostk\Documents\文章优化提示词2.0-Aduit\outputs\keyword_revisions\Best_Plastics_for_CNC_Machining_WordPress_Ready.original.docx"
)
OUTPUT = Path(
    r"C:\Users\Lostk\Documents\文章优化提示词2.0-Aduit\outputs\keyword_revisions\Best_Plastics_for_CNC_Machining_WordPress_Ready_keyword_optimized.docx"
)
LOG = OUTPUT.with_suffix(".keyword_replacements.json")


REPLACEMENTS = [
    {
        "old": "plastic CNC machining projects",
        "new": "CNC plastic machining projects",
        "max": 1,
        "keyword_evidence": "cnc plastic machining: volume 590 vs plastic cnc machining: volume 210",
        "reason": "Same process scope; higher-volume word order used once to avoid repetition.",
    },
    {
        "old": "Plastic CNC Machining Tolerance Risks",
        "new": "CNC Plastic Machining Tolerance Risks",
        "max": 1,
        "keyword_evidence": "cnc plastic machining: volume 590 vs plastic cnc machining: volume 210",
        "reason": "Heading-level synonym with unchanged topic.",
    },
    {
        "old": "CNC machined plastic parts",
        "new": "machined plastic parts",
        "max": 2,
        "keyword_evidence": "machined plastic parts: volume 260 vs cnc machined plastic parts: volume 70",
        "reason": "Removes redundant CNC wording where CNC context is already explicit.",
    },
    {
        "old": "CNC machined plastic part",
        "new": "machined plastic part",
        "max": 1,
        "keyword_evidence": "machined plastic parts: volume 260 vs cnc machined plastic parts: volume 70",
        "reason": "Singular local variant; context remains CNC machining.",
    },
    {
        "old": "Polycarbonate CNC Machining: Best for Transparent Impact-Resistant Guards",
        "new": "Machining Polycarbonate: Best for Transparent Impact-Resistant Guards",
        "max": 1,
        "keyword_evidence": "machining polycarbonate: volume 110 vs polycarbonate cnc machining: volume 20",
        "reason": "Same material/process meaning; more searched natural phrase.",
    },
    {
        "old": "Polycarbonate CNC machining requires",
        "new": "Machining polycarbonate requires",
        "max": 1,
        "keyword_evidence": "machining polycarbonate: volume 110 vs polycarbonate cnc machining: volume 20",
        "reason": "Same technical statement with higher-volume phrase.",
    },
    {
        "old": "PMMA CNC Machining: Best for Clear Cosmetic and Display Parts",
        "new": "Acrylic CNC Machining (PMMA): Best for Clear Cosmetic and Display Parts",
        "max": 1,
        "keyword_evidence": "acrylic cnc machining: volume 320 vs pmma cnc machining: volume 0",
        "reason": "Acrylic is the common synonym for PMMA and keeps PMMA visible.",
    },
    {
        "old": "PMMA CNC machining is not the same as machining a tough guard material.",
        "new": "Acrylic CNC machining is not the same as machining a tough guard material.",
        "max": 1,
        "keyword_evidence": "acrylic cnc machining: volume 320 vs pmma cnc machining: volume 0",
        "reason": "Same material scope because the section defines PMMA as acrylic.",
    },
    {
        "old": "For CNC machined PMMA parts, define the required visual level before quotation.",
        "new": "For acrylic CNC machining projects, define the required visual level before quotation.",
        "max": 1,
        "keyword_evidence": "acrylic cnc machining: volume 320 vs pmma cnc machining: volume 0",
        "reason": "Same section scope; improves query alignment without adding a new claim.",
    },
    {
        "old": "At PlasticHubs, we support CNC machined parts in POM, PEEK, Nylon, PC, ABS, PMMA, and other engineering plastics.",
        "new": "At PlasticHubs, we support machined plastic parts in POM, PEEK, Nylon, PC, ABS, PMMA, and other engineering plastics.",
        "max": 1,
        "keyword_evidence": "machined plastic parts: volume 260 vs cnc machined plastic parts: volume 70",
        "reason": "Same capability statement; CNC context is established by surrounding section.",
    },
]


def replace_limited(text: str, old: str, new: str, limit: int) -> tuple[str, int]:
    count = 0
    while count < limit and old in text:
        text = text.replace(old, new, 1)
        count += 1
    return text, count


def replace_in_paragraph(paragraph, replacements: list[dict]) -> list[dict]:
    changes = []
    for run in paragraph.runs:
        if not run.text:
            continue
        updated = run.text
        for item in replacements:
            if item["_count"] >= item["max"]:
                continue
            updated, made = replace_limited(
                updated, item["old"], item["new"], item["max"] - item["_count"]
            )
            if made:
                item["_count"] += made
                changes.append(
                    {
                        "old": item["old"],
                        "new": item["new"],
                        "count": made,
                        "keyword_evidence": item["keyword_evidence"],
                        "reason": item["reason"],
                    }
                )
        run.text = updated

    # Word sometimes splits a visible sentence across runs. For body paragraphs
    # without special inline styling, a paragraph-level fallback keeps targeted
    # keyword edits from being skipped while avoiding a broader rewrite.
    paragraph_text = paragraph.text
    for item in replacements:
        if item["_count"] >= item["max"]:
            continue
        if item["old"] not in paragraph_text:
            continue
        updated, made = replace_limited(
            paragraph_text, item["old"], item["new"], item["max"] - item["_count"]
        )
        if made:
            paragraph.clear()
            paragraph.add_run(updated)
            item["_count"] += made
            paragraph_text = updated
            changes.append(
                {
                    "old": item["old"],
                    "new": item["new"],
                    "count": made,
                    "keyword_evidence": item["keyword_evidence"],
                    "reason": item["reason"],
                }
            )
    return changes


def iter_paragraphs(document: Document):
    for paragraph in document.paragraphs:
        yield paragraph
    for table in document.tables:
        for row in table.rows:
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    yield paragraph


def main() -> None:
    document = Document(INPUT)
    replacements = [dict(item, _count=0) for item in REPLACEMENTS]
    changes = []
    for paragraph in iter_paragraphs(document):
        changes.extend(replace_in_paragraph(paragraph, replacements))

    missing = [
        {
            "old": item["old"],
            "expected_max": item["max"],
            "actual_count": item["_count"],
        }
        for item in replacements
        if item["_count"] == 0
    ]

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    document.save(OUTPUT)
    LOG.write_text(
        json.dumps(
            {
                "input": str(INPUT),
                "output": str(OUTPUT),
                "total_replacements": sum(item["_count"] for item in replacements),
                "changes": changes,
                "missing": missing,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(json.dumps({"output": str(OUTPUT), "total_replacements": sum(item["_count"] for item in replacements), "missing": missing}, ensure_ascii=False))


if __name__ == "__main__":
    main()
