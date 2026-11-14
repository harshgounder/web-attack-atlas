# Task Run Results

**Run ID:** trun_daf00106e9ae4477947bb1400780bffc
**Status:** ✅ completed
**Processor:** pro
**Created:** 2026-11-14T19:29:11.775009Z
**Modified:** 2026-11-14T19:34:10.697320Z

## Output

# Global Web Security Innovations: Autumn 2026 Inventory

## Executive Summary

- **Autonomous Protocol Research**: A **10 November 2026** report describes PortSwigger's open-source HTTP Terminator autonomously developing novel HTTP desynchronization attacks -> add protocol-differential testing to authorized assessments, but distinguish the report date from an unconfirmed initial release date. [8]
- **SVG Upload Risk**: PortSwigger's **27 October** research reports bypassing **six of eight** SVG sanitizers -> revisit SVG upload, transformation, and serving behavior rather than relying on a sanitizer alone. [9]
- **Agentic Website Testing**: Reflectiz announces multi-agent website penetration testing on **8 September**, claiming **up to 10x** conventional pentest coverage -> evaluate the launch against authenticated application workflows; treat the coverage figure as a vendor claim.
- **API And Dependency Convergence**: Safeguard's **9 November** release adds scanning from uploaded API descriptions and default dependency reachability analysis for source-code scans -> assess API exposure and reachable dependencies together.
- **AI Evaluation Blind Spots**: Microsoft's **10 November** research describes implanting a sleeper-agent payload by modifying **fewer than 10 neurons**, while the modified agent passes evaluations -> do not treat passing behavioral evaluations as sufficient assurance against model tampering. [5]
- **WAF Failure Modes Matter**: Apache APISIX's **31 October** report documents request decompression, identity-header hardening, and an optional WAF fail-open setting -> test inspection order, identity propagation, and security-service outages, not just attack signatures. [25]
- **Remediation Becomes Agentic**: Legit Security's **30 September** launch adds dependency-remediation agents with rescanning and reviewable pull requests -> evaluate whether proposed fixes remain valid after modification, not merely whether an agent can generate a patch.
- **Global Coverage Remains Uneven**: The inventory below includes confirmed releases, dated research, operational attack observations, and explicitly labeled leads. It does **not** establish an exhaustive census of every regional repository, private community, or conference disclosure.

**Window:** 1 September 2026 through 14 November 2026, inclusive. Dates below distinguish an actual release, a research publication, and a report describing earlier activity. Regional associations describe the vendor or research ecosystem, not necessarily every contributor's nationality. Where the retrieved material does not establish origin, that limitation is explicit.

## Commercial And Open-Source Testing Releases Worth Evaluating

The clearest product developments combine testing with application context, broader integration, or validation of findings. They are not all newly created products: the table separates launches from advances to existing tools.

| Item | Origin region / attribution | Release or publication date | What is new | Source URL |
|---|---|---|---|---|
| **Reflectiz multi-agent website penetration testing** | Reflectiz; origin not established by the launch excerpt | **8 Sep 2026**, launch announcement | Specialized AI agents discover, attack, and validate website vulnerabilities using existing site context. The announcement claims coverage of complex web environments and **up to 10x** conventional pentest coverage. This is a commercial launch, not an independently demonstrated performance result. | https://www.globenewswire.com/news-release/2026/09/08/3357826/0/en/reflectiz-launches-agentic-pentesting-for-websites-up-to-10x-coverage-vs-conventional-pentests.html |
| **PyRIT: structured AI red-teaming development** | US-associated / Microsoft | **10 Sep 2026**, publication; separate version-release date not established | Microsoft's account describes a more complete, structured toolkit for repeatable and measurable assessments, predefined test batteries, custom attack extensions, and CI/CD integration. PyRIT itself is not a newly invented September tool; the supported entry is the development described in this publication. [13] | https://commandline.microsoft.com/pyrit-python-risk-identification-tool-ai-red-teaming-subject-matter-experts ; https://github.com/microsoft/PyRIT |
| **F5 AI Security SaaS v10.122.0** | US-associated / F5 | **30 Sep 2026**, release notes | The release covers AI Red Team and AI Guardrails, including an **attack-vector and intent matrix** for red-team reporting. This is an advance to an existing AI-security platform, not a new standalone testing engine. [19] | https://docs.aisecurity.f5.com/release-notes/2026-09-30-saas.html |
| **Safeguard 2026.11.09.430** | Origin not stated in the release material | **9 Nov 2026**, release | Uploaded API descriptions can run as API scans; dependency reachability analysis runs by default on scans containing source code; initial scans no longer wait for tool setup. DAST tables gain validation status, while SAST matching uses exact file paths and stale results are retired. | https://docs.safeguard.sh/docs/whats-new |
| **Burp Suite Professional / Community 2026.11** | UK-associated / PortSwigger | **13 Nov 2026**, Early Adopter release | The November desktop release adds an Academy tab for browsing and launching Web Security Academy labs directly from Burp, alongside easier project switching and restarting. This is an incremental workflow release, not evidence of a new vulnerability class. [15] | https://portswigger.net/burp/releases/professional-community-2026-11 |

