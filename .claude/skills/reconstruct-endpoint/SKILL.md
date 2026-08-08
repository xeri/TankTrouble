---
name: reconstruct-endpoint
description: Use when implementing or changing a server endpoint, SAJAX function, wire format or response grammar — the backend fidelity procedure, including what to do about behaviour the corpus can never show.
---

# Reconstruct an endpoint

The backend is the half nobody can see, which is why it is the half where
invention survives longest. The standard is the same as for pixels: **evidence,
then verdict, then bytes.**

## 1. Inventory before implementing (free and decisive)

- [ ] Pull the endpoint's CDX rows. A **single constant response digest** across
      thousands of rows means the body is recoverable — implement it. Varying
      digests with no held bodies means it stays 501, and that is a decision to
      record, not a gap to fill.
- [ ] Collect every archived request shape. Key sets, parameter order, which
      parameters are cache-busters, which values are literal.
- [ ] Collect every archived response body. Decode them. Count distinct
      contents, and count distinct *states* — those differ, and the difference
      usually rewrites the data model.
- [ ] Find the client. A decompiled reader fully specifies its writer; the
      client's own parser is the strongest available spec for a response.

## 2. Split observable from unobservable

Write both columns into `docs/standards/BACKEND-CONTRACTS.md` before writing code.

**Typically observable:** request key sets, response grammar and field names,
byte-exact bodies for constant responses, limits the corpus never violates,
first/last appearance dates.

**Typically not:** response headers and `Content-Type`, trailing newline,
behaviour on malformed input, selection mechanism (`ORDER BY RAND()` vs
anything else), case and padding semantics, the server's own shuffle
implementation, anything behind login.

For every unobservable: choose the **least inventive** option, mirroring a
convention already proven elsewhere in this corpus; state it in `@caveat`;
register it. Never emit a plausible value silently.

## 3. Implement

- [ ] `@provenance` / `@evidence` / `@verified` / `@written` / `@caveat` header
      first, and make it honest — `NONE for the name, method, or wire format -
      ALL INVENTED` is a real line in this repo.
- [ ] Reject rather than fake: unknown or malformed input dies with a loud
      `RECONSTRUCTION:` message and a real status code.
- [ ] Escape everything even though `mysql_*` is period-correct — an injection
      corrupts the seeded archive, which is the data being preserved.
- [ ] Reproduce the original's faults; do not tidy them.

## 4. Gate it

The endpoint's ledger row cannot leave stub state until `verified_by` names a
test that exists, added in the same commit.

Pick the strongest gate the evidence supports:

* **Byte replay** — archived bodies replayed exactly. Strongest; only possible
  when the response is deterministic.
* **Content replay** — when the original provably randomised (per-request
  shuffle, random selection), gate the invariants the corpus *does* pin: exact
  outer format, byte-exact constant bodies such as `notFound`, decoded field
  multisets, exact key set, and full state coverage by sampling with a hard
  request cap.
* **Contract test** — for invented endpoints. It pins the invention so it cannot
  drift, and says so in its own docstring. It is not evidence.

Say which one you used, in the header and in `DECISIONS.md`.

## 5. Land it

- [ ] `DECISIONS.md` entry: what was chosen, what the evidence forced, what was
      **rejected**, reversibility.
- [ ] `docs/FOUNDATIONS.md` row if the endpoint pins a wire format, a key, or a
      data model — with its falsifier and its dependents.
- [ ] `docs/standards/BACKEND-CONTRACTS.md` updated with the final observable/chosen split.
- [ ] Anything user-visible that differs → `docs/standards/DIVERGENCES-SERVED.md`, before
      shipping.

## Escalate first

Changing a wire format, touching authentication, or altering the schema key of a
seeded table: stop and ask. These are the changes whose cost is measured in
milestones.
