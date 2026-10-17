# Whispers Of Yesterday daily run (runbook)

Follow PIPELINE.md for every rule. This file is the order of operations. Default: one day.
If Scott asked for more days ahead (vacation), multiply counts by that number of days.

**First read the "All pages: hard rules" section of PIPELINE.md (no realistic people, no reused quotes or jokes, rejected = replaced). They override the skill and this file.**

## 0. Setup
- Clone/pull this repo (woodspan1967/post-images, push access). Work in it.
- Load the Whispers Of Yesterday skill (`whispers-of-yesterday`) for voice, themes, templates, story captions, first comments, hashtag block, quote bank.
- Pipeline overrides to the skill (the pipeline wins where they differ):
  - Format is vertical 4:5, never "Square 1:1" or "8K". Drop those phrases from the skill's prompt templates.
  - Do NOT put the skill's watermark sentence in prompts. The watermark is stamped afterwards (`--brand "Whispers Of Yesterday"`).
  - Story-caption and first-comment rules are the skill's own (4-8 sentence story caption; 2-4 sentence first-person first comment + 5-8 hashtags after a line break). Do not apply Wine Wimsey's ~100-word caption rule.
- Read `held/whispers-of-yesterday.json`: approved posts carried over. They count toward today's 10 and go first. Clear the file after you use them.
- Read `used/whispers-of-yesterday-quotes.txt`: never reuse a quote or headline. Also avoid repeating a topic used in the last 7 days of that file.

## 0b. Inbox (Scott's curated items) — use these first
- Inbox page: https://claude.ai/artifact/ELPgE7UJER5X8nkBwC74ch . Read collection `inbox` with ArtifactData (action list).
- Each doc: quote, note, placement (auto|feed|tobi|story), assetId (uploaded image, may be empty), status (new|used), createdAt.
- For an image item: download it with the Artifact tool (action read, url = inbox page, path = assetId) and look at it.
  - If it carries a quote, that quote is the post's quote, word for word (skill QUOTE FIDELITY). If he also typed a quote, the typed one wins.
  - Rebuild it in Whispers Of Yesterday style (skill RECREATE). Never reproduce someone else's art, logos, or watermarks; make a fresh image in one of the page's templates.
- Quote-only items follow skill CREATE FOR THIS: pick a template (or follow his note), write caption + first comment.
- Placement: tobi -> TOBI slot (quote must be under 130 chars, else make it a feed post and say so); story -> story slot; feed or auto -> feed slot (auto may go to story if the feed is full).
- New inbox items fill slots before anything you write yourself. Oldest first. If there are more than fit today, leave the rest as new for tomorrow.
- Mark each used item in the inbox: ArtifactData update {status:"used", usedIn:"<Mon D> review"} with its if_version. Mention on the review page subtitle how many came from the inbox.

## 1. Write the day
- 10 feed posts total = held posts + new ones. Pick 1 or 2 TOBIs (vary day to day); the rest are image posts (so 9+1 or 8+2).
- 3 stories (image only, own quotes, never a feed quote).
- Templates across the image posts, roughly the skill's 5/3/2 ratio: for 8-9 images about 4-5 Template 1 (illustrated scene), 2-3 Template 2 (vintage photo), 1-2 Template 3 (retro poster). Stories use any template.
- Template 1 change: it must read as a PAINTING, not a photo. Replace the skill's "richly painted photorealistic illustration" with "a warm hand-painted Saturday Evening Post style illustration with visible brushstrokes and slightly stylized faces, clearly a painting, not a photograph".
- Template 2 change: vintage photos must contain NO people (no faces, hands or figures, not even in the background). Use the era's objects and places: a 1960s gas station at dusk, a chrome diner counter, a wood-paneled station wagon, a brass cash register, a rotary phone on a kitchen wall. Add "no people anywhere in the frame" to the prompt.
- Never use the skill's QUOTE / CONCEPT BANK lines; write fresh ones (see PIPELINE.md hard rule 2).
- Themes: rotate the skill's Core Nostalgia Themes, never more than 2 on the same theme in a day (feed + stories together).
- Quote text on images in ALL CAPS in the prompt, and the quote field in batch.json matches what the image should show.
- Children appear only in wholesome, era-typical family/school/play scenes. No cigarettes, no named celebrities, no real brand logos or store names.
- Image prompts: end with "No other text, signs, logos, signatures, or watermarks anywhere in the image; keep the bottom corners plain. Vertical 4:5 portrait format." Never ask the model for a watermark.
- TOBI: text under 130 characters, a nostalgia memory line or question in the page voice, + first comment (skill format, with hashtags). Background `black`.
- Ids: feed `wy-YYYYMMDD-NN`, TOBI `wy-YYYYMMDD-tN`, stories `wys-YYYYMMDD-N`.
- Write `batches/whispers-of-yesterday/YYYY-MM-DD/batch.json` (format in tools/build_review.py) with title "Whispers Of Yesterday Review · <Mon D>", a one-line subtitle, `"bucket": "Whispers Of Yesterday"`, `"story_bucket": "Whispers Of Yesterday Stories"`, feed in queue order with TOBIs spread between images. Put the template name in `template` (e.g. "T1 illustrated scene", "T2 vintage photo", "T3 retro poster") and the theme in `character`.

