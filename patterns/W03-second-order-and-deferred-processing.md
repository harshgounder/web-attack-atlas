# W03: second-order and deferred processing

Generated from `waves/W03/patterns.jsonl`. Do not edit by hand.
50 patterns. Every one answers the five questions and carries a counter.

## Index

| id | pattern | atoms | persists | counter mechanism |
|---|---|---|---|---|
| W03-0001 | Stored value rendered unescaped in a privileged console | A01, A02 | until the record is edited or deleted | context aware escaping at render, plus CSP |
| W03-0002 | Spreadsheet formula injection through an export | A01, A10 | in the file, permanently | prefix neutralisation on export, and formula disabled policy |
| W03-0003 | Stored content reaches a PDF or document renderer | A01, A08 | the document persists and is forwarded | render in a sandbox with egress denied, strip active content |
| W03-0004 | Stored value rendered in an outbound email template | A01, A08 | in the mailbox permanently | template escaping per context, header encoding |
| W03-0005 | Markdown renderer sanitizer differential | A01, A05 | until edited | sanitize the rendered output, not the input |
| W03-0006 | SVG upload rendered inline on a shared origin | A01, A05 | until the asset is removed | serve user uploads from a separate origin, force download, sanitize |
| W03-0007 | Filename stored and rendered in a listing without escaping | A01, A06 | until renamed | escape on render, generate display names, validate charset |
| W03-0008 | Profile field rendered inside a third party embed or widget | A01, A02 | everywhere the embed loads | escape for the embed context, or render in a sandboxed iframe |
| W03-0009 | Webhook fires later and fetches an attacker chosen URL | A02, A07 | every event, indefinitely | destination allowlist, egress filtering, no redirect following |
| W03-0010 | Thumbnail or preview generation fetches a stored URL | A02, A07 | on upload, and on reprocess | fetch through a proxy with an allowlist and no private ranges |
| W03-0011 | Deferred SSRF through an HTML to image or document converter | A02, A01 | per conversion | deny egress, pre-fetch assets yourself |
| W03-0012 | Link preview or unfurl fetches on someone else's behalf | A02, A14 | each message posted | bot in a segmented network, allowlist, no redirects to private ranges |
| W03-0013 | Second order SQL injection through a stored value | A01, A04 | until the value is changed | parameterise every query including batch jobs |
| W03-0014 | Stored filename reaches a shell in a batch job | A01, A06 | on each batch run | never interpolate filenames into commands, use argv |
| W03-0015 | Stored template fragment compiled later | A01, A05 | until the fragment is removed | logic-less templates, never compile user input |
| W03-0016 | Log poisoning used as the input for a later file read | A01, A06 | until log rotation | logs outside the web root, no dynamic include |
| W03-0017 | Cache poisoning via a stored value reflected into a shared cache entry | A06, A04 | until TTL or purge | key every varying input, or do not cache |
| W03-0018 | Cache deception stores a private page under a public path | A06, A08 | until TTL | cache only by explicit rule, normalize before keying |
| W03-0019 | Queue message injected with a field the worker trusts | A02, A05 | on each processed message | sign messages, never trust body identity |
| W03-0020 | Internal header trusted by a worker after the edge stripped it | A03, A02 | per request | strip inbound internal headers at the edge, mTLS between services |
| W03-0021 | Report generator builds a shell command from stored data | A01, A10 | each run | library calls not shell, argv only |
| W03-0022 | Report chart loads an image from a stored URL | A02, A01 | each render | allowlist image hosts, no schemes |
| W03-0023 | Scheduled import re-reads a URL the user supplied once | A02, A04 | each scheduled run | revalidate host on every run, pin to allowlist |
| W03-0024 | Backup restore writes attacker supplied records | A04, A02 | permanent | restore revalidates ownership, restore is a controlled operation |
| W03-0025 | Search index ingestion renders stored markup in results | A01, A05 | until reindex | escape before highlight, mark matches with safe spans |
| W03-0026 | Search suggestion endpoint surfaces content the user cannot open | A08, A02 | until reindex | apply the same authorisation filter to every index entry point |
| W03-0027 | Feed or RSS generation emits stored content unescaped | A01, A08 | until the item rotates out | escape per XML context, strip active content |
| W03-0028 | Webhook delivery can be replayed to repeat a state change | A04, A12 | repeated per replay | idempotency key plus timestamp window plus signature over the exact bytes |
| W03-0029 | Verification token leaks through a referrer on a deferred redirect | A03, A08 | until token expiry | referrer policy no-referrer, single use short lived tokens, never in query |
| W03-0030 | Unsubscribe or magic link token is long lived and reusable | A03, A05 | until manually invalidated, often forever | purpose bound, single use, short lived, revocable |
| W03-0031 | Invitation link is fetched by a preview bot and consumed | A03, A04 | permanently consumed | never consume on GET, require a confirmation POST |
| W03-0032 | Link preview caches attacker content under a trusted card | A05, A08 | until cache expiry | key previews by content hash or revalidate |
| W03-0033 | oEmbed or embed endpoint fetches attacker JSON and renders it | A05, A01 | per render or cached | provider allowlist, sanitize embed html, sandbox iframes |
| W03-0034 | Crawler or favicon fetch reaches an internal address | A02, A07 | each crawl | resolve then block private ranges, egress proxy |
| W03-0035 | Import of a subscription list triggers fetches of attacker feeds | A02, A04 | recurring | allowlist, per user rate limit, segmented fetcher |
| W03-0036 | Calendar invite injects fields the client trusts | A05, A01 | until deleted, and it propagates | escape and strip CRLF in ICS fields |
| W03-0037 | Calendar attachment causes the client to fetch an external resource | A02, A08 | per view | strip external references, proxy images, plain text descriptions |
| W03-0038 | Generated document leaks data through metadata or hidden layers | A08, A05 | in the file | build the export from an allowlist of fields, flatten and strip |
| W03-0039 | Uploaded image metadata is retained and republished | A08, A05 | until the asset is replaced | strip metadata on ingest, re-encode |
| W03-0040 | Download served with a sniffable type executes in the app origin | A01, A05 | until the file is removed | separate asset origin, nosniff, attachment disposition |
| W03-0041 | Content-Disposition filename carries a stored hostile value | A05, A01 | per download | generate safe filenames, encode per RFC |
| W03-0042 | Archive entry names are used later by a batch unzip | A06, A01 | files persist | canonicalise and contain per entry, no links |
| W03-0043 | Stored blob is deserialised by a later process | A01, A04 | per job | signed or encrypted blobs, allowlisted types |
| W03-0044 | Stored user content becomes part of a shared template | A04, A06 | until the template is edited | never cache user fragments in shared keys |
| W03-0045 | Notification content is rendered in a privileged operator surface | A01, A02 | until the notification is dismissed | one escaping layer for all notification renderers |
| W03-0046 | Audit log viewer renders the log line as markup | A01, A11 | permanent in the log | logs are data, viewer is a data renderer, escape everything |
| W03-0047 | Ticket or comment body executes in the support console | A01, A14 | until the ticket is closed | render as text, sanitize agent side |
| W03-0048 | Pending approval object carries fields the approver trusts | A05, A02 | permanent in the approval record | immutable snapshot at approval, apply exactly that |
| W03-0049 | Deleted object still served from cache or index | A04, A08 | until TTL or reindex | deletion propagates to every derived store, tombstone on read |
| W03-0050 | Revoked or downgraded privilege persists in existing sessions | A03, A04 | until the session ends, which may be never | short lived tokens, revocation list checked per request |

