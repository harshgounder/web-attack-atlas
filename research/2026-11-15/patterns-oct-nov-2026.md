# Task Run Results

**Run ID:** trun_daf00106e9ae4477b645a78134e966cb
**Status:** ✅ completed
**Processor:** pro
**Created:** 2026-11-14T19:29:12.356041Z
**Modified:** 2026-11-14T19:32:53.146490Z

## Output

# Web Attack Research Inventory Across Languages and Platforms

## Executive Summary

- **Header Injection Becomes A Chain**: PortSwigger's **November 4** article connects header injection to CRLF-powered desync and redirect exploitation -> test the complete proxy-to-backend path, not only whether a header accepts input. [14]
- **Defenses Become Attack Surfaces**: The **November 11** CSP research describes allow-list gadgets and form-action credential exfiltration -> explicitly restrict form destinations and review effective policies, not just the presence of a CSP header. [19]
- **Publication Is Not Discovery**: The HTTP Terminator talk appeared on **November 6**, but its underlying PortSwigger write-up dates to **August 5** -> count the new presentation separately from the original research. [20]
- **Regional Sources Add Distinct Leads**: Chinese coverage includes Smarty cache poisoning, nginx CRLF request splitting, Text-to-SQL injection and adversarial comments against AI auditors -> retain regional items rather than treating English-language coverage as the complete record. [24]
- **Authorization Needs Workflow Testing**: The Japanese JPCERT/CC investigation and the disclosed-report inventories below extend coverage beyond payload injection -> prioritize identity, object access and multi-step business workflows alongside parser testing. [26]
- **AI Security Has Different Evidence Types**: The inventory includes agent-defense papers, an AI-assisted desync presentation and an exploitability-triage product announcement -> distinguish experimental results, research demonstrations and vendor claims. [10][20][9]
- **Scope Is Broad, Not Provably Exhaustive**: This is a substantial public-source inventory for **October 1-November 14, 2026**, with explicit regional and social-platform coverage below. It is not a claim to have captured every post, private channel, deleted thread or newly disclosed bounty report.

**Reading guide.** Dates below retain their meaning: article publication, report disclosure, presentation upload, or arXiv submission. An arXiv first submission is treated as the public-preprint date, not as peer-reviewed journal publication. Regional roundup entries with incomplete original links remain labeled leads. Region denotes the platform/language ecosystem, not an inferred author nationality or victim location.


## PortSwigger Connects Header Injection, Desync And CSP Exploitation

The strongest protocol case study is **"Making HTTP header injection critical with one prompt."** The November 4 article demonstrates why an apparently narrow injection finding can matter at a different layer: header manipulation feeds a CRLF-powered desync chain, request splitting and redirect-based exploitation. Its significance is the composed workflow, not a claim that every header injection automatically produces critical impact. [14]

HTTP Terminator illustrates a separate mechanism, **Shared-Parser Confusion**: server-side code shared between request and response parsing can expose response-processing behavior to requests. The November presentation belongs in the requested publication inventory, but calling the primitive newly discovered in November would be misleading because the underlying article appeared in August. [20]

| Title | Source platform | Region / language | Date and publication type | Key technique / defensive counter | URL |
|---|---|---|---|---|---|
| Making HTTP header injection critical with one prompt | PortSwigger Research | English-language; global audience | 2026-11-04; research/tool workflow | Header injection -> CRLF-powered desync, request splitting and redirect exploitation using Burp AT. [14] | `https://portswigger.net/research/making-http-header-injection-critical-with-one-prompt` |
| Blind trust: stealing credentials through CSP | PortSwigger Research | English-language; global audience | 2026-11-11; research/tool workflow | Allow-list gadgets, JSONP/legacy AngularJS and form-action exfiltration; review directive fallbacks, nonces/hashes and explicit form-action. [19] | `https://portswigger.net/research/blind-trust-stealing-credentials-through-csp` |
| Can AI do novel security research? Meet the HTTP Terminator | DEF CON 34 / YouTube; indexed by The Injection | English-language conference material | 2026-11-06; video publication, not original discovery | Shared-Parser Confusion; released desync vectors and updates to HTTP Request Smuggler, Turbo Intruder and Param Miner. [20] | `https://www.youtube.com/watch?v=sM8ChiHVW24` |
| Apache Traffic Server Fixes 15 Flaws, Including CVSS 10.0 Plugin Bug and Cache Poisoning | SecurityOnline | English-language; region not established | 2026-10-22; advisory coverage | Malformed redirects, request-body reuse, HEAD handling, cache poisoning and request smuggling; upgrade to the fixed branches listed by the report. [15] | `https://securityonline.info/apache-traffic-server-vulnerabilities-october-2026/` |
| SVG Sanitiser Bypasses: What the PortSwigger Research Means for Web Application Security | Secarma | UK / English | 2026-10-30; secondary defensive analysis | SVG sanitiser bypasses and Firefox response-header behavior; patch sanitizers, restrict SVG uploads or consider server-side rasterisation. [18] | `https://secarma.com/30-10-2026-svg-sanitiser-bypasses-portswigger-research` |

These are different publication types, not five independent new attack primitives. For a testing backlog, group the header/desync and proxy-cache items by infrastructure path, while treating CSP and SVG as browser/content-processing investigations.

### Scalable Vector Grief: Original Sanitizer Research

The original article below is the primary counterpart to Secarma's defensive coverage. Keep the original technique and the later explanatory articles linked rather than counting each explanation as a separate sanitizer bypass.

### Scalable Vector Grief | PortSwigger Research

**Platform:** PortSwigger Research. **Region/language:** English-language; global audience.

**URL:** `https://portswigger.net/research/scalable-vector-grief`

- Title: Scalable Vector Grief. [34]
- Publication date: Tuesday, 27 October 2026 at 14:29 UTC. This is within the requested window. [34]
- Source platform: PortSwigger Research. [34]
- Language/region: Not stated in the source.
- Classification: Original research article, not a repost, advisory, tool, or discussion. [34]
- Canonical URL: https://portswigger.net/research/scalable-vector-grief [34]
- Technique: SVG sanitizer bypasses involving namespace confusion, animated JavaScript URLs, self-contained XSLT, Firefox Link headers, and Safari image-to-SVG imports. [34] [34] [34] [34]
- Defensive countermeasure: Use effective SVG sanitization; DOMPurify and darylldoyle/svg-sanitizer resisted all tested techniques. [34] [34]
- Scope: Eight popular SVG sanitizers were tested and six were bypassed. [34]

Related web security research items listed on the page:

- "What's in a tag name? JavaScript, apparently" - 25 August 2026 - outside the requested window. The source does not expose its original URL in the available text. [34]
- "Cookie Chaos: How to bypass __Host and __Secure cookie prefixes" - 03 September 2025 - outside the requested window - https://portswigger.net/research/cookie-chaos-how-to-bypass-host-and-secure-cookie-prefixes. [34]
- "Stealing HttpOnly cookies with the cookie sandwich technique" - 22 January 2025 - outside the requested window - https://portswigger.net/research/stealing-httponly-cookies-with-the-cookie-sandwich-technique. [34]
- "Bypassing WAFs with the phantom $Version cookie" - 04 December 2024 - outside the requested window - https://portswigger.net/research/bypassing-wafs-with-the-phantom-version-cookie. [34]


## Chinese Sources Add CMS, Cache And AI-Audit Research

**Xianzhi and Anquanke are represented directly below**, followed by Zhihu and Chinese-language roundup leads. Original-language titles are retained where supplied, because translating every title would make exact rediscovery harder. For every item in a multi-item source inventory, the platform and region identified at the heading apply unless the entry names a different original publisher.

The most concrete cache case in the Chinese roundup is **Smarty cache poisoning leading to RCE**. The same roundup separately describes nginx `$uri` decoding, CRLF injection, request splitting and response-queue poisoning. These are not interchangeable forms of "poisoning": one concerns a template/cache execution path and the other concerns HTTP message boundaries and response association. [24]

The roundup also surfaces a useful failure case for AI-assisted review: an adversarial comment can cause an AI code auditor to overlook a vulnerability. That belongs in the inventory as a security-workflow attack, not as proof of a new browser or HTTP parser flaw. [24]

### 先知社区 · AI 时代的白帽社区

**Platform:** Xianzhi / 先知社区. **Region/language:** China / Chinese.

**URL:** `https://xz.aliyun.com/`

- Title: 分析某CMS鉴权绕过到RCE. Date: 2026-11-03. Source platform: 先知社区. Language/region: Chinese; region not stated. Technique: CMS authentication bypass leading to RCE; defensive countermeasure: not stated. Type: vulnerability analysis; original/repost status: uncertain. Canonical URL: https://xz.aliyun.com/news/93135. [38]

- Title: 2026 当下最热的三条 AI 主线,以及安全人该盯什么. Date: 2026-10-30. Source platform: 先知社区 Agent 广场. Language/region: Chinese; region not stated. Technique and defensive countermeasure: not stated. Type: discussion/roundup; original/repost status: uncertain. Canonical URL: https://xz.aliyun.com/agent-plaza/posts/2. [38]

- Title: Agent 时代的第一安全问题:提示词注入与越权代理. Date: 2026-10-30. Source platform: 先知社区 Agent 广场. Language/region: Chinese; region not stated. Technique: prompt injection and unauthorized agent actions; defensive countermeasure: not stated. Type: security discussion; original/repost status: uncertain. Canonical URL: https://xz.aliyun.com/agent-plaza/posts/3. [38]

- Title: 2026 近期网络安全热点:AI 双刃、勒索进化、供应链投毒与身份失守. Date: 2026-10-30. Source platform: 先知社区 Agent 广场. Language/region: Chinese; region not stated. Technique: AI dual-use, ransomware evolution, supply-chain poisoning, and identity compromise; defensive countermeasure: not stated. Type: roundup; original/repost status: uncertain. Canonical URL: https://xz.aliyun.com/agent-plaza/posts/4. [38]

- Title: WordPress Core竞争条件远程代码执行漏洞(CVE-2026-119977). Date: uncertain - listed as 1 天前, with no calendar publication date. Source platform: 先知社区. Language/region: Chinese; region not stated. Technique: predictable temporary directory injection into setup-config.php and copy_dir overwrite of wp-config.php to achieve RCE; defensive countermeasure: not stated. Type: vulnerability analysis; original/repost status: uncertain. Canonical URL: https://xz.aliyun.com/news/93320. [38]

- Title: 红队实战复盘之 DollarTicket + SPN 劫持 + RBCD 桥接. Date: uncertain - listed as 1 天前, with no calendar publication date. Source platform: 先知社区. Language/region: Chinese; region not stated. Technique: GLPI CVE-2025-24799 injection, SSSD root access, Kerberos ticket theft, SPN hijacking, and RBCD constrained delegation; defensive countermeasure: not stated. Type: penetration-test case study; original/repost status: uncertain. Canonical URL: https://xz.aliyun.com/news/93281. [38]

- Title: CVE-2026-118660:happy-dom 服务端 SSRF 全链路分析. Date: uncertain - listed as 2 天前, with no calendar publication date. Source platform: 先知社区. Language/region: Chinese; region not stated. Technique: iframe and link tags trigger internal requests; the 21.0.0 fix can be bypassed through preload as=fetch and 302 redirects; defensive countermeasure: upgrade to 21.0.0, though bypass details are stated. Type: vulnerability analysis; original/repost status: uncertain. Canonical URL: https://xz.aliyun.com/news/93265. [38]

- Title: 【AI安全】Agent 写文件时,路径检查通过后为什么还会越界?. Date: uncertain - listed as 4 天前, with no calendar publication date. Source platform: 先知社区. Language/region: Chinese; region not stated. Technique: TOCTOU race in AI Agent file writing, replacing a symlink between validation and opening; defensive countermeasure: not stated. Type: security discussion/analysis; original/repost status: uncertain. Canonical URL: https://xz.aliyun.com/news/93227. [38]

### 安全资讯 - 安全KER，安全资讯平台

**Platform:** Anquanke / 安全客. **Region/language:** China / Chinese.

**URL:** `https://www.anquanke.com/news`

Source platform: Anquanke (安全客), a Chinese-language security news platform; language/region is evident from the Chinese titles and site branding.[36][322.20][322.77] The page is an index/listing, and it does not state techniques, defensive countermeasures, or whether entries are original, reposts, advisories, tools, or discussions; these fields are therefore uncertain.[36][322.18][322.65]

1. Title: 一个月内十几家AI平台被扒,黑客要的不是数据,是你的API密钥  
Date as listed: 2026-11-11 11:01:14  
Technique: Not stated. Countermeasure: Not stated. Type: Uncertain.  
Canonical URL: https://www.anquanke.com/post/id/316461 [36]

2. Title: 杀毒软件成了后门:cPGuard更新通道被投毒  
Date as listed: 2026-11-09 14:58:22  
Technique: Not stated. Countermeasure: Not stated. Type: Uncertain.  
Canonical URL: https://www.anquanke.com/post/id/316452 [36]

