# Porting `TankTrouble_v4.0.swf` to HTML5 — feasibility

Assessment of whether the decompiled classic client can be rewritten in another
language rather than emulated. Measured from the decompile, not estimated.

Subject: `TankTrouble_v4.0.swf`, 366,827 b, sha256 `188062aff7f7d969…` — the build
frozen 2013-03-13 → 2020-12-25. Decompile at
`archive/decompiled/CLASSIC_TankTrouble_v4.0/`.

Evidence conventions: `DEDUCE.md`. Provenance tiers: `RECONSTRUCTION-STATUS.md`.

---

## 1. Verdict

**Feasible, and unusually so.** The blocker in a typical Flash port — lost or
unreadable logic — does not apply here. The obstacle is animation, not code.

| Question | Answer |
|---|---|
| Is the code recoverable? | **Yes.** 15,859 lines, 101 files, **0 decompilation failures** |
| Is the logic complete? | **Yes.** AI, all weapons, collision, round flow, UI, netcode all present |
| Is the art recoverable? | **Yes.** Vector shapes → SVG, 20 JPEGs, 30 sounds all exportable |
| Is a physics engine in the way? | **No.** Collision is hand-rolled `hitTest`; no Box2D, no p2 |
| How big is the Flash-runtime surface? | **~30 distinct calls.** Enumerated in §4 |
| What does *not* port? | **Timeline animation** — §6 |

---

## 2. Why ActionScript 2 is the favourable case

**AS2 is ECMAScript.** Same lineage as JavaScript: `var`, `function`, prototypes,
closures, `for`/`while`, the same `String`/`Array`/`Math` methods. `Math.` alone
appears **709 times** and needs no translation at all.

This is not a rewrite in the usual sense. The *language* transfers nearly verbatim;
what must be replaced is the **runtime binding layer** — the MovieClip display list,
the drawing API, sound, and input. That layer is small and fully enumerated in §4.

Contrast with an AS3/AVM2 port, where the class system, event model and display
framework would all need mapping. None of that applies.

---

## 3. What the decompile contains

| Measure | Value |
|---|---|
| ActionScript | **15,859 lines / 101 files** |
| Decompilation failures | **0** — no `//Unknown`, no error markers |
| Frame scripts | 8,071 lines across 14 frames |
| Sprite scripts | 7,788 lines across 43 sprites |
| `__Packages` classes | `Base64`, `MazeDataFetcher`, `MazeDataLoader` |

Top-level tag census of the 744,511-byte uncompressed body:

| Content | Bytes | Share |
|---|---:|---:|
| Code (`DoAction` + `DoInitAction`) | 165,826 | 22.4% |
| Sound (30 × `DefineSound`) | 153,666 | 20.7% |
| Fonts (2 × `DefineFont3`) | 122,610 | 16.5% |
| Vector shapes (155 × `DefineShape*`) | 58,526 | 7.9% |
| JPEG (20 × `DefineBitsJPEG3`) | 46,515 | 6.3% |
| Lossless bitmaps | **0** | 0% |

*(`DefineSprite` accounts for a further 167,885 b; its nested shapes and code are
counted inside the categories above where the per-file listing reaches them.)*

### 3.1 Systems present, by sprite

```
107_tankTroubleAI (1,489 lines)   ← the AI, intact
Weapons:  170_deathRay (422)  162_homingbullet (406)  158_mine (310)
          150_rCMissile (288)  169_electricbullet (214)  168_fragbomb (187)
          182_elToro (250)  173_bullet  159_laser  165_gatling
          164_gatlingBullet  167_fragbombfragment  119_rCSignal  178_scopeCircle
Effects:  108_shieldGraphic (268)  109_shield  179_fluid  180_fluidLBM (200)
          181_fluidDiffuse
UI:       249_gamePanel (248)  264_chatPanel (234)  265_chatMessagesPanel
          214_settingsPanel  220_scoreboardPanel  240_newGamePanel
          230_randomGamePanel  257_countdownPanel  251_flagAndTextPanel
          243_multiplayerInfo  274_aimer  282_leaveGame  189_sliderChoice
          192_settingsPanelDefaultButton  194_settingsPanelCloseButton
          197_sliderEnabler
Net:      118_serverInfo
```

14 frame scripts, of which three carry the weight: `frame_58` (2,766),
`frame_53` (2,658), `frame_1` (469). The remainder are a linear preloader chain.

---

## 4. The entire Flash-runtime surface — this is the whole shim

Every Flash-specific call in the codebase, with call counts. **The shim is bounded
by this table**; nothing outside it is used.

