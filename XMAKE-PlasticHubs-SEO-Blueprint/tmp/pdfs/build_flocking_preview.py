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
from reportlab.platypus import BaseDocTemplate, Frame, HRFlowable, LongTable, PageBreak, PageTemplate, Paragraph, Spacer, TableStyle

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "xmake-electrostatic-flocking-surface-finishing-page.md"
OUTPUT = ROOT / "output" / "pdf" / "xmake-electrostatic-flocking-bilingual-review.pdf"

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
        super().__init__(filename, pagesize=A4, leftMargin=18*mm, rightMargin=18*mm, topMargin=19*mm, bottomMargin=18*mm,
                         title="Electrostatic Flocking - Bilingual Review Draft", author="Xmake",
                         subject="Electrostatic flocking bilingual page review")
        frame = Frame(self.leftMargin, self.bottomMargin, self.width, self.height, id="normal")
        self.addPageTemplates(PageTemplate(id="content", frames=frame, onPage=self.draw_page))

    def draw_page(self, canvas, doc):
        canvas.saveState()
        if doc.page > 1:
            canvas.setStrokeColor(LINE); canvas.setLineWidth(0.5)
            canvas.line(18*mm, A4[1]-13*mm, A4[0]-18*mm, A4[1]-13*mm)
            canvas.setFont("CJK", 7.5); canvas.setFillColor(MUTED)
            canvas.drawString(18*mm, A4[1]-10*mm, "Xmake · Electrostatic Flocking")
            canvas.drawRightString(A4[0]-18*mm, A4[1]-10*mm, "中英文对照审核稿 / Bilingual Review Draft")
        canvas.setStrokeColor(LINE); canvas.line(18*mm, 12*mm, A4[0]-18*mm, 12*mm)
        canvas.setFont("CJK", 7.5); canvas.setFillColor(MUTED)
        canvas.drawString(18*mm, 8.2*mm, "Primary keyword: electrostatic flocking")
        canvas.drawRightString(A4[0]-18*mm, 8.2*mm, f"{doc.page}")
        canvas.restoreState()

styles = getSampleStyleSheet()
BODY = ParagraphStyle("BodyCJK", parent=styles["BodyText"], fontName="CJK", fontSize=9.0, leading=13.8, textColor=INK, spaceAfter=6.2, allowWidows=0, allowOrphans=0)
META = ParagraphStyle("Meta", parent=BODY, backColor=PALE, borderColor=colors.HexColor("#D9EAF4"), borderWidth=0.5, borderPadding=6, fontSize=8.5, leading=12.8, spaceAfter=5)
H1 = ParagraphStyle("H1CJK", parent=BODY, fontName="CJK-Bold", fontSize=19, leading=26, textColor=NAVY, spaceBefore=5, spaceAfter=11, keepWithNext=True)
H2 = ParagraphStyle("H2CJK", parent=BODY, fontName="CJK-Bold", fontSize=13, leading=18, textColor=BLUE, spaceBefore=10, spaceAfter=6, keepWithNext=True)
H3 = ParagraphStyle("H3CJK", parent=BODY, fontName="CJK-Bold", fontSize=10.5, leading=15.5, textColor=NAVY, spaceBefore=7, spaceAfter=3, keepWithNext=True)
BULLET = ParagraphStyle("BulletCJK", parent=BODY, leftIndent=5*mm, firstLineIndent=-3.5*mm, bulletIndent=0, spaceAfter=3.2)
NUMBERED = ParagraphStyle("NumberedCJK", parent=BODY, leftIndent=6*mm, firstLineIndent=-4.5*mm, spaceAfter=4)
COVER_KICKER = ParagraphStyle("CoverKicker", parent=BODY, fontName="CJK-Bold", fontSize=11, leading=16, textColor=CYAN, alignment=TA_CENTER, tracking=1.4)
COVER_TITLE = ParagraphStyle("CoverTitle", parent=BODY, fontName="CJK-Bold", fontSize=27, leading=37, textColor=NAVY, alignment=TA_CENTER)
COVER_SUB = ParagraphStyle("CoverSub", parent=BODY, fontSize=12, leading=18, textColor=MUTED, alignment=TA_CENTER)
TABLE_HEADER = ParagraphStyle("TableHeader", parent=BODY, fontName="CJK-Bold", fontSize=7.5, leading=10.3, textColor=WHITE, alignment=TA_LEFT)
TABLE_BODY = ParagraphStyle("TableBody", parent=BODY, fontSize=7.3, leading=10.2, textColor=INK, alignment=TA_LEFT)

def inline_markup(text):
    escaped = html.escape(text.strip())
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", escaped)
    escaped = re.sub(r"\[([^\]]+)\]\((https://[^)]+)\)", r'<link href="\2" color="#1769AA">\1</link>', escaped)
    return escaped

