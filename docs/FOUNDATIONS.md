<!-- Machine-parsed by tests/test_foundations.py. Keep the eight bold field
     labels exactly as written; add rows, never renumber them. -->

# Foundations — the structures everything else rests on

A wrong pixel is cheap. A wrong **structure** — a schema key, a wire format, a
lattice origin, an interaction model — is expensive, because by the time
evidence contradicts it, a milestone of work is bolted to it. This file exists
so that never happens quietly.

Every load-bearing structural commitment gets a row **before** code depends on
it. `tests/test_foundations.py` checks that every row is complete and that every
file it names exists.

## The five rules

1. **No structure without a falsifier.** If you cannot state the observation
   that would overturn it, it is a preference, not a deduction. Write the
   falsifier while you still know exactly what would settle it.
2. **Grade C or below is `provisional`.** It may be built on only when its
   dependents are listed and it sits behind a single named seam.
3. **One seam per invention.** The invented value lives in exactly one module,
   consumed verbatim. Two copies guarantee an eventual disagreement, and make
   THE OVERHAUL RULE unaffordable.
4. **Cheap outstanding evidence is gathered before building on the guess**, not
   after. If a `docs/standards/VISUAL-EVIDENCE-WANTED.md` entry would settle a foundation
   in an afternoon, that afternoon comes first.
5. **A contradiction opens an overhaul, never a patch.** Mark the row
   `falsified`, open the `overhaul` row in `docs/PROGRESS.md` with the blast
   radius, and rewrite the piece wholesale.

## Fields

`Grade` uses `DEDUCE.md` §0.1 — **A** directly observed · **B** observed
indirectly but unambiguously · **C** name or shape proven, content not · **D**
wrong era or wrong site · **X** artefact — plus **scope** for deliberate
decisions that no observation can overturn.

`Status` is `pinned` · `provisional` · `falsified` · `superseded`.

---

### F-01 — Target era is 2017–2018; the corpus is partitioned CLASSIC / MODERN
- **Layer:** scope
- **Grade:** scope
- **Status:** pinned
- **Evidence:** `DECISIONS.md` 2026-08-02 "target era"; the partition itself is grade A — the modern SPA answers 200 for any path, so a modern-era 200 is worthless as filesystem evidence (`DEDUCE.md` Part 2).
- **Falsifier:** none — a deliberate scope choice. Reversible by re-running `tools/resolve_era.py` with a different window and re-copying.
- **Dependents:** every `O`/`O?` row in `LEDGER.tsv`; `tools/resolve_era.py`; `tools/era_choices.tsv`; every gate.
- **Blast radius:** total. Every asset re-resolves; every capture set changes.
- **Seam:** `tools/resolve_era.py`

### F-02 — The classic site is six `?query` routes served by one `index.php`
- **Layer:** document-root shape
- **Grade:** A
- **Status:** pinned
- **Evidence:** era CDX rows and captures; `DEDUCE.md` Part 2 era partition (classic uses `?query` routes, modern uses path routes).
- **Falsifier:** an in-era CDX row with a 200 for a path-routed page that is not `/` plus a query string.
- **Dependents:** `srv/index.php`; `archive-cleaned/classification/*.tsv`; `tests/test_render_diff.py`.
- **Blast radius:** the whole de-render; every mask; gate F.
- **Seam:** `srv/index.php` route dispatch

### F-03 — De-render is verbatim fences, not shared emitters; no new files under `srv/`
- **Layer:** document-root shape
- **Grade:** scope
- **Status:** pinned
- **Evidence:** `DECISIONS.md` 2026-08-03 "de-render strategy: verbatim fences, not shared emitters". A new file under `srv/` is a fetchable path with no CDX evidence — i.e. a claim about the original filesystem.
- **Falsifier:** an era capture referencing an include path that must exist as a file.
- **Dependents:** `srv/index.php`; `tests/test_fenced_regions.py`; `.claude/rules/php-endpoints.md`.
- **Blast radius:** structural rewrite of `index.php`; fenced-region verifier re-pinned.
- **Seam:** `srv/index.php`

