import { readFileSync } from 'fs';
import { chromium } from 'playwright';
const F = '/home/eranti/learning-with-ai/docs/index.html';
const CONFIGS = [['390 light',390,844,'light'],['390 dark',390,844,'dark'],
                 ['1400 light',1400,900,'light'],['1400 dark',1400,900,'dark']];
const src = readFileSync(F,'utf8');
const bad = [];
const tail = src.slice(src.lastIndexOf('</html>')+7).trim();
if (!src.includes('</html>')) bad.push('no closing </html>');
else if (tail) bad.push(`${tail.length} chars after </html>`);
const b = await chromium.launch();
for (const [name,width,height,colorScheme] of CONFIGS) {
  const ctx = await b.newContext({viewport:{width,height},colorScheme});
  const p = await ctx.newPage();
  const errs = [];
  p.on('pageerror', e => errs.push(String(e).slice(0,140)));
  p.on('console', m => { if (m.type()==='error') errs.push(m.text().slice(0,140)); });
  await p.goto('file://'+F, {waitUntil:'networkidle'});
  await p.waitForTimeout(400);
  const r = await p.evaluate(() => {
    const over = document.documentElement.scrollWidth - document.documentElement.clientWidth;
    const wide = [...document.querySelectorAll('body *')]
      .filter(e => e.getBoundingClientRect().right > document.documentElement.clientWidth + 1)
      .slice(0,4).map(e => e.tagName+'.'+(e.className||'')+' r='+Math.round(e.getBoundingClientRect().right));
    return {over, wide,
      css: !!document.querySelector('link[href="site.css"]'),
      bars: document.querySelectorAll('#bars svg g').length,
      slope: document.querySelectorAll('#slope svg g').length,
      est: document.querySelectorAll('#est svg g').length,
      estAria: document.querySelector('#est svg')?.getAttribute('aria-label')?.slice(0,60),
      slopeCols: [...document.querySelectorAll('#slope svg text.ax')].map(t=>t.textContent),
      estCols: [...document.querySelectorAll('#est svg text.ax')].map(t=>t.textContent),
      rows: document.querySelectorAll('#bartable tr').length,
    };
  });
  if (r.over > 1) bad.push(`${name} H-SCROLL +${r.over}px :: ${r.wide.join(' | ')}`);
  if (!r.css) bad.push(`${name} NO-CSS`);
  if (errs.length) bad.push(`${name} ERR ${errs[0]}`);
  console.log(name, JSON.stringify({over:r.over,bars:r.bars,slope:r.slope,est:r.est,estCols:r.estCols,slopeCols:r.slopeCols,rows:r.rows,aria:r.estAria}));
  await ctx.close();
}
await b.close();
console.log(bad.length ? 'FAIL\n'+bad.join('\n') : '\nOK — dashboard passes 4 configurations');
process.exit(bad.length?1:0);