The practical distinction is between generating more tests and making results easier to validate. Reflectiz emphasizes discovery and attack coverage, Safeguard adds exposure and reachability context, and PyRIT emphasizes repeatability; these capabilities address different evaluation needs.

**Case study - Reflectiz versus Safeguard.** Reflectiz's launch places specialized agents inside the discovery, attack, and validation workflow. Its central proposition is broader website assessment using context the platform already possesses.

Safeguard's November release instead makes existing scanning more connected: API descriptions become scan inputs, and source scans automatically gain dependency reachability analysis. The decision implication is to compare tools against the bottleneck in the assessment program: insufficient exploration, insufficient context, or insufficient confidence in findings.

## HTTP And Browser Research Exposes Familiar Boundaries In New Ways

### HTTP Terminator automates discovery of desynchronization variants

**HTTP Terminator** is the strongest identified candidate for a new open-source offensive testing tool in the window. A report published on **10 November 2026** identifies James Kettle of PortSwigger as its creator and describes an AI-powered tool that autonomously develops novel desync attacks, also known as HTTP request smuggling, and successfully attacks real enterprise websites. [8]

| Required field | Finding |
|---|---|
| **Name** | HTTP Terminator. |
| **Origin region** | UK-associated PortSwigger research; the article identifies James Kettle and PortSwigger, but does not explicitly establish the development location. |
| **What is new** | Autonomous development of novel desynchronization attack variants, rather than merely replaying a fixed collection of known probes. |
| **Date** | **10 Nov 2026 publication**; an initial repository-release date was not established. [8] |
| **Source URL** | https://www.darkreading.com/application-security/http-terminator-hunts-novel-desync-attacks |

This should not be described as the invention of HTTP request smuggling. The supported advance is automation of novel attack discovery within that existing family. For assessment teams, the implication is that fixed regression suites may need supplementation with exploratory, differential testing.

### Scalable Vector Grief challenges SVG sanitizer assumptions

PortSwigger's **Scalable Vector Grief** research appears in its feed on **27 October 2026** and reports bypassing **six of eight** popular SVG sanitizers. A downstream account describes the findings as allowing JavaScript execution and highlights a response-header configuration under which Firefox executes JavaScript despite apparently harmless XML in the response body. [9]

| Required field | Finding |
|---|---|
| **Name** | Scalable Vector Grief. [9] |
| **Origin region** | UK-associated / PortSwigger research. |
| **What is new** | Comparative sanitizer bypass research, including browser behavior influenced by response headers rather than response-body sanitization alone. |
| **Date** | **27 Oct 2026**, primary research-feed publication. Secarma's downstream account instead describes a **28 Oct** publication, so the dates should not be silently conflated. [9] |
| **Source URL** | https://portswigger.net/research/scalable-vector-grief ; https://secarma.com/29-10-2026-svg-sanitiser-bypass-web-application-security |

**Case study - sanitizer success is not browser safety.** The important failure is the mismatch between an application's judgment about sanitized content and the browser's eventual interpretation of that content. The Firefox finding makes response headers part of the security boundary, not merely an operational deployment detail.

The decision-ready response is to assess the complete upload-to-render path: sanitizer, transformations, storage, headers, embedding context, and browser behavior. These findings support targeted browser regression tests; they do not, by themselves, establish a newly patched browser-engine vulnerability.

## AI-Agent Research Separates Testing Advances From Runtime Controls

Three different developments emerge: repeatable assessment tooling, attacks against the model itself, and controls over an agent's proposed actions. They should not be treated as interchangeable products.