### F-04 — `loadMaze` response is `r=` + base64(shuffle(`t`,`n`,`d`,`s`))
- **Layer:** wire format
- **Grade:** A
- **Status:** pinned
- **Evidence:** all 842 archived payloads decode to exactly keys `{t,n,d,s}` with `s` **inside** the base64; all 24 pair orders occur, so the shuffle is per-request. Corrects guide §6.2. `DECISIONS.md` 2026-08-03 mazes-remodel entry.
- **Falsifier:** an archived body with a key outside `{t,n,d,s}`, or with `s` outside the base64 envelope.
- **Dependents:** `srv/includes/loadMaze.php`; `srv/includes/saveMaze.php` (mirrors it); `seed/seed_mazes.py`; `tests/test_loadmaze_replay.py`; `src/mazecreator/MazeData.as`.
- **Blast radius:** gate B, the seed, and the editor's save path all re-pin together.
- **Seam:** `srv/includes/loadMaze.php`

### F-05 — `mazes` is one row per `(author, slot)`, latest capture wins
- **Layer:** schema
- **Grade:** B
- **Status:** pinned
- **Evidence:** the corpus is a time series — 842 bodies → 744 distinct contents → 672 `(author, slot)` states, with 70 authors re-captured holding mazes that never coexisted. Key shape deduced from `MazeDataFetcher.as`'s userName query. `DECISIONS.md` 2026-08-03, supersedes the digest-keyed model.
- **Falsifier:** evidence that the live DB held more than one maze per `(author, slot)` simultaneously, or that lookup was not by author.
- **Dependents:** `docker/mysql/init/00-schema.sql`; `seed/seed_mazes.py`; `srv/includes/loadMaze.php`; `tests/test_seed.py`; `tests/test_loadmaze_replay.py`.
- **Blast radius:** reseed plus gate B's entire winner-set construction.
- **Seam:** `seed/seed_mazes.py`

### F-06 — `mazes.author` is `VARBINARY(16)` — byte-exact, no PAD-SPACE, no case folding
- **Layer:** schema
- **Grade:** B
- **Status:** pinned
- **Evidence:** the corpus holds 12 byte-distinct author pairs that collide under `VARCHAR` PAD-SPACE + `utf8_general_ci` (10 case pairs, 2 trailing-space pairs). Merging them would invent identity and drop observed states. `DECISIONS.md` 2026-08-03.
- **Falsifier:** evidence that the original treated those pairs as one account — e.g. an archived response serving the same maze for both spellings.
- **Dependents:** `docker/mysql/init/00-schema.sql`; `srv/includes/loadMaze.php` (byte-exact lookup); `seed/seed_mazes.py`.
- **Blast radius:** reseed; 12 observed states appear or vanish.
- **Seam:** `docker/mysql/init/00-schema.sql`

### F-07 — Engine MyISAM, charset utf8mb3, collation `utf8_general_ci`
- **Layer:** schema
- **Grade:** C
- **Status:** provisional
- **Evidence:** period default at the site's 2008 birth, matching `mysql_*`-era PHP; a full-corpus scan found 44,739 BMP non-ASCII characters and zero astral ones. Never observed. `DECISIONS.md` 2026-08-03 "milestone-2 DDL choices are M3".
- **Falsifier:** any archived server error, header or export disclosing the real engine or charset.
- **Dependents:** `docker/mysql/init/00-schema.sql`; every seed importer.
- **Blast radius:** low — reseed only. No wire format depends on it.
- **Seam:** `docker/mysql/init/00-schema.sql`

### F-08 — mazeCreator lattice is fixed for the session; mazes snap to integer cells
- **Layer:** visual geometry
- **Grade:** C
- **Status:** falsified
- **Evidence:** derived from one screenshot (`docs/standards/MAZECREATOR-VISUAL-SPEC.md`), which shows half-cell centring but cannot show what happens as a maze grows. `DECISIONS.md` 2026-08-04 item 7 records it as an M3 choice.
- **Falsifier:** footage of a maze growing at the edge — stated in `docs/standards/VISUAL-EVIDENCE-WANTED.md` #6. **This falsifier has fired:** `docs/evidence/manual-evidence/B-maze-editor-interaction.md` reports the lattice re-fits and re-centres live.
- **Dependents:** `src/mazecreator/MazeRenderer.as`; `oracle/editor-visual/gauntlet.json`; the gate C pixel baseline; `docs/standards/MAZECREATOR-VISUAL-SPEC.md`.
- **Blast radius:** renderer geometry, the transcribed test vector, and the pixel oracle's baseline all re-pin together. The wire format is untouched.
- **Seam:** `src/mazecreator/MazeRenderer.as` statics, fed by `docs/standards/MAZECREATOR-VISUAL-SPEC.md`

