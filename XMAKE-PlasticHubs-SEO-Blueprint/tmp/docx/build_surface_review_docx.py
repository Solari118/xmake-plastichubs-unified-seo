from __future__ import annotations

import re
from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK, WD_LINE_SPACING
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "output" / "word"
SOURCES = sorted(ROOT.glob("xmake-*-surface-finishing-page.md"))

WESTERN_FONT = "Calibri"
EAST_ASIA_FONT = "Microsoft YaHei"
NAVY = "20384F"
BLUE = "2E74B5"
DARK_BLUE = "1F4D78"
MUTED = "667085"
LIGHT_BLUE = "E8EEF5"
LIGHT_GRAY = "F2F4F7"
BORDER = "C8D1DC"
WHITE = "FFFFFF"
CONTENT_WIDTH_DXA = 9360
TABLE_INDENT_DXA = 120


def set_run_font(run, western=WESTERN_FONT, east_asia=EAST_ASIA_FONT, size=None,
                 bold=None, italic=None, color=None):
    run.font.name = western
    run._element.get_or_add_rPr().rFonts.set(qn("w:ascii"), western)
    run._element.get_or_add_rPr().rFonts.set(qn("w:hAnsi"), western)
    run._element.get_or_add_rPr().rFonts.set(qn("w:eastAsia"), east_asia)
    if size is not None:
        run.font.size = Pt(size)
    if bold is not None:
        run.bold = bold
    if italic is not None:
        run.italic = italic
    if color is not None:
        run.font.color.rgb = RGBColor.from_string(color)


def set_cell_shading(cell, fill):
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = tc_pr.find(qn("w:shd"))
    if shd is None:
        shd = OxmlElement("w:shd")
        tc_pr.append(shd)
    shd.set(qn("w:fill"), fill)


def set_cell_margins(cell, top=80, start=120, bottom=80, end=120):
    tc_pr = cell._tc.get_or_add_tcPr()
    tc_mar = tc_pr.first_child_found_in("w:tcMar")
    if tc_mar is None:
        tc_mar = OxmlElement("w:tcMar")
        tc_pr.append(tc_mar)
    for side, value in (("top", top), ("start", start), ("bottom", bottom), ("end", end)):
        node = tc_mar.find(qn(f"w:{side}"))
        if node is None:
            node = OxmlElement(f"w:{side}")
            tc_mar.append(node)
        node.set(qn("w:w"), str(value))
        node.set(qn("w:type"), "dxa")


def set_repeat_table_header(row):
    tr_pr = row._tr.get_or_add_trPr()
    tbl_header = OxmlElement("w:tblHeader")
    tbl_header.set(qn("w:val"), "true")
    tr_pr.append(tbl_header)


def set_cell_width(cell, width_dxa):
    tc_pr = cell._tc.get_or_add_tcPr()
    tc_w = tc_pr.find(qn("w:tcW"))
    if tc_w is None:
        tc_w = OxmlElement("w:tcW")
        tc_pr.append(tc_w)
    tc_w.set(qn("w:w"), str(width_dxa))
    tc_w.set(qn("w:type"), "dxa")


def set_table_geometry(table, widths):
    table.alignment = WD_TABLE_ALIGNMENT.LEFT
    table.autofit = False
    tbl_pr = table._tbl.tblPr

    tbl_w = tbl_pr.find(qn("w:tblW"))
    if tbl_w is None:
        tbl_w = OxmlElement("w:tblW")
        tbl_pr.append(tbl_w)
    tbl_w.set(qn("w:w"), str(sum(widths)))
    tbl_w.set(qn("w:type"), "dxa")

    tbl_ind = tbl_pr.find(qn("w:tblInd"))
    if tbl_ind is None:
        tbl_ind = OxmlElement("w:tblInd")
        tbl_pr.append(tbl_ind)
    tbl_ind.set(qn("w:w"), str(TABLE_INDENT_DXA))
    tbl_ind.set(qn("w:type"), "dxa")

    tbl_layout = tbl_pr.find(qn("w:tblLayout"))
    if tbl_layout is None:
        tbl_layout = OxmlElement("w:tblLayout")
        tbl_pr.append(tbl_layout)
    tbl_layout.set(qn("w:type"), "fixed")

    grid = table._tbl.tblGrid
    for child in list(grid):
        grid.remove(child)
    for width in widths:
        col = OxmlElement("w:gridCol")
        col.set(qn("w:w"), str(width))
        grid.append(col)

    for row in table.rows:
        for cell, width in zip(row.cells, widths):
            cell.width = Inches(width / 1440)
            set_cell_width(cell, width)


