# W01: write primitives and object lifecycle

Generated from `waves/W01/patterns.jsonl`. Do not edit by hand.
50 patterns. Every one answers the five questions and carries a counter.

## Index

| id | pattern | atoms | persists | counter mechanism |
|---|---|---|---|---|
| W01-0001 | Parallel creates bypass a uniqueness check that is not atomic | A04, A12 | permanent duplicate records | unique constraint in the store, not in code |
| W01-0002 | Lost update overwrites a concurrent change silently | A04, A12 | the earlier change is gone | optimistic concurrency via version or ETag, or field level patch |
| W01-0003 | Partial update resets omitted fields to defaults | A05, A04 | permanent data loss | patch semantics with explicit presence handling |
| W01-0004 | Client supplied identifier chosen on create | A03, A05 | permanent | server generates ids, ignore client values |
| W01-0005 | Client supplied timestamps forge the audit trail | A05, A11 | permanent in records and logs | server clock only, ignore client time |
| W01-0006 | State set directly instead of through the transition endpoint | A10, A04 | permanent, skips approvals | state not bindable, transitions only |
| W01-0007 | Immutable identity fields are mutable on update | A05, A06 | permanent | immutable after create, enforced in the writer |
| W01-0008 | Foreign key swapped on update reparents the object | A06, A02 | permanent | parent change is an authorised operation with both sides checked |
| W01-0009 | Delete leaves children reachable by their own route | A04, A08 | permanent | cascade or tombstone plus parent check on child reads |
| W01-0010 | Soft delete filtered on read but not on write | A04 | until purge | deleted predicate in the writer and the reader |
| W01-0011 | Restore returns an object into a changed world | A04, A06 | permanent | revalidate references on restore |
| W01-0012 | Draft autosave overwrites published content | A04, A10 | public | separate draft from published, publish copies |
| W01-0013 | Merge operation accepts a source you do not own | A02, A04 | permanent and destructive | authorise both operands |
| W01-0014 | Clone copies fields the original kept private | A08, A05 | permanent | clone from an allowlist projection |
| W01-0015 | Bulk update selects rows by filter rather than explicit ids | A06, A10 | mass modification | bulk writes take ids, filters are read only |
| W01-0016 | Sort and filter parameters reach the query builder | A01, A05 | read mostly, write if the same builder is reused | allowlist sortable and filterable fields |
| W01-0017 | Create with a reference to a private object is an existence oracle | A08, A05 | none, it is inference | uniform errors, rate limit, scope check before existence |
| W01-0018 | Duplicate ids inside one payload produce a partial write | A05, A04 | unpredictable | reject duplicates, transactional batch, honest reporting |
| W01-0019 | Delete via a safe method or a prefetchable link | A06, A04 | permanent | safe methods never mutate, confirmation for destructive ops |
| W01-0020 | Update resurrects an object mid delete | A04, A12 | until next purge | state transition guarded by a conditional write |
| W01-0021 | Export and reimport roundtrip changes security attributes | A04, A05 | permanent after import | roundtrip test in CI, explicit defaults |
| W01-0022 | Trash and recycle bin reachable without the parent check | A02, A08 | until purge | trash is a scoped view like any other |
| W01-0023 | Undo restores a state that was superseded | A04, A10 | permanent | undo targets a version and rejects if superseded |
| W01-0024 | Delete removes the record but not the stored blobs | A06, A08 | forever | delete orchestrates storage, short lived signed urls |
| W01-0025 | Counters drift because increments have no matching decrement | A04, A10 | permanent drift | derive counters, or make them transactional |
| W01-0026 | Update leaves the version unchanged so caches keep serving old data | A04, A06 | until TTL | bump the validator on every write |
| W01-0027 | Write does not invalidate derived stores | A04, A08 | until rebuild | outbox pattern with reconciliation |
| W01-0028 | Client assigns the sequence or ticket number | A10, A05 | permanent | server assigns, enforced unique |
| W01-0029 | Collection update replaces instead of appends | A04, A05 | permanent | explicit add, remove and set operations |
| W01-0030 | Collection replace drops entries the server added | A04, A02 | permanent | protected entries outside the client writable set |
| W01-0031 | Null clears a field the validator considers present | A05, A04 | permanent | validate type and nullability, not presence |
| W01-0032 | Enum coercion accepts a value outside the declared set | A05, A03 | permanent | strict enum parsing, reject unknown |
| W01-0033 | Create accepts an already approved state | A10, A04 | permanent | initial state forced server side |
| W01-0034 | Dangling foreign key accepted and later dereferenced | A04, A05 | until cleanup | enforce referential integrity at the store |
| W01-0035 | Bulk delete by filter removes rows outside the visible set | A06, A10 | destructive | delete by ids, filters are read only |
| W01-0036 | Nested relation write bypasses the child endpoint checks | A05, A02 | permanent | one validator per resource, nested writes reuse it |
| W01-0037 | Create accepts a client supplied owner | A02, A05 | permanent | ownership derived from the session, never the body |
| W01-0038 | Predictable identifier reuse after deletion | A03, A04 | permanent confusion | random or non-reusing ids, tombstones |
| W01-0039 | Duplicate field names in form encoding split validation from storage | A05, A06 | permanent | reject duplicates, one binder |
| W01-0040 | Unique key collision lets an update land on another record | A04, A02 | permanent | scope the match, enforce uniqueness per tenant |
| W01-0041 | Client sets the version field to skip conflict detection | A05, A04 | overwrites another writer | version compared and incremented server side only |
| W01-0042 | Restore payload repoints the object at another tenant | A06, A02 | permanent | restore re-derives ownership from the target scope |
| W01-0043 | Write to a popular object triggers a notification storm | A07, A10 | rate limited or not | coalesce notifications, per object cooldown |
| W01-0044 | Retry without idempotency duplicates the effect | A12, A10 | duplicates persist | idempotency keys with a bounded store |
| W01-0045 | Idempotency key collides across principals | A03, A04 | permanent | scope the key to the principal and route |
| W01-0046 | Batch reports success while individual items failed | A08, A04 | until noticed | per item results, no aggregate only |
| W01-0047 | Recursive delete walks into objects shared with others | A06, A02 | destructive | cascade follows ownership only, detach references |
| W01-0048 | Polymorphic type field changed to reinterpret the same record | A05, A03 | permanent | type immutable, one schema per record |
| W01-0049 | Object id from one collection resolves in another | A06, A03 | permanent | globally unique ids or composite keys in the route |
| W01-0050 | Write succeeds against a replica that will be discarded | A04, A12 | until failover, then lost | writes to primary, read-your-writes routing |

