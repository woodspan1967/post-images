# Wine Wimsey daily run (runbook)

Follow PIPELINE.md for every rule. This file is the order of operations. Default: one day.
If Scott asked for more days ahead (vacation), multiply counts by that number of days.

**First read the "All pages: hard rules" section of PIPELINE.md (no realistic people, no reused quotes or jokes, rejected = replaced). They override the skill and this file.**

## 0. Setup
- Clone/pull this repo (woodspan1967/post-images, push access). Work in it.
- Load the Wine Wimsey skill (`wine-niche-initiative`) for characters, templates, voice, caption/comment rules, quote quality filter.
- Read `held/wine-wimsey.json`: approved posts carried over. They count toward today's 16 and go first. Clear the file after you use them.
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

## 0c. Quote/format test (batches dated 2026-11-05 through 2026-11-16 only)
- Follow `tests/quote-test-2026-11/README.md` and `plan.json` for the batch date. Of the day's 16 feed slots, 4 are test posts (cells A-D); the other 12 are regular. Stories and TOBIs are unchanged.
- Test posts have NO caption and NO first comment (empty strings in batch.json; build_csv.py writes empty cells). Alt text and AI-content setting as for any image post.
- Cells B and D are plain cards: `python3 tools/make_card.py out.png "<quote>"` (or `--batch`), then `python3 tools/stamp.py --brand WineWimsey out.png` (no `--ai`). No image generation credits needed. The tool sets the punchline apart after a blank gap (last sentence of a multi-sentence quote); do not change the quote wording to force it. Cells A and C use the normal character image.
- Ids: `qt-YYYYMMDD-A` ... `-D`. Mark the template field "TEST A/B/C/D" so the review page shows which is which.
- Reject of a test post: replace it with another quote for the SAME cell (unused inbox item first for A/B, a new short inward two-beat quote for C/D); keep the cell and slot.
- After upload, append the scheduled time of each test post to `tests/quote-test-2026-11/log.csv`. Do not change anything else about the posts during the test.

## 0d. Seasonal posts (added 2026-11-04, Scott; batches dated 2026-11-05 on)
- Why: the best Wine Wimsey posts of Nov 1-3 were all timely (clocks back, dark by 4:30, pajamas at 6:30). Scott wants to lean into seasonal content through Thanksgiving and Christmas.
- Count: 6 of the 12 regular feed posts a day are seasonal (raised from 4 on 2026-11-04, Scott: "make a few more"; not test posts, not TOBIs), plus 1 of the 4 stories. The rest stay evergreen. Curated seasonal items from Scott's inbox count toward the 6 and go first.
- Seasonal quotes must make sense on their PUBLISH date (posts go out a day or two after the batch date). Same rules as everything: new quotes only, no engagement bait, no brand names, no weekday references that will be wrong on the publish day (flag per Scott's standing rule).
- Calendar (2026):
  - Through Nov 25: early dark, cold, sweaters, thermostat, holiday-prep dread; Thanksgiving planning (hosting, who brings what, the good dishes, grocery store before the holiday).
  - Nov 24-26: Thanksgiving itself (cooking, the kids' table, nap after dinner). Thanksgiving is Thu Nov 26.
  - Nov 27-30: leftovers, Black Friday avoidance, recovery.
  - Dec 1-24: Christmas (tangled lights, cards, wrapping, shopping, cookies, relatives arriving, hiding gifts, the one box of ornaments).
  - Dec 25-31: the day itself, returns and leftovers, being asleep before midnight on New Year's Eve.
- Do not use seasonal posts for test cells A and B (see tests/quote-test-2026-11/README.md): cells A/B take the 4th and 11th NON-seasonal image quotes, so seasonality can't confound the test. Cells C and D are evergreen by design.

**TOBIs are dropped (2026-11-04, Scott): all 16 feed posts are image posts; ignore every TOBI count/alternation rule below. A held TOBI is converted to an image post or dropped.**

## 1. Write the day
- 16 feed posts total = held posts + new ones (changed from 12 by Scott, 2026-10-28). TOBIs count toward the 16; the rest are image posts. TOBI count alternates (Scott, 2026-10-28): in an EVEN ISO week (week of Oct 26 2026 = week 44) Mon/Wed/Fri/Sun get 2 TOBIs and Tue/Thu/Sat get 1; in an ODD ISO week it is switched (Tue/Thu/Sat get 2, Mon/Wed/Fri/Sun get 1).
- 4 stories (image only, own quotes).
- Characters (Scott, 2026-11-04): The Hot Mess is the default for character images. Use The Homebody whenever the quote fits her, with NO cap (Scott, 2026-11-04: she was the strongest character in his Oct posts, median views about 2x Hot Mess). Fits = staying in, couch, pajamas, TV, snacks, early bedtime, cancelling plans, cozy or lazy, plus the quiet-life quotes: coffee and the bird feeder, baking, gardening, reading, puttering, choosing a quiet night over going out, enjoying her own company. Never force her onto chaos, aging-body or errand jokes. Record the character in batch.json as usual so the Nov 23 read-out can compare Homebody vs Hot Mess. An inbox note naming a character or template overrides this.
- Mix templates per the skill (I2 is the primary format). Do NOT use Template B (photoreal) or Template C (vintage B&W photo) with people; if you want those looks, make them people-free (still life, empty porch) or draw the people as illustration. Template D still life is fine (AI label).
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
  - AI content + alt text (PIPELINE.md): after each bucket upload, reload that bucket's page, take one screenshot (the list doesn't draw while the pane is hidden), paste `tools/pp_post_options.js` into javascript_tool, run `__pp.start(<output of python3 tools/alt_jobs.py batch.json approved.txt feed>)` and poll `({prog: window.__prog, res: window.__res})` about every 30 s until `res` is not null (a run takes 30-60 s per post, longer than javascript_tool's timeout, so never await it directly) (stories bucket: `stories`). All results must be ok:true (the helper retries each failure once by itself; stories are re-found by their new image URL after the save); if one still fails, tell Scott which post.
  - Spot-check in the bucket (search a caption) that images, first comments, AI content and alt text landed. Reset viewport.

## 4b. Upload step: slot times and slot order (added 2026-11-08, Scott)
- Scott sets the Post Planner time slots himself (10 feed + 4 story slots a day, each slot at a different time). BEFORE building the CSVs, open Post Planner (built-in browser) and read the time currently set for every open slot on each day being uploaded (Wine Wimsy and Wine Wimsy Stories buckets). Tell Scott the list, save it in tests/volume-format-2026-11/slot-times.md (date, slot number, time), and re-read the times after each upload and report any change. The CSV posting-time column stays blank so posts fill the open slots in order.
- After each upload check that plain cards and character posts sit in the slots the batch expects (odd batch date: plain at 1,3,5,7,9; even: 2,4,6,8,10). Stories have no format order.
- If any post lands in the wrong slot, fix it in Post Planner by swapping scheduled times or moving posts within the same day (never across days, never delete or recreate posts). Only do this to restore the plain/character order. Tell Scott which posts are out of place and the planned swap before changing anything, then re-read that day's 10 feed times and confirm the final order. If a fix fails twice, stop and tell Scott rather than trying other things.
- Log the FINAL scheduled times (after any swaps) in tests/volume-format-2026-11/log.csv, not the original ones.
