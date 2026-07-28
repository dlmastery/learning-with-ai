import { chromium } from 'playwright';
import { readdirSync } from 'fs';
const dir='/home/eranti/learning-with-ai/docs/demos/';
const pages=readdirSync(dir).filter(f=>f.endsWith('.html'));
const b=await chromium.launch(); let fail=0;
for(const f of pages){
  for(const [sn,w,h] of [['m',390,844],['d',1400,900]]){
    const ctx=await b.newContext({viewport:{width:w,height:h}});
    const p=await ctx.newPage(); const errs=[],cons=[];
    p.on('pageerror',e=>errs.push(String(e).slice(0,120)));
    p.on('console',m=>{if(m.type()==='error')cons.push(m.text().slice(0,120))});
    await p.goto('file://'+dir+f,{waitUntil:'networkidle'}); await p.waitForTimeout(350);
    const r=await p.evaluate(()=>({o:document.documentElement.scrollWidth>window.innerWidth+1,
      css:!!document.querySelector('link[href="demo.css"]'),
      chip:!!document.querySelector('.chip'), t:document.title.slice(0,40)}));
    const bad=errs.length||cons.length||r.o||!r.css;
    if(bad)fail++;
    console.log(`${bad?'FAIL':'ok  '} ${f.padEnd(24)} ${sn} ${r.o?'H-SCROLL ':''}${!r.css?'NO-CSS ':''}${!r.chip?'no-chip ':''}${errs[0]||cons[0]||''}`);
    await ctx.close();
  }
}
await b.close(); console.log(fail?`\n${fail} FAILURES`:'\nALL DEMO PAGES PASS');