## W01-0001: Parallel creates bypass a uniqueness check that is not atomic

**Atoms:** `A04` state confusion, `A12` timing and ordering  
**State changed:** the uniqueness invariant of a collection  
**Acting as:** you  
**Persistence:** permanent duplicate records  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- uniqueness is checked in application code before insert
- no unique constraint in the store
- requests can be parallelised

Procedure:
1. send N identical creates in parallel
2. count the created records
3. attempt to use both records where one is expected

**Oracle:** `more than one record with the same logical key`, `two accounts or entries resolve from one identity`  
**Negative control:** sequential creates produce exactly one record, isolating the race

| mutation axis | variant | why it matters |
|---|---|---|
| timing | `staggered_ms` | window size varies by framework |

**Detected by:** duplicate logical keys

**Counter:** unique constraint in the store, not in code  
**Counter precondition:** constraint is the authority  
**Counter cost:** low

---

## W01-0002: Lost update overwrites a concurrent change silently

**Atoms:** `A04` state confusion, `A12` timing and ordering  
**State changed:** the current value of a record  
**Acting as:** whoever wrote last  
**Persistence:** the earlier change is gone  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- update sends the whole object
- no version or ETag check
- no merge on the server

Procedure:
1. read the object as two sessions
2. have session A change field one, session B change field two, both from the same base
3. submit B after A
4. re-read

**Oracle:** `field one reverts to the base value`, `no conflict is reported to either session`  
**Negative control:** an update with a stale version token is rejected, proving versioning exists elsewhere

| mutation axis | variant | why it matters |
|---|---|---|
| timing | `parallel_submit` | same base read |

**Detected by:** write with a stale version

**Counter:** optimistic concurrency via version or ETag, or field level patch  
**Counter precondition:** base version required on write  
**Counter cost:** low

---

## W01-0003: Partial update resets omitted fields to defaults

**Atoms:** `A05` type and shape confusion, `A04` state confusion  
**State changed:** fields the client did not send  
**Acting as:** you  
**Persistence:** permanent data loss  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- update binds a partial body to a full model
- missing fields take defaults
- no field mask

Procedure:
1. read an object with several fields set
2. send an update containing only one field
3. re-read the object

**Oracle:** `untouched fields became null, empty or default`, `data set by another user disappears`  
**Negative control:** a full representation update preserves the fields, proving the partial path is the cause

| mutation axis | variant | why it matters |
|---|---|---|
| type | `empty_object` | clears everything |

**Detected by:** write nulling populated fields

**Counter:** patch semantics with explicit presence handling  
**Counter precondition:** absent means absent  
**Counter cost:** low

---

## W01-0004: Client supplied identifier chosen on create

**Atoms:** `A03` identity confusion, `A05` type and shape confusion  
**State changed:** the primary key namespace  
**Acting as:** you  
**Persistence:** permanent  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- create accepts an id
- no server generation
- no collision rejection that reveals existence

Procedure:
1. create with an id you choose
2. attempt to create with an id that likely exists
3. observe error differences

**Oracle:** `your id is honoured`, `or an existence oracle distinguishes taken ids`  
**Negative control:** a server generated create ignores any id you send

| mutation axis | variant | why it matters |
|---|---|---|
| type | `uuid_v1_vs_v4` | time ordered ids leak creation time |

**Detected by:** client supplied primary key

**Counter:** server generates ids, ignore client values  
**Counter precondition:** ids are not client data  
**Counter cost:** low

---

## W01-0005: Client supplied timestamps forge the audit trail

**Atoms:** `A05` type and shape confusion, `A11` dependency compromise  
**State changed:** created and updated times used for ordering and evidence  
**Acting as:** you  
**Persistence:** permanent in records and logs  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- timestamps accepted from the payload
- or mass assignment lets them through
- ordering logic trusts them

Procedure:
1. create or update with a chosen timestamp
2. observe ordering and any retention or expiry logic
3. check the audit view

**Oracle:** `the record shows your timestamp, not now`, `ordering or retention changed accordingly`  
**Negative control:** a server generated record shows the real time

| mutation axis | variant | why it matters |
|---|---|---|
| timing | `future_date` | defeats retention windows |

**Detected by:** client supplied timestamp

**Counter:** server clock only, ignore client time  
**Counter precondition:** time is server state  
**Counter cost:** low

---

## W01-0006: State set directly instead of through the transition endpoint

**Atoms:** `A10` logic assumption violation, `A04` state confusion  
**State changed:** the workflow state of an object  
**Acting as:** you  
**Persistence:** permanent, skips approvals  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- state is a writable field
- a transition endpoint exists with checks
- the update endpoint also writes state

Procedure:
1. create or update with the target state in the payload
2. compare with the transition endpoint
3. observe which checks ran

**Oracle:** `the object reaches the state without a transition record`, `approval artefacts absent`  
**Negative control:** the transition endpoint on the same object requires the missing approval

| mutation axis | variant | why it matters |
|---|---|---|
| context | `state_in_nested_object` | binding may reach it |

**Detected by:** state change without a transition event

**Counter:** state not bindable, transitions only  
**Counter precondition:** one writer for state  
**Counter cost:** low

---

## W01-0007: Immutable identity fields are mutable on update

**Atoms:** `A05` type and shape confusion, `A06` path and namespace confusion  
**State changed:** what the object is and who it belongs to  
**Acting as:** you  
**Persistence:** permanent  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- update binds the whole model
- fields like owner, tenant, type are in the model
- no immutability check after create