| Group | Calls (count) | HTML5 target | Difficulty |
|---|---|---|---|
| **Maths** | `Math.*` (709) | native | **none** — already JS |
| **Vector drawing** | `lineTo` (90) `moveTo` (71) `lineStyle` (62) `clear` (15) `beginFill` (10) `endFill` (8) | Canvas2D path API | **low** — near 1:1 |
| **Display list** | `getNextHighestDepth` (124) `removeMovieClip` (93) `createEmptyMovieClip` (47) `attachMovie` (46) `swapDepths` (24) | scene-graph shim with a depth-ordered container | **medium** — the main shim |
| **Ticking** | `onEnterFrame` (85) | one `requestAnimationFrame` loop dispatching to registered objects | **low** |
| **Timeline control** | `play` (206) `gotoAndStop` (70) `stop` (42) `gotoAndPlay` (1) | per-clip frame cursor | **medium** — see §6 |
| **Collision** | `hitTest` (48) | AABB + point-in-shape | **low** — hand-rolled already |
| **Colour** | `Color` (27) `setRGB` (27) | canvas tint / CSS filter | **low** — tank colours |
| **Coordinates** | `localToGlobal` (27) `globalToLocal` (4) | matrix transform | **low** |
| **Sound** | `Sound` (30) `attachSound` (30) | Web Audio | **low** |
| **Input** | `Key.*` (26) `onMouseDown` (9) `onKeyDown` (5) `Mouse.*` (3) `onRelease` (2) `onMouseMove` (3) `onKeyUp` (1) | DOM events | **low** |
| **Stage** | `Stage.*` (13) | canvas dimensions | **low** |
| **Network** | `loadVariables` (10) `getURL` (10) | `fetch` + direct calls | **low** |
| **Text** | `createTextField` (4) | DOM overlay or canvas text | **low** |
| **Timers** | `setInterval` (1) `clearInterval` (1) | native | **none** |

Roughly **30 distinct APIs**, dominated by two groups: display-list management
(~334 call sites) and vector drawing (~256).

### 4.1 The finding that matters most

**The arena is drawn in code, not stored as art.** 256 calls to
`lineStyle`/`moveTo`/`lineTo`/`beginFill`/`endFill` mean maze rendering is
procedural — it reads out of the decompile and maps directly onto Canvas2D. No
art extraction, no asset pipeline, no fidelity loss for the single most visually
identifying element of the game.

---

## 5. Assets — all reusable, none need redrawing

| Asset | Count | Route |
|---|---|---|
| Sounds | 30 (153 KB) | FFDec export → MP3/WAV → Web Audio, byte-identical |
| JPEGs | 20 (46 KB) | FFDec export, reuse as-is |
| Vector shapes | 155 (58 KB) | FFDec exports SVG; or re-emit as Canvas2D paths |
| Fonts | 2 embedded (111 KB) | **redundant** — `c64.ttf/.eot/.woff` already held separately as `O` |
| Lossless bitmaps | 0 | n/a |

Provenance note: exported assets stay **`O`** — they are original bytes in a new
container. Re-drawn assets are **`M2`**/`M3`. Do not blur the two in `LEDGER.tsv`.

---

## 6. The honest hard part — timeline animation

**Tweens and frame-by-frame motion are not in the ActionScript.** They live in
`PlaceObject2` tags (35 at top level, more nested across the 129 sprites) — a
declarative per-frame transform stream the Flash player interprets.

This is why `play` appears 206 times and `gotoAndStop` 70: much of the visual
behaviour is *timeline* driven, and the code only steers it.

Three options, in increasing fidelity:

1. **Re-author** the animations by hand from exported frames. Highest effort,
   result is **M2** — it will not be frame-exact.
2. **Export frame sequences** as sprite sheets and play them back. Mechanical,
   good fidelity, larger payload, result is **O**-derived.
3. **Write a minimal `PlaceObject2` interpreter** — read the tag stream, apply
   matrix and colour transforms per frame. Highest fidelity, and it makes the
   port *provably* faithful rather than approximately so.

Option 3 is more tractable than it sounds because the tag set actually in use is
small, and it is the only route that keeps the animation layer at tier `O`.

---

## 7. Risks and unknowns

| Risk | Assessment |
|---|---|
| Depth-management semantics | Flash's depth rules (`swapDepths`, implicit depths, `_level`) have edge cases. 334 call sites means bugs here are systemic, not local. **Build the display-list shim first and test it in isolation** |
| Frame-rate coupling | `onEnterFrame` logic is written against a fixed SWF frame rate. Physics tuned to that rate will drift on a `requestAnimationFrame` loop. Use a fixed-timestep accumulator, do not run logic per animation frame |
| `hitTest` shape-flag mode | Flash's `hitTest(x, y, true)` tests actual shape, not bounds. Where the code passes `true`, bounds-only collision changes gameplay |
| Netcode | `loadVariables` (10 sites) targets PHP endpoints that are themselves being reconstructed. Port and server must agree on the wire format — which for mazes is fully specified, and for the rest is `M2` |
| Sound timing | 30 sounds; Web Audio has different latency behaviour. Cosmetic, not blocking |

---

## 8. What this changes about the plan

The current stack decision is Ruffle for the browsable build with a Flash projector
as oracle. A port is a **third option**, and it removes a specific risk already
flagged: Ruffle's AS2 support is partial, and the gaps most likely to bite are
`SetVariable` and the `getURL("javascript: …")` bridge — precisely the APIs the
garage and the maze editor depend on.

A native port has no Flash runtime, so those gaps cannot occur.

Recommended sequencing, unchanged in spirit:

1. Run the Ruffle-vs-projector spike first regardless. It is cheap and it answers
   whether emulation is viable at all.
2. If Ruffle handles the bridge, keep emulation as the primary path — it is `O`
   bytes running, which no port can claim.
3. Treat the port as the **fallback with better fidelity guarantees for the pieces
   Ruffle cannot run**, and as the natural home for a rebuilt maze editor, which has
   no original bytes to emulate anyway.

Provenance consequence, stated plainly: **an emulated SWF is `O`. A port is `M1` at
best** — verifiable against the original's behaviour, but not the original. Both are
legitimate; they are not the same claim, and the ledger must not present them as
one.
