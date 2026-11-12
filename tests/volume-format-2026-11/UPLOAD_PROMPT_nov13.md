Upload the approved Wine Wimsey batch 2026-11-13 (posts Fri Nov 13) to Post Planner. I'm at my desktop with Post Planner signed in. Repo: woodspan1967/post-images (attach with push access, clone it, git pull --rebase). Read RUN_WINE_WIMSEY.md sections 4 and 4b and PIPELINE.md, and follow them. Use the built-in browser, viewport 1280x800.

APPROVALS: the review page is fully approved (14 of 14): https://claude.ai/artifact/5gcgNwBLXw1QVkj2R6XD89. Read its `decisions` collection (ArtifactData) and write the approved ids to approved.txt. If any item is not approved, leave it out and tell me.

STEP 1, read and check the calendar BEFORE building anything:
- In Post Planner open bucket "Wine Wimsy" and "Wine Wimsy Stories". For Fri Nov 13, read the time set for every slot (10 feed + 4 story slots; I set each feed slot at a different time). Show me the full list and save it to tests/volume-format-2026-11/slot-times.md (date, slot number, time).
- Check that all 14 Nov 13 slots are EMPTY. If anything is already sitting in a Nov 13 slot, or any slot is missing, tell me what you see and wait. Do not delete anything yourself.
- Check no post from this batch is already in Post Planner (search a quote) so nothing gets doubled.

STEP 2, build and upload:
- `python3 tools/build_csv.py batches/wine-wimsey/2026-11-13/batch.json approved.txt <scratch>/csv-2026-11-13`. Leave the POSTING TIME column blank. Feed posts have no caption and no first comment (that is intended). Check the row counts: 10 feed + 4 stories.
- Create multiple posts, bucket "Wine Wimsy", inject the feed CSV, confirm the count of 10 with me, upload. Then bucket "Wine Wimsy Stories" with the stories CSV (4).
- After each bucket upload: set AI content and alt text with tools/pp_post_options.js + tools/alt_jobs.py exactly as RUN_WINE_WIMSEY.md section 4 describes (feed, then stories). Everything must be ok:true; tell me about any failure.

STEP 3, check date and slot order:
- All 10 feed posts + 4 stories must sit on Fri Nov 13, nothing spilling into another day.
- Slot order: Nov 13 is an ODD day, so plain cards (template PLAIN) at feed slots 1,3,5,7,9 and character posts (template CHAR) at 2,4,6,8,10. Match each post to its position using batch.json ids (ww-20261113-01 is position 1, and so on).
- If any post is in the wrong slot, tell me which posts and the swap you plan BEFORE changing anything. Then fix it by swapping scheduled times or moving posts within the SAME day only. Never move across days, never delete or recreate posts. Re-read that day's 10 feed times and confirm the final order. If a fix fails twice, stop and tell me.
- Spot-check in the bucket that images, AI content and alt text landed.

STEP 4, record:
- Append one row per feed post and story to tests/volume-format-2026-11/log.csv (date, position, format, character, quote_id, src, scheduled_time) using the FINAL scheduled times after any swaps (stories use position s1 to s4 with format "story", as in the existing rows). Update slot-times.md if the times changed.
- git pull --rebase, commit, push to main.
- Send me a short summary (counts, any swaps made, any failures) by email and a push notification.

Do not run or touch the nightly batch. Do not spend ElevenLabs credits in this chat.
