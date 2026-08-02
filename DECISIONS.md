# DECISIONS — append-only

Every judgement call gets an entry (guide §3.3). Newest at the bottom. Never
edit an existing entry; supersede it.

## 2026-08-02 — target era is 2017–2018
User decision. Where held captures of one path differ across eras, the copy
that was live 2017-2018 wins. Reversible: yes (re-run tools/resolve_era.py
with a different window, re-copy).

## 2026-08-02 — era method (tools/resolve_era.py)
Methods, in order: identical (all candidates same sha256) →
sha1-digest-match (candidate's base32-SHA1 appears in a 2017-2018 CDX row;
on a mid-era content change the longest in-era presence wins) →
digest-run-continuity → nearest-capture (tier O?). Single-capture files stay
tier O — bytes are authentic; era fit is recorded in notes, not by demotion.
Per-file outcomes: tools/era_choices.tsv (committed, reviewed).
Notable outcomes: styles.css 2017-2018 window served ONLY the 1,276 b digest
(83 rows) — the 8,053 b 2010 classic stylesheet was already gone; the
"gutted" copy is era-correct. swfobject.js changed mid-era (39 rows old
digest vs 44 new); the 9,328 b build chosen. Tank.swf window shows 3 distinct
digests; only the classic-host pull's digest is among the held bytes.

## 2026-08-02 — srv/ tree corrections vs guide §2
Adopted from HUNT-LOG §46 (all evidence-cited there):
* NO srv/RELEASE-*/ — proven cache-busting rewrite prefix, not a directory.
* ADD srv/Assets/{Tank,GameTank,Crate,Laika}.swf — web root, capital A.
* ADD srv/robots.txt (http-observed, CC body held) and srv/feedback.php stub
  (http-observed, referenced in 2018 bodies).
* signUpTankDesign04StandardColours.swf IS held (2012-06-01 200 capture);
  guide §2.2's never-captured listing is stale — copied, no known-lost row.
* theLabReport/ layout is FLAT (The_Lab_Report_volume_N_issue_M.pdf,
  CDX-verified, volumes to 18); guide §2's vol{1..14}/ shape not observed —
  single theLabReport/index.php stub. The PDFs are still-fetchable and
  deferred; no rows yet.
* logIn.php: known-lost row (name proven via 404 by 2008; pre-era).
* ads.txt: known-lost row (first capture 2023-06, outside era, no body held).

## 2026-08-02 — images scope
srv/images/ = the 122-file recovered set (archive/classic-ui-images/, incl.
shop/). The other ~214 /images/ paths held elsewhere in the archive and the
assets/images/{tankInfo,lobby}/ tree are DEFERRED follow-ups, not milestone-1
scope. User decision.

## 2026-08-02 — TankTrouble_v3.6e.swf is O? via zip extraction
Bare SWF exists only inside the held O zip. Bytes authentic, served-path
placement inferred → tier O?. Removed from the known-lost list. v3.5/v3.6
inner SWFs are NOT extracted (guide tree places only 3.6c/3.6e); their
known-lost rows note "promotion candidate".

## 2026-08-02 — row vocabulary and exit criterion
Tier vocabulary adds `pending` (path evidenced, rebuild scheduled) beside
`known-lost` (no bytes, no plan). Both are rows without files. Guide §4's
"LEDGER row count == srv/ file count" is refined to set equality:
{row.path : tier ∉ {known-lost, pending}} == files under srv/ (excluding
*.provenance sidecars). Enforced by tests/test_assets.py both directions.

## 2026-08-02 — provenance carriers
O files get NO injected header (that would edit original bytes) — their
provenance is the ledger row; verified_by = tests/test_assets.py. M* text
files carry the §3.2 header. M* binaries (none yet) get a .provenance
sidecar. O binaries deliberately get no sidecar.

## 2026-08-02 — mixed provenance (de-render forward-compat)
A de-rendered page is verbatim original HTML inside written PHP; one scalar
tier cannot describe it. Convention fixed now: file tier = authorship tier;
verbatim-original regions fenced with /* @O-begin source=… */ … /* @O-end */;
header declares them in @contains. Step-6 harness must verify each fenced
region byte-matches its named source span. Grammar documented in README.md.

## 2026-08-02 — filenames that are conventions, not findings
infirmary/index.html: capture is of /infirmary/; the filename is inferred.
Directory stubs are index.php by convention (faq/ shop/ privacy/ like/
statistics/ spreadTheWord/ tellAFriendMail/ ios/ theLabReport/). game/ gets
only embed.php — the game route was index.php?game, not game/index.php.
db.php: name pure invention (guide §2.1), M3, DO NOT PROMOTE.