## W03-0001: Stored value rendered unescaped in a privileged console

**Atoms:** `A01` interpreter confusion, `A02` trust boundary crossing  
**State changed:** the DOM of an admin or agent view  
**Acting as:** an operator with more rights than the writer  
**Persistence:** until the record is edited or deleted  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- a low privilege user can write a free text field
- the field is rendered in a staff facing view
- that view escapes differently or not at all

Procedure:
1. write a benign marker into the field from a low privilege account
2. open the staff view that renders it
3. confirm the marker executes or renders as markup, not text

**Oracle:** `the marker executes in the staff session`, `a callback fires from the operator's browser`  
**Negative control:** the same value renders as inert text in the user facing view, proving the staff view is the vulnerable renderer

| mutation axis | variant | why it matters |
|---|---|---|
| context | `attribute_context` | escaping differs inside attribute vs text |

**Detected by:** stored content executing in a privileged origin

**Counter:** context aware escaping at render, plus CSP  
**Counter precondition:** escaping belongs to the render site, not the writer  
**Counter cost:** low

---

## W03-0002: Spreadsheet formula injection through an export

**Atoms:** `A01` interpreter confusion, `A10` logic assumption violation  
**State changed:** a cell in a file an operator opens  
**Acting as:** whoever opens the export  
**Persistence:** in the file, permanently  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- user text is exported to CSV or XLSX without neutralising formula prefixes
- an operator opens it in a spreadsheet
- the spreadsheet resolves external references

Procedure:
1. store a value beginning with a formula prefix in a user controlled field
2. export the dataset as an operator
3. observe whether the cell is interpreted as a formula

**Oracle:** `the cell evaluates on open`, `an outbound request fires from the operator workstation`  
**Negative control:** the same value prefixed to neutralise it renders as text, proving the prefix is the mechanism

| mutation axis | variant | why it matters |
|---|---|---|
| encoding | `tab_or_cr_leading` | some exporters trim only equals |

**Detected by:** exported cell beginning with a formula token

**Counter:** prefix neutralisation on export, and formula disabled policy  
**Counter precondition:** all export paths share the sanitizer  
**Counter cost:** low

---

## W03-0003: Stored content reaches a PDF or document renderer

**Atoms:** `A01` interpreter confusion, `A08` information exposure  
**State changed:** the generated document  
**Acting as:** the recipient  
**Persistence:** the document persists and is forwarded  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- HTML or markup is fed to a headless renderer
- the renderer resolves external resources
- output is delivered to a human

Procedure:
1. store markup that references an external resource
2. trigger the document generation
3. observe the renderer's outbound request and the resulting document

**Oracle:** `the renderer fetches your URL`, `the document contains the injected content`  
**Negative control:** plain text in the same field produces no outbound request

| mutation axis | variant | why it matters |
|---|---|---|
| context | `css_url` | renderers load stylesheets |

**Detected by:** document renderer egress to non allowlisted hosts

**Counter:** render in a sandbox with egress denied, strip active content  
**Counter precondition:** renderer never trusted with user markup  
**Counter cost:** infra

---

## W03-0004: Stored value rendered in an outbound email template

**Atoms:** `A01` interpreter confusion, `A08` information exposure  
**State changed:** an email body delivered to a third party  
**Acting as:** the recipient  
**Persistence:** in the mailbox permanently  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- user text is interpolated into an HTML email
- the mail client renders it
- no escaping on the mail template

Procedure:
1. store markup or a tracking style payload
2. trigger the notification to an account you control
3. inspect the received message source and rendering

**Oracle:** `the client renders the injected markup`, `a remote resource loads on open`  
**Negative control:** the same value in a plain text template arrives escaped

| mutation axis | variant | why it matters |
|---|---|---|
| context | `display_name_header` | header injection changes recipients |

**Detected by:** outbound mail containing user markup

**Counter:** template escaping per context, header encoding  
**Counter precondition:** same sanitizer for every template  
**Counter cost:** low

---

## W03-0005: Markdown renderer sanitizer differential

**Atoms:** `A01` interpreter confusion, `A05` type and shape confusion  
**State changed:** the rendered HTML of stored markdown  
**Acting as:** any reader  
**Persistence:** until edited  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- markdown is stored raw and rendered on read
- sanitizer allowlist differs from the renderer's parser
- renderer supports raw HTML passthrough

Procedure:
1. store markdown that parses differently in the renderer and the sanitizer
2. open the rendered view
3. find a construct the sanitizer allows but the browser executes

**Oracle:** `script executes in the reader's session`, `or an event handler attribute survives`  
**Negative control:** a construct both layers reject renders inert

| mutation axis | variant | why it matters |
|---|---|---|
| syntax | `nested_html_in_code` | sanitizer may skip code blocks |

**Detected by:** markdown containing raw html

**Counter:** sanitize the rendered output, not the input  
**Counter precondition:** one parser for render and sanitize  
**Counter cost:** low

---

## W03-0006: SVG upload rendered inline on a shared origin

**Atoms:** `A01` interpreter confusion, `A05` type and shape confusion  
**State changed:** the origin's DOM context for every viewer  
**Acting as:** viewers  
**Persistence:** until the asset is removed  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- SVG accepted as an image
- served inline rather than as attachment
- same origin as the app

Procedure:
1. upload an SVG containing script and an event handler
2. request the asset directly and via an embed
3. check whether it executes in the app origin

**Oracle:** `script runs when the SVG is viewed`, `or when embedded in a page`  
**Negative control:** the same SVG served as attachment or from a separate origin does not execute

| mutation axis | variant | why it matters |
|---|---|---|
| context | `xlink_href_script` | older parsers allow it |

**Detected by:** svg served with image/svg+xml inline

**Counter:** serve user uploads from a separate origin, force download, sanitize  
**Counter precondition:** no user content on the app origin  
**Counter cost:** infra

