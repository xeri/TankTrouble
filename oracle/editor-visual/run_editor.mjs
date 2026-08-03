// Phase 3 interaction gate: boots the real editor SWF under Ruffle and
// asserts the full page contract + editing semantics. Exit 0 = green.
// --screenshot: save ruffle_editor.png after fade-in and exit (gate C).
import http from "node:http";
import { readFile } from "node:fs/promises";
import { readFileSync } from "node:fs";
import { execFileSync } from "node:child_process";
import path from "node:path";
import puppeteer from "puppeteer-core";

const DIR = path.dirname(new URL(import.meta.url).pathname.replace(/^\/([A-Za-z]:)/, "$1"));
const ORACLE = path.resolve(DIR, "..");
const SRC = path.resolve(DIR, "../../src/mazecreator");
const PORT = 8082;
const MIME = { ".html": "text/html", ".js": "text/javascript",
               ".wasm": "application/wasm", ".swf": "application/x-shockwave-flash" };
const SHOT = process.argv.includes("--screenshot");

const gauntlet = JSON.parse(readFileSync(path.join(DIR, "gauntlet.json"), "utf8"));
const INIT = Buffer.from(
  `u=7&n=testuser01&t=${gauntlet.title}&d=${gauntlet.d}&s=1`).toString("base64");

