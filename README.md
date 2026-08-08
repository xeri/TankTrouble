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

What a browser could reach in 2018, and what the pages of that year actually
asked for.

```
/
├── index.php ····················· all six routes + the SAJAX dispatcher
├── embed.php ····················· the embeddable stage for other sites
├── content.php · getimage.php ···· media delivery
├── changePassword.php · sendRequest.php · feedback.php · uploadimage.php
├── robots.txt
│
├── Assets/ ······················· runtime-shared libraries — the game pulls
│   └── Tank.swf · GameTank.swf ··· these itself, the page never names them
│       Crate.swf · Laika.swf
│
├── includes/ ····················· 403 to the browser; the server's own shelf
│   ├── TankTrouble_v4.0.swf ······ the game
│   ├── mazeCreator_v0.3.swf ······ the maze editor, opened from the garage
│   ├── signUpTankDesign18StandardColours.swf ··· the tank designer
│   ├── laika02.swf · loggedInTank06.swf ······· lab and header decoration
│   │
│   ├── loadMaze.php · saveMaze.php ············ the maze store
│   ├── getScrapyard.php ······················· the scrap counter
│   ├── getUserAuthentication.php · achievement.php
│   ├── updateGameStatistics.php
│   │
│   ├── mootools-release-1.11.js ··············· the UI framework
│   ├── swfobject.js ·········· embeds the game
│   ├── scrapyard.js ·········· drives the flip-counter
│   ├── embed.js · phaser.min.js
│   ├── styles.css · boxStyles.css ············ page and panel chrome
│   ├── forumStyles.css · newsStyles.css · shopStyles.css
│   ├── c64.eot · c64.woff · c64.ttf ·········· the headline face
│   └── TTTradingCards Series I · II · Special Anniversary  (.pdf)
│
├── images/ ······················· the whole UI, as flat files
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

### Where it differs from 2018

Every user-visible difference is written down **before** it ships, not after
someone notices, and anything visibly non-original announces itself on screen —
so no screenshot taken from this stack can be mistaken for evidence. Full log
with the undo for each: [`docs/standards/DIVERGENCES-SERVED.md`](docs/standards/DIVERGENCES-SERVED.md).

| | |
|---|---|
| **The game does not run** | Browsers have no Flash plugin, so the stage shows the browser's own message. Nothing is substituted and no shim is injected — a player would change what the page contains, and players are judged separately against the original SWF. |
| **The ad slots are empty** | Both `160×600` boxes keep their exact size; the layout never depended on an ad rendering. A dev overlay can fill them with labelled hatching, off by default. |
| **Live numbers are frozen** | Visit counters, online counts, top-ten rankings, forum latest-posters, the rotating tagline, seasonal promos — all held at the era-final capture's bytes. They are unrecoverable state, and plausible invented numbers would be the most dangerous kind of stub. |
| **The Scrapyard counter stops** | It creeps for about a minute, then pins. The seed row is frozen, so the original client re-derives a velocity of zero — the endpoint, the seed and the untouched client are all behaving exactly as written. |
| **Most SAJAX calls refuse** | Only reconstructed functions are exported; everything else answers the stock `not callable` error. Reject, never fake. |
| **Login is deliberately modern** | The original ran authentication over `GET`, which is why real credentials sit in the public archive index to this day. This rebuild uses `POST` and hashed passwords, verifies only synthetic accounts, and will never reproduce that. |
| **Nothing behind the login renders** | Almost no logged-in page was ever captured. Reconstructing the garage from nothing would be invention, so it is left undone rather than guessed. |

Two other things are **not** divergences, and are not to be "fixed":

- The older game builds and earlier tank-designer generations sit on the shelf
  under `includes/`. The 2018 server still answered for them; the 2018 pages
  just never asked. The map above shows what the pages asked for.
- Duplicated version strings across four files, and `infirmary/index.html`
  being a hand-copy rather than a template — those are the original's own
  faults, reproduced on purpose.

### Run it

```bash
cd docker && docker compose up -d      # needs MYSQL_ROOT_PASSWORD in .env
```

→ **http://127.0.0.1:8056**. Unreconstructed endpoints answer `501` on purpose.

The stack is period-correct — PHP 5.6, MySQL 5.5, both long past end of life —
and binds `127.0.0.1` only. It must never face the internet (`SECURITY.md`).

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
