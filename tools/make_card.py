"""Render plain quote cards (flat off-white, text only) for the Wine Wimsey quote test.

Pause before the punchline (FFF-style): if the quote has two or more sentences, the last sentence is set
apart after a blank gap. A quote may also carry its own break as a literal "\\n\\n" (or a real blank line).
Single-sentence quotes are set as one block.

usage: make_card.py out.png "Quote text"
       make_card.py --batch quotes.json out_dir      # quotes.json: [{"id": "...", "quote": "..."}]
1080x1350 (4:5). Off-white background, near-black bold centered text, auto-sized to fit.
No watermark here: run tools/stamp.py --brand WineWimsey on the result (no --ai: flat type is not photo-style).
"""
import json, os, re, sys
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


def segments(text):
    text = text.replace("\\n", "\n").strip()
    if "\n\n" in text:
        return [s.strip() for s in text.split("\n\n") if s.strip()]
    sents = re.split(r"(?<=[.!?])\s+", text)
    if len(sents) >= 2:
        return [" ".join(sents[:-1]), sents[-1]]
    return [text]


def render(text, out):
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    width = W - 2 * MARGIN
    segs = segments(text)
    for size in range(76, 31, -2):
        font = ImageFont.truetype(FONT, size)
        blocks = [wrap(d, s, font, width) for s in segs]
        if sum(len(b) for b in blocks) <= MAX_LINES:
            break
    lead = round(size * 1.32)
    gap = round(size * 0.9) if len(blocks) > 1 else 0
    total = lead * sum(len(b) for b in blocks) + gap * (len(blocks) - 1)
    y = (H - total) // 2 - 20
    for i, b in enumerate(blocks):
        for ln in b:
            w = d.textlength(ln, font=font)
            d.text(((W - w) / 2, y), ln, font=font, fill=FG)
            y += lead
        if i < len(blocks) - 1:
            y += gap
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    im.save(out)
    return size, sum(len(b) for b in blocks)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--batch":
        for q in json.load(open(a[1])):
            out = os.path.join(a[2], q["id"] + ".png")
            print(out, *render(q["quote"], out))
    else:
        print(a[0], *render(a[1], a[0]))