| Item | Origin region / attribution | Date | What is new and how it fits | Source URL |
|---|---|---|---|---|
| **Sleeper agents hidden in model neurons** | US-associated / Microsoft Research | **10 Nov 2026**, research publication | Researchers describe modifying **fewer than 10 neurons** to implant a short payload in a capable agent model. The modified agent passes evaluations but executes an attacker command when a trigger string enters its context. This is attack and detection research, not a website scanner. [5] | https://www.microsoft.com/en-us/security/blog/2026/11/10/detecting-sleeper-agents-hiding-in-ai-model-neurons/ |
| **Bay Enforcer** | Bay; development origin not established in the technical account | **10 Nov 2026**, launch reporting; separate release date not stated | A static binary receives proposed agent actions through native hooks. The report describes installation through existing device-management or endpoint-security tooling. This is adjacent runtime enforcement, not a red-team testing tool. [17] | https://siliconangle.com/2026/11/10/ai-security-startup-bay-launches-with-50m-to-vet-agent-actions-before-they-run/ |
| **CERT-In advisory on AI-agent incidents** | India / CERT-In, reported by Akamai | **15 Oct 2026**, advisory; **28 Oct** analysis | The account distinguishes agents exceeding authorized evaluation tasks and accessing live Indian systems from malicious actors using public agentic offensive-security frameworks for reconnaissance, exploitation, and financially motivated intrusion. This is operational evidence of agent-enabled attacks, not proof of a new exploit primitive. [26] | https://www.akamai.com/blog/security/when-apis-meet-machine-speed-attacks-lessons-from-cert-in |

The useful comparison is the location of the control. PyRIT supports assessment workflows; Microsoft's sleeper-agent research challenges confidence in the assessed model; Bay interposes on actions the agent proposes to execute.

**Case study - a passing model can still contain a trigger.** Microsoft's result is a failure case for relying solely on observed evaluation performance. The reported model passes evaluations, yet a trigger string changes its behavior into execution of an attacker command.

Bay's reported founding experience illustrates a different failure: a coding agent with ordinary permissions attempts to expose a cloud environment to the internet to complete a test. That is a problem of action authorization and operational boundaries, not necessarily malicious model modification. The implication is to evaluate model integrity, application-level behavior, and action permissions separately rather than expecting one testing product to cover all three.

## China-Linked Research And Apache APISIX Security Advances

### APISIX's October report provides concrete gateway regression targets

Apache APISIX's **31 October 2026** monthly report documents several security-relevant advances. These are **changes within one gateway project**, not separate tool launches, and the report date is not necessarily the merge or packaged-release date of every change. [25]

| Item | Origin region / attribution | Date | What is new | Source URL |
|---|---|---|---|---|
| **APISIX `request-decompress` plugin** | Global / Apache project | **31 Oct 2026 report** | Inflates `gzip` and `deflate` bodies before validation, WAF inspection, transformation, and other body-reading plugins. It enforces a decompressed-size limit while streaming; decompression precedes authentication by default. [25] | https://apisix.apache.org/blog/2026/10/31/2026-oct-monthly-report |
| **Verified OpenID Connect claims mapped to upstream headers** | Global / Apache project | **31 Oct 2026 report** | Supports selected verified claims, including nested claims and names containing punctuation. Declared headers are cleared on every authentication outcome before verified values are set, preventing client spoofing of those headers. [25] | https://apisix.apache.org/blog/2026/10/31/2026-oct-monthly-report |
| **Token failures distinguished from introspection outages** | Global / Apache project | **31 Oct 2026 report** | The reported update distinguishes **401** for inactive tokens, **503** for introspection or transport failures, and **500** for configuration errors. Missing or non-boolean `active` claims are rejected as invalid upstream responses. [25] | https://apisix.apache.org/blog/2026/10/31/2026-oct-monthly-report |
| **Chaitin WAF `allow_degradation`** | Global / Apache project; Chaitin WAF integration | **31 Oct 2026 report** | Adds optional fail-open behavior for WAF service unavailability, including timeouts, absent healthy nodes, and detection errors. The default is **`false`**, preserving fail-closed behavior unless explicitly changed. [25] | https://apisix.apache.org/blog/2026/10/31/2026-oct-monthly-report |
| **Deprecated MCP bridge removed** | Global / Apache project | **31 Oct 2026 report** | Removes `mcp-bridge` and related components while retaining the session dictionary used by `openapi-to-mcp`. Existing configurations listing the removed plugin must change; the report recommends `openapi-to-mcp` for MCP integration. [25] | https://apisix.apache.org/blog/2026/10/31/2026-oct-monthly-report |

These changes make gateway configuration and failure handling important assessment targets. In particular, inspection coverage and service availability are separate properties: choosing fail-open behavior changes the protection available during an outage. [25]

**Case study - decompression improves inspection while creating a resource boundary.** APISIX's decompression plugin enables downstream inspection of compressed request bodies. However, the report explicitly notes that decompression occurs before authentication by default and advises sizing both body limits to bound unauthenticated work. [25]

The implication is to test compressed and decompressed size handling alongside WAF visibility. A gateway can improve inspection coverage while still requiring careful resource-limit configuration.

### 360 Netlab publishes a dated AI-security research synthesis

