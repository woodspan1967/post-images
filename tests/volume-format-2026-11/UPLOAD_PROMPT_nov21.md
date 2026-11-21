Upload the approved Wine Wimsey batch 2026-11-21 (posts Sat Nov 21) to Post Planner. I'm at my desktop with Post Planner signed in. Repo: woodspan1967/post-images (attach with push access, clone it, git pull --rebase). Read RUN_WINE_WIMSEY.md sections 0e, 4 and 4b and PIPELINE.md, and follow them. Use the built-in browser, viewport 1280x800.

APPROVALS: Scott has reviewed the page (7 feed + 2 stories; #1, #4 and story 1 were replaced with inbox quotes after round 1): https://claude.ai/artifact/3L8zUdagJ4GLYKnF47asHq. Read its `decisions` collection (ArtifactData) and write the approved ids to approved.txt. If any item is not approved, leave it out and tell me.

STEP 1, read and check the calendar BEFORE building anything:
- In Post Planner open bucket "Wine Wimsy" and "Wine Wimsy Stories". For Sat Nov 21, read the time set for every slot (7 feed + 2 story slots; each slot is at a different time). Show me the full list and save it to tests/volume-format-2026-11/slot-times.md (date, bucket, slot number, time).
- Check that all 9 Nov 21 slots are EMPTY. If anything is already sitting in a Nov 21 slot, or any slot is missing, tell me what you see and wait. Do not delete anything yourself.
- Check no post from this batch is already in Post Planner (search a quote) so nothing gets doubled.

STEP 2, build and upload:
- `python3 tools/build_csv.py batches/wine-wimsey/2026-11-21/batch.json approved.txt <scratch>/csv-2026-11-21`. Leave the POSTING TIME column blank. Feed posts have no caption and no first comment (that is intended). Check the row counts: 7 feed + 2 stories.
- Create multiple posts, bucket "Wine Wimsy", inject the feed CSV, confirm the count of 7 with me, upload. Then bucket "Wine Wimsy Stories" with the stories CSV (2).
- After each bucket upload: set AI content and alt text with tools/pp_post_options.js + tools/alt_jobs.py exactly as RUN_WINE_WIMSEY.md section 4 describes (feed, then stories). Everything must be ok:true; tell me about any failure.

STEP 3, check date and slot order:
- All 7 feed posts + 2 stories must sit on Sat Nov 21, nothing spilling into another day.
- Slot order: Nov 21 is an ODD day, so plain cards (template PLAIN) at feed slots 1,3,5,7 and character posts (template CHAR) at 2,4,6. Match each post to its position using batch.json ids (ww-20261118-01 is position 1, and so on).
- If any post is in the wrong slot, tell me which posts and the swap you plan BEFORE changing anything. Then fix it by swapping scheduled times or moving posts within the SAME day only. Never move across days, never delete or recreate posts. Re-read that day's 7 feed times and confirm the final order. If a fix fails twice, stop and tell me.
- Spot-check in the bucket that images, AI content and alt text landed.

STEP 4, record:
- Append one row per feed post and story to tests/volume-format-2026-11/log.csv (date, position, format, character, quote_id, src, scheduled_time) using the FINAL scheduled times after any swaps (stories use position s1 and s2 with format "story", as in the existing rows). Update slot-times.md if the times changed. Row data (src/character) is in batch.json.
- git pull --rebase, commit, push to main.
- Send me a short summary (counts, any swaps made, any failures) by email and a push notification.

Do not run or touch the nightly batch. Do not spend ElevenLabs credits in this chat.