def proportional_widths(rows, cols):
    maxima = []
    for i in range(cols):
        lengths = [len(re.sub(r"[*`\[\]()]", "", row[i])) if i < len(row) else 0 for row in rows]
        maxima.append(max(8, min(max(lengths, default=8), 52)))
    if cols == 2:
        first = max(1800, min(3000, int(CONTENT_WIDTH_DXA * maxima[0] / sum(maxima))))
        return [first, CONTENT_WIDTH_DXA - first]
    minimum = 1100 if cols >= 4 else 1300
    available = CONTENT_WIDTH_DXA - minimum * cols
    total = sum(maxima)
    widths = [minimum + int(available * value / total) for value in maxima]
    widths[-1] += CONTENT_WIDTH_DXA - sum(widths)
    return widths


def add_hyperlink(paragraph, label, url, bold=False, italic=False):
    part = paragraph.part
    r_id = part.relate_to(url, "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink", is_external=True)
    hyperlink = OxmlElement("w:hyperlink")
    hyperlink.set(qn("r:id"), r_id)
    run = OxmlElement("w:r")
    r_pr = OxmlElement("w:rPr")
    color = OxmlElement("w:color")
    color.set(qn("w:val"), BLUE)
    r_pr.append(color)
    underline = OxmlElement("w:u")
    underline.set(qn("w:val"), "single")
    r_pr.append(underline)
    r_fonts = OxmlElement("w:rFonts")
    r_fonts.set(qn("w:ascii"), WESTERN_FONT)
    r_fonts.set(qn("w:hAnsi"), WESTERN_FONT)
    r_fonts.set(qn("w:eastAsia"), EAST_ASIA_FONT)
    r_pr.append(r_fonts)
    if bold:
        r_pr.append(OxmlElement("w:b"))
    if italic:
        r_pr.append(OxmlElement("w:i"))
    run.append(r_pr)
    text = OxmlElement("w:t")
    text.text = label
    run.append(text)
    hyperlink.append(run)
    paragraph._p.append(hyperlink)


TOKEN_RE = re.compile(r"(\*\*.*?\*\*|`[^`]+`|\[[^\]]+\]\([^)]+\))")


def add_inline(paragraph, text, base_size=None, color=None):
    pos = 0
    for match in TOKEN_RE.finditer(text):
        if match.start() > pos:
            run = paragraph.add_run(text[pos:match.start()])
            set_run_font(run, size=base_size, color=color)
        token = match.group(0)
        if token.startswith("**"):
            run = paragraph.add_run(token[2:-2])
            set_run_font(run, size=base_size, bold=True, color=color)
        elif token.startswith("`"):
            run = paragraph.add_run(token[1:-1])
            set_run_font(run, western="Consolas", east_asia=EAST_ASIA_FONT, size=(base_size or 10.5) - 0.5, color="44546A")
            run.font.highlight_color = None
        else:
            found = re.match(r"\[([^\]]+)\]\(([^)]+)\)", token)
            if found:
                add_hyperlink(paragraph, found.group(1), found.group(2))
        pos = match.end()
    if pos < len(text):
        run = paragraph.add_run(text[pos:])
        set_run_font(run, size=base_size, color=color)


def add_metadata_paragraph(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.15
    match = re.match(r"^([^：:]{1,40})([：:])(.*)$", text)
    if match:
        label = p.add_run(match.group(1) + match.group(2))
        set_run_font(label, size=9.5, bold=True, color=NAVY)
        add_inline(p, match.group(3), base_size=9.5, color="344054")
    else:
        add_inline(p, text, base_size=9.5, color="344054")
    return p


def add_rule(doc):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(3)
    p.paragraph_format.space_after = Pt(8)
    p_pr = p._p.get_or_add_pPr()
    p_bdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "6")
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), BORDER)
    p_bdr.append(bottom)
    p_pr.append(p_bdr)


