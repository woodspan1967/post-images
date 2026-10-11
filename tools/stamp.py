"""Stamp brand marks onto finished post images, in place.

usage: stamp.py [--brand WineWimsey] [--ai] image.png ...
  --brand TEXT  bold watermark, bottom-right; charcoal on light corners, white on dark ones
  --ai          faint 'AI-generated' label, bottom-left (photo-style images)
"""
import sys
from PIL import Image, ImageDraw, ImageFont, ImageStat
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def brand(im, text):
    w, h = im.size
    font = ImageFont.truetype(BOLD, max(12, round(h * 0.019)))
    l, t, r, b = ImageDraw.Draw(im).textbbox((0, 0), text, font=font)
    tw, th = r - l, b - t
    x, y = w - tw - round(w * 0.022), h - th - round(h * 0.02) - t
    lum = ImageStat.Stat(im.convert("L").crop((x - 6, y, x + tw + 6, y + th + t + 6))).mean[0]
    if lum > 110: fill, edge = (40, 40, 40, 240), (255, 255, 255, 200)
    else: fill, edge = (255, 255, 255, 235), (30, 30, 30, 200)
    layer = Image.new("RGBA", im.size, (0, 0, 0, 0))
    ImageDraw.Draw(layer).text((x, y), text, font=font, fill=fill, stroke_width=max(1, round(h * 0.0018)), stroke_fill=edge)
    return Image.alpha_composite(im, layer)

def ai_label(im):
    w, h = im.size
    size = max(12, round(h * 0.016))
    font = ImageFont.truetype(REG, size)
    layer = Image.new("RGBA", im.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    x, y = round(w * 0.018), h - round(h * 0.018) - size
    d.text((x + 1, y + 1), "AI-generated", font=font, fill=(0, 0, 0, 90))
    d.text((x, y), "AI-generated", font=font, fill=(255, 255, 255, 150))
    return Image.alpha_composite(im, layer)

args = sys.argv[1:]
text = None; ai = False; files = []
while args:
    a = args.pop(0)
    if a == "--brand": text = args.pop(0)
    elif a == "--ai": ai = True
    else: files.append(a)
for f in files:
    im = Image.open(f).convert("RGBA")
    if text: im = brand(im, text)
    if ai: im = ai_label(im)
    im.convert("RGB").save(f); print("stamped", f)