Procedure:
1. update your own object changing owner, tenant or type
2. re-read and exercise the new identity

**Oracle:** `the field changed`, `the object now resolves under the other owner or tenant`  
**Negative control:** the create endpoint requires those fields and the update of a benign field leaves them intact

| mutation axis | variant | why it matters |
|---|---|---|
| context | `nested_owner_object` | binding recursion |

**Detected by:** update changing an identity field

**Counter:** immutable after create, enforced in the writer  
**Counter precondition:** identity fields are not bindable  
**Counter cost:** low

---

## W01-0008: Foreign key swapped on update reparents the object

**Atoms:** `A06` path and namespace confusion, `A02` trust boundary crossing  
**State changed:** the parent relationship  
**Acting as:** you  
**Persistence:** permanent  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- parent id is writable
- no check that the new parent is visible to you
- children inherit parent permissions

Procedure:
1. move your object under a parent you can see but do not own
2. or under a parent you cannot see, using a guessed id
3. observe permissions and listing

**Oracle:** `the object appears under the other parent`, `or inherits its sharing`  
**Negative control:** moving under a nonexistent parent fails

| mutation axis | variant | why it matters |
|---|---|---|
| type | `null_parent` | orphans may be globally visible |

**Detected by:** reparenting operation

**Counter:** parent change is an authorised operation with both sides checked  
**Counter precondition:** no direct bind of parent id  
**Counter cost:** low

---

## W01-0009: Delete leaves children reachable by their own route

**Atoms:** `A04` state confusion, `A08` information exposure  
**State changed:** the reachability of dependent records  
**Acting as:** the deleter  
**Persistence:** permanent  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- delete removes the parent only
- children keep their ids
- child routes do not check parent existence

Procedure:
1. create a parent with a child, note the child id
2. delete the parent
3. request the child directly

**Oracle:** `the child is still returned`, `its data is intact`  
**Negative control:** a child of a never existing parent returns 404

| mutation axis | variant | why it matters |
|---|---|---|
| protocol | `list_by_parent_id` | orphan listing |

**Detected by:** read of an orphaned child

**Counter:** cascade or tombstone plus parent check on child reads  
**Counter precondition:** referential integrity enforced  
**Counter cost:** low

---

## W01-0010: Soft delete filtered on read but not on write

**Atoms:** `A04` state confusion  
**State changed:** whether a deleted object can still be modified  
**Acting as:** you  
**Persistence:** until purge  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- delete sets a flag
- reads filter the flag
- writes do not

Procedure:
1. delete your object
2. send an update to its id
3. re-read through an admin or restore view

**Oracle:** `the update succeeded`, `the object returns with new values`  
**Negative control:** an update to a hard deleted id fails

| mutation axis | variant | why it matters |
|---|---|---|
| timing | `update_during_purge` | window |

**Detected by:** write to a soft deleted row

**Counter:** deleted predicate in the writer and the reader  
**Counter precondition:** one access layer  
**Counter cost:** low

---

## W01-0011: Restore returns an object into a changed world

**Atoms:** `A04` state confusion, `A06` path and namespace confusion  
**State changed:** the relationships a restored object points at  
**Acting as:** you  
**Persistence:** permanent  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- restore reinserts the record with old references
- referenced objects may be deleted or reassigned
- no revalidation on restore

Procedure:
1. create an object referencing another, delete the referent, restore the first
2. or restore after the referent changed owner
3. observe resolution

**Oracle:** `the restored object resolves to a different object than before`, `or exposes data through the stale reference`  
**Negative control:** restoring an object whose referent is unchanged behaves identically

| mutation axis | variant | why it matters |
|---|---|---|
| timing | `restore_after_purge` | id reuse |

**Detected by:** restore with dangling references

**Counter:** revalidate references on restore  
**Counter precondition:** restore is a write, not a copy  
**Counter cost:** low

---

## W01-0012: Draft autosave overwrites published content

**Atoms:** `A04` state confusion, `A10` logic assumption violation  
**State changed:** the live version of a document  
**Acting as:** the author  
**Persistence:** public  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- autosave writes to the same record as publish
- no separate draft table
- save endpoint does not check state

Procedure:
1. publish content
2. continue editing so autosave fires
3. observe the public view

**Oracle:** `public content changes without a publish action`  
**Negative control:** a save on a never published document keeps it private

| mutation axis | variant | why it matters |
|---|---|---|
| timing | `save_race_with_publish` | ordering |

**Detected by:** public content changed by a save event

**Counter:** separate draft from published, publish copies  
**Counter precondition:** one public writer  
**Counter cost:** design

---

## W01-0013: Merge operation accepts a source you do not own

**Atoms:** `A02` trust boundary crossing, `A04` state confusion  
**State changed:** the surviving record and its contents  
**Acting as:** the source owner  
**Persistence:** permanent and destructive  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- merge takes a source and a target id
- only one side is authorised
- merged content is copied

Procedure:
1. attempt a merge with your record as source and a target you choose
2. inspect what was copied and what was destroyed

**Oracle:** `content from the other record appears in yours`, `or their record is deleted`  
**Negative control:** merging two records you own works as documented

| mutation axis | variant | why it matters |
|---|---|---|
| type | `reversed_arguments` | source and target swapped |

**Detected by:** merge across ownership

**Counter:** authorise both operands  
**Counter precondition:** destructive ops need both sides  
**Counter cost:** low

---

## W01-0014: Clone copies fields the original kept private

**Atoms:** `A08` information exposure, `A05` type and shape confusion  
**State changed:** what the clone reveals  
**Acting as:** you  
**Persistence:** permanent  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- clone copies the whole record
- some fields are hidden from the API
- the clone is owned by you

Procedure:
1. clone a shared object you can read
2. inspect the clone for fields absent from the original read

**Oracle:** `internal fields, tokens or notes appear in the clone`  
**Negative control:** cloning your own object yields no fields you could not already read