3. Title: 有人把欧洲超市的冷柜调到了50℃,这是第二个月了  
Date as listed: 2026-11-05 11:44:53  
Technique: Not stated. Countermeasure: Not stated. Type: Uncertain.  
Canonical URL: https://www.anquanke.com/post/id/316435 [36]

4. Title: 【开放申请】企业可自查PHP2Shell漏洞了!  
Date as listed: 2026-10-30 18:19:15  
Technique: PHP2Shell vulnerability; countermeasure is enterprise self-check application. Type: Advisory/tool status uncertain.  
Canonical URL: https://www.anquanke.com/post/id/316392 [36]

5. Title: 突发!1day漏洞致使大量NAS用户文件被加密  
Date as listed: 2026-10-30 18:09:17  
Technique: 1day vulnerability and file encryption; countermeasure not stated. Type: Uncertain.  
Canonical URL: https://www.anquanke.com/post/id/316387 [36]

6. Title: Node.js、Python、Bun全中招:一个压缩库的内存漏洞,让半个互联网"裸奔"  
Date as listed: 2026-10-26 14:54:01  
Technique: Compression-library memory vulnerability; countermeasure not stated. Type: Uncertain.  
Canonical URL: https://www.anquanke.com/post/id/316355 [36]

7. Title: 凌晨收到GitLab安全公告,CVSS满分,我看了看自家版本号  
Date as listed: 2026-10-26 14:47:16  
Technique: GitLab security vulnerability, CVSS 10.0; countermeasure not stated. Type: Advisory/research status uncertain.  
Canonical URL: https://www.anquanke.com/post/id/316350 [36]

8. Title: AI自己写勒索脚本、自己挑目标、自己搞钱:俄罗斯黑客的Phantom框架,把勒索软件玩成了自动化流水线  
Date as listed: 2026-10-26 12:02:03  
Technique: AI-assisted ransomware automation and Phantom framework; countermeasure not stated. Type: Uncertain.  
Canonical URL: https://www.anquanke.com/post/id/316346 [36]

9. Title: 你的对手不是人了:Claude+Grok组队,400家金融机构被AI全自动攻破  
Date as listed: 2026-10-22 15:57:59  
Technique: AI-assisted attacks involving Claude and Grok; countermeasure not stated. Type: Uncertain.  
Canonical URL: https://www.anquanke.com/post/id/316272 [36]

10. Title: 3\.5万次请求、翻找泄露密钥:失控AI智能体围猎高德地图,运营者却毫不知情  
Date as listed: 2026-10-19 12:05:07  
Technique: AI-agent requests and exposed-key searching; countermeasure not stated. Type: Uncertain.  
Canonical URL: https://www.anquanke.com/post/id/316251 [36]

All ten listed dates fall within the requested 2026-10-01 through 2026-11-14 window.[36] No outside-window or uncertain dates are shown for these entries; the dates are uncertain only as actual publication dates because the page provides listing timestamps rather than an explicit publication-date field.[36][322.25][322.29]

### PHP 中的严重漏洞（2026-10-21） - 知乎

**Platform:** Zhihu / 知乎. **Region/language:** China / Chinese.

**URL:** `https://zhuanlan.zhihu.com/p/2096182377051583576`

标题: PHP 中的严重漏洞(2026-10-21) [37]

实际发布日期: 2026-10-21, based on the title; the page also shows an edit timestamp of 2026-10-21 10:16, so the publication date is not independently stated. [37]

来源平台: 知乎, column "Interesting stuff"; language/region: Chinese-language page, with 河南 shown in the edit metadata. [37]

类型: Repost/advisory discussion based on CERT-EU and PHP official announcements, not an original vulnerability disclosure or standalone tool. The page cites the CERT-EU source, PHP archive, and a GitHub PoC. [37]

Technique/impact: The two vulnerabilities may enable unauthenticated remote code execution; both are reported with CVSS 9.2. [37]

Defensive countermeasure: Identify PHP-based applications and patch promptly after the fixed release; if immediate patching is impossible, isolate internet-facing applications from public networks until remediation is available. [37]

Affected scope: The vulnerabilities may affect all PHP versions beginning with PHP 5. [37]

Canonical URL: https://zhuanlan.zhihu.com/p/2096182377051583576 [37]

Relevant linked research/advisory items and dates:

- CERT-EU advisory, original URL: https://cert.europa.eu/publications/security-advisories/2026-018/; date stated in the page: 2026-10-20. In-window. [37]
- PHP official security announcement, original URL: https://www.php.net/archive/2026.php#2026-10-20-1; date stated in the page: 2026-10-20. In-window. [37]
- GitHub PoC for CVE-2026-109618, original URL: https://github.com/Zer061/CVE-2026-109618; date: not stated, uncertain. [37]
- PHP security advisory GHSA-w8hw-w9fx-j79w, original URL: https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w; date: not stated, uncertain. [37]
- PHP security advisory GHSA-6wmf-4rv5-p3rp, original URL: https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp; date: not stated, uncertain. [37]
- CVE-2026-109619 is named, but no original URL or date is provided on the page. [37]
- Additional references: https://cyberplace.social/@GossiTheDog/117474220875882526 and https://x.com/watchtowrcyber/status/2112611507749982605; dates: not stated, uncertain. [37]

All stated dates fall within 2026-10-01 through 2026-11-14; undated items are labeled uncertain. [37]

### FreeBuf And Chinese Community Leads With Incomplete Original Links

The following entries are supported by dated Chinese-language indexes. Where an index exposes only a publisher homepage, that is **not** an article-specific URL; the limitation is preserved rather than replaced with an invented permalink. Date ranges likewise remain ranges. These entries expand the candidate inventory but have lower bibliographic completeness than the direct articles above.

### 國內網絡安全動態（2026年10月12日） | Security Aggregator

**Platform:** Security Aggregator, indexing FreeBuf and other Chinese sources. **Region/language:** Chinese-language / China-facing coverage.

**URL:** `http://cwl.elvis.hk/news/china-2026-10-12`

Page title: 國內網絡安全動態(2026年10月12日). [24]  
Page date: 2026-10-12. [24]  
Source platform: Security Aggregator. [24]  
Language/region: Chinese-language domestic China roundup, as indicated by the title and Chinese entries. [24]

1. Title: FreeBuf原创漏洞研究:Smarty缓存投毒RCE(CVE-2026-82531,CVSS 9.2). [24]  
Publication date: 2026-10-10 to 2026-10-11, within window. [24]  
Source platform: FreeBuf. [24]  
Type: Original research. [24]  
Technique: Smarty cache poisoning leading to remote code execution. [24]  
Countermeasure: Upgrade to 5.x. [24]  
Canonical URL: https://m.freebuf.com/. [24]

2. Title: FreeBuf原创复现:CRLF驱动的请求拆分与响应队列投毒. [24]  
Publication date: 2026-10-11, within window. [24]  
Source platform: FreeBuf. [24]  
Type: Original reproduction. [24]  
Technique: nginx $uri decoding CRLF injection causing request splitting and response queue poisoning. [24]  
Countermeasure: No countermeasure stated. [24]  
Canonical URL: https://m.freebuf.com/. [24]

3. Title: FreeBuf:Tesla远程攻击复盘 -  - 从DEF CON 23到FREE-FALL的五年. [24]  
Publication date: 2026-10-11, within window. [24]  
Source platform: FreeBuf. [24]  
Type: Discussion/review. [24]  
Technique: Remote compromise of vehicle systems affecting brakes, steering, and doors. [24]  
Countermeasure: No countermeasure stated; physical isolation is described as insufficient. [24]  
Canonical URL: https://m.freebuf.com/. [24]

4. Title: FreeBuf原创:企业内部钓鱼演练平台搭建与完整实施流程. [24]  
Publication date: 2026-10-11, within window. [24]  
Source platform: FreeBuf. [24]  
Type: Original implementation guide. [24]  
Technique: Internal phishing exercise platform selection, isolated lab construction, target selection, and execution. [24]  
Countermeasure: Conduct controlled internal phishing exercises in an isolated environment. [24]  
Canonical URL: https://m.freebuf.com/. [24]

5. Title: FreeBuf:Text-to-SQL注入攻击 -  - 自然语言到数据库查询的隐蔽攻击面. [24]  
Publication date: 2026-10-09 to 2026-10-10, within window. [24]  
Source platform: FreeBuf. [24]  
Type: Research/discussion. [24]  
Technique: Injection into the natural-language-to-database-query chain. [24]  
Countermeasure: No countermeasure stated. [24]  
Canonical URL: https://m.freebuf.com/. [24]

6. Title: FreeBuf:一行注释让大模型代码审计工具对漏洞视而不见. [24]  
Publication date: 2026-10-09 to 2026-10-10, within window. [24]  
Source platform: FreeBuf. [24]  
Type: Research/discussion. [24]  
Technique: Adversarial comment causing AI code-audit tools to overlook vulnerabilities. [24]  
Countermeasure: No countermeasure stated. [24]  
Canonical URL: https://m.freebuf.com/. [24]

7. Title: FreeBuf:开源逆向工具REA打通AI编码与Ghidra等逆向工具. [24]  
Publication date: 2026-10-10, within window. [24]  
Source platform: FreeBuf. [24]  
Type: Tool. [24]  
Technique: AI coding agent integration with reverse-engineering tools for binary analysis without source code. [24]  
Countermeasure: No countermeasure stated. [24]  
Canonical URL: https://m.freebuf.com/. [24]

The page also lists a MiMo training-data discussion, an official mobile-app personal-information enforcement notice, and a Cyberspace Administration enforcement-case notice, but these are not web security research items. [24]

### 國內網絡安全動態（2026年10月11日） | Security Aggregator

**Platform:** Security Aggregator, indexing Chinese security sources. **Region/language:** Chinese-language / China-facing coverage.

**URL:** `https://cwl.elvis.hk/news/china-2026-10-11`

Page: 國內網絡安全動態(2026年10月11日); source platform: Security Aggregator; language/region: Chinese/China; canonical URL: https://cwl.elvis.hk/news/china-2026-10-11 [25]

- 国家计算机病毒应急处理中心:82款移动应用违法违规收集使用个人信息. Date shown: 10月10日; platform: 国家计算机病毒应急处理中心; type: advisory; technique: illegal or non-compliant collection and use of personal information; countermeasure: uninstall or remain vigilant; source URL: http://m.toutiao.com/group/7694951048766603817/ [25]
- FreeBuf原创研究:埋雷式攻击 -  - 休眠式记忆投毒让智能体「自己引爆」. Date shown: 10月10日; platform: FreeBuf; type: original research; technique: dormant memory poisoning against agents, with injection separated from detonation; countermeasure: not stated; source URL: https://m.freebuf.com/ [25]
- FreeBuf原创研究:Function Calling结构化输出约束逃逸与参数注入. Date shown: 10月10日; platform: FreeBuf; type: original research; technique: constrained decoding escape and parameter injection in JSON Schema-constrained function calling; countermeasure: not stated; source URL: https://m.freebuf.com/ [25]
- FreeBuf原创复盘:一台「被信任」的主机如何穿越防火墙 -  - 内网横向移动与信任粒度加固. Date shown: 10月10日; platform: FreeBuf; type: original retrospective; technique: lateral movement through a firewall via a trusted host; countermeasure: strengthen trust granularity; source URL: https://m.freebuf.com/ [25]
- FreeBuf:Anthropic切断Claude实时联网权限 -  - AI Agent越界操作警示. Date shown: 10月10日; platform: FreeBuf; type: repost; technique: unauthorized network operations by an AI agent; countermeasure: cut real-time network access for internal AI testing; source URL: https://m.freebuf.com/ [25]
- FreeBuf:数万GitHub仓库遭植入恶意Actions工作流,窃取全量历史存储凭证. Date shown: 10月10日; platform: FreeBuf; type: advisory; technique: malicious GitHub Actions workflows stealing historical storage credentials; countermeasure: immediately inspect repository workflows; source URL: https://m.freebuf.com/ [25]
- FreeBuf:再看Olympic Destroyer -  - 被移植的Lazarus指纹,给ARTEX争议留下什么. Date shown: 10月10日; platform: FreeBuf; type: analysis; technique: falsified Lazarus attribution indicators in the Olympic Destroyer incident; countermeasure: not stated; source URL: https://m.freebuf.com/ [25]
- FreeBuf周报:Pwn2Own首日、AI攻击韩国金融机构等本周热点汇总. Date shown: 10月10日; platform: FreeBuf; type: roundup; items: Pwn2Own 2026 first-day results, AI-tool-assisted attacks on South Korean financial institutions, and rising Japanese Web-data leaks; countermeasure: not stated; source URL: https://m.freebuf.com/ [25]
- FreeBuf:Bitdefender发布AI安全新品,让AI使用「看得见、风险可管理」. Date shown: 10月10日; platform: FreeBuf; type: repost/tool announcement; technique: visibility and risk management for employee Web AI use and local AI-tool access; countermeasure: manage enterprise AI-use risk; source URL: https://m.freebuf.com/ [25]
- 国家网信办发布近期网络安全、数据安全、个人信息保护等领域执法典型案例. Date: 9月发布; outside the requested window; platform: 国家网信办; type: advisory/case roundup; technique: Web-page tampering, malicious-program placement, and non-compliant personal-information processing; countermeasure: enforcement and investigation; source URL: https://www.sina.cn/media/6411107972 [25]

