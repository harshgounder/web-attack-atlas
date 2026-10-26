# W02: authorisation on writes

Generated from `waves/W02/patterns.jsonl`. Do not edit by hand.
50 patterns. Every one answers the five questions and carries a counter.

## Index

| id | pattern | atoms | persists | counter mechanism |
|---|---|---|---|---|
| W02-0001 | Object level write substitution on an update endpoint | A02 | until corrected, visible to the victim immediately | object level authorisation on every item write |
| W02-0002 | Tenant escape through a nested reference on create | A02, A06 | permanent until deleted | derive tenant from token, never from body, and validate every referenced parent |
| W02-0003 | Field level privilege through mass assignment | A05, A02 | permanent, survives re-login | explicit allowlist per role, never object hydration |
| W02-0004 | Write path missing the function level check the read path has | A02 | varies, often permanent | authorise at the route group level and again at the handler |
| W02-0005 | Ownership transfer without consent | A02, A10 | permanent and often destructive | owner consent required, two party confirmation |
| W02-0006 | Soft delete resurrection | A04, A02 | indefinite | enforce the deleted predicate in the data layer, not the query layer |
| W02-0007 | Bulk endpoint skips per item authorisation | A02, A07 | scales with batch size | authorise each element, report per element |
| W02-0008 | Alternate representation reaches the same write with weaker checks | A05, A06 | permanent | one parser per resource, reject alternates |
| W02-0009 | Write through an operation that was never designed as a write | A10, A04 | until recompute, sometimes forever | no state change on safe methods |
| W02-0010 | Authorisation evaluated on a stale copy of the object | A04, A12 | window dependent | authorise against the authoritative store, or push invalidation synchronously |
| W02-0011 | Identifier harvested from a public surface unlocks the write | A02, A08 | as long as the object lives | object level authorisation independent of id secrecy |
| W02-0012 | Child object write under a parent you do not own | A02, A06 | visible immediately to the parent owner | authorise the parent on every nested operation |
| W02-0013 | Membership add as a privilege escalation primitive | A02, A03 | permanent until removed | separate permission to add from permission to be added |
| W02-0014 | Invitation flow used to mint a privileged account | A02, A10 | permanent | role determined server side at acceptance from the inviter's authority |
| W02-0015 | Duplicate parameter decides which role is written | A05, A02 | permanent | reject duplicate parameters, parse once |
| W02-0016 | Import feature overwrites records it does not own | A02, A10 | destructive, often unrecoverable | scope the match query to the importer's tenant and objects |
| W02-0017 | Webhook configuration as a write primitive | A02, A10, A07 | until changed, and every future event leaks | admin only, destination allowlist, egress filtering |
| W02-0018 | API key scope not enforced on the write path | A02, A03 | as long as the change lasts | scope check at the handler, derived from the route |
| W02-0019 | OAuth scope upgraded on refresh or re-consent | A02, A03 | for the token lifetime, refreshable | refresh scope must be a subset of the original grant |
| W02-0020 | Support impersonation used to perform the write | A03, A02, A14 | permanent, logged as the customer | read only impersonation by default, dual attribution in audit |
| W02-0021 | Version history restore bypasses the current authorisation | A04, A02 | permanent, and it overwrites current content | authorise restore against current permissions on the parent |
| W02-0022 | Draft state is permissive and publication skips the check | A10, A04 | publication makes it permanent | validate at every transition, treat drafts as untrusted |
| W02-0023 | Self approval inside a workflow | A10, A02 | permanent record of false approval | separation of duties enforced server side |
| W02-0024 | Quota or limit reset endpoint used to write demand | A07, A10 | repeatedly exploitable | eligibility checked server side, counters append only |
| W02-0025 | Referral or points ledger written without a real event | A10, A12 | monetisable, until reconciled | credit from server verified events, idempotency keys |
| W02-0026 | Log injection used to write into the audit trail | A01, A08 | permanent, and it poisons future forensics | structured logging with escaping, append only store |
| W02-0027 | Shared cache key collision overwrites another user's view | A06, A04 | until TTL, seen by many users | include every varying input in the key, or do not cache personalised responses |
| W02-0028 | Shared edit link grants more than the sharer intended | A02, A03 | until revoked, sometimes unrevocable | server side permission per link, short expiry, revocable |
| W02-0029 | Email change without verification starts an account takeover chain | A03, A10 | permanent unless noticed | confirm from the old address, notify both, delay recovery |
| W02-0030 | Reset token reusable or raced across two requests | A12, A03 | takeover | atomic single use, invalidate siblings on issue |
| W02-0031 | Alias or plus addressing resolves to a victim identity | A03, A10 | permanent | exact match identity, verify before linking |
| W02-0032 | Identity provider attribute maps straight into a role | A03, A05 | until next login, or permanent if persisted | map roles from groups the app controls, not free attributes |
| W02-0033 | Provisioning endpoint accepts writes it should reserve for the IdP | A02, A03 | permanent | mutual auth, source allowlist, separate audience |
| W02-0034 | Directory sync overwrites local attributes it should not own | A04, A05 | on every sync cycle | field level ownership between systems |
| W02-0035 | GraphQL aliases multiply a mutation past its guard | A07, A02 | scales with alias count | cost analysis per operation, authorise per node |
| W02-0036 | GraphQL input coercion supplies a value the UI never sends | A05 | varies | allowlist at the resolver, not the schema |
| W02-0037 | Protobuf field presence lets a client clear a protected value | A05, A04 | permanent | field masks with an allowlist |
| W02-0038 | Duplicate JSON keys split validation from persistence | A05, A06 | permanent | strict parser, reject duplicates |
| W02-0039 | Null versus absent decides whether a guard runs | A05, A04 | varies | explicit state machine, no null branch for authz |
| W02-0040 | Quantity arithmetic overflows or wraps at the write | A05, A10 | monetary | bounded integers, server side totals |
| W02-0041 | Negative or zero value passes a check written for positives | A10, A05 | monetary | sign and range validation per field |
| W02-0042 | Unicode normalisation makes two identifiers collide | A06, A03 | permanent, and enables impersonation | single normalisation form, enforced at write and lookup |
| W02-0043 | Case insensitive storage collides with case sensitive authorisation | A06, A03 | permanent | one comparison rule everywhere |
| W02-0044 | Trailing whitespace or control characters create a shadow identity | A06, A03 | permanent | strict identifier charset, trim before store |
| W02-0045 | Identifier type juggling across query layers | A05, A06 | varies | typed binding at the edge |
| W02-0046 | Archive extraction writes outside its intended directory | A06, A05 | files persist | canonicalise and verify containment per entry |
| W02-0047 | Rename or move endpoint reparents a file without rechecking | A06, A02 | permanent | authorise both source and destination |
| W02-0048 | Share permission raised by the recipient | A02, A05 | until revoked, often unnoticed | only the sharer can change the grant |
| W02-0049 | Retired API version still writes with the old guard | A15, A06 | permanent | retire versions, or route them through the current policy layer |
| W02-0050 | Legacy protocol endpoint bypasses the modern authorisation layer | A15, A06 | permanent | decommission or front with one policy proxy |

## W02-0001: Object level write substitution on an update endpoint

