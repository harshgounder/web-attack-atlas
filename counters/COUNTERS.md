# Counters by control class

HOW TO READ THIS: a defender picks the classes they own and sees exactly how many atlas patterns that
closes. A researcher reads it the other way: this is what will stop you, grouped by what you can test for.

`50` patterns across `11` control classes.

| class | control | patterns closed | typical mechanism | cost |
|---|---|---|---|---|
| C01 | object level authorisation | 8 | object level authorisation on every item write | one query per write, or a scoped query by owner |
| C02 | function level authorisation | 16 | explicit allowlist per role, never object hydration | schema maintenance |
| C03 | binding allowlist | 4 | mutual auth, source allowlist, separate audience | infra |
| C04 | identity canonicalisation | 4 | exact match identity, verify before linking | low |
| C05 | state machine integrity | 6 | validate at every transition, treat drafts as untrusted | revalidate |
| C06 | credential and token policy | 3 | derive tenant from token, never from body, and validate every referenced parent | one scoped lookup per reference |
| C07 | parser strictness | 3 | one parser per resource, reject alternates | low |
| C09 | cache and key discipline | 1 | include every varying input in the key, or do not cache personalised responses | design |
| C10 | cost and resource control | 1 | cost analysis per operation, authorise per node | engine config |
| C11 | audit integrity | 2 | read only impersonation by default, dual attribution in audit | one flag |
| C12 | protocol lifecycle | 2 | retire versions, or route them through the current policy layer | infra |

## C01: object level authorisation

per object ownership check on every operation

- `W02-0001` Object level write substitution on an update endpoint  
  - counter: object level authorisation on every item write
- `W02-0005` Ownership transfer without consent  
  - counter: owner consent required, two party confirmation
- `W02-0007` Bulk endpoint skips per item authorisation  
  - counter: authorise each element, report per element
- `W02-0011` Identifier harvested from a public surface unlocks the write  
  - counter: object level authorisation independent of id secrecy
- `W02-0012` Child object write under a parent you do not own  
  - counter: authorise the parent on every nested operation
- `W02-0021` Version history restore bypasses the current authorisation  
  - counter: authorise restore against current permissions on the parent
- `W02-0034` Directory sync overwrites local attributes it should not own  
  - counter: field level ownership between systems
- `W02-0047` Rename or move endpoint reparents a file without rechecking  
  - counter: authorise both source and destination

## C02: function level authorisation

per operation role and permission check, deny by default

- `W02-0003` Field level privilege through mass assignment  
  - counter: explicit allowlist per role, never object hydration
- `W02-0004` Write path missing the function level check the read path has  
  - counter: authorise at the route group level and again at the handler
- `W02-0006` Soft delete resurrection  
  - counter: enforce the deleted predicate in the data layer, not the query layer
- `W02-0009` Write through an operation that was never designed as a write  
  - counter: no state change on safe methods
- `W02-0010` Authorisation evaluated on a stale copy of the object  
  - counter: authorise against the authoritative store, or push invalidation synchronously
- `W02-0013` Membership add as a privilege escalation primitive  
  - counter: separate permission to add from permission to be added
- `W02-0014` Invitation flow used to mint a privileged account  
  - counter: role determined server side at acceptance from the inviter's authority
- `W02-0016` Import feature overwrites records it does not own  
  - counter: scope the match query to the importer's tenant and objects
- `W02-0017` Webhook configuration as a write primitive  
  - counter: admin only, destination allowlist, egress filtering
- `W02-0018` API key scope not enforced on the write path  
  - counter: scope check at the handler, derived from the route
- `W02-0023` Self approval inside a workflow  
  - counter: separation of duties enforced server side
- `W02-0028` Shared edit link grants more than the sharer intended  
  - counter: server side permission per link, short expiry, revocable
- `W02-0029` Email change without verification starts an account takeover chain  
  - counter: confirm from the old address, notify both, delay recovery