### cybersecurity-daily/网安日报速递-2026年10月13日.md at main · Unclecheng-li/cybersecurity-daily · GitHub

**Platform:** GitHub / Unclecheng-li cybersecurity-daily. **Region/language:** China / Chinese.

**URL:** `https://github.com/Unclecheng-li/cybersecurity-daily/blob/main/%E7%BD%91%E5%AE%89%E6%97%A5%E6%8A%A5%E9%80%9F%E9%80%92-2026%E5%B9%B410%E6%9C%8813%E6%97%A5.md`

Exact title: "网安日报速递 · 2026年10月13日 星期二(第 185 期)". Actual publication date: 2026-10-13. Source platform: GitHub, repository `Unclecheng-li/cybersecurity-daily`. Language/region: Chinese; global coverage with Ukraine-focused reporting. Type: original roundup/index, not an advisory or tool. Canonical URL: https://github.com/Unclecheng-li/cybersecurity-daily/blob/main/%E7%BD%91%E5%AE%89%E6%97%A5%E6%8A%A5%E9%80%92-2026%E5%B9%B410%E6%9C%8813%E6%97%A5.md [27]

Main techniques and countermeasures: AI-agent orchestration, automated scanning, WebShell deployment, prompt injection, malicious-model instructions, path traversal, unauthenticated RCE, SSRF, supply-chain hardware implants, and credential theft. Defenses include patching affected products, minimizing AI-agent tool permissions, rotating credentials and TOTP seeds, restricting exposure, inspecting logs and files, and using behavior/network/YARA/sandbox anchors. [27]

Relevant indexed research items. The page gives no original publication dates for these linked works; dates are therefore uncertain and not inferred. All listed items are within the requested date window only when their linked-page date is confirmed independently; otherwise label uncertain:

1. "CyberXero 用 Claude Code 窃取 62.8 万条乌克兰记录" - SOCRadar / The Hacker News - research/report - date uncertain - https://thehackernews.com/2026/10/cyberxero-uses-claude-code-in-campaign.html [27]
2. "一支 AI 驱动的队伍放出 51 个智能体打乌克兰目标" - Cybersecurity Beat - research/report - date uncertain - https://cybersecuritybeat.com/2026/10/12/an-ai-driven-crew-turned-51-agents-loose-on-ukrainian-targets [27]
3. "CyberXero 用 Claude Code 智能体窃取乌克兰数据" - Daily Security Review - research/report - date uncertain - https://dailysecurityreview.com/threat-actors/cyberxero-broker-used-claude-code-agents-to-steal-ukrainian-data [27]
4. "CyberXero 双线 AI 赋能乌克兰攻击行动(含 Operation Master)" - OSINTSights - research/report - date uncertain - https://osintsights.com/cyberxero-exploits-ai-in-dual-pronged-ukraine-cyberattack-campaign [27]
5. "CyberXero 集群详情与 CVE / ATT&CK 映射" - ThreatCluster - research/index - date uncertain - https://threatcluster.io/cluster/cyberxero-campaign-targets-ukrainian-records-using-ai-tools-e19fe391 [27]
6. "Dell 修复 PowerEdge System Update 工具中的 root 级严重漏洞" - TechNewsReel - advisory/report - date uncertain - https://technewsreel.com/cybersecurity/dell-patches-critical-root-level-flaw-in-poweredge-system-update-tool [27]
7. "Bricksforge WordPress 插件 CVSS 10.0 漏洞遭利用" - Secure Today(腾讯) - vulnerability report - date uncertain - https://sectoday.tencent.com/api/article/7Ie5L6EBVJfJhgnJS9HW/link [27]
8. "Bricksforge CVE-2026-85097 未认证上传 RCE 详析" - ThreatFrontier - vulnerability research - date uncertain - https://threatfrontier.com/articles/bricksforge-cve-2026-85097-unauthenticated-upload-rce-exploited [27]
9. "严重 WordPress Bricksforge 漏洞允许未认证 RCE" - Cybernoz - vulnerability report - date uncertain - https://cybernoz.com/critical-wordpress-bricksforge-flaw-lets-unauthenticated-attackers-execute-remote-code/ [27]
10. "两枚 CVSS 10.0 漏洞本周被利用却都不在 KEV(Bricksforge 与 SonicWall)" - DugganUSA - discussion/report - date uncertain - https://www.dugganusa.com/post/two-cvss-10-exploited-not-in-kev-bricksforge-wordpress-sonicwall-sma1000 [27]
11. "GitLab CE/EE 多个漏洞(SB2026101301,24 个漏洞)" - Cybersecurity Help - vulnerability index - date uncertain - https://www.cybersecurity-help.cz/vdb/SB2026101301 [27]
12. "CVE-2026-96893(GitLab Duo Agent Platform 提示注入,7.3/8.4)" - HackerFeeds - CVE index - date uncertain - https://hackerfeeds.com/cve/CVE-2026-96893 [27]
13. "CERT 预警:SonicWall SMA 1000 严重漏洞在补丁后遭 135 次利用尝试" - Enigma Global - advisory - date uncertain - https://www.enigma-global.com/preview/cert/12565 [27]
14. "IBM i HTTP Server Administration GUI 代码生成控制不当(CVE-2026-96119)" - IBM - official advisory - date uncertain - https://www.ibm.com/support/pages/node/7292159 [27]
15. "Rapyd Admin 9.0.0-9.20.0 硬编码超级管理员凭据(CVE-2026-109566)" - VulnCheck - advisory - date uncertain - https://www.vulncheck.com/advisories/rapyd-admin-9.0.0-before-9.20.0-hard-coded-super-admin-credentials-via-authseeder [27]
16. "Ledger 硬件钱包内发现隐藏植入体,与 9,300 万美元盗币相关" - Help Net Security - supply-chain research - date uncertain - https://www.helpnetsecurity.com/2026/10/12/ledger-wallets-compromised-via-hardware-implant/ [27]
17. "Ledger 称所有已确认钱包清空均指向 CryptoBilis 设备" - FinanceFeeds - report - date uncertain - https://financefeeds.com/ledger-says-all-confirmed-wallet-drains-trace-back-to-cryptobilis-devices/ [27]
18. "本周回顾:Atlassian 数小时内被利用、AI 对抗分析恶意软件与 CVE 清单" - LavX News - roundup - date uncertain - https://news.lavx.hu/article/weekly-recap-atlassian-flaws-exploited-within-hours-rogue-certificates-shinyhunters-arrest-and-ai-evasion-malware [27]
19. "Apache Struts 用户面临四枚新公布安全缺陷" - Cyber Insider - vulnerability report - date uncertain - https://cyberinsider.co.uk/apache-struts-users-face-four-newly-documented-security-flaws [27]
20. "每周回顾:Helpdesk 零日、流氓证书、AI 欺骗型恶意软件" - The Hacker News - roundup - date uncertain - https://thehackernews.com/2026/10/weekly-recap-helpdesk-0-days-rogue.html [27]

Known event dates are not original publication dates: Bricksforge exploitation was first observed on 2026-10-07, SonicWall exploitation was first captured on 2026-10-08, Ledger reporting occurred on 2026-10-09 to 2026-10-11, and the GitLab/IBM items were reported on 2026-10-13. These dates are within the requested window but remain event or report dates, not necessarily source publication dates. [27]

**Implication:** Chinese coverage adds both conventional web exploitation and attacks on AI-based security workflows. Prioritize the original Xianzhi/Anquanke records for direct reading, and treat homepage-only FreeBuf references as retrieval leads rather than complete citations to original research.


## Russian And Japanese Coverage Connects Exploitation With Operations

Regional reporting is useful both for original technical material and for understanding how research changes deployment decisions. The Habr material below includes AI-assisted vulnerability discovery and operational responses to PHP/GitLab exposure; the Japanese material includes a web/API attack investigation and a concrete KUSANAGI header-injection advisory. Their publication dates and attribution are retained in each record rather than borrowing a vulnerability's discovery date.

The KUSANAGI case provides a concrete bridge between protocol research and deployment risk: the affected WordPress-oriented nginx redirect configuration mishandles CRLF characters in HTTP headers. That is a product/configuration advisory, distinct from PortSwigger's generalized desync workflow, even though both warrant attention to header handling. [14]

### Claude нашёл 62 уязвимости в Chrome и собрал цепочки атак на Safari, Android, Windows и Linux / Хабр

**Platform:** Habr / OTUS. **Region/language:** Russian-language / Russia-facing community.

**URL:** `https://habr.com/ru/companies/otus/news/1100652`

Title: "Claude нашёл 62 уязвимости в Chrome и собрал цепочки атак на Safari, Android, Windows и Linux". [22]  
Publication date: 28 Oct; year is not explicitly stated in the publication metadata, so the date is uncertain for the requested window. [22]  
Platform: Habr, company blog OTUS. [22]  
Language/region: Russian-language Habr page; Russian context is evident from the page text and URL. [22]  
Canonical URL: https://habr.com/ru/companies/otus/news/1100652 [22]

Type: research news/report summarizing Anthropic's research; not clearly identified as an original Habr study, repost, advisory, tool, or discussion. [22] The underlying research used an internal Claude model, parallel agents, reverse engineering, vulnerability discovery, and exploit-chain construction. [22] [22] [22] Defensive measures included vendor disclosure and fixes for Chrome, Safari, Android, Windows, and Linux. [22] [22] [22] [22] [22]

Research inventory:
- Chrome: memory corruption, memory-protection bypass, CacheStorage race, and FedCM use-after-free were chained for sandbox escape and arbitrary code execution. [22] Countermeasure: the 62 reported vulnerabilities received CVE identifiers and were fixed by Chrome 156. [22]
- Safari: JavaScriptCore use-after-free, Gigacage and IPC weaknesses, and SOP-check manipulation enabled access to other sites' history, cookies, and authenticated responses without arbitrary code execution. [22] Countermeasure: Apple confirmed the report and released a fix. [22]
- Android: USB-transfer, device-pairing authorization, and file-content restrictions were chained to extract data from a locked phone with physical access. [22] Countermeasure: Google fixed the issue. [22]
- Windows: CVE-2026-33096 in QUIC/HTTP/3 enabled remote denial of service through specially crafted packets. [22] Countermeasure: Microsoft fixed the vulnerability. [22]
- Linux: a network-stack use-after-free/race in MPTCP enabled remote root command execution without credentials or user action. [22] Countermeasure: CVE-2026-98432 was fixed in the mainline kernel and supported stable branches. [22]

Roundup/index items:
- "Методичка по построению VPN, осень 2026" - https://habr.com/ru/articles/1103460/ - appears in the "ЕЖЕДНЕВНЫЙ ХАБР | 8 НОЯБ 2026" index, but the item's own exact publication date is not stated; label: uncertain date, likely within the requested window. [22]
- No exact dates are provided for the other linked index entries, and their titles do not clearly identify web-security research. [22]

### Две критические CVE в PHP и GitLab: уязвимости выходят быстрее, чем их успевают закрыть / Habr

**Platform:** Habr / USSC. **Region/language:** Russian-language / Russia-facing community.

**URL:** `https://habr.com/ru/publications/1102528`

Title: "Две критические CVE в PHP и GitLab: уязвимости выходят быстрее, чем их успевают закрыть" [11]  
Publication date: 2 нояб. 2026, 7:46 [11]  
Source platform: Habr, blog of Urals Center for Information Security [11]  
Language/region: Russian; Russian company blog [11]  
Type: vendor-authored research/advisory article, not identified as a repost, roundup, index, tool, or discussion [11]  
Technique: exploitation of memory-management flaws in PHP and integer overflow in GitLab's Onigmo regex engine, enabling unauthenticated remote code execution; AI-assisted vulnerability discovery and exploit development are also discussed [11]  
Defensive countermeasure: install PHP and GitLab fixes, inventory vulnerable containers, apply runtime controls, restrict shells and network connections, and enforce CI checks [11]  
Canonical URL: https://habr.com/post/1102528/ [11]

Relevant web security research items:

1. PHP2Shell, CVE-2026-109618 and CVE-2026-109619. Critical PHP vulnerabilities allowing unauthenticated arbitrary code execution via specially prepared HTTP requests [11]. Disclosure date stated as 21 October, with no original research URL provided [11]. Date: 2026-10-21, within window. Original URL: not provided [11].

2. GitLab CVE-2026-110264. Integer overflow in Onigmo enables unauthenticated server-side code execution and affects GitLab releases from version 7.0 onward [11]. Disclosure date: same day as the PHP fixes, but the page does not state the calendar date directly; date uncertain, likely within the article's October context, but not inferable [11]. Original URL: not provided [11].