**Atoms:** `A02` trust boundary crossing  
**State changed:** another user's object field  
**Acting as:** the victim user, borrowed by the attacker  
**Persistence:** until corrected, visible to the victim immediately  
**Status:** VERIFIED  
**Authorization:** written scope from the target owner, and a second account you control

Preconditions:
- update endpoint accepts an object identifier from the request
- authorisation checked on the collection, not the item
- identifiers are enumerable or leaked in a list response

Procedure:
1. read the collection as self
2. capture the exact update request
3. substitute the object id with a victim id
4. replay with the same session
5. re-read as the victim to confirm the change

**Oracle:** `victim session shows the changed value`, `response body reflects the new value`, `second read from a different session agrees`  
**Negative control:** same request with a nonexistent id returns 404, proving the id path is live and not a silent success

| mutation axis | variant | why it matters |
|---|---|---|
| encoding | `id_in_body_vs_query_vs_path` | authz middleware may only cover one |
| protocol | `PATCH_instead_of_PUT` | method level middleware differs |
| type | `array_of_ids` | bulk handlers often skip per item checks |

**Detected by:** object id ownership mismatch log, write to object not in session scope

**Counter:** object level authorisation on every item write  
**Counter precondition:** the check must run after parsing and before persistence  
**Counter cost:** one query per write, or a scoped query by owner

**Tools (resolve in ai-web-arsenal):** `d11-newman`, `d11-ffuf`

---

## W02-0002: Tenant escape through a nested reference on create

**Atoms:** `A02` trust boundary crossing, `A06` path and namespace confusion  
**State changed:** a record owned by another tenant  
**Acting as:** the victim tenant  
**Persistence:** permanent until deleted  
**Status:** VERIFIED  
**Authorization:** written scope, two tenants you control

Preconditions:
- create accepts a reference to a parent object
- parent ownership not verified against the caller tenant
- tenant id is in the token but the parent id is in the body

Procedure:
1. create an object in your own tenant
2. note the parent reference shape
3. replace the parent reference with a victim tenant parent
4. create and read back through the victim tenant view

**Oracle:** `read back through victim scoped query returns the record`, `victim side listing shows the injected record`  
**Negative control:** parent id from a tenant you cannot see returns 403, confirming the guard exists elsewhere

| mutation axis | variant | why it matters |
|---|---|---|
| context | `nested_object_instead_of_id` | validators recurse differently than the writer |
| type | `null_parent_falls_back` | null may default to a shared root |

**Detected by:** cross tenant reference audit

**Counter:** derive tenant from token, never from body, and validate every referenced parent  
**Counter precondition:** the parent resolution must be tenant scoped  
**Counter cost:** one scoped lookup per reference

**Tools (resolve in ai-web-arsenal):** `d11-newman`

---

## W02-0003: Field level privilege through mass assignment

**Atoms:** `A05` type and shape confusion, `A02` trust boundary crossing  
**State changed:** a security relevant field on your own profile  
**Acting as:** you, escalated  
**Persistence:** permanent, survives re-login  
**Status:** VERIFIED  
**Authorization:** written scope, your own account

Preconditions:
- update binds request body to an internal model
- the model has fields the UI never sends
- no allowlist on the binding

Procedure:
1. read your profile
2. add fields not present in the UI, one at a time: role, is_admin, plan, verified, tenant_id
3. observe which are accepted silently
4. confirm by re-reading and by exercising the new privilege

**Oracle:** `re-read shows the new value`, `behaviour changes accordingly`, `privilege is usable in a follow up request`  
**Negative control:** an invented field name returns 200 but is absent on re-read, proving acceptance is not proof of persistence

| mutation axis | variant | why it matters |
|---|---|---|
| context | `json_key_case_variants` | binding is case sensitive, authorisation may not be |
| type | `string_where_bool` | coercion at persistence layer |

**Detected by:** write to a field not in the request schema for that role

**Counter:** explicit allowlist per role, never object hydration  
**Counter precondition:** allowlist evaluated per request not per controller  
**Counter cost:** schema maintenance

**Tools (resolve in ai-web-arsenal):** `d11-arjun`

---

## W02-0004: Write path missing the function level check the read path has

**Atoms:** `A02` trust boundary crossing  
**State changed:** an administrative object  
**Acting as:** an admin, borrowed  
**Persistence:** varies, often permanent  
**Status:** VERIFIED  
**Authorization:** written scope, role accounts provided

Preconditions:
- the read endpoint enforces role
- the corresponding write endpoint shares routing or middleware but not the guard
- ids observed from a permitted read or an error

Procedure:
1. enumerate admin read endpoints as a low privilege user and note 403
2. find the sibling write endpoints
3. attempt the write with the same low privilege session
4. compare the guard behaviour read vs write

**Oracle:** `write succeeds where read is denied`, `effect observable through a permitted admin read as a second admin account`  
**Negative control:** the read endpoint still returns 403 in the same session, isolating the finding to the write path

| mutation axis | variant | why it matters |
|---|---|---|
| protocol | `method_override_header` | some frameworks honour X-HTTP-Method-Override |
| protocol | `batch_endpoint` | bulk routes often mount different middleware |

**Detected by:** role to endpoint matrix per method

**Counter:** authorise at the route group level and again at the handler  
**Counter precondition:** no endpoint inherits auth merely from adjacency  
**Counter cost:** duplicate checks

---

## W02-0005: Ownership transfer without consent

**Atoms:** `A02` trust boundary crossing, `A10` logic assumption violation  
**State changed:** the owner field of a shared object  
**Acting as:** the new owner or the attacker  
**Persistence:** permanent and often destructive  
**Status:** PROBABLE  
**Authorization:** written scope, accounts you control

Preconditions:
- an endpoint exists to change owner or sharing
- the recipient is attacker supplied
- no confirmation from the current owner

Procedure:
1. share or transfer an object you own
2. note the owner or share request
3. substitute the recipient with a controlled account, then with a victim object reference
4. observe whether the transfer completes without the owner acting

**Oracle:** `ownership visible in both accounts`, `the original owner loses access, which is the impact proof`  
**Negative control:** transfer to an invalid account fails, so success is not a default no-op

| mutation axis | variant | why it matters |
|---|---|---|
| timing | `two step create then transfer` | the guard may only apply to the first step |

**Detected by:** ownership change without owner initiated event

**Counter:** owner consent required, two party confirmation  
**Counter precondition:** the consent step must be server enforced  
**Counter cost:** extra flow

---

## W02-0006: Soft delete resurrection

**Atoms:** `A04` state confusion, `A02` trust boundary crossing  
**State changed:** the deleted flag and its dependents  
**Acting as:** the deleted object's former owner, or a new user  
**Persistence:** indefinite  
**Status:** VERIFIED  
**Authorization:** written scope, your own objects

Preconditions:
- delete is a flag, not a row delete
- read paths filter the flag
- write paths do not
- or uniqueness indexes exclude soft deleted rows

Procedure:
1. delete an object you own
2. attempt update, share, restore and duplicate against the same id
3. re-register the same unique key and observe whether the old object resurfaces

**Oracle:** `object reappears in a listing`, `update on the deleted id succeeds`, `unique key collision reveals the hidden row`  
**Negative control:** a truly absent id fails, proving the resurrection is specific to soft deleted rows

