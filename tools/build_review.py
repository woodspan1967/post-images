"""Build a review page folder from a batch file.

usage: build_review.py batch.json out_dir
batch.json: {"title","subtitle","bucket","story_bucket","posts":[...feed in queue order...],"stories":[...]}
Each item: id, kind (image|tobi|story), template, character, quote, caption, first, image (repo-relative png path, not for tobi),
  alt (alt text for every image post and story, under 500 chars; not for tobi)
Writes out_dir/index.html and out_dir/img/<id>.jpg. Publish index.html with files img/*.jpg and capabilities {db:{}, user:{}}.
"""
import json, os, sys
from PIL import Image
here = os.path.dirname(os.path.abspath(__file__)); repo = os.path.dirname(here)
b = json.load(open(sys.argv[1])); out = sys.argv[2]
os.makedirs(os.path.join(out, "img"), exist_ok=True)
items = b["posts"] + b.get("stories", [])
for p in items:
    if p.get("image"):
        Image.open(os.path.join(repo, p["image"])).convert("RGB").save(os.path.join(out, "img", p["id"] + ".jpg"), quality=86, optimize=True)
slim = [{k: p.get(k, "") for k in ("id", "kind", "template", "character", "quote", "caption", "first", "alt")} for p in items]
t = open(os.path.join(here, "review_template.html")).read()
t = t.replace("__TITLE__", b["title"]).replace("__SUB__", b["subtitle"]).replace("__STORYBUCKET__", b.get("story_bucket", "Wine Wimsy Stories")).replace("__BUCKET__", b.get("bucket", "Wine Wimsy")).replace("__POSTS__", json.dumps(slim).replace("</", "<\\/"))
open(os.path.join(out, "index.html"), "w").write(t)
missing = [p["id"] for p in items if p.get("kind") != "tobi" and not p.get("alt")]
if missing: print("WARNING: no alt text on", ", ".join(missing))
print("built", len(slim), "items ->", out)