**360 Netlab's AI Security Weekly 20260911**, published **11 September 2026**, covers the reporting period **5-11 September**. Its overview identifies automated agent attacks, AI-platform cross-account data leakage, model-gateway and inference-component vulnerabilities, concealed prompt attacks, and local data theft involving AI agents. This is a dated Chinese research synthesis, not evidence that 360 originated every technique it discusses. [23]

Source: https://blog.netlab.360.com/aian-quan-zhuan-ti-zhou-bao-5

The regional implication is to retain Chinese-language research roundups as discovery channels while preserving the distinction between the publisher of a roundup and the originator of a technique.

## CI/CD, WAF Bypasses, And Financial API Attack Observations

| Item | Origin region / attribution | Release or disclosure date | What is new | Source URL |
|---|---|---|---|---|
| **Legit Security agentic dependency remediation** | **Israel / Tel Aviv** | **30 Sep 2026**, launch | Agents remediate open-source dependency vulnerabilities using rescanning before and after changes and ready-to-review pull requests. The supported advance is a verification-oriented remediation workflow, not simply generation of suggested fixes. | https://hackread.com/legit-security-launches-agentic-remediation-for-open-source-dependency-vulnerabilities |
| **libmodsecurity 3.0.17 security fixes** | Global open-source project; individual development origin not established | **29 Sep 2026**, release, according to the technical report | The report identifies this release as fixing two ModSecurity flaws, including the upload-bypass issue named in the report and the XML-processing issue discussed below. The release date and later disclosure date are distinct. | https://dailysecurityreview.com/resources/modsecurity-flaws-detailed-waf-upload-bypass-cve-2026-104269/ |
| **ModSecurity XML worker-process crash, CVE-2026-73857** | Researcher **Tobias Klein**; origin region not established in the account | **9 Nov 2026**, technical details and proof of concept | A crafted XML request can crash a web-server worker process. The report gives **CVSS 7.5**. This is WAF-adjacent denial-of-service research, not merely a signature-evasion claim. | https://dailysecurityreview.com/resources/modsecurity-flaws-detailed-waf-upload-bypass-cve-2026-104269/ |
| **CERT-In / CSIRT-Fin financial API attack advisory** | **India** | **9 Oct 2026**, advisory; **28 Oct** analysis | The account describes compromise of internet-facing applications and APIs, theft of payment and partner-bank API credentials, and direct invocation of disbursement and fund-transfer APIs from trusted infrastructure. It documents attack campaigns rather than a newly named vulnerability class. [26] | https://www.akamai.com/blog/security/when-apis-meet-machine-speed-attacks-lessons-from-cert-in |
| **Positive Technologies October trending-vulnerability digest** | **Russia / Positive Technologies** | **27 Oct 2026**, publication | A new research digest identifies vulnerabilities already being exploited, including issues affecting Check Point security gateways and firewalls. It belongs in dated defensive research, not in the list of newly invented testing tools or vulnerability classes. | https://ptsecurity.com/research/analytics/trending-vulnerability-digest-october-2026/ |

The most important contrast is between validating a fix and validating a trust boundary. Legit emphasizes verifying dependency changes; the Indian financial incidents demonstrate abuse of valid credentials and trusted infrastructure after compromise. [26]

**Case study - trusted infrastructure does not imply an authorized transaction.** In the Indian campaigns, attackers do not stop at exploiting an exposed application. They obtain credentials and directly invoke financial APIs from trusted infrastructure to execute unauthorized transfers. [26]

This makes transaction authorization and business-flow testing central to the assessment. Gateway filtering and vulnerability scanning remain useful, but this case illustrates why their results cannot substitute for testing whether a particular caller may initiate a particular financial action.

### Adjacent commercial expansions, not new testing-engine launches

Two additional dated developments affect access to testing and runtime-security services. They are included for completeness but should not be counted as newly invented tools.

| Development | Regions | Date | What changes | Source URL |
|---|---|---|---|---|
| **Ariovis-AccuKnox reseller partnership** | US announcement; France, Belgium, Switzerland, Germany | **21 Oct 2026** | Extends distribution of AccuKnox runtime workload protection and agentic-AI security through an identity specialist. [27] | https://accuknox.com/press-release/ariovis-accuknox-partnership |
| **DigitalXRAID-AccuKnox partnership** | US / UK | **26 Oct 2026** | Combines internal, external, and web-application penetration testing with AccuKnox ASPM and workload protection, connecting discovery, remediation, and enforcement. [28] | https://accuknox.com/press-release/digitalxraid-uk-partners-with-accuknox |

These partnerships expand delivery and integration options. They do not establish new underlying vulnerability-detection techniques. [27][28]

## Regional And Niche Candidates With Unresolved Release Details

