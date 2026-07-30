import { chromium } from 'playwright';
import { fileURLToPath, pathToFileURL } from 'url';
import { dirname, join } from 'path';
const here=dirname(fileURLToPath(import.meta.url));
const root=pathToFileURL(join(here,'..','docs')+'/').href;
const pages=[
  ['dashboard','index.html'],
  ['deck','deck.html'],
  ['paper','paper.html'],
  ['atlas','atlas.html'],
  ['gallery','demos/index.html']
];
const sizes=[['mobile',390,844],['tablet',820,1180],['desktop',1440,900]];
const b=await chromium.launch();
let fail=0;
for(const [name,path] of pages){
  for(const [sn,w,h] of sizes){
    const ctx=await b.newContext({viewport:{width:w,height:h},deviceScaleFactor:2});
    const p=await ctx.newPage();
    const errs=[],cons=[];
    p.on('pageerror',e=>errs.push(String(e)));
    p.on('console',m=>{if(m.type()==='error')cons.push(m.text())});
    const resp=await p.goto(root+path,{waitUntil:'networkidle'});
    await p.waitForTimeout(400);
    // horizontal overflow check
    const ov=await p.evaluate(()=>({
      docW:document.documentElement.scrollWidth, winW:window.innerWidth,
      capabilities:document.querySelectorAll('.cap').length,
      moments:document.querySelectorAll('.moment').length,
      experiments:document.querySelectorAll('.experiment').length,
      slides:document.querySelectorAll('.slide').length,
      headings:document.querySelectorAll('h1').length,
      title:document.title
    }));
    const scrolls = ov.docW > ov.winW+1;
    const bad = errs.length||cons.length||scrolls;
    if(bad)fail++;
    const structural=(name==='deck'&&ov.slides!==15)||(name==='paper'&&ov.headings!==1);
    if(structural&&!bad)fail++;
    console.log(`${bad||structural?'FAIL':'ok  '} ${name}/${sn} ${w}x${h} status=${resp.status()} docW=${ov.docW} winW=${ov.winW}${scrolls?' <-- H-SCROLL':''} capabilities=${ov.capabilities} moments=${ov.moments} experiments=${ov.experiments} slides=${ov.slides} h1=${ov.headings}`);
    if(errs.length)console.log('   pageerror:',errs.join(' | '));
    if(cons.length)console.log('   console:',cons.join(' | '));
    if(name!=='atlas'&&(sn==='desktop'||sn==='mobile'))
      await p.screenshot({path:`${name}-${sn}.png`,fullPage:sn==='desktop'});
    await ctx.close();
  }
}
// dark mode
const ctx=await b.newContext({viewport:{width:1440,height:900},colorScheme:'dark',deviceScaleFactor:2});
const p=await ctx.newPage(); await p.goto(root+'index.html',{waitUntil:'networkidle'});
await p.waitForTimeout(300); await p.screenshot({path:'dashboard-dark.png',fullPage:false});
// capability filter interaction
await p.click('[data-filter="generation"]'); await p.waitForTimeout(100);
const filtered=await p.evaluate(()=>({
  visible:[...document.querySelectorAll('.cap')].filter(x=>!x.hidden).length,
  wrong:[...document.querySelectorAll('.cap')].filter(x=>!x.hidden&&x.dataset.kind!=='generation').length
}));
if(filtered.visible===5&&filtered.wrong===0) console.log('ok   capability filter shows the five generation rows');
else { console.log(`FAIL capability filter visible=${filtered.visible} wrong=${filtered.wrong}`); fail++; }
await b.close();
console.log(fail?`\n${fail} FAILING CONFIGURATIONS`:'\nALL CONFIGURATIONS PASS');
