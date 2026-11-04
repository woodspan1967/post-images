"""Render plain quote cards (flat off-white, text only) for the Wine Wimsey quote test.

usage: make_card.py out.png "Quote text"
       make_card.py --batch quotes.json out_dir      # quotes.json: [{"id": "...", "quote": "..."}]
1080x1350 (4:5). Off-white background, near-black bold centered text, auto-sized to fit.
No watermark here: run tools/stamp.py --brand WineWimsey on the result (no --ai: flat type is not photo-style).
"""
import json, os, sys
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1350
BG, FG = (244, 241, 234), (31, 31, 31)
MARGIN = 100
MAX_LINES = 8
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def wrap(draw, text, font, width):
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=font) <= width or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def render(text, out):
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    width = W - 2 * MARGIN
    for size in range(76, 31, -2):
        font = ImageFont.truetype(FONT, size)
        lines = wrap(d, text, font, width)
        if len(lines) <= MAX_LINES:
            break
    lead = round(size * 1.32)
    total = lead * len(lines)
    y = (H - total) // 2 - 20
    for ln in lines:
        w = d.textlength(ln, font=font)
        d.text(((W - w) / 2, y), ln, font=font, fill=FG)
        y += lead
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    im.save(out)
    return size, len(lines)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--batch":
        for q in json.load(open(a[1])):
            out = os.path.join(a[2], q["id"] + ".png")
            print(out, *render(q["quote"], out))
    else:
        print(a[0], *render(a[1], a[0]))
