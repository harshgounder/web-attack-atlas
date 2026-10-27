# web-attack-atlas

<p align="center">
  <b>The thinking layer for web platform attacks.</b><br/>
  Not a tool list. Patterns with preconditions, oracles, mutations and counters.<br/>
  Organised by <i>state mutation</i>, not by vulnerability class.
</p>

<p align="center">
  <img alt="patterns" src="https://img.shields.io/badge/patterns-150%2C%20gate%20passing-8a2be2?style=flat-square"/>
  <img alt="atoms" src="https://img.shields.io/badge/primitives-16%20atoms-blue?style=flat-square"/>
  <img alt="waves" src="https://img.shields.io/badge/waves-3%20of%2023-2ea44f?style=flat-square"/>
  <img alt="classes" src="https://img.shields.io/badge/control%20classes-13-orange?style=flat-square"/>
  <img alt="license" src="https://img.shields.io/badge/license-MIT-lightgrey?style=flat-square"/>
</p>

<p align="center">
  <a href="#the-thesis">Thesis</a> ·
  <a href="#the-grammar">Grammar</a> ·
  <a href="#the-gate">Gate</a> ·
  <a href="#what-the-numbers-already-say">Findings</a> ·
  <a href="#waves">Waves</a> ·
  <a href="#companion-repo">Companion</a> ·
  <a href="#contributing">Contributing</a>
</p>

---

## The thesis

Every web security list is sorted by vulnerability class, and almost all of them are read oriented:
recon, enumeration, disclosure, misconfiguration. That is backwards relative to where impact lives.

**Impact is a write.** A read gives you information. A write changes what the system believes, what it
will show the next user, what it will execute later, or what it will charge.

Stored XSS is a write. Account takeover is a write. Business logic abuse is a write. Cache poisoning is a
write to shared state. Supply chain is a write to the build. RAG poisoning is a write to memory.
Deserialization is a write that executes.

So this atlas is organised by **what state you are changing and who believes it afterwards**:

```
write(target_state, principal_used, persistence, blast_radius, cost_to_detect)
```

Vulnerability classes become properties of a write, not the other way round. That is why the atlas can
hold many techniques without collapsing into a list: the techniques are compositions over state,
principal and persistence, not names to memorise.

---

## The grammar

```
attack = atom(sink, carrier, preconditions, oracle) x mutation(encoding, context, protocol, timing)
chain  = attack_1 . attack_2 ... where capability(attack_n) enables preconditions(attack_{n+1})
```

**16 atoms.** Every technique is a composition of one or more:

| id | atom | the violation |
|---|---|---|
| A01 | interpreter confusion | data treated as inert is executed downstream |
| A02 | trust boundary crossing | a lower principal acts with higher authority |
| A03 | identity confusion | the system misidentifies who is acting |
| A04 | state confusion | the system's view of state diverges from reality |
| A05 | type and shape confusion | the same bytes mean different things in two layers |
| A06 | path and namespace confusion | two components resolve the same name differently |
| A07 | resource exhaustion | a finite resource is consumed faster than replenished |
| A08 | information exposure | data reaches a party that should not receive it |
| A09 | cryptographic weakness | a property the design assumes is false |
| A10 | logic assumption violation | the workflow assumes an invariant the attacker breaks |
| A11 | dependency compromise | an upstream artefact is trusted and is not trustworthy |
| A12 | timing and ordering | the window between check and use is exploitable |
| A13 | side channel | observable behaviour leaks protected information |
| A14 | human manipulation | the human in the loop is the weak component |
| A15 | configuration divergence | deployed state differs from intended state |
| A16 | model and agent manipulation | an AI component's instruction following is the boundary |

Full model: [`docs/ONTOLOGY.md`](docs/ONTOLOGY.md). Machine readable: [`data/atoms.json`](data/atoms.json).

---

## The gate

A pattern ships only when it answers all five questions:

1. **What state changes?** the object, field, store, cache entry, token claim
2. **As whom?** the principal whose authority is borrowed
3. **Does it persist?** one response, one session, one deploy, or forever
4. **How do you know?** the oracle, plus the negative control that proves the oracle is sound
5. **What stops it?** the counter, with its own precondition and cost

```bash
python3 scripts/render-patterns.py --check   # exit 1 on failure
```

Every pattern also carries at least one **mutation** with the axis and the reason, because the minute
variant is what defeats a filter without changing the technique:

```json
"mutations": [
  {"axis": "encoding", "variant": "double_url", "why": "two decode passes in the chain"},
  {"axis": "protocol", "variant": "PATCH_instead_of_PUT", "why": "method level middleware differs"},
  {"axis": "type", "variant": "array_of_ids", "why": "bulk handlers skip per item checks"}
]
```

---

## What the numbers already say

**Output handling and state integrity dominate the write surface.**

| class | control | patterns closed |
|---|---|---|
| C03 | binding and output escaping | **35** |
| C05 | state machine integrity | **31** |
| C02 | function level authorisation | 18 |
| C01 | object level authorisation | 18 |
| C09 | cache and key discipline | 9 |
| C04 | identity canonicalisation | 8 |
| C06 C07 C10 C11 C12 C13 | tokens, parsers, cost, audit, lifecycle, process | 31 |

Authorisation together is 36 patterns, or 24 percent. **That contradicts the standard narrative that
authorisation is the whole game.** For write side attacks, the bugs that let you change someone's data are
data rendered in the wrong context later, and state transitions that do not hold their invariants.