const server = http.createServer(async (req, res) => {
  try {
    const rel = decodeURIComponent(req.url.split("?")[0]).replace(/^\/+/, "") || "index.html";
    if (rel.startsWith("includes/") && rel !== "includes/editor.swf") {
      // proxy PHP endpoints to the docker stack so LoadVars posts land
      const chunks = [];
      for await (const c of req) chunks.push(c);
      const upstream = await fetch("http://127.0.0.1:8056/" + rel, {
        method: req.method,
        headers: { "content-type": req.headers["content-type"] || "application/x-www-form-urlencoded" },
        body: req.method === "POST" ? Buffer.concat(chunks) : undefined,
      });
      const buf = Buffer.from(await upstream.arrayBuffer());
      res.writeHead(upstream.status, { "Content-Type": "text/plain" });
      res.end(buf);
      return;
    }
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

const EXE = process.env.TT_BROWSER ||
  "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe";
const browser = await puppeteer.launch({ executablePath: EXE, headless: true,
  args: ["--no-first-run", "--force-device-scale-factor=1"] });
const page = await browser.newPage();
await page.setViewport({ width: 688, height: 400 });
await page.evaluateOnNewDocument(() => {
  window.__calls = [];
  window.showMazeCreatorToolsAndTitle = (u, t) => window.__calls.push(["show", u, t]);
  window.hideMazeCreatorToolsAndTitle = (u) => window.__calls.push(["hide", u]);
});
await page.goto(`http://127.0.0.1:${PORT}/index.html?swf=includes/editor.swf`
  + `&initCode=${encodeURIComponent(INIT)}`);
await page.waitForFunction("window.__gate && (window.__gate.loaded || window.__gate.loadfail)",
  { timeout: 30000 });
await new Promise(r => setTimeout(r, 1500));

const results = [];
const check = (name, cond) => { results.push([name, !!cond]); if (!cond) console.log("FAIL:", name); };
const sv = (n, v) => page.evaluate((a, b) => window.__player.SetVariable(a, b), n, v);
const gv = (n) => page.evaluate(a => window.__player.GetVariable(a), n);
const wait = (ms) => new Promise(r => setTimeout(r, ms));
const CELL = 32, LX = 56, LY = 50;
// gauntlet is 13x8: lattice offset int part (2,1), frac (16px, 0)
const FX = 16, FY = 0;
const cellClick = (cx, cy) =>
  page.mouse.click(LX + FX + cx * CELL + CELL / 2, LY + FY + cy * CELL + CELL / 2);

// boot: hidden until the page fades us in (page contract, +1200ms)
check("boots hidden", (await gv("stageAlpha")) === "0");
await sv("fadeOut", "false");
await wait(1200);
check("fades in over 15 frames", (await gv("stageAlpha")) === "100");

if (SHOT) {
  await wait(500);
  await page.screenshot({ path: path.join(DIR, "ruffle_editor.png") });
  console.log("saved ruffle_editor.png");
  await browser.close(); server.close();
  process.exit(0);
}

check("boots into preview", (await gv("state")) === "preview");
check("initCode round-trips", (await gv("mazeD")) === gauntlet.d);
check("initCode title", (await gv("titleText")) === gauntlet.title);

// preview click -> edit + outbound showMazeCreatorToolsAndTitle
await cellClick(6, 4); await wait(300);
check("click enters edit", (await gv("state")) === "edit");
const calls1 = await page.evaluate(() => window.__calls);
check("show call fired", calls1.some(c => c[0] === "show" && c[1] === "7" && c[2] === gauntlet.title));
check("default tool construct", (await gv("tool")) === "construct");

// construct: paint a floor cell on, then off (lattice corner 0,0)
const d0 = await gv("mazeD");
await cellClick(0, 0); await wait(200);
const d1 = await gv("mazeD");
check("floor paint changes maze", d1 !== d0);
await cellClick(0, 0); await wait(200);
check("floor unpaint restores", (await gv("mazeD")) === d0);

// construct: toggle an interior wall between two floor cells. Paint two
// adjacent cells in an empty lattice region (gauntlet spans lattice cols
// 2-14, rows 1-8 -- row 0 cols 16,17 are clear), click their shared edge.
await cellClick(16, 0); await cellClick(17, 0); await wait(200);
const dPair = await gv("mazeD");
await page.mouse.click(LX + FX + 17 * CELL + 1, LY + FY + 0 * CELL + CELL / 2);
await wait(200);
const dWall = await gv("mazeD");
check("interior wall toggles", dWall !== dPair);
await page.mouse.click(LX + FX + 17 * CELL + 1, LY + FY + 0 * CELL + CELL / 2);
await wait(200);
check("interior wall toggles back", (await gv("mazeD")) === dPair);

// tankSpawn: gauntlet has 5 tanks already -> cap refuses a 6th; crateSpawn
// same; toggling off then re-adding works within the cap
await sv("newToolRequested", "tankSpawn");
check("tool switches", (await gv("tool")) === "tankSpawn");
const countType = (d, t) => {
  const f = d.split("#"); let n = +f[3], i = 4, k = 0;
  for (let o = 0; o < n; o++) { if (+f[i + 2] === t) k++; i += 4; }
  return k;
};
check("boot maze at tank cap", countType(await gv("mazeD"), 5) === 5);
await cellClick(14, 8); await wait(200);   // painted floor cell, empty
check("tank cap refuses 6th", countType(await gv("mazeD"), 5) === 5);
// remove one tank (gauntlet tank at maze cell (7,2) -> lattice (7-1+2, 2-1+1)=(8,2))
await cellClick(8, 2); await wait(200);
check("tank toggle removes", countType(await gv("mazeD"), 5) === 4);
await cellClick(8, 2); await wait(200);
check("tank re-adds within cap", countType(await gv("mazeD"), 5) === 5);

// title + error panel vocabulary (literal _root.-prefixed names)
await sv("_root.mazeName", "New Name");
check("mazeName literal name", (await gv("titleText")) === "New Name");
check("error hidden initially", (await gv("errorVisible")) === "false");
await sv("_root.mazeName", "");
await sv("_root.saveRequested", "true"); await wait(300);
check("save with empty title shows error", (await gv("errorVisible")) === "true");
await sv("_root.errorPanel.hide", "yes");
check("errorPanel.hide literal name", (await gv("errorVisible")) === "false");

// real save last: rename, request save, expect hide call + preview + DB write
await sv("_root.mazeName", "Phase Three Gate");
await sv("_root.saveRequested", "true");
await wait(2000);
const calls2 = await page.evaluate(() => window.__calls);
check("hide call fired on save", calls2.some(c => c[0] === "hide" && c[1] === "7"));
check("save flips to preview", (await gv("state")) === "preview");
check("no error on good save", (await gv("errorVisible")) === "false");
const savedD = await gv("mazeD");
const q = Buffer.from("userName=testuser01&a=0.1&b=0.2").toString("base64");
const body = await (await fetch(`http://127.0.0.1:8056/includes/loadMaze.php?q=${q}`)).text();
const pairs = Object.fromEntries(Buffer.from(body.slice(2), "base64").toString("latin1")
  .split("&").map(p => p.split("=")));
check("DB round-trip d matches editor", pairs.d === savedD);
check("DB round-trip title", pairs.t === "Phase Three Gate");

// previewLoaded + fadeOut vocabulary still fine after a save cycle
await sv("previewLoaded", "");
check("previewLoaded -> preview", (await gv("state")) === "preview");
await sv("fadeOut", "true"); await wait(1200);
check("fadeOut fades to 0", (await gv("stageAlpha")) === "0");

const failed = results.filter(r => !r[1]);
console.log(`editor interaction: ${results.length - failed.length}/${results.length} checks green`);
await browser.close(); server.close();
// keep the seeded corpus pristine (gate B coverage) -- same rule as
// tests/test_savemaze.py
try {
  execFileSync("docker", ["exec", "docker-mysql-1", "sh", "-c",
    'exec mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" tanktrouble ' +
    "-e \"DELETE FROM mazes WHERE author='testuser01'\""], { timeout: 60000 });
} catch {}
process.exit(failed.length === 0 ? 0 : 1);
