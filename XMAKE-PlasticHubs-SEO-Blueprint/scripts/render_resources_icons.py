from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "plastichubs" / "resources-icons"
S = 4
BLUE = (11, 87, 255, 255)
W = 2 * S


def canvas():
    return Image.new("RGBA", (64 * S, 64 * S), (0, 0, 0, 0))


def line(draw, points, width=W):
    pts = [(round(x * S), round(y * S)) for x, y in points]
    draw.line(pts, fill=BLUE, width=width, joint="curve")
    r = width // 2
    for x, y in (pts[0], pts[-1]):
        draw.ellipse((x-r, y-r, x+r, y+r), fill=BLUE)


def ring(draw, center, radius):
    x, y = center
    draw.ellipse(((x-radius)*S, (y-radius)*S, (x+radius)*S, (y+radius)*S), outline=BLUE, width=W)


def rounded_rect(draw, box, radius):
    draw.rounded_rectangle(tuple(round(v * S) for v in box), radius=radius * S, outline=BLUE, width=W)


def quadratic(draw, start, control, end, steps=24):
    points = []
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        points.append((
            u*u*start[0] + 2*u*t*control[0] + t*t*end[0],
            u*u*start[1] + 2*u*t*control[1] + t*t*end[1],
        ))
    line(draw, points)


def save(img, name):
    img.resize((256, 256), Image.Resampling.LANCZOS).save(OUT / f"{name}.png")


def page(draw, chart=False):
    line(draw, [(18, 8), (38, 8), (48, 18), (48, 56), (18, 56), (18, 8)])
    line(draw, [(38, 8), (38, 18), (48, 18)])
    if chart:
        line(draw, [(24, 46), (47, 46)])
        for x, y in [(25, 36), (33, 28), (41, 32)]:
            line(draw, [(x, 46), (x, y), (x+5, y), (x+5, 46)])
    else:
        line(draw, [(25, 29), (41, 29)])
        line(draw, [(25, 36), (41, 36)])
        line(draw, [(25, 43), (37, 43)])


img = canvas(); d = ImageDraw.Draw(img); page(d); save(img, "blog")
img = canvas(); d = ImageDraw.Draw(img)
rounded_rect(d, (16, 14, 48, 56), 3)
rounded_rect(d, (24, 8, 40, 18), 3)
line(d, [(23,45),(23,28)])
line(d, [(23,45),(44,45)])
line(d, [(24,41),(31,34),(37,38),(44,28)])
save(img, "case-studies")

img = canvas(); d = ImageDraw.Draw(img)
for pts in [[(32,24),(32,15)],[(25,29),(16,23)],[(39,29),(48,23)],[(32,40),(32,49)]]: line(d, pts)
for c, r in [((32,32),8),((32,9),6),((11,20),6),((53,20),6),((32,55),6)]: ring(d, c, r)
save(img, "material-guide")

img = canvas(); d = ImageDraw.Draw(img)
ring(d, (32,14), 5)
for pts in [[(29,18),(17,51)],[(35,18),(47,51)],[(24,34),(40,34)],[(14,52),(21,52)],[(43,52),(50,52)]]: line(d, pts)
quadratic(d, (19,46), (32,56), (45,46))
save(img, "design-guides")