| mutation axis | variant | why it matters |
|---|---|---|
| context | `clone_then_export` | export path differs |

**Detected by:** clone containing non exposed fields

**Counter:** clone from an allowlist projection  
**Counter precondition:** clone is a projection  
**Counter cost:** low

---

## W01-0015: Bulk update selects rows by filter rather than explicit ids

**Atoms:** `A06` path and namespace confusion, `A10` logic assumption violation  
**State changed:** every row matching a filter  
**Acting as:** you  
**Persistence:** mass modification  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- a bulk endpoint takes a filter
- the filter is passed to the datastore
- scope is applied only to the visible list

Procedure:
1. craft a filter that matches more than your visible set
2. run the bulk update
3. check a row you should not have touched

**Oracle:** `a record outside your scope changed`  
**Negative control:** the same filter with an explicit id list changes only those

| mutation axis | variant | why it matters |
|---|---|---|
| type | `operator_injection` | filter parser |

**Detected by:** bulk write affecting rows outside scope

**Counter:** bulk writes take ids, filters are read only  
**Counter precondition:** write scope resolved before the query  
**Counter cost:** low

---

## W01-0016: Sort and filter parameters reach the query builder

**Atoms:** `A01` interpreter confusion, `A05` type and shape confusion  
**State changed:** which rows and which order  
**Acting as:** you  
**Persistence:** read mostly, write if the same builder is reused  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- sort or filter names are passed through to the query
- no allowlist
- error verbosity available

Procedure:
1. supply a sort field that is not a column
2. observe errors or ordering changes
3. attempt boolean based ordering to infer data

**Oracle:** `error names a column or the ordering changes in a way data explains`  
**Negative control:** an allowlisted sort field behaves normally

| mutation axis | variant | why it matters |
|---|---|---|
| encoding | `nested_field_path` | ORM relation traversal |

**Detected by:** non allowlisted sort field

**Counter:** allowlist sortable and filterable fields  
**Counter precondition:** never pass names through  
**Counter cost:** low

---

## W01-0017: Create with a reference to a private object is an existence oracle

**Atoms:** `A08` information exposure, `A05` type and shape confusion  
**State changed:** knowledge of which identifiers exist  
**Acting as:** you  
**Persistence:** none, it is inference  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- create validates the referenced id exists
- the error differs from a generic rejection
- no rate limit

Procedure:
1. create references to a range of ids
2. record which are accepted versus rejected differently
3. map existence

**Oracle:** `a distinguishable error or timing for existing ids`  
**Negative control:** random ids produce a uniform rejection rate

| mutation axis | variant | why it matters |
|---|---|---|
| timing | `timing_only` | error text suppressed |

**Detected by:** enumeration of references

**Counter:** uniform errors, rate limit, scope check before existence  
**Counter precondition:** existence is not disclosed  
**Counter cost:** low

---

## W01-0018: Duplicate ids inside one payload produce a partial write

**Atoms:** `A05` type and shape confusion, `A04` state confusion  
**State changed:** which element wins and what the response claims  
**Acting as:** you  
**Persistence:** unpredictable  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- bulk endpoint accepts an array
- duplicate ids allowed
- no transaction around the batch

Procedure:
1. send the same id twice with different values
2. observe the stored value and the per item response
3. interrupt mid batch

**Oracle:** `stored value differs from the reported result`, `or a partial write with a success response`  
**Negative control:** distinct ids produce consistent results and reports

| mutation axis | variant | why it matters |
|---|---|---|
| volume | `many_duplicates` | truncated reporting |

**Detected by:** duplicate ids in a batch

**Counter:** reject duplicates, transactional batch, honest reporting  
**Counter precondition:** batch is atomic or reports per item  
**Counter cost:** low

---

## W01-0019: Delete via a safe method or a prefetchable link

**Atoms:** `A06` path and namespace confusion, `A04` state confusion  
**State changed:** existence of the object  
**Acting as:** you or a victim's client  
**Persistence:** permanent  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- a delete route answers GET
- or a link with a token is prefetched by a client or crawler
- no confirmation step

Procedure:
1. request the delete route with GET
2. or place the link in a page a client will prefetch
3. observe deletion

**Oracle:** `the object is gone without an explicit POST`  
**Negative control:** the same route with the wrong token does not delete

| mutation axis | variant | why it matters |
|---|---|---|
| protocol | `method_override` | _method parameter |

**Detected by:** state change on a safe method

**Counter:** safe methods never mutate, confirmation for destructive ops  
**Counter precondition:** framework enforced  
**Counter cost:** low

---

## W01-0020: Update resurrects an object mid delete

**Atoms:** `A04` state confusion, `A12` timing and ordering  
**State changed:** whether the object exists  
**Acting as:** you  
**Persistence:** until next purge  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- delete is soft or two phase
- an update on the same id does not check the deleted flag
- ordering is not serialised

Procedure:
1. issue delete and update concurrently
2. read the object through every view
3. check the deleted flag against content

**Oracle:** `object readable after delete with the update applied`, `or deleted flag true while content changed`  
**Negative control:** sequential delete then update is rejected

| mutation axis | variant | why it matters |
|---|---|---|
| timing | `many_parallel` | widen window |

**Detected by:** update after delete event in the same second

**Counter:** state transition guarded by a conditional write  
**Counter precondition:** delete is a state, not a row removal  
**Counter cost:** low

---

## W01-0021: Export and reimport roundtrip changes security attributes

**Atoms:** `A04` state confusion, `A05` type and shape confusion  
**State changed:** ownership, role and visibility fields  
**Acting as:** you  
**Persistence:** permanent after import  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- export omits a field
- import applies a default
- or import matches by name not id

Procedure:
1. export your object
2. reimport it unchanged
3. compare every field, especially security ones

**Oracle:** `a field changed value across the roundtrip`, `visibility or owner differs`  
**Negative control:** a field by field diff of a read only object shows no change

| mutation axis | variant | why it matters |
|---|---|---|
| context | `reordered_fields` | positional parsers |

