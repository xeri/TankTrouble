// Editor-spike runner: is ExternalInterface.addCallback("SetVariable") enough
// to run the ORIGINAL page JS against a REBUILT editor SWF under Ruffle?
// Run:    node run_editor_spike.mjs        (after sh build.sh)
// Output: results.json + spike-*.png; findings -> ../DIVERGENCES.md by hand.

import http from "node:http";
import { readFile } from "node:fs/promises";
import { writeFileSync } from "node:fs";
import path from "node:path";
import puppeteer from "puppeteer-core";

const DIR = path.dirname(new URL(import.meta.url).pathname.replace(/^\/([A-Za-z]:)/, "$1"));
const ORACLE = path.resolve(DIR, "..");   // so /ruffle-spike/ruffle/* resolves
const PORT = 8078;
const MIME = { ".html": "text/html", ".js": "text/javascript",
               ".wasm": "application/wasm", ".swf": "application/x-shockwave-flash" };

const server = http.createServer(async (req, res) => {
  try {
    const rel = decodeURIComponent(req.url.split("?")[0]).replace(/^\/+/, "") || "index.html";
    const base = rel.startsWith("ruffle-spike/") ? ORACLE : DIR;
    const body = await readFile(path.join(base, rel.startsWith("ruffle-spike/") ? rel : rel));
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
await page.setViewport({ width: 900, height: 600 });
const console_lines = [];
page.on("console", m => console_lines.push(m.text()));
page.on("pageerror", e => console_lines.push("PAGEERROR " + e.message));

await page.goto(`http://127.0.0.1:${PORT}/index.html`);
await page.waitForFunction("window.__spike && (window.__spike.loaded || window.__spike.loadfail)",
  { timeout: 30000 });
await new Promise(r => setTimeout(r, 2000));   // let the SWF boot + getURL fire

const shot = n => page.screenshot({ path: path.join(DIR, n) });
await shot("spike-boot.png");

const result = await page.evaluate(async () => {
  const p = window.__player;
  const out = { boot: window.__spike.boot, loadfail: window.__spike.loadfail || null,
                setvar_type: typeof p.SetVariable, getvar_type: typeof p.GetVariable };
  const call = (f, ...a) => { try { return { ok: true, ret: f(...a) }; }
                              catch (e) { return { ok: false, err: String(e) }; } };
  // THE question: does the EI-exposed SetVariable answer the ORIGINAL call shape?
  out.set_tool  = call((n, v) => p.SetVariable(n, v), "newToolRequested", "crateSpawn");
  await new Promise(r => setTimeout(r, 500));
  out.get_last  = call(n => p.GetVariable(n), "lastSet");
  out.get_init  = call(n => p.GetVariable(n), "initDecoded");
  out.set_save  = call((n, v) => p.SetVariable(n, v), "_root.saveRequested", "true");
  await new Promise(r => setTimeout(r, 500));
  out.saved = window.__spike.saved;
  return out;
});
await shot("spike-after.png");

result.console_tail = console_lines.slice(-40);
result.verdicts = {
  flashvars_delivered:  result.boot === "u=99&n=testuser01&",
  geturl_boot_fired:    result.boot !== null,
  ei_setvariable_works: result.set_tool?.ok === true &&
                        result.get_last?.ret === "newToolRequested=crateSpawn",
  geturl_save_fired:    result.saved === "_root.saveRequested=true",
};
writeFileSync(path.join(DIR, "results.json"), JSON.stringify(result, null, 2));
console.log(JSON.stringify(result.verdicts, null, 2));
console.log("full details in results.json");
await browser.close(); server.close();