### F-09 — Editor interaction model: click-to-toggle, no drag-paint, no hover preview
- **Layer:** interaction model
- **Grade:** X
- **Status:** falsified
- **Evidence:** none — invented so the editor ran end to end. `DECISIONS.md` 2026-08-04 item 1, flagged revisable by any editing footage (`docs/standards/VISUAL-EVIDENCE-WANTED.md` #5).
- **Falsifier:** footage of someone drawing a maze. **This falsifier has fired:** `docs/evidence/manual-evidence/B-maze-editor-interaction.md` reports drag-paint, hover wall preview and a cursor ghost all present.
- **Dependents:** `src/mazecreator/Editor.as`; the 28-check interaction gate in `oracle/editor-visual/`.
- **Blast radius:** the editor's whole input layer. Behaviour only — no wire format, no page contract.
- **Seam:** `src/mazecreator/Editor.as`

### F-10 — Editor floor tone is a deterministic hash, ~1/3 light
- **Layer:** visual geometry
- **Grade:** C
- **Status:** provisional
- **Evidence:** the screenshot's tone mix is ≈1/3 light and fits no parity, row or column rule, so the original was probably per-cell random. A deterministic hash was chosen so gate C stays stable across runtimes. `DECISIONS.md` 2026-08-04 item 6.
- **Falsifier:** two frames of the **same** maze — identical tones prove a deterministic function (then derivable); different tones prove runtime randomness (and the hash is a fair stand-in). `docs/standards/VISUAL-EVIDENCE-WANTED.md` #8a.
- **Dependents:** `src/mazecreator/MazeRenderer.as`; the gate C baseline.
- **Blast radius:** one function and one baseline.
- **Seam:** `src/mazecreator/MazeRenderer.as`

### F-11 — SAJAX library is a lightly modified Sajax 0.12
- **Layer:** wire format
- **Grade:** B
- **Status:** pinned
- **Evidence:** the wrapper emission template was recovered byte-exact from captures, including tab/space quirks, and diffed against stock `sajax_get_one_stub()`. `DECISIONS.md` 2026-08-03 "SAJAX verdict".
- **Falsifier:** an era capture whose wrapper bytes differ from the pinned template, or a stock release that matches byte-exactly and moves the verdict to unmodified.
- **Dependents:** `srv/index.php` SAJAX block and per-route export lists; `archive-cleaned/classification/*.tsv` (`template-edit` windows).
- **Blast radius:** the dispatcher, the error format, and every route's gate F mask.
- **Seam:** `srv/index.php` SAJAX region

### F-12 — Authentication is a deliberate divergence: POST + `password_hash`
- **Layer:** HTTP surface
- **Grade:** scope
- **Status:** pinned
- **Evidence:** the original ran SAJAX auth over GET, which is why real credentials are permanently in the public CDX index. Reproducing it would reproduce the leak. Guide §6.4; `SECURITY.md`; `tests/test_auth_divergence.py`.
- **Falsifier:** none. This is the one place fidelity is deliberately refused, and it must never be "corrected".
- **Dependents:** `srv/includes/getUserAuthentication.php`; `SECURITY.md`; `docs/standards/DIVERGENCES-SERVED.md`.
- **Blast radius:** none downstream — logged-in rendering is not reconstructed.
- **Seam:** `srv/includes/getUserAuthentication.php`

### F-13 — Gate F compares in line mode with difflib projection, anchor mode for loops
- **Layer:** build/runtime
- **Grade:** B
- **Status:** pinned
- **Evidence:** era captures of one route differ in line count, so `GATE_F_SPEC.md`'s positional line-drop comparator could not work unchanged. `DECISIONS.md` 2026-08-03 "gate F mask model".
- **Falsifier:** a route where difflib alignment demonstrably mis-projects a mask range, producing a false pass.
- **Dependents:** `tests/test_render_diff.py`; `tests/maskcheck.py`; every mask under `archive-cleaned/classification/`.
- **Blast radius:** every gate F verdict already recorded.
- **Seam:** `tests/test_render_diff.py`

---

## Open questions not yet foundations

Things that will become rows the moment something depends on them. Listed so
they are not silently decided:

* **Three maze slots per tank.** `docs/evidence/manual-evidence/C-maze-slots-and-save-flow.md`
  reports three; the corpus only ever observed `s=1`. Blocks any garage work.
* **In-round floor tone.** Reported as a single flat tone, not the editor's
  two-tone mix — a different surface from F-10, and currently unmodelled.
* **The chat system.** Reported in footage; appears in no held byte, no ledger
  row and no want-list entry. Nothing depends on it yet, and nothing should
  until it is evidenced.
