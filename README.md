<h1 align="center">TankTrouble</h1>

<p align="center">
  <em>tanktrouble.com as it ran — PHP 5.6, MySQL, Flash.</em><br>
  <sub>Six query routes, one <code>index.php</code>, and a garage full of tanks.</sub>
</p>

<p align="center">
  <sub><a href="#the-reconstruction">↓ this is a reconstruction — how it was rebuilt is the second half</a></sub>
</p>

---

## The site

### Routes

The whole site is one file. `index.php` reads `QUERY_STRING` and dispatches —
no rewrite rules, no path routing.

| | |
|---|---|
| `/` | front page — the game stage, the Scrapyard counter, news teasers |
| `/?game` | the game, full width |
| `/?garage` | your tank: paint, accessories, mazes, achievements |
| `/?news` | The Lab Report and site news |
| `/?forum` | the Tank Owner's Forum |
| `/?lab` | Laika's lab |
| `/?shop` | merchandise |

Anything else is not a page. Directory listing is off site-wide, and
`/includes/` answers `403`.

### The document root

```
/
├── index.php ····················· all six routes + the SAJAX dispatcher
├── embed.php ····················· the embeddable stage for other sites
├── content.php · getimage.php ···· media delivery
├── changePassword.php
├── sendRequest.php · feedback.php
├── uploadimage.php
├── robots.txt
│
├── Assets/ ······················· runtime-shared Flash libraries
│   └── Tank.swf · GameTank.swf · Crate.swf · Laika.swf
│
├── includes/ ····················· 403 to the browser; the server's own shelf
│   ├── TankTrouble_v4.0.swf ······ the game
│   ├── TankTrouble_v4.03.swf · v3.6c · v3.6e ··· older builds, still served
│   ├── mazeCreator_v0.3.swf ······ the maze editor
│   ├── signUpTankDesign*.swf ····· the tank-designer, five generations
│   ├── scrapyard06/10/11.swf · laika02.swf · loggedInTank06.swf
│   ├── ima3_preloader_1.5.swf
│   │
│   ├── loadMaze.php · saveMaze.php ············ the maze store
│   ├── getScrapyard.php ······················· the scrap counter
│   ├── getUserAuthentication.php · achievement.php
│   ├── updateGameStatistics.php
│   │
│   ├── mootools-release-1.11.js ··············· the UI framework
│   ├── swfobject.js · embed.js · scrapyard.js · phaser.min.js
│   ├── styles.css · main.css · boxStyles.css
│   ├── forumStyles.css · newsStyles.css · news.css · shopStyles.css
│   ├── c64.ttf · c64.woff · c64.eot ·········· the headline face
│   └── TTTradingCards*.pdf ··················· four printable card sheets
│
├── images/ ······················· 254 files
│   ├── box* ·········· 49   the three-slice panel chrome, per colour
│   ├── bigBox* ······· 28   the wide variant
│   ├── tab* ·········· 16   the six nav tabs, selected and deselected
│   ├── menu* ·········· 8   the connectors between them
│   └── shop/ ········· 10   merchandise shots
│
├── faq/ · privacy/ · ios/ · like/
├── shop/ · statistics/ · tankRanks/
├── spreadTheWord/ ················ banners to paste on your own site
├── tellAFriendMail/
├── theLabReport/ ················· the newsletter archive
└── infirmary/ ···················· index.html, hand-copied from index.php
```

### Talking to the server

Two channels, both on `index.php`.

**SAJAX**, for the page:

```
GET /?rs=<function>&rst=&rsrnd=<nonce>&rsargs[]=<arg>
```

The export list is emitted into every page, so the browser knows what it may
call. Anything not on it answers `-:<func> not callable`.

**Pair messages**, for the Flash client — base64 of shuffled `key=value` pairs,
in and out:

```
GET  /includes/loadMaze.php?q=<base64>      →  r=<base64 of t,n,d,s>
POST /includes/saveMaze.php                 →  r=<base64>
```