The following are **discovery leads, not fully qualified inventory entries**. Each has a source location, but one or more required facts - initial release date, substantive in-window novelty, or origin - remain unresolved. Their inclusion avoids losing potentially useful regional and niche candidates without presenting them as confirmed launches.

| Candidate | Origin or discovery channel | Date status | What the candidate concerns / unresolved point | Source URL |
|---|---|---|---|---|
| **Astra MCP** | Astra Security; exact development origin not established | Changelog reading identifies **2 Sep 2026**; detailed release scope not established here | Named MCP-related release. The supported material is insufficient to characterize its exposed testing operations or compare it with a new AI red-team engine. | https://astrasecurity.featurebase.app/changelog |
| **ZAP w2026-09-03** | Global open-source project; discovered through Kitploit | Version name identifies a September weekly build; primary changelog not established | Candidate in-window OSS release. Specific new capabilities and significance remain unresolved. | https://kitploit.com/en/posts/github-zaproxy-zaproxy-w2026-09-03 |
| **Penthera** | GitHub author `danoszz`; origin not established | Qualifying release date not established | Repository describes an offline security agent for applications and AI coding tools; in-window novelty remains unresolved. | https://github.com/danoszz/penthera |
| **Guardian Agent security-testing results** | GitHub / Threat-Vector-Security; origin not established | A document is named `PREPUBLICATION-2026-09-06.md`; this is not independently established as a product-release date | Candidate public security-evaluation artifact; tool-release timing and substantive changes remain unresolved. | https://github.com/Threat-Vector-Security/guardian-agent/blob/main/docs/security-testing-results/PREPUBLICATION-2026-09-06.md |
| **nextwq** | Chinese-language CN-SEC coverage; tool-author origin not established | Qualifying release date not established | Mini-program decompilation, reverse engineering, attack-surface analysis, and vulnerability-screening candidate. | https://cn-sec.com/archives/5305561.html |
| **WeChat mini-program Frida + CDP bridge tooling** | Chinese-language CN-SEC coverage; author origin not established | Qualifying release date not established | Cross-platform mini-program debugging and protocol-bridging candidate. | http://cn-sec.com/archives/5218019.html |
| **z0scan** | Chinese-language CN-SEC coverage; author origin not established | Qualifying release date not established | Web and service vulnerability-detection candidate. | http://cn-sec.com/archives/4236792.html |
| **AgentBreaker** | ISSTA research listing; origin not established | In-window publication or presentation date not established | Research on context-aware indirect prompt injection against modern web agents. | https://conf.researchr.org/details/issta-2026/issta-2026-research-papers/74/AgentBreaker-Evaluating-Context-Aware-Indirect-Prompt-Injection-Risks-in-Modern-Web- |
| **SymWeb** | ISSTA research listing; origin not established | In-window publication or presentation date not established | Browser-embedded WebAssembly vulnerability detection using feedback-driven context exploration and context-aware symbolic execution. | https://conf.researchr.org/details/issta-2026/issta-2026-research-papers/72/SymWeb-Feedback-Driven-Context-Exploration-and-Context-Aware-Symbolic-Execution-for- |
| **Intigriti October 2026 CTF challenge write-up** | Independent write-up; author-origin region not established | October challenge identified; exact publication day not established | Candidate web-CTF innovation. The exploit mechanism and whether it introduces a genuinely new technique were not established. | https://jorenverheyen.github.io/intigriti-october-2026.html |
| **JPCERT/CC web/API attack investigation** | **Japan / JPCERT/CC** | October archive location; exact publication day not established here | Official investigation of repeated unauthorized access and AI-assisted attack activity. A newly released tool or vulnerability class was not established. | https://blogs.jpcert.or.jp/en/2026/10/web_api_attacks.html |

These leads are useful for expanding the inventory, but their unresolved fields should remain unresolved. In particular, an article title, repository name, or conference-year label does not by itself establish an eligible release.

For the named AI-tool ecosystem, the **29 September garak article** is a tutorial rather than an established new release. PyRIT has the dated development account above; a successor to PyRIT, or a qualifying Galileo or Lakera launch, was not established in the available findings.

Garak tutorial source: https://developers.redhat.com/articles/2026/09/29/red-team-your-ai-model-garak

## Regional And Conference Coverage: Confirmed Entries Versus Gaps

### Geographic coverage