---

## W03-0007: Filename stored and rendered in a listing without escaping

**Atoms:** `A01` interpreter confusion, `A06` path and namespace confusion  
**State changed:** every listing view that shows the name  
**Acting as:** viewers  
**Persistence:** until renamed  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- filename is stored verbatim
- rendered into HTML in a table or link
- no escaping on that view

Procedure:
1. upload a file whose name contains markup and a path separator
2. open the file listing
3. inspect how the name renders and where the link points

**Oracle:** `markup executes in the listing`, `or the link target is attacker chosen`  
**Negative control:** a normal filename renders identically and links correctly

| mutation axis | variant | why it matters |
|---|---|---|
| encoding | `unicode_rtl` | visual spoofing of extension |

**Detected by:** filename containing markup or control chars

**Counter:** escape on render, generate display names, validate charset  
**Counter precondition:** filename is data never markup  
**Counter cost:** low

---

## W03-0008: Profile field rendered inside a third party embed or widget

**Atoms:** `A01` interpreter confusion, `A02` trust boundary crossing  
**State changed:** the DOM of an embedded widget on partner sites  
**Acting as:** the partner origin's users  
**Persistence:** everywhere the embed loads  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- profile text is exposed via an embed script
- the embed renders it without escaping
- the widget runs on third party origins

Procedure:
1. set a profile field containing markup
2. load a page that embeds the widget
3. observe execution in the embedding origin

**Oracle:** `script runs in the partner origin`, `or the widget's own frameless context is escaped differently`  
**Negative control:** the same field in the main app view is escaped

| mutation axis | variant | why it matters |
|---|---|---|
| context | `json_in_script_tag` | breakout from a JS string |

**Detected by:** embed payload containing raw html

**Counter:** escape for the embed context, or render in a sandboxed iframe  
**Counter precondition:** embed output treated as public  
**Counter cost:** design

---

## W03-0009: Webhook fires later and fetches an attacker chosen URL

**Atoms:** `A02` trust boundary crossing, `A07` resource exhaustion  
**State changed:** server side network reach  
**Acting as:** the platform  
**Persistence:** every event, indefinitely  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- a member can configure a destination
- the worker fetches it asynchronously
- no egress allowlist

Procedure:
1. set the destination to an internal address you can observe
2. trigger an event
3. watch for a request arriving from the platform's network position

**Oracle:** `the request arrives at your listener with platform characteristics`, `or an internal error differs from an external timeout`  
**Negative control:** a destination you cannot resolve produces a distinct error, proving the fetch happened

| mutation axis | variant | why it matters |
|---|---|---|
| protocol | `redirect_to_internal` | follow redirects |

**Detected by:** webhook egress to private ranges

**Counter:** destination allowlist, egress filtering, no redirect following  
**Counter precondition:** worker network is segmented  
**Counter cost:** infra

---

## W03-0010: Thumbnail or preview generation fetches a stored URL

**Atoms:** `A02` trust boundary crossing, `A07` resource exhaustion  
**State changed:** server side fetch during media processing  
**Acting as:** the platform  
**Persistence:** on upload, and on reprocess  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- an image or link field accepts a remote URL
- the worker downloads it
- no size or host validation

Procedure:
1. submit a URL pointing to an address you control on the internal side or an external collector
2. trigger processing
3. observe the request

**Oracle:** `request arrives at your collector`, `or processing succeeds for an internal host that should not be reachable`  
**Negative control:** an invalid URL fails at validation rather than fetch

| mutation axis | variant | why it matters |
|---|---|---|
| encoding | `dns_rebinding` | resolve check then fetch |

**Detected by:** media worker egress anomalies

**Counter:** fetch through a proxy with an allowlist and no private ranges  
**Counter precondition:** resolve and connect to the same address  
**Counter cost:** infra

---

## W03-0011: Deferred SSRF through an HTML to image or document converter

**Atoms:** `A02` trust boundary crossing, `A01` interpreter confusion  
**State changed:** the renderer's network position  
**Acting as:** the renderer  
**Persistence:** per conversion  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- user HTML or CSS is converted
- the converter loads remote assets
- converter runs inside the perimeter

Procedure:
1. submit markup referencing a resource you control
2. let the conversion run
3. observe the callback and what the converter sent

**Oracle:** `callback received with a user agent matching the converter`, `converted output contains data from the internal fetch`  
**Negative control:** local-only markup produces no callback

| mutation axis | variant | why it matters |
|---|---|---|
| context | `iframe_src` | converters honour frames |

**Detected by:** converter egress

**Counter:** deny egress, pre-fetch assets yourself  
**Counter precondition:** converter treated as untrusted  
**Counter cost:** infra

---

## W03-0012: Link preview or unfurl fetches on someone else's behalf

**Atoms:** `A02` trust boundary crossing, `A14` human manipulation  
**State changed:** the preview bot's network reach and the victim's client IP exposure  
**Acting as:** the platform bot  
**Persistence:** each message posted  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- posting a link triggers server side unfurl
- bot egress is broad
- preview is delivered to recipients

Procedure:
1. post a link to an address you control
2. observe the bot request and its headers
3. point it at an internal host in scope and compare

**Oracle:** `bot request arrives at your collector`, `or the preview shows internal content`  
**Negative control:** a link to an unresolvable host shows no preview

| mutation axis | variant | why it matters |
|---|---|---|
| protocol | `redirect_chain` | each hop may be validated differently |

**Detected by:** unfurl bot egress

**Counter:** bot in a segmented network, allowlist, no redirects to private ranges  
**Counter precondition:** bot has no internal reach  
**Counter cost:** infra

---

## W03-0013: Second order SQL injection through a stored value

**Atoms:** `A01` interpreter confusion, `A04` state confusion  
**State changed:** a later query built from stored data  
**Acting as:** the application  
**Persistence:** until the value is changed  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- input is stored escaped or safely
- a later process reads it and concatenates into SQL
- different code path, different trust

Procedure:
1. store a benign looking value that includes quote and comment syntax
2. trigger the later process, a report, export or reconciliation job
3. observe error signatures or behaviour change

**Oracle:** `error signature appears only after the deferred step`, `or a time delay proportional to the payload`  
**Negative control:** the same value never processed by the job produces no delay

| mutation axis | variant | why it matters |
|---|---|---|
| timing | `delayed_trigger` | job runs on a schedule |

**Detected by:** query errors in batch jobs

**Counter:** parameterise every query including batch jobs  
**Counter precondition:** no string concatenation anywhere  
**Counter cost:** low

**Tools (resolve in ai-web-arsenal):** `sqlmap`

---

## W03-0014: Stored filename reaches a shell in a batch job