- `W02-0032` Identity provider attribute maps straight into a role  
  - counter: map roles from groups the app controls, not free attributes
- `W02-0043` Case insensitive storage collides with case sensitive authorisation  
  - counter: one comparison rule everywhere
- `W02-0048` Share permission raised by the recipient  
  - counter: only the sharer can change the grant

## C03: binding allowlist

explicit field allowlist, never object hydration

- `W02-0033` Provisioning endpoint accepts writes it should reserve for the IdP  
  - counter: mutual auth, source allowlist, separate audience
- `W02-0036` GraphQL input coercion supplies a value the UI never sends  
  - counter: allowlist at the resolver, not the schema
- `W02-0037` Protobuf field presence lets a client clear a protected value  
  - counter: field masks with an allowlist
- `W02-0045` Identifier type juggling across query layers  
  - counter: typed binding at the edge

## C04: identity canonicalisation

one normalisation form, exact match, verified linking

- `W02-0031` Alias or plus addressing resolves to a victim identity  
  - counter: exact match identity, verify before linking
- `W02-0042` Unicode normalisation makes two identifiers collide  
  - counter: single normalisation form, enforced at write and lookup
- `W02-0044` Trailing whitespace or control characters create a shadow identity  
  - counter: strict identifier charset, trim before store
- `W02-0046` Archive extraction writes outside its intended directory  
  - counter: canonicalise and verify containment per entry

## C05: state machine integrity

invariants enforced per step, separation of duties

- `W02-0022` Draft state is permissive and publication skips the check  
  - counter: validate at every transition, treat drafts as untrusted
- `W02-0024` Quota or limit reset endpoint used to write demand  
  - counter: eligibility checked server side, counters append only
- `W02-0025` Referral or points ledger written without a real event  
  - counter: credit from server verified events, idempotency keys
- `W02-0039` Null versus absent decides whether a guard runs  
  - counter: explicit state machine, no null branch for authz
- `W02-0040` Quantity arithmetic overflows or wraps at the write  
  - counter: bounded integers, server side totals
- `W02-0041` Negative or zero value passes a check written for positives  
  - counter: sign and range validation per field

## C06: credential and token policy

atomic single use, subset scopes, verified identity

- `W02-0002` Tenant escape through a nested reference on create  
  - counter: derive tenant from token, never from body, and validate every referenced parent
- `W02-0019` OAuth scope upgraded on refresh or re-consent  
  - counter: refresh scope must be a subset of the original grant
- `W02-0030` Reset token reusable or raced across two requests  
  - counter: atomic single use, invalidate siblings on issue

## C07: parser strictness

one parser, reject duplicates and alternates

- `W02-0008` Alternate representation reaches the same write with weaker checks  
  - counter: one parser per resource, reject alternates
- `W02-0015` Duplicate parameter decides which role is written  
  - counter: reject duplicate parameters, parse once
- `W02-0038` Duplicate JSON keys split validation from persistence  
  - counter: strict parser, reject duplicates

## C09: cache and key discipline

every varying input in the key

- `W02-0027` Shared cache key collision overwrites another user's view  
  - counter: include every varying input in the key, or do not cache personalised responses

## C10: cost and resource control

per operation cost and quotas by principal

- `W02-0035` GraphQL aliases multiply a mutation past its guard  
  - counter: cost analysis per operation, authorise per node

## C11: audit integrity

structured append only logging with attribution

- `W02-0020` Support impersonation used to perform the write  
  - counter: read only impersonation by default, dual attribution in audit
- `W02-0026` Log injection used to write into the audit trail  
  - counter: structured logging with escaping, append only store

## C12: protocol lifecycle

retired versions decommissioned, one policy point

- `W02-0049` Retired API version still writes with the old guard  
  - counter: retire versions, or route them through the current policy layer
- `W02-0050` Legacy protocol endpoint bypasses the modern authorisation layer  
  - counter: decommission or front with one policy proxy

