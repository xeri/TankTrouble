# Asset discipline — what the page asks for is the work list

*Standing rule. Applies to every route, every milestone, every future edit.*

## The failure this exists to prevent

The 2018 front page was de-rendered to `srv/index.php` from a verbatim
CommonCrawl body. Gates A, D and F were green. The page rendered as a column
of unstyled text with three broken-image icons: no header bar, no panel
chrome, no store badges, no envelope.

193 assets the page requests did not exist under `srv/`. Not one had a ledger
row. Of the 112 files that *were* in `srv/images/`, **2** were referenced by
anything the site serves.

Nothing was lying. Every gate answered the question it was asked:

| Gate | Question | Why it stayed green |
|---|---|---|
| A | do the O rows' bytes match ledger and archive? | the rows that existed were all correct |
| D | does every file under `srv/` have a row? | the files that existed were all labelled |
| F | does the served HTML byte-match the capture? | it did — HTML says nothing about whether `images/` answers |

All three walk **srv → ledger**. None walks **page → subresource**. A
byte-perfect page serving zero images passes every one of them.

The cause was one line, `tools/build_skeleton.py`:

```python
IMAGES_DIR = "classic-ui-images"  # archive dir mirrored 1:1 to srv/images/
```

The asset set was whatever one archive folder happened to hold. It was then
recorded in the guide as "122 classic UI images, **complete**". That folder
turned out to be a different site generation — the page asks for
`logInToGetStarted.gif`, the folder holds `.jpg` and `.png` of that name.

## The rule

> **An asset inventory is derived from the site's own references, never from
> a directory listing. A reference that does not resolve is a defect until it
> is either satisfied or written into `LEDGER.tsv` as `known-lost` with the
> evidence that it is lost.**

Corollaries, each one paid for:

1. **Resolve URLs the way a browser does, not the way a path looks.**
   `srv/includes/scrapyard.js:104` loads `'images/scrapyardPlates.png'`.
   Read script-relative that is `/includes/images/scrapyardPlates.png`, and
   that is exactly how it entered the ledger: `known-lost`, "obs in CDX, 404
   only". The browser resolves a URL in a script string against the
   **document**, so the real request is `/images/scrapyardPlates.png` — which
   the era captured with status 200, 63 rows. The file was never lost. It was
   looked for at a path the site never used, and the Scrapyard counter stayed
   blank for it.

2. **`../` above the document root is not an error.** RFC 3986 §5.2.4 drops
   the excess segments, so `/?news` asking for `../images/x.png` really
   fetches `/images/x.png`. 19 references on this site rely on it. Treat them
   as normal references (`refgraph.Ref.clamped` records which they are).

3. **Bytes that exist are not automatically the right bytes.** Every
   candidate is accepted only against a 2017-2018 CDX digest for that exact
   served path. `flashpoint-gamezip` holds `menuBackground.jpg`, but its
   payload hashes to `UWJWLWANNYT4JMMKYB7D2ZLHPC3PPEMV` while the era window
   served `4IW4FYJLD4JDXRD3ZGKTDDASBR2FRJEL` on 53 rows. Copying it in would
   have looked like a fix and been a forgery.

4. **A basename match is not evidence.** `ia-items/extracted/images/
   DimitrisEmporium.png` is not proof of `/images/dimitrisEmporium.png` —
   different case, unrelated tree. Those get `weak-candidate-only` and a
   human decides; they never auto-promote.

5. **Not held is not the same as not recoverable.** A CDX row with a digest
   is a fetch target. 56 assets came back from Wayback and were accepted only
   because `base32(SHA1(payload))` equalled the digest the CDX row recorded.

6. **When the window captured nothing, argue in writing or not at all.**
   `images/tab{2,4,5}Select.jpg` have a CDX gap 2015-03 → 2019-09, so no
   automated rule can reach them, and until they were placed, clicking
   news/shop/forum collapsed the header tab. They ship as `O?` on a written
   timeline argument in `tools/asset_judgements.tsv` — the nav strip is
   versioned as a set; siblings date the strip-wide change to 20181218;
   tab3/tab6Select hold one digest through Dec 2019. A judgement row fires
   only if the fetched payload matches the digest the row names, its ceiling
   is `O?`, and the argument is copied verbatim into the ledger note so it
   can be attacked later. Never a quiet copy.

