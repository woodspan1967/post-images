# Horse Soup daily run (runbook)

Follow PIPELINE.md for every rule. This file is the order of operations. Default: one day.
If Scott asked for more days ahead (vacation), multiply counts by that number of days.

**First read the "All pages: hard rules" section of PIPELINE.md (no realistic people, no reused quotes or jokes, rejected = replaced). They override the skill and this file.**

## 0. Setup
- Clone/pull this repo (woodspan1967/post-images, push access). Work in it.
- Load the Horse Soup skill (`horse-soup`) for characters, Shared Style Lock / Whimsy Lock, templates (I2, I, W, H, F), auto-routing, caption and first-comment rules, the TOBI five-test quality filter, theme rotation and guardrails. The meme sections only: reels are not part of this run.
- Pipeline overrides to the skill (the pipeline wins where they differ):
  - Every image is vertical 4:5. Templates W and H (square 1:1 in the skill) are composed for 4:5: W keeps its bubble upper right; H puts the character in the lower left and the hand-lettered quote in the upper right.
  - Do NOT use the skill's STANDARD FOOTER (the 'HorseSoup' watermark sentence). Replace it with the pipeline ending below. The watermark is stamped afterwards as "Horse Soup".
  - No second comment. Write the caption + one first comment (posted with a 5-minute delay). The skill's SECOND COMMENT is skipped.
  - TOBI = the quote text + first comment. Quote under 130 characters (Post Planner TOBI). The skill's TOBI caption is not written (the quote is the post).
- Read `held/horse-soup.json`: approved posts carried over. They count toward today's 6 and go first. Clear the file after you use them.
- Read `used/horse-soup-quotes.txt`: never reuse a quote. Also avoid repeating a theme used in the last 3 days of that file.

## 0b. Inbox (Scott's curated items) — use these first
- Inbox page: https://claude.ai/artifact/4WXju43mLVkJfK1CLEwp7v . Read collection `inbox` with ArtifactData (action list).
- Each doc: quote, note, placement (auto|feed|tobi|story), assetId (uploaded image, may be empty), status (new|used), createdAt.
- For an image item: download it with the Artifact tool (action read, url = inbox page, path = assetId) and look at it.
  - If it carries a quote, that quote is the post's quote, word for word (skill QUOTE FIDELITY). If he also typed a quote, the typed one wins.
  - Rebuild it in Horse Soup style (skill RECREATE) with one of the five characters. Never reproduce trademarked characters, logos or someone else's art.
- Quote-only items follow skill CREATE FOR THIS: pick template + character with the skill's READ THE FEEL table (or follow his note), write caption + first comment.
- Placement: tobi -> TOBI slot (quote must be under 130 chars, else make it a feed post and say so); story -> story slot; feed or auto -> feed slot (auto may go to story if the feed is full).
- New inbox items fill slots before anything you write yourself. Oldest first. If there are more than fit today, leave the rest as new for tomorrow.
- Mark each used item in the inbox: ArtifactData update {status:"used", usedIn:"<Mon D> review"} with its if_version. Mention on the review page subtitle how many came from the inbox.

## 1. Write the day
- 6 feed posts total = held posts + new ones: 5 image posts + 1 TOBI. TOBI goes in the middle of the queue (slot 3 or 4), not first or last.
- 2 stories (image only, own quotes, never a feed quote).
- Characters: all five appear once across the 5 image posts (The Diva, Big Red, The Homebody, The Old Timer, Pudding), assigned by the quote's feel. At most 1 two-character scene a day. Stories may use any character.
- Templates across the 5 image posts: 2 I2 (speech bubble, ALL CAPS), 1 W (whimsical storybook), 1 H (character card), 1 F (banner) or I (soft bubble), alternating F and I day to day. Stories use I2 or W. Never the same setting twice in a day.
- Quotes: image text about 25 words max (W up to 40). ALL CAPS in I2 and F in the prompt; the quote field in batch.json matches exactly what the image should show. Wall signs 2-4 words from the skill's sign bank.
- Themes: rotate the skill's theme list, never more than 2 posts on the same theme in a day (feed + stories together).
- Captions: skill SEE MORE structure, ~100 words (hook / story / button), never repeats the quote, one real barn detail, no em dashes, none of the banned phrases. First comment ~50 words, first person, no question, no CTA, no emoji, no hashtags.
- TOBI: one quote under 130 characters that passes the skill's five-test filter, + first comment (same first-comment rules). Background `black`.
- Image prompts: open with the Shared Style Lock (Whimsy Lock for W), paste the full character descriptor, follow the template, and end with:
  "The only text in the image is the [speech bubble / banner / hand-lettered] text[ and the small wall sign]. Keep the bottom corners plain. Vertical 4:5 format."
  Never ask the model for a watermark. No banned phrases (skill rule 4).