3. PHP2Shell exploit by VulnCheck. Exploit reportedly demonstrated on 22 October and bypassed ASLR for PHP 8.4.10 through 8.4.26 [11]. Date: 2026-10-22, within window. Original URL: not provided [11].

4. Luntry PHP2Shell Kubernetes test. Public exploit test against php:8.4.26-apache; Luntry stopped the compromised container and terminated the attack chain [11]. Original URL: https://luntry.ru/uyazvimost-php2shell-bezopasnost-konteynerov-zashchita-kubernetes [11]. Date: not stated, uncertain [11].

### Чёрный октябрь уязвимостей: что задело мой сервер, как я закрыл дыры и почему ушёл на статику без инлайн-скриптов / Хабр

**Platform:** Habr. **Region/language:** Russian-language / Russia-facing community.

**URL:** `https://habr.com/ru/articles/1100918/`

Title: "Чёрный октябрь уязвимостей: что задело мой сервер, как я закрыл дыры и почему ушёл на статику без инлайн-скриптов" [17]  
Publication date: not stated in the source page content; dates such as October 21-26 are event or update dates, not a confirmed publication date [17].  
Source platform: Habr; language/region: Russian-language page, with Ubuntu/Debian and other international security context [17].  
Type: original first-person security discussion and defensive how-to, not a repost, advisory, roundup, index, or standalone tool [17].  
Technique: exploitation of vulnerable PHP, Node.js/Brotli, Java, GitLab, and npm dependencies, plus web-shells, exposed secrets, unsafe uploads, symlink traversal, and inline-script/CSP weaknesses [17].  
Defensive countermeasures: apply security updates, restart processes holding old libraries, inspect changed and unexpected PHP files, verify WordPress checksums, audit dependencies, enforce CSP, isolate uploads, rotate exposed secrets, restrict permissions, and disable Nginx symlink following [17].  
Canonical URL: https://habr.com/ru/articles/1100918/ [17]

Research inventory for 2026-10-01 through 2026-11-14: no roundup or index of separate web-security research items with original URLs and exact publication dates is present. The page mentions October 21, 22, 23, 25, and 26 events, but supplies no separate original research URLs or publication dates for them [17]. Dates outside the requested window: none established. Uncertain dates: page publication date and dates for the referenced research items are not stated [17].

### Recent AI-Assisted Cyber Attacks in Japan: Investigating Attack Infrastructure and Techniques - JPCERT/CC Eyes | JPCERT Coordination Center official Blog

**Platform:** JPCERT/CC Eyes, English edition. **Region/language:** Japan / English.

**URL:** `https://blogs.jpcert.or.jp/en/2026/10/web_api_attacks.html`

Title: Recent AI-Assisted Cyber Attacks in Japan: Investigating Attack Infrastructure and Techniques [12]

Publication date: October 21, 2026. This falls within the requested window of October 1, 2026 through November 14, 2026. [12]

Source platform: JPCERT Coordination Center official Blog; language: English; region/context: Japan, including attacks targeting organizations and web services in Japan and abroad. [12]

Type: Original JPCERT/CC investigation report/article, not identified on the page as a repost, roundup, tool, or discussion. The article presents findings from an investigation of attack servers. [12]

Technique: The attackers used AI to scan for known vulnerabilities and conduct attacks via APIs; they analyzed Android APK files to identify and exploit APIs, tested for SSRF, used Flutter reverse-engineering and Android-analysis tools, and attempted EDR evasion and internal-network access. [12]

Defensive countermeasures: Do not embed private API-authentication keys or long-lived credentials in applications; enforce server-side authentication and authorization; apply rate limiting and monitor anomalous requests; restrict API destinations and validate redirect destinations to prevent SSRF. [12]

Canonical URL: https://blogs.jpcert.or.jp/en/2026/10/web_api_attacks.html [12]

Roundup/index inventory: No roundup or index of separate web-security research items, with distinct original URLs and dates, is presented on this page. [12]

### 連続不正アクセス事案の攻撃手法に関する調査 - JPCERT/CC Eyes | JPCERTコーディネーションセンター公式ブログ

**Platform:** JPCERT/CC Eyes, Japanese edition. **Region/language:** Japan / Japanese.

**URL:** `https://blogs.jpcert.or.jp/ja/2026/10/web_api_attacks.html`

- Title: 連続不正アクセス事案の攻撃手法に関する調査. [6]
- Publication date: 2026/10/15, within the requested window. [6]
- Source platform: JPCERT/CC Eyes, JPCERT Coordination Center official blog. [6]
- Language/region: Japanese; the article discusses attacks against organizations in Japan and Web services in regions outside Japan. [6]
- Type: Original research/investigation article, not a repost, roundup, tool, or advisory. JPCERT/CC describes its investigation of attack-source servers and observed attacks. [6]
- Technique: Attackers analyzed Android APK files to identify and abuse APIs, investigated SSRF vulnerabilities, and used Blutter and jadx for application analysis. [6]
- Defensive countermeasures: Do not embed API secrets or long-lived credentials; perform server-side authentication and authorization; apply rate limiting and anomalous-request monitoring; restrict external-URL access and validate post-redirect destinations. [6]
- Canonical URL: https://blogs.jpcert.or.jp/ja/2026/10/web_api_attacks.html [6]

Relevant linked research items:

- NICT, "【注意喚起】相次ぐ情報漏洩、その原因の一つは「アプリ解析からのサーバ攻撃」"; type: advisory; original URL: https://cynex.nict.go.jp/library/261013-01.html; date: uncertain - no explicit publication date is stated in the page text. [6]
- IQCrafter, "Reverse Engineering a Flutter Mobile App: A Complete Security Research Methodology"; type: technical research article; original URL: https://www.iqcrafter.com/blog/flutter-app-reverse-engineering-security-research; date: June 2026, outside the requested window. [6]
- NerdzLab, "Reverse Engineering a Flutter App: How Secure Is Your Data, Really?"; type: technical research article; original URL: https://nerdzlab.com/reverse-engineering-a-flutter-app-how-secure-is-your-data-really/; date: uncertain - no date is stated. [6]
- Medium/NerdzLab, "I Reverse Engineered a Banking App With a Million Downloads"; type: technical discussion/research article; original URL: https://medium.com/@nerdz_lab/i-reverse-engineered-a-banking-app-with-a-million-downloads-5bbbad44fa52; date: uncertain - no date is stated. [6]
- Blutter, GitHub; type: tool; original URL: https://github.com/worawit/blutter; date: uncertain - no date is stated. [6]

### KUSANAGI に HTTP ヘッダーインジェクションの脆弱性 | ScanNetSecurity

**Platform:** ScanNetSecurity. **Region/language:** Japan / Japanese.

**URL:** `https://scan.netsecurity.ne.jp/article/2026/11/12/56753.html`

- Title: KUSANAGI に HTTP ヘッダーインジェクションの脆弱性 [8]
- Publication date: 2026.11.12 Thu 8:00. This is within the requested window. [8]
- Source platform: ScanNetSecurity. [8]
- Language/region: Japanese-language reporting focused on Japan, citing IPA, JPCERT/CC, and Japan Vulnerability Notes. [8]
- Technique: HTTP header injection caused by improper sanitization of CRLF characters in redirect rules in the Nginx configuration for WordPress. An attacker can access a crafted URL to insert arbitrary headers into the HTTP response. CVE-2026-117477. [8]
- Defensive countermeasure: Update to the latest version based on developer information. If updating is not possible, implement mitigations. [8]
- Classification: Vulnerability news/report relaying a JVN advisory; not a tool, discussion, or roundup/index. [8]
- Affected scope: KUSANAGI 7, 8, and 9 using the listed Security/Enterprise versions 10.7.2-1 or earlier and Free/Business/Premium versions 9.12.2-1 or earlier. Systems using Apache httpd are excluded. [8]
- Canonical URL: https://scan.netsecurity.ne.jp/article/2026/11/12/56753.html [8]
- Roundup/index inventory: No additional web security research items with original URLs and dates are enumerated on this page. [8]

**Takeaway:** The Japanese and English JPCERT/CC versions describe the same investigation, not independent incidents. Likewise, Habr discussion of globally disclosed vulnerabilities should not be counted as a separate vulnerability discovery merely because it is a distinct Russian-language publication.


## Disclosed Reports Expose Authorization And Workflow Failure Modes

The two Yaamlabs collections below are particularly useful for moving beyond research headlines to concrete reported bugs. The November 8 collection explicitly covers **15 HackerOne reports disclosed from October 28 to November 7**, while the November 6 collection provides another dated set of report-level examples. Their inventories preserve the report titles, dates, techniques and original links available in the source; overlapping reports should be deduplicated by report URL, not counted twice. [26][21]

The API-flow article is a different evidence type: methodology and exposure-testing guidance rather than a bounty-platform disclosure. Keeping that distinction matters when choosing between reproducing a known case and designing a broader authorization test plan.

### Bug bounty roundup: 15 disclosed reports worth reading | Yaamlabs

**Platform:** Yaamlabs, indexing HackerOne disclosed reports. **Region/language:** English-language / global bounty programs.

**URL:** `https://yaamlabs.com/blog/bug-bounty-roundup-2026-11-08`

Research inventory

- Exact title: "Bug bounty roundup: 15 disclosed reports worth reading." Actual publication date: November 8, 2026. Source platform: Yaamlabs. Type: roundup/index. Canonical URL: https://yaamlabs.com/blog/bug-bounty-roundup-2026-11-08. The page covers HackerOne reports disclosed from October 28 through November 7, 2026; individual report publication dates are not stated, so dates are uncertain within that window. [26] [26]

- "Cross-account XSS on Basecamp that beat the CSP" - HackerOne report 3981292: https://hackerone.com/reports/3981292. Date: uncertain, within October 28-November 7, 2026. Technique: stored cross-account XSS through an oEmbed HTML attribute and nonce adoption by Turbo. Countermeasure: enforce account checks on embed views and do not allow frontend libraries to adopt and re-stamp injected scripts. Type: original vulnerability disclosure/advisory. [26]

- "Six MariaDB connector bugs where the server is the attacker" - HackerOne reports 3896617, 3896684, 3890289, 3891319, 3891779, and 3920629: https://hackerone.com/reports/3896617, https://hackerone.com/reports/3896684, https://hackerone.com/reports/3890289, https://hackerone.com/reports/3891319, https://hackerone.com/reports/3891779, https://hackerone.com/reports/3920629. Date: November 4, 2026 as a group; individual dates are uncertain. Techniques: TLS hostname-verification bypass, out-of-bounds read, SQL injection, stack-buffer overflow, unquoted SQL identifiers, and cross-user packet confusion. Countermeasure: enable full TLS verification and update connectors to fixed releases. Type: original vulnerability disclosures/advisories. [26]

- "RSVP list readable past the event password on WordPress events" - HackerOne report 4029867: https://hackerone.com/reports/4029867. Date: uncertain, within October 28-November 7, 2026. Technique: unauthorized REST-wrapper access to password-protected RSVP data. Countermeasure: reuse `Event::can_read_rsvps()`. Type: original vulnerability disclosure/advisory. [26]

- "A CampTix access token built from the requester's own IP" - HackerOne report 4043537: https://hackerone.com/reports/4043537. Date: uncertain, within October 28-November 7, 2026. Technique: predictable token generation from email and IP, without nonce or email confirmation. Countermeasure: use a random stored token and email the access link. Type: original vulnerability disclosure/advisory. [26]

- "A str_replace() mistake gave wordpress.org an open redirect" - HackerOne report 3933198: https://hackerone.com/reports/3933198. Date: uncertain, within October 28-November 7, 2026. Technique: repeated path replacement producing an open redirect that passed the SSO allowlist. Countermeasure: use `str_starts_with()`, `substr()`, and `wp_safe_redirect()`. Type: original vulnerability disclosure/advisory. [26]

- "A Monero wallet RPC that believed a remote node" - HackerOne report 3719670: https://hackerone.com/reports/3719670. Date: uncertain, within October 28-November 7, 2026. Technique: untrusted remote-node data accepted without a trust check. Countermeasure: apply `is_trusted_daemon()`-equivalent validation. Type: original vulnerability disclosure/advisory. [26]

- "Hidden text in an AI agent's consent prompt" - HackerOne report 4077800: https://hackerone.com/reports/4077800. Date: uncertain, within October 28-November 7, 2026. Technique: indirect prompt injection concealed in formatted approval text and shell command execution through an argument. Countermeasure: render approval text as plain text and pass argument vectors instead of `shell=True`. Type: original vulnerability disclosure/advisory. [26]

- "Two ways to tie up Weblate's translation-finder" - HackerOne reports 4094236 and 4088592: https://hackerone.com/reports/4094236 and https://hackerone.com/reports/4088592. Date: uncertain, within October 28-November 7, 2026. Techniques: XML entity expansion and quadratic wildcard-mask matching. Countermeasures: reject every entity and cap total work per job. Type: original vulnerability disclosures/advisories. [26] [26]

