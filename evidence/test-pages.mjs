import { chromium } from 'playwright';
const root='file:///home/eranti/learning-with-ai/docs/';
const pages=[['dashboard','index.html'],['gallery','demos/index.html']];
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
      bars:document.querySelectorAll('#bars svg g').length,
      slope:document.querySelectorAll('#slope svg g').length,
      tblRows:document.querySelectorAll('#bartable tr').length,
      title:document.title
    }));
    const scrolls = ov.docW > ov.winW+1;
    const bad = errs.length||cons.length||scrolls;
    if(bad)fail++;
    console.log(`${bad?'FAIL':'ok  '} ${name}/${sn} ${w}x${h} status=${resp.status()} docW=${ov.docW} winW=${ov.winW}${scrolls?' <-- H-SCROLL':''} bars=${ov.bars} slope=${ov.slope} tableRows=${ov.tblRows}`);
    if(errs.length)console.log('   pageerror:',errs.join(' | '));
    if(cons.length)console.log('   console:',cons.join(' | '));
    if(sn==='desktop'||sn==='mobile')
      await p.screenshot({path:`${name}-${sn}.png`,fullPage:sn==='desktop'});
    await ctx.close();
  }
}
// dark mode
const ctx=await b.newContext({viewport:{width:1440,height:900},colorScheme:'dark',deviceScaleFactor:2});
const p=await ctx.newPage(); await p.goto(root+'index.html',{waitUntil:'networkidle'});
await p.waitForTimeout(300); await p.screenshot({path:'dashboard-dark.png',fullPage:false});
// tooltip interaction
await p.hover('#bars svg g:nth-child(3)'); await p.waitForTimeout(200);
const tipOpacity=await p.evaluate(()=>getComputedStyle(document.getElementById('tip')).opacity);
console.log(tipOpacity>'0'?'ok   tooltip fires on hover':'FAIL tooltip did not fire');
await b.close();
console.log(fail?`\n${fail} FAILING CONFIGURATIONS`:'\nALL CONFIGURATIONS PASS');
