from pathlib import Path
import html
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    HRFlowable,
    LongTable,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "xmake-vacuum-plating-pvd-surface-finishing-page.md"
OUTPUT = ROOT / "output" / "pdf" / "xmake-vacuum-plating-pvd-bilingual-review.pdf"


pdfmetrics.registerFont(TTFont("CJK", r"C:\Windows\Fonts\msyh.ttc", subfontIndex=0))
pdfmetrics.registerFont(TTFont("CJK-Bold", r"C:\Windows\Fonts\msyhbd.ttc", subfontIndex=0))


NAVY = colors.HexColor("#102A43")
BLUE = colors.HexColor("#1769AA")
CYAN = colors.HexColor("#2CB1BC")
INK = colors.HexColor("#243B53")
MUTED = colors.HexColor("#627D98")
PALE = colors.HexColor("#EAF4FA")
LINE = colors.HexColor("#BCCCDC")
WHITE = colors.white


class ReviewDocTemplate(BaseDocTemplate):
    def __init__(self, filename):
        super().__init__(
            filename,
            pagesize=A4,
            leftMargin=18 * mm,
            rightMargin=18 * mm,
            topMargin=19 * mm,
            bottomMargin=18 * mm,
            title="Vacuum Plating (PVD) — Bilingual Review Draft",
            author="Xmake",
            subject="PVD coating services bilingual page review",
        )
        frame = Frame(
            self.leftMargin,
            self.bottomMargin,
            self.width,
            self.height,
            id="normal",
        )
        self.addPageTemplates(PageTemplate(id="content", frames=frame, onPage=self.draw_page))

    def draw_page(self, canvas, doc):
        canvas.saveState()
        if doc.page > 1:
            canvas.setStrokeColor(LINE)
            canvas.setLineWidth(0.5)
            canvas.line(18 * mm, A4[1] - 13 * mm, A4[0] - 18 * mm, A4[1] - 13 * mm)
            canvas.setFont("CJK", 7.5)
            canvas.setFillColor(MUTED)
            canvas.drawString(18 * mm, A4[1] - 10 * mm, "Xmake · Vacuum Plating (PVD)")
            canvas.drawRightString(A4[0] - 18 * mm, A4[1] - 10 * mm, "中英文对照审核稿 / Bilingual Review Draft")
        canvas.setStrokeColor(LINE)
        canvas.line(18 * mm, 12 * mm, A4[0] - 18 * mm, 12 * mm)
        canvas.setFont("CJK", 7.5)
        canvas.setFillColor(MUTED)
        canvas.drawString(18 * mm, 8.2 * mm, "Primary keyword: pvd coating services")
        canvas.drawRightString(A4[0] - 18 * mm, 8.2 * mm, f"{doc.page}")
        canvas.restoreState()


styles = getSampleStyleSheet()
BODY = ParagraphStyle(
    "BodyCJK",
    parent=styles["BodyText"],
    fontName="CJK",
    fontSize=9.2,
    leading=14.2,
    textColor=INK,
    spaceAfter=6.5,
    allowWidows=0,
    allowOrphans=0,
)
META = ParagraphStyle(
    "Meta",
    parent=BODY,
    backColor=PALE,
    borderColor=colors.HexColor("#D9EAF4"),
    borderWidth=0.5,
    borderPadding=6,
    fontSize=8.7,
    leading=13.2,
    spaceAfter=5,
)
H1 = ParagraphStyle(
    "H1CJK",
    parent=BODY,
    fontName="CJK-Bold",
    fontSize=20,
    leading=27,
    textColor=NAVY,
    spaceBefore=5,
    spaceAfter=12,
    keepWithNext=True,
)
H2 = ParagraphStyle(
    "H2CJK",
    parent=BODY,
    fontName="CJK-Bold",
    fontSize=13.4,
    leading=19,
    textColor=BLUE,
    spaceBefore=11,
    spaceAfter=6,
    keepWithNext=True,
)
H3 = ParagraphStyle(
    "H3CJK",
    parent=BODY,
    fontName="CJK-Bold",
    fontSize=10.7,
    leading=16,
    textColor=NAVY,
    spaceBefore=7,
    spaceAfter=3,
    keepWithNext=True,
)
BULLET = ParagraphStyle(
    "BulletCJK",
    parent=BODY,
    leftIndent=5 * mm,
    firstLineIndent=-3.5 * mm,
    bulletIndent=0,
    spaceAfter=3.5,
)
NUMBERED = ParagraphStyle(
    "NumberedCJK",
    parent=BODY,
    leftIndent=6 * mm,
    firstLineIndent=-4.5 * mm,
    spaceAfter=4,
)
COVER_KICKER = ParagraphStyle(
    "CoverKicker",
    parent=BODY,
    fontName="CJK-Bold",
    fontSize=11,
    leading=16,
    textColor=CYAN,
    alignment=TA_CENTER,
    tracking=1.4,
)
COVER_TITLE = ParagraphStyle(
    "CoverTitle",
    parent=BODY,
    fontName="CJK-Bold",
    fontSize=28,
    leading=38,
    textColor=NAVY,
    alignment=TA_CENTER,
)
COVER_SUB = ParagraphStyle(
    "CoverSub",
    parent=BODY,
    fontSize=12,
    leading=18,
    textColor=MUTED,
    alignment=TA_CENTER,
)
TABLE_HEADER = ParagraphStyle(
    "TableHeader",
    parent=BODY,
    fontName="CJK-Bold",
    fontSize=7.8,
    leading=10.8,
    textColor=WHITE,
    alignment=TA_LEFT,
)
TABLE_BODY = ParagraphStyle(
    "TableBody",
    parent=BODY,
    fontSize=7.6,
    leading=10.6,
    textColor=INK,
    alignment=TA_LEFT,
)