- Guardrails: no horse injury/neglect/slaughter humor, no alcohol or smoking, adult humans only and secondary, no real brand names, no politics.
- Ids: feed `hs-YYYYMMDD-NN`, TOBI `hs-YYYYMMDD-t1`, stories `hss-YYYYMMDD-N`.
- Write `batches/horse-soup/YYYY-MM-DD/batch.json` (format in tools/build_review.py) with title "Horse Soup Review · <Mon D>", a one-line subtitle, `"bucket": "Horse Soup"`, `"story_bucket": "Horse Soup Stories"`, feed in queue order. Put the template name in `template` (e.g. "I2 speech bubble", "W storybook", "H character card", "F banner", "I soft bubble") and the character in `character`.

## 2. Images
- ElevenLabs: one flow per day, one image-generation node per image (7 a day), model gpt-image-2.5-sunburst, {aspect_ratio 4:5, resolution 1K, quality low}; run all nodes; poll creative_get_flow_run_status until done.
- `python3 tools/signed_urls.py <dest>=<generation_id> ... > queue/<name>.txt` with dest `horse-soup/YYYY-MM-DD/<id>.png` (stories under `.../stories/`). Commit + push, wait ~60s, pull.
- Stamp: `python3 tools/stamp.py --brand "Horse Soup" <pngs>` on every image. No `--ai`: every Horse Soup image is a cartoon. (If an inbox item ever has to stay photo-style, it gets `--ai` too.) Commit + push.
- Look at every image: quote matches word for word, four-legged horse anatomy (no hands, not upright), Pudding cute (no teeth, no half-lidded eyes), right character markings, no stray logos or extra text. Regenerate any that fail (once), then flag anything still off in the page subtitle.
- Set each item's `image` to the repo path.

## 3. Review page
- `python3 tools/build_review.py batches/.../batch.json <scratch>/review` then publish `<scratch>/review/index.html` as a NEW artifact with files img/*.jpg, capabilities {db:{}, user:{}}, icon "checklist".
- Append today's quotes to used/horse-soup-quotes.txt as "YYYY-MM-DD | theme | quote", commit + push batch.json.
- Send Scott the review link with SendUserMessage (counts, credits used, anything flagged).

## 4. When Scott replies
- Read the page's `decisions` collection (ArtifactData). `redo` -> regenerate with his note; `rejected` -> write a replacement for that slot; update the page (same artifact) and reset those docs to "" so they show as Waiting.
- Approved posts he wants to hold for tomorrow go into held/horse-soup.json (same shape as held/wine-wimsey.json).
- On "upload" (needs his desktop app open; built-in browser, Post Planner signed in, viewport 1280x800 or it shows a mobile wall):
  - `python3 tools/build_csv.py batch.json approved.txt <scratch>/csv`
  - Create multiple posts -> Bucket "Horse Soup" -> inject feed CSV into the spreadsheet file input via DataTransfer -> confirm count with Scott -> Upload to bucket.
  - Repeat with bucket "Horse Soup Stories" and the stories CSV.
  - First upload only: check the exact bucket names in Post Planner's list and fix this file and PIPELINE.md if they differ.
  - Spot-check in the bucket (search a caption) that images and first comments landed. Reset viewport.