**Detected by:** roundtrip diff on security fields

**Counter:** roundtrip test in CI, explicit defaults  
**Counter precondition:** export is complete  
**Counter cost:** low

---

## W01-0022: Trash and recycle bin reachable without the parent check

**Atoms:** `A02` trust boundary crossing, `A08` information exposure  
**State changed:** deleted content and its metadata  
**Acting as:** the deleter or anyone  
**Persistence:** until purge  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- trash has its own listing route
- it does not apply the same scope as the main listing
- items retain metadata

Procedure:
1. delete an object as one account
2. list trash as another account or unauthenticated
3. inspect what is returned

**Oracle:** `deleted items of other users appear`  
**Negative control:** the main listing never shows other users items

| mutation axis | variant | why it matters |
|---|---|---|
| protocol | `export_trash` | bulk path |

**Detected by:** trash listing without scope

**Counter:** trash is a scoped view like any other  
**Counter precondition:** same authorisation everywhere  
**Counter cost:** low

---

## W01-0023: Undo restores a state that was superseded

**Atoms:** `A04` state confusion, `A10` logic assumption violation  
**State changed:** the object after an undo  
**Acting as:** you  
**Persistence:** permanent  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- undo replays a previous snapshot
- no check that a later change happened
- undo is available long after

Procedure:
1. change an object, change it again, then undo the first change
2. observe which state results

**Oracle:** `the second change is lost`, `or the undo applies to the wrong version`  
**Negative control:** undo immediately after one change restores correctly

| mutation axis | variant | why it matters |
|---|---|---|
| timing | `undo_twice` | stack desync |

**Detected by:** undo applied out of order

**Counter:** undo targets a version and rejects if superseded  
**Counter precondition:** versions are identified  
**Counter cost:** low

---

## W01-0024: Delete removes the record but not the stored blobs

**Atoms:** `A06` path and namespace confusion, `A08` information exposure  
**State changed:** files still retrievable by direct path  
**Acting as:** anyone with the path  
**Persistence:** forever  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- metadata deleted, object storage untouched
- blob paths are predictable or already known
- no expiry

Procedure:
1. upload a file, note the direct storage url
2. delete the record
3. request the url directly

**Oracle:** `the file still downloads`  
**Negative control:** a url never issued returns an error

| mutation axis | variant | why it matters |
|---|---|---|
| encoding | `signed_url_still_valid` | signature outlives deletion |

**Detected by:** object storage request for a deleted record

**Counter:** delete orchestrates storage, short lived signed urls  
**Counter precondition:** one deletion pipeline  
**Counter cost:** low

---

## W01-0025: Counters drift because increments have no matching decrement

**Atoms:** `A04` state confusion, `A10` logic assumption violation  
**State changed:** aggregate counts and quotas  
**Acting as:** you  
**Persistence:** permanent drift  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- counts are maintained incrementally
- delete or failure paths miss the decrement
- or increments are client supplied

Procedure:
1. create and delete repeatedly
2. or fail a create after the increment
3. compare the counter with the real count

**Oracle:** `counter diverges`, `a quota or limit is bypassable by driving the counter down`  
**Negative control:** a recompute endpoint returns the true count

| mutation axis | variant | why it matters |
|---|---|---|
| timing | `parallel_increment` | lost update on the counter |

**Detected by:** counter diverging from row count

**Counter:** derive counters, or make them transactional  
**Counter precondition:** one writer per counter  
**Counter cost:** low

---

## W01-0026: Update leaves the version unchanged so caches keep serving old data

**Atoms:** `A04` state confusion, `A06` path and namespace confusion  
**State changed:** what every reader sees after the write  
**Acting as:** the writer  
**Persistence:** until TTL  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- responses are cached by version, ETag or last modified
- the update does not bump it
- no explicit purge

Procedure:
1. read an object to populate the cache
2. update it
3. request again with the conditional headers and without

**Oracle:** `the old representation is served`, `a conditional request returns not modified`  
**Negative control:** a forced revalidation returns the new value

| mutation axis | variant | why it matters |
|---|---|---|
| protocol | `different_accept_encoding` | separate cache entries |

**Detected by:** version unchanged after a write

**Counter:** bump the validator on every write  
**Counter precondition:** one write path  
**Counter cost:** low

---

## W01-0027: Write does not invalidate derived stores

**Atoms:** `A04` state confusion, `A08` information exposure  
**State changed:** search index, feeds, aggregates and caches  
**Acting as:** readers  
**Persistence:** until rebuild  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- derived stores are updated asynchronously
- the async path can be skipped or fail silently
- no reconciliation

Procedure:
1. update a field that appears in search or a feed
2. query the derived store
3. then query the primary store

**Oracle:** `the derived store shows the old value`, `or shows content that was removed`  
**Negative control:** a forced reindex reflects the change

| mutation axis | variant | why it matters |
|---|---|---|
| timing | `update_during_rebuild` | ordering |

**Detected by:** derived store divergence

**Counter:** outbox pattern with reconciliation  
**Counter precondition:** every write emits an event  
**Counter cost:** infra

---

## W01-0028: Client assigns the sequence or ticket number

**Atoms:** `A10` logic assumption violation, `A05` type and shape confusion  
**State changed:** ordering and identity of documents  
**Acting as:** you  
**Persistence:** permanent  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- the number is a client field
- uniqueness not enforced
- downstream treats the number as authoritative

Procedure:
1. create two records with chosen numbers, out of order and duplicated
2. observe ordering, gaps and any downstream reconciliation

**Oracle:** `numbering conflicts or gaps appear`, `a record sorts ahead of older ones`  
**Negative control:** a server assigned sequence is monotonic and unique

| mutation axis | variant | why it matters |
|---|---|---|
| type | `leading_zeros` | string vs int comparison |

**Detected by:** client supplied sequence number

**Counter:** server assigns, enforced unique  
**Counter precondition:** numbering is server state  
**Counter cost:** low

---

## W01-0029: Collection update replaces instead of appends