A maze travels as four fields: `t` its title, `n` its author, `d` the grid
itself, `s` which of the author's slots it sits in.

### Behind the login

The garage is where a tank belongs to someone: paint and accessories, three
maze slots with the editor behind them, achievements, ranks, and the forum
identity. Almost none of it was ever crawled — a logged-out spider sees the
front page and stops.

---

## The reconstruction

This repository rebuilds the site above from what survived: Wayback and Common
Crawl captures, decompiled SWFs, archived API responses, and 74,165 CDX rows.
The server's PHP is gone and always will be — a web server emits output, never
source.

> A reconstruction that cannot be told apart from the original is a forgery,
> not a preservation.

So every file says what it is. `LEDGER.tsv` carries one row per path with a
provenance tier:

| | |
|---|---|
| `O` | original bytes, verified against the era captures |
| `O?` | authentic bytes, era service inferred rather than proven |
| `M1` | written, and gated byte-for-byte against real captures |
| `M2` | written from constrained evidence — a decompiled reader, a measurement |
| `M3` | invented, and it says so in its own header |
| `known-lost` | referenced, unrecoverable, filed with the evidence that it is lost |

Original bytes are never edited. Written files carry a header naming their
evidence and their caveats. Judgement calls go into `DECISIONS.md`,
append-only — superseded, never rewritten.

### Run it

```bash
cd docker && docker compose up -d      # needs MYSQL_ROOT_PASSWORD in .env
```

→ **http://127.0.0.1:8056**. Unreconstructed endpoints answer `501` on purpose.

The stack is period-correct — PHP 5.6, MySQL 5.5, both long past end of life —
and binds `127.0.0.1` only. It must never face the internet (`SECURITY.md`).

Browsers no longer have Flash, so the game stage shows the browser's own
message. Nothing is substituted into the page; players belong in the pixel
oracle, not in the served bytes.

### Setup

The archive is a read-only junction, and needs no administrator rights:

```powershell
New-Item -ItemType Junction -Path "C:\Users\eth\websites\TankTrouble\archive" -Target "C:\Users\eth\websites\_NOT-PART-OF-MAIN-ARCHIVE_swf-recovered-2026-08-02"
```

Or set `TT_ARCHIVE_ROOT`. Without either, the gates **fail** — they never skip.

### Gates

```bash
python -m pytest tests/ -q                 # everything
python -m pytest tests/ -m "not live" -q   # offline only
```

| | |
|---|---|
| **A** | every `O` file's bytes match the ledger **and** the archive source |
| **B** | `loadMaze` reproduces every invariant the 843-payload corpus pins |
| **C** | the projector and Ruffle render the rebuilt SWF identically |
| **D** | everything labelled, everything announced, no stub returning `200` |
| **E** | every subresource a page requests resolves, or is a recorded loss |
| **F** | served HTML byte-matches every era capture, outside the masks |
| **S** | the seeded row counts match the corpora |

Gates A, D and F all walk `srv/` → ledger. Only **E** walks page → subresource,
which is why a byte-perfect page serving zero images once passed three of them
at once.

### Where everything is

| | |
|---|---|
| Working on it | [`CLAUDE.md`](CLAUDE.md) — the operating manual · [`docs/NOW.md`](docs/NOW.md) — the current target |
| The rules | [`docs/REBUILD-GUIDE.md`](docs/REBUILD-GUIDE.md) — read its superseded table first |
| What is structurally committed | [`docs/FOUNDATIONS.md`](docs/FOUNDATIONS.md) — with the falsifier for each |
| Done, active, blocked | [`docs/PROGRESS.md`](docs/PROGRESS.md) · plans in [`docs/plans/`](docs/plans/) |
| The standing disciplines | [`docs/standards/`](docs/standards/) |
| Commands, constants, vocabulary | [`docs/reference/`](docs/reference/) |
| How each claim was reached | [`DEDUCE.md`](DEDUCE.md) · [`docs/evidence/`](docs/evidence/) |