def inline_markup(text):
    escaped = html.escape(text.strip())
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", escaped)
    escaped = re.sub(
        r"(https://[^\s<]+)",
        r'<link href="\1" color="#1769AA">\1</link>',
        escaped,
    )
    return escaped


def parse_table(lines, start, usable_width):
    rows = []
    i = start
    while i < len(lines) and lines[i].strip().startswith("|"):
        cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
        rows.append(cells)
        i += 1
    if len(rows) > 1 and all(re.fullmatch(r":?-{3,}:?", c) for c in rows[1]):
        rows.pop(1)
    col_count = max(len(r) for r in rows)
    normalized = [r + [""] * (col_count - len(r)) for r in rows]
    formatted = []
    for row_index, row in enumerate(normalized):
        style = TABLE_HEADER if row_index == 0 else TABLE_BODY
        formatted.append([Paragraph(inline_markup(cell), style) for cell in row])
    if col_count == 2:
        widths = [usable_width * 0.27, usable_width * 0.73]
    elif col_count == 3:
        widths = [usable_width * 0.24, usable_width * 0.35, usable_width * 0.41]
    else:
        widths = [usable_width / col_count] * col_count
    table = LongTable(formatted, colWidths=widths, repeatRows=1, hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), NAVY),
                ("GRID", (0, 0), (-1, -1), 0.35, LINE),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 4.5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4.5),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, colors.HexColor("#F7FAFC")]),
            ]
        )
    )
    return table, i


def build_story(md_text, usable_width):
    story = []
    story.extend(
        [
            Spacer(1, 32 * mm),
            HRFlowable(width="22%", thickness=3, color=CYAN, spaceAfter=10 * mm, hAlign="CENTER"),
            Paragraph("XMAKE SURFACE FINISHING", COVER_KICKER),
            Spacer(1, 7 * mm),
            Paragraph("真空镀（PVD）", COVER_TITLE),
            Paragraph("Vacuum Plating (PVD)", COVER_TITLE),
            Spacer(1, 8 * mm),
            Paragraph("中英文对照审核稿 / Bilingual Review Draft", COVER_SUB),
            Spacer(1, 12 * mm),
            Paragraph("Primary keyword", COVER_KICKER),
            Paragraph("pvd coating services", COVER_SUB),
            Spacer(1, 28 * mm),
            Paragraph("Content preview · Not the publish-ready WordPress version", COVER_SUB),
            Paragraph("内容预览 · 非最终 WordPress 发布版", COVER_SUB),
            PageBreak(),
        ]
    )

    lines = md_text.splitlines()
    i = 0
    first_language_heading = True
    while i < len(lines):
        raw = lines[i].rstrip()
        stripped = raw.strip()
        if not stripped:
            i += 1
            continue
        if stripped == "---":
            story.append(Spacer(1, 3 * mm))
            i += 1
            continue
        if stripped.startswith("| ") or (stripped.startswith("|") and stripped.endswith("|")):
            table, i = parse_table(lines, i, usable_width)
            story.extend([Spacer(1, 2 * mm), table, Spacer(1, 4 * mm)])
            continue
        if stripped.startswith("# "):
            title = stripped[2:].strip()
            if title in {"真空镀（PVD）/ Vacuum Plating (PVD)"}:
                i += 1
                continue
            if title in {"中文审核稿", "English Review Draft"}:
                if not first_language_heading:
                    story.append(PageBreak())
                first_language_heading = False
            story.append(Paragraph(inline_markup(title), H1))
            story.append(HRFlowable(width="100%", thickness=1.2, color=CYAN, spaceAfter=5 * mm))
            i += 1
            continue
        if stripped.startswith("## "):
            story.append(Paragraph(inline_markup(stripped[3:].strip()), H2))
            i += 1
            continue
        if stripped.startswith("### "):
            story.append(Paragraph(inline_markup(stripped[4:].strip()), H3))
            i += 1
            continue
        if stripped.startswith("- "):
            story.append(Paragraph("• " + inline_markup(stripped[2:]), BULLET))
            i += 1
            continue
        number_match = re.match(r"^(\d+)\.\s+(.*)$", stripped)
        if number_match:
            story.append(
                Paragraph(
                    f"<b>{number_match.group(1)}.</b> {inline_markup(number_match.group(2))}",
                    NUMBERED,
                )
            )
            i += 1
            continue
        paragraph_lines = [stripped]
        i += 1
        while i < len(lines):
            candidate = lines[i].strip()
            if not candidate or candidate.startswith(("#", "- ", "|", "---")) or re.match(r"^\d+\.\s+", candidate):
                break
            paragraph_lines.append(candidate)
            i += 1
        paragraph_text = " ".join(paragraph_lines).replace("  ", " ")
        style = META if re.match(r"^(Meta |Primary Keyword|Secondary Keywords|Search Intent|Review Status)", paragraph_text) else BODY
        story.append(Paragraph(inline_markup(paragraph_text), style))
    return story


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    markdown_text = SOURCE.read_text(encoding="utf-8")
    doc = ReviewDocTemplate(str(OUTPUT))
    story = build_story(markdown_text, doc.width)
    doc.build(story)
    print(f"Created {OUTPUT}")


if __name__ == "__main__":
    main()
