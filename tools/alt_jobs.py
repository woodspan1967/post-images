"""Print the job list for tools/pp_post_options.js (AI content + alt text in Post Planner).

usage: alt_jobs.py batch.json approved.txt [feed|stories]
Prints a JSON array to paste into: await __pp.run(<array>)
Feed image posts are found by searching their caption; stories (no caption) by image file name.
TOBIs are skipped: they have no media, so Post Planner shows no AI/alt options for them.
"""
import json, os, sys
b = json.load(open(sys.argv[1])); ok = set(open(sys.argv[2]).read().split())
which = sys.argv[3] if len(sys.argv) > 3 else "feed"
items = b["posts"] if which == "feed" else b.get("stories", [])
jobs, missing = [], []
for p in items:
    if p["id"] not in ok or p.get("kind") == "tobi" or not p.get("image"): continue
    if not p.get("alt"): missing.append(p["id"]); continue
    if which == "feed":
        words = p["caption"].split()
        jobs.append({"search": " ".join(words[:6]), "caption": p["caption"][:40], "alt": p["alt"][:500]})
    else:
        jobs.append({"image": os.path.basename(p["image"]), "alt": p["alt"][:500]})
if missing: sys.exit("no alt text on: " + ", ".join(missing) + " (write it into batch.json first)")
print(json.dumps(jobs, ensure_ascii=False))
