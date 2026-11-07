// Post Planner post options helper: AI content + alt text, set per post after a bulk upload.
// The bulk spreadsheet (v3.1) has no columns for these, so they are set in each post's editor.
//
// Use in the built-in browser on the bucket page (https://app.postplanner.com/posts/buckets/<id>/posts),
// viewport 1280x800. Reload the bucket page and take ONE screenshot first: while the browser pane is
// hidden the post list doesn't draw its rows until a screenshot is taken. Then paste this whole file into javascript_tool once per page load, then:
//   __pp.start([{search: "<distinctive caption words>", caption: "<caption start>", alt: "<alt text>"}, ...])
//   then poll ({prog: window.__prog, res: window.__res}) every ~30 s until res is not null. (A run takes
//   30-60 s per post, longer than javascript_tool's timeout, so don't await __pp.run(...) directly.)
//   stories (no caption): {image: "<image file name, e.g. wys-20261017-1.png>", alt: "..."}
// run() searches the bucket for each post (the list only draws rows on screen, so search is how we
// reach a post), opens Edit Post, switches AI content ON and Add alt text ON, fills the alt text box,
// clicks Finish editing, then reopens the post and reads the settings back. Every result line must
// say ok:true. TOBIs have no media and no POST OPTIONS section, so they are never passed in.
window.__pp = {
  sleep: ms => new Promise(r => setTimeout(r, ms)),
  async search(q) {
    const inp = document.querySelector('input[type=search]'); if (!inp) return false;
    Object.getOwnPropertyDescriptor(HTMLInputElement.prototype, 'value').set.call(inp, q || '');
    inp.dispatchEvent(new Event('input', { bubbles: true }));
    for (const t of ['keydown', 'keyup']) inp.dispatchEvent(new KeyboardEvent(t, { key: 'Enter', code: 'Enter', keyCode: 13, which: 13, bubbles: true }));
    await this.sleep(2500); return true;
  },
  scrollers() {
    return [document.scrollingElement, ...document.querySelectorAll('main, main *')]
      .filter(e => e.scrollHeight > e.clientHeight + 100).slice(0, 4);
  },
  async findRow(match) {
    const els = this.scrollers();
    els.forEach(e => e.scrollTop = 0); await this.sleep(400);
    for (let i = 0; i < 40; i++) {
      const hit = match();
      if (hit) {
        // Smallest ancestor that has a More button and holds at most one post image. Counting buttons
        // is not enough: story rows have only 2 buttons, so the climb overshot to an ancestor holding
        // every row and the first row's More button got clicked for every story (fixed 2026-10-29).
        const media = el => [...el.querySelectorAll('img')].filter(i => /^https?:/.test(i.src) && !/icons|\.svg/.test(i.src)).length;
        let row = hit;
        for (let j = 0; j < 14 && row; j++) {
          row = row.parentElement;
          if (row && media(row) <= 1 && [...row.querySelectorAll('button')].some(b => /More/.test(b.outerHTML))) break;
        }
        return row;
      }
      els.forEach(e => e.scrollTop += 500); await this.sleep(250);
    }
    return null;
  },
  matcher(p) {
    return p.image
      ? () => [...document.querySelectorAll('main img')].find(i => i.src.includes(p.image))
      : () => [...document.querySelectorAll('main *')].find(e => e.children.length === 0 && e.textContent.startsWith(p.caption));
  },
  async open(p) {
    if (p.search !== undefined) await this.search(p.search);
    const row = await this.findRow(this.matcher(p));
    if (!row) return 'post not found';
    const more = [...row.querySelectorAll('button')].find(b => /More/.test(b.outerHTML));
    if (!more) return 'no More button';
    more.click(); await this.sleep(700);
    const edit = [...document.querySelectorAll('[role=menuitem]')].find(e => e.innerText.trim() === 'Edit Post');
    if (!edit) return 'no Edit Post item';
    edit.click();
    for (let i = 0; i < 25; i++) { await this.sleep(300); const d = document.querySelector('[role=dialog]'); if (d && /POST OPTIONS/.test(d.innerText)) return 'open'; }
    if (document.querySelector('[role=dialog]')) await this.close(false);
    return 'no POST OPTIONS (TOBI or text post?)';
  },
  toggle(label) {
    const d = document.querySelector('[role=dialog]'); if (!d) return null;
    return [...d.querySelectorAll('input[type=checkbox]')].find(c => {
      let p = c; for (let i = 0; i < 6; i++) { p = p.parentElement; if (p && p.innerText.trim().startsWith(label)) return true; } return false;
    });
  },
  state() {
    const d = document.querySelector('[role=dialog]'); if (!d) return null;
    const ta = d.querySelector('[aria-label="Alt text"]');
    return { ai: this.toggle('AI content')?.checked, altOn: this.toggle('Add alt text')?.checked, alt: ta ? ta.value : '' };
  },
  async apply(alt) {
    const ai = this.toggle('AI content');
    if (ai && !ai.checked) { ai.click(); await this.sleep(400); }
    const sw = this.toggle('Add alt text');
    if (sw && !sw.checked) { sw.click(); await this.sleep(700); }
    const ta = document.querySelector('[role=dialog] [aria-label="Alt text"]');
    if (!ta) return 'no alt text box';
    const proto = ta.tagName === 'TEXTAREA' ? HTMLTextAreaElement.prototype : HTMLInputElement.prototype;
    Object.getOwnPropertyDescriptor(proto, 'value').set.call(ta, alt.slice(0, 500));
    ta.dispatchEvent(new Event('input', { bubbles: true }));
    ta.dispatchEvent(new Event('change', { bubbles: true }));
    await this.sleep(400);
    return this.state();
  },
  async close(save) {
    const d = document.querySelector('[role=dialog]'); if (!d) return 'no dialog';
    [...d.querySelectorAll('button')].find(b => b.innerText.trim() === (save ? 'Finish editing' : 'Close')).click();
    for (let i = 0; i < 25; i++) { await this.sleep(300); if (!document.querySelector('[role=dialog]')) return save ? 'saved' : 'closed'; }
    return 'still open';
  },
  // Every post-image URL currently drawn or scrolled past in the list (the list only draws rows on screen,
  // so scroll through it). Used to spot a story's new image URL after a save (see one()).
  async scanSrcs() {
    const els = this.scrollers(); els.forEach(e => e.scrollTop = 0); await this.sleep(400);
    const seen = new Set();
    for (let i = 0; i < 40; i++) {
      document.querySelectorAll('main img').forEach(im => { if (/^https?:/.test(im.src) && !/icons|\.svg|graph\.facebook/.test(im.src)) seen.add(im.src); });
      const before = els.map(e => e.scrollTop);
      els.forEach(e => e.scrollTop += 400); await this.sleep(250);
      if (els.every((e, k) => e.scrollTop === before[k])) break;
    }
    els.forEach(e => e.scrollTop = 0);
    return [...seen];
  },
  async one(p) {
    const label = p.image || p.caption.slice(0, 30);
    // Stories have no caption and are found by image file name. Post Planner re-hosts a story's image under
    // a new file name when the edit is saved (seen 2026-11-06 and 2026-11-07), so the file name no longer
    // matches on the recheck. Fix: remember every image URL before saving, then find the one new URL after.
    const before = p.image ? await this.scanSrcs() : null;
    let o = await this.open(p); if (o !== 'open') return { post: label, ok: false, error: o };
    const st = await this.apply(p.alt);
    if (typeof st === 'string') { await this.close(false); return { post: label, ok: false, error: st }; }
    const saved = await this.close(true); if (saved !== 'saved') return { post: label, ok: false, error: 'save: ' + saved };
    await this.sleep(1500);
    let q = p;
    if (before) {
      const fresh = (await this.scanSrcs()).filter(s => !before.includes(s));
      // Keep the new URL on the job too, so a retry of this post (see run()) can still find it.
      if (fresh.length === 1) { q = { ...p, image: fresh[0] }; p.image = fresh[0]; }
      else if (fresh.length > 1) return { post: label, ok: false, error: 'recheck: ' + fresh.length + ' new image URLs, cannot tell which is this post' };
    }
    o = await this.open(q); if (o !== 'open') return { post: label, ok: false, error: 'recheck: ' + o };
    const back = this.state(); await this.close(false);
    const ok = back.ai === true && back.altOn === true && back.alt === p.alt.slice(0, 500);
    return { post: label, ok, ai: back.ai, altOn: back.altOn, altSaved: back.alt === p.alt.slice(0, 500) };
  },
  // Runs every item, then retries each failure once (the runbook rule). A failed first pass is usually the
  // list not drawing yet or a slow save; the settings are idempotent, so a retry is safe.
  async run(items) {
    const out = [];
    for (const p of items) { out.push(await this.one(p)); window.__prog = out.length; }
    for (let i = 0; i < out.length; i++) {
      if (out[i].ok) continue;
      const first = out[i].error;
      await this.search('');
      out[i] = await this.one(items[i]); out[i].retried = true; out[i].firstError = first;
    }
    await this.search('');
    return out;
  },
  // Use this from javascript_tool instead of awaiting run(): a run takes about 30-60 s per post, longer than
  // the tool's timeout. start() returns at once; poll `({prog: window.__prog, res: window.__res})` until
  // window.__res is not null (an array of per-post results, or {error}).
  start(items) {
    window.__res = null; window.__prog = 0;
    this.run(items).then(r => window.__res = r).catch(e => window.__res = { error: String(e) });
    return 'started ' + items.length;
  }
};
'__pp ready';
