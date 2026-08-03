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

## 2026-08-03 — docker stack VALIDATED; both deferrals closed
Docker became available. mysql:5.5 executed all six init files with zero
errors; row counts exact (mazes 842, threads 467, replies 228,316, news 224,
users 10, accessories 21, achievements 8); the notFound maze slot is
correctly absent; byte round-trips green for maze data and for non-ASCII
forum text (© U+00A9, soft hyphen U+00AD) read back with
--default-character-set=utf8. One import bug found and fixed BEFORE first
import: the 5.5 entrypoint client defaults to latin1, which would have
double-encoded the UTF-8 seed bytes — every generated file now opens with
`SET NAMES utf8;` (seed/common.py). php:5.6 image builds; serves O bytes
byte-identically (styles.css sha256 match over HTTP); every probed stub dies
with 501; php bound 127.0.0.1:8056 only, mysql has no host port. Supersedes
the two "docker unvalidated/deferred" entries above.

## 2026-08-03 — archive-cleaned/ is a locked manifest, not a byte-copy tree
Guide §6.1a step 1 wants cleaned captures as O ground truth. Survey of all
628 warc-bodies: zero gzip bodies, zero Wayback markers — every Common Crawl
body is already exactly what the server sent. Copying ~150 MB of them into
git would duplicate the archive to say "no transform needed"; instead
archive-cleaned/MANIFEST.tsv sha256-locks all 411 in-scope captures at their
archive paths (Gate C1 re-verifies), and a physical file appears under
archive-cleaned/ only where bytes must actually change (so far: none).
Scope: classic era (<= 2020-12-04), hosts tanktrouble.com/www, routes
root/game/garage/news/forum/lab/shop + embed.php + infirmary + statistics.

## 2026-08-03 — classic captures are PageSpeed-free; depagespeed/ empty
Guide §6.1a step 2 (un-do PageSpeed) does not bite the classic site: every
capture containing `.pagespeed.` is either beta.tanktrouble.com (HTML5
client) or tanktrouble.com from 2021+ (modern SPA era) — the classic PHP
pages were never served through PageSpeed in anything we hold.
tools/clean_captures.py keeps a verified inverter (jc-bundle splitting, URL
de-mangling) for the day a PageSpeed-bearing classic capture surfaces, and
the manifest counts artefacts per file (all zeros today). The §6.1a example
bundle came from the beta client tree, which is out of classic scope.

## 2026-08-03 — region classification draft (guide 6.1a step 3)
tools/classify_regions.py diffs every era capture per route against the
latest era capture, line-level. Line static-rates: root 93%, game 93%,
garage 96%, news 93%, forum 95%, lab 92%, shop 94% — the six routes are
overwhelmingly literal template, strongly de-renderable. embed.php is 18%
static (its body is per-request embed-config JS + RELEASE-tag cache-busted
asset URLs — correctly dynamic); infirmary is 100% static across its 2 era
captures. Outputs under archive-cleaned/classification/ are the DRAFT masks
for gate F; milestone 3 must annotate every dynamic region before writing
route PHP (tests/GATE_F_SPEC.md). Line granularity chosen because classic
captures are artifact-free and the originals keep one statement per line
almost everywhere; byte-level refinement is milestone-3 work.

## 2026-08-03 — Ruffle spike verdict (guide §9 step 2, run before step 8)
Headless-Chromium harness (oracle/ruffle-spike/) ran the ORIGINAL
signUpTankDesign13 bytes under Ruffle 0.4.1:
* getURL("javascript:") SWF-to-page bridge WORKS — paint-can clicks wrote
  0xff00/0x80ff into the page's signup* inputs, original page contract.
* SetVariable/GetVariable page-to-SWF API is ABSENT from Ruffle's player
  element — and the recovered garage JS drives mazeCreator EXCLUSIVELY
  through SetVariable. Original page JS + rebuilt SWF cannot work as-is
  under Ruffle; design options recorded in oracle/DIVERGENCES.md, decision
  deferred to the mazeCreator step. The projector half of gate C is not yet
  runnable: no Flash projector binary held; gap recorded.

## 2026-08-03 — §10.3 settled: single dispatcher, no per-route files
74,165-row CDX scan: zero hits for garage.php / news.php / forum.php /
shop.php / lab.php / game.php (or .html variants) on any tanktrouble host.
Combined with the ?query route evidence, index.php as the single dispatcher
is confirmed, not assumed. Remaining §10 items: charset settled at
milestone 2 (utf8); db.php rename and the save-endpoint constant stay open
until their milestone-3 files are first touched.

