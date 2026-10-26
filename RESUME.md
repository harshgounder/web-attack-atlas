# RESUME: how to continue this repo

Verified by running on 2026-10-26.

## State

| | count |
|---|---|
| patterns | 150, all passing the five-question gate |
| waves done | 3 of 23 (W01 lifecycle, W02 authorisation, W03 second-order) |
| atoms | 16 declared, 13 exercised |
| control classes | 13, with a defender-facing index |
| status vocabulary | 149 ESTABLISHED, 1 PROBABLE, 0 OBSERVED |

## The gate

A pattern ships only when it answers all five:

1. `target_state`: what state changes
2. `principal`: as whom
3. `persistence`: does it last
4. `oracle` plus `negative_control`: how you know, and what proves the oracle is sound
5. `counter`: what stops it, with `mechanism`, `precondition` and `cost`

```bash
python3 scripts/render-patterns.py --check   # exit 1 on failure
```

## Add a wave

1. Create `waves/<ID>/patterns.jsonl`, one JSON object per line, using `waves/W02/patterns.jsonl` as the
   reference shape.
2. Every pattern needs the five answers, at least one `mutation`, and `status` from
   ESTABLISHED / OBSERVED / PROBABLE / DRAFT.
3. `OBSERVED` requires a recorded run in `waves/<ID>/runs/`. Nothing else may claim it.
4. Run `python3 scripts/maintain.py` (classifies counters, regenerates COUNTERS.md and QUEUE.json).
5. Run `python3 scripts/build-index.py` to refresh INDEX.md and the atom matrix.
6. Run `python3 scripts/render-patterns.py --render`.

## What the numbers already say

- Output handling (C03, 35 patterns) and state integrity (C05, 31) together are 44% of the atlas.
  Authorisation together is 36, or 24%. That contradicts the usual narrative and it is the finding.
- Each write domain dominates a different atom: W01 A04 state confusion 28, W02 A02 trust boundary 24,
  W03 A01 interpreter confusion 26. If they shared one atom they would be one domain.

## Do not repeat these mistakes

1. **Never fold unmatched counters into another class.** A fallback of `C02` made "authz closes 31%"
   look like a finding. Unmatched is `C99` and is reported.
2. **Never keep stale labels.** `maintain.py` now always recomputes unless an override is set.
3. **Never claim VERIFIED for something not executed.** The vocabulary exists because that happened.
4. **Check the atom matrix after each wave.** If a new wave has the same dominant atom as an existing
   one, it probably is that domain wearing a different name.

## Next waves, in order of value

1. **W07 identity state** (session, token, MFA enrolment, recovery, device trust). D04 already points at
   it and currently links to a queue entry, which is honest but incomplete.
2. **W04 datastore writes**, **W05 file materialisation** to finish the write suite.
3. **W12 AI memory and retrieval**, which D19 and D20 both point at.
4. **X03 defence counters** as a first-class wave rather than a per-pattern field.


---

## Closing note, 2026-10-27

This project's recurring failure mode was a **plausible-looking artifact that nothing validated**.
Eight instances were caught, none by reading:

1. two recalled facts wrong (a repo called stale that was active, one called live that was archived)
2. link checker used HEAD, which real sites answer 404, producing 7 false dead links
3. classifier fallback turned every unmatched counter into "authorisation", inflating a finding to 31%
4. two repository URLs were invented and looked exactly like the 110 real ones
5. a mirror coverage metric was measuring its own scoring, giving 14% then 26% then 52%
6. the backlog was 10,476 until measured properly at 1,491
7. the corpus was 24,759 until image URLs were removed, giving 21,397
8. a name repair ran after its generator and was silently discarded, then the retry never matched

Every one was found by a measurement disagreeing with a claim. That is the method this repo is trying
to encode: if a number cannot be regenerated from disk, it is not a number, it is a memory.
