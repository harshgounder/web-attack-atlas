# Counters by control class

A defender picks the classes they own and sees how many atlas patterns that closes. A researcher reads
it the other way: this is what will stop you.

`100` patterns across `11` control classes.

| class | control | patterns closed |
|---|---|---|
| C02 | function level authorisation | 27 |
| C03 | binding allowlist | 27 |
| C01 | object level authorisation | 9 |
| C05 | state machine integrity | 9 |
| C04 | identity canonicalisation | 6 |
| C06 | credential and token policy | 5 |
| C09 | cache and key discipline | 5 |
| C07 | parser strictness | 4 |
| C11 | audit integrity | 4 |
| C10 | cost and resource control | 2 |
| C12 | protocol lifecycle | 2 |

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
- `W03-0001` Stored value rendered unescaped in a privileged console
  - counter: context aware escaping at render, plus CSP
- `W03-0002` Spreadsheet formula injection through an export
  - counter: prefix neutralisation on export, and formula disabled policy
- `W03-0011` Deferred SSRF through an HTML to image or document converter
  - counter: deny egress, pre-fetch assets yourself
- `W03-0013` Second order SQL injection through a stored value
  - counter: parameterise every query including batch jobs
- `W03-0014` Stored filename reaches a shell in a batch job
  - counter: never interpolate filenames into commands, use argv
- `W03-0021` Report generator builds a shell command from stored data
  - counter: library calls not shell, argv only
- `W03-0026` Search suggestion endpoint surfaces content the user cannot open
  - counter: apply the same authorisation filter to every index entry point
- `W03-0029` Verification token leaks through a referrer on a deferred redirect
  - counter: referrer policy no-referrer, single use short lived tokens, never in query
- `W03-0031` Invitation link is fetched by a preview bot and consumed
  - counter: never consume on GET, require a confirmation POST
- `W03-0034` Crawler or favicon fetch reaches an internal address
  - counter: resolve then block private ranges, egress proxy
- `W03-0045` Notification content is rendered in a privileged operator surface
  - counter: one escaping layer for all notification renderers

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
- `W03-0003` Stored content reaches a PDF or document renderer
  - counter: render in a sandbox with egress denied, strip active content
- `W03-0004` Stored value rendered in an outbound email template
  - counter: template escaping per context, header encoding
- `W03-0005` Markdown renderer sanitizer differential
  - counter: sanitize the rendered output, not the input
- `W03-0006` SVG upload rendered inline on a shared origin
  - counter: serve user uploads from a separate origin, force download, sanitize
- `W03-0007` Filename stored and rendered in a listing without escaping
  - counter: escape on render, generate display names, validate charset
- `W03-0008` Profile field rendered inside a third party embed or widget
  - counter: escape for the embed context, or render in a sandboxed iframe
- `W03-0009` Webhook fires later and fetches an attacker chosen URL
  - counter: destination allowlist, egress filtering, no redirect following
- `W03-0010` Thumbnail or preview generation fetches a stored URL
  - counter: fetch through a proxy with an allowlist and no private ranges
- `W03-0012` Link preview or unfurl fetches on someone else's behalf
  - counter: bot in a segmented network, allowlist, no redirects to private ranges
- `W03-0020` Internal header trusted by a worker after the edge stripped it
  - counter: strip inbound internal headers at the edge, mTLS between services
- `W03-0022` Report chart loads an image from a stored URL
  - counter: allowlist image hosts, no schemes
- `W03-0023` Scheduled import re-reads a URL the user supplied once
  - counter: revalidate host on every run, pin to allowlist
- `W03-0025` Search index ingestion renders stored markup in results
  - counter: escape before highlight, mark matches with safe spans
- `W03-0027` Feed or RSS generation emits stored content unescaped
  - counter: escape per XML context, strip active content
- `W03-0033` oEmbed or embed endpoint fetches attacker JSON and renders it
  - counter: provider allowlist, sanitize embed html, sandbox iframes
- `W03-0035` Import of a subscription list triggers fetches of attacker feeds
  - counter: allowlist, per user rate limit, segmented fetcher
- `W03-0036` Calendar invite injects fields the client trusts
  - counter: escape and strip CRLF in ICS fields
- `W03-0037` Calendar attachment causes the client to fetch an external resource
  - counter: strip external references, proxy images, plain text descriptions