## 2. Images
- ElevenLabs: one flow per day, one image-generation node per image, model gpt-image-2.5-sunburst, {aspect_ratio 4:5, resolution 1K, quality low}; run all nodes; poll creative_get_flow_run_status until done.
- `python3 tools/signed_urls.py <dest>=<generation_id> ... > queue/<name>.txt` with dest `whispers-of-yesterday/YYYY-MM-DD/<id>.png` (stories under `.../stories/`). Commit + push, wait ~60s, pull.
- Stamp: `python3 tools/stamp.py --brand "Whispers Of Yesterday" <pngs>` on every image; add `--ai` to every photo-style image (Template 2, which is people-free). Painted Template 1 scenes and flat retro posters get the brand only. If any person looks photographic, regenerate before stamping. Commit + push.
- Look at every image: quote must match word for word, no stray logos or extra text, era looks right (no modern objects). Regenerate any that fail (once), then flag anything still off in the page subtitle.
- Set each item's `image` to the repo path.
- Alt text: add `alt` to every image post and story (not TOBIs), following PIPELINE.md "AI content + alt text". Write it after you've looked at the final image, so it describes what is actually there.

## 3. Review page
- `python3 tools/build_review.py batches/.../batch.json <scratch>/review` then publish `<scratch>/review/index.html` as a NEW artifact with files img/*.jpg, capabilities {db:{}, user:{}}, icon "checklist".
- Append today's quotes/headlines to used/whispers-of-yesterday-quotes.txt, commit + push batch.json.
- Send Scott the review link with SendUserMessage (counts, credits used, anything flagged, any post missing alt text).

## 4. When Scott replies
- Read the page's `decisions` collection (ArtifactData). `redo` -> regenerate with his note; `rejected` -> write a replacement for that slot; update the page (same artifact) and reset those docs to "" so they show as Waiting.
- Approved posts he wants to hold for tomorrow go into held/whispers-of-yesterday.json (same shape as held/wine-wimsey.json).
- On "upload" (needs his desktop app open; built-in browser, Post Planner signed in, viewport 1280x800 or it shows a mobile wall):
  - `python3 tools/build_csv.py batch.json approved.txt <scratch>/csv`
  - Create multiple posts -> Bucket "Whispers Of Yesterday" -> inject feed CSV into the spreadsheet file input via DataTransfer -> confirm count with Scott -> Upload to bucket.
  - Repeat with bucket "Whispers Of Yesterday Stories" and the stories CSV.
  - AI content + alt text (PIPELINE.md): after each bucket upload, reload that bucket's page, take one screenshot (the list doesn't draw while the pane is hidden), paste `tools/pp_post_options.js` into javascript_tool, run `await __pp.run(<output of python3 tools/alt_jobs.py batch.json approved.txt feed>)` (stories bucket: `stories`). All results must be ok:true; retry failures once, then tell Scott which posts.
  - Spot-check in the bucket (search a caption) that images, first comments, AI content and alt text landed. Reset viewport.