| mutation axis | variant | why it matters |
|---|---|---|
| timing | `update immediately after delete` | async purge may lag |

**Detected by:** write to a soft deleted row

**Counter:** enforce the deleted predicate in the data layer, not the query layer  
**Counter precondition:** every write also filters  
**Counter cost:** one predicate

---

## W02-0007: Bulk endpoint skips per item authorisation

**Atoms:** `A02` trust boundary crossing, `A07` resource exhaustion  
**State changed:** many objects in one request  
**Acting as:** mixed  
**Persistence:** scales with batch size  
**Status:** VERIFIED  
**Authorization:** written scope, two accounts

Preconditions:
- a batch, import or sync endpoint exists
- it authorises the request, not each element

Procedure:
1. build a batch containing one object you own and one you do not
2. submit
3. observe partial success semantics
4. read back both

**Oracle:** `response reports per item status`, `the foreign item is modified and readable by its owner`  
**Negative control:** single object submission of the foreign id fails, isolating the finding to the batch path

| mutation axis | variant | why it matters |
|---|---|---|
| volume | `large_batch_to_hide_one` | truncated error reporting |
| type | `mixed_ids_types` | per item validation skipped |

**Detected by:** batch with heterogeneous ownership

**Counter:** authorise each element, report per element  
**Counter precondition:** no early exit on first failure  
**Counter cost:** linear

---

## W02-0008: Alternate representation reaches the same write with weaker checks

**Atoms:** `A05` type and shape confusion, `A06` path and namespace confusion  
**State changed:** the same field, through a different parser  
**Acting as:** same  
**Persistence:** permanent  
**Status:** VERIFIED  
**Authorization:** written scope

Preconditions:
- the API accepts more than one content type or version
- validation lives in one representation and not the other

Procedure:
1. identify the canonical JSON write
2. replay the same semantic operation as form encoded, XML, multipart, or a v1 path
3. compare validation and authorisation outcomes

**Oracle:** `the weaker representation persists a value the strict one rejects`  
**Negative control:** the strict representation rejects the same payload, proving the difference is the parser path

| mutation axis | variant | why it matters |
|---|---|---|
| context | `json_in_form_field` | double parse |
| protocol | `version_downgrade_path` | older contract, older guards |

**Detected by:** non canonical content type on a write

**Counter:** one parser per resource, reject alternates  
**Counter precondition:** content type allowlist  
**Counter cost:** low

---

## W02-0009: Write through an operation that was never designed as a write

**Atoms:** `A10` logic assumption violation, `A04` state confusion  
**State changed:** derived or cached state  
**Acting as:** the system itself  
**Persistence:** until recompute, sometimes forever  
**Status:** PROBABLE  
**Authorization:** written scope

Preconditions:
- a read or compute endpoint mutates state as a side effect
- the side effect is user influenceable

Procedure:
1. identify endpoints with side effects: view counters, exports, previews, previews of uploads, report generators
2. influence inputs so the side effect writes attacker chosen data
3. verify persistence across sessions

**Oracle:** `the derived value changes and persists`, `a fresh session sees it`  
**Negative control:** the same endpoint with benign input produces a different, expected derived value

| mutation axis | variant | why it matters |
|---|---|---|
| timing | `trigger via scheduled job` | deferred write |

**Detected by:** state change on a GET

**Counter:** no state change on safe methods  
**Counter precondition:** enforced by framework or review  
**Counter cost:** low

---

## W02-0010: Authorisation evaluated on a stale copy of the object

**Atoms:** `A04` state confusion, `A12` timing and ordering  
**State changed:** the object's security attributes  
**Acting as:** a user whose access was just revoked  
**Persistence:** window dependent  
**Status:** PROBABLE  
**Authorization:** written scope, an account you can revoke

Preconditions:
- authorisation reads a cached or denormalised copy
- the copy is refreshed lazily
- revocation is not pushed

Procedure:
1. grant access, then revoke it
2. immediately attempt the write repeatedly
3. measure the window where the write still succeeds

**Oracle:** `write succeeds after revocation, and the audit log timestamp proves ordering`  
**Negative control:** the same write after the cache TTL fails, bounding the window

| mutation axis | variant | why it matters |
|---|---|---|
| timing | `parallel_revoke_and_write` | race the refresh |

**Detected by:** access decision timestamp versus revocation timestamp

**Counter:** authorise against the authoritative store, or push invalidation synchronously  
**Counter precondition:** revocation must be synchronous  
**Counter cost:** latency

---

## W02-0011: Identifier harvested from a public surface unlocks the write

**Atoms:** `A02` trust boundary crossing, `A08` information exposure  
**State changed:** an object the attacker did not enumerate, only discovered  
**Acting as:** the victim owner  
**Persistence:** as long as the object lives  
**Status:** VERIFIED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- ids are unguessable but published somewhere
- the write endpoint trusts the id alone
- no session ownership check

Procedure:
1. harvest ids from public feeds: sitemaps, JS, RSS, API listings, emails, embeds
2. take one id belonging to another account
3. issue the update with your own session

**Oracle:** `owner sees the change on their next read`, `the response echoes the new value`  
**Negative control:** a random id of the same shape returns 404, proving existence matters and success is real

| mutation axis | variant | why it matters |
|---|---|---|
| encoding | `uuid_without_hyphens` | parser may accept and match both forms |

**Detected by:** write on object whose id never appeared in this session

**Counter:** object level authorisation independent of id secrecy  
**Counter precondition:** never treat unguessable as authorisation  
**Counter cost:** one scoped query

**Tools (resolve in ai-web-arsenal):** `d11-ffuf`

---

## W02-0012: Child object write under a parent you do not own

**Atoms:** `A02` trust boundary crossing, `A06` path and namespace confusion  
**State changed:** a nested collection element  
**Acting as:** the parent owner  
**Persistence:** visible immediately to the parent owner  
**Status:** VERIFIED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- nested routes authorise the parent only on read
- create validates the parent exists, not that you own it

Procedure:
1. find a nested create route, parent slash child
2. create a child under a victim parent
3. read the parent as the victim

**Oracle:** `child appears in the victim's nested listing`  
**Negative control:** creating under a nonexistent parent fails, isolating the flaw to the ownership check

| mutation axis | variant | why it matters |
|---|---|---|
| protocol | `flat_endpoint_with_parent_in_body` | parent check may only exist on the nested route |

**Detected by:** child created under a parent outside session scope

**Counter:** authorise the parent on every nested operation  
**Counter precondition:** nested routes inherit nothing  
**Counter cost:** one lookup

---

## W02-0013: Membership add as a privilege escalation primitive

**Atoms:** `A02` trust boundary crossing, `A03` identity confusion  
**State changed:** a group, team or project membership list  
**Acting as:** the group owner or an admin role  
**Persistence:** permanent until removed  
**Status:** VERIFIED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- an add member endpoint exists
- it checks that you are a member, not that you may add
- role defaults are privileged

Procedure:
1. join or create a low privilege group
2. attempt to add yourself or another account to a privileged group
3. check whether the added role can be chosen

**Oracle:** `the added account can perform privileged actions`, `membership visible to a genuine admin`  
**Negative control:** adding to a group you were removed from fails, proving membership state is enforced