**Atoms:** `A04` state confusion, `A05` type and shape confusion  
**State changed:** list valued fields such as tags, roles or members  
**Acting as:** you  
**Persistence:** permanent  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- update semantics for arrays are replace
- the client sends a partial list
- no merge strategy

Procedure:
1. update a list field with one item
2. observe whether the rest survive
3. try sending an empty list

**Oracle:** `items vanish`, `an empty list clears the field`  
**Negative control:** an append endpoint leaves existing items intact

| mutation axis | variant | why it matters |
|---|---|---|
| type | `empty_array_vs_absent` | clear vs no-op |

**Detected by:** list shrink on a partial write

**Counter:** explicit add, remove and set operations  
**Counter precondition:** semantics documented per field  
**Counter cost:** low

---

## W01-0030: Collection replace drops entries the server added

**Atoms:** `A04` state confusion, `A02` trust boundary crossing  
**State changed:** server managed memberships inside a client editable list  
**Acting as:** you  
**Persistence:** permanent  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- the server adds entries with elevated meaning
- the client can write the whole list
- no protected entries

Procedure:
1. read a list containing a server added entry
2. write back the list without it
3. check whether it returns

**Oracle:** `the protected entry is gone`, `or can be re-added with different attributes`  
**Negative control:** a server added entry marked immutable cannot be removed by the same write

| mutation axis | variant | why it matters |
|---|---|---|
| type | `reorder` | order based logic |

**Detected by:** removal of a server managed entry

**Counter:** protected entries outside the client writable set  
**Counter precondition:** ownership per entry  
**Counter cost:** low

---

## W01-0031: Null clears a field the validator considers present

**Atoms:** `A05` type and shape confusion, `A04` state confusion  
**State changed:** required fields  
**Acting as:** you  
**Persistence:** permanent  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- required means not absent, not not-null
- null passes
- downstream assumes a value

Procedure:
1. send null for a required field
2. observe acceptance
3. find a code path that dereferences it

**Oracle:** `the field is null in storage`, `or the path errors revealing the assumption`  
**Negative control:** an absent field is rejected, proving presence is checked and null is not

| mutation axis | variant | why it matters |
|---|---|---|
| type | `empty_string` | two falsy variants |

**Detected by:** null in a required field

**Counter:** validate type and nullability, not presence  
**Counter precondition:** one validator  
**Counter cost:** low

---

## W01-0032: Enum coercion accepts a value outside the declared set

**Atoms:** `A05` type and shape confusion, `A03` identity confusion  
**State changed:** a role, state or type field  
**Acting as:** you  
**Persistence:** permanent  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- enum parsed leniently
- unknown values fall back or pass through
- downstream compares by string

Procedure:
1. send an unlisted enum value
2. then a case variant, then a numeric index
3. observe storage and behaviour

**Oracle:** `the value persists as sent`, `or a fallback grants unexpected behaviour`  
**Negative control:** a clearly invalid enum type is rejected

| mutation axis | variant | why it matters |
|---|---|---|
| encoding | `numeric_index` | ordinal mapping |

**Detected by:** enum value outside the declared set

**Counter:** strict enum parsing, reject unknown  
**Counter precondition:** closed set  
**Counter cost:** low

---

## W01-0033: Create accepts an already approved state

**Atoms:** `A10` logic assumption violation, `A04` state confusion  
**State changed:** the workflow position at birth  
**Acting as:** you  
**Persistence:** permanent  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- state is in the create payload
- create does not force an initial state
- downstream trusts state

Procedure:
1. create with the final state
2. compare with the documented initial state
3. observe which checks ran

**Oracle:** `the object exists in a privileged state`, `no transition record`  
**Negative control:** omitting state yields the documented initial state

| mutation axis | variant | why it matters |
|---|---|---|
| context | `state_in_nested` | binding |

**Detected by:** create in a non initial state

**Counter:** initial state forced server side  
**Counter precondition:** state not bindable on create  
**Counter cost:** low

---

## W01-0034: Dangling foreign key accepted and later dereferenced

**Atoms:** `A04` state confusion, `A05` type and shape confusion  
**State changed:** referential integrity  
**Acting as:** you  
**Persistence:** until cleanup  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- foreign keys not enforced in the store
- references accepted without existence check
- readers assume they resolve

Procedure:
1. create a reference to an id that never existed
2. or delete the referent after creation
3. observe listing and detail views

**Oracle:** `the record exists with an unresolvable reference`, `a detail view errors or leaks a stack trace`  
**Negative control:** a valid reference resolves

| mutation axis | variant | why it matters |
|---|---|---|
| timing | `delete_referent_after` | ordering |

**Detected by:** unresolvable reference

**Counter:** enforce referential integrity at the store  
**Counter precondition:** constraints exist  
**Counter cost:** low

---

## W01-0035: Bulk delete by filter removes rows outside the visible set

**Atoms:** `A06` path and namespace confusion, `A10` logic assumption violation  
**State changed:** existence of many records  
**Acting as:** you  
**Persistence:** destructive  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- a delete endpoint accepts a filter
- scope applied to display not to the delete query
- no confirmation count

Procedure:
1. craft a filter matching more than you can see
2. run it
3. check a record you should not have been able to remove

**Oracle:** `a record outside your scope is gone`  
**Negative control:** the same filter with explicit ids deletes only those

| mutation axis | variant | why it matters |
|---|---|---|
| type | `operator_in_filter` | parser |

**Detected by:** bulk delete affecting out of scope rows

**Counter:** delete by ids, filters are read only  
**Counter precondition:** scope resolved before query  
**Counter cost:** low

---

## W01-0036: Nested relation write bypasses the child endpoint checks

**Atoms:** `A05` type and shape confusion, `A02` trust boundary crossing  
**State changed:** child records created through a parent payload  
**Acting as:** you  
**Persistence:** permanent  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- the parent write accepts nested children
- children are persisted without their own validation
- the child endpoint has stricter checks

Procedure:
1. create or update a parent including a child object in the payload
2. compare what the child endpoint would reject
3. observe which validations ran

