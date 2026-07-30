/* Render check for docs/index.html and docs/deck.html — the pattern in
   evidence/test-demos.mjs: 390px and 1400px, light and dark, no console error,
   no horizontal scroll. Plus: the deck must advance through every slide. */
import { chromium } from 'playwright';
import { join } from 'path';

const docs = '/home/eranti/learning-with-ai/docs';
const CONFIGS = [
  ['390 light', 390, 844, 'light'], ['390 dark', 390, 844, 'dark'],
  ['1400 light', 1400, 900, 'light'], ['1400 dark', 1400, 900, 'dark'],
];

const b = await chromium.launch();
let fail = 0;

for (const f of ['index.html', 'deck.html']) {
  const bad = [];
  for (const [name, width, height, colorScheme] of CONFIGS) {
    const ctx = await b.newContext({ viewport: { width, height }, colorScheme });
    const p = await ctx.newPage();
    const errs = [];
    p.on('pageerror', e => errs.push(String(e).slice(0, 140)));
    p.on('console', m => { if (m.type() === 'error') errs.push(m.text().slice(0, 140)); });
    await p.goto('file://' + join(docs, f), { waitUntil: 'networkidle' });
    await p.waitForTimeout(400);
    const r = await p.evaluate(() => ({
      over: document.documentElement.scrollWidth - document.documentElement.clientWidth,
      css: !!document.querySelector('link[href="site.css"]') || !!document.querySelector('style'),
      gen: document.querySelectorAll('[data-gen]').length,
      qh4: document.querySelectorAll('.q > h4').length,
      qb: document.querySelectorAll('.q > b').length,
    }));
    if (r.over > 1) bad.push(`${name} H-SCROLL +${r.over}px`);
    if (!r.css) bad.push(`${name} NO-CSS`);
    if (errs.length) bad.push(`${name} ${errs[0]}`);
    if (f === 'index.html' && name === '1400 light') {
      console.log(`     data-gen spans: ${r.gen}, .q > h4: ${r.qh4}, leftover .q > b: ${r.qb}`);
    }
    if (f === 'deck.html' && name === '1400 light') {
      const n = await p.evaluate(() => document.querySelectorAll('.slide').length);
      const seen = [];
      for (let i = 1; i < n; i++) {
        await p.click('#next');
        await p.waitForTimeout(500);
        seen.push(await p.evaluate(() => document.getElementById('pos').textContent));
      }
      const last = seen[seen.length - 1];
      console.log(`     deck advance: ${n} slides, forward path → ${seen.join(' ')}`);
      if (last !== `${n} / ${n}`) bad.push(`deck did not reach slide ${n} (ended ${last})`);
      const backs = [];
      for (let i = 0; i < n - 1; i++) {
        await p.click('#prev');
        await p.waitForTimeout(500);
        backs.push(await p.evaluate(() => document.getElementById('pos').textContent));
      }
      if (backs[backs.length - 1] !== `1 / ${n}`) bad.push(`deck did not return to slide 1 (ended ${backs[backs.length - 1]})`);
      console.log(`     deck reverse: back to ${backs[backs.length - 1]}`);
    }
    await ctx.close();
  }
  if (bad.length) fail++;
  console.log(`${bad.length ? 'FAIL' : 'ok  '} ${f.padEnd(12)} ${bad.join(' · ')}`);
}

await b.close();
console.log(fail ? `\n${fail} page(s) FAILED` : `\nboth pages pass — ${CONFIGS.length} configurations each`);
process.exit(fail ? 1 : 0);
