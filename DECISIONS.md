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
