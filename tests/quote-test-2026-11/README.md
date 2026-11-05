# Wine Wimsey quote/format test (batch dates Nov 5-16, 2026)

Question: is the Wine Wimsey reach problem the writing, the character image, or neither? Agreed with Scott 2026-11-03.

## Design
4 test posts a day for 12 batch days (48 posts, 12 per cell; 12 days = 3 full slot rotations, so every cell gets every position equally). Dates here are batch dates; a batch's posts publish a day or two later, so the last test posts go out around Nov 17-18. They REPLACE 4 of the 16 daily feed slots (12 regular posts + 4 test). Stories, TOBIs and everything else stay as they are.

| Cell | Quote | Image |
|---|---|---|
| A | usual-style quote from the day's regular output | character image (normal template) |
| B | usual-style quote from the day's regular output | plain card |
| C | new quote from plan.json (short, inward, two-beat) | character image |
| D | new quote from plan.json | plain card |

- No caption and no first comment on any test post, in all four cells. Alt text and AI-content setting follow PIPELINE.md as for every image post, identical across cells.
- Plain card = tools/make_card.py (1080x1350, flat off-white, bold text) + `tools/stamp.py --brand WineWimsey`, no `--ai` (flat type is not photo-style). Added 2026-11-04 (Scott): cards set the punchline apart with a blank-line pause. make_card.py does this automatically: a quote with two or more sentences gets a gap before its last sentence; a single-sentence quote stays one block. Do not edit quote wording to force a pause. Applies to cells B and D alike. Upload as a photo post, never a native Text post.
- Cells A and B: write the day's regular image quotes as usual, then take the 4th and 11th NON-seasonal image quotes (fixed positions, NOT chosen by merit; seasonal posts are excluded from A/B, added 2026-11-04, so seasonality can't confound the test). 4th -> A, 11th -> B. Strip their caption and first comment. Remaining regular quotes stay regular.
- Cells C and D: use that day's entry in plan.json (`C` = quote + suggested character, `D` = quote). Quotes were checked against used/wine-wimsey-quotes.txt on 2026-11-03; re-check before use, and append them to the used log.
- Slot rotation: queue positions 2, 6, 10, 14 (TOBIs were dropped 2026-11-04, so every slot is an image post). `slots` in plan.json says which cell takes which position each day; it rotates so no cell always gets the strong morning slots.
- Everything else stays constant for the 12 days: no videos, no new templates, no other format changes.

## Logging
After upload, read each test post's scheduled time in Post Planner and append a row to log.csv (date, cell, post_id, quote_id, scheduled_time). Test posts have no caption, so the Meta export is joined on Publish time, not on caption.

## Read-out (not before Nov 22)
Export per-post data (Meta Business Suite > Insights > Content). For each cell compare MEDIAN views, shares and reactions per post at 72 hours. Twelve posts per cell only shows large effects: treat about 2x or more as real; if all four cells are within about 30% of each other, format is not the lever. Also report EARNINGS (added 2026-11-04, Scott): median earnings per post and earnings per 1,000 views for each cell, because RPM differs by format (Scott's figures on 2026-11-04: TOBI about $0.11, image about $0.31, reels about $0.13 per 1,000 views). Earnings keep accumulating for days after posting, so read them no sooner than the views. Report the top post per cell. Read seasonal posts separately from the cells; do not mix them in. Note that Scott's recent top posts were curated and lightly reworded from pages where they had already done well, so the original quotes in cells C and D start without that proven-elsewhere advantage; weigh that when comparing against A/B. Do not average (a single viral post skews it).

## Not in this test
Videos (phase 2, see below).

## Earnings baseline (Scott's Earnings-rate screenshots, 28 days ending Nov 3-4, 2026)
Rates are per 1,000 QUALIFIED views (views that earn), not per total view.
| Format | Earnings (28d) | Rate per 1K qualified | Qualified views | Main non-qualified reason |
|---|---|---|---|---|
| Photos | $452.49 | $0.28 | 1,588,540 | repeat views 24%, restricted users 4% |
| Reels | $25.36 | $0.14 | 185,782 | view duration too short 46% |
| Text (TOBI) | $5.51 | $0.12 | 44,547 | repeat views 28%, restricted users 8% |
Photos rate dipped to about $0.15 around Oct 10 and has run about $0.30-0.33 since late October. At the read-out (Nov 23), ask Scott for the same three screenshots and compare to this table. Rough per-slot estimate (about 1.5 TOBIs and 14.5 image posts a day): about $0.13 per TOBI vs about $1.10 per image post.

## Phase 2 (agreed with Scott 2026-11-04)
After the read-out, bring reels back at 1-2 a week as a probe (Scott's call, given restriction history). Watch Page Quality and the reel "view duration too short" share (46% of reel views were non-qualified).
