from __future__ import annotations

import hashlib
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "output" / "word"
NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
}


def norm(text: str) -> str:
    return re.sub(r"\s+", "", text).replace("\\|", "|")


def visible_markdown_line(line: str) -> str:
    s = line.strip()
    if not s or s == "---" or re.fullmatch(r"\|?\s*:?-{3,}:?(\s*\|\s*:?-{3,}:?)+\s*\|?", s):
        return ""
    s = re.sub(r"^#{1,6}\s+", "", s)
    s = re.sub(r"^H[1-6][：:]\s*", "", s)
    s = re.sub(r"^[-*+]\s+", "", s)
    s = re.sub(r"^\d+[.)]\s+", "", s)
    s = re.sub(r"^>\s+", "", s)
    if s.startswith("|") and s.endswith("|"):
        s = "".join(part.strip() for part in re.split(r"(?<!\\)\|", s.strip("|")))
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
    s = s.replace("**", "").replace("`", "")
    return s


def check_one(docx: Path):
    source = ROOT / docx.name.replace("-bilingual-review.docx", "-surface-finishing-page.md")
    errors = []
    with zipfile.ZipFile(docx) as zf:
        bad = zf.testzip()
        if bad:
            errors.append(f"corrupt member: {bad}")
        document_xml = zf.read("word/document.xml")
        styles_xml = zf.read("word/styles.xml")
        footer_xml = b"".join(zf.read(name) for name in zf.namelist() if name.startswith("word/footer") and name.endswith(".xml"))

    root = ET.fromstring(document_xml)
    doc_text = norm("".join(node.text or "" for node in root.findall(".//w:t", NS)))
    source_lines = source.read_text(encoding="utf-8-sig").splitlines()
    visible_lines = [visible_markdown_line(line) for line in source_lines]
    missing = []
    for line_no, line in enumerate(visible_lines, 1):
        candidate = norm(line)
        if len(candidate) >= 4 and candidate not in doc_text:
            missing.append((line_no, line[:120]))
    if missing:
        errors.append(f"missing visible source lines: {missing[:8]} (total={len(missing)})")

    source_headings = sum(1 for line in source_lines if re.match(r"^#{1,6}\s+", line)) - 1
    heading_paras = 0
    for p in root.findall(".//w:body/w:p", NS):
        style = p.find("./w:pPr/w:pStyle", NS)
        if style is not None and style.attrib.get(f"{{{NS['w']}}}val", "").startswith("Heading"):
            heading_paras += 1
    if source_headings != heading_paras:
        errors.append(f"heading count source={source_headings} docx={heading_paras}")

    source_links = sum(len(re.findall(r"\[[^\]]+\]\([^)]+\)", line)) for line in source_lines)
    doc_links = len(root.findall(".//w:hyperlink", NS))
    if source_links != doc_links:
        errors.append(f"hyperlink count source={source_links} docx={doc_links}")

    table_blocks = 0
    in_table = False
    for line in source_lines:
        current = line.strip().startswith("|")
        if current and not in_table:
            table_blocks += 1
        in_table = current
    doc_tables = root.findall(".//w:tbl", NS)
    if table_blocks != len(doc_tables):
        errors.append(f"table count source={table_blocks} docx={len(doc_tables)}")

    for idx, table in enumerate(doc_tables, 1):
        tbl_w = table.find("./w:tblPr/w:tblW", NS)
        tbl_ind = table.find("./w:tblPr/w:tblInd", NS)
        width = int(tbl_w.attrib.get(f"{{{NS['w']}}}w", "0")) if tbl_w is not None else 0
        indent = int(tbl_ind.attrib.get(f"{{{NS['w']}}}w", "-1")) if tbl_ind is not None else -1
        grid = [int(n.attrib.get(f"{{{NS['w']}}}w", "0")) for n in table.findall("./w:tblGrid/w:gridCol", NS)]
        if width != 9360 or indent != 120 or sum(grid) != 9360:
            errors.append(f"table {idx} geometry tblW={width} tblInd={indent} grid={grid}")
        for r_idx, row in enumerate(table.findall("./w:tr", NS), 1):
            tcws = []
            for cell in row.findall("./w:tc", NS):
                tcw = cell.find("./w:tcPr/w:tcW", NS)
                tcws.append(int(tcw.attrib.get(f"{{{NS['w']}}}w", "0")) if tcw is not None else 0)
            if tcws != grid:
                errors.append(f"table {idx} row {r_idx} cell widths={tcws} grid={grid}")
                break
        if table.findall(".//w:trHeight", NS):
            errors.append(f"table {idx} has fixed row height")
        header = table.find("./w:tr/w:trPr/w:tblHeader", NS)
        if header is None:
            errors.append(f"table {idx} missing repeating header")

    styles_text = styles_xml.decode("utf-8", errors="ignore")
    if "Microsoft YaHei" not in styles_text or "Calibri" not in styles_text:
        errors.append("required western/eastAsia font mappings missing")
    if b"PAGE" not in footer_xml:
        errors.append("footer PAGE field missing")
    for residue in ("**", "# H1", "## H2", "### H3"):
        if residue in doc_text:
            errors.append(f"markdown residue: {residue}")

    sha = hashlib.sha256(docx.read_bytes()).hexdigest()
    return {
        "file": docx.name,
        "bytes": docx.stat().st_size,
        "sha256": sha,
        "source_lines": len(source_lines),
        "headings": heading_paras,
        "tables": len(doc_tables),
        "hyperlinks": doc_links,
        "errors": errors,
    }


def main():
    results = [check_one(path) for path in sorted(OUT.glob("*.docx"))]
    failed = False
    for result in results:
        status = "PASS" if not result["errors"] else "FAIL"
        print(f"{status} {result['file']} lines={result['source_lines']} headings={result['headings']} tables={result['tables']} links={result['hyperlinks']} sha256={result['sha256']}")
        for error in result["errors"]:
            print(f"  - {error}")
        failed = failed or bool(result["errors"])
    raise SystemExit(1 if failed else 0)


if __name__ == "__main__":
    main()