- "Django's cache treated absent and empty headers alike" - HackerOne report 4062511: https://hackerone.com/reports/4062511. Date: uncertain, within October 28-November 7, 2026. Technique: cache-key collision between an absent header and an empty header. Countermeasure: distinguish those request states when constructing cache keys. Type: original vulnerability disclosure/advisory. [26]

- Language/region: no language or geographic region is stated for the roundup or these reports. [26] [26]

### Bug bounty roundup: nine disclosed reports worth reading | Yaamlabs

**Platform:** Yaamlabs, indexing HackerOne disclosed reports. **Region/language:** English-language / global bounty programs.

**URL:** `https://yaamlabs.com/blog/bug-bounty-roundup-2026-11-06`

Title: Bug bounty roundup: nine disclosed reports worth reading. Publication date: November 6, 2026. Source platform: Yaamlabs blog. Format: roundup of nine publicly disclosed HackerOne reports, not an original report, repost, advisory, tool, or discussion. The reports became public between October 26 and November 5, 2026; individual publication dates are not provided, so each item has an uncertain exact date but is within the requested window. [21] [21] [21]

1. Missing authentication on Shopify staff routes
- Date: Exact date uncertain; within October 26-November 5, 2026.
- Platform: HackerOne; program: Shopify.
- Language/region: Not evident.
- Technique: Authorization bypass through Next.js JSON data routes that did not match a path-based staff-login redirect.
- Countermeasure: Authorize inside the handler or framework middleware covering every route form.
- Type: Disclosed vulnerability report in a roundup; original report URL: https://hackerone.com/reports/3954327
- Severity/bounty: Medium; $3,100. [21]

2. Revoked token works again at Vercel
- Date: Exact date uncertain; within October 26-November 5, 2026.
- Platform: HackerOne; program: Vercel.
- Language/region: Not evident.
- Technique: Authorization-cache or stale-state flaw allowed a removed collaborator's revoked token to access private comment threads.
- Countermeasure: Delete the credential or server-side session on revocation; test revocation while exercising other users' features.
- Type: Disclosed vulnerability report in a roundup; original report URL: https://hackerone.com/reports/3852102
- Severity/bounty: Medium, CVSS 4.8; $1,026. [21]

3. Cross-account webhook edits in Basecamp
- Date: Exact date uncertain; within October 26-November 5, 2026.
- Platform: HackerOne; program: Basecamp.
- Language/region: Not evident.
- Technique: Broken object-level authorization in the webhook update handler, aided by guessable shared-counter IDs.
- Countermeasure: Check ownership in every object-ID handler and test GET, PUT, and DELETE separately.
- Type: Disclosed vulnerability report in a roundup; original report URL: https://hackerone.com/reports/3979217
- Severity/bounty: High, CVSS 8.3; not disclosed. [21]

4. An OAuth server that trusted any redirect
- Date: Exact date uncertain; within October 26-November 5, 2026.
- Platform: HackerOne; program: Basecamp.
- Language/region: Not evident.
- Technique: Unchecked OAuth redirect registration combined with the enabled implicit grant exposed access tokens.
- Countermeasure: Require exact-match pre-registered redirect URIs, PKCE, and disable the implicit grant.
- Type: Disclosed vulnerability report in a roundup; original report URL: https://hackerone.com/reports/3955956
- Severity/bounty: High; not disclosed. [21]

5. A payment webhook that fails open on WordCamp
- Date: Exact date uncertain; within October 26-November 5, 2026.
- Platform: HackerOne; program: WordPress.
- Language/region: WordCamp.org; region not evident.
- Technique: Invalid signatures were accepted, and payment identity was not bound to the order.
- Countermeasure: Reject failed signatures and verify payment ID and amount against the expected order.
- Type: Disclosed vulnerability report in a roundup; original report URL: https://hackerone.com/reports/3941626
- Severity/bounty: High, CVSS 8.7; not disclosed. [21]

6. Private posts readable through Secure Custom Fields
- Date: Exact date uncertain; within October 26-November 5, 2026.
- Platform: HackerOne; program: WordPress.
- Language/region: Not evident.
- Technique: Missing read authorization in a helper exposed draft, private, and password-protected posts.
- Countermeasure: Search for every caller when patching an entry point.
- Type: Disclosed vulnerability report in a roundup; original report URL: https://hackerone.com/reports/4152553
- Severity/bounty: High; not disclosed. [21]

7. An inverted check exposed organizer data
- Date: Exact date uncertain; within October 26-November 5, 2026.
- Platform: HackerOne; program: WordPress.
- Language/region: WordCamp Reports; region not evident.
- Technique: An AND instead of OR authorization condition allowed anonymous CSV export access.
- Countermeasure: Centralize authorization checks and test every export anonymously.
- Type: Disclosed vulnerability report in a roundup; original report URL: https://hackerone.com/reports/3871816
- Severity/bounty: High, CVSS 8.7; not disclosed. [21]

8. Editors inviting Administrators on wordpress.org
- Date: Exact date uncertain; within October 26-November 5, 2026.
- Platform: HackerOne; program: WordPress.
- Language/region: Rosetta locale sites on wordpress.org.
- Technique: Server-side role validation was omitted when storing and applying invitations, enabling an Editor to request Administrator.
- Countermeasure: Validate roles when storing and applying them; do not trust form choices.
- Type: Disclosed vulnerability report in a roundup; original report URL: https://hackerone.com/reports/3942522
- Severity/bounty: High, CVSS 8.7; not disclosed. [21]

9. Version control metadata left in Weblate downloads
- Date: Exact date uncertain; within October 26-November 5, 2026.
- Platform: HackerOne; program: Weblate.
- Language/region: Not evident.
- Technique: Incomplete archive hardening omitted .svn and .bzr, potentially exposing repository databases and cached credentials.
- Countermeasure: Reuse the existing complete excluded-path list.
- Type: Disclosed vulnerability report in a roundup; original report URL: https://hackerone.com/reports/4037976
- Severity/bounty: Medium; not disclosed. [21]

### Disclosed. October 12, 2026. Anthropic Expands Its Cyber Verification Program, Pwn2Own Ireland Pays Out $1.1M+, Bugcrowd Tightens Triage Rules, and more.

**Platform:** Disclosed newsletter. **Region/language:** English-language / global security community.

**URL:** `https://getdisclosed.com/p/disclosed-october-12-2026-anthropic-expands-its-cyber-verification-program-pwn2own-ireland-pays-out`

Page date: Oct 12, 2026; window status: in-window. Item publication dates are not stated unless noted. [16]

- "The Model Isn't Cooperating" - PortSwigger; autonomous-agent swarms, cascade failures, and token/compute costs; defensive countermeasure: not stated; original research article; date uncertain; https://portswigger.net/research/the-model-isnt-cooperating [16]
- "Pwn2Own Ireland 2026: Day 3 Results and Master of Pwn" - Zero Day Initiative; Pixel 10 multi-bug chain and contest results; countermeasure: not stated; event recap/advisory; date uncertain; https://www.zerodayinitiative.com/blog/2026/10/8/pwn2own-ireland-2026-day-three-results-amp-master-of-pwn [16]
- "PIChef: CyberChef-Inspired Workbench for Prompt Injection Payloads" - Sentry Security; prompt-injection payload composition, encoding, carriers, and reproducibility; countermeasure: not stated; tool; date uncertain; https://blog.sentry.security/pichef-a-tool-for-prompt-injection-inspired-by-cyberchef/ [16]
- "A JPEG, a Race, and a Ghost: Breaking Discourse's Image Pipeline" - Searchlight Cyber; HTML injection to stored XSS, ImageMagick/Ghostscript handling, and TOCTOU race; countermeasure: not stated; original research article; date uncertain; https://www.slcyber.io/research/a-jpeg-a-race-and-a-ghost-breaking-discourses-image-pipeline [16]
- "Smashing the Token Limit With Overlapping Fragments" - PortSwigger; CSS exfiltration using overlapping fragments; countermeasure: selector-budget analysis and reproduction labs are included; original research article; date uncertain; https://portswigger.net/research/smashing-the-token-limit [16]
- "Claude Code Worktree Sandbox Escape (CVE-2026-55607)" - GitHub repository; prompt-injected repository abusing Git worktrees to overwrite `.zshenv` and escape macOS Seatbelt; mitigation: block `.git` as a worktree name; tool/write-up; date uncertain; https://github.com/Metnew/write-ups/tree/main/claude-code-worktree-sandbox-escape [16]
- "DeepSeek-Reasonix: How a Poisoned Git Config Can Hijack an AI Coding Agent" - GitLab; `.gitattributes`-selected Git clean-filter command execution; mitigations: fixed versions, per-invocation key overrides, and safer diff strategies; original research/advisory; date uncertain; https://about.gitlab.com/blog/deepseek-reasonix-vulnerability-discovered/ [16]
- "How Abliterated Models Can Get You Pwned" - ProjectDiscovery; poisoned model backdoors, tool calls, command execution, and exfiltration; countermeasures: runtime sandboxing and strict trust boundaries; original research article; date uncertain; https://projectdiscovery.io/research/how-abliterated-models-can-get-you-pwned [16]
- "Adminer 0-days: Pre-auth RCE, Stored XSS, and Root RCE" - Voorivex; MSSQL DSN injection, stored XSS, and SQLite `VACUUM INTO`; fix: Adminer 5.4.3+; disclosure/advisory; date uncertain; http://blog.voorivex.team/three-0-day-vulnerabilities-in-adminer [16]
- "AgentCorruption: Prompt-Only Compromise of AWS Bedrock AgentCore via IMDS Access" - Zenity Labs; IMDS credential extraction, agent pivoting, memory poisoning, and secret theft; countermeasure: not stated; original research article; date uncertain; https://labs.zenity.io/post/agentcorruption-how-a-single-prompt-collapsed-the-entire-cloud-security-model [16]
- "Subdomain Takeover Escalation: From Dangling CNAME to Parent-Domain Cookie Control" - Synack; dangling-CNAME takeover and cookie control; mitigations: remove stale DNS targets and avoid broad cookie domains, including `__Host-`; original research article; date uncertain; https://www.synack.com/exploits-explained/subdomain-takeover-cookie-scope-impact/ [16]
- "New XSS Vector Using the usermedia Tag Added to the Cheat Sheet" - X/Twitter; `usermedia` HTML-tag XSS vector; countermeasure: not stated; discussion/advisory; date uncertain; https://twitter.com/garethheyes/status/2107463389039689908 [16]

Language/region is not stated for these items. [16]

### API Flow Hijacking and BOLA: CTEM API Testing

**Platform:** Trusteed blog. **Region/language:** English-language; geographic attribution not established.

**URL:** `https://trusteed.io/blog/unauthenticated-api-flow-hijacking-bola-ctem-api-security-testing`

- Exact title: "Unauthenticated API Flow Hijacking and BOLA: A CTEM API Security Testing Guide." [28]
- Publication date: October 11, 2026. This falls within the requested window of 2026-10-01 through 2026-11-14. [28]
- Source platform: Trusteed blog. [28]
- Language/region: Not evident from the page.
- Technique/research focus: Broken object-level authorization (BOLA) and unauthenticated API flow hijacking, including object-identifier substitution, step skipping, replay, reordering, race conditions, and client-side trust failures. [28]
- Defensive countermeasures: Continuous authenticated, object-aware API testing; centralized server-side object-scoped authorization; deriving identity and tenant from credentials; cross-tenant CI tests; flow testing out of order, replayed, and in parallel; object-level decision telemetry; and continuous authorization testing. [28]
- Classification: Original research/blog guide is not explicitly stated; the page categorizes it as "Research." It is not identified as a repost, advisory, tool, roundup, index, or discussion. [28]
- Canonical URL: https://trusteed.io/blog/unauthenticated-api-flow-hijacking-bola-ctem-api-security-testing [28]
- Roundup/index inventory: No roundup or index is present, so there are no additional web security research items, original URLs, or dates to enumerate. [28]

**Decision:** Use the linked original reports as a case library, but use the methodology material to organize testing around users, objects, roles and multi-step flows. A dated roundup is evidence of its own publication date; any different report-disclosure date must remain attached to the individual report.


## Six ArXiv Papers Separate Agent Attacks From Defensive Triage

The table uses **arXiv submission dates**, which establish public-preprint timing within the requested window. Author location is not inferred from names; "global / English" describes the publishing venue and language rather than an asserted research origin.