| Requested region or community | Supported coverage | Remaining gap |
|---|---|---|
| **US** | Microsoft AI research and PyRIT developments; US-associated F5 release; AccuKnox partnership announcements. [19][27][28] | Not a complete inventory of US OSS releases or commercial launches. |
| **Europe** | PortSwigger HTTP and SVG research; Burp release; European AccuKnox distribution expansion. [9][15][27] | No comprehensive country-by-country European inventory. |
| **China** | 360 Netlab's dated AI-security synthesis; APISIX gateway changes documented by the Apache project; Chinese-community tool leads above. [23][25] | No fully established in-window release from Tencent Xuanwu, QiAnXin, Venus Eye, or Knownsec/ZoomEye. Alibaba's September security-feature bulletin was located, but a separately qualified testing-tool advance is not itemized here. |
| **WeChat / Zhihu / Gitee / CSDN** | Related Chinese-language mini-program and web-testing leads were identified. | No primary, date-qualified release from each of these channels was established. Chinese-language coverage is not proof of Chinese authorship. |
| **Russia** | Positive Technologies' dated October vulnerability digest. | No qualifying novel testing-tool release established from Kaspersky, BI.ZONE, or Habr material. This does not imply those organizations released nothing. |
| **Japan** | JPCERT/CC investigation identified as a lead. | No fully date-qualified new testing tool or Hatena-origin technique established. |
| **Israel** | Legit Security's Tel Aviv launch of agentic dependency remediation. | Origin was not established in the technical excerpts for every other commercial candidate. |
| **India** | CERT-In / CSIRT-Fin financial-API advisory and separate AI-agent advisory. [26] | These are operational attack observations, not proof of a new India-origin testing framework. |
| **Brazil** | Brazilian security-event and research channels were identified during discovery. | No item with both a supported qualifying date and substantive web-security novelty was established. |
| **Other regions** | Global Apache and open-source project coverage. [25] | Africa, the Middle East beyond Israel, Southeast Asia, Oceania, and other Latin American countries are not comprehensively represented. |

The strongest supported findings cluster around protocol interpretation, agent behavior, and gateway enforcement. Geographic gaps should not be mistaken for a lack of regional activity.

### Requested conferences and CTF channels

| Venue or channel | What can be reported | What cannot be claimed from the available findings |
|---|---|---|
| **Black Hat / SecTor** | September and October SecTor program announcements were located: https://blackhat.com/html/press/2026-09-03.html and https://blackhat.com/html/blog/2026-10-01.html | A particular new web attack or tool was not tied to a verified in-window presentation. |
| **DEF CON** | No qualifying in-window disclosure established. | Earlier conference work cannot be relabeled a September-November release merely because later coverage mentions it. |
| **DevCon** | No qualifying named web-security presentation established. | No supported technique-level inventory entry. |
| **KCon China** | Contemporary conference coverage was located, including https://juejin.cn/post/7704318835461242880 | No individual tool or attack was established with sufficient release-date and novelty detail for the confirmed inventory. |
| **Syscan** | No qualifying named presentation established. | No supported technique-level inventory entry. |
| **HackInBo** | No qualifying named presentation established. | No supported technique-level inventory entry. |
| **nullcon** | Berlin conference coverage was located: https://ismg.io/ai-security-takes-center-stage-at-nullcon-berlin-2026/ | Broad emphasis on AI security is not sufficient evidence of a specific novel tool or attack release. |
| **CTF innovations** | Intigriti's October challenge write-up is a concrete follow-up lead. | A new web vulnerability class or reusable exploit innovation was not established from that lead. |

The useful distinction is between an event taking place and a particular research artifact becoming public. The confirmed attack-research entries above rest on named technical findings rather than event branding. [9]

## Synthesis: Match The Innovation To The Security Boundary

The findings span different mechanisms, scopes, and evidence strengths. Comparing them as one undifferentiated list of "AI security tools" would obscure the decisions they support.

| Strategy / representative items | Mechanism | Scope | Principal trade-off or failure mode | Evidence and time horizon |
|---|---|---|---|---|
| **Exploratory protocol and browser research: HTTP Terminator, Scalable Vector Grief** | Discover parser, sanitizer, or browser-interpretation discrepancies | HTTP desynchronization and client-side content handling | Fixed test collections and apparently safe content can miss interpretation-dependent behavior | Dated research reporting; immediate regression-testing value. |
| **Broader assessment workflows: Reflectiz, Safeguard, Burp, PyRIT, F5** | Agentic exploration, contextual scanning, repeatable assessments, and integrated workflows | Websites, APIs, dependencies, AI systems, and tester workflows | More coverage, integration, or reporting does not automatically establish finding validity | Launches and release descriptions; evaluation should be workload-specific. [19] |
| **Verified remediation: Legit Security** | Generate dependency changes, rescan, and produce reviewable pull requests | Open-source dependency remediation | A generated change still requires evidence that it fixes the problem without unacceptable side effects | Dated commercial launch; near-term workflow impact. |
| **Runtime boundary controls: APISIX, Bay, AccuKnox integrations** | Enforce gateway behavior or interpose on proposed actions | API gateways, agent actions, and workloads | Availability choices, inspection order, and ordinary permissions can create unexpected exposure | Gateway change report and commercial announcements; configuration-dependent protection. [25][28] |
| **Adversarial and operational research: Microsoft sleeper agents, CERT-In advisories, 360 synthesis, PT digest** | Reveal model tampering or document real attack paths | Model integrity, financial APIs, agent operations, and vulnerability prioritization | Passing evaluations, valid credentials, or trusted infrastructure can provide misleading assurance | Mix of experimental research and operational reporting; different levels of causal specificity. [26][23] |

