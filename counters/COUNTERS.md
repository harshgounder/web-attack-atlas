# Counters

Derived from every pattern. A pattern without a counter does not pass the gate, so this file is
the complete counterpart set for the atlas, not a sample.

`50` patterns, `50` distinct counter mechanisms.

| counter mechanism | patterns it closes | precondition | cost |
|---|---|---|---|
| object level authorisation on every item write | 1 (`W02-0001`) | the check must run after parsing and before persistence | one query per write, or a scoped query by owner |
| derive tenant from token, never from body, and validate every referenced parent | 1 (`W02-0002`) | the parent resolution must be tenant scoped | one scoped lookup per reference |
| explicit allowlist per role, never object hydration | 1 (`W02-0003`) | allowlist evaluated per request not per controller | schema maintenance |
| authorise at the route group level and again at the handler | 1 (`W02-0004`) | no endpoint inherits auth merely from adjacency | duplicate checks |
| owner consent required, two party confirmation | 1 (`W02-0005`) | the consent step must be server enforced | extra flow |
| enforce the deleted predicate in the data layer, not the query layer | 1 (`W02-0006`) | every write also filters | one predicate |
| authorise each element, report per element | 1 (`W02-0007`) | no early exit on first failure | linear |
| one parser per resource, reject alternates | 1 (`W02-0008`) | content type allowlist | low |
| no state change on safe methods | 1 (`W02-0009`) | enforced by framework or review | low |
| authorise against the authoritative store, or push invalidation synchronously | 1 (`W02-0010`) | revocation must be synchronous | latency |
| object level authorisation independent of id secrecy | 1 (`W02-0011`) | never treat unguessable as authorisation | one scoped query |
| authorise the parent on every nested operation | 1 (`W02-0012`) | nested routes inherit nothing | one lookup |
| separate permission to add from permission to be added | 1 (`W02-0013`) | role supplied by server per inviter privilege | one policy check |
| role determined server side at acceptance from the inviter's authority | 1 (`W02-0014`) | invite token binds role | one comparison |
| reject duplicate parameters, parse once | 1 (`W02-0015`) | same parser for validate and write | low |
| scope the match query to the importer's tenant and objects | 1 (`W02-0016`) | upsert never resolves globally | one predicate |
| admin only, destination allowlist, egress filtering | 1 (`W02-0017`) | secret never readable after creation | policy plus network |
| scope check at the handler, derived from the route | 1 (`W02-0018`) | no route reuses a group with different requirements | one attribute read |
| refresh scope must be a subset of the original grant | 1 (`W02-0019`) | grant recorded | one comparison |
| read only impersonation by default, dual attribution in audit | 1 (`W02-0020`) | operator identity always recorded | one flag |
| authorise restore against current permissions on the parent | 1 (`W02-0021`) | version ids scoped | one check |
| validate at every transition, treat drafts as untrusted | 1 (`W02-0022`) | no trust in earlier state | revalidate |
| separation of duties enforced server side | 1 (`W02-0023`) | approver cannot be requester | one comparison |
| eligibility checked server side, counters append only | 1 (`W02-0024`) | no client supplied plan | one check |
| credit from server verified events, idempotency keys | 1 (`W02-0025`) | never trust a client signal | event store |
| structured logging with escaping, append only store | 1 (`W02-0026`) | log parser treats fields as data | low |
| include every varying input in the key, or do not cache personalised responses | 1 (`W02-0027`) | cache key reviewed per route | design |
| server side permission per link, short expiry, revocable | 1 (`W02-0028`) | claims not trusted alone | one lookup |
| confirm from the old address, notify both, delay recovery | 1 (`W02-0029`) | recovery binds to a verified identity | flow change |
| atomic single use, invalidate siblings on issue | 1 (`W02-0030`) | token consumption is a compare and set | one transaction |
| exact match identity, verify before linking | 1 (`W02-0031`) | normalisation never merges accounts | low |
| map roles from groups the app controls, not free attributes | 1 (`W02-0032`) | no user writable attribute is authoritative | sync |
| mutual auth, source allowlist, separate audience | 1 (`W02-0033`) | not reachable from the internet | infra |
| field level ownership between systems | 1 (`W02-0034`) | explicit ownership matrix | mapping review |
| cost analysis per operation, authorise per node | 1 (`W02-0035`) | aliases counted | engine config |
| allowlist at the resolver, not the schema | 1 (`W02-0036`) | schema is not the permission model | one check |
| field masks with an allowlist | 1 (`W02-0037`) | absence never means clear | one mask |
| strict parser, reject duplicates | 1 (`W02-0038`) | one parser for the whole path | low |
| explicit state machine, no null branch for authz | 1 (`W02-0039`) | three states handled deliberately | code review |
| bounded integers, server side totals | 1 (`W02-0040`) | validate range before arithmetic | low |
| sign and range validation per field | 1 (`W02-0041`) | domain specific bounds | low |
| single normalisation form, enforced at write and lookup | 1 (`W02-0042`) | confusable policy | low |
| one comparison rule everywhere | 1 (`W02-0043`) | documented collation | low |
| strict identifier charset, trim before store | 1 (`W02-0044`) | one canonical form | low |
| typed binding at the edge | 1 (`W02-0045`) | reject arrays on scalars | low |
| canonicalise and verify containment per entry | 1 (`W02-0046`) | no symlink following | low |
| authorise both source and destination | 1 (`W02-0047`) | no implicit inherit | two checks |
| only the sharer can change the grant | 1 (`W02-0048`) | recipient is not an author of the grant | one check |
| retire versions, or route them through the current policy layer | 1 (`W02-0049`) | one policy enforcement point | infra |
| decommission or front with one policy proxy | 1 (`W02-0050`) | no parallel auth stacks | infra |