**Oracle:** `the child is persisted with a value the child endpoint rejects`  
**Negative control:** the same child through its own endpoint is rejected

| mutation axis | variant | why it matters |
|---|---|---|
| context | `nested_array` | bulk nesting |

**Detected by:** child written via parent with non conforming fields

**Counter:** one validator per resource, nested writes reuse it  
**Counter precondition:** no second path  
**Counter cost:** low

---

## W01-0037: Create accepts a client supplied owner

**Atoms:** `A02` trust boundary crossing, `A05` type and shape confusion  
**State changed:** who the record belongs to  
**Acting as:** you  
**Persistence:** permanent  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- owner is a bindable field
- create does not overwrite it with the session identity
- reads authorise by that field

Procedure:
1. create with another account's identifier as owner
2. read as that account
3. or read as yourself

**Oracle:** `the record appears in the other account`, `or you retain access to a record owned by them`  
**Negative control:** omitting owner yields your own identity

| mutation axis | variant | why it matters |
|---|---|---|
| type | `owner_as_object` | nesting |

**Detected by:** created record owner differs from session

**Counter:** ownership derived from the session, never the body  
**Counter precondition:** owner not bindable  
**Counter cost:** low

---

## W01-0038: Predictable identifier reuse after deletion

**Atoms:** `A03` identity confusion, `A04` state confusion  
**State changed:** which record an old identifier now points at  
**Acting as:** anyone holding the old id  
**Persistence:** permanent confusion  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- ids come from a sequence
- deleted ids are reused or never burned
- old links and logs persist

Procedure:
1. create and delete records until the sequence wraps or reuses
2. hold an old identifier
3. create a new record and observe whether it takes the old id

**Oracle:** `an old link now resolves to a different owner's record`  
**Negative control:** random ids never collide

| mutation axis | variant | why it matters |
|---|---|---|
| timing | `wrap_sequence` | bounded id space |

**Detected by:** id reuse after delete

**Counter:** random or non-reusing ids, tombstones  
**Counter precondition:** ids are never recycled  
**Counter cost:** low

---

## W01-0039: Duplicate field names in form encoding split validation from storage

**Atoms:** `A05` type and shape confusion, `A06` path and namespace confusion  
**State changed:** which of the two values is authoritative  
**Acting as:** you  
**Persistence:** permanent  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- form or multipart parsing binds the last or first value
- the validator and the writer disagree
- no duplicate rejection

Procedure:
1. submit the same field twice with different values
2. try both orders
3. re-read the record

**Oracle:** `stored value is the one the validator did not check`  
**Negative control:** a single value roundtrips correctly

| mutation axis | variant | why it matters |
|---|---|---|
| encoding | `field_and_field_brackets` | different binders |

**Detected by:** duplicate field names on a security relevant field

**Counter:** reject duplicates, one binder  
**Counter precondition:** single parser  
**Counter cost:** low

---

## W01-0040: Unique key collision lets an update land on another record

**Atoms:** `A04` state confusion, `A02` trust boundary crossing  
**State changed:** which record the write modifies  
**Acting as:** the other record's owner  
**Persistence:** permanent  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- updates match by a natural key such as email or slug
- no scope on the match
- the app upserts

Procedure:
1. create a record whose natural key matches another account's record
2. observe whether it updates theirs or creates a conflicting one

**Oracle:** `their record changes`, `or an error reveals their record's existence`  
**Negative control:** a fresh natural key creates a new record

| mutation axis | variant | why it matters |
|---|---|---|
| encoding | `case_or_whitespace` | normalisation |

**Detected by:** upsert matching outside scope

**Counter:** scope the match, enforce uniqueness per tenant  
**Counter precondition:** natural keys are scoped  
**Counter cost:** low

---

## W01-0041: Client sets the version field to skip conflict detection

**Atoms:** `A05` type and shape confusion, `A04` state confusion  
**State changed:** whether a concurrent change is detected  
**Acting as:** you  
**Persistence:** overwrites another writer  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- version is a request field
- server compares it to the stored value
- client can supply any number

Procedure:
1. read the object and note the version
2. update after another session changed it, sending a higher version
3. observe acceptance and the lost change

**Oracle:** `the conflict is not reported`, `the other change is gone`  
**Negative control:** a stale version is rejected, proving comparison exists

| mutation axis | variant | why it matters |
|---|---|---|
| type | `version_as_string` | coercion |

**Detected by:** version jump greater than one

**Counter:** version compared and incremented server side only  
**Counter precondition:** client cannot set it  
**Counter cost:** low

---

## W01-0042: Restore payload repoints the object at another tenant

**Atoms:** `A06` path and namespace confusion, `A02` trust boundary crossing  
**State changed:** tenant and parent after restore  
**Acting as:** you  
**Persistence:** permanent  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- restore accepts the serialised object
- tenant or parent ids are in it
- no scope check on restore

Procedure:
1. export an object
2. modify its tenant or parent id
3. restore
4. observe where it lands

**Oracle:** `the object is now visible in the other tenant`  
**Negative control:** an unmodified restore keeps it in place

| mutation axis | variant | why it matters |
|---|---|---|
| context | `nested_parent` | binding |

**Detected by:** restore with a foreign tenant id

**Counter:** restore re-derives ownership from the target scope  
**Counter precondition:** ids in the payload are hints not facts  
**Counter cost:** low

---

## W01-0043: Write to a popular object triggers a notification storm

**Atoms:** `A07` resource exhaustion, `A10` logic assumption violation  
**State changed:** notification and email queues  
**Acting as:** the platform  
**Persistence:** rate limited or not  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- each write fans out notifications
- no dedupe or cooldown
- queue capacity shared with production

Procedure:
1. write repeatedly to an object with many subscribers
2. measure fan out and delivery
3. observe queue latency for unrelated traffic

**Oracle:** `queue depth rises and unrelated latency follows`  
**Negative control:** the same number of writes to an object with no subscribers has no effect

| mutation axis | variant | why it matters |
|---|---|---|
| volume | `batch_write` | one request many fan outs |