def parse_table(lines, start, usable_width):
    rows=[]; i=start
    while i < len(lines) and lines[i].strip().startswith("|"):
        rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")]); i += 1
    if len(rows)>1 and all(re.fullmatch(r":?-{3,}:?", c) for c in rows[1]): rows.pop(1)
    cols=max(len(r) for r in rows); normalized=[r+[""]*(cols-len(r)) for r in rows]
    formatted=[[Paragraph(inline_markup(cell), TABLE_HEADER if ri==0 else TABLE_BODY) for cell in row] for ri,row in enumerate(normalized)]
    widths=[usable_width*0.27, usable_width*0.73] if cols==2 else ([usable_width*0.22, usable_width*0.25, usable_width*0.25, usable_width*0.28] if cols==4 else [usable_width/cols]*cols)
    table=LongTable(formatted, colWidths=widths, repeatRows=1, hAlign="LEFT")
    table.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),NAVY),("GRID",(0,0),(-1,-1),0.35,LINE),("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),5),("RIGHTPADDING",(0,0),(-1,-1),5),("TOPPADDING",(0,0),(-1,-1),4.2),("BOTTOMPADDING",(0,0),(-1,-1),4.2),("ROWBACKGROUNDS",(0,1),(-1,-1),[WHITE,colors.HexColor("#F7FAFC")])]))
    return table,i

def build_story(md_text, usable_width):
    story=[Spacer(1,32*mm),HRFlowable(width="22%",thickness=3,color=CYAN,spaceAfter=10*mm,hAlign="CENTER"),Paragraph("XMAKE SURFACE FINISHING",COVER_KICKER),Spacer(1,7*mm),Paragraph("植绒",COVER_TITLE),Paragraph("Electrostatic Flocking",COVER_TITLE),Spacer(1,8*mm),Paragraph("中英文对照审核稿 / Bilingual Review Draft",COVER_SUB),Spacer(1,12*mm),Paragraph("Primary keyword",COVER_KICKER),Paragraph("electrostatic flocking",COVER_SUB),Spacer(1,28*mm),Paragraph("Content preview · Not the publish-ready WordPress version",COVER_SUB),Paragraph("内容预览 · 非最终 WordPress 发布版",COVER_SUB),PageBreak()]
    lines=md_text.splitlines(); i=0
    while i < len(lines):
        stripped=lines[i].strip()
        if not stripped: i+=1; continue
        if stripped=="---": story.append(Spacer(1,3*mm)); i+=1; continue
        if stripped.startswith("|") and stripped.endswith("|"):
            table,i=parse_table(lines,i,usable_width); story.extend([Spacer(1,2*mm),table,Spacer(1,4*mm)]); continue
        if stripped.startswith("# "):
            title=stripped[2:].strip()
            if title=="植绒 / Flocking": i+=1; continue
            story.append(Paragraph(inline_markup(title),H1)); story.append(HRFlowable(width="100%",thickness=1.2,color=CYAN,spaceAfter=5*mm)); i+=1; continue
        if stripped.startswith("## "): story.append(Paragraph(inline_markup(stripped[3:]),H2)); i+=1; continue
        if stripped.startswith("### "): story.append(Paragraph(inline_markup(stripped[4:]),H3)); i+=1; continue
        if stripped.startswith("- "): story.append(Paragraph("• "+inline_markup(stripped[2:]),BULLET)); i+=1; continue
        number_match=re.match(r"^(\d+)\.\s+(.*)$",stripped)
        if number_match:
            story.append(Paragraph(f"<b>{number_match.group(1)}.</b> {inline_markup(number_match.group(2))}",NUMBERED)); i+=1; continue
        paragraph_lines=[stripped]; i+=1
        while i < len(lines):
            candidate=lines[i].strip()
            if not candidate or candidate.startswith(("#","- ","|","---")) or re.match(r"^\d+\.\s+",candidate): break
            paragraph_lines.append(candidate); i+=1
        paragraph_text=" ".join(paragraph_lines).replace("  "," ")
        style=META if re.match(r"^(Suggested URL|Canonical URL Status|Meta |Primary Keyword|Secondary Keywords|Query Variants|Key Entities|Search Intent|Review Status)",paragraph_text) else BODY
        story.append(Paragraph(inline_markup(paragraph_text),style))
    return story

def main():
    OUTPUT.parent.mkdir(parents=True,exist_ok=True)
    doc=ReviewDocTemplate(str(OUTPUT))
    doc.build(build_story(SOURCE.read_text(encoding="utf-8"),doc.width))
    print(f"Created {OUTPUT}")

if __name__ == "__main__": main()
