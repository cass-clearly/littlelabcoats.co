const puppeteer = require('puppeteer-core');
const path = require('path');
(async()=>{
 const inFile = process.argv[2];
 const outFile = process.argv[3];
 if (!inFile || !outFile) throw new Error('usage: node scripts/render-lesson-pdf.js <input.html> <output.pdf>');
 const browser = await puppeteer.launch({executablePath:'/usr/bin/google-chrome', headless:true, args:['--no-sandbox','--disable-gpu']});
 const page = await browser.newPage();
 await page.goto('file://' + path.resolve(inFile), {waitUntil:'networkidle0', timeout:120000});
 await page.pdf({path: outFile, format:'Letter', printBackground:true, preferCSSPageSize:true, margin:{top:'0',right:'0',bottom:'0',left:'0'}});
 await browser.close();
})();