def clean_heading(text):
    return re.sub(r"^H[1-6][：:]\s*", "", text).strip()


def configure_styles(doc):
    styles = doc.styles
    normal = styles["Normal"]
    normal.font.name = WESTERN_FONT
    normal._element.rPr.rFonts.set(qn("w:ascii"), WESTERN_FONT)
    normal._element.rPr.rFonts.set(qn("w:hAnsi"), WESTERN_FONT)
    normal._element.rPr.rFonts.set(qn("w:eastAsia"), EAST_ASIA_FONT)
    normal.font.size = Pt(11)
    normal.paragraph_format.space_before = Pt(0)
    normal.paragraph_format.space_after = Pt(6)
    normal.paragraph_format.line_spacing = 1.25

    specs = {
        "Title": (25, NAVY, 0, 8),
        "Subtitle": (11, MUTED, 0, 16),
        "Heading 1": (16, BLUE, 18, 10),
        "Heading 2": (13, BLUE, 14, 7),
        "Heading 3": (12, DARK_BLUE, 10, 5),
        "Heading 4": (11, DARK_BLUE, 8, 4),
    }
    for name, (size, color, before, after) in specs.items():
        style = styles[name]
        style.font.name = WESTERN_FONT
        style._element.rPr.rFonts.set(qn("w:ascii"), WESTERN_FONT)
        style._element.rPr.rFonts.set(qn("w:hAnsi"), WESTERN_FONT)
        style._element.rPr.rFonts.set(qn("w:eastAsia"), EAST_ASIA_FONT)
        style.font.size = Pt(size)
        style.font.color.rgb = RGBColor.from_string(color)
        style.font.bold = name != "Subtitle"
        style.paragraph_format.space_before = Pt(before)
        style.paragraph_format.space_after = Pt(after)
        style.paragraph_format.keep_with_next = True

    for name in ("List Bullet", "List Number"):
        style = styles[name]
        style.font.name = WESTERN_FONT
        style._element.rPr.rFonts.set(qn("w:ascii"), WESTERN_FONT)
        style._element.rPr.rFonts.set(qn("w:hAnsi"), WESTERN_FONT)
        style._element.rPr.rFonts.set(qn("w:eastAsia"), EAST_ASIA_FONT)
        style.font.size = Pt(11)
        style.paragraph_format.left_indent = Inches(0.375)
        style.paragraph_format.first_line_indent = Inches(-0.188)
        style.paragraph_format.space_after = Pt(4)
        style.paragraph_format.line_spacing = 1.25


def add_page_number(paragraph):
    paragraph.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = paragraph.add_run("Page ")
    set_run_font(run, size=8.5, color=MUTED)
    fld = OxmlElement("w:fldSimple")
    fld.set(qn("w:instr"), "PAGE")
    paragraph._p.append(fld)


def configure_document(doc, title):
    section = doc.sections[0]
    section.page_width = Inches(8.5)
    section.page_height = Inches(11)
    section.top_margin = Inches(1)
    section.right_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Inches(1)
    section.header_distance = Inches(0.492)
    section.footer_distance = Inches(0.492)

    header = section.header
    p = header.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_after = Pt(0)
    run = p.add_run("XMAKE  |  SURFACE FINISHING REVIEW")
    set_run_font(run, size=8.5, bold=True, color=MUTED)

    footer = section.footer
    add_page_number(footer.paragraphs[0])

    doc.core_properties.title = title
    doc.core_properties.subject = "Bilingual surface-finishing page review draft"
    doc.core_properties.author = "XMAKE"
    doc.core_properties.keywords = "XMAKE, surface finishing, bilingual review draft"


def add_title_block(doc, title):
    kicker = doc.add_paragraph()
    kicker.paragraph_format.space_before = Pt(14)
    kicker.paragraph_format.space_after = Pt(4)
    run = kicker.add_run("XMAKE SURFACE FINISHING")
    set_run_font(run, size=9, bold=True, color=BLUE)

    p = doc.add_paragraph(style="Title")
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(6)
    add_inline(p, title, base_size=25, color=NAVY)

    subtitle = doc.add_paragraph(style="Subtitle")
    add_inline(subtitle, "中英文预览审核版 / Bilingual Review Draft", base_size=11, color=MUTED)
    add_rule(doc)