## 2026-08-03 — DB credentials reach PHP via TT_DB_* environment
Milestone-3 endpoints need a DB connection. docker-compose.yml now creates a
dedicated mysql user (MYSQL_USER/MYSQL_PASSWORD from .env — PHP never holds
root) and passes TT_DB_HOST/NAME/USER/PASSWORD into the php container's
environment; the include reads them with getenv(). Rejected: hard-coded
credentials in PHP (gate D credscan exists precisely to forbid this; the
original's config was never captured, so nothing is lost by diverging).
Environment plumbing is infrastructure, invisible on the wire — tier
concerns do not attach. Reversible: compose edit.

## 2026-08-03 — §10.4 settled: db include renamed rebuild-db.php
Tier: M3, DO NOT PROMOTE. The original surely had some shared DB include;
neither its name nor its contents were ever observable. Renamed
srv/includes/db.php -> srv/includes/rebuild-db.php: the hyphen and the word
"rebuild" make it impossible to mistake for a recovered period file, which
is exactly guide §10.4's ask. Rejected: keeping db.php (plausibility would
harden into false provenance); config.php (equally plausible-period).
Invented constants of later phases (e.g. the save-endpoint name) will live
here so no second invented file is ever needed. Reversible: one
require_once string per endpoint. Body stays a 501 stub until the first
consumer (loadMaze.php) lands with gate B as its verified_by — gate D
requires unverified M* stubs to die 501.

## 2026-08-03 — mazes remodel: the corpus is a time series, one row per
## (author, slot), latest capture wins  [SUPERSEDES "maze seed keyed by
## corpus filename code", 2026-08-03]
Three findings force this (all re-verified against the raw corpus today):
1. The filename CODE is the first 12 chars of the Wayback sha1-base32
   digest of the response body (matches 843/843) — a CAPTURE identity, not
   a "userName request code" as the superseded entry said. And per
   archive/cdx-passes/F_loadmaze200.json, 842/843 bodies answered anonymous
   `c=<random>` requests — no archived response was produced by a real
   userName query.
2. The true wire format is r=<base64(shuffle("t=&n=&d=&s="))> — `s` sits
   INSIDE the base64 (all 842 payloads have exactly keys {t,n,d,s}; the
   guide §6.2 comment `r=<b64>&s=<slot>` does not match the corpus), and
   the inner pair order is a per-request server shuffle: all 24
   permutations occur. The old seed silently discarded s and the (random,
   unreproducible) order.
3. The corpus spans fetches 2017-01..2019-04: 842 bodies -> 744 distinct
   contents -> 672 distinct (author, slot) states; 70 authors were
   re-captured with DIFFERENT mazes that never coexisted in the live DB.
Row model chosen: one row per (author, slot), latest fetchts wins — the DB
is one site snapshot, matching the notFound precedent (absence of a row is
also a dated observation). Superseded captures and per-row witnesses live
in the 10-mazes.sql trailer; the corpus remains the O record. s observed
only as 1; emitted from the row, not hardcoded. unquote_plus dropped: zero
% and zero + across all 842 payloads (fields are raw bytes, not
urlencoded); the seed now FAILS if either char ever appears, so the
encoding question reopens loudly instead of silently mangling.
Rejected: digest-keyed rows (models the corpus, not the site; 98
duplicate-content rows); all-744-contents rows (co-hosts states that
provably never coexisted); per-capture snapshots (mutates seed per test).
Consequence for gate B: byte-identical replay of archived bodies is
impossible by construction (random shuffle + random selection); the gate
compares canonical field content plus byte-exact notFound — recorded in
the gate-B entry when tests/test_loadmaze_replay.py lands.