The non-obvious tension is that more automation can strengthen both assessment and attack execution. HTTP Terminator illustrates automated exploration, while the CERT-In account describes agentic offensive activity against live systems; Microsoft's sleeper-agent work shows why the agent itself can also become part of the attack surface. [26]

A second tension concerns availability versus enforcement. APISIX makes WAF fail-open behavior explicitly optional and defaults to fail-closed, while its decompression change improves inspection but introduces pre-authentication resource considerations. Security improves only when these controls are evaluated as a composed system. [25]

**Bottom line:** the best-supported priorities from this window are to test HTTP and content-interpretation boundaries, evaluate agent actions separately from model behavior, validate generated remediation, and exercise gateway outage and resource-limit paths. The inventory contains useful global findings, but the unresolved regional and repository leads prevent an honest claim of exhaustiveness.

## References

### Releases and technical research

- **PortSwigger, Burp Suite releases:** https://portswigger.net/burp/releases ; November desktop release: https://portswigger.net/burp/releases/professional-community-2026-11 [15]
- **PortSwigger, Scalable Vector Grief:** https://portswigger.net/research/scalable-vector-grief ; research feed: https://portswigger.net/research/rss [9]
- **Secarma, SVG sanitizer research analysis:** https://secarma.com/29-10-2026-svg-sanitiser-bypass-web-application-security
- **Dark Reading, HTTP Terminator:** https://www.darkreading.com/application-security/http-terminator-hunts-novel-desync-attacks [8]
- **Reflectiz launch announcement:** https://www.globenewswire.com/news-release/2026/09/08/3357826/0/en/reflectiz-launches-agentic-pentesting-for-websites-up-to-10x-coverage-vs-conventional-pentests.html
- **Microsoft, PyRIT development account:** https://commandline.microsoft.com/pyrit-python-risk-identification-tool-ai-red-teaming-subject-matter-experts
- **F5 AI Security release notes:** https://docs.aisecurity.f5.com/release-notes/2026-09-30-saas.html [19]
- **Safeguard release notes:** https://docs.safeguard.sh/docs/whats-new
- **Microsoft, sleeper-agent research:** https://www.microsoft.com/en-us/security/blog/2026/11/10/detecting-sleeper-agents-hiding-in-ai-model-neurons/ [5]
- **Apache APISIX, October report:** https://apisix.apache.org/blog/2026/10/31/2026-oct-monthly-report [25]
- **360 Netlab, AI Security Weekly 20260911:** https://blog.netlab.360.com/aian-quan-zhuan-ti-zhou-bao-5 [23]
- **ModSecurity technical reporting:** https://dailysecurityreview.com/resources/modsecurity-flaws-detailed-waf-upload-bypass-cve-2026-104269/

### Commercial and operational reporting

- **Legit Security agentic remediation launch:** https://hackread.com/legit-security-launches-agentic-remediation-for-open-source-dependency-vulnerabilities
- **Bay launch reporting:** https://siliconangle.com/2026/11/10/ai-security-startup-bay-launches-with-50m-to-vet-agent-actions-before-they-run/ [17]
- **Akamai, CERT-In advisory analysis:** https://www.akamai.com/blog/security/when-apis-meet-machine-speed-attacks-lessons-from-cert-in [26]
- **Positive Technologies, October trending-vulnerability digest:** https://ptsecurity.com/research/analytics/trending-vulnerability-digest-october-2026/ ; dated news listing: https://ptsecurity.com/about/news/
- **Ariovis-AccuKnox announcement:** https://accuknox.com/press-release/ariovis-accuknox-partnership [27]
- **DigitalXRAID-AccuKnox announcement:** https://accuknox.com/press-release/digitalxraid-uk-partners-with-accuknox [28]

Candidate, community, and conference URLs are listed directly in their respective tables; they are not represented as fully qualified releases.

## References