**Atoms:** `A01` interpreter confusion, `A06` path and namespace confusion  
**State changed:** the filesystem and process namespace of a worker  
**Acting as:** the worker  
**Persistence:** on each batch run  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- filename is used in a command or a glob
- no quoting
- worker runs with more rights than the uploader

Procedure:
1. upload a file with a name containing shell metacharacters
2. trigger the batch that processes it
3. observe side effects in the working directory

**Oracle:** `a file appears where the command created it`, `or a callback fires from the worker`  
**Negative control:** a normal filename produces no extra artefacts

| mutation axis | variant | why it matters |
|---|---|---|
| encoding | `glob_wildcard` | expansion without a shell |

**Detected by:** filenames with metacharacters reaching a job

**Counter:** never interpolate filenames into commands, use argv  
**Counter precondition:** no shell=True anywhere  
**Counter cost:** low

---

## W03-0015: Stored template fragment compiled later

**Atoms:** `A01` interpreter confusion, `A05` type and shape confusion  
**State changed:** the template namespace  
**Acting as:** the server  
**Persistence:** until the fragment is removed  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- users may store text that is later compiled as a template
- template engine evaluates expressions
- compile happens in a different path than save

Procedure:
1. store template syntax in a field that is compiled later
2. trigger the render
3. look for expression evaluation or errors naming internals

**Oracle:** `expression result appears in output`, `or an error reveals engine internals`  
**Negative control:** the same syntax in a plain text field renders literally

| mutation axis | variant | why it matters |
|---|---|---|
| context | `nested_delimiters` | engine specific |

**Detected by:** user content compiled as template

**Counter:** logic-less templates, never compile user input  
**Counter precondition:** user text is data  
**Counter cost:** design

---

## W03-0016: Log poisoning used as the input for a later file read

**Atoms:** `A01` interpreter confusion, `A06` path and namespace confusion  
**State changed:** a file the application will include  
**Acting as:** the application  
**Persistence:** until log rotation  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- user input reaches a log written to disk
- another component includes or reads that file
- path is reachable

Procedure:
1. write a payload into a logged field
2. trigger the include of the log path
3. check execution

**Oracle:** `payload executes when the log is included`, `or the log content appears in output`  
**Negative control:** the include of a path you never wrote to fails

| mutation axis | variant | why it matters |
|---|---|---|
| encoding | `newline_injection` | multiline payloads survive logging |

**Detected by:** log file included by the application

**Counter:** logs outside the web root, no dynamic include  
**Counter precondition:** log path never user influenced  
**Counter cost:** low

---

## W03-0017: Cache poisoning via a stored value reflected into a shared cache entry

**Atoms:** `A06` path and namespace confusion, `A04` state confusion  
**State changed:** a cached response served to many users  
**Acting as:** every later requester  
**Persistence:** until TTL or purge  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- a response reflects stored or request data
- cache key omits that input
- shared cache in front

Procedure:
1. find the unkeyed input
2. cause a response to be cached containing your value
3. request from a clean session

**Oracle:** `second session receives your value`, `cached header present`  
**Negative control:** a cache bypass header returns the clean response

| mutation axis | variant | why it matters |
|---|---|---|
| protocol | `header_case_or_order` | key normalisation |

**Detected by:** cache key audit, response variance per unkeyed input

**Counter:** key every varying input, or do not cache  
**Counter precondition:** cache review per route  
**Counter cost:** design

---

## W03-0018: Cache deception stores a private page under a public path

**Atoms:** `A06` path and namespace confusion, `A08` information exposure  
**State changed:** a cache entry holding another user's private data  
**Acting as:** the victim  
**Persistence:** until TTL  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- path normalisation differs between cache and origin
- private routes reached with a suffix the origin ignores
- cache stores by full path

Procedure:
1. request a private page with an appended static extension or path segment
2. check whether the response is cached
3. then request the same path without a session

**Oracle:** `private content served without authentication`, `age or cache headers on the response`  
**Negative control:** the same page without the suffix is never cacheable

| mutation axis | variant | why it matters |
|---|---|---|
| encoding | `semicolon_path_param` | origin ignores, cache keys |

**Detected by:** cache hit on an authenticated route

**Counter:** cache only by explicit rule, normalize before keying  
**Counter precondition:** no cache anything by default  
**Counter cost:** design

---

## W03-0019: Queue message injected with a field the worker trusts

**Atoms:** `A02` trust boundary crossing, `A05` type and shape confusion  
**State changed:** what the worker believes about the request  
**Acting as:** the worker's assumed user  
**Persistence:** on each processed message  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- producer and consumer share a schema
- consumer trusts fields the producer derived, such as user id
- attacker can influence the message body

Procedure:
1. find a field that carries identity or tenancy into the queue
2. craft a job whose body carries a different identity
3. observe what the worker does

**Oracle:** `worker acts as the injected identity`, `result visible in that identity's data`  
**Negative control:** a message with the original identity behaves normally

| mutation axis | variant | why it matters |
|---|---|---|
| type | `string_vs_int_id` | consumer coercion |

**Detected by:** message identity not matching the producer's session

**Counter:** sign messages, never trust body identity  
**Counter precondition:** worker re-derives identity  
**Counter cost:** low

---

## W03-0020: Internal header trusted by a worker after the edge stripped it

**Atoms:** `A03` identity confusion, `A02` trust boundary crossing  
**State changed:** the authenticated identity inside the service mesh  
**Acting as:** any user  
**Persistence:** per request  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- the edge sets an identity header
- the service trusts that header
- the edge does not strip client supplied copies

Procedure:
1. send a request with your own value for the identity header
2. compare behaviour with and without
3. test from a path that bypasses the edge if one exists

**Oracle:** `the service acts as the injected identity`, `data from that identity returned`  
**Negative control:** a random value for the header is rejected or creates no access

| mutation axis | variant | why it matters |
|---|---|---|
| protocol | `header_case` | stripping is case sensitive |

**Detected by:** client supplied internal header

**Counter:** strip inbound internal headers at the edge, mTLS between services  
**Counter precondition:** edge is the only ingress  
**Counter cost:** low

---

## W03-0021: Report generator builds a shell command from stored data

**Atoms:** `A01` interpreter confusion, `A10` logic assumption violation  
**State changed:** the reporting host  
**Acting as:** the reporting service  
**Persistence:** each run  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- report export shells out to a converter
- parameters include stored user data
- no argv separation

Procedure:
1. store data that appears in a report title or filename
2. run the export
3. look for side effects or timing

**Oracle:** `extra artefact appears`, `or a delay proportional to injected command`  
**Negative control:** a title without metacharacters produces a clean run

