// Renders gauntlet.json under Ruffle, screenshots to ruffle_render.png.
import http from "node:http";
import { readFile } from "node:fs/promises";
import { readFileSync } from "node:fs";
import path from "node:path";
import puppeteer from "puppeteer-core";

const DIR = path.dirname(new URL(import.meta.url).pathname.replace(/^\/([A-Za-z]:)/, "$1"));
const ORACLE = path.resolve(DIR, "..");
const PORT = 8081;
const MIME = { ".html": "text/html", ".js": "text/javascript",
               ".wasm": "application/wasm", ".swf": "application/x-shockwave-flash" };

const gauntlet = JSON.parse(readFileSync(path.join(DIR, "gauntlet.json"), "utf8"));

const server = http.createServer(async (req, res) => {
  try {
    const rel = decodeURIComponent(req.url.split("?")[0]).replace(/^\/+/, "") || "index.html";
    const base = rel.startsWith("ruffle-spike/") ? ORACLE : DIR;
    const body = await readFile(path.join(base, rel));
    res.writeHead(200, { "Content-Type": MIME[path.extname(rel)] || "application/octet-stream" });
    res.end(body);
  } catch { res.writeHead(404); res.end("nope"); }
});
await new Promise(r => server.listen(PORT, "127.0.0.1", r));

const EXE = process.env.TT_BROWSER ||
  "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe";
const browser = await puppeteer.launch({ executablePath: EXE, headless: true,
  args: ["--no-first-run", "--force-device-scale-factor=1"] });
const page = await browser.newPage();
await page.setViewport({ width: 688, height: 400 });
await page.goto(`http://127.0.0.1:${PORT}/index.html`);
await page.waitForFunction("window.__gate && (window.__gate.loaded || window.__gate.loadfail)",
  { timeout: 30000 });
await new Promise(r => setTimeout(r, 1500));

const verdict = await page.evaluate(d => window.__player.renderMaze(d), gauntlet.d);
console.log("renderMaze:", verdict);
await new Promise(r => setTimeout(r, 500));
await page.screenshot({ path: path.join(DIR, "ruffle_render.png") });
await browser.close(); server.close();
process.exit(verdict === "ok" ? 0 : 1);