## The gate

`tests/test_subresources.py` (gate E) — offline, runs with A and D.

```
python -m pytest tests/test_subresources.py -q
```

* `test_every_referenced_subresource_resolves` — every reference either
  resolves under `srv/` or has a `known-lost` row. **This is the gate.**
* `test_dynamic_families_declared` — a name built at runtime
  (`'images/x' + tool + 'Select.jpg'`) cannot be read statically, so every
  such family in the source must enumerate its concrete names in
  `tests/gate_e_dynamic.tsv`. Six mazeCreator tool icons live there.
* `test_dynamic_decl_rows_are_live` — a declared family the source no longer
  contains is stale; delete the row.
* `test_known_lost_rows_have_no_file` — a `known-lost` row that gained a file
  is an unrecorded promotion.
* `test_subresources_serve_as_labelled` *(live)* — asks the stack. Windows
  matches paths case-insensitively and the php:5.6 container does not, so a
  file stored as `DimitrisEmporium.png` satisfies a request for
  `dimitrisEmporium.png` on the developer's disk and 404s in the container.

## The tools

```
tools/refgraph.py        the reference graph. Gate E and resolve_assets both
                         import it, so they cannot disagree about what
                         "referenced" means. Run it alone for a report.
tools/resolve_assets.py  takes its work list FROM refgraph, era-resolves each
                         defect against CDX digests -> tools/asset_choices.tsv
tools/fetch_missing.py   refetches the CDX-observed ones from Wayback, keeps
                         a payload only if its digest matches the CDX row
tools/place_assets.py    copies (never moves), re-verifies sha256 on arrival,
                         appends ledger rows; --promote rewrites a known-lost
                         row when evidence later arrives
```

Standard loop when a route is de-rendered or any page-side file changes:

```bash
python tools/refgraph.py                    # what does the site ask for now?
python tools/resolve_assets.py              # verdict + evidence per defect
python tools/fetch_missing.py               # recover what CDX proves existed
python tools/resolve_assets.py              # re-verdict with the new bytes
python tools/place_assets.py --promote      # lay down + label
python -m pytest tests/ -q                  # A, D, E, F
```

## Verdict vocabulary

`tools/asset_choices.tsv`, one row per defect, evidence in the `notes` column.

| verdict | tier | meaning |
|---|---|---|
| `era-digest-match` | `O` | payload sha1 appears on a 2017-2018 CDX row for that served path |
| `judged` | `O?` | no era capture exists; placed on a written timeline argument in `tools/asset_judgements.tsv` |
| `held-no-era-cdx` | `O?` | bytes sit at the served path in an archived host tree; era service unproven |
| `wrong-era-bytes` | `known-lost` | era digest known, every held copy hashes to another era |
| `cdx-observed` | `known-lost` | era captured the path, bytes not held — Wayback target |
| `weak-candidate-only` | `known-lost` | only a basename collision links a file to the path |
| `unobserved` | `known-lost` | referenced by the era pages, no era CDX row, no bytes |

## State at the time of writing (2026-08-04)

219 distinct subresources referenced. 156 resolve; 63 carry a `known-lost`
row. 134 assets were recovered in this pass:

* 78 from `flashpoint-gamezip/content/tanktrouble.com/images/` by era-digest
  match
* 53 refetched from Wayback and digest-verified into
  `archive/wayback-images-2026-08-03/`
* 3 (`tab{2,4,5}Select.jpg`) placed as `O?` on a written timeline argument

The remainder are honest gaps and the ledger says why each is one. Notable:
the six mazeCreator tool icons (`VISUAL-EVIDENCE-WANTED` #1), the news poll
bars, and `getItOnGooglePlay.png`.

Also fixed on the way through: `srv/images/scrapyardPlates.png` had been
filed `known-lost` at `srv/includes/images/…` (see corollary 1) — the
Scrapyard flip-counter renders again.

## When you add or change a page

1. Run gate E. It fails on anything new the page asks for.
2. Resolve each defect through the tools above — never by copying a
   plausible file into place.
3. If it cannot be recovered, write the `known-lost` row with the evidence
   that it is lost. A red gate is a to-do list; a fabricated file is a
   forgery.
4. If the reconstruction has to differ from what the original served, that is
   a divergence: record it in `docs/DIVERGENCES-SERVED.md` before shipping.
