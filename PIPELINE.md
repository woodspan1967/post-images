# Post pipeline rules

Standing rules for generating, reviewing, and uploading posts. Agreed with Scott on 2026-10-11.

## Images
- Engine: ElevenLabs, model GPT Image 2.5 (`gpt-image-2.5-sunburst`), 1K, low quality, 4:5.
- Prompts never ask the model for a watermark; they ask for plain bottom corners and no extra signs, logos, or text.
- After generation, `tools/stamp.py` adds:
  - `--brand <PageName>` watermark, bottom-right (every image except vintage-poster templates that carry an in-scene signature).
  - `--ai` faint "AI-generated" label, bottom-left, on every photo-style image (photoreal, vintage photo, still life). Cartoons don't get it.
- Images are copied here by the Fetch images workflow (drop a `queue/*.txt` list of `path url` lines) for permanent links.

## Wine Wimsey
- Bucket: Wine Wimsy. 12 posts a day total: 1-2 of them TOBIs (vary), the rest image posts (so 11+1 or 10+2). TOBI background `black`.
- Daily run at about 6 AM Central covers one day (12 posts + 4 stories). Scott asks for multi-day runs when he needs them. See RUN_WINE_WIMSEY.md. TOBIs are interleaved between image posts in queue order.
- Each post: caption + first comment (5-minute delay). No second comment in bulk uploads.
- TOBI text stays under 130 characters.
- Stories: 4 a day into the Wine Wimsy Stories bucket (12 per 3-day run). One image per story, same templates, characters, size (4:5) and stamping as feed images, but their own quotes (never a feed quote). No caption or comment. Uploaded as a second CSV with REEL OR STORY set to `story` (confirmed working 2026-10-11).
- Stories appear in their own section on the same review page and follow the same approve / redo / reject rules.

## Whispers Of Yesterday
- Buckets: Whispers Of Yesterday (feed) and Whispers Of Yesterday Stories. Daily run at about 6:15 AM Central, one day. See RUN_WHISPERS_OF_YESTERDAY.md.
- 10 feed posts a day: 1-2 TOBIs (vary), the rest image posts (9+1 or 8+2). TOBI background `black`, text under 130 characters.
- 3 stories a day, own quotes, image only, same templates/size/stamping as feed images.
- Captions and first comments follow the Whispers skill (story caption 4-8 sentences; first comment 2-4 sentences + 5-8 hashtags). 5-minute first-comment delay, no second comment.
- Stamping: `--brand "Whispers Of Yesterday"` on every image; `--ai` on every image that looks real (T1 photoreal scenes, T2 vintage photos); flat retro posters (T3) brand only. Prompts are 4:5 and never include the skill's watermark sentence.
- Inbox: https://claude.ai/artifact/ELPgE7UJER5X8nkBwC74ch (separate from Wine Wimsey's). Same rules as the Wine Wimsey inbox below.

## Horse Soup
- Buckets: Horse Soup (feed) and Horse Soup Stories. Daily run at about 6:20 AM Central, one day. See RUN_HORSE_SOUP.md.
- 6 feed posts a day: 5 image posts + 1 TOBI. TOBI background `black`, text under 130 characters.
- 2 stories a day, own quotes, image only, same templates/size/stamping as feed images.
- Captions and first comments follow the Horse Soup skill (SEE MORE caption ~100 words; first comment ~50 words, no hashtags). 5-minute first-comment delay. The skill's second comment is not used.
- All images 4:5, including the skill's square templates (W, H), re-composed for the taller frame. Prompts never include the skill's 'HorseSoup' footer sentence.
- Prompt ending allows the skill's 2-4 word wall signs: "The only text in the image is the [bubble/banner/lettered] text[ and the small wall sign]. Keep the bottom corners plain. Vertical 4:5 format."
- No TOBI caption and no second comment (no slot in bulk upload). TOBI = quote under 130 characters + first comment.
- Skill/pipeline differences settled with Scott on 2026-10-11.
- Stamping: `--brand "Horse Soup"` on every image. Every Horse Soup image is a cartoon, so no `--ai` label.
- Meme posts only. Reels (Meta AI video + voiceover) stay a manual, on-request workflow.
- Inbox: https://claude.ai/artifact/4WXju43mLVkJfK1CLEwp7v (separate from the other pages'). Same rules as the Wine Wimsey inbox below.

## Inbox
- Scott drops quotes/images into the Wine Wimsey Inbox page (https://claude.ai/artifact/Fxf3RdrmK5pmoH3bfJzVwD). The daily run uses new items first, word-for-word quotes, and marks them used.

## Review page
- One page per batch: approve / redo / reject per post, decisions stored in the page's database.
- Redo: regenerate using the note, put back as Waiting.
- Reject: drop it from the upload and write a fresh replacement post for that slot, added as Waiting.
- Upload only when nothing is Waiting or Redo, and only approved posts.

## Upload
- Post Planner bulk CSV (version 3.1 template), posting time blank (queue), bottom of queue, bucket chosen on the upload screen.
- Uploaded through the Claude desktop app's built-in browser; Scott confirms before the final click.

## Weekly performance review
- Mondays about 6 AM Central, pages on this pipeline only. See RUN_WEEKLY_REVIEW.md.
- Scott exports post insights from Meta Business Suite himself and drops them on https://claude.ai/artifact/2s9ytPX14C65UGFPGVhL3X . Never automate anything on Facebook or Meta Business Suite.
- Measures reach and earnings. Reach/earnings data stays out of this repo (public); it lives in the private dashboard.
- Recommendations are proposals; runbooks change only after Scott approves.
