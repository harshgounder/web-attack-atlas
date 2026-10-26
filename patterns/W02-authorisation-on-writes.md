# W02: authorisation on writes

Generated from `waves/W02/patterns.jsonl`. Do not edit by hand.
10 patterns. Every one answers the five questions and carries a counter.

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
