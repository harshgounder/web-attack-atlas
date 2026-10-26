# web-attack-atlas: the thinking layer

Companion to `ai-web-arsenal`. That repo answers **what to run**. This one answers **what to think,
what to try, what will stop you, and what changes on the target if it works**.

They join on a stable `entry_id`. Neither duplicates the other. A pattern here may name a tool, and that
name resolves in the arsenal. The arsenal never describes a technique.

---

## 1. The organising principle: state mutation

Every web security list on earth is sorted by vulnerability class, and almost all of them are
read-oriented: recon, enumeration, disclosure, misconfiguration. That is backwards relative to where
impact lives.

**Impact is a write.** A read gives you information. A write changes what the system believes, what it
will show the next user, what it will execute later, or what it will charge. Stored XSS is a write.
Account takeover is a write. Business logic abuse is a write. Cache poisoning is a write to shared state.
Supply chain is a write to the build. RAG poisoning is a write to memory. Deserialization is a write
that executes.

So this atlas is organised by **what state you are changing and who believes it afterwards**:

```
write(target_state, principal_used, persistence, blast_radius, cost_to_detect)
```

That is the unit. Vulnerability classes become properties of a write, not the other way round. This is
why the atlas can hold "tens of thousands of ways" without collapsing into a list: the ways are
compositions over state, principal and persistence, not names to memorise.

### 1.1 The five questions every pattern must answer

1. **What state changes?** name the object, the field, the store, the cache entry, the token claim.
2. **As whom?** the principal whose authority is being borrowed, and whether that principal exists.
3. **Does it persist?** one response, one session, one deploy, or forever.
4. **How do you know it worked?** the oracle, plus the negative control that proves the oracle is sound.
5. **What stops it?** the control that would block it, and the detection that would catch it.

A pattern missing any of the five is a note, not a pattern. It gets marked `DRAFT` and stays out of the
rendered atlas.

---

## 2. Domains

Three series. W is the core, R is the necessary prerequisite, X is cross-cutting.

### W: write and state mutation

| id | domain | the state being changed |
|---|---|---|
| W01 | write primitives and object lifecycle | create, update, delete, restore, version, soft-delete |
| W02 | authorisation on writes | whose object, whose role, which field, which tenant |
| W03 | second-order and deferred processing | queues, cron, webhooks, imports, reports, emails |
| W04 | datastore writes | SQL, NoSQL, graph, search index, ORM, bulk endpoints |
| W05 | file write and materialisation | upload, archive, path, template, cache file, log |
| W06 | shared state and cache | CDN, reverse proxy, app cache, session store, feature flag |
| W07 | identity state | session, token, claims, MFA enrolment, recovery, device trust |
| W08 | business logic state machines | orders, payments, quotas, entitlements, approvals |
| W09 | concurrency and ordering | races, TOCTOU, idempotency, replay, double-spend |
| W10 | code path writes | deserialisation, template, expression, plugin, hook, migration |
| W11 | control plane writes | cloud IAM, K8s, CI/CD, secrets, DNS, certificates |
| W12 | AI memory and retrieval state | context, memory, vector store, RAG corpus, tool registry |

### R: read and acquisition

| id | domain | what it gets you |
|---|---|---|
| R01 | passive acquisition | OSINT, history, certs, leaks, third parties |
| R02 | surface and stack mapping | routes, hosts, frameworks, versions |
| R03 | interface recovery | schemas from specs, traffic, bundles, clients |
| R04 | data exposure | what the system already tells you for free |
| R05 | artifact and secret mining | JS, sourcemaps, mobile, containers, repos |

### X: cross-cutting

| id | domain | what it gives the atlas |
|---|---|---|
| X01 | chains and escalation | write A enables write B |
| X02 | oracles and proof | how a claim becomes evidence |
| X03 | defence counters | for each control class, the counter and its cost |
| X04 | detection mirror | for each pattern, the rule that catches it |
| X05 | reasoning and methodology | how an elite operator actually decides |
| X06 | labs and calibration | how a claim gets tested before it ships |

---

## 3. The counter layer (X03), because you asked for it explicitly

Every defence and every recon tool has a counter here. Not "bypass WAF" as a slogan, but:

```
counter(defence_tool, mechanism, precondition, observability_cost, which_detections_fire)
```

Covered defence classes, at minimum:

- signature and protocol-aware WAFs, per engine family
- bot management and browser fingerprinting
- rate limiters and quota systems, per algorithm
- RASP and in-app instrumentation
- CSP, SRI, Trusted Types
- CORS and postMessage restrictions
- SSO, MFA, conditional access, device trust
- EDR and audit logging on the server side
- schema validation and allowlists
- canary tokens and honeytokens
- ML and behavioural anomaly detection
- AI-specific: prompt guards, output filters, tool permissioning

And the reverse: for each recon or offensive tool on our own side, the counter that a defender would
deploy against it, so the atlas is honest about its own detectability.

The rule: **no pattern ships without its counter row.** An attack with no counter listed is treated as
unresearched, not as unstoppable.

---

## 4. Wave protocol

Research runs in waves. Each wave is one domain, end to end, and it is not published until it passes
the gate. No wave is "mostly done".

```
seed -> search -> harvest -> normalise -> enrich -> verify -> counters -> publish -> log
```

| stage | what happens | artefact |
|---|---|---|
| seed | pull the taxonomy IDs and corpus entries that belong to this domain | `waves/<id>/seed.json` |
| search | at least 3 independent queries, including one non-English and one regional | `waves/<id>/search.json` |
| harvest | raw pages and repos saved before anything is extracted | `waves/<id>/raw/` |
| normalise | one record per pattern, schema enforced | `waves/<id>/patterns.jsonl` |
| enrich | the five questions answered, plus edge cases and mutations | same file, richer |
| verify | two independent sources per non-obvious claim, recorded | `waves/<id>/verify.md` |
| counters | one counter row per pattern, plus the counter to our own tooling | `waves/<id>/counters.json` |
| publish | markdown rendered from JSON, never hand written | `patterns/W..md` |
| log | what ran, what failed, what stays open | `waves/<id>/LOG.md` |

Gate: a wave closes only when every pattern has the five answers and a counter, or is explicitly marked
`DRAFT` with the reason recorded.

---

## 5. Edge cases and mutations are first class

The ask is explicitly about the "very minute mutation". In this atlas that is not prose, it is a field:

```json
"mutations": [
  {"axis": "encoding", "variant": "double_url", "why": "two decode passes in the chain"},
  {"axis": "context", "variant": "json_in_json", "why": "body parsed twice by gateway and service"},
  {"axis": "type", "variant": "string_for_int", "why": "coercion differs between validator and store"},
  {"axis": "timing", "variant": "split_across_two_requests", "why": "validation on request A, write on B"}
]
```

Mutations are generated from axes, not memorised. That is how one pattern yields dozens of rows that are
all real, and how the atlas grows without anyone hand-writing variants.

---

## 6. What "elite human replication" means here, and how it is measured

The target is that an AI with this atlas performs like a top-tier human operator. That is a testable
claim, so it gets tests:

| test | what it proves |
|---|---|
| blind reproduction | given a lab target and only the atlas, does the model reproduce the intended finding |
| oracle discipline | does it produce a negative control, or does it claim success without one |
| chain depth | can it reach a 3 hop chain, or does it stop at the first finding |
| counter awareness | does it change approach when told which defence is present |
| calibration | rate of findings that survive human review, tracked over time |

A pattern that no model can turn into a working test is not a good pattern, even if the prose is
beautiful. That is the quality bar: **executable by an agent, verifiable by a skeptic.**

---

## 7. Bar per domain

50 or more enriched patterns, each with the five answers, at least one counter, and at least three
mutations. Fewer domains, higher density. A thin domain is worse than an absent one because it implies
coverage that does not exist.

---

## 8. Boundary

This is knowledge and decision support for authorised security work. Every pattern carries its
authorisation precondition. Patterns are described at the level of mechanism, precondition and
verification. No target-specific exploitation against systems the operator does not own or have written
permission to test.

---

## 9. Status vocabulary (corrected 2026-10-26)

An earlier draft used `VERIFIED` for patterns that had never been executed. That overclaims, so the
vocabulary is now explicit:

| status | meaning |
|---|---|
| ESTABLISHED | the mechanism is documented in independent sources (OWASP, WSTG, published research, bug bounty reports). Not executed by this project. |
| OBSERVED | reproduced in a lab by this project, with the run recorded in `waves/<id>/runs/` |
| PROBABLE | plausible, implementation dependent, not yet confirmed in any source we can cite |
| DRAFT | incomplete, excluded from the rendered atlas |

No pattern ever claims OBSERVED without a recorded run. The gate enforces the vocabulary; the honesty
rule enforces the meaning.