| mutation axis | variant | why it matters |
|---|---|---|
| encoding | `newline_in_parameter` | argument splitting |

**Detected by:** export job spawning shells

**Counter:** library calls not shell, argv only  
**Counter precondition:** no shell in reporting  
**Counter cost:** low

---

## W03-0022: Report chart loads an image from a stored URL

**Atoms:** `A02` trust boundary crossing, `A01` interpreter confusion  
**State changed:** the reporting host's network  
**Acting as:** the report service  
**Persistence:** each render  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- chart or logo accepts a URL
- server renders the report
- no host restriction

Procedure:
1. set a dataset label or logo to a URL you control
2. generate the report
3. observe the fetch

**Oracle:** `request arrives from the reporting host`  
**Negative control:** a data URI produces no external request

| mutation axis | variant | why it matters |
|---|---|---|
| protocol | `file_scheme` | local file read by the renderer |

**Detected by:** report renderer egress

**Counter:** allowlist image hosts, no schemes  
**Counter precondition:** renderer sandboxed  
**Counter cost:** low

---

## W03-0023: Scheduled import re-reads a URL the user supplied once

**Atoms:** `A02` trust boundary crossing, `A04` state confusion  
**State changed:** what the system believes about external data  
**Acting as:** the import job  
**Persistence:** each scheduled run  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- an import source URL is stored at setup
- the job fetches it on a schedule
- the URL is not revalidated

Procedure:
1. set a source URL you control
2. observe scheduled fetches
3. change the response content between runs to see what the importer trusts

**Oracle:** `scheduled requests arrive`, `imported data changes without a UI action`  
**Negative control:** a source that stops responding stops the import, proving the fetch is real

| mutation axis | variant | why it matters |
|---|---|---|
| timing | `slow_drip` | importer may time out partially |

**Detected by:** import fetches to changed hosts

**Counter:** revalidate host on every run, pin to allowlist  
**Counter precondition:** URL is not a capability  
**Counter cost:** low

---

## W03-0024: Backup restore writes attacker supplied records

**Atoms:** `A04` state confusion, `A02` trust boundary crossing  
**State changed:** the database after a restore  
**Acting as:** the restorer  
**Persistence:** permanent  
**Status:** PROBABLE  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- restore accepts an uploaded archive
- records are inserted without revalidation
- restore is privileged

Procedure:
1. export, modify identifiers or ownership fields, re-import
2. observe which accounts the records belong to after restore

**Oracle:** `records land under a different owner`, `or appear in another tenant`  
**Negative control:** an unmodified export restores identically

| mutation axis | variant | why it matters |
|---|---|---|
| type | `sqlite_vs_json` | different restore paths |

**Detected by:** restore with cross tenant ids

**Counter:** restore revalidates ownership, restore is a controlled operation  
**Counter precondition:** no blind insert  
**Counter cost:** process

---

## W03-0025: Search index ingestion renders stored markup in results

**Atoms:** `A01` interpreter confusion, `A05` type and shape confusion  
**State changed:** the highlighted results page  
**Acting as:** searchers  
**Persistence:** until reindex  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- indexed fields contain user text
- the UI highlights matches by injecting markup around them
- highlighting does not escape the source

Procedure:
1. store markup in an indexed field
2. search for a term that highlights inside it
3. inspect the rendered result

**Oracle:** `markup executes in the results page`  
**Negative control:** the same term in a non indexed field is not highlighted

| mutation axis | variant | why it matters |
|---|---|---|
| context | `highlight_boundary_breakout` | splitting the term across tags |

**Detected by:** search result DOM containing raw markup

**Counter:** escape before highlight, mark matches with safe spans  
**Counter precondition:** highlighting operates on escaped text  
**Counter cost:** low

---

## W03-0026: Search suggestion endpoint surfaces content the user cannot open

**Atoms:** `A08` information exposure, `A02` trust boundary crossing  
**State changed:** what the search index will disclose  
**Acting as:** a lower privileged searcher  
**Persistence:** until reindex  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- index includes objects the searcher cannot open
- the suggestion endpoint omits the authorisation filter the main search applies
- suggestions are cheap and rate limited leniently

Procedure:
1. index or observe a private object as a user who can see it
2. query suggestions as a user who cannot
3. compare the suggestion set with the main search result set

**Oracle:** `private object titles appear in suggestions`, `the main search excludes them`  
**Negative control:** a title belonging to a fully public object appears in both

| mutation axis | variant | why it matters |
|---|---|---|
| encoding | `partial_words_and_tokens` | prefix search bypasses filters |

**Detected by:** suggestion results not filtered by access

**Counter:** apply the same authorisation filter to every index entry point  
**Counter precondition:** filters cannot be skipped per endpoint  
**Counter cost:** query cost

---

## W03-0027: Feed or RSS generation emits stored content unescaped

**Atoms:** `A01` interpreter confusion, `A08` information exposure  
**State changed:** the feed consumed by aggregators and readers  
**Acting as:** feed subscribers  
**Persistence:** until the item rotates out  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- a feed is generated from user content
- CDATA or XML escaping is incomplete
- readers render HTML in descriptions

Procedure:
1. store markup in a field that appears in the feed
2. fetch the feed and inspect raw XML
3. subscribe in a reader and observe rendering

**Oracle:** `markup survives into the reader`, `or the XML structure is broken by the payload`  
**Negative control:** a plain text value appears escaped in the same feed

| mutation axis | variant | why it matters |
|---|---|---|
| encoding | `cdata_breakout` | ] ]> terminator |

**Detected by:** feed output containing raw user markup

**Counter:** escape per XML context, strip active content  
**Counter precondition:** feeds treat user text as data  
**Counter cost:** low

---

## W03-0028: Webhook delivery can be replayed to repeat a state change

**Atoms:** `A04` state confusion, `A12` timing and ordering  
**State changed:** whatever the receiver applies on each delivery  
**Acting as:** the receiver  
**Persistence:** repeated per replay  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- deliveries are signed but the timestamp or nonce is not enforced
- the receiver is idempotent by hope not by design
- a captured delivery can be resent

Procedure:
1. capture a legitimate delivery you can observe
2. resend it unchanged and with a modified body
3. observe whether the receiver applies it again

**Oracle:** `the receiver applies the same change twice`, `or a modified body is accepted with the original signature`  
**Negative control:** a delivery with an expired timestamp is rejected, proving timestamp checking exists and replay is the gap

| mutation axis | variant | why it matters |
|---|---|---|
| timing | `delayed_replay` | window expiry |

**Detected by:** duplicate delivery id processed

**Counter:** idempotency key plus timestamp window plus signature over the exact bytes  
**Counter precondition:** receiver enforces all three  
**Counter cost:** low

