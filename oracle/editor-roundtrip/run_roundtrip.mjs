// Phase 2 exit gate: MazeData.parse->emit must reproduce every corpus grid
// byte-for-byte under Ruffle. Run: node run_roundtrip.mjs  (exit 0 = green)

import http from "node:http";
import { readFile } from "node:fs/promises";
import { readFileSync, writeFileSync } from "node:fs";
import path from "node:path";
import puppeteer from "puppeteer-core";

const DIR = path.dirname(new URL(import.meta.url).pathname.replace(/^\/([A-Za-z]:)/, "$1"));
const ORACLE = path.resolve(DIR, "..");
const PORT = 8079;
const MIME = { ".html": "text/html", ".js": "text/javascript",
               ".wasm": "application/wasm", ".swf": "application/x-shockwave-flash" };

const grids = JSON.parse(readFileSync(path.join(DIR, "grids.json"), "utf8"));

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
  args: ["--no-first-run"] });
const page = await browser.newPage();
await page.goto(`http://127.0.0.1:${PORT}/index.html`);
await page.waitForFunction("window.__gate && (window.__gate.loaded || window.__gate.loadfail)",
  { timeout: 30000 });
await new Promise(r => setTimeout(r, 1500));

const out = { total: grids.length, pass: 0, fail: 0, failures: [] };
for (const d of grids) {
  const got = await page.evaluate(g => window.__player.roundTrip(g), d);
  if (got === d) out.pass++;
  else { out.fail++; if (out.failures.length < 20) out.failures.push({ d, got }); }
}
writeFileSync(path.join(DIR, "results.json"), JSON.stringify(out, null, 2));
console.log(`roundtrip: ${out.pass}/${out.total} byte-identical, ${out.fail} failures`);
if (out.failures.length) console.log("first failure:", JSON.stringify(out.failures[0], null, 2));
await browser.close(); server.close();
process.exit(out.fail === 0 ? 0 : 1);