**Detected by:** fan out per write above threshold

**Counter:** coalesce notifications, per object cooldown  
**Counter precondition:** fan out bounded  
**Counter cost:** low

---

## W01-0044: Retry without idempotency duplicates the effect

**Atoms:** `A12` timing and ordering, `A10` logic assumption violation  
**State changed:** how many times an action applied  
**Acting as:** you  
**Persistence:** duplicates persist  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- no idempotency key
- client or proxy retries on timeout
- the operation is not naturally idempotent

Procedure:
1. submit a create or payment, dropping the response and retrying
2. or send two identical requests in parallel
3. count the effects

**Oracle:** `two records or two charges`  
**Negative control:** a request with an idempotency key applied twice produces one effect

| mutation axis | variant | why it matters |
|---|---|---|
| timing | `parallel_identical` | race |

**Detected by:** identical operations within the retry window

**Counter:** idempotency keys with a bounded store  
**Counter precondition:** keys scoped per principal  
**Counter cost:** low

---

## W01-0045: Idempotency key collides across principals

**Atoms:** `A03` identity confusion, `A04` state confusion  
**State changed:** whose operation a replay applies to  
**Acting as:** another user  
**Persistence:** permanent  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- keys stored globally
- not scoped to the principal
- reuse returns the stored result

Procedure:
1. use a common key value such as a timestamp or uuid you saw in a response
2. observe whether you receive another principal's result or overwrite it

**Oracle:** `you get their response body`, `or your operation is suppressed by their key`  
**Negative control:** a key scoped per user behaves independently

| mutation axis | variant | why it matters |
|---|---|---|
| type | `key_in_header_vs_body` | different stores |

**Detected by:** key reused across principals

**Counter:** scope the key to the principal and route  
**Counter precondition:** keys are per user  
**Counter cost:** low

---

## W01-0046: Batch reports success while individual items failed

**Atoms:** `A08` information exposure, `A04` state confusion  
**State changed:** the operator's belief about what was written  
**Acting as:** the operator  
**Persistence:** until noticed  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- batch responds with an aggregate status
- per item errors are swallowed or truncated
- no report file

Procedure:
1. submit a batch with some items that must fail
2. read the aggregate response
3. verify each item independently

**Oracle:** `response says success, some items absent`, `or error list truncated below the real count`  
**Negative control:** a fully valid batch reports success and all items exist

| mutation axis | variant | why it matters |
|---|---|---|
| volume | `large_batch` | truncation |

**Detected by:** batch success with missing rows

**Counter:** per item results, no aggregate only  
**Counter precondition:** batch is honest  
**Counter cost:** low

---

## W01-0047: Recursive delete walks into objects shared with others

**Atoms:** `A06` path and namespace confusion, `A02` trust boundary crossing  
**State changed:** objects you own plus objects you merely reference  
**Acting as:** other owners  
**Persistence:** destructive  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- delete cascades through references
- not just ownership
- shared objects indistinguishable from owned

Procedure:
1. share an object into your space
2. delete your space or the object
3. check whether the original is affected

**Oracle:** `the other owner's object is deleted or detached`  
**Negative control:** deleting an unshared object affects only yours

| mutation axis | variant | why it matters |
|---|---|---|
| type | `transitive_cascade` | depth |

**Detected by:** cascade across ownership

**Counter:** cascade follows ownership only, detach references  
**Counter precondition:** delete is ownership scoped  
**Counter cost:** low

---

## W01-0048: Polymorphic type field changed to reinterpret the same record

**Atoms:** `A05` type and shape confusion, `A03` identity confusion  
**State changed:** which schema the record is read as  
**Acting as:** you  
**Persistence:** permanent  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- records have a type discriminator
- the type is writable
- readers trust the type to select a schema

Procedure:
1. create a record of a low privilege type
2. change its type to a privileged one
3. read it and observe which fields are interpreted

**Oracle:** `the record is read as the other type`, `privileged behaviour follows`  
**Negative control:** changing the type of a record you do not own is rejected

| mutation axis | variant | why it matters |
|---|---|---|
| context | `type_in_path` | route based dispatch |

**Detected by:** type change on an existing record

**Counter:** type immutable, one schema per record  
**Counter precondition:** type not bindable  
**Counter cost:** low

---

## W01-0049: Object id from one collection resolves in another

**Atoms:** `A06` path and namespace confusion, `A03` identity confusion  
**State changed:** which resource an identifier addresses  
**Acting as:** you  
**Persistence:** permanent  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- ids are unique per collection but not globally
- routes do not check the collection
- or a generic lookup accepts any id

Procedure:
1. take an id from a collection you can write
2. address it under a different collection's route
3. observe which record resolves

**Oracle:** `a record from the other collection is read or modified`  
**Negative control:** an id that exists in neither collection returns 404

| mutation axis | variant | why it matters |
|---|---|---|
| encoding | `prefixed_vs_bare` | parsers strip prefixes |

**Detected by:** id resolved under the wrong collection

**Counter:** globally unique ids or composite keys in the route  
**Counter precondition:** id names its collection  
**Counter cost:** low

---

## W01-0050: Write succeeds against a replica that will be discarded

**Atoms:** `A04` state confusion, `A12` timing and ordering  
**State changed:** which database is authoritative for the next read  
**Acting as:** you  
**Persistence:** until failover, then lost  
**Status:** PROBABLE  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- writes can land on a replica or an edge store
- reads use a different node
- no write forwarding

Procedure:
1. write through a path that may hit a region or replica
2. read immediately and later
3. compare

**Oracle:** `the write vanishes after consistency settles`, `or two sessions see different truth`  
**Negative control:** a write to the primary is immediately visible everywhere

| mutation axis | variant | why it matters |
|---|---|---|
| timing | `read_your_writes_window` | lag |

**Detected by:** write acknowledged but absent after settle

**Counter:** writes to primary, read-your-writes routing  
**Counter precondition:** one authoritative writer  
**Counter cost:** infra

---