| mutation axis | variant | why it matters |
|---|---|---|
| type | `role_field_optional` | omitted role may default to highest |

**Detected by:** membership change without an owner initiated event

**Counter:** separate permission to add from permission to be added  
**Counter precondition:** role supplied by server per inviter privilege  
**Counter cost:** one policy check

---

## W02-0014: Invitation flow used to mint a privileged account

**Atoms:** `A02` trust boundary crossing, `A10` logic assumption violation  
**State changed:** an account and its role assignment  
**Acting as:** the inviter role  
**Persistence:** permanent  
**Status:** VERIFIED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- invites carry a role
- the inviter role is checked at send time only
- the accepting account can change its own role or the invite role is echoed

Procedure:
1. invite an address you control with the lowest role
2. observe the invite payload and acceptance request
3. attempt to modify the role during acceptance

**Oracle:** `accepted account has the higher role`, `privilege usable in a follow up request`  
**Negative control:** accepting with an unmodified payload yields the low role, proving the difference is your change

| mutation axis | variant | why it matters |
|---|---|---|
| timing | `role_changed_after_invite_sent` | invite may freeze the role at send |

**Detected by:** role at acceptance differs from role at invitation

**Counter:** role determined server side at acceptance from the inviter's authority  
**Counter precondition:** invite token binds role  
**Counter cost:** one comparison

---

## W02-0015: Duplicate parameter decides which role is written

**Atoms:** `A05` type and shape confusion, `A02` trust boundary crossing  
**State changed:** the persisted role on an account  
**Acting as:** you, escalated  
**Persistence:** permanent  
**Status:** VERIFIED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- parameter parsing differs between the validator and the writer
- duplicate keys allowed

Procedure:
1. send the role parameter twice with different values
2. try order variants and encodings
3. re-read the account

**Oracle:** `persisted role is the value the validator saw as benign`, `privilege confirmed by action`  
**Negative control:** a single well formed low role persists as low, proving the duplicate is the cause

| mutation axis | variant | why it matters |
|---|---|---|
| encoding | `body_and_query_both` | frameworks merge in different order |

**Detected by:** duplicate security parameter

**Counter:** reject duplicate parameters, parse once  
**Counter precondition:** same parser for validate and write  
**Counter cost:** low

---

## W02-0016: Import feature overwrites records it does not own

**Atoms:** `A02` trust boundary crossing, `A10` logic assumption violation  
**State changed:** existing rows matched by an external key  
**Acting as:** the record owners  
**Persistence:** destructive, often unrecoverable  
**Status:** VERIFIED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- import matches on a natural key
- no ownership scoping on the match
- upsert semantics

Procedure:
1. export a sample to learn the column shape
2. craft rows whose natural key collides with another account's records
3. import

**Oracle:** `victim record values change`, `import report shows updates, not inserts`  
**Negative control:** rows with a fresh key insert instead of update, proving the match path is live

| mutation axis | variant | why it matters |
|---|---|---|
| context | `alternate_delimiter` | different importers validate differently |

**Detected by:** import updating rows outside the importer scope

**Counter:** scope the match query to the importer's tenant and objects  
**Counter precondition:** upsert never resolves globally  
**Counter cost:** one predicate

---

## W02-0017: Webhook configuration as a write primitive

**Atoms:** `A02` trust boundary crossing, `A10` logic assumption violation, `A07` resource exhaustion  
**State changed:** outbound integration configuration  
**Acting as:** the workspace admin  
**Persistence:** until changed, and every future event leaks  
**Status:** VERIFIED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- any member may set a webhook url
- no approval step
- secret is either optional or returned on read

Procedure:
1. create or modify the webhook url to a host you control
2. trigger an event
3. inspect what the platform sends, headers and body

**Oracle:** `your endpoint receives an authenticated request`, `payload contains data you can correlate`  
**Negative control:** an unrelated event type does not fire, proving the event trigger, not a generic probe

| mutation axis | variant | why it matters |
|---|---|---|
| protocol | `internal_hostname` | server side request from inside the perimeter |

**Detected by:** webhook target changes by non admin

**Counter:** admin only, destination allowlist, egress filtering  
**Counter precondition:** secret never readable after creation  
**Counter cost:** policy plus network

---

## W02-0018: API key scope not enforced on the write path

**Atoms:** `A02` trust boundary crossing, `A03` identity confusion  
**State changed:** a resource the key should only read  
**Acting as:** the key owner  
**Persistence:** as long as the change lasts  
**Status:** VERIFIED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- scopes are declared
- enforcement is per route group, not per method
- read scope present

Procedure:
1. obtain a read only key
2. issue a write with it
3. compare with the documented scope

**Oracle:** `write succeeds and is visible`, `audit attributes the change to the key`  
**Negative control:** a key with no scopes fails the same write, proving scopes exist and are partially enforced

| mutation axis | variant | why it matters |
|---|---|---|
| protocol | `batch_or_bulk_route` | bulk routes often mount under a different group |

**Detected by:** write attributed to a read scoped key

**Counter:** scope check at the handler, derived from the route  
**Counter precondition:** no route reuses a group with different requirements  
**Counter cost:** one attribute read

---

## W02-0019: OAuth scope upgraded on refresh or re-consent

**Atoms:** `A02` trust boundary crossing, `A03` identity confusion  
**State changed:** the granted scope set of a token  
**Acting as:** the resource owner  
**Persistence:** for the token lifetime, refreshable  
**Status:** VERIFIED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- refresh accepts a scope parameter
- the original grant is not checked against the request
- consent screen is not re-shown

Procedure:
1. request a low scope
2. refresh while requesting a higher scope
3. use the new token

**Oracle:** `the new token performs the higher scope action`, `token introspection shows the expanded scope`  
**Negative control:** refreshing without the scope parameter keeps the low scope

| mutation axis | variant | why it matters |
|---|---|---|
| context | `scope_in_body_not_query` | different validation site |

**Detected by:** scope expansion at refresh

**Counter:** refresh scope must be a subset of the original grant  
**Counter precondition:** grant recorded  
**Counter cost:** one comparison

**Tools (resolve in ai-web-arsenal):** `d11-jwt_tool`

---

## W02-0020: Support impersonation used to perform the write

**Atoms:** `A03` identity confusion, `A02` trust boundary crossing, `A14` human manipulation  
**State changed:** anything the impersonated user owns  
**Acting as:** the customer  
**Persistence:** permanent, logged as the customer  
**Status:** VERIFIED  
**Authorization:** written scope plus a support role provisioned for the test

Preconditions:
- impersonation exists for support
- the operator is not restricted to read
- audit attributes to the customer not the operator

Procedure:
1. invoke the impersonation feature on an account you control
2. perform a write
3. inspect the audit trail

**Oracle:** `the write lands on the customer account`, `audit shows the customer as actor`  
**Negative control:** direct write as the operator is attributed to the operator, isolating the attribution flaw

| mutation axis | variant | why it matters |
|---|---|---|
| timing | `impersonate_then_revoke` | session may outlive revocation |

**Detected by:** support session performing writes

**Counter:** read only impersonation by default, dual attribution in audit  
**Counter precondition:** operator identity always recorded  
**Counter cost:** one flag

---