## 2026-08-02 — ledger regeneration window
tools/build_skeleton.py regenerates LEDGER.tsv (sorted by path) during
milestone 1. Append-only discipline begins at the skeleton-complete tag.
Ledger rows are metadata, not archive bytes and not code — each commit
carries its files plus their rows (guide §3.1's own example pairs them).

## 2026-08-02 — stub commits batched by tier
Guide §3.4 wants one commit per file. The 21 M2 skeleton stubs are a single
template render; per-file commits would add 21 identical messages without
adding evidence. Batched by tier (M1 / M2 / M3) — the tier boundary, which
is what §3.4 protects, stays intact. User-approved deviation.

## 2026-08-02 — docker skeleton unvalidated
No docker runtime on the build machine. Compose file and Dockerfile are
written per guide §6.3 (127.0.0.1 only, no MySQL host port) but have never
been run. Validate before milestone 2 seeding.

## 2026-08-02 — uploadimage.php observed post-era
Only CDX capture is 2021. Kept in the tree (guide §2 lists it) with the
caveat in its stub evidence line.

## 2026-08-03 — tree corrections from DEDUCE.md §2.2 (CDX-reverified here)
DEDUCE.md and PORT-FEASIBILITY.md landed in the repo root; their filesystem
claims were spot-checked against the raw CDX before adoption.
* srv/game/embed.php REMOVED. Its sole CDX row is
  `https://tanktrouble.com/?game/embed.php` — a query string on `/`, not a
  path. Guide §2's "(obs)" grading is wrong; the real file is top-level
  srv/embed.php (170 CDX rows), already present. Supersedes the milestone-1
  decision that gave game/ only embed.php.
* srv/tankRanks/index.php ADDED (M2 stub). /tankRanks/ has 86 200s
  (2010-2015, zero era CDX rows) BUT 2017-2018 ?lab captures ship
  `window.open('tankRanks',...)` — the live era site still linked it, so the
  era tree includes it. Absence from era CDX has a mechanism: popup page,
  nothing crawled it.
* /verification/, /facebook/, /kickstarterFAQ/ NOT added: all captures
  pre-era, zero era CDX rows, zero references in 206 era-captured bodies.
  DEDUCE.md documents the all-years classic filesystem; srv/ is era-scoped.
  Revisit if era evidence appears.

## 2026-08-03 — milestone-2 DDL choices are M3 (guide §5.2)
Engine MyISAM (period default at the site's 2008 birth; matches mysql_*-era
PHP), charset utf8 (=utf8mb3) collation utf8_general_ci. Basis: full-corpus
scan found 44,739 BMP non-ASCII chars and ZERO astral chars, so utf8mb3 is
lossless for everything held; latin1 would mangle 301 of 468 threads.
Column types/widths sized from observed maxima (header 50→VARCHAR(64),
message 5,755→TEXT, creator ids ≤8 chars→VARCHAR(16), maze data 275→
VARCHAR(512)). forum `banned` was observed ONLY as null — TINYINT(1) NULL is
a pure guess. None of this DDL is recovered; do not promote.

## 2026-08-03 — news is verbatim blobs; the page was hand-maintained
One ?news capture mixes ≥3 markup generations ("news4 standard" collapsed,
"news standard"+header/content pretty-printed, "text medium" boxed), with
drifting indentation, a duplicated back-to-back anchor (26-01-2009), and
titles live-edited across captures (28-04-2017 lost "- 7 Days Left to
Vote"). A single template looping over field data cannot emit that; the page
was hand-edited HTML or stored per-item HTML blobs — which, is NOT
observable. Consequence: guide §5's "news: schema M1" is overclaimed —
seeded as byte-verbatim per-item slices (data O) keyed (posted, seq), schema
M2. Anchor dates collide (03-10-2016 ×2), so the site's own permalink is not
a unique key. The social-share widget is per-item template output, present
only in later captures; blobs keep the latest capture's state and the
importer records every cross-capture divergence in the SQL trailer.
Milestone-3 de-render may supersede the table with literal HTML; the blobs
transfer unchanged.

## 2026-08-03 — forum seed: what is and is not a row
Fetch-era fields `html` (2026 client rendering) and `time` (fetch clock) are
NOT seeded; `threadMeta` (a captured listing page, redundant with the thread
objects) is skipped. thread_467915.json is an archived fetch-miss — no
thread payload came back — so it gets NO row; fabricating one would be M3
data in an O table. Actual counts: 467 threads + 228,316 replies from 468
archived thread files (guide §5's 468/225,438 was point-in-time). The corpus
includes post-classic posts (created up to 2026): ALL are seeded — the data
is O and era-scoping is a render-time concern for gate F, not a seed-time
truncation. creator/coCreator/moderatedBy are modern numeric id strings kept
as display metadata with deliberately no FK to users (guide §5.1).

## 2026-08-03 — maze seed keyed by corpus filename code
Archived loadMaze bodies hold only `r=`; the userName request key survives
only in the corpus filename `<fetchts>_<CODE>.txt`. MazeDataFetcher.as shows
loadMaze queries by userName (one maze slot per user), so mazes.user_code =
that code. The one notFound=true payload proves its slot was EMPTY: gate-B
replay must reproduce it by the row's absence, so it is recorded in the SQL
trailer, never as a row.

## 2026-08-03 — accessories seed = the developer's DEBUG catalogue
The live accessory catalogue (initCode tal/baral/fal/bacal, "id-toolbox,"
pairs) flowed only to logged-in garages and was never captured; era signup
embeds carry NO initCode. The only recoverable listing is the DEBUG block in
the signUpTankDesign18 decompile — seeded as-is, M2, clearly labelled. The
same applies to achievements: only ids {28,29,30,31,32,34,35,36} appear at
v4.0 call sites; the numbering proves 1–27 and 33 existed, but unobserved
means no rows.

## 2026-08-03 — seed outputs carry provenance in-file, not in LEDGER.tsv
LEDGER.tsv stays srv/-scoped (its rule is "every file in srv/ has a row").
Generated docker/mysql/init/*.sql files carry a machine-parseable
`-- @provenance data <tier> / schema <tier>` header instead, enforced by
tests/test_seed.py, and reproducibility is enforced by byte-identical
regeneration (forum exempted from the re-run for cost; covered by count
checks). Seeded O data (mazes/forum/news SQL) is credscan-allowlisted by
path — user post text may contain anything and must not be edited.

## 2026-08-03 — milestone-2 seeding done file-level; live DB deferred
Still no docker runtime on this machine. The milestone-1 decision said
"validate before milestone 2 seeding"; that validation remains impossible
here, so milestone 2 ships deterministic, content-tested SQL files and the
docker-level import (mysql:5.5 actually executing them) is the FIRST step
whenever a docker runtime appears. Until then the DDL has never been parsed
by a real MySQL 5.5. Partially supersedes the milestone-1 docker entry.