## 2026-08-03 — mazes.author is VARBINARY(16): byte-exact key
First import of the remodel failed: MySQL VARCHAR PKs compare PAD-SPACE and
utf8_general_ci compares case-insensitively, and the corpus holds 12
byte-distinct author pairs that collide under those semantics — 10 case
pairs ('Cheesed'/'cheesed' …) and 2 trailing-space pairs ('b11'/'b11 ',
'devo'/'devo '). Whether these were one live user or two is unknowable from
the wire; merging them would invent identity and silently drop 12 observed
states. VARBINARY (NO PAD, binary compare) keeps all 672. All corpus
authors are pure ASCII, so no charset is lost. Consequence: the userName
lookup in loadMaze.php becomes byte-exact — the original's case handling
was never observable (M3 detail, noted in that file's @caveat). Rejected:
utf8_bin collation (still PAD SPACE — trailing-space pairs still collide);
merging under ci semantics (invents identity).

## 2026-08-03 — gate B redesigned: content replay, not byte replay
Guide §7.2 asks for byte-identical replay 843/843. The corpus proves that
impossible (see the mazes-remodel entry): per-request response shuffle +
random selection for 842/843 bodies. tests/test_loadmaze_replay.py instead
gates every invariant the corpus DOES pin down:
* notFound body byte-identical (r=bm90Rm91bmQ9dHJ1ZQ==) for replays of the
  archived userName=undefined request shape;
* outer `r=<base64>` format exact (regex + canonical-padding round-trip);
* every sampled response's decoded field content equals a seeded winner
  state, and coupon-collector sampling must surface ALL 672 states (cap
  25,000 requests; expected ≈4.8k; P(miss) < 1e-12);
* response key set exactly {t,n,d,s};
* malformed/unknown input dies a loud 400 (guide 6.2 rule 3);
* a clearly-labelled NON-GATE sanity test exercises the DEDUCED
  userName->author lookup (never archived).
Implementation choices in loadMaze.php, all caveated in-file: shuffle
mirrors the client's naive swap-shuffle; ORDER BY RAND() selection; q read
from QUERY_STRING+rawurldecode (archived requests are raw base64 or %3D —
$_GET would corrupt a base64 '+' into space); lenient base64_decode like
the client's decoder. The 13-row G7SVMWKCBAA3 anomaly (2018-06-03/04,
stable unshuffled body, never archived) is explicitly out of scope.

## 2026-08-03 — live gates FAIL without the stack; offline runs are explicit
New pytest marker `live` (gates B, later F) with a session `stack` fixture
that fetches includes/styles.css over 127.0.0.1:8056 and sha256-checks it
against the ledger before any live test runs. No stack -> pytest.fail with
instructions, never skip — same philosophy as archive_root (a silently
skipped gate is a green lie). Deliberate offline runs say so on the command
line: pytest -m "not live" (gates A/D/S/C1 remain docker-free). Full suite
green with the stack up is the milestone-3 definition of green.

