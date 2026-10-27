# Contributing

## The gate

A pattern ships only when it answers all five:

1. `target_state` what state changes
2. `principal` as whom
3. `persistence` does it last
4. `oracle` plus `negative_control` how you know, and what proves the oracle is sound
5. `counter` with `mechanism`, `precondition` and `cost`

Plus at least one `mutation` with its axis and the reason it matters.

```bash
python3 scripts/render-patterns.py --check   # exits 1 on failure
```

A pattern without a negative control is a hypothesis. It will be marked DRAFT, not merged.

## Adding a wave

1. Create `waves/<ID>/patterns.jsonl`, one JSON object per line. Use `waves/W02/patterns.jsonl` as the
   reference shape.
2. `status` must be one of ESTABLISHED, OBSERVED, PROBABLE, DRAFT.
3. `OBSERVED` requires a recorded run in `waves/<ID>/runs/`. Nothing else may claim it.
4. Run the maintenance sequence:

```bash
python3 scripts/maintain.py        # classify counters, regenerate COUNTERS.md and QUEUE.json
python3 scripts/build-index.py     # refresh INDEX.md and the atom matrix
python3 scripts/render-patterns.py --render
```

## Do not repeat these four mistakes

1. **Never fold unmatched counters into another class.** A fallback of `C02` once made "authorisation
   closes 31 percent" look like a finding. Unmatched is `C99` and is reported as its own bucket.
2. **Never keep stale labels.** `maintain.py` always recomputes unless an explicit override is set.
3. **Never claim VERIFIED for something not executed.** The vocabulary exists because that happened.
4. **Check the atom matrix after each wave.** If a new wave has the same dominant atom as an existing one,
   it is probably that domain wearing a different name.

## What is out of scope

Operational assistance for unauthorised access, and licence or DRM circumvention. Patterns are described
at the level of mechanism, precondition and verification, each with its authorisation requirement.
