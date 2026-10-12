"""Turn Meta Business Suite post exports into one tagged table for the weekly review.

usage: insights.py out.csv "<Page Name>=export.csv" ["<Page Name>=export2.csv" ...] [--history old_posts.csv]

- Reads each export (UTF-8, UTF-8 BOM or UTF-16), finds columns by name (Meta renames them now and then).
- Matches every post to the pipeline's batch.json files (batches/<page-slug>/<date>/batch.json) by caption,
  or by quote for TOBIs, and copies kind / template / character / quote from the batch.
- Posts not made by the pipeline (older posts, manual posts) stay in with source "manual".
- --history merges a previous posts.csv so the table keeps growing week to week (deduped by post_id).
- Prints a short summary of what it found and which columns were missing.
"""
import csv, glob, io, json, os, re, sys
from datetime import datetime

here = os.path.dirname(os.path.abspath(__file__)); repo = os.path.dirname(here)
SLUG = {"wine wimsey": "wine-wimsey", "whispers of yesterday": "whispers-of-yesterday", "horse soup": "horse-soup"}
OUT_COLS = ["post_id", "page", "published", "date", "weekday", "hour", "post_type", "source", "kind", "template",
            "character", "caption_words", "text", "permalink", "reach", "views", "reactions", "comments", "shares",
            "engagements", "clicks", "earnings"]

def read_rows(path):
    raw = open(path, "rb").read()
    for enc in ("utf-8-sig", "utf-16"):
        try:
            text = raw.decode(enc); break
        except UnicodeDecodeError:
            continue
    else:
        text = raw.decode("latin-1")
    sample = text[:4000]
    delim = "\t" if sample.count("\t") > sample.count(",") else ","
    return list(csv.DictReader(io.StringIO(text), delimiter=delim))

def col(headers, *wants, exact=False, avoid=()):
    low = {h: h.lower().strip() for h in headers}
    for w in wants:
        for h, l in low.items():
            if any(a in l for a in avoid):
                continue
            if (l == w) if exact else (w in l):
                return h
    return None

def num(v):
    if v is None: return ""
    s = str(v).replace(",", "").replace("$", "").strip()
    if s in ("", "-", "--"): return ""
    try: return float(s)
    except ValueError: return ""

def when(v):
    v = (v or "").strip()
    for f in ("%m/%d/%Y %H:%M", "%m/%d/%Y %I:%M %p", "%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M", "%m/%d/%Y"):
        try: return datetime.strptime(v, f)
        except ValueError: pass
    return None

def key(s):
    return re.sub(r"[^a-z0-9]+", "", (s or "").lower())[:60]

def batch_index(page):
    idx = {}
    for f in glob.glob(os.path.join(repo, "batches", SLUG.get(page.lower(), "?"), "*", "batch.json")):
        try: b = json.load(open(f))
        except Exception: continue
        for p in b.get("posts", []) + b.get("stories", []):
            for t in (p.get("caption"), p.get("quote")):
                if t and len(key(t)) >= 20:
                    idx.setdefault(key(t), p)
    return idx

def convert(page, path):
    rows = read_rows(path)
    if not rows: return [], ["no rows"]
    H = list(rows[0].keys())
    c = {
        "id": col(H, "post id"), "time": col(H, "publish time", "published", "created"),
        "text": col(H, "description", "message", "title"), "type": col(H, "post type", "type"),
        "link": col(H, "permalink", "link"),
        "reach": col(H, "reach", exact=True) or col(H, "reach", avoid=("paid",)),
        "views": col(H, "views", exact=True) or col(H, "impressions", avoid=("ad ",)),
        "rcs": col(H, "reactions, comments and shares"), "reactions": col(H, "reactions", exact=True),
        "comments": col(H, "comments", exact=True), "shares": col(H, "shares", exact=True),
        "clicks": col(H, "total clicks", "clicks"), "earn": col(H, "earning"),
    }
    missing = [k for k in ("id", "time", "text", "reach", "earn") if not c[k]]
    idx = batch_index(page); out = []
    for r in rows:
        g = lambda k: r.get(c[k], "") if c[k] else ""
        t = when(g("time")); text = g("text") or ""
        hit = idx.get(key(text))
        if not hit:  # caption may be cut; try prefix match
            k = key(text)
            hit = next((p for kk, p in idx.items() if k and (kk.startswith(k[:40]) or k.startswith(kk[:40]))), None) if len(k) >= 40 else None
        rx, cm, sh = num(g("reactions")), num(g("comments")), num(g("shares"))
        eng = num(g("rcs")) or (sum(x for x in (rx, cm, sh) if x != "") if any(x != "" for x in (rx, cm, sh)) else "")
        out.append({
            "post_id": g("id") or key(text)[:24], "page": page,
            "published": t.isoformat(timespec="minutes") if t else g("time"), "date": t.date().isoformat() if t else "",
            "weekday": t.strftime("%a") if t else "", "hour": t.hour if t else "", "post_type": g("type"),
            "source": "pipeline" if hit else "manual", "kind": (hit or {}).get("kind", ""),
            "template": (hit or {}).get("template", ""), "character": (hit or {}).get("character", ""),
            "caption_words": len(text.split()), "text": text[:140].replace("\n", " "), "permalink": g("link"),
            "reach": num(g("reach")), "views": num(g("views")), "reactions": rx, "comments": cm, "shares": sh,
            "engagements": eng, "clicks": num(g("clicks")), "earnings": num(g("earn")),
        })
    return out, missing

def main(a):
    out = a[0]; hist = None; pairs = []
    i = 1
    while i < len(a):
        if a[i] == "--history": hist = a[i + 1]; i += 2; continue
        pairs.append(a[i].split("=", 1)); i += 1
    rows = {}
    if hist and os.path.exists(hist):
        for r in csv.DictReader(open(hist)): rows[(r["page"], r["post_id"])] = r
    for page, path in pairs:
        new, missing = convert(page, path)
        for r in new: rows[(r["page"], r["post_id"])] = r
        pl = sum(1 for r in new if r["source"] == "pipeline")
        print(f"{page}: {len(new)} posts, {pl} matched to pipeline batches" + (f"; missing columns: {', '.join(missing)}" if missing else ""))
    w = csv.DictWriter(open(out, "w", newline=""), fieldnames=OUT_COLS, extrasaction="ignore")
    w.writeheader()
    for r in sorted(rows.values(), key=lambda r: (r["page"], r["published"])): w.writerow(r)
    print("wrote", len(rows), "rows ->", out)

if __name__ == "__main__":
    main(sys.argv[1:])