---

## W03-0029: Verification token leaks through a referrer on a deferred redirect

**Atoms:** `A03` identity confusion, `A08` information exposure  
**State changed:** the secrecy of an account activation token  
**Acting as:** the account being claimed  
**Persistence:** until token expiry  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- the token is in a URL
- the landing page loads third party resources or redirects
- no referrer policy

Procedure:
1. request a verification link for an account you control
2. open it in a client that loads third party assets
3. observe the referrer sent to a host you control

**Oracle:** `the token arrives in a referrer header at your collector`  
**Negative control:** a direct request with no external assets sends no referrer

| mutation axis | variant | why it matters |
|---|---|---|
| context | `meta_refresh_chain` | two hops |

**Detected by:** token in referrer

**Counter:** referrer policy no-referrer, single use short lived tokens, never in query  
**Counter precondition:** tokens never in URLs where avoidable  
**Counter cost:** low

---

## W03-0030: Unsubscribe or magic link token is long lived and reusable

**Atoms:** `A03` identity confusion, `A05` type and shape confusion  
**State changed:** the ability to act as the account  
**Acting as:** the account owner  
**Persistence:** until manually invalidated, often forever  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- the link carries a durable token
- the token is not bound to a purpose or expiry
- the action it performs is state changing

Procedure:
1. capture your own link
2. wait past the stated window if any
3. use it twice and from a different client

**Oracle:** `both uses succeed`, `the action applies again`  
**Negative control:** a token with a corrupted signature is rejected

| mutation axis | variant | why it matters |
|---|---|---|
| type | `token_in_path_vs_query` | different handlers |

**Detected by:** token reuse

**Counter:** purpose bound, single use, short lived, revocable  
**Counter precondition:** token is a capability with limits  
**Counter cost:** low

---

## W03-0031: Invitation link is fetched by a preview bot and consumed

**Atoms:** `A03` identity confusion, `A04` state confusion  
**State changed:** whether the invite is still valid  
**Acting as:** the invitee  
**Persistence:** permanently consumed  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- invite links are single use on GET
- link preview bots fetch URLs
- no distinction between a bot and a human

Procedure:
1. create an invite to a mailbox you control
2. let the mail client or chat unfurl the link
3. attempt to use it as a human

**Oracle:** `the invite is reported used`, `or the acceptance page shows an error on first visit`  
**Negative control:** an invite delivered without unfurling is still usable

| mutation axis | variant | why it matters |
|---|---|---|
| timing | `partial_get_then_confirm` | check on GET, apply on POST |

**Detected by:** invite consumed without a user agent match

**Counter:** never consume on GET, require a confirmation POST  
**Counter precondition:** safe methods do not change state  
**Counter cost:** low

---

## W03-0032: Link preview caches attacker content under a trusted card

**Atoms:** `A05` type and shape confusion, `A08` information exposure  
**State changed:** what other users see for a URL  
**Acting as:** readers of the message  
**Persistence:** until cache expiry  
**Status:** PROBABLE  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- preview metadata is fetched once and cached by URL
- the cache key ignores the poster
- preview renders title, image, description

Procedure:
1. post a URL whose metadata you control
2. have a second account post the same URL after you change the metadata
3. observe which metadata is shown

**Oracle:** `the second poster sees your metadata`, `the card does not match the live page`  
**Negative control:** a URL with a cache busting query shows the current metadata

| mutation axis | variant | why it matters |
|---|---|---|
| encoding | `case_or_trailing_slash` | key normalisation |

**Detected by:** preview mismatch with live page

**Counter:** key previews by content hash or revalidate  
**Counter precondition:** preview is not authoritative for long  
**Counter cost:** low

---

## W03-0033: oEmbed or embed endpoint fetches attacker JSON and renders it

**Atoms:** `A05` type and shape confusion, `A01` interpreter confusion  
**State changed:** the embed HTML on the page  
**Acting as:** page visitors  
**Persistence:** per render or cached  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- the app renders third party oEmbed responses
- fields are inserted into HTML without escaping
- provider allowlist is loose or absent

Procedure:
1. serve an oEmbed response with markup in a field
2. get the app to embed your URL
3. observe the rendered page

**Oracle:** `markup executes on the embedding page`  
**Negative control:** a provider that returns plain text renders inert

| mutation axis | variant | why it matters |
|---|---|---|
| context | `iframe_src_javascript` | embed html field |

**Detected by:** embed html containing script from a non allowlisted provider

**Counter:** provider allowlist, sanitize embed html, sandbox iframes  
**Counter precondition:** third party responses are untrusted  
**Counter cost:** low

---

## W03-0034: Crawler or favicon fetch reaches an internal address

**Atoms:** `A02` trust boundary crossing, `A07` resource exhaustion  
**State changed:** the crawler's network position  
**Acting as:** the platform  
**Persistence:** each crawl  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- the platform fetches favicons or link metadata for stored URLs
- no private range blocking
- crawler runs inside the network

Procedure:
1. store a URL pointing at an internal address
2. wait for or trigger the crawl
3. observe timing or error differences

**Oracle:** `response differs between an internal host and a closed port`, `or a callback arrives`  
**Negative control:** an unresolvable host times out differently

| mutation axis | variant | why it matters |
|---|---|---|
| encoding | `decimal_ip` | naive filters miss alternate encodings |

**Detected by:** crawler egress to private ranges

**Counter:** resolve then block private ranges, egress proxy  
**Counter precondition:** crawler segmented  
**Counter cost:** infra

---

## W03-0035: Import of a subscription list triggers fetches of attacker feeds

**Atoms:** `A02` trust boundary crossing, `A04` state confusion  
**State changed:** what gets fetched and imported on a schedule  
**Acting as:** the importer  
**Persistence:** recurring  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- OPML or feed import accepts arbitrary URLs
- the importer fetches each on a schedule
- no allowlist

Procedure:
1. import a feed URL you control
2. observe recurring fetches
3. point a second entry at an internal host in scope

**Oracle:** `recurring requests arrive at your collector`  
**Negative control:** a feed that returns invalid XML is dropped after the first fetch, proving per URL behaviour

| mutation axis | variant | why it matters |
|---|---|---|
| timing | `slow_feed` | resource retention |

**Detected by:** feed fetches to non allowlisted hosts

**Counter:** allowlist, per user rate limit, segmented fetcher  
**Counter precondition:** import is untrusted input  
**Counter cost:** infra

---

## W03-0036: Calendar invite injects fields the client trusts

**Atoms:** `A05` type and shape confusion, `A01` interpreter confusion  
**State changed:** the recipient's calendar and its rendering  
**Acting as:** the recipient  
**Persistence:** until deleted, and it propagates  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- the app generates ICS from user fields
- fields are not escaped for the ICS grammar
- clients render descriptions as HTML or text