## W02-0021: Version history restore bypasses the current authorisation

**Atoms:** `A04` state confusion, `A02` trust boundary crossing  
**State changed:** the object's content, reverted  
**Acting as:** a principal who had access before  
**Persistence:** permanent, and it overwrites current content  
**Status:** VERIFIED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- version history exists
- restore authorises against the version owner, not the object owner
- removed collaborators can still restore

Procedure:
1. get removed from an object you previously edited
2. attempt restore of your old version
3. read the object as the current owner

**Oracle:** `content reverts`, `owner sees an unexpected change from a non collaborator`  
**Negative control:** restore by a never collaborator fails, proving the check is version history based

| mutation axis | variant | why it matters |
|---|---|---|
| type | `restore_by_version_id_only` | version ids may not be tenant scoped |

**Detected by:** restore by non current collaborator

**Counter:** authorise restore against current permissions on the parent  
**Counter precondition:** version ids scoped  
**Counter cost:** one check

---

## W02-0022: Draft state is permissive and publication skips the check

**Atoms:** `A10` logic assumption violation, `A04` state confusion  
**State changed:** a draft that becomes public  
**Acting as:** the publisher  
**Persistence:** publication makes it permanent  
**Status:** VERIFIED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- drafts saved with weaker validation
- publish is a separate transition
- publish does not re-run validation

Procedure:
1. save a draft with content the publish path would reject
2. publish directly via the transition endpoint
3. or share the draft link

**Oracle:** `published content renders the rejected payload`, `the share link works before publish`  
**Negative control:** publishing content that is valid anyway produces no finding, isolating the path

| mutation axis | variant | why it matters |
|---|---|---|
| protocol | `transition_endpoint_direct` | UI hides it, API does not |

**Detected by:** publish without a validation event

**Counter:** validate at every transition, treat drafts as untrusted  
**Counter precondition:** no trust in earlier state  
**Counter cost:** revalidate

---

## W02-0023: Self approval inside a workflow

**Atoms:** `A10` logic assumption violation, `A02` trust boundary crossing  
**State changed:** the approval status of a request  
**Acting as:** the requester  
**Persistence:** permanent record of false approval  
**Status:** VERIFIED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- workflow requires an approver
- approver role is assignable to the requester
- no separation of duties check

Procedure:
1. submit a request
2. assign yourself, or a second account you control, as approver
3. approve

**Oracle:** `request leaves pending state`, `the effect of the request occurs`  
**Negative control:** approval by an unrelated third account is rejected, proving approval is not simply open

| mutation axis | variant | why it matters |
|---|---|---|
| timing | `approve_before_request_completes` | race in state machine |

**Detected by:** requester and approver identity equal

**Counter:** separation of duties enforced server side  
**Counter precondition:** approver cannot be requester  
**Counter cost:** one comparison

---

## W02-0024: Quota or limit reset endpoint used to write demand

**Atoms:** `A07` resource exhaustion, `A10` logic assumption violation  
**State changed:** the usage counter for an account  
**Acting as:** the account owner  
**Persistence:** repeatedly exploitable  
**Status:** PROBABLE  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- a reset or upgrade endpoint exists
- reset authorises the account but not the eligibility
- no idempotency

Procedure:
1. exhaust a quota
2. call the reset or upgrade with altered plan or scope parameters
3. observe counter and access to paid features

**Oracle:** `counter resets out of cycle`, `paid feature becomes usable`  
**Negative control:** reset on a fully used free account after the intended window is rejected

| mutation axis | variant | why it matters |
|---|---|---|
| type | `negative_increment` | arithmetic on counters |

**Detected by:** counter reset frequency per account

**Counter:** eligibility checked server side, counters append only  
**Counter precondition:** no client supplied plan  
**Counter cost:** one check

---

## W02-0025: Referral or points ledger written without a real event

**Atoms:** `A10` logic assumption violation, `A12` timing and ordering  
**State changed:** a balance in a rewards ledger  
**Acting as:** the account  
**Persistence:** monetisable, until reconciled  
**Status:** PROBABLE  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- credit is granted on a client observable event
- no server verification of the event
- credit is idempotent by request only

Procedure:
1. trigger the qualifying event once
2. replay the credit request
3. or self refer between two accounts

**Oracle:** `balance exceeds what the events justify`, `redemption succeeds`  
**Negative control:** the same request for an ineligible account credits nothing

| mutation axis | variant | why it matters |
|---|---|---|
| timing | `parallel_replay` | idempotency key absent |

**Detected by:** credit without matching qualifying event

**Counter:** credit from server verified events, idempotency keys  
**Counter precondition:** never trust a client signal  
**Counter cost:** event store

---

## W02-0026: Log injection used to write into the audit trail

**Atoms:** `A01` interpreter confusion, `A08` information exposure  
**State changed:** the integrity of the audit record  
**Acting as:** the system  
**Persistence:** permanent, and it poisons future forensics  
**Status:** PROBABLE  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- user input reaches a log line unescaped
- the log is the evidence source
- downstream log parser or SIEM

Procedure:
1. submit a value containing newlines and structured fields
2. locate the resulting log entry
3. check whether a forged entry or altered attribution appears

**Oracle:** `a forged line appears in the log source`, `or the real line is broken into a misleading entry`  
**Negative control:** a benign value produces one clean line, proving the injection did the work

| mutation axis | variant | why it matters |
|---|---|---|
| encoding | `json_breakout` | structured logging may parse your payload |

**Detected by:** log lines without a matching request record

**Counter:** structured logging with escaping, append only store  
**Counter precondition:** log parser treats fields as data  
**Counter cost:** low

---

## W02-0027: Shared cache key collision overwrites another user's view

**Atoms:** `A06` path and namespace confusion, `A04` state confusion  
**State changed:** a cached response served to others  
**Acting as:** whoever requests next  
**Persistence:** until TTL, seen by many users  
**Status:** VERIFIED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- cache key omits a varying element such as user, tenant or header
- shared cache in front of personalised content

Procedure:
1. determine the cache key by varying one input at a time
2. cause a personalised response to be stored under a key others share
3. request the same key from a different session

**Oracle:** `second session receives content belonging to the first`, `the response carries the first user's data`  
**Negative control:** a request with a cache bypass header returns your own content, proving the difference is the cache

| mutation axis | variant | why it matters |
|---|---|---|
| protocol | `host_or_scheme_in_key` | key normalisation differs by CDN |

**Detected by:** cache hit with a session specific body

**Counter:** include every varying input in the key, or do not cache personalised responses  
**Counter precondition:** cache key reviewed per route  
**Counter cost:** design

---

## W02-0028: Shared edit link grants more than the sharer intended

**Atoms:** `A02` trust boundary crossing, `A03` identity confusion  
**State changed:** the permission level attached to a link token  
**Acting as:** the sharer  
**Persistence:** until revoked, sometimes unrevocable  
**Status:** VERIFIED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- links carry a permission claim
- the claim is chosen by the sharer or mutable client side
- acceptance trusts the link over the account

Procedure:
1. create a read link
2. inspect the token payload
3. attempt to raise the permission claim, or use the read token on a write route

**Oracle:** `write succeeds through a read link`, `or the token decodes to a higher permission`  
**Negative control:** a revoked link fails, proving link state is enforced

