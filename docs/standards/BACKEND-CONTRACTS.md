# Backend contracts — what the corpus proves, and what we chose

The backend is the half nobody can inspect, which is why it is the half where
invention survives longest. A wrong pixel gets noticed. A wrong `ORDER BY`, a
wrong header, an invented error body — those look identical to the real thing
forever.

**The standing rule: unobservable is not unaccountable.** Every behaviour the
corpus cannot show is chosen deliberately, declared in the file's `@caveat`, and
registered here. Never emit a plausible value silently.

Procedure for adding or changing one: the `reconstruct-endpoint` skill.

## What the corpus can and cannot show

| Usually observable | Usually not |
|---|---|
| request key sets, and which keys are cache-busters | response headers and `Content-Type` |
| response grammar and field names | trailing newline, whitespace framing |
| byte-exact bodies where the response is constant | behaviour on malformed or unknown input |
| limits the corpus never violates | selection mechanism (random, ordered, first) |
| first and last appearance dates of a feature | case, padding and collation semantics |
| the client's parser, which is a spec for the response | the server's own shuffle implementation |
| | anything behind login |

## Per-endpoint register

### `srv/includes/loadMaze.php` — M1, gate B

**Proven:** request key sets `{userName,a,b}` and `{c,a,b}`, with `a`/`b`/`c` as
cache-busters and `userName` always the literal `"undefined"` in archived
requests. Response is `r=` + base64 of shuffled `t/n/d/s` pairs, `s` inside the
base64, key set exactly `{t,n,d,s}` (F-04). The `notFound` body is byte-exact
(`MAZE_NOTFOUND_BODY` in `docs/reference/ARCHITECTURE.md`). No percent-encoding
anywhere in the corpus.

**Chosen, and caveated in-file:** the shuffle mirrors the client's naive
swap-shuffle — the server's real implementation is unverifiable from output, so
the gate compares multisets, not bytes. Random selection is `ORDER BY RAND()`;
the real mechanism is unobservable. `q` is read from `QUERY_STRING` +
`rawurldecode` because `$_GET` would corrupt a base64 `+` into a space. Malformed
or unknown input dies with a loud 400 — the original's behaviour is unarchived
and is not guessed. No explicit `Content-Type`; headers were never archived.

**Out of scope, explicitly:** the 13-row 2018-06-03/04 anomaly, whose stable
unshuffled body was never archived.

### `srv/includes/saveMaze.php` — M3, contract test only

**Proven:** nothing. The name, method and wire format are all invented. The
deduction chain that says the endpoint existed: no maze function among the SAJAX
exports, so the page did not save; the recovered page JS sets
`_root.errorPanel.hide`, so the SWF saw a response; therefore the SWF posted to a
URL that lived only inside the lost `mazeCreator_v0.3.swf`.

**Chosen:** mirror `loadMaze`'s conventions as the least inventive option —
`q=`/`r=` base64 pair messages, the same naive shuffle. POST-only is a
rebuild-era choice. Validation limits are the corpus-measured editor constraints
(`EDITOR_LIMITS`).

`tests/test_savemaze.py` pins the invention so it cannot drift. **It is not
evidence, and the file says `DO NOT PROMOTE`.**

### `srv/includes/getScrapyard.php` — M2, replay of two pre-era bodies

**Proven:** two archived request/response pairs, 2015-09-28 and 2016-01-26. The
requested query keys select which fields are emitted.

**Chosen / caveated:** both observations are **pre-era** — the era scrapyard
moved to the SAJAX `getScraps` call in `index.php` at the 2017-02-21 deploy — so
this file's era behaviour is unarchived and the tier stays `M2`. Exactly the two
archived query strings are accepted; anything else is not guessed. `velocity`'s
storage and derivation are unobservable, so the state row keeps the archived
decimal string and emits it verbatim.

**Consequence, not a bug:** the counter creeps for ~60 s and then pins. Against a
frozen row the O client re-derives a velocity of zero. See
`docs/standards/DIVERGENCES-SERVED.md` §5 — including the option that was considered and
**not** taken, because it would put extrapolated digits on screen.

### `srv/includes/getUserAuthentication.php` — M3, deliberate divergence (F-12)

The original ran SAJAX auth over GET, which is why real credentials are
permanently in the public CDX index. This does not reconstruct that: POST +
`password_hash`, 200/401/405/400, minimal session, synthetic accounts only.
Response format is invention — no original response was ever archived. Logged-in
page rendering is not reconstructed, so nothing consumes the session. TLS is out
of scope for a localhost-only stack.

**This one is never "fixed" toward fidelity.** `tests/test_auth_divergence.py`
proves it stays POST-only.

### `srv/includes/achievement.php` — M2, stays 501

Six client call sites name the parameters; **no response of any kind was ever
observed**. A decision, not an omission: it returns 501 and says so.

### `srv/includes/updateGameStatistics.php` — M2, stays 501

2,305 CDX rows and known client call sites, but no archived body. The digest
check is the deciding test: a single constant response digest across those rows
would make the body recoverable. Until that resolves, 501.

### SAJAX surface on `index.php`

Only reconstructed functions are in `$GLOBALS['sajax_export_list']`. Everything
else returns the stock library "not callable" error — reject, never fake. Zero
era SAJAX response bodies are archived, so `showForumPreviews` and
`showForumThread` can **never** be byte-gated; that is permanent, not pending.
The strongest available constraint on their markup is the class names in the `O`
`forumStyles.css`.

Library and export counts: `SAJAX_VERSION`, `SAJAX_EXPORTS` in
`docs/reference/ARCHITECTURE.md`.

### `srv/includes/rebuild-db.php` — M3, deliberately modern name

The one invented file, and its hyphen announces it. Credentials come from the
`TT_DB_*` container environment, never from code. `mysql_*` is kept for period
fidelity inside a never-exposed container, and **every query input passes the
escape helper** — an injection here corrupts the seeded archive, which is the
data being preserved.

## HTTP surface

| Behaviour | Status |
|---|---|
| directory listing | off site-wide |
| `/includes/` | 403 |
| rewrite rules | none — query routing is native PHP |
| response headers, `Content-Type` | **unarchived.** Nothing sets them explicitly; do not invent one |
| trailing newline on endpoint output | omitted (no closing `?>`); unarchived |
| unimplemented endpoint | 501 + `STUB`, never 200 |
| malformed input to a reconstructed endpoint | loud `RECONSTRUCTION:` message + a real status code |
| unimplemented SAJAX function | the stock library error, not an invented body |

## Faults that must be reproduced

Fidelity, not bugs. Tidying one is a divergence and needs an entry in
`docs/standards/DIVERGENCES-SERVED.md` before it ships.

* The SWF version string is hard-coded in four separate files with no shared
  constant — which is why the reminder comments exist.
* `infirmary/index.html` is a hand-copied simplification of `index.php`, not a
  template render.