Procedure:
1. create an event with line breaks and property names in a field
2. send the invite to an account you control
3. inspect the ICS and how the client renders it

**Oracle:** `an injected property appears in the client`, `or the event details render markup`  
**Negative control:** a field without CRLF produces no extra property

| mutation axis | variant | why it matters |
|---|---|---|
| encoding | `folded_lines` | 75 octet folding |

**Detected by:** ics containing unexpected properties

**Counter:** escape and strip CRLF in ICS fields  
**Counter precondition:** generator treats fields as data  
**Counter cost:** low

---

## W03-0037: Calendar attachment causes the client to fetch an external resource

**Atoms:** `A02` trust boundary crossing, `A08` information exposure  
**State changed:** the recipient's IP and client fingerprint exposure  
**Acting as:** the recipient  
**Persistence:** per view  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- event attachments or images accept URLs
- the client loads them automatically
- no proxying

Procedure:
1. create an event whose description references an image you control
2. invite an account you control
3. observe the fetch and its headers

**Oracle:** `request arrives when the event is opened`, `headers reveal client and approximate location by IP`  
**Negative control:** an event with no external reference produces no request

| mutation axis | variant | why it matters |
|---|---|---|
| context | `html_in_description` | some clients render html |

**Detected by:** client fetching external resources for calendar

**Counter:** strip external references, proxy images, plain text descriptions  
**Counter precondition:** calendar content is untrusted  
**Counter cost:** low

---

## W03-0038: Generated document leaks data through metadata or hidden layers

**Atoms:** `A08` information exposure, `A05` type and shape confusion  
**State changed:** what the exported file carries beyond what is shown  
**Acting as:** the recipient  
**Persistence:** in the file  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- export includes internal fields or comments
- or redaction is visual not structural
- or the file keeps revision history

Procedure:
1. export a document you can create
2. inspect metadata, deleted content, layers and embedded files
3. compare with what the UI shows

**Oracle:** `extractable content the UI never displayed`  
**Negative control:** a document created without the sensitive field carries no trace

| mutation axis | variant | why it matters |
|---|---|---|
| context | `hidden_slide_or_layer` | redaction by overlay |

**Detected by:** export containing non displayed fields

**Counter:** build the export from an allowlist of fields, flatten and strip  
**Counter precondition:** export is a projection, not a dump  
**Counter cost:** low

**Tools (resolve in ai-web-arsenal):** `fq`

---

## W03-0039: Uploaded image metadata is retained and republished

**Atoms:** `A08` information exposure, `A05` type and shape confusion  
**State changed:** what the platform discloses about the uploader  
**Acting as:** the uploader  
**Persistence:** until the asset is replaced  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- the platform strips no metadata
- originals or derivatives are served
- metadata includes location, device, author

Procedure:
1. upload an image with known EXIF fields
2. request the served asset
3. read its metadata

**Oracle:** `EXIF survives in the served file`  
**Negative control:** an image uploaded through a path that strips metadata carries none

| mutation axis | variant | why it matters |
|---|---|---|
| context | `thumbnail_keeps_exif` | derivatives often skip stripping |

**Detected by:** served asset with EXIF

**Counter:** strip metadata on ingest, re-encode  
**Counter precondition:** one ingest pipeline  
**Counter cost:** low

**Tools (resolve in ai-web-arsenal):** `re_media`

---

## W03-0040: Download served with a sniffable type executes in the app origin

**Atoms:** `A01` interpreter confusion, `A05` type and shape confusion  
**State changed:** the origin context of every downloader  
**Acting as:** downloaders  
**Persistence:** until the file is removed  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- upload accept types loosely
- download sets no content type or nosniff
- files served from the app origin

Procedure:
1. upload a file whose content is HTML but whose declared type is benign
2. request it directly
3. observe whether the browser renders it as a document in the app origin

**Oracle:** `the file renders as HTML on the app origin`, `script runs in that origin`  
**Negative control:** the same file served as an attachment downloads instead of rendering

| mutation axis | variant | why it matters |
|---|---|---|
| context | `polyglot_image_html` | valid as both |

**Detected by:** user upload served inline from the app origin

**Counter:** separate asset origin, nosniff, attachment disposition  
**Counter precondition:** user files never on app origin  
**Counter cost:** infra

---

## W03-0041: Content-Disposition filename carries a stored hostile value

**Atoms:** `A05` type and shape confusion, `A01` interpreter confusion  
**State changed:** where the browser saves the file, and how it renders the name  
**Acting as:** the downloader  
**Persistence:** per download  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- the download filename comes from stored user data
- not encoded for the header
- the client honours the value

Procedure:
1. store a filename with quotes, separators and markup
2. download it
3. inspect the suggested filename and any rendering

**Oracle:** `the saved path escapes the download directory`, `or the name renders as markup`  
**Negative control:** a plain filename saves normally

| mutation axis | variant | why it matters |
|---|---|---|
| encoding | `rfc5987_extended` | filename* handling differs |

**Detected by:** content-disposition with control characters

**Counter:** generate safe filenames, encode per RFC  
**Counter precondition:** stored name never used raw  
**Counter cost:** low

---

## W03-0042: Archive entry names are used later by a batch unzip

**Atoms:** `A06` path and namespace confusion, `A01` interpreter confusion  
**State changed:** the filesystem after the job runs  
**Acting as:** the worker  
**Persistence:** files persist  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- an archive is stored then processed asynchronously
- the extractor trusts entry names
- the worker runs with more rights

Procedure:
1. upload an archive whose entries contain traversal or absolute paths
2. wait for the batch
3. attempt to read the out of place file through the app

**Oracle:** `a file exists outside the extraction root`, `content reachable via a served path`  
**Negative control:** a clean archive extracts entirely inside the root

| mutation axis | variant | why it matters |
|---|---|---|
| encoding | `symlink_entry` | link then write through |

**Detected by:** archive entry with traversal

**Counter:** canonicalise and contain per entry, no links  
**Counter precondition:** extraction is a sandbox  
**Counter cost:** low

---

## W03-0043: Stored blob is deserialised by a later process

**Atoms:** `A01` interpreter confusion, `A04` state confusion  
**State changed:** the worker process  
**Acting as:** the worker  
**Persistence:** per job  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- objects are serialised into a store and rebuilt later
- the store is user influenceable
- the reader uses a dangerous format

Procedure:
1. identify what is stored serialised, sessions, caches, jobs, drafts
2. influence that value
3. trigger the read

**Oracle:** `deserialisation side effect, callback or crash signature`  
**Negative control:** a tampered value in a signed store is rejected, proving integrity exists elsewhere

