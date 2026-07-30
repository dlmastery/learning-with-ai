/**
 * Demo page test — every demo renders, runs, and fits.
 *
 * Four configurations per page: 390px and 1400px, light and dark. A page fails
 * if it throws, logs a console error, scrolls horizontally, or has lost its
 * stylesheet link.
 *
 * The horizontal-scroll check is not cosmetic. It has caught a table with a
 * min-width outside its scroll box, a chip holding a sentence with nowrap on
 * it, and an SVG rect rendered at NaN — each of which reached the published
 * site because the check was not being run.
 *
 *   npx playwright install chromium     # once
 *   node evidence/test-demos.mjs        # exits non-zero on failure
 */
import { readdirSync, readFileSync } from 'fs';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

let chromium;
try {
  ({ chromium } = await import('playwright'));
} catch {
  console.error('playwright is not installed. Run:\n' +
                '  npm i -D playwright && npx playwright install chromium');
  process.exit(2);
}

const dir = join(dirname(fileURLToPath(import.meta.url)), '..', 'docs', 'demos');
// index.html is the gallery, not a demo — it carries no evidence chip.
const pages = readdirSync(dir).filter(f => f.endsWith('.html') && f !== 'index.html').sort();
if (!pages.length) { console.error('no demo pages found — refusing to pass'); process.exit(2); }

const CONFIGS = [
  ['390 light',  390, 844, 'light'], ['390 dark',  390, 844, 'dark'],
  ['1400 light', 1400, 900, 'light'], ['1400 dark', 1400, 900, 'dark'],
];

const b = await chromium.launch();
let fail = 0;

for (const f of pages) {
  const bad = [];
  // Three published pages carried tool-call residue after </html>. Browsers ignore
  // it and every render test passed, so nothing caught it.
  const src = readFileSync(join(dir, f), 'utf8');
  const tail = src.slice(src.lastIndexOf('</html>') + 7).trim();
  if (!src.includes('</html>')) bad.push('no closing </html>');
  else if (tail) bad.push(`${tail.length} chars after </html>: ${tail.slice(0, 40).replace(/\s+/g, ' ')}`);
  for (const [name, width, height, colorScheme] of CONFIGS) {
    const ctx = await b.newContext({ viewport: { width, height }, colorScheme });
    const p = await ctx.newPage();
    const errs = [];
    p.on('pageerror', e => errs.push(String(e).slice(0, 110)));
    p.on('console', m => { if (m.type() === 'error') errs.push(m.text().slice(0, 110)); });
    await p.goto('file://' + join(dir, f), { waitUntil: 'networkidle' });
    await p.waitForTimeout(350);
    const r = await p.evaluate(() => ({
      over: document.documentElement.scrollWidth - document.documentElement.clientWidth,
      css: !!document.querySelector('link[href="demo.css"]'),
      chip: !!document.querySelector('.chip'),
    }));
    if (r.over > 1) bad.push(`${name} H-SCROLL +${r.over}px`);
    if (!r.css) bad.push(`${name} NO-CSS`);
    if (!r.chip) bad.push(`${name} no evidence chip`);
    if (errs.length) bad.push(`${name} ${errs[0]}`);
    await ctx.close();
  }
  if (bad.length) fail++;
  console.log(`${bad.length ? 'FAIL' : 'ok  '} ${f.padEnd(26)} ${bad.join(' · ')}`);
}

await b.close();
console.log(fail
  ? `\n${fail} of ${pages.length} demo pages FAILED`
  : `\nall ${pages.length} demo pages pass — ${CONFIGS.length} configurations each`);
process.exit(fail ? 1 : 0);