| mutation axis | variant | why it matters |
|---|---|---|
| encoding | `token_prefix_variants` | different parsers |

**Detected by:** link token used for an action its claim forbids

**Counter:** server side permission per link, short expiry, revocable  
**Counter precondition:** claims not trusted alone  
**Counter cost:** one lookup

**Tools (resolve in ai-web-arsenal):** `d11-jwt_tool`

---

## W02-0029: Email change without verification starts an account takeover chain

**Atoms:** `A03` identity confusion, `A10` logic assumption violation  
**State changed:** the recovery identity of the account  
**Acting as:** the account owner  
**Persistence:** permanent unless noticed  
**Status:** VERIFIED  
**Authorization:** written scope, accounts you fully control

Preconditions:
- email change does not require confirmation from the old address
- recovery uses the new address
- no notification to the old address

Procedure:
1. on your own account, change the email to a second address you control
2. observe whether the old address must confirm
3. on a test account where you control the original, do the same and confirm the takeover path

**Oracle:** `the new address receives recovery mail`, `the old address cannot recover`  
**Negative control:** changing to an address that already exists is rejected, proving some validation runs

| mutation axis | variant | why it matters |
|---|---|---|
| timing | `change_then_revert_race` | notification and state update order |

**Detected by:** email change without old address confirmation

**Counter:** confirm from the old address, notify both, delay recovery  
**Counter precondition:** recovery binds to a verified identity  
**Counter cost:** flow change

---

## W02-0030: Reset token reusable or raced across two requests

**Atoms:** `A12` timing and ordering, `A03` identity confusion  
**State changed:** the account password  
**Acting as:** the owner  
**Persistence:** takeover  
**Status:** VERIFIED  
**Authorization:** written scope, accounts you control

Preconditions:
- reset token single use is not enforced atomically
- or the token remains valid until expiry
- or two tokens can be valid at once

Procedure:
1. request a reset on an account you control
2. use the token once, then attempt a second use
3. or send two concurrent uses and observe both succeeding

**Oracle:** `second use accepted`, `password changes twice, or a stale token still works`  
**Negative control:** a token after the documented expiry is rejected, proving expiry is enforced and single use is not

| mutation axis | variant | why it matters |
|---|---|---|
| timing | `parallel_two_tokens` | older token may not be invalidated |

**Detected by:** reset token used more than once

**Counter:** atomic single use, invalidate siblings on issue  
**Counter precondition:** token consumption is a compare and set  
**Counter cost:** one transaction

---

## W02-0031: Alias or plus addressing resolves to a victim identity

**Atoms:** `A03` identity confusion, `A10` logic assumption violation  
**State changed:** which account an email maps to  
**Acting as:** the victim  
**Persistence:** permanent  
**Status:** PROBABLE  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- registration or verification normalises addresses loosely
- a secondary alias can be added without verifying the primary
- lookup is case or plus insensitive

Procedure:
1. add an address variant that normalises to a victim's account
2. attempt password reset or invitation acceptance
3. observe which account receives the effect

**Oracle:** `the effect lands on the victim account`, `or the variant is accepted as already registered`  
**Negative control:** a genuinely unrelated address is treated as new, proving normalisation did the join

| mutation axis | variant | why it matters |
|---|---|---|
| encoding | `dots_in_local_part` | provider specific normalisation |

**Detected by:** account resolution across normalised variants

**Counter:** exact match identity, verify before linking  
**Counter precondition:** normalisation never merges accounts  
**Counter cost:** low

---

## W02-0032: Identity provider attribute maps straight into a role

**Atoms:** `A03` identity confusion, `A05` type and shape confusion  
**State changed:** the role assigned at login  
**Acting as:** the assertion issuer  
**Persistence:** until next login, or permanent if persisted  
**Status:** VERIFIED  
**Authorization:** written scope, a test tenant you own

Preconditions:
- roles derive from an assertion attribute
- attribute is one the user can influence at the IdP
- no allowlist mapping

Procedure:
1. inspect the assertion after login
2. identify which attribute maps to role
3. change that attribute in a tenant or profile you control, or in a self service IdP
4. log in again

**Oracle:** `role changes in the application`, `privileged action succeeds`  
**Negative control:** changing an unrelated attribute does not affect role, isolating the mapping

| mutation axis | variant | why it matters |
|---|---|---|
| context | `display_name_injection` | some SPs map by name pattern |

**Detected by:** role differs from directory group

**Counter:** map roles from groups the app controls, not free attributes  
**Counter precondition:** no user writable attribute is authoritative  
**Counter cost:** sync

---

## W02-0033: Provisioning endpoint accepts writes it should reserve for the IdP

**Atoms:** `A02` trust boundary crossing, `A03` identity confusion  
**State changed:** user records and group memberships  
**Acting as:** the provisioning system  
**Persistence:** permanent  
**Status:** VERIFIED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- SCIM or equivalent endpoint exposed
- authenticated by a static token or by the app session
- no source restriction

Procedure:
1. locate the provisioning route
2. attempt a create or patch with an application session rather than the provisioning token
3. attempt with a leaked or default token

**Oracle:** `user created or modified`, `group membership changed`  
**Negative control:** the same request without any credential is rejected, proving the endpoint itself is live

| mutation axis | variant | why it matters |
|---|---|---|
| protocol | `patch_with_filter` | filter based patch may bypass per object checks |

**Detected by:** provisioning calls from non IdP source

**Counter:** mutual auth, source allowlist, separate audience  
**Counter precondition:** not reachable from the internet  
**Counter cost:** infra

---

## W02-0034: Directory sync overwrites local attributes it should not own

**Atoms:** `A04` state confusion, `A05` type and shape confusion  
**State changed:** locally managed fields such as role or quota  
**Acting as:** the sync job  
**Persistence:** on every sync cycle  
**Status:** PROBABLE  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- sync writes the full record
- source of truth is partial
- local overrides not protected

Procedure:
1. set a local attribute the directory does not carry
2. trigger a sync
3. check whether the local value survives

**Oracle:** `local value reverted or blanked`, `sync log shows a write to that field`  
**Negative control:** a field the directory owns survives correctly, proving the sync path and isolating the overreach

| mutation axis | variant | why it matters |
|---|---|---|
| timing | `sync_during_update` | last writer wins race |

**Detected by:** sync writing fields outside its scope

**Counter:** field level ownership between systems  
**Counter precondition:** explicit ownership matrix  
**Counter cost:** mapping review

---

## W02-0035: GraphQL aliases multiply a mutation past its guard

**Atoms:** `A07` resource exhaustion, `A02` trust boundary crossing  
**State changed:** many objects, one request  
**Acting as:** mixed  
**Persistence:** scales with alias count  
**Status:** VERIFIED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- a single mutation is authorised once per request
- aliases allow the same field many times
- cost limits per operation absent

Procedure:
1. issue one request containing the same mutation under many aliases with different ids
2. observe which succeed
3. check rate limiting and per object authorisation

**Oracle:** `multiple objects changed in one request`, `rate limiter counted one`  
**Negative control:** the same ids issued as separate requests hit the limit or the guard

| mutation axis | variant | why it matters |
|---|---|---|
| volume | `fragments_to_repeat` | operation counting differs |

