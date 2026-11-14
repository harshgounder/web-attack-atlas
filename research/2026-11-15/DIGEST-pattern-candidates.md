# Research digest 2026-11-15: new pattern/atom candidates for the atlas

Sources: research/2026-11-15/patterns-oct-nov-2026.md (105KB), research/2026-11-15/global-tools-2026Q4.md (41KB).
Method: parallel-task pro deep research x2, 2026-11-14, all regions. This digest maps findings to atlas grammar.
Rule: nothing enters patterns/ until it has a lab (quality protocol + labs contract).

## Candidate additions (atom -> supporting evidence)

| candidate | atom | why it is new or newly general | source section |
|---|---|---|---|
| HTTP header injection to CRLF desync chain (composed) | A01 + A12 | composition of header injection into desync shown critical in one workflow, Nov 4 | PortSwigger header injection |
| Shared-parser confusion via automated discovery (HTTP Terminator) | A01 | desync variant discovery automated; new tool class for wave W01/W02 labs | HTTP Terminator |
| SVG sanitizer bypasses (6 of 8 tested) | A05 | type/shape confusion in upload+serve pipelines; new wave candidate W04 content processing | Scalable Vector Grief |
| Prompt injection in HTTP headers (217M responses study) | A16 | AI component instruction-following as boundary, headers as carrier; extends A16 to transport layer | HN thread |
| PHP2Shell: AI-discovered RCE chain in PHP | A01 + A11 | AI-assisted discovery of dependency-level chain | HN thread |
| Neo Triage: proven-exploitability replaces static scores | A14 (evidence) | triage philosophy shift affecting oracle design | ProjectDiscovery |
| APISIX gateway WAF failure modes (decompression, identity headers) | A15 | config divergence at the edge, concrete regression targets | APISIX Oct report |
| Agent defense papers + sleeper-agent neuron patching (<10 neurons) | A16 | model tampering passing evaluations; relevant to AI-surface labs | MSFT research |
| Claude-assisted Chrome 62-vuln chains (RU source) | A02 | agentic vuln discovery at chain scale | Habr |
| JPCERT attack-infrastructure investigation pattern | A13 | operational telemetry as evidence class | JPCERT Eyes |
| BOLA / API flow hijacking (CTEM) | A02 + A10 | authorization as workflow property, matches W02 findings | Yaamlabs roundup |

## Regional sources worth ongoing monitoring (for the denominator)

- CN: 先知社区, FreeBuf, 安全客, 安全KER, 知乎, cybersecurity-daily 网安日报
- RU: Habr, Telegram channels (Claude/Chrome chains, PHP/GitLab CVE pace)
- JP: JPCERT/CC Eyes, ScanNetSecurity (KUSANAGI header injection)
- EN core: PortSwigger research, ProjectDiscovery blog, Yaamlabs roundups, HN, r/netsec

## Gaps the research itself flags (do not assume coverage)

- regional leads with incomplete links (FreeBuf aggregator entries)
- vendor claims (Reflectiz 10x) are marketing until lab-verified
- deleted/private channels permanently uncapturable: class III ceiling applies