| mutation axis | variant | why it matters |
|---|---|---|
| context | `nested_container` | deeper object graph |

**Detected by:** deserialisation of unsigned user data

**Counter:** signed or encrypted blobs, allowlisted types  
**Counter precondition:** no polymorphic deserialisation  
**Counter cost:** low

**Tools (resolve in ai-web-arsenal):** `ysoserial`

---

## W03-0044: Stored user content becomes part of a shared template

**Atoms:** `A04` state confusion, `A06` path and namespace confusion  
**State changed:** what every visitor of that template receives  
**Acting as:** all visitors  
**Persistence:** until the template is edited  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- a layout or template allows user supplied fragments
- fragments are cached and shared
- no per user keying

Procedure:
1. store a fragment with a unique marker
2. request the shared page as another user
3. check whether the marker appears

**Oracle:** `your marker appears for an unrelated session`  
**Negative control:** the same fragment rendered per user never appears elsewhere

| mutation axis | variant | why it matters |
|---|---|---|
| timing | `race_two_users` | cache stampede |

**Detected by:** shared cache containing user marker

**Counter:** never cache user fragments in shared keys  
**Counter precondition:** template cache is keyed per scope  
**Counter cost:** design

---

## W03-0045: Notification content is rendered in a privileged operator surface

**Atoms:** `A01` interpreter confusion, `A02` trust boundary crossing  
**State changed:** the operator's session  
**Acting as:** an operator  
**Persistence:** until the notification is dismissed  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- a user can trigger a notification whose body they control
- operators see notifications in a richer UI than users
- that UI escapes less

Procedure:
1. trigger a notification with a marker payload
2. observe it in a user view and an operator view
3. compare rendering

**Oracle:** `markup executes only in the operator view`  
**Negative control:** the user view renders the same payload inert

| mutation axis | variant | why it matters |
|---|---|---|
| context | `toast_vs_email_vs_inbox` | three renderers |

**Detected by:** operator UI rendering raw user content

**Counter:** one escaping layer for all notification renderers  
**Counter precondition:** renderers share a code path  
**Counter cost:** low

---

## W03-0046: Audit log viewer renders the log line as markup

**Atoms:** `A01` interpreter confusion, `A11` dependency compromise  
**State changed:** the integrity of the forensic record  
**Acting as:** the auditor  
**Persistence:** permanent in the log  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- logged values include user input
- the viewer renders lines as HTML
- no escaping in the viewer

Procedure:
1. cause an event whose logged field contains markup
2. open the audit viewer as an authorised auditor
3. observe execution

**Oracle:** `markup executes in the auditor session`  
**Negative control:** an event with a clean field renders as text

| mutation axis | variant | why it matters |
|---|---|---|
| encoding | `json_field_breakout` | structured logs still concatenate on display |

**Detected by:** log viewer executing content

**Counter:** logs are data, viewer is a data renderer, escape everything  
**Counter precondition:** never innerHTML a log line  
**Counter cost:** low

---

## W03-0047: Ticket or comment body executes in the support console

**Atoms:** `A01` interpreter confusion, `A14` human manipulation  
**State changed:** the support agent's session  
**Acting as:** the agent  
**Persistence:** until the ticket is closed  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- customers write free text
- agents view it in a console that renders html
- agents hold elevated privileges

Procedure:
1. submit a ticket with a marker payload from a customer account
2. have an agent open it
3. observe execution and what the session can reach

**Oracle:** `markup executes in the agent session`, `a callback proves it`  
**Negative control:** the customer's own view escapes the same payload

| mutation axis | variant | why it matters |
|---|---|---|
| context | `email_in_thread` | email rendering path differs |

**Detected by:** support console rendering raw customer html

**Counter:** render as text, sanitize agent side  
**Counter precondition:** agent console is higher risk, not lower  
**Counter cost:** low

---

## W03-0048: Pending approval object carries fields the approver trusts

**Atoms:** `A05` type and shape confusion, `A02` trust boundary crossing  
**State changed:** what the approver believes they are approving  
**Acting as:** the approver  
**Persistence:** permanent in the approval record  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- submission and approval are separate steps
- the approver UI shows a summary
- the stored object differs from the summary

Procedure:
1. submit a request, then modify fields the approver UI does not show
2. prompt approval
3. compare approved summary with the applied object

**Oracle:** `the applied object differs from the approved summary`  
**Negative control:** a request modified before submission shows the modification in the summary

| mutation axis | variant | why it matters |
|---|---|---|
| timing | `edit_after_approval_before_apply` | TOCTOU |

**Detected by:** approved summary hash differs from applied object

**Counter:** immutable snapshot at approval, apply exactly that  
**Counter precondition:** approval binds to a hash  
**Counter cost:** low

---

## W03-0049: Deleted object still served from cache or index

**Atoms:** `A04` state confusion, `A08` information exposure  
**State changed:** whether deletion actually removes visibility  
**Acting as:** the deleter  
**Persistence:** until TTL or reindex  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- delete removes the primary record
- caches, search, CDN and feeds are not invalidated
- no tombstone check on read

Procedure:
1. create an object with a unique marker
2. delete it
3. query search, direct URL, feeds and cached paths for the marker

**Oracle:** `the object remains reachable through a secondary channel`  
**Negative control:** a never created marker returns nothing through the same channels

| mutation axis | variant | why it matters |
|---|---|---|
| timing | `read_during_delete` | race window |

**Detected by:** read of a deleted object

**Counter:** deletion propagates to every derived store, tombstone on read  
**Counter precondition:** one deletion event  
**Counter cost:** infra

---

## W03-0050: Revoked or downgraded privilege persists in existing sessions

**Atoms:** `A03` identity confusion, `A04` state confusion  
**State changed:** what an established session can still do  
**Acting as:** a user who lost the right  
**Persistence:** until the session ends, which may be never  
**Status:** ESTABLISHED  
**Authorization:** written scope from the target owner, and accounts you control

Preconditions:
- authorisation is cached in the token or session
- revocation does not invalidate sessions
- tokens are long lived

Procedure:
1. establish a session, then revoke or downgrade the account from a second session
2. continue using the original session
3. observe whether the revoked capability still works

**Oracle:** `the revoked action still succeeds in the old session`  
**Negative control:** a freshly created session after revocation is correctly denied

| mutation axis | variant | why it matters |
|---|---|---|
| timing | `revoke_then_refresh` | refresh may mint a stale claim |

**Detected by:** action authorised by a claim older than the revocation

**Counter:** short lived tokens, revocation list checked per request  
**Counter precondition:** revocation is authoritative  
**Counter cost:** latency

---
