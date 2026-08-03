// Boot-path check with ExternalInterface unavailable (projector simulation):
// allowScriptAccess=false -> EI off -> editor must boot VISIBLE with maze.
import http from "node:http";
import { readFile } from "node:fs/promises";
import { readFileSync } from "node:fs";
import path from "node:path";
import puppeteer from "puppeteer-core";
const DIR = path.dirname(new URL(import.meta.url).pathname.replace(/^\/([A-Za-z]:)/, "$1"));
const ORACLE = path.resolve(DIR, "..");
const SRC = path.resolve(DIR, "../../src/mazecreator");
const PORT = 8085;
const MIME = { ".html": "text/html", ".js": "text/javascript", ".wasm": "application/wasm", ".swf": "application/x-shockwave-flash" };
const gauntlet = JSON.parse(readFileSync(path.join(DIR, "gauntlet.json"), "utf8"));
const INIT = Buffer.from(`u=7&n=testuser01&t=${gauntlet.title}&d=${gauntlet.d}&s=1`).toString("base64");
const HTML = `<!DOCTYPE html><html><head><meta charset="utf-8"><style>body{margin:0}</style>
<script src="ruffle-spike/ruffle/ruffle.js"></script></head><body>
<div id="swfhost" style="width:688px;height:400px"></div><script>
window.__gate = {};
window.RufflePlayer = window.RufflePlayer || {};
window.RufflePlayer.config = { autoplay: 'on', unmuteOverlay: 'hidden', allowScriptAccess: false, logLevel: 'warn', base: 'includes/' };
window.addEventListener('load', function () {
  var p = window.RufflePlayer.newest().createPlayer(); window.__player = p;
  p.style.width='688px'; p.style.height='400px';
  document.getElementById('swfhost').appendChild(p);
  p.load('includes/editor.swf?initCode=${INIT}')
   .then(function(){ window.__gate.loaded = true; })
   .catch(function(e){ window.__gate.loadfail = String(e); });
});
</script></body></html>`;
const server = http.createServer(async (req, res) => {
  try {
    const rel = decodeURIComponent(req.url.split("?")[0]).replace(/^\/+/, "") || "index.html";
    if (rel === "index.html") { res.writeHead(200, {"Content-Type": "text/html"}); res.end(HTML); return; }
    let file;
    if (rel === "includes/editor.swf") file = path.join(SRC, "editor.swf");
    else if (rel.startsWith("ruffle-spike/")) file = path.join(ORACLE, rel);
    else file = path.join(DIR, rel);
    const body = await readFile(file);
    res.writeHead(200, { "Content-Type": MIME[path.extname(rel)] || "application/octet-stream" });
    res.end(body);
  } catch { res.writeHead(404); res.end("nope"); }
});
await new Promise(r => server.listen(PORT, "127.0.0.1", r));
const EXE = process.env.TT_BROWSER || "C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe";
const browser = await puppeteer.launch({ executablePath: EXE, headless: true, args: ["--no-first-run", "--force-device-scale-factor=1"] });
const page = await browser.newPage();
await page.setViewport({ width: 688, height: 400 });
await page.goto(`http://127.0.0.1:${PORT}/index.html`);
await page.waitForFunction("window.__gate && (window.__gate.loaded || window.__gate.loadfail)", { timeout: 30000 });
await new Promise(r => setTimeout(r, 2500));
await page.screenshot({ path: path.join(DIR, "ruffle_noei.png") });
console.log("saved ruffle_noei.png; loadfail:", await page.evaluate(() => window.__gate.loadfail || "none"));
await browser.close(); server.close();
