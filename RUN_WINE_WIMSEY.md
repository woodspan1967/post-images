# Wine Wimsey daily run (runbook)

Follow PIPELINE.md for every rule. This file is the order of operations. Default: one day.
If Scott asked for more days ahead (vacation), multiply counts by that number of days.

**First read the "All pages: hard rules" section of PIPELINE.md (no realistic people, no reused quotes or jokes, rejected = replaced). They override the skill and this file.**

## 0. Setup
- Clone/pull this repo (woodspan1967/post-images, push access). Work in it.
- Load the Wine Wimsey skill (`wine-niche-initiative`) for characters, templates, voice, caption/comment rules, quote quality filter.
- Read `held/wine-wimsey.json`: approved posts carried over. They count toward today's 12 and go first. Clear the file after you use them.
- Read `used/wine-wimsey-quotes.txt`: never reuse a quote.

## 0b. Inbox (Scott's curated items) — use these first
- Inbox page: https://claude.ai/artifact/Fxf3RdrmK5pmoH3bfJzVwD . Read collection `inbox` with ArtifactData (action list).
- Each doc: quote, note, placement (auto|feed|tobi|story), assetId (uploaded image, may be empty), status (new|used), createdAt.
- For an image item: download it with the Artifact tool (action read, url = inbox page, path = assetId) and look at it.
  - If it carries a quote, that quote is the post's quote, word for word (skill QUOTE FIDELITY). If he also typed a quote, the typed one wins.
  - Rebuild it in Wine Wimsey style (skill RECREATE). Never reproduce trademarked characters, logos or someone else's art; swap in a Wine Wimsey character.
- Quote-only items follow skill CREATE FOR THIS: pick template + character (or follow his note), write caption + first comment.
- Placement: tobi -> TOBI slot (quote must be under 130 chars, else make it a feed post and say so); story -> story slot; feed or auto -> feed slot (auto may go to story if the feed is full).
- New inbox items fill slots before anything you write yourself. Oldest first. If there are more than fit today, leave the rest as new for tomorrow.
- Mark each used item in the inbox: ArtifactData update {status:"used", usedIn:"<Mon D> review"} with its if_version. Mention on the review page subtitle how many came from the inbox.

## 1. Write the day
- 12 feed posts total = held posts + new ones. Pick 1 or 2 TOBIs (vary day to day); the rest are image posts.
- 4 stories (image only, own quotes).
- Mix templates and characters per the skill (I2 is the primary format). Do NOT use Template B (photoreal) or Template C (vintage B&W photo) with people; if you want those looks, make them people-free (still life, empty porch) or draw the people as illustration. Template D still life is fine (AI label).
- Captions ~100 words (hook / story / button), first comment ~50 words, no hashtags. TOBI text under 130 characters + first comment.
- Image prompts: end with "No other text, signs, logos, signatures, or watermarks anywhere in the image; keep the bottom corners plain. Vertical 4:5 portrait format." Never ask the model for a watermark.
- Ids: feed `ww-YYYYMMDD-NN`, TOBI `ww-YYYYMMDD-tN`, stories `ws-YYYYMMDD-N`.
- Write `batches/wine-wimsey/YYYY-MM-DD/batch.json` (format in tools/build_review.py) with title "Wine Wimsey Review · <Mon D>" and a one-line subtitle, feed in queue order with TOBIs spread between images.

## 2. Images
- ElevenLabs: one flow per day, one image-generation node per image, model gpt-image-2.5-sunburst, {aspect_ratio 4:5, resolution 1K, quality low}; run all nodes; poll creative_get_flow_run_status until done.
- `python3 tools/signed_urls.py <dest>=<generation_id> ... > queue/<name>.txt` with dest `wine-wimsey/YYYY-MM-DD/<id>.png` (stories under `.../stories/`). Commit + push, wait ~60s, pull.
- Stamp: `python3 tools/stamp.py --brand WineWimsey <pngs>`; add `--ai` for photo-style images; skip --brand for vintage posters with an in-scene signature. Commit + push.
- Look at every image: quote must match word for word, no stray brand logos. Regenerate any that fail (once), then flag anything still off in the page subtitle.
- Set each item's `image` to the repo path.
- Alt text: add `alt` to every image post and story (not TOBIs), following PIPELINE.md "AI content + alt text". Write it after you've looked at the final image, so it describes what is actually there.

## 3. Review page
- `python3 tools/build_review.py batches/.../batch.json <scratch>/review` then publish `<scratch>/review/index.html` as a NEW artifact with files img/*.jpg, capabilities {db:{}, user:{}}, icon "checklist".
- Append today's quotes to used/wine-wimsey-quotes.txt, commit + push batch.json.
- Send Scott the review link with SendUserMessage (counts, credits used, anything flagged, any post missing alt text).

## 4. When Scott replies
- Read the page's `decisions` collection (ArtifactData). `redo` -> regenerate with his note; `rejected` -> write a replacement for that slot; update the page (same artifact) and reset those docs to "" so they show as Waiting.
- On "upload" (needs his desktop app open; built-in browser, Post Planner signed in, viewport 1280x800 or it shows a mobile wall):
  - `python3 tools/build_csv.py batch.json approved.txt <scratch>/csv`
  - Create multiple posts -> Bucket "Wine Wimsy" -> inject feed CSV into the spreadsheet file input via DataTransfer -> confirm count with Scott -> Upload to bucket.
  - Repeat with bucket "Wine Wimsy Stories" and the stories CSV.
  - AI content + alt text (PIPELINE.md): after each bucket upload, reload that bucket's page, take one screenshot (the list doesn't draw while the pane is hidden), paste `tools/pp_post_options.js` into javascript_tool, run `await __pp.run(<output of python3 tools/alt_jobs.py batch.json approved.txt feed>)` (stories bucket: `stories`). All results must be ok:true; retry failures once, then tell Scott which posts.
  - Spot-check in the bucket (search a caption) that images, first comments, AI content and alt text landed. Reset viewport.