def split_table_row(line):
    text = line.strip().strip("|")
    return [cell.strip() for cell in re.split(r"(?<!\\)\|", text)]


def is_separator_row(cells):
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", c.replace(" ", "")) for c in cells)


def add_table(doc, raw_lines):
    rows = [split_table_row(line) for line in raw_lines]
    if len(rows) >= 2 and is_separator_row(rows[1]):
        rows.pop(1)
    if not rows:
        return
    cols = max(len(row) for row in rows)
    rows = [row + [""] * (cols - len(row)) for row in rows]
    widths = proportional_widths(rows, cols)
    table = doc.add_table(rows=len(rows), cols=cols)
    table.style = "Table Grid"
    set_table_geometry(table, widths)
    set_repeat_table_header(table.rows[0])
    table_size = 9.2 if cols <= 3 else 8.5

    for r_idx, row in enumerate(rows):
        for c_idx, text in enumerate(row):
            cell = table.cell(r_idx, c_idx)
            cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
            set_cell_margins(cell)
            if r_idx == 0:
                set_cell_shading(cell, LIGHT_BLUE)
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.12
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            add_inline(p, text.replace("\\|", "|"), base_size=table_size, color=(NAVY if r_idx == 0 else "243647"))
            if r_idx == 0:
                for run in p.runs:
                    run.bold = True
    after = doc.add_paragraph()
    after.paragraph_format.space_after = Pt(2)


def build_document(source):
    text = source.read_text(encoding="utf-8-sig")
    lines = text.splitlines()
    title = source.stem
    start = 0
    for idx, line in enumerate(lines):
        if line.startswith("# "):
            title = line[2:].strip()
            start = idx + 1
            break

    doc = Document()
    configure_styles(doc)
    configure_document(doc, title)
    add_title_block(doc, title)

    i = start
    while i < len(lines):
        line = lines[i].rstrip()
        stripped = line.strip()
        if not stripped:
            i += 1
            continue
        if stripped == "---":
            add_rule(doc)
            i += 1
            continue
        if stripped.startswith("|"):
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                table_lines.append(lines[i])
                i += 1
            add_table(doc, table_lines)
            continue

        heading = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if heading:
            level = len(heading.group(1))
            h_text = clean_heading(heading.group(2))
            if h_text.lower().startswith("english review draft"):
                doc.add_page_break()
            style_level = min(max(level, 1), 4)
            p = doc.add_paragraph(style=f"Heading {style_level}")
            add_inline(p, h_text)
            i += 1
            continue

        bullet = re.match(r"^[-*+]\s+(.*)$", stripped)
        if bullet:
            p = doc.add_paragraph(style="List Bullet")
            add_inline(p, bullet.group(1))
            i += 1
            continue

        numbered = re.match(r"^\d+[.)]\s+(.*)$", stripped)
        if numbered:
            p = doc.add_paragraph(style="List Number")
            add_inline(p, numbered.group(1))
            i += 1
            continue

        if stripped.startswith("> "):
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.25)
            p.paragraph_format.right_indent = Inches(0.15)
            p.paragraph_format.space_before = Pt(4)
            p.paragraph_format.space_after = Pt(6)
            add_inline(p, stripped[2:], color="475467")
            for run in p.runs:
                run.italic = True
            i += 1
            continue

        if re.match(r"^(Review Status|Process Category|Suggested URL|Canonical URL Status|Meta Title|Meta Description|meta title|meta description|Primary Keyword|Secondary Keywords|Query Variants|Key Entities|Search Intent)[：:]", stripped):
            add_metadata_paragraph(doc, stripped)
        else:
            p = doc.add_paragraph()
            add_inline(p, stripped)
        i += 1

    OUT.mkdir(parents=True, exist_ok=True)
    output = OUT / source.name.replace("-surface-finishing-page.md", "-bilingual-review.docx")
    doc.save(output)
    return output


def main():
    if not SOURCES:
        raise SystemExit("No surface-finishing Markdown sources found")
    outputs = [build_document(source) for source in SOURCES]
    for output in outputs:
        print(output)


if __name__ == "__main__":
    main()
