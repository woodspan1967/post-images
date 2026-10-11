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
- Runs cover 3 days (36 posts). TOBIs are interleaved between image posts in queue order.
- Each post: caption + first comment (5-minute delay). No second comment in bulk uploads.
- TOBI text stays under 130 characters.

## Review page
- One page per batch: approve / redo / reject per post, decisions stored in the page's database.
- Redo: regenerate using the note, put back as Waiting.
- Reject: drop it from the upload and write a fresh replacement post for that slot, added as Waiting.
- Upload only when nothing is Waiting or Redo, and only approved posts.

## Upload
- Post Planner bulk CSV (version 3.1 template), posting time blank (queue), bottom of queue, bucket chosen on the upload screen.
- Uploaded through the Claude desktop app's built-in browser; Scott confirms before the final click.