**Detected by:** operation count versus request count

**Counter:** cost analysis per operation, authorise per node  
**Counter precondition:** aliases counted  
**Counter cost:** engine config

**Tools (resolve in ai-web-arsenal):** `d11-batchql`

---

## W02-0036: GraphQL input coercion supplies a value the UI never sends

**Atoms:** `A05` type and shape confusion  
**State changed:** a field the schema accepts but the form does not offer  
**Acting as:** you  
**Persistence:** varies  
**Status:** VERIFIED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- input type has optional fields
- resolver writes them without an allowlist
- defaults are privileged

Procedure:
1. introspect the mutation input type
2. send fields the UI omits
3. check which persist

**Oracle:** `field persisted on re-read`, `behaviour changes`  
**Negative control:** a field not in the input type is rejected by validation, proving the schema is enforced and the flaw is permit-by-schema

| mutation axis | variant | why it matters |
|---|---|---|
| type | `enum_by_name` | enum coercion may accept unknown names |

**Detected by:** mutation writing a field not present in the UI schema

**Counter:** allowlist at the resolver, not the schema  
**Counter precondition:** schema is not the permission model  
**Counter cost:** one check

**Tools (resolve in ai-web-arsenal):** `d11-inql`

---

## W02-0037: Protobuf field presence lets a client clear a protected value

**Atoms:** `A05` type and shape confusion, `A04` state confusion  
**State changed:** an optional field on an object  
**Acting as:** you  
**Persistence:** permanent  
**Status:** PROBABLE  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- proto3 optional or wrapper types
- server treats absence and default differently
- no server side allowlist on which fields may be cleared

Procedure:
1. send an update that omits or zeroes a field
2. observe whether the server clears it
3. target a field that gates behaviour, such as a security flag

**Oracle:** `the field is cleared and the behaviour changes`, `or the default applies`  
**Negative control:** a field the server owns stays unchanged, proving the difference is presence handling

| mutation axis | variant | why it matters |
|---|---|---|
| type | `explicit_null_vs_absent` | JSON gateway flattens both |

**Detected by:** update clearing a non editable field

**Counter:** field masks with an allowlist  
**Counter precondition:** absence never means clear  
**Counter cost:** one mask

**Tools (resolve in ai-web-arsenal):** `d11-grpcurl`

---

## W02-0038: Duplicate JSON keys split validation from persistence

**Atoms:** `A05` type and shape confusion, `A06` path and namespace confusion  
**State changed:** any field written from JSON  
**Acting as:** you  
**Persistence:** permanent  
**Status:** VERIFIED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- one parser validates, another persists
- duplicate keys tolerated
- different last wins behaviour

Procedure:
1. send the field twice with a benign and a hostile value
2. try both orders
3. compare what validation saw with what persisted

**Oracle:** `persisted value differs from the value that passed validation`, `or the role or price reflects the second key`  
**Negative control:** a single key with the hostile value is rejected, proving duplicates are the mechanism

| mutation axis | variant | why it matters |
|---|---|---|
| encoding | `escaped_key_names` | unicode escapes bypass naive dedupe |

**Detected by:** duplicate keys in a security relevant object

**Counter:** strict parser, reject duplicates  
**Counter precondition:** one parser for the whole path  
**Counter cost:** low

---

## W02-0039: Null versus absent decides whether a guard runs

**Atoms:** `A05` type and shape confusion, `A04` state confusion  
**State changed:** the state a guard depends on  
**Acting as:** you  
**Persistence:** varies  
**Status:** VERIFIED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- code branches on null
- absent means skip, null means check, or the reverse
- partial update semantics

Procedure:
1. send the field as null
2. send it absent
3. send an empty string
4. compare which branch executed by observing behaviour

**Oracle:** `a guard skipped or applied differently per variant`, `state change proves it`  
**Negative control:** the normal value behaves identically in all cases, isolating the null path

| mutation axis | variant | why it matters |
|---|---|---|
| type | `empty_array` | may be treated as absent by one layer |

**Detected by:** null on a required security field

**Counter:** explicit state machine, no null branch for authz  
**Counter precondition:** three states handled deliberately  
**Counter cost:** code review

---

## W02-0040: Quantity arithmetic overflows or wraps at the write

**Atoms:** `A05` type and shape confusion, `A10` logic assumption violation  
**State changed:** an order total, balance or stock level  
**Acting as:** you  
**Persistence:** monetary  
**Status:** VERIFIED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- quantity is parsed to a fixed width integer
- no range check before arithmetic
- total computed server side from quantity

Procedure:
1. submit a quantity near the type boundary
2. then try one beyond it
3. observe total, stock and any credit

**Oracle:** `total wraps to a small or negative value`, `order accepted at an impossible price`  
**Negative control:** a large but in range quantity produces the expected total, proving the boundary is the cause

| mutation axis | variant | why it matters |
|---|---|---|
| type | `float_precision` | 0.1 style rounding in totals |

**Detected by:** quantity outside business range

**Counter:** bounded integers, server side totals  
**Counter precondition:** validate range before arithmetic  
**Counter cost:** low

---

## W02-0041: Negative or zero value passes a check written for positives

**Atoms:** `A10` logic assumption violation, `A05` type and shape confusion  
**State changed:** a ledger entry or entitlement  
**Acting as:** you  
**Persistence:** monetary  
**Status:** VERIFIED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- validation checks an upper bound only
- sign not enforced
- arithmetic on the value credits the account

Procedure:
1. submit a negative quantity or price
2. observe direction of the ledger change
3. try zero and fractional variants

**Oracle:** `balance increases on a transaction that should cost`, `or an entitlement is granted`  
**Negative control:** the same magnitude positive produces the expected debit, isolating the sign check

| mutation axis | variant | why it matters |
|---|---|---|
| type | `unicode_minus` | parser may accept then coerce |

**Detected by:** negative amount in a debit context

**Counter:** sign and range validation per field  
**Counter precondition:** domain specific bounds  
**Counter cost:** low

---

## W02-0042: Unicode normalisation makes two identifiers collide

**Atoms:** `A06` path and namespace confusion, `A03` identity confusion  
**State changed:** uniqueness of a username or slug  
**Acting as:** the victim  
**Persistence:** permanent, and enables impersonation  
**Status:** VERIFIED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- registration normalises, lookup does not, or the reverse
- uniqueness index on raw bytes
- confusables allowed

Procedure:
1. register an identifier that normalises to a victim's
2. or that differs only by a confusable or combining mark
3. attempt login, mention or invite resolution

**Oracle:** `you receive actions meant for the victim`, `or the system treats both as the same account`  
**Negative control:** a clearly distinct identifier behaves distinctly, proving normalisation is the join

| mutation axis | variant | why it matters |
|---|---|---|
| encoding | `homoglyph` | visual impersonation with no byte equality |

**Detected by:** identifier with mixed scripts or combining marks

**Counter:** single normalisation form, enforced at write and lookup  
**Counter precondition:** confusable policy  
**Counter cost:** low

---

## W02-0043: Case insensitive storage collides with case sensitive authorisation

