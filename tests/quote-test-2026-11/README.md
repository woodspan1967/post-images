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
- Plain card = tools/make_card.py (1080x1350, flat off-white, bold text) + `tools/stamp.py --brand WineWimsey`, no `--ai` (flat type is not photo-style). Upload as a photo post, never a native Text post.
- Cells A and B: write the day's regular image quotes as usual, then take the 4th and 11th image quotes (fixed positions, NOT chosen by merit). 4th -> A, 11th -> B. Strip their caption and first comment. Remaining regular quotes stay regular.
- Cells C and D: use that day's entry in plan.json (`C` = quote + suggested character, `D` = quote). Quotes were checked against used/wine-wimsey-quotes.txt on 2026-11-03; re-check before use, and append them to the used log.
- Slot rotation: queue positions 2, 6, 10, 14 (if a TOBI sits there, take the next image post). `slots` in plan.json says which cell takes which position each day; it rotates so no cell always gets the strong morning slots.
- Everything else stays constant for the 12 days: no videos, no new templates, no other format changes.

## Logging
After upload, read each test post's scheduled time in Post Planner and append a row to log.csv (date, cell, post_id, quote_id, scheduled_time). Test posts have no caption, so the Meta export is joined on Publish time, not on caption.

## Read-out (not before Nov 22)
Export per-post data (Meta Business Suite > Insights > Content). For each cell compare MEDIAN views, shares and reactions per post at 72 hours. Twelve posts per cell only shows large effects: treat about 2x or more as real; if all four cells are within about 30% of each other, format is not the lever. Report the medians and the top post per cell. Do not average (a single viral post skews it).

## Not in this test
Videos (phase 2, after the read-out, small and watching Page Quality).
