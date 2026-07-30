import { chromium } from 'playwright';
const b = await chromium.launch();
for (const w of [390, 1400]) {
  const ctx = await b.newContext({ viewport:{width:w,height:1200}, deviceScaleFactor:2 });
  const p = await ctx.newPage();
  await p.goto('file:///home/eranti/learning-with-ai/docs/index.html', {waitUntil:'networkidle'});
  await p.locator('#bars').scrollIntoViewIfNeeded();
  await p.waitForTimeout(300);
  await p.locator('#bars').screenshot({ path:`/tmp/claude-1000/-home-eranti/795498ca-1049-4fbf-9be0-44c3dc673b6d/scratchpad/b2-${w}.png` });
  await ctx.close();
}
await b.close();
