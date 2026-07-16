from pathlib import Path
from PIL import Image, ImageDraw

HERE = Path(__file__).resolve().parent
pages = sorted((HERE / "flocking-pages").glob("page-*.png"))
thumb_w, margin, label_h, columns, per_sheet = 320, 18, 28, 3, 6

for sheet_index in range(0, len(pages), per_sheet):
    batch = pages[sheet_index:sheet_index + per_sheet]
    thumbs = []
    for page in batch:
        image = Image.open(page).convert("RGB")
        ratio = thumb_w / image.width
        thumbs.append((page, image.resize((thumb_w, int(image.height * ratio)))))
    cell_h = max(thumb.height for _, thumb in thumbs) + label_h
    rows = (len(thumbs) + columns - 1) // columns
    sheet = Image.new("RGB", (columns*thumb_w+(columns+1)*margin, rows*cell_h+(rows+1)*margin), "#D9E2EC")
    draw = ImageDraw.Draw(sheet)
    for index, (page, thumb) in enumerate(thumbs):
        row, col = divmod(index, columns)
        x, y = margin+col*(thumb_w+margin), margin+row*cell_h
        sheet.paste(thumb, (x, y+label_h))
        draw.text((x, y+5), page.stem, fill="#102A43")
    out = HERE / f"flocking-contact-{sheet_index//per_sheet+1}.png"
    sheet.save(out, quality=92)
    print(out)