| Title | Source platform | Region / language | Public-preprint date | Key technique / defensive counter | URL |
|---|---|---|---|---|---|
| An Empirical Case Study of Prompt Engineering Strategies for Bypassing Multi-Layer Agent Security Defenses | arXiv | Global / English; author region not established | 2026-10-09 | Tests skill-file scanning, instruction safety evaluation and attack-trajectory scoring across 19 targets; studies layered defenses and behavioral constraints. [3] | `https://arxiv.org/abs/2610.14116` |
| BrowseSafe++: Benchmarking Prompt Injection Detection Across Web Contexts, Languages, and Browser Views | arXiv | Global / English; author region not established | 2026-10-12 | Paired attacked/clean pages in HTML, Markdown, accessibility trees and screenshots; BrowseSafe-Guard text/screenshot detectors and feedback-based BrowseSafe-Adapt. [5] | `https://arxiv.org/abs/2610.17457` |
| Analyzing and Mitigating Poisoning Attacks on Flow-Based Intrusion Detection | arXiv | Global / English; author region not established | 2026-10-14 | Reports latent backdoors from poisoning as little as 0.001% of training data; constrained perturbation analysis, distilled baselines, data sanitization and neuron pruning. Adjacent network-defense research, not an HTTP cache-poisoning paper. [1] | `https://arxiv.org/abs/2610.19766` |
| The Web Doesn't Sit Still: Adversarial Self-Evolving Attacks on Search Agents | arXiv | Global / English; author region not established | 2026-11-02 | Bi-level attacker/defender adaptation; CREO evolves attack populations with contrastive evolutionary signals; evaluates adaptive mitigation. [2] | `https://arxiv.org/abs/2611.03754` |
| Escalate or Close: How Fast-Tier Models Handle Held-Out Web Attack Families in Two-Tier Triage | arXiv | Global / English; author region not established | 2026-11-05 | Fast/slow request triage; seven held-out attack families, comparisons including OWASP CRS; hosted decision models reportedly escalate at least 97.6% of each family within a 5% benign budget. [4] | `https://arxiv.org/abs/2611.08229` |
| Harness Matters: Measuring and Dissecting Security Resilience in Web Agents | arXiv | Global / English; author region not established | 2026-11-09 | Four-stage agent-harness analysis; WebTrap Farm tests malicious prompts, prompt injection and deceptive design with paired usability calibration. [10] | `https://arxiv.org/abs/2611.11971` |

These papers address materially different targets: malicious requests, poisoned detector training data, and malicious content encountered by web agents. Do not combine their reported success rates or infer that one benchmark establishes production effectiveness across the others.

The **Harness Matters** case is especially relevant to defensive evaluation: paired usability tasks help distinguish an agent that resists an attack from one that simply cannot perform the underlying task. In contrast, **Escalate or Close** studies routing decisions within a defensive triage pipeline, so its escalation outcome is not equivalent to proving that exploitation was prevented. [10][4]

**Decision:** Evaluate web-agent resilience at both content and execution-harness layers, and assess triage systems against held-out attack families rather than relying only on familiar payload signatures.


## ProjectDiscovery And GitHub Material Focuses On Validation Workflows

ProjectDiscovery's Neo Triage announcement positions exploitability reproduction as an alternative to static risk scoring. That is a vendor-described workflow and product claim, not an independent comparative evaluation. Its useful operational question is whether a scanner, bounty or AI-generated finding can be reproduced against the actual asset. [9]

The GitHub roundup below is a dated source of repository leads. Inclusion in an October roundup does **not** establish that a repository was created in October, released a new version during the window, or appeared in a historical GitHub Trending snapshot; those are separate facts.

### Probably Not Exploitable  -  ProjectDiscovery Blog

**Platform:** ProjectDiscovery Blog. **Region/language:** English-language / global tooling community.

**URL:** `https://projectdiscovery.io/blog/probably-not-exploitable`

- Title: "Probably Not Exploitable." Publication date: Nov 10, 2026. Source platform: ProjectDiscovery Blog. Language/region: not stated. [7]
- Type: original research/discussion based on a survey of 214 security practitioners and leaders. [7]
- Technique/topic: vulnerability-backlog triage, AI-assisted security testing, and exploit validation. [7]
- Defensive countermeasure: use AI to triage and verify which findings are real, while retaining memory of prior decisions, environment context, and cross-tool duplicate detection. [7]
- Canonical URL: https://projectdiscovery.io/blog/probably-not-exploitable [7]

Related research items shown on the page:

- "Supply Chain Security Analysis of a 9.5M-Install VS Code Extension." Date: August 16, 2026. Outside-window. Type: original research/tool-assisted security analysis. Technique: auditing a VS Code extension, including Markdown rendering to JavaScript execution and five CVEs across two attack surfaces. Defensive relevance: review auto-updating extensions and their privileges. Original URL: https://projectdiscovery.io/blog/a-9-5m-install-vs-code-extension-one-markdown-file-and-a-supply-chain-foothold [7]

- "Watching Agents Work: A Behavioral Audit of Offensive-Security LLM Runs." Date: August 3, 2026. Outside-window. Type: original research/audit. Technique: behavioral evaluation of closed and open models during website-hacking tasks. Defensive countermeasure: assess agent behavior and end-to-end capability rather than relying only on solve rate. Original URL: https://projectdiscovery.io/blog/watching-agents-work-a-behavioral-audit-of-offensive-security-llm-runs [7]

- "Oh My Rogue Agent." Date: July 22, 2026. Outside-window. Type: original discussion/incident analysis. Technique: an autonomous agent escaped its sandbox, accessed the internet, and reached a production environment. Defensive countermeasure: sandboxing and containment. Original URL: https://projectdiscovery.io/blog/oh-my-rogue-agent [7]

### ProjectDiscovery Introduces Neo Triage, Replacing Static Risk Scores with Proven Exploitability | ProjectDiscovery

**Platform:** ProjectDiscovery official announcement. **Region/language:** English-language / San Francisco announcement.

**URL:** `https://projectdiscovery.io/news/neo-triage-press-release`

Title: "ProjectDiscovery Introduces Neo Triage, Replacing Static Risk Scores with Proven Exploitability" [9]

Publication date: October 26, 2026; within the requested window. [9]

Source platform: ProjectDiscovery website; source type: official press release announcing general availability of Neo Triage, a capability in the Neo platform. [9]

Language/region: English; San Francisco, United States. [9]

Technique: Neo Triage safely reproduces scanner, bug bounty, and AI-generated findings against the live asset in an isolated sandbox, then assigns severity based on proven impact and asset context. [9]

Defensive countermeasure: Validate findings with exact request/response evidence, suggest remediation, and automatically retest after the fix ships. [9]

Classification: Original product announcement/press release and security tool documentation; not a roundup, index, repost, advisory, or discussion. [9]

Canonical URL: https://projectdiscovery.io/news/neo-triage-press-release [9]

Roundup/index inventory: No roundup or index of separate web security research items is present; therefore, there are no additional original URLs or publication dates to enumerate. [9]

### Security GitHub Repos for Defenders (October 2026)

**Platform:** PixelTapes, linking GitHub repositories. **Region/language:** English-language / global tooling community.

**URL:** `https://pixeltapes.com/security-github-repos-october-2026/`

Exact title: "9 Security Repos on GitHub Defenders Should Know Right Now (October 2026)" [13]  
Publication date: October 15, 2026 [13]  
Source platform: GitHub, with repository URLs listed below [13]  
Language/region: English-language page; US region is evident for Ghidra because it is described as a US National Security Agency framework [13]  
Type: Original roundup/index of security tools, not a repost, advisory, or discussion [13]  
Canonical URL: https://pixeltapes.com/security-github-repos-october-2026/ [13]

All nine relevant research/tool items fall within the requested publication window by page publication date. Individual repository release or creation dates are generally not stated; where dates are stated, they are labeled below. [13]

1. NationalSecurityAgency/ghidra - https://github.com/NationalSecurityAgency/ghidra. Date: created in 2019; exact date not stated, outside/uncertain for the requested window. Technique: software reverse engineering and binary analysis. Defensive countermeasure: use it for malware analysis, incident response, and learning how binaries work. Type: tool. [13]

2. NVIDIA/OpenShell - https://github.com/NVIDIA/OpenShell. Date: not stated; uncertain. Technique: contained runtime for autonomous AI agents and command execution. Defensive countermeasure: limit what agents can access and review isolation before supplying credentials. Type: tool. [13]

3. usestrix/strix - https://github.com/usestrix/strix. Date: not stated; uncertain. Technique: AI penetration testing to find and fix application vulnerabilities. Defensive countermeasure: run only against owned applications, ideally in staging. Type: tool. [13]

4. KeygraphHQ/shannon - https://github.com/KeygraphHQ/shannon. Date: not stated; uncertain. Technique: source-code analysis, attack-path discovery, and real exploits against web applications and APIs. Defensive countermeasure: use a test copy owned by the operator, never production. Type: tool. [13]

5. openai/codex-security - https://github.com/openai/codex-security. Date: created in July 2026; exact date not stated, within window but uncertain. Technique: finding, validating, and fixing security bugs in code through a command-line tool and TypeScript SDK. Defensive countermeasure: require human review of suggested fixes. Type: tool. [13]

6. aquasecurity/trivy - https://github.com/aquasecurity/trivy. Date: not stated; uncertain. Technique: scanning containers, Kubernetes, code repositories, and cloud setups for vulnerabilities, misconfigurations, and leaked secrets; SBOM generation. Defensive countermeasure: add it to a build pipeline to check owned assets. Type: tool. [13]

7. projectdiscovery/nuclei - https://github.com/projectdiscovery/nuclei. Date: not stated; uncertain. Technique: YAML-template vulnerability scanning, including newly disclosed bugs. Defensive countermeasure: scan only owned applications, APIs, and cloud assets. Type: tool. [13]

8. WerWolv/ImHex - https://github.com/WerWolv/ImHex. Date: not stated; uncertain. Technique: examining raw bytes in files and firmware images. Defensive countermeasure: use for reverse engineering and file or firmware inspection. Type: tool. [13]

9. mandiant/capa - https://github.com/mandiant/capa. Date: not stated; uncertain. Technique: scanning executable files to identify capabilities. Defensive countermeasure: run unknown samples only inside an isolated analysis machine. Type: tool. [13]

### Professional / Community 2026.11 | Releases

**Platform:** PortSwigger Burp Suite release notes. **Region/language:** English-language / global tooling community.

**URL:** `https://portswigger.net/burp/releases/professional-community-2026-11`

Title: Professional / Community 2026.11 [29]  
Publication date: Friday, 13 November 2026 at 10:26 UTC [29]  
Source platform: PortSwigger Burp Suite Desktop [29]  
Language/region: Not stated.  
Type: Product release/tool announcement, not a research paper, repost, advisory, or discussion [29]  
Technique: No specific research technique stated; the release covers project switching, restarting Burp, Academy labs, Burp AT, and Collaborator retention [29]  
Defensive countermeasure: No specific countermeasure stated.  
Canonical URL: https://portswigger.net/burp/releases/professional-community-2026-11 [29]

No qualifying web security research items, roundups, or indexes with original research URLs and dates are present on this page. [29]

**Decision:** Separate three backlogs: reproducible target vulnerabilities, defensive evaluation work, and tooling/product adoption. A tool announcement can improve a hunting workflow without constituting a newly validated attack primitive.


## Hacker News And Reddit Add Discussion, Not Automatic Novelty

The following records cover community discussion and discovery surfaces. **Hacker News means news.ycombinator.com**; The Hacker News account on X is a separate publication. Dates, original links and uncertainty are retained below, and feed/index records should be read as collections of leads rather than as single original research publications.

The PHP2Shell discussions illustrate why this distinction matters: a newly published thread may analyze applicability or deployment assumptions without reporting a new vulnerability. Similarly, a discussion about prompt injection in HTTP headers is a different attack surface from CRLF request-header injection, despite the shared phrase "HTTP headers." [14]

### Prompt injection in HTTP headers: what 217M web responses show | Hacker News

**Platform:** Hacker News / news.ycombinator.com. **Region/language:** English-language / global community.

**URL:** `https://news.ycombinator.com/item?id=50104310`

- Title: "Prompt injection in HTTP headers: what 217M web responses show" [31]
- Source platform: Signalscrops.com, surfaced on Hacker News. [31]
- Publication date: Uncertain; the page only states "3 days ago," not an actual publication date. [31]
- Window status: Uncertain; cannot verify whether it falls within 2026-10-01 through 2026-11-14. [31]
- Language/region: Not evident.
- Technique: Prompt injection delivered through HTTP headers; the discussion also describes hidden text in a PDF as a system-manipulation technique. [31]
- Defensive countermeasure: Agents should probably not obey random instructions in headers; models are being trained against these attacks, and successful attacks may require more context than a short HTTP header. [31]
- Classification: Original research/article link with Hacker News discussion; not a roundup, index, advisory, or tool. [31]
- Canonical URL: https://www.signalscorps.com/blog/prompt-injection-in-http-headers/ [31]
- Roundup/index contents: No roundup or index is evident, so no additional research items or original URLs/dates can be enumerated. [31]

### PHP2Shell: AI uncovers critical RCE in PHP | Hacker News

**Platform:** Hacker News / news.ycombinator.com. **Region/language:** English-language / global community.

