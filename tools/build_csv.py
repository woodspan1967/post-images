"""Build Post Planner bulk-upload CSVs (template v3.1) for approved items.

usage: build_csv.py batch.json approved_ids.txt out_dir
Writes out_dir/feed.csv and out_dir/stories.csv, plus feed.js.txt / stories.js.txt holding each CSV
as a JSON string literal for pasting into the browser's file-input injection script.
Image URLs are https://raw.githubusercontent.com/woodspan1967/post-images/main/<image>.
No hashtags in first comments (PIPELINE.md hard rule 3): any #tag is stripped here with a warning.
"""
import csv, io, json, os, re, sys
b = json.load(open(sys.argv[1])); ok = set(open(sys.argv[2]).read().split()); out = sys.argv[3]
RAW = "https://raw.githubusercontent.com/woodspan1967/post-images/main/"
HEAD = [["## This is a comment row. Any row starting with ## will be ignored when your posts are uploaded. You can use comment rows to add notes.", "BULK UPLOAD VERSION 3.1 — Please DO NOT EDIT this cell.", "", "", "", "", "", "", ""],
        ["## POSTING TIME", "CAPTION", "LINK", "MEDIA", "TITLE", "FIRST COMMENT", "FIRST COMMENT DELAY", "TOBI BACKGROUND", "REEL OR STORY"]]
def write(name, rows):
    s = io.StringIO(); csv.writer(s, quoting=csv.QUOTE_ALL, lineterminator="\r\n").writerows(HEAD + rows)
    open(os.path.join(out, name + ".csv"), "w").write(s.getvalue())
    open(os.path.join(out, name + ".js.txt"), "w").write(json.dumps(s.getvalue()))
    print(name, len(rows), "rows")
os.makedirs(out, exist_ok=True)
TAG = re.compile(r"(?<![\w&])#[A-Za-z][\w]*")
stripped = []
def clean(pid, text):
    if not TAG.search(text or ""): return text
    stripped.append(pid)
    lines = [re.sub(r"[ \t]{2,}", " ", TAG.sub("", ln)).strip() for ln in text.split("\n")]
    while lines and not lines[-1]: lines.pop()
    return "\n".join(lines)
feed = []
for p in b["posts"]:
    if p["id"] not in ok: continue
    if p["kind"] == "tobi": feed.append(["", p["quote"], "", "", "", clean(p["id"], p["first"]), "5", "black", ""])
    else: feed.append(["", clean(p["id"] + " caption", p["caption"]), "", RAW + p["image"], "", clean(p["id"], p["first"]), "5", "", ""])
if stripped: print("WARNING: removed hashtags from", ", ".join(stripped), "(no hashtags in first comments)")
write("feed", feed)
write("stories", [["", "", "", RAW + s["image"], "", "", "", "", "story"] for s in b.get("stories", []) if s["id"] in ok])
