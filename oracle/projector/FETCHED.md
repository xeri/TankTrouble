# Adobe Flash Player standalone projector (gate C oracle)

- Item: https://archive.org/details/flashplayer_standalone_projectors
- File: https://archive.org/download/flashplayer_standalone_projectors/flashplayer_32_sa.exe
- Fetched: 2026-08-03
- sha256: a4b333ac1da12026989549015303d82231982838bccfb544ba5fd188746066f0
- sha1: 7736efc1c76e6a80132a22e1f9fc87a5884fa375 (matches the item's own metadata)
- Version (PE resource): **32.0.0.465** — the true final Windows standalone
  build (Dec 2020), not the 32.0.0.371 the guide guessed. ProductName
  "Shockwave Flash", 15,983,672 bytes, MZ magic verified.
- Role: gate C ground truth (guide 7.3). Runs O SWFs natively.

## Smoke tests, 2026-08-03

- `oracle/editor-spike/spike.swf?initCode=dT05OSZuPXRlc3R1c2VyMDEm` via
  `file:///` URL: renders (boot fill 0x336699) and shows the 180px FlashVars
  marker strip — **query-string FlashVars reach `_root` in the projector**,
  so the projector half of gate C can drive SWFs with the same initCode
  mechanism the site used.
- `srv/includes/TankTrouble_v4.0.swf` standalone: window opens, stage stays
  white at 15s. Not a projector defect — the game boots through a preloader
  into server-coupled init (loadVariables/serverInfo) and was only ever run
  inside the site embed with an initCode. Gate C game-rendering runs need
  the docker stack reachable or a harness initCode; that wiring is phase 2.
- Note: `getURL("javascript:")` is inert in the projector; page-bridge
  behaviour is only testable under Ruffle. Gate C compares RENDERING.
