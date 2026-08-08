# mazeCreator visual spec (M2 — measured 2026-08-03)

Source: `archive/ia-items/extracted/images/Making a maze.png` (832×556,
editor v0.3 in edit state, 2016-01-30). Measurement tool:
`tools/measure_editor_screenshot.py`.

## Scale derivation

Capture spans the SWF stage edge-to-edge horizontally: **scale = 832/688
= 1.2093**. Guide §6.5's per-axis factors (1.209/1.390) were an artifact
of dividing the full capture height (which includes ~72 px of page chrome
below the SWF: title input, tool buttons, ✗/✓) by the 400 px stage.
Proof of uniformity: wall-run pitch is 38.69 px horizontal / 38.88 px
vertical → 31.99 / 32.15 stage px — square 32 px cells. Vertical stage
origin sits ≈ 2 capture px below the capture top (panel border).

## Pinned constants

| Constant | Value | Evidence |
|---|---|---|
| CELL | 32 px | pitch 38.69/1.2093 = 31.99 |
| LATTICE (18×10 region) origin | (56, 50) | maze bbox left 136.4 = 56 + 2.5·32 (13 wide → offset (18−13)/2 = 2.5); top 81.9 = 50 + 1·32 (8 tall → offset (10−8)/2 = 1) — both axes land exactly |
| Maze placement | bbox centered on the lattice at exact (L−size)/2 cell offsets — **half-cell precision when parity is odd** | both axes above |
| Wall thickness | 4 px (≈4.7 capture), square caps, centered on gridlines | dark-run widths 4-5 px |
| Wall color | #444444 | exact dominant tone (3606 px) |
| Floor tones | #dddddd (dark) / #eeeeee (light) | exact dominant tones |
| Floor tone pattern | **NOT a checkerboard.** Per-cell mix, ≈ 1/3 light (29 D : 15 L cells; 35278 : 17139 px). No parity/row/column rule fits → per-cell random in the original. Rebuild: deterministic hash `((x*3 + y*7) % 3 == 0) → light` (≈1/3, stable across runtimes for gate C). Original pattern unknowable — logged in DIVERGENCES + VISUAL-EVIDENCE-WANTED. | tone grid dump |
| Title text | #666666, device sans, centered; band stage y ≈ 10-22 (≈18 px), stage-wide | scan (371-460, 12-27) capture |
| Watermark | "version 0.3", ≈#bbbbbb, wide letter-spacing, right-aligned to x ≈ 682, bottom edge ≈ 400 (flush corner), ≈12 px | scan (732-825, 477-486) capture |
| Tank spawn icon | small top-view tank, dark blue-violet outline, light blue body, **soft blue glow**; core tone ≈ (175,180,238); not clearly rotated (upscale too soft to pin exact angles — treated as axis-aligned) | cell close-up crop |
| Crate spawn icon | axis-aligned amber square ≈16×16 with darker border + **soft yellow glow**; core ≈ (219,183,85), border darker ≈ (170,130,50) | cell close-up crop |
| Object caps in shot | exactly 5 tanks + 5 crates — the corpus caps at max | transcription |

## Gauntlet transcription

`oracle/editor-visual/gauntlet.json` — the shot's 13×8 maze transcribed to
wire format (44 floor cells, 10 objects, boundary bits normalized per the
670/670 invariant). Interior-wall reads are best-effort from an upscaled
capture; the render-compare in the visual harness is the accuracy check.

## Known unknowns (see docs/standards/VISUAL-EVIDENCE-WANTED.md)

Floor tone pattern rule; icon rotation (if any); exact font faces; error
panel (never captured); preview mode; fade easing.