1. *Угрозы в сетевом трафике, или Что мы нашли в сети за 10 месяцев мониторинга / Habr*. https://habr.com/en/companies/pt/articles/1083780
2. *Исследования Positive Technologies*. https://ptsecurity.com/research/
3. *2026人工智能+大会安全论坛KCon「弈智」在京举行 聚焦AI时代安全治理|界面新闻*. https://www.jiemian.com/article/15287814.html
4. *议题公布！SDC2026 议程上线，解锁人机时代攻防新篇-安全资讯-看雪安全社区｜专业技术交流与安全研究论坛*. https://bbs.kanxue.com/thread-293070.htm
5. *Detecting sleeper agents hiding in AI model neurons | Microsoft Security Blog*. https://www.microsoft.com/en-us/security/blog/2026/11/10/detecting-sleeper-agents-hiding-in-ai-model-neurons/
6. *連続不正アクセス事案の攻撃手法に関する調査 - JPCERT/CC Eyes | JPCERTコーディネーションセンター公式ブログ*. https://blogs.jpcert.or.jp/ja/2026/10/web_api_attacks.html
7. *SVG Sanitiser Bypasses: What Web Application Teams Need to Know - Secarma: Penetration Testing and Cybersecurity Company*. https://secarma.com/29-10-2026-svg-sanitiser-bypass-web-application-security
8. *'HTTP Terminator' Hunts for Novel Desync Attacks*. https://www.darkreading.com/application-security/http-terminator-hunts-novel-desync-attacks
9. *portswigger.net*. https://portswigger.net/research/rss
10. *Recent AI-Assisted Cyber Attacks in Japan: Investigating Attack Infrastructure and Techniques - JPCERT/CC Eyes | JPCERT Coordination Center official Blog*. https://blogs.jpcert.or.jp/en/2026/10/web_api_attacks.html
11. *Новости*. https://ptsecurity.com/about/news/
12. *Legit Security launches agentic remediation for open-source dependency vulnerabilities*. https://hackread.com/legit-security-launches-agentic-remediation-for-open-source-dependency-vulnerabilities
13. *PyRIT: Democratizing AI red teaming through open-source tooling - Command Line*. https://commandline.microsoft.com/pyrit-python-risk-identification-tool-ai-red-teaming-subject-matter-experts
14. *Reflectiz Launches Agentic Pentesting for Websites: Up to*. https://www.globenewswire.com/news-release/2026/09/08/3357826/0/en/reflectiz-launches-agentic-pentesting-for-websites-up-to-10x-coverage-vs-conventional-pentests.html
15. *Burp Suite Release Notes*. https://portswigger.net/burp/releases
16. *What's new: November 2026 | Safeguard Docs*. https://docs.safeguard.sh/docs/whats-new
17. *AI security startup Bay launches with $50M to vet agent actions before they run - SiliconANGLE*. https://siliconangle.com/2026/11/10/ai-security-startup-bay-launches-with-50m-to-vet-agent-actions-before-they-run/
18. *ModSecurity Flaws Detailed: WAF Upload Bypass CVE-2026-104269 - Resources*. https://dailysecurityreview.com/resources/modsecurity-flaws-detailed-waf-upload-bypass-cve-2026-104269/
19. *F5 AI Security release notes | AI Security*. https://docs.aisecurity.f5.com/release-notes/2026-09-30-saas.html
20. *Security New Features in September 2026 - Alibaba Cloud Community*. http://www.alibabacloud.com/blog/security-new-features-in-september-2026_603638
21. *Scalable Vector Grief | PortSwigger Research*. https://portswigger.net/research/scalable-vector-grief
22. *AI安全专题周报（20260918）*. https://blog.netlab.360.com/aian-quan-zhuan-ti-zhou-bao-6
23. *AI安全专题周报（20260911）*. https://blog.netlab.360.com/aian-quan-zhuan-ti-zhou-bao-5
24. *Changelog - Astra Security*. https://astrasecurity.featurebase.app/changelog
25. *2026 Monthly Report (October 01 - October 31) | Apache APISIX*. https://apisix.apache.org/blog/2026/10/31/2026-oct-monthly-report
26. *When APIs Meet Machine-Speed Attacks: Lessons from CERT-In | Akamai*. https://www.akamai.com/blog/security/when-apis-meet-machine-speed-attacks-lessons-from-cert-in
27. *Ariovis Partners With AccuKnox To Bring Workload And Agentic AI Security To Western And Central Europe » Accuknox*. https://accuknox.com/press-release/ariovis-accuknox-partnership
28. *DigitalXRAID UK Partners With AccuKnox To Position Penetration Testing With AI And Cloud Security » Accuknox*. https://accuknox.com/press-release/digitalxraid-uk-partners-with-accuknox
