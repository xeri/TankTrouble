# Served-side divergence log

Every way the reconstruction's **user-facing output** differs from what
tanktrouble.com served in 2017-2018. One entry per divergence, with what the
original did, what we do, why, and how to undo it.

Rules:

* The default stack (`docker compose up -d`) serves era bytes. Anything that
  changes them is opt-in, off by default, and listed here.
* A divergence lands here **before** it ships, not after someone notices.
* Anything visibly non-original must announce itself on screen, so no
  screenshot taken from this stack can be mistaken for evidence.
* Runtime divergences under Ruffle/projector live in `oracle/DIVERGENCES.md`
  (gate C). This file is the page/server side.

---

## 1. Flash game stage — unavoidable, no workaround shipped

**Original:** `includes/TankTrouble_v4.0.swf` in a `swfobject` embed; the
maze and the 1/2/3-player entry buttons are drawn by the SWF.

**Now:** browsers have no Flash plugin, so the stage shows the browser's own
"Couldn't load plugin" text. Page bytes are unchanged — nothing is
substituted, no shim is injected.

**Why not fix it:** any player (Ruffle, a projector wrapper) changes what the
page contains. Gate C evaluates runtimes separately against the original SWF;
that is where a player belongs, not in the served page.

**Undo:** n/a — the divergence is the browser's, not ours.

---

## 2. AdSense skyscraper slots — dev-only filler, OFF by default

**Original:** two `<ins class="adsbygoogle" style="…width:160px;height:600px">`
slots, left and right of the content column, filled by
`pagead2.googlesyndication.com`.

**Now, default stack:** the slots keep their exact 160×600 box (the inline
width/height and the floated parents do that on their own — the layout never
depended on an ad rendering) and stay blank. **Served bytes are unchanged.**

**Now, dev overlay:** `docker compose -f docker-compose.yml -f
docker-compose.dev.yml up -d` sets `TT_DEV_FILLER=1` and mounts
`docker/php/dev-filler.php`, which appends one `<style id="tt-dev-filler">`
before `</head>`. The slots get a grey diagonal hatch and the rotated label
*"ad slot — dev filler, not original"*.

**Why:** a blank 160×600 reads as breakage when reviewing a route, and that
noise is what let a real 193-asset hole sit unnoticed. The filler removes the
false alarm without touching the reconstruction.

**Constraints honoured:** the file lives outside `srv/`, has no ledger row,
is unreachable by any request, and no-ops unless `TT_DEV_FILLER=1` — so even
a stray mount cannot change output. Gate F must run against the default
stack:

```bash
docker compose up -d --force-recreate php
```

**Undo:** stop using the overlay file; delete `docker/php/dev-filler.*` and
`docker/docker-compose.dev.yml`.

---

## 3. Per-request regions frozen at era-final bytes

**Original:** live values — visit counters, online counts, top-10 rankings,
forum latest posters, the rotating tagline, seasonal promos.

**Now:** frozen at the era-final capture's bytes inside the `@O` fences of
`srv/index.php`. Declared in that file's `@caveat` block; gate F masks them.

**Why:** the values are unrecoverable state, and inventing plausible live
numbers would be the most dangerous kind of stub.

**Undo:** each region becomes dynamic again when its endpoint and seed data
are reconstructed; the mask annotation names the producing variable.

---

## 4. SAJAX endpoints answer the stock "not callable" error

**Original:** a full SAJAX export list.

**Now:** `$GLOBALS['sajax_export_list']` holds only reconstructed endpoints
(`getScraps`, and the maze endpoints added since). Everything else returns
stock Sajax 0.12 `-:<func> not callable`. Zero era SAJAX response bodies are
archived.

**Why:** guide §6.2 rule 3 — reject, never fake.

**Undo:** each function joins the list as its endpoint is reconstructed and
gains a replay test.

---

## 5. Scrapyard counter stops after ~60 s — frozen state, client self-corrects to zero

**Original:** `scrapyard_state` was live. `getScraps` returned a rising total
and the flip-plate counter climbed continuously.

**Now:** the table holds one frozen row —
`scraps=1785664230, velocity=0.0071382502652744` (seed
`docker/mysql/init/60-scrapyard.sql`, labelled ARBITRARY: latest archived
scraps from `includes-tree/20160126_getScrapyard.php`, the only archived
velocity from `20150928_getScrapyard.php`).

**Observed behaviour and why**, traced through the O client
(`srv/includes/scrapyard.js`):

1. `create()` calls `_getScraps(true)` — the one request that asks for
   velocity (:133). The client sets `velocity = 0.00714/1000` scraps per ms,
   i.e. one scrap every ~140 s, so the last plate would flip about twice an
   hour even in the best case.
2. Every later poll is `_getScraps(false)` (:247, :251) — first at
   `SCRAPYARD_FIRST_UPDATE` 60 s, then every 300 s. Those responses carry no
   velocity, so the client re-derives it (:214-217):
   `velocity = max(0, (deltaScraps + discrepancy * 0.25) / deltaTime)`.
3. Against a frozen row `deltaScraps` is 0 and `discrepancy` is negative (the
   display crept above the server value), so `max(0, …)` yields **0**.

The counter therefore creeps for the first 60 s and is then pinned forever.
Not a rendering fault and not a missing asset — the endpoint, the seed and
the O client are all behaving exactly as written.

**Why not "fix" it:** making the counter climb means the server inventing
live state. Gate D's own comment — "a stub that returns plausible data is the
most dangerous thing in this project" — applies directly, and no era body
records what the real rate was in 2017-2018.

**Option, if a moving counter is wanted (not taken):** add an `as_of` column
and return `scraps + floor(velocity * (now - as_of))`. That is monotonic,
uses only archived numbers, and stops the client zeroing its own velocity —
but the digits on screen would then be extrapolated, not observed, and every
screenshot would carry a fabricated total. It would need its own DECISIONS
entry, a schema bump, and an update to `tests/test_getscrapyard_replay.py`.

**Undo:** n/a — current behaviour is the no-invention default.
