// Ruffle SetVariable / JS-bridge spike runner (guide 9 step 2, 7.3).
// Loads index.html in headless Chrome, lets Ruffle run the ORIGINAL
// signUpTankDesign13 bytes, probes the Flash-player JS API, then clicks the
// paint editor's colour cans and checks whether the SWF's
// getURL("javascript:...") bridge wrote into the page's hidden inputs.
//
// Setup (once):  see README.md  (fetch ruffle, copy swf, npm i)
// Run:           node run_spike.mjs
// Output:        results.json + spike.png (gitignored artefacts; findings go
//                to ../DIVERGENCES.md by hand)

import http from "node:http";
import { readFile } from "node:fs/promises";
import { writeFileSync } from "node:fs";
import path from "node:path";
import puppeteer from "puppeteer-core";

const DIR = path.dirname(new URL(import.meta.url).pathname.replace(/^\/([A-Za-z]:)/, "$1"));
const PORT = 8077;
const MIME = { ".html": "text/html", ".js": "text/javascript",
               ".wasm": "application/wasm", ".swf": "application/x-shockwave-flash" };

const server = http.createServer(async (req, res) => {
  try {
    const rel = decodeURIComponent(req.url.split("?")[0]).replace(/^\/+/, "") || "index.html";
    const body = await readFile(path.join(DIR, rel));
    res.writeHead(200, { "Content-Type": MIME[path.extname(rel)] || "application/octet-stream" });
    res.end(body);
  } catch {
    res.writeHead(404); res.end("nope");
  }
});
await new Promise(r => server.listen(PORT, "127.0.0.1", r));

// any Chromium works; TT_BROWSER overrides (this machine: Brave)
const EXE = process.env.TT_BROWSER ||
  "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe";
const browser = await puppeteer.launch({ executablePath: EXE, headless: true,
  args: ["--no-first-run"] });
const page = await browser.newPage();
await page.setViewport({ width: 900, height: 600 });

const console_lines = [];
page.on("console", m => console_lines.push(m.text()));
page.on("pageerror", e => console_lines.push("PAGEERROR " + e.message));

await page.goto(`http://127.0.0.1:${PORT}/index.html`);
await page.waitForFunction("window.__spike && (window.__spike.loaded || window.__spike.loadfail)",
  { timeout: 30000 });

// click across the paint editor. Decompile constants: colour cans sit in two
// groups, leftGroupLow=90..leftGroupHigh=234 and rightGroupLow=382, 9 cans,
// setUpCans(100) -- stage is 600x250 at 1:1 in our embed. Click a sweep along
// y=100 plus a few other rows to hit cans regardless of exact sprite origin.
const host = await page.$("#swfhost");
const box = await host.boundingBox();
const clicks = [];
for (const y of [40, 48, 56, 100, 150]) {
  for (let x = 60; x <= 560; x += 16) clicks.push([x, y]);
}
for (const [x, y] of clicks) {
  await page.mouse.click(box.x + x, box.y + y);
  await new Promise(r => setTimeout(r, 25));
}
await new Promise(r => setTimeout(r, 1000));

const result = await page.evaluate(() => ({
  probes: window.__spike.probes,
  loadfail: window.__spike.loadfail || null,
  inputs: Object.fromEntries(
    [...document.querySelectorAll("input")].map(i => [i.id, i.value])),
}));
result.console_tail = console_lines.slice(-60);
result.bridge_fired = Object.values(result.inputs).some(v => v !== "");

await page.screenshot({ path: path.join(DIR, "spike.png") });
writeFileSync(path.join(DIR, "results.json"), JSON.stringify(result, null, 2));
console.log(JSON.stringify({ probes: result.probes, inputs: result.inputs,
  bridge_fired: result.bridge_fired, loadfail: result.loadfail }, null, 2));

await browser.close();
server.close();
