import { chromium } from 'playwright';
const F='/home/eranti/learning-with-ai/docs/index.html';
const b=await chromium.launch();
const ctx=await b.newContext({viewport:{width:390,height:844},colorScheme:'light'});
const p=await ctx.newPage();
await p.goto('file://'+F,{waitUntil:'networkidle'});
await p.waitForTimeout(400);
await p.locator('figure').nth(1).screenshot({path:'/tmp/claude-1000/-home-eranti/795498ca-1049-4fbf-9be0-44c3dc673b6d/scratchpad/slope-narrow.png'});
await b.close();
