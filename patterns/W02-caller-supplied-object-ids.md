# Pattern P-W02-019: caller-supplied object identifiers on collection endpoints

Wave: W02 (authorisation on writes) - new pattern, gated 2026-11-15.
Atoms: A02 (trust boundary crossing) + A10 (logic assumption violation).
Source: Yaamlabs CTEM/BOLA roundup (research/2026-11-15/patterns-oct-nov-2026.md),
confirmed against juice-shop basket API (lab: web-attack-labs/labs/juice-shop-live).

## The gate

1. **What state changes?** the basket/document record addressed by its identifier
   in the request path or body; the server trusts the identifier without checking
   that the authenticated principal owns it.
2. **As whom?** any authenticated principal (or anonymous, where the collection
   is unauthenticated) acting on another principal's record.
3. **Does it persist?** yes for write verbs (PUT/POST/DELETE on the object path);
   reads are one-response disclosure.
4. **How do you know?** oracle: register two principals, A reads/writes B's object
   id; differential response vs B's own view. Negative control: A accesses a
   nonexistent id (must 404/empty) and B's own id (must succeed).
5. **What stops it?** counter: server-side ownership predicate on every object
   dereference (not just UI-level filtering); counter precondition: session
   identity must be authoritative, not a caller-supplied header. Counter cost:
   one ownership check per dereference, plus tests with two principals.

## Mutations observed in the wild

- {"axis": "identifier", "variant": "sequential_int_to_uuid", "why": "enumeration resistance is a property of the id space, not of the check"}
- {"axis": "carrier", "variant": "basket_id_in_cookie_or_body", "why": "the same identifier often arrives via several carriers; middleware may check one and trust another"}
- {"axis": "verb", "variant": "PUT_vs_PATCH_merge_semantics", "why": "merge handlers may update fields without re-checking ownership per field"}

## Lab contract (web-attack-labs/labs/juice-shop-live)

- positive: GET /rest/basket/2 vs GET /rest/basket/1 as anonymous (driver
  evidence ev-0012..ev-0014, engagement juice-lab-02: all three returned
  basket data with different id spaces)
- negative control: /rest/basket/0 and a nonexistent id (ev-0014)
- remaining lab work: two-principal differential with authentication (next
  driver run); this pattern stays status: candidate until that lands.