**Each write domain dominates a different primitive**, which is the design proving itself:

| atom | W01 lifecycle | W02 authorisation | W03 second-order |
|---|---|---|---|
| A04 state confusion | **28** | 9 | 11 |
| A02 trust boundary | 9 | **24** | 17 |
| A01 interpreter confusion | 1 | 1 | **26** |

If all three shared one dominant atom they would be one domain wearing three names.

Full view: [`INDEX.md`](INDEX.md). Defender view: [`counters/COUNTERS.md`](counters/COUNTERS.md).

---

## What a pattern looks like

```json
{
  "id": "W02-0001",
  "title": "Object level write substitution on an update endpoint",
  "atom": ["A02"],
  "target_state": "another user's object field",
  "principal": "the victim user, borrowed by the attacker",
  "persistence": "until corrected, visible to the victim immediately",
  "preconditions": [
    "update endpoint accepts an object identifier from the request",
    "authorisation checked on the collection, not the item"
  ],
  "oracle": ["victim session shows the changed value"],
  "negative_control": "same request with a nonexistent id returns 404, proving the id path is live",
  "mutations": [{"axis": "protocol", "variant": "PATCH_instead_of_PUT", "why": "method level middleware differs"}],
  "counter": {
    "mechanism": "object level authorisation on every item write",
    "precondition": "the check must run after parsing and before persistence",
    "cost": "one query per write"
  }
}
```

The `negative_control` field is the one that separates this from every list on GitHub. A scanner that
reports without a control is guessing.

---

## Waves

Research runs in waves. Each wave is one domain, end to end, and it is not published until it passes the
gate.

```
seed -> search -> harvest -> normalise -> enrich -> verify -> counters -> publish -> log
```

| wave | domain | patterns |
|---|---|---|
| W01 | write primitives and object lifecycle | 50 |
| W02 | authorisation on writes | 50 |
| W03 | second-order and deferred processing | 50 |
| W04 | datastore writes | queued |
| W05 | file write and materialisation | queued |
| W06 | shared state and cache | queued |
| W07 | identity state | queued |
| W08 | business logic state machines | queued |
| W09 | concurrency and ordering | queued |
| W10 | code path writes | queued |
| W11 | control plane writes | queued |
| W12 | AI memory and retrieval state | queued |
| R01 to R05 | read and acquisition | queued |
| X01 to X06 | chains, oracles, counters, detection, reasoning, labs | queued |

Queue and status: [`waves/QUEUE.json`](waves/QUEUE.json).

### W03 is the domain almost nobody treats as a class

The write lands in one request and the effect happens in another trust zone, later. That is why it
survives input validation by construction: validation happens at write time, the sink is elsewhere.

Covers stored XSS in privileged consoles, spreadsheet formula injection, PDF and email renderers,
markdown sanitiser differentials, deferred SSRF through webhooks and unfurl bots, second order SQLi and
command injection, log poisoning, cache poisoning and deception, queue message identity injection,
internal header trust, report generator RCE, webhook replay, token leakage via referrer, calendar ICS
injection, deferred deserialisation, and privilege that outlives revocation.

---

## Status vocabulary

| status | meaning |
|---|---|
| ESTABLISHED | mechanism documented in independent sources, **not executed by this project** |
| OBSERVED | reproduced in a lab here, with the run recorded in `waves/<id>/runs/` |
| PROBABLE | plausible and implementation dependent, not yet confirmed anywhere citable |
| DRAFT | incomplete, excluded from the rendered atlas |

Current: **134 ESTABLISHED, 15 PROBABLE, 1 OBSERVED.**

The single observation is `W01-0001`, the parallel create race. It was run on 2026-10-27 against a
purpose built target in the companion repo: 24 parallel creates produced 24 records of which 23 were
duplicates, and the sequential control produced exactly one record with 23 rejections. The record is
`waves/W01/runs/W01-0001.json` and the gate now refuses any `OBSERVED` pattern whose run record is
missing, belongs to another pattern, or carries no negative control.

Six labs exist in the companion repo and only one lands here, because this atlas is about writes. The
other five demonstrate reads: SSRF, object authorisation on a read, cache poisoning, path normalisation
and algorithm confusion. That is a property of the thesis rather than a gap in the evidence, and it is
the reason the observed count is one here while the arsenal counts six. An earlier draft used
`VERIFIED` for patterns that had never been run, which overclaimed, so the vocabulary was corrected and
the correction is in the commit history.

---

## Companion repo

| | this repo | [ai-web-arsenal](https://github.com/harshgounder/ai-web-arsenal) |
|---|---|---|
| owns | atoms, patterns, preconditions, oracles, chains, counters | tools, install, drivers, MCP wiring, REA, corpus |
| answers | what do I think, what do I try, what will stop me | what do I run, and how |
| join key | `entry_id` | `entry_id` |

A pattern here may name a tool, and that name resolves in the arsenal. The arsenal never describes a
technique. Tools die every 18 months, techniques survive decades.

---

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md). The short version: a pattern without a negative control is not
a pattern, and `OBSERVED` requires a recorded run.

## Security

Read [SECURITY.md](SECURITY.md). Every pattern carries its authorisation requirement.

## License

[MIT](LICENSE).

<p align="center"><sub>Every count in this file is produced by <code>scripts/render-patterns.py</code> and <code>scripts/maintain.py</code>. If a number disagrees with a script, the script is right.</sub></p>