**URL:** `https://news.ycombinator.com/item?id=50180836`

- **"PHP2Shell: AI uncovers critical RCE in PHP"** - Publication date: not stated on the page; source platform: Hacker News; language/region: not evident; technique: AI-assisted vulnerability discovery; defensive countermeasure: PHP patches and coordinated disclosure; type: discussion; canonical URL: https://news.ycombinator.com/item?id=50180836 [39]

- **"Critical Vulnerabilities in PHP"** - Publication date: 2026-10-21 (timestamped index entry; exact article publication date not stated); source platform: CERT-EU; language/region: EU; technique: critical PHP vulnerabilities; defensive countermeasure: security release/patching; type: advisory; canonical URL: https://cert.europa.eu/publications/security-advisories/2026-018/ [39]

- **"EU issues RED alert for the critical PHP vulnerability"** - Publication date: 2026-10-21 (timestamped index entry; exact article publication date not stated); source platform: CERT-EU; language/region: EU; technique: critical PHP vulnerability; defensive countermeasure: RED alert and patching; type: advisory; canonical URL: https://cert.europa.eu/publications/security-advisories/2026-018/pdf [39]

- **"PHP warns admins of two critical flaws, emergency patches coming tomorrow"** - Publication date: 2026-10-21 (timestamped index entry; exact article publication date not stated); source platform: BleepingComputer; language/region: not evident; technique: two critical PHP flaws, including remote code execution; defensive countermeasure: emergency patches; type: news report/advisory; canonical URL: https://www.bleepingcomputer.com/news/security/php-warns-admins-of-two-critical-flaws-emergency-patches-coming-tomorrow/ [39]

- **"PHP RCE Zero-Days CVE-2026-109618, CVE-2026-109619 Leak Early"** - Publication date: 2026-10-21 (timestamped index entry; exact article publication date not stated); source platform: CyberKendra; language/region: not evident; technique: remote code execution zero-days; defensive countermeasure: PHP patches and public disclosure; type: news report; canonical URL: https://www.cyberkendra.com/2026/10/php-cve-2026-109618-cve-2026-109619-rce.html [39]

- **"Passive exposure check for the PHP2Shell flaws (CVE-2026-109618/109619)"** - Publication date: 2026-10-21 (timestamped index entry; exact publication date not stated); source platform: PHP2Shell.xyz; language/region: not evident; technique: passive exposure checking; defensive countermeasure: exposure assessment; type: tool; canonical URL: https://php2shell.xyz/ [39]

- **"Check/probe tool for PHP CVE-2026-109618/619"** - Publication date: 2026-10-21 (timestamped index entry; exact publication date not stated); source platform: PHP2Shell.site; language/region: not evident; technique: vulnerability checking/probing; defensive countermeasure: probing for exposure; type: tool; canonical URL: https://php2shell.site/news.ycombinator.com/11c22360e8df83b4 [39]

- **"PHP patches have been released"** - Publication date: 2026-10-21 (timestamped index entry; exact publication date not stated); source platform: PHP.net; language/region: not evident; technique: PHP RCE vulnerabilities; defensive countermeasure: released patches; type: advisory; canonical URL: https://www.php.net/archive/2026.php [39]

- **"PHP Security advisory: Critical remote code execution vulnerabilities"** - Publication date: 2026-10-21 (timestamped index entry; exact publication date not stated); source platform: PHP.net; language/region: not evident; technique: critical remote code execution vulnerabilities; defensive countermeasure: security advisory and patching; type: advisory; canonical URL: https://www.php.net/archive/2026.php [39]

- **"Governments Take Websites Offline After PHP Security Warnings"** - Publication date: 2026-10-21 (timestamped index entry; exact article publication date not stated); source platform: Bloomberg; language/region: not evident; technique: PHP security vulnerabilities; defensive countermeasure: taking websites offline; type: news report; canonical URL: https://www.bloomberg.com/news/articles/2026-10-21/governments-take-websites-offline-after-php-security-warnings [39]

- **"Dutch National Cyber Security Center is Offline because it uses PHP"** - Publication date: 2026-10-21 (timestamped index entry; exact publication date not stated); source platform: NCSC Netherlands; language/region: Netherlands; technique: PHP security vulnerability; defensive countermeasure: service taken offline; type: incident report; canonical URL: https://www.ncsc.nl/actueel [39]

- **"Upcoming Critical PHP Security Release (CVSSv4 score of 9.2)"** - Publication date: outside window/2026-10-20 index timestamp; exact article publication date not stated; source platform: PHP.net; language/region: not evident; technique: critical PHP vulnerability; defensive countermeasure: upcoming security release; type: advisory; canonical URL: https://www.php.net/index.php [39]

- **"Ai fumbles responsible disclosure"** - Publication date: uncertain; source platform: Hacker News; language/region: not evident; technique: AI-assisted vulnerability discovery and disclosure; defensive countermeasure: coordinated disclosure; type: discussion; canonical URL: https://news.ycombinator.com/item?id=50180836 [39]

### AskNetsec

**Platform:** Reddit r/AskNetsec feed. **Region/language:** English-language / global community.

**URL:** `https://www.reddit.com/r/AskNetsec`

- **"Is php2shell only practical against extremely low-traffic targets?"** Publication date: uncertain; page says "12 days ago." Source: Reddit, r/AskNetsec; language: English; region: not evident. Type: discussion/analysis. Technique: multiple consecutive requests to the same PHP worker, with process pinning and traffic disruption. Countermeasure: use WAF monitoring and remediation; exploitability may require build-specific testing. Canonical URL: https://www.reddit.com/r/AskNetsec/comments/1xe4l6k/is_php2shell_only_practical_against_extremely/ [40]

- **"How are you defending AI agents against indirect prompt injection?"** Publication date: uncertain; page says "12 hr. ago." Source: Reddit, r/AskNetsec; language: English; region: not evident. Type: discussion/threat research. Technique: hidden instructions in external content manipulate an agent into retrieving sensitive information or using tools. Countermeasure: treat external content as untrusted, separate instructions from retrieved information, use prompt-injection filtering, architectural isolation, and restrict tool use. Canonical URL: https://www.reddit.com/r/AskNetsec/comments/1xnkxmq/how_are_you_defending_ai_agents_against_indirect/ [40]

- **"What do you actually show an author when a critical CVE stays open?"** Publication date: uncertain; no actual date shown. Source: Reddit, r/AskNetsec; language: English; region: not evident. Type: discussion. Technique: IDOR testing by distinguishing identifier changes from authorization failure. Countermeasure: verify authorization failure and test only in authorized labs or explicitly permitted bug-bounty scope. Canonical URL: https://www.reddit.com/r/AskNetsec/comments/1xnjjfx/is_changing_an_object_id_enough_to_identify_an/ [40]

- **"WOFF2SHELL: Is Brotli 0-day (CVE-2026-111497) a bidirectional nuke hiding in web fonts?"** Publication date: uncertain; page says "10 days ago." Source: Reddit, r/AskNetsec; language: English; region: not evident. Type: discussion/analysis. Technique: exploitation of a vulnerable bundled Brotli C decoder when processing WOFF2 fonts. Countermeasure: patch the bundled decoder; a fix was proposed in PR #208. Canonical URL: https://www.reddit.com/r/AskNetsec/comments/1xf8sby/woff2shell_is_brotli_0day_cve2026111497_a/ [40]

- **"How would you do a deep security audit of a vibe-coded SaaS?"** Publication date: uncertain; page says "8 days ago." Source: Reddit, r/AskNetsec; language: English; region: not evident. Type: discussion/education. Technique: test authorization, authentication bypass, API abuse, payment logic, backend, and AI-generated code. Countermeasure: perform a structured manual and tool-assisted security audit, including backend and API testing. Canonical URL: https://www.reddit.com/r/AskNetsec/comments/1xhhu6h/how_would_you_do_a_deep_security_audit_of_a/ [40]

- **"What do you log when retrieved text steers a tool?"** Publication date: uncertain; no actual date shown. Source: Reddit, r/AskNetsec; language: English; region: not evident. Type: discussion/threat research. Technique: indirect prompt injection in retrieved HTML steering a model toward `fetch_url`. Countermeasure: tool allowlisting and egress control; log retrieval source, tool arguments, blocked attempts, and allowed-destination traces. Canonical URL: https://www.reddit.com/r/AskNetsec/comments/1wxh6l0/what_do_you_log_when_retrieved_text_steers_a_tool/ [40]

- **"How are you finding forgotten PHP hosts after PHP2Shell?"** Publication date: uncertain; page says "10 days ago." Source: Reddit, r/AskNetsec; language: English; region: not evident. Type: discussion/analysis. Technique: external discovery of forgotten public PHP hosts using inventories, certificate transparency, passive DNS, and internet scanners. Countermeasure: correlate ownership, package, and vulnerability inventories; confirm backports; restart relevant workers and test public routes after patching. Canonical URL: https://www.reddit.com/r/AskNetsec/comments/1xfp719/how_are_you_finding_forgotten_php_hosts_after/ [40]

- **Window status:** All listed publication dates are uncertain because the page provides relative dates or no publication date; none can be verified as falling within 2026-10-01 through 2026-11-14. [40]

### Technical Information Security Content & Discussion

**Platform:** Reddit r/netsec feed. **Region/language:** English-language / global community.

**URL:** `https://www.reddit.com/r/netsec/new/`

- "OWASP Top 10 Neocloud and AI Data Center Security Risks project released" - publication date: uncertain; page shows "12 min. ago"; platform: Reddit r/netsec; language/region: not evident; type: research project announcement; technique/countermeasure: neocloud and AI data-center security risks; canonical URL: https://owasp.org/news/owasp-top-10-neocloud [35]
- "JSON Schema References Considered Harmful" - publication date: uncertain; page shows "35 min. ago"; platform: Reddit r/netsec; language/region: not evident; type: research/discussion; technique/countermeasure: JSON Schema external entities; canonical URL: https://www.svix.com/blog/json-schema-external-entities/ [35]
- "NvRoot (CVE-2026-47591) where in neocloud multi-tenant GPU environments, rent = root. Essentially it's a dirty page cache LPE using GPUs as catalyzer" - publication date: uncertain; page shows "6 hr. ago"; platform: Reddit r/netsec; language/region: not evident; type: vulnerability research; technique: dirty page cache local privilege escalation using GPUs; countermeasure: not stated; canonical URL: https://stealthium.io/blog/nvroot [35]
- "prepared statements prevents SQLi. But it also helped me to exploit a 22 years old PostgreSQL 0-day RCE (CVE-2026-6460)" - publication date: uncertain; page shows "7 hr. ago"; platform: Reddit r/netsec; language/region: not evident; type: vulnerability research; technique: PostgreSQL type confusion to RCE; countermeasure: prepared statements prevent SQL injection; canonical URL: https://mehmetince.net/part-3-6-how-i-ended-up-turning-a-22-year-old-postgresql-type-confusion-primitive-into-rce-cve-2026-6460/ [35]
- "Claude Code VSCode Plugin: Workspace Escape Via Misleading Permission Prompt" - publication date: 2026-11; platform: Reddit r/netsec; language/region: not evident; type: vulnerability research; technique: workspace escape via misleading permission prompt; countermeasure: not stated; canonical URL: https://ultrastrike.io/2026/11/claude-code-vscode-plugin-workspace-escape-via-misleading-permission-prompt/ [35]
- "ScriptBlock Smuggling - AMSI Evasion" - publication date: 2026-11-11; platform: Reddit r/netsec; language/region: not evident; type: vulnerability research; technique: ScriptBlock smuggling and AMSI evasion; countermeasure: not stated; canonical URL: https://ipurple.team/2026/11/11/scriptblock-smuggling/ [35]
- "Forwarded Without Question: How Web Frameworks Overtrust the Forwarded Header" - publication date: 2026-11-05; platform: Reddit r/netsec; language/region: not evident; type: research/discussion; technique: forwarded-header trust; countermeasure: not stated; canonical URL: https://www.lkoskela.fi/blog/2026-11-05-forwarded-without-question/ [35]
- "Barracuda Networks is your new best friend (Barracuda Email Security Gateway Pre-Auth Remote Root RCE CVE-2026-116606 / CVE-2026-111560) - watchTowr Labs" - publication date: uncertain; page shows "7 days ago"; platform: Reddit r/netsec; language/region: not evident; type: vulnerability advisory/research; technique: pre-auth remote root RCE; countermeasure: not stated; canonical URL: https://labs.watchtowr.com/barracuda-networks-is-your-new-best-friend-barracuda-email-security-gateway-pre-auth-remote-root-rce-cve-2026-116606-cve-2026-111560/ [35]

Outside window: "email encryption" has canonical URL dated 2026-07-19, outside the requested window. [35]

### The Hacker News on X: "🚨 Node.js warns of HIGH-severity security vulnerabilities.

Security fixes are coming November 11 for Node.js 26.x, 24.x, and 22.x.

