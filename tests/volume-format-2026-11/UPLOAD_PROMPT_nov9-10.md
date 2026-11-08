Upload the two approved Wine Wimsey batches to Post Planner: batch 2026-11-09 (posts Mon Nov 9) first, then batch 2026-11-10 (posts Tue Nov 10). I'm at my desktop with Post Planner signed in. Repo: woodspan1967/post-images (attach with push access, clone it, git pull --rebase). Read RUN_WINE_WIMSEY.md sections 4 and 4b and PIPELINE.md, and follow them. Use the built-in browser, viewport 1280x800.

APPROVALS: both review pages are fully approved (14 of 14 each). Nov 9: https://claude.ai/artifact/3VcAkvKZttQwkw1v4jLxSp. Nov 10: https://claude.ai/artifact/5JmV9KSeAuAp3JVsb2d9fv. Read each page's `decisions` collection (ArtifactData) and write the approved ids to approved.txt. If any item is not approved, leave it out and tell me.

STEP 1, read and clean the calendar BEFORE building anything:
- In Post Planner open bucket "Wine Wimsy" and "Wine Wimsy Stories". For Mon Nov 9 and Tue Nov 10, read the time set for every slot (10 feed + 4 story slots per day; I set each feed slot at a different time, story times repeat). Show me the full list and save it to tests/volume-format-2026-11/slot-times.md (date, slot number, time).
- Check that all 14 slots on each of those two days are EMPTY. I deleted the old run's posts for Nov 9; if anything is still sitting in a Nov 9 or Nov 10 slot, or any slot is missing, tell me what you see and wait. Do not delete anything yourself.
- Check no post from these batches is already in Post Planner (search a caption/quote) so nothing gets doubled.

STEP 2, build and upload (Nov 9 first, then Nov 10, so each fills its own day's open slots in order):
- `python3 tools/build_csv.py batches/wine-wimsey/<date>/batch.json approved.txt <scratch>/csv-<date>`. Leave the POSTING TIME column blank. Feed posts have no caption and no first comment (that is intended). Check the row counts: 10 feed + 4 stories per batch.
- Create multiple posts, bucket "Wine Wimsy", inject the feed CSV, confirm the count of 10 with me, upload. Then bucket "Wine Wimsy Stories" with the stories CSV (4).
- After each bucket upload: set AI content and alt text with tools/pp_post_options.js + tools/alt_jobs.py exactly as RUN_WINE_WIMSEY.md section 4 describes (feed, then stories). Everything must be ok:true; tell me about any failure.
- Do Nov 9 fully (feed, stories, alt text) before starting Nov 10.

STEP 3, check dates and slot order for each day:
- Every post must sit on its own day: all 10 Nov 9 feed posts + 4 stories on Mon Nov 9, all Nov 10 posts on Tue Nov 10. Nothing spilling into another day.
- Slot order: Nov 9 (odd) plain cards at feed slots 1,3,5,7,9 and character posts at 2,4,6,8,10. Nov 10 (even) plain cards at 2,4,6,8,10 and character posts at 1,3,5,7,9. Match each post to its position using batch.json ids (template PLAIN or CHAR).
- If any post is in the wrong slot, tell me which posts and the swap you plan BEFORE changing anything. Then fix it by swapping scheduled times or moving posts within the SAME day only. Never move across days, never delete or recreate posts. Re-read that day's 10 feed times and confirm the final order. If a fix fails twice, stop and tell me.
- Spot-check in the bucket that images, AI content and alt text landed.

STEP 4, record:
- Append one row per feed post and story to tests/volume-format-2026-11/log.csv (date, position, format, character, quote_id, src, scheduled_time) using the FINAL scheduled times after any swaps. Update slot-times.md if the times changed.
- git pull --rebase, commit, push to main.
- Send me a short summary (counts per day, any swaps made, any failures) by email and a push notification.

Do not run or touch tomorrow's nightly batch. Do not spend ElevenLabs credits in this chat.