**Atoms:** `A06` path and namespace confusion, `A03` identity confusion  
**State changed:** account or object identity  
**Acting as:** the victim  
**Persistence:** permanent  
**Status:** PROBABLE  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- storage compares case insensitively
- authorisation or token subject compares exactly
- or the reverse

Procedure:
1. register a case variant of a target identifier
2. attempt to act where the exact case is expected
3. observe which layer matched

**Oracle:** `action succeeds against the victim's object`, `or the variant inherits the victim's session`  
**Negative control:** a variant that differs by more than case is treated as distinct

| mutation axis | variant | why it matters |
|---|---|---|
| encoding | `unicode_case_folding` | non ASCII case rules differ |

**Detected by:** case variant of an existing identifier

**Counter:** one comparison rule everywhere  
**Counter precondition:** documented collation  
**Counter cost:** low

---

## W02-0044: Trailing whitespace or control characters create a shadow identity

**Atoms:** `A06` path and namespace confusion, `A03` identity confusion  
**State changed:** an identifier that resolves ambiguously  
**Acting as:** the victim  
**Persistence:** permanent  
**Status:** PROBABLE  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- leading or trailing space trimmed at some layers
- unique index on raw value
- lookup trims

Procedure:
1. register an identifier with a trailing space or zero width character
2. attempt login and resolution as the plain identifier
3. observe which account is used

**Oracle:** `you are mapped to the victim account, or vice versa`, `or both can be registered`  
**Negative control:** an identifier with an interior space is rejected, proving trimming specifically is the issue

| mutation axis | variant | why it matters |
|---|---|---|
| encoding | `zero_width_joiner` | invisible and often untrimmed |

**Detected by:** identifier with control or invisible characters

**Counter:** strict identifier charset, trim before store  
**Counter precondition:** one canonical form  
**Counter cost:** low

---

## W02-0045: Identifier type juggling across query layers

**Atoms:** `A05` type and shape confusion, `A06` path and namespace confusion  
**State changed:** which object a request resolves to  
**Acting as:** the owner  
**Persistence:** varies  
**Status:** VERIFIED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- id accepted as string in one layer and int in another
- loose comparison somewhere
- arrays accepted

Procedure:
1. send the id as string, int, array and object
2. observe which form resolves and to what
3. try scientific notation and leading zeros

**Oracle:** `an id you should not access resolves`, `or a write lands on a different object than validated`  
**Negative control:** a strictly invalid type is rejected, proving type handling is partial

| mutation axis | variant | why it matters |
|---|---|---|
| type | `array_of_one` | framework binds arrays to single params |

**Detected by:** non canonical id type

**Counter:** typed binding at the edge  
**Counter precondition:** reject arrays on scalars  
**Counter cost:** low

---

## W02-0046: Archive extraction writes outside its intended directory

**Atoms:** `A06` path and namespace confusion, `A05` type and shape confusion  
**State changed:** the filesystem path of extracted content  
**Acting as:** the extractor  
**Persistence:** files persist  
**Status:** VERIFIED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- upload accepts an archive
- extraction trusts entry names
- no canonical path check after extraction

Procedure:
1. craft an archive with entries containing dot segments or absolute paths
2. upload and trigger extraction
3. read the expected out of place file back through the application

**Oracle:** `a file exists outside the extraction root`, `or a served path resolves to your file`  
**Negative control:** a normal archive extracts inside the root, proving the traversal is the cause

| mutation axis | variant | why it matters |
|---|---|---|
| encoding | `nested_archive` | second pass may skip the check |

**Detected by:** archive entry containing traversal

**Counter:** canonicalise and verify containment per entry  
**Counter precondition:** no symlink following  
**Counter cost:** low

---

## W02-0047: Rename or move endpoint reparents a file without rechecking

**Atoms:** `A06` path and namespace confusion, `A02` trust boundary crossing  
**State changed:** the location and owner of a file  
**Acting as:** the file owner  
**Persistence:** permanent  
**Status:** VERIFIED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- move accepts a destination id
- destination ownership not verified
- or move across tenants allowed

Procedure:
1. create a file in your own space
2. move it to a destination you do not own
3. read it as the destination owner

**Oracle:** `file appears in the victim space`, `or gains the victim space's sharing`  
**Negative control:** moving to a nonexistent destination fails, isolating the ownership check

| mutation axis | variant | why it matters |
|---|---|---|
| protocol | `copy_then_delete` | two operations, one guarded |

**Detected by:** move across ownership boundaries

**Counter:** authorise both source and destination  
**Counter precondition:** no implicit inherit  
**Counter cost:** two checks

---

## W02-0048: Share permission raised by the recipient

**Atoms:** `A02` trust boundary crossing, `A05` type and shape confusion  
**State changed:** the permission bit on a share  
**Acting as:** the sharer  
**Persistence:** until revoked, often unnoticed  
**Status:** VERIFIED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- share record is writable by the recipient
- permission field is in the update payload
- no check that the sharer granted it

Procedure:
1. accept a read only share
2. attempt to patch the share record's permission
3. or use a write route with the read share token

**Oracle:** `write through the share succeeds`, `share record shows the raised permission`  
**Negative control:** the same patch as an unrelated account is denied

| mutation axis | variant | why it matters |
|---|---|---|
| type | `role_name_synonyms` | different names map to the same level |

**Detected by:** share permission changed by recipient

**Counter:** only the sharer can change the grant  
**Counter precondition:** recipient is not an author of the grant  
**Counter cost:** one check

---

## W02-0049: Retired API version still writes with the old guard

**Atoms:** `A15` configuration divergence, `A06` path and namespace confusion  
**State changed:** the same records, through an older contract  
**Acting as:** you  
**Persistence:** permanent  
**Status:** VERIFIED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- v1 still reachable
- v1 predates the ownership check
- routing does not normalise to the current version

Procedure:
1. find an old version path in docs, mobile client or error messages
2. replay a write against it
3. compare the guard behaviour to the current version

**Oracle:** `v1 write succeeds where the current version denies`, `data visible in the current UI`  
**Negative control:** the same call to the current version is denied, proving the version delta

| mutation axis | variant | why it matters |
|---|---|---|
| protocol | `version_in_header` | different router |

**Detected by:** writes via deprecated versions

**Counter:** retire versions, or route them through the current policy layer  
**Counter precondition:** one policy enforcement point  
**Counter cost:** infra

---

## W02-0050: Legacy protocol endpoint bypasses the modern authorisation layer

**Atoms:** `A15` configuration divergence, `A06` path and namespace confusion  
**State changed:** records shared with the modern API  
**Acting as:** you  
**Persistence:** permanent  
**Status:** PROBABLE  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- SOAP or RPC endpoint still mounted
- it talks to the same store
- its auth is older or weaker

Procedure:
1. enumerate legacy endpoints from WSDL, docs, error pages or client binaries
2. perform a write with legacy auth
3. read the result through the modern interface

**Oracle:** `record changed and visible in the modern UI`, `legacy response confirms success`  
**Negative control:** the same write through the modern interface with equivalent credentials is denied

| mutation axis | variant | why it matters |
|---|---|---|
| protocol | `soap_action_header` | routing and auth keyed on it |

**Detected by:** legacy protocol writes

**Counter:** decommission or front with one policy proxy  
**Counter precondition:** no parallel auth stacks  
**Counter cost:** infra

---
