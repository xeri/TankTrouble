---
name: resolve-subresources
description: Use when gate E fails, an image or script 404s, a page renders unstyled or with broken images, or after any change to a served page — the reference-derived asset loop (refgraph, resolve_assets, fetch_missing, place_assets).
---

# Resolve subresources (gate E)

**An asset inventory is derived from the site's own references, never from a
directory listing.** A reference that does not resolve is a defect until it is
either satisfied or written into `LEDGER.tsv` as `known-lost` with the evidence
that it is lost.

This exists because a page once passed gates A, D and F while rendering as
unstyled text, with most of what it requested absent and almost nothing in
`srv/images/` referenced by anything served. Full account, with the counts:
`docs/standards/ASSET-DISCIPLINE.md`.

## The loop

```bash
python tools/refgraph.py                    # what does the site ask for now?
python tools/resolve_assets.py              # verdict + evidence per defect
python tools/fetch_missing.py               # recover what CDX proves existed
python tools/resolve_assets.py              # re-verdict with the new bytes
python tools/place_assets.py --promote      # lay down + label
python -m pytest tests/ -q                  # A, D, E, F
```

## Verdicts

| Verdict | Tier | Meaning |
|---|---|---|
| `era-digest-match` | `O` | payload sha1 appears on an era CDX row for that served path |
| `judged` | `O?` | no era capture; placed on a written timeline argument in `tools/asset_judgements.tsv` |
| `held-no-era-cdx` | `O?` | bytes sit at the served path in an archived host tree; era service unproven |
| `wrong-era-bytes` | `known-lost` | era digest known, every held copy hashes to another era |
| `cdx-observed` | `known-lost` | era captured the path, bytes not held — a Wayback target |
| `weak-candidate-only` | `known-lost` | only a basename collision links a file to the path |
| `unobserved` | `known-lost` | referenced by era pages, no era CDX row, no bytes |

## Rules each defect must survive

1. **Resolve URLs the way a browser does.** A URL in a script string resolves
   against the *document*, not the script. Reading one script-relative filed a
   live 200-status asset as `known-lost` and left a counter blank.
2. **`../` above the document root is not an error** (RFC 3986 §5.2.4 drops the
   excess). Treat those as normal references.
3. **Bytes that exist are not automatically the right bytes.** Accept only
   against an era CDX digest for that exact served path.
4. **A basename match is not evidence.** Different case or an unrelated tree
   gets `weak-candidate-only` and a human decides. Never auto-promote.
5. **Not held ≠ not recoverable.** A CDX row with a digest is a fetch target;
   keep the payload only if `base32(SHA1(payload))` equals it.
6. **When the window captured nothing, argue in writing or not at all.** A
   judgement row fires only if the fetched payload matches the digest it names,
   its ceiling is `O?`, and the argument is copied verbatim into the ledger note
   so it can be attacked later.

## Names built at runtime

A name assembled in code (`'images/x' + tool + 'Select.jpg'`) cannot be read
statically, so every such family must enumerate its concrete names in
`tests/gate_e_dynamic.tsv`. A declared family the source no longer contains is
stale — delete the row.

## Case sensitivity

Windows matches paths case-insensitively; the `php:5.6` container does not. A
file stored as `DimitrisEmporium.png` satisfies a request for
`dimitrisEmporium.png` on your disk and 404s in the container.
`test_subresources_serve_as_labelled` (live) is what catches this.

## Finishing

- [ ] Every new file has a ledger row placed by `place_assets.py` (which copies,
      never moves, and re-verifies sha256 on arrival).
- [ ] Everything unrecoverable has a `known-lost` row **with the evidence that it
      is lost**. A red gate is a to-do list; a fabricated file is a forgery.
- [ ] Anything worth hunting for later goes in `docs/standards/VISUAL-EVIDENCE-WANTED.md`.