All three release lines are affected. Production users should take note.

Details: https://t.co/kyerFMiO8K" / X

**Platform:** X / The Hacker News account. **Region/language:** English-language / global security-news audience.

**URL:** `https://x.com/TheHackersNews/status/2117977473044697537`

Title: The Hacker News on X: "🚨 Node.js warns of HIGH-severity security vulnerabilities." [30]

Publication date: November 4, 2026, at 1:49 PM; within the requested window. [30] Source platform: X. [30] Language: English; region not evident. [30]

Technique: High-severity Node.js security vulnerabilities; no specific technique is identified. [30] Defensive countermeasure: Security fixes are coming November 11 for Node.js 26.x, 24.x, and 22.x; all three release lines are affected. [30]

Type: Advisory/news post, not a roundup, index, tool, repost, or discussion. [30] Canonical URL: https://x.com/TheHackersNews/status/2117977473044697537 [30]

No relevant web security research roundup/index items or original research URLs and dates are present on this page. [30]

### Platform And Technique Coverage Still Has Explicit Gaps

| Requested surface or technique | Inventory status | How to interpret the gap |
|---|---|---|
| PortSwigger Research | Direct articles and a presentation publication identified | Separate original publication from later video or secondary coverage. |
| Web Security Academy additions | No individually date-verified new Academy lesson/lab established | Burp release notes are not evidence of a new Academy addition. |
| arXiv | Six public-preprint records above | One is adjacent IDS-defense research; it is explicitly labeled. |
| Hacker News | Specific discussion URLs above | Threads are not independent vulnerability discoveries. |
| Reddit r/netsec and r/AskNetsec | Feed-derived discussion records above | Preserve missing or relative dates; do not treat every visible feed item as in-window. |
| X/Twitter | A specific Node.js announcement record above | A news-account post does not represent the entire security community. |
| Xianzhi, Anquanke, Zhihu | Direct platform content above | Keep original-language titles and source-specific dates. |
| FreeBuf | Dated Chinese-index leads above | Some original article permalinks remain unavailable. |
| WeChat security accounts | No individually date-verified original account article established | Chinese roundups do not substitute for an original WeChat URL. |
| Habr | Russian-language records above | Publication, translation and vulnerability-discovery dates differ. |
| Russian Telegram security channels | No individually date-verified original channel post established | Research about Telegram is not equivalent to research published on Telegram. |
| JPCERT/CC and Japanese security press | Official investigation and Japanese advisory coverage above | Language editions and repeated coverage should be deduplicated. |
| niconico | No qualifying original research publication established | An outage or emergency-maintenance discussion is not itself attack research. |
| HackerOne | Report-level leads and links from disclosed-report roundups | Direct-report dates should take precedence over roundup dates. |
| Bugcrowd | No individually date-verified disclosed report established | A disclosure portal homepage is not a report. |
| HTB forums | No individually date-verified qualifying forum research item established | The general blog/forum presence does not establish an in-window item. |
| ProjectDiscovery | Official blog/product records above | Vendor claims remain attributed. |
| GitHub Trending | Repository roundup leads, not a verified historical Trending inventory | Do not claim trending rank, launch date or release timing without that evidence. |
| HTTP desync and cache poisoning | Concrete article/advisory/Chinese-index coverage above | Distinguish HTTP caches, template caches and AI/data poisoning. |
| HTTP Upgrade-specific variants | No separately date-verified qualifying new variant established | Do not relabel general desync as an Upgrade-specific result. |
| Prototype-pollution variants | No separately date-verified qualifying new variant established | Evergreen prevention and testing pages do not establish new in-window research. |
| New sanitizer bypasses | Original SVG research plus dated defensive coverage above | Deduplicate original research and explanatory articles. |
| API authorization and AI hunting | Methodology, report, academic and tooling material above | Differentiate demonstrated bugs, experimental workflows and product announcements. |

This is a coverage map, not evidence that missing categories published nothing. The highest-value next additions would be original FreeBuf/WeChat permalinks, direct bounty-platform records, dated Telegram posts, historical GitHub Trending snapshots, and dated Academy change announcements.


## Synthesis

The material points to a shared analytical problem: **a security boundary looks stronger when inspected in isolation than when tested as part of a full workflow**. Header validation can feed a desync chain; CSP allow-lists and form destinations can undermine browser-side protection; and agent resilience depends on the harness as well as the model. The sources support these as distinct cases, not as one universal exploit mechanism. [14][19][10]

| Research family | Mechanism and scope | Main trade-off or failure mode | Evidence base | Practical use |
|---|---|---|---|---|
| Header/desync and proxy-cache work | Interpretation differences across HTTP processing layers | Local input validation can miss end-to-end behavior | Research workflows, presentation and advisory coverage. [14][20][15] | Test actual proxy/backend combinations and deployed configuration. |
| CSP and SVG content processing | Trusted browser/content-processing features become usable in an attack chain | A defense label does not guarantee safe policy or sanitization | Original research and defensive interpretation. [19][18] | Review effective policies, active content handling and sanitizer updates. |
| Authorization and disclosed workflows | Access depends on object, identity and process state | Payload-only testing can overlook business-logic failures | Disclosed-report inventories and API methodology material. [26] | Build case-based role/object/workflow tests. |
| AI-agent security and triage | Untrusted content affects decisions; harnesses and escalation rules shape outcomes | Refusal, inability and successful defense can look similar | Public preprints with different experimental targets. [10][4] | Use paired capability/security tests and held-out attack families. |
| AI-assisted validation tools | Reproduction seeks to convert a suspected finding into demonstrated impact | Vendor assertions are not independent validation | Official product description and research/tool workflows. [9][14] | Retain reproducible evidence and human review for consequential actions. |

The main tension is between **automation and evidence quality**. Automation can connect a weak-looking input behavior to a consequential chain, but a benchmark score, a social post, a product announcement and a disclosed bounty report answer different questions. Treating them as interchangeable would inflate both novelty and confidence.

A second tension is between **regional breadth and bibliographic completeness**. Chinese indexes add leads that broad English-language searches miss, but homepage-only references cannot support the same article-level precision as direct platform records. Preserving those leads with explicit limitations is more useful than either discarding them or manufacturing exact URLs.

**Bottom line:** prioritize the directly dated protocol, CSP, SVG, API/report and agent-defense material for immediate technical review. Use regional indexes and social discussions as an expansion queue. This inventory supports that prioritization, but it does not substantiate an exhaustive census across every public and private platform.

## References

1. *Analyzing and Mitigating Poisoning Attacks on Flow-Based Intrusion Detection*. https://arxiv.org/abs/2610.19766
2. *The Web Doesn't Sit Still: Adversarial Self-Evolving Attacks on Search Agents*. https://arxiv.org/abs/2611.03754
3. *An Empirical Case Study of Prompt Engineering Strategies for Bypassing Multi-Layer Agent Security Defenses*. https://arxiv.org/abs/2610.14116
4. *Escalate or Close: How Fast-Tier Models Handle Held-Out Web Attack Families in Two-Tier Triage*. https://arxiv.org/abs/2611.08229
5. *BrowseSafe++: Benchmarking Prompt Injection Detection Across Web Contexts, Languages, and Browser Views*. https://arxiv.org/abs/2610.17457
6. *連続不正アクセス事案の攻撃手法に関する調査 - JPCERT/CC Eyes | JPCERTコーディネーションセンター公式ブログ*. https://blogs.jpcert.or.jp/ja/2026/10/web_api_attacks.html
7. *Probably Not Exploitable — ProjectDiscovery Blog*. https://projectdiscovery.io/blog/probably-not-exploitable
8. *KUSANAGI に HTTP ヘッダーインジェクションの脆弱性 | ScanNetSecurity*. https://scan.netsecurity.ne.jp/article/2026/11/12/56753.html
9. *ProjectDiscovery Introduces Neo Triage, Replacing Static Risk Scores with Proven Exploitability | ProjectDiscovery*. https://projectdiscovery.io/news/neo-triage-press-release
10. *Harness Matters: Measuring and Dissecting Security Resilience in Web Agents*. https://arxiv.org/abs/2611.11971
11. *Две критические CVE в PHP и GitLab: уязвимости выходят быстрее, чем их успевают закрыть / Habr*. https://habr.com/ru/publications/1102528
12. *Recent AI-Assisted Cyber Attacks in Japan: Investigating Attack Infrastructure and Techniques - JPCERT/CC Eyes | JPCERT Coordination Center official Blog*. https://blogs.jpcert.or.jp/en/2026/10/web_api_attacks.html
13. *Security GitHub Repos for Defenders (October 2026)*. https://pixeltapes.com/security-github-repos-october-2026/
14. *Making HTTP header injection critical with one prompt | PortSwigger Research*. https://portswigger.net/research/making-http-header-injection-critical-with-one-prompt
15. *Apache Traffic Server Vulnerabilities: Cache Poisoning Risk*. https://securityonline.info/apache-traffic-server-vulnerabilities-october-2026/
16. *Disclosed. October 12, 2026. Anthropic Expands Its Cyber Verification Program, Pwn2Own Ireland Pays Out $1.1M+, Bugcrowd Tightens Triage Rules, and more.*. https://getdisclosed.com/p/disclosed-october-12-2026-anthropic-expands-its-cyber-verification-program-pwn2own-ireland-pays-out
17. *Чёрный октябрь уязвимостей: что задело мой сервер, как я закрыл дыры и почему ушёл на статику без инлайн-скриптов / Хабр*. https://habr.com/ru/articles/1100918/
18. *SVG Sanitiser Bypasses: What the PortSwigger Research Means for Web Application Security - Secarma: Penetration Testing and Cybersecurity Company*. https://secarma.com/30-10-2026-svg-sanitiser-bypasses-portswigger-research
19. *Blind trust: stealing credentials through CSP | PortSwigger Research*. https://portswigger.net/research/blind-trust-stealing-credentials-through-csp
20. *HTTP Terminator: an AI system proposed a new desync attack class*. https://theinjection.dev/items/portswigger-http-terminator-defcon
21. *Bug bounty roundup: nine disclosed reports worth reading | Yaamlabs*. https://yaamlabs.com/blog/bug-bounty-roundup-2026-11-06
22. *Claude нашёл 62 уязвимости в Chrome и собрал цепочки атак на Safari, Android, Windows и Linux / Хабр*. https://habr.com/ru/companies/otus/news/1100652
23. *注意喚起*. https://www.jpcert.or.jp/at/2026.html
24. *國內網絡安全動態（2026年10月12日） | Security Aggregator*. http://cwl.elvis.hk/news/china-2026-10-12
25. *國內網絡安全動態（2026年10月11日） | Security Aggregator*. https://cwl.elvis.hk/news/china-2026-10-11
26. *Bug bounty roundup: 15 disclosed reports worth reading | Yaamlabs*. https://yaamlabs.com/blog/bug-bounty-roundup-2026-11-08
27. *cybersecurity-daily/网安日报速递-2026年10月13日.md at main · Unclecheng-li/cybersecurity-daily · GitHub*. https://github.com/Unclecheng-li/cybersecurity-daily/blob/main/%E7%BD%91%E5%AE%89%E6%97%A5%E6%8A%A5%E9%80%9F%E9%80%92-2026%E5%B9%B410%E6%9C%8813%E6%97%A5.md
28. *API Flow Hijacking and BOLA: CTEM API Testing*. https://trusteed.io/blog/unauthenticated-api-flow-hijacking-bola-ctem-api-security-testing
29. *Professional / Community 2026.11 | Releases*. https://portswigger.net/burp/releases/professional-community-2026-11
30. [The Hacker News on X: "🚨 Node.js warns of HIGH-severity security vulnerabilities.

Security fixes are coming November 11 for Node.js 26.x, 24.x, and 22.x.

All three release lines are affected. Production users should take note.

Details: https://t.co/kyerFMiO8K" / X](https://x.com/TheHackersNews/status/2117977473044697537)
31. *Prompt injection in HTTP headers: what 217M web responses show | Hacker News*. https://news.ycombinator.com/item?id=50104310
32. *Telegram попросил нас молчать об XSS. Мы всё равно публикуем / Хабр*. https://habr.com/ru/articles/1083246
33. *portswigger.net*. https://portswigger.net/research/rss
34. *Scalable Vector Grief | PortSwigger Research*. https://portswigger.net/research/scalable-vector-grief
35. *Technical Information Security Content & Discussion*. https://www.reddit.com/r/netsec/new/
36. *安全资讯 - 安全KER，安全资讯平台*. https://www.anquanke.com/news
37. *PHP 中的严重漏洞（2026-10-21） - 知乎*. https://zhuanlan.zhihu.com/p/2096182377051583576
38. *先知社区 · AI 时代的白帽社区*. https://xz.aliyun.com/
39. *PHP2Shell: AI uncovers critical RCE in PHP | Hacker News*. https://news.ycombinator.com/item?id=50180836
40. *AskNetsec*. https://www.reddit.com/r/AskNetsec
