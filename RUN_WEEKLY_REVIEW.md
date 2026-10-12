# Weekly performance review (runbook)

Runs Mondays about 6 AM Central. Pages: Wine Wimsey, Whispers Of Yesterday, Horse Soup.
What counts: **reach and earnings**, weighed together. Scott exports the data himself; never sign in to
Facebook or Meta Business Suite, and never drive any Facebook page in a browser (his accounts are under
restriction and automated access is a risk). This run needs no browser at all.

Data privacy: reach and earnings never go in this repo (it is public). They live only in the private
dashboard and the private drop page.

## 0. Setup
- Clone/pull this repo (woodspan1967/post-images). Read PIPELINE.md and this file.
- Drop page (Scott uploads exports here): https://claude.ai/artifact/2s9ytPX14C65UGFPGVhL3X
- Dashboard (the report): URL is in the `Dashboard` line at the bottom of this file. If that line has no URL yet,
  create the dashboard from the Dashboard artifact type (title "Page Performance"), with datasets `posts` and
  `findings` built in steps 2-5, then write its URL into that line and push.

## 1. Collect the exports
- ArtifactData list collection `exports` on the drop page. Each doc: page, assetId, filename, status (new|analyzed), createdAt.
- Use every doc with status `new`. If a page has none, the report says that page's numbers are missing this week.
- If there are no new exports at all: SendUserMessage Scott a one-line reminder with the drop page link
  ("No exports this week yet. Drop them in and reply go."), then stop and wait. On "go", start from step 1.
- Download each: Artifact read, url = drop page, path = assetId (saves the CSV locally).

## 2. Build the table
- History: on the dashboard, ArtifactData get `datasets/posts`; its `source.url` is `/_blob/<id>`. Download it with
  Artifact read, url = dashboard, path = <id>. That file is every post analyzed so far.
- `python3 tools/insights.py <scratch>/posts.csv "Wine Wimsey=<csv>" "Whispers Of Yesterday=<csv>" "Horse Soup=<csv>" --history <old posts.csv>`
  (only the pages that have a new export). Read its printout: if it says columns are missing (earnings especially),
  say so in the report and to Scott instead of guessing.
- It matches posts to `batches/<page>/<date>/batch.json` and copies kind, template and character. Posts it can't
  match are `manual` (older posts or ones posted by hand).

## 3. Analyze (pandas, in scratch)
For each page, this week (last 7 days by publish date) against the previous 4 weeks:
- Posts, total and median reach, total earnings, earnings per 1,000 reach.
- By kind (image / TOBI), template, character, caption length (under 60 / 60-120 / over 120 words),
  weekday, and hour posted. A group needs at least 3 posts before it is called better or worse; say "too few
  to tell" otherwise. Use medians for reach (one viral post skews averages).
- Top 5 and bottom 5 posts by reach and by earnings, with the text snippet and template/character.
- Stories are not in the post export; leave them out and don't guess.

## 4. Recommendations
- At most 5, each one concrete and tied to numbers from step 3 ("Template E averaged 2.1x the reach of B on
  Wine Wimsey over 18 vs 15 posts: shift one B slot to E"). Name which runbook/skill rule it would change.
- Only things the pipeline can act on: template mix, character mix, TOBI count, caption length, themes, topics.
  Posting times come from Post Planner buckets: suggest, don't change.
- Never edit a runbook, PIPELINE.md or a skill in this run. Scott approves first (step 6).

## 5. Update the report
- Upload the new posts.csv to the dashboard (Artifact publish, url = dashboard, asset: true) and update
  `datasets/posts` (`source.url`, `source.name`, `updated: {at, by: "Weekly review"}`).
- Write findings as JSON rows `[{week, page, kind: "headline"|"recommendation"|"note", text, rule}]`, upload it the
  same way, and update `datasets/findings`. Append this week's rows to the previous findings file so the history stays.
- Follow the dashboard type's instructions (its SKILL.md) for any change to the page itself.
- On the drop page: set `meta/report` to `{url: <dashboard>, updatedAt: <ms>}`, and update each used export to
  `{status: "analyzed", analyzedIn: "<Mon D> review"}` (with its if_version).

## 6. Tell Scott, then wait
- SendUserMessage: one line per page (posts, reach, earnings, change vs the 4-week median), the recommendations
  numbered, and the dashboard link. Then stop.
- When he approves recommendations: make those edits in the RUN_*.md files and PIPELINE.md (pipeline rules
  win over skills), commit and push. Skill text itself (in his skill files) is his to change: give him the exact
  wording to paste.

Dashboard: (set during the first look-back)