## 2026-08-03 — gate F mask model (vocabulary, sidecars, comparator)
Classification TSVs gain annotation (5th col) + region_sha (6th col,
sha256[:12] of the region's reference lines). Owned by
tools/annotate_regions.py from now on; regeneration re-attaches annotations
by (route, region_sha) and surfaces changed regions as unannotated — that
is the safety property (tests/test_masks.py proves byte-stability).
Vocabulary: echo:$name [re=regex, exactly one capture group, single-line
regions only], loop:name, template-edit:FROM[..TO] (YYYYMMDD, inclusive),
per-request:what, ad-block, needs-split:why. ';'-separated multi-annots,
';' forbidden inside details, ' re=' cells are single-annotation. Empty or
needs-split blocks gate F for the whole route (GATE_F_SPEC rule).
template-edit is SIDE-DEPENDENT: capture side gated only inside the window
(the ref bytes were live then), render side always gated (reconstruction
emits era-final text). Refines GATE_F_SPEC's positional line-drop into
difflib projection (era captures differ in line count): gated ref lines
must survive byte-identical, masked regions absorb replace/delete, inserts
must touch a masked region. Content REMOVED before the era-final reference
has no ref lines to mask, so <route>-removed.tsv sidecars record
(ref position, validity window, max observed lines, name); capture-side
inserts matching a row are legal, the render side never gets the
allowance. Sidecars are position-keyed to the current reference — if the
reference changes they fail loudly and must be re-derived.

## 2026-08-03 — annotation pass (all 217 regions, method + findings)
Method: per-region variant dump across every era capture (annotate_regions
--variants); regions whose byte-forms partition the timeline monotonically
(no same-day clash, ref form last, form count small) are hand-edited
template text -> template-edit:<first ts of ref form>; a form-count guard
(forms > max(4, captures/3)) rejects always-varying regions that look
trivially monotonic when every capture differs (top10 tables — this guard
caught a real false positive on garage). 187 regions auto-classified this
way, 30 classified manually, 0 needs-split. Manual classes: initCode
(random k=<int> pair, base64, differs across same-day captures) ->
echo:$initCode with full-line regex, validated against all 62 archived
root+game lines; live-player-stats, top10-rankings, latest-posters (forum),
random-tagline (root+game only; same-day captures differ -> per-request
rotation), seasonal-promo (halloween box byte-identical 20171119 AND
20181020, December calendar box tracks the DAY -> date-derived,
per-request per "never fake the clock"); news D009 -> loop:news-items (era
items accrete monotonically; DB as-of deferred to de-render). Ad
skyscrapers: lijit/adsbygoogle ROTATED per-request pre-20170429 (same-day
divergence) then froze -> template-edit:20170429 gates the stable era
byte-exact, masks the rotating tail; stronger than always-masked ad-block
(vocab kept for future use). Template history recovered: signUpTankDesign
13->17 between 20170330..20170429 (NOT 2017-01-24 as planning notes had
it), 17->18 between 20180722..20180814, so 2018-03-17 captures embed 17 —
resolves the planning-agent conflict. showShop wrapper still present in
the 20170330 root capture -> removal deploy in (20170330, 20170429], not
2017-03-30 itself. sendFeedback block still present 20180422 -> removed by
the (20180422, 20180523] deploy. Removed-block catalogue (72 rows):
sendFeedback feature, showShop wrapper + shop backer items + showShop_cb
js, lab statistics-link block (gone by 20171212) and v3.8c download line
(gone by 20170228), one 20180814 leading-blank capture artifact,
pre-cleanup whitespace-only lines.

## 2026-08-03 — gate F activation + split (offline/live)
Gate F runs in two halves. Offline (tests/test_masks.py, no docker): masks
hold against every era capture of every route — wrong windows or missed
dynamics fail here. Live (tests/test_render_diff.py): render vs era-final
reference with render-side modes; transitivity (ref==capture offline,
ref==render live) yields render==capture per capture without fetching once
per capture; the render is fetched once per DISTINCT era Host (www/apex)
instead. A route is active iff the serving file's ledger verified_by names
tests/test_render_diff.py (gate-D mechanics); claimed-but-blocked masks and
claimed-but-501 routes fail loudly; unclaimed routes stay gate-D 501s.
Bring-up: infirmary (srv/infirmary/index.html, O) — zero dynamic regions,
so the live half also byte-compares the raw body against the era-final
capture; its ledger row flips verified_by tests/test_assets.py ->
tests/test_render_diff.py (O bytes remain hash-locked by gate A
regardless). statistics has 0 era captures — never activatable in-era.

## 2026-08-03 — @O-begin fence grammar refinement
README's fence grammar named only a source file; a bare path cannot be
byte-verified. Fences now carry the span: /* @O-begin source=<path>
lines=<a>-<b> */ ?> ... <?php /* @O-end */. Body = file text between the
newline after ?> and the newline before the closing marker (PHP eats
exactly one newline after ?>, so emitted bytes equal fenced bytes).
tests/test_fenced_regions.py verifies byte-match + @contains declaration;
a synthetic self-test keeps the parser honest while zero fences exist.

## 2026-08-03 — de-render strategy: verbatim fences, not shared emitters
srv/index.php is generated (tools/derender.py) as: stock Sajax dispatcher +
reconstructed behaviour (initCode, tagline) + per-route page functions that
emit the route's ERA-FINAL capture bytes verbatim inside @O fences, split
only at reconstructed-behaviour lines (root/game: tagline line 113,
initCode line 202; other routes: one fence each; 11 fences total). The
plan's shared-emitter dedup was rejected: per-route shell bytes are not
provably identical across routes, and a shared chunk could name only one
route's capture as its fence source — duplication inside fences is
verbatim original bytes, zero invention, every byte source-named. The
generator is deterministic; regenerating after mask/archive changes is the
maintenance path (never hand-edit fenced bytes).

## 2026-08-03 — SAJAX verdict: lightly modified 0.12
Stock Sajax 0.12 obtained (thirdparty/sajax/FETCHED.md). Era pages embed
sajax_get_common_js output byte-matching stock for 149 lines except
sajax_remote_uri="/" (config) and four site-inserted sajax_debug lines;
wrapper stubs match stock's template modulo site whitespace edits
(two-tab indent, trailing tabs after the function name); header comment
"(c) copyright 2005 modernmethod, inc" matches. Version pinned: 0.12,
lightly modified. Consequences: dispatcher functions inherited verbatim
from stock (sajax_esc, sajax_get_js_repr, sajax_handle_client_request:
GET/POST rs, "-:<func> not callable" error form, "+:var res = ...; res;"
success form, GET-path anti-cache headers); the in-page JS+wrappers ship
inside the fenced verbatim bytes so no wrapper emitter is needed. The
export list starts EMPTY: every era SAJAX function answers the stock
"-:<func> not callable" — in-protocol and truthful (zero era SAJAX
response bodies are archived; fabricating "+:" replies would violate
guide 6.2 rule 3). Endpoints that get reconstructed (getScraps, milestone
3 phase D) register into the list one by one.

## 2026-08-03 — per-request and DB regions frozen at era-final bytes
live-player-stats, top10-rankings, forum latest-posters, seasonal-promo,
and the news item list render as the era-final capture bytes (inside the
fences). The originals were live DB values / date-derived content; no
archive evidence supports generating fresh values, so the reconstruction
freezes what the archive holds. Gate F masks these regions (or gates them
as template-edit windows), so the freeze is visible, not hidden. This
settles DECISIONS-16's anticipation for news: the news page de-renders as
literal HTML; the seeded news table remains data evidence, NOT wired into
rendering. Reconstructed live behaviour is limited to what output alone
proves: initCode (random k pair, naive swap-shuffle mirror of the client
port, base64 — only mechanism consistent with both observed permutations;
RNG/range unobservable, mt_rand(0, 2^31-1) chosen) and the tagline
rotation (pool = 10 texts observed across all root+game era captures,
uniform pick; pool completeness unknowable).

## 2026-08-03 — route resolution
Exact QUERY_STRING match: '' -> root page, the six evidenced route names ->
their pages, rs= handled by the dispatcher before page emission, anything
else -> loud 400 RECONSTRUCTION message. Archived request URLs evidence
exactly these shapes; original behaviour on other inputs (mixed keys,
unknown keys, cache-busted root) is unarchived and deliberately not
guessed.

## 2026-08-03 — index.php promoted M2 -> M1
Citation: gate F offline half (masks hold against every era capture of all
8 masked routes, ~205 captures), live half (root game garage news forum
lab shop rendered under every distinct era Host and diffed against
era-final references; infirmary byte-identical), fence verifier (11 @O
fences byte-match their named capture spans). Full suite 50 passed with
the stack up.

## 2026-08-03 — scrapyard reconstructed on both surfaces
Pre-era file surface: includes/getScrapyard.php answers exactly the two
archived query strings (?scraps, ?scraps&velocity — the requested keys
select the emitted fields, the only semantics consistent with both
pairs); state lives in the M3 scrapyard_state single-row table (schema
invention — original storage unobservable; velocity kept as the archived
decimal STRING to avoid float re-formatting). Gate:
tests/test_getscrapyard_replay.py injects each archived state via docker
exec (credentials never leave the mysql container), replays both bodies
byte-exact, restores the seed row. Tier stays M2: both observations are
pre-era; the era pages call SAJAX getScraps instead. That era surface is
reconstructed in index.php (export list = getScraps only): returns a JSON
string parsed by scrapyard.js (shape deduced from the O parse code —
scraps always, velocity iff the client asked; zero era bodies archived,
so the checks are labelled shape-only). Seed: scraps from 2016-01-26,
velocity from 2015-09-28, labelled arbitrary.

## 2026-08-03 — updateGameStatistics.php stays 501 (and explains the
## loadMaze 13-row anomaly)
New digest pass archive/cdx-passes/N_updategamestatistics_digest.json
(2,578 rows, fetched 2026-08-03): 2,415 status-200 rows carry 495 DISTINCT
digests with varying lengths — the response body varied per request, and
not one body is archived. Guide 6.2 rule 3: nothing to replay, nothing to
copy — the stub stays 501. Request side for the record: ?q=<base64> with
shuffled pairs (players=N, rounds=N, tanksSc…), same wire scheme as
loadMaze. Bonus finding: the second-most-common digest
(G7SVMWKCBAA3EZSAFHYBE3AM5PILZ3NX, 636 rows 2013-2020) is EXACTLY the
digest of the 13 anomalous 2018-06 loadMaze CDX rows scoped out in the
gate-B redesign — the anomaly is Wayback attributing a common
updateGameStatistics response body to loadMaze.php URLs, not a lost
loadMaze behaviour. The gate-B scope-out stands, now with a cause.

## 2026-08-03 — endpoints that stay 501, as scope not neglect
achievement.php: zero CDX rows of any kind — no observed response ever.
getimage.php: all 99 CDX 200s are beta.tanktrouble.com/2021+ (the next
site generation); the classic host has zero era rows — the classic file's
behaviour is unobservable. Directory-index stubs (faq ios privacy like
statistics spreadTheWord tellAFriendMail tankRanks theLabReport): no
captured bodies. All remain loud 501 stubs through milestone 3.

## 2026-08-03 — auth divergence implemented; logged-in rendering is a boundary
getUserAuthentication.php gets its guide-6.4 body: POST-only (GET -> 405
with the divergence explanation), bcrypt password_verify against the ten
synthetic testuser rows, minimal PHP session, invented response format
("ok"/"denied" — no original response was ever archived), M3 BY CHOICE
with a never-promote note. users.password_sha256 placeholder becomes
password_hash VARCHAR(60); seeds are bcrypt produced once inside the
stack's own php:5.6 container with PRNG-fixed salts so the seed file
stays byte-stable; the per-user secrets derive from the same fixed-seed
PRNG (seed_users.secrets()), which is how tests/test_auth_divergence.py
logs in without any plaintext secret existing in the repo. BOUNDARY:
logged-in page rendering is NOT reconstructed — near-zero logged-in
captures exist; anything beyond "session variable set" would be invention.
TLS termination is out of scope for the 127.0.0.1-only stack.

## 2026-08-03 — saveMaze constant + write-side boundary (milestone 3 ends here)
TT_SAVE_MAZE_ENDPOINT = 'saveMaze.php' lands in includes/rebuild-db.php
(guide 3.3's own worked example of an invented name), with a `pending`
ledger row and NO file — the caller (mazeCreator SWF, guide 6.5) is lost
and no request for the endpoint was ever archived; the mazeCreator
milestone owns both. Write-side SAJAX functions (login, signup, vote,
updateTank, post/moderation set, sendFeedback, ...) stay OUT of the export
list and answer the stock "-:<func> not callable": zero era request or
response bodies are archived for any of them, and a write path that
fabricates success would corrupt the seeded archive it exists to protect
(guide 6.3). Milestone 3's write-side surface is: loadMaze (M1, gate B),
getScraps (shape-only), getScrapyard replay (M2), auth divergence (M3) —
everything else loud, in-protocol errors.

## 2026-08-03 — mazeCreator control channel: dual-channel SWF, page JS untouched
Tier: M2 (editor SWF, phase 2), O (page contract unchanged).
The rebuilt editor implements BOTH control routes: (a)
ExternalInterface.addCallback("SetVariable"/"GetVariable"), so Ruffle's
player element answers the ORIGINAL page calls verbatim — proven by
oracle/editor-spike (results 2026-08-03, all four verdicts true); and (b)
_root variable watch, so native SetVariable works under real Flash
(projector 32.0.0.465, oracle/projector/). Page-side JS stays the O bytes —
zero divergence. Names arriving with a "_root." prefix through route (a)
are resolved by stripping the prefix, reproducing the native plugin's
path resolution.
Header facts pinned by measurement: SWF version 8, 688x400, 25 fps —
sibling paint editors and the game all read version=8 fps=25
(tools/swf_header.py), stage from the O embed line (srv/index.php:3617),
25fps corroborated by the O comment (srv/index.php:3637).
Toolchain: MTASC 1.14 (thirdparty/mtasc/FETCHED.md) — era-plausible open
AS2 compiler; the ORIGINAL was authored in the Flash IDE, so the rebuilt
SWF is M2 regardless of compiler.
Rejected: page-side adapter shim (needless — (a) answers the original call
shape); HTML5 port for the editor (PORT-FEASIBILITY.md remains the fallback
if Ruffle regresses).
Reversible: yes — channel (b) alone suffices for any real-Flash runtime.
Supersedes: the "decision deferred" options list in oracle/DIVERGENCES.md
2026-08-03 SetVariable spike entry.