- `W03-0038` Generated document leaks data through metadata or hidden layers
  - counter: build the export from an allowlist of fields, flatten and strip
- `W03-0039` Uploaded image metadata is retained and republished
  - counter: strip metadata on ingest, re-encode
- `W03-0043` Stored blob is deserialised by a later process
  - counter: signed or encrypted blobs, allowlisted types
- `W03-0046` Audit log viewer renders the log line as markup
  - counter: logs are data, viewer is a data renderer, escape everything
- `W03-0047` Ticket or comment body executes in the support console
  - counter: render as text, sanitize agent side

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
- `W03-0024` Backup restore writes attacker supplied records
  - counter: restore revalidates ownership, restore is a controlled operation

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
- `W03-0028` Webhook delivery can be replayed to repeat a state change
  - counter: idempotency key plus timestamp window plus signature over the exact bytes
- `W03-0048` Pending approval object carries fields the approver trusts
  - counter: immutable snapshot at approval, apply exactly that
- `W03-0049` Deleted object still served from cache or index
  - counter: deletion propagates to every derived store, tombstone on read

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
- `W03-0019` Queue message injected with a field the worker trusts
  - counter: sign messages, never trust body identity
- `W03-0042` Archive entry names are used later by a batch unzip
  - counter: canonicalise and contain per entry, no links

## C06: credential and token policy

atomic single use, subset scopes, verified identity

- `W02-0002` Tenant escape through a nested reference on create
  - counter: derive tenant from token, never from body, and validate every referenced parent
- `W02-0019` OAuth scope upgraded on refresh or re-consent
  - counter: refresh scope must be a subset of the original grant
- `W02-0030` Reset token reusable or raced across two requests
  - counter: atomic single use, invalidate siblings on issue
- `W03-0030` Unsubscribe or magic link token is long lived and reusable
  - counter: purpose bound, single use, short lived, revocable
- `W03-0050` Revoked or downgraded privilege persists in existing sessions
  - counter: short lived tokens, revocation list checked per request

## C09: cache and key discipline

every varying input in the key

- `W02-0027` Shared cache key collision overwrites another user's view
  - counter: include every varying input in the key, or do not cache personalised responses
- `W03-0017` Cache poisoning via a stored value reflected into a shared cache entry
  - counter: key every varying input, or do not cache
- `W03-0018` Cache deception stores a private page under a public path
  - counter: cache only by explicit rule, normalize before keying
- `W03-0032` Link preview caches attacker content under a trusted card
  - counter: key previews by content hash or revalidate
- `W03-0044` Stored user content becomes part of a shared template
  - counter: never cache user fragments in shared keys

## C07: parser strictness

one parser, reject duplicates and alternates

- `W02-0008` Alternate representation reaches the same write with weaker checks
  - counter: one parser per resource, reject alternates
- `W02-0015` Duplicate parameter decides which role is written
  - counter: reject duplicate parameters, parse once
- `W02-0038` Duplicate JSON keys split validation from persistence
  - counter: strict parser, reject duplicates
- `W03-0040` Download served with a sniffable type executes in the app origin
  - counter: separate asset origin, nosniff, attachment disposition

## C11: audit integrity

structured append only logging with attribution

- `W02-0020` Support impersonation used to perform the write
  - counter: read only impersonation by default, dual attribution in audit
- `W02-0026` Log injection used to write into the audit trail
  - counter: structured logging with escaping, append only store
- `W03-0015` Stored template fragment compiled later
  - counter: logic-less templates, never compile user input
- `W03-0016` Log poisoning used as the input for a later file read
  - counter: logs outside the web root, no dynamic include

## C10: cost and resource control

per operation cost and quotas by principal

- `W02-0035` GraphQL aliases multiply a mutation past its guard
  - counter: cost analysis per operation, authorise per node
- `W03-0041` Content-Disposition filename carries a stored hostile value
  - counter: generate safe filenames, encode per RFC

## C12: protocol lifecycle

retired versions decommissioned, one policy point

- `W02-0049` Retired API version still writes with the old guard
  - counter: retire versions, or route them through the current policy layer
- `W02-0050` Legacy protocol endpoint bypasses the modern authorisation layer
  - counter: decommission or front with one policy proxy

