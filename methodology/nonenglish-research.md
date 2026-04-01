# Non-English Market Research Methodology

**Purpose:** How to research ERPNext/Frappe ecosystem opportunities in non-English speaking markets  
**Date:** March 2026  
**Output:** Market reports in `market-research/` + regional personas in `research-personas/`

---

## Overview

The original English-only forum corpus (discuss.frappe.io) captures only a fraction of global ERPNext activity. To identify non-English market opportunities, this research used a community-mapping approach:

1. **Map** all non-English ERPNext communities (Telegram, GitHub, partner directories)
2. **Research** compliance requirements per country
3. **Identify** GitHub localization repos
4. **Score** opportunities per market
5. **Create** regional personas

---

## Step 1: Community Mapping

### Finding Telegram Channels

Telegram is the dominant platform for non-English ERPNext communities. Use web search to find them:

```
site:t.me ERPNext India
site:t.me ERPNext Brazil
site:t.me ERPNext Germany
site:t.me Frappe Arabic
site:t.me ERPNext Africa
site:t.me ERPNext Mexico
site:t.me ERPNext Vietnam
site:t.me ERPNext Indonesia
```

**Key Telegram search terms by region:**

| Region | Search terms |
|--------|------------|
| India | `t.me/erpnext India`, `t.me/frappe India`, `ERPNext Hindi` |
| MENA | `t.me/erpnext Arabic`, `t.me/frappe MENA`, `t.me/erpnext Saudi` |
| Brazil | `t.me/erpnext Brazil`, `t.me/erpnext brasil` |
| Germany | `t.me/erpnext Germany`, `t.me/frappe DE`, `t.me/erpnext deutschland` |
| Africa | `t.me/erpnext Africa`, `t.me/erpnext Nigeria`, `t.me/erpnext Kenya` |
| China | `t.me/erpnext China`, `t.me/frappe CN` |
| SEA | `t.me/erpnext Vietnam`, `t.me/erpnext Thailand`, `t.me/erpnext Indonesia` |
| LatAm | `t.me/erpnext Mexico`, `t.me/erpnext Argentina`, `t.me/erpnext Colombia` |

**Accessing Telegram channels:**
- Public channels can be viewed at web.telegram.org
- Historical messages may be limited (Telegram doesn't expose full history via web)
- Member counts and recent messages give activity signals
- No deep topic analysis from Telegram alone

### Frappe.io Partner Directory

The Frappe partner directory (frappe.io/partners) lists certified partners by country. This is a signal of market activity and implementation capacity.

```
Search: frappe.io/partners
Filter by: country
```

### GitHub Organization Search

Search GitHub for ERPNext localization by language/country:

```
site:github.com ERPNext India localization
site:github.com ERPNext Brazil localization
site:github.com ERPNext German localization
site:gitee.com ERPNext China localization  (China-specific)
```

**Gitee:** Gitee (gitee.com) is China's GitHub alternative. Chinese ERPNext projects are often on Gitee, not GitHub.

---

## Step 2: Compliance Research Per Country

For each country, research the following compliance requirements:

### E-Invoicing Mandates

Every country in the world is moving to mandatory e-invoicing. For each country:

1. What government authority manages e-invoicing? (e.g., FIRS Nigeria, ZATCA Saudi Arabia, SAT Mexico)
2. What is the mandate status? (Active, Phase 1, Phase 2, Upcoming, Voluntary)
3. Is ERPNext on the list of supported ERPs?
4. What API/integration is required?

**Key resources:**
- Country tax authority websites
- PEPPOL (global e-invoicing standard) documentation
- Tax technology blogs and consulting firms
- Government digital transformation initiatives

### Localization Requirements

1. **Chart of accounts:** Does the country have a standard chart of accounts?
   - Germany: SKR03, SKR04
   - Brazil: SPED chart of accounts
   - OHADA (17 African countries): SYSCOHADA
   - India: No standard, but GST requires specific structure

2. **Tax requirements:**
   - VAT/GST rates and filing requirements
   - Withholding tax
   - Payroll tax and social contributions
   - E-invoicing tax calculations

3. **Banking:**
   - Country-specific bank format (MT940, CAMT, etc.)
   - Payment file formats (SEPA, SWIFT, local)
   - Bank API integrations

4. **Language and formatting:**
   - UI translation completeness
   - RTL (right-to-left) support for Arabic
   - Date, number, currency formatting
   - Legal document formats

---

## Step 3: GitHub Localization Repository Analysis

For each market, search for existing ERPNext localization repositories:

### India
- `resilient-tech/india-compliance` — India GST, E-invoice, E-waybill (most important)
- `laxmantandon/express_tally` — Tally migration (unmaintained)

### Brazil
- `Intelligence8official/ERPNext_Brazil` — primary localization
- `Intelligence8official/ERPNext_Brazil_NF` — NF-e integration
- `techmaxsolucoes/motor_tributario_py` — Brazilian tax calculation (7 stars)

### Germany
- `alyf-de/erpnext_germany` — 80 stars, main German localization
- `libracore/erpnextswiss` — 95 stars, Swiss localization (model for Germany)

### China
- `yuzelin/erpnext_chinese` — Gitee, 202 stars, most active
- `SolutionAlliance/erpnext_chinese` — GitHub

### Africa
- `TinasheErasmus/sa_vat_compliance` — South Africa VAT (Jan 2026, active)

### Southeast Asia
- `agile-technica/erpnext-indonesia-localization` — Indonesia, 40 stars

### Key metrics per repo:
- Stars and forks (community interest signal)
- Last commit date (active vs. stale)
- Open issues and PRs (community engagement)
- README completeness (how mature is the project)

---

## Step 4: Scoring Opportunities Per Market

For each country, score opportunities using:

### Market Opportunity Matrix

| Dimension | Scoring | Notes |
|-----------|---------|-------|
| Market size | 1-10 | Population, GDP, ERPNext adoption |
| Compliance urgency | 1-10 | Deadline proximity, penalty severity |
| ERPNext readiness | 1-10 | How much ERPNext support exists |
| Solo-founder viability | YES/PARTIAL/NO | Can a solo non-local build this? |
| First mover advantage | 1-10 | How many competitors exist? |

### Country Scorecard Template

```markdown
### [Country] Market Scorecard

| Metric | Score | Evidence |
|--------|-------|---------|
| ERPNext users (est.) | X | Source |
| Market size | X | GDP, population |
| E-invoicing mandate | [STATUS] | Deadline: [DATE] |
| ERPNext compliance | X/10 | [What's missing] |
| GitHub repos | [N repos] | [Key repos] |
| Telegram channels | [N channels] | [Activity level] |
| Solo-viable? | YES/PARTIAL/NO | [Why] |

### Top Opportunities

1. **[OPP-##]: [Name]** — [Score]/10
   - Evidence: [Source]
   - Build difficulty: [Easy/Medium/Hard]
   - Local partner needed: [Yes/No]

2. **[OPP-##]: [Name]** — [Score]/10
   ...
```

---

## Step 5: Regional Persona Creation

Based on market research, create regional personas representing market-specific archetypes:

### Persona Template

```markdown
# Persona: [Persona Name]

**Source:** [Non-English Market Research — Country]
**Read:** `market-research/[country].md`

## Profile
[Who is this person? E.g., Indian accountant locked into Tally, German CFO locked into DATEV]

## Core Characteristics
- What they believe about ERPNext
- What actually frustrates them
- What they secretly want

## How They Evaluate Opportunities
- What they look for
- Red flags that kill interest
- Pricing tolerance

## WTP Signals
- Evidence of willingness to pay
- Market size signals

## Opportunity Architecture
- What needs to be built for them
- Build difficulty
- Pricing model

## Persona Scorecard
| Dimension | Score | Notes |
|-----------|-------|-------|
| Market Size | X/10 | |
| WTP | X/10 | |
| Urgency | X/10 | |
| Competition | X/10 | |
| Solo-Founder Fit | X/10 | |
| Moat | X/10 | |
| Exit Potential | X/10 | |
| **Overall** | **X.X/10** | |
```

### Personas Created for This Research

| Persona | Market | Key Insight |
|---------|--------|------------|
| Tally Survivor | India | 10M Tally users need migration help |
| DATEV Prisoner | Germany | 7yr demand, zero solutions |
| FIRS Deadline Fighter | Nigeria | Crisis mode, max WTP |
| SPED Compliance Navigator | Brazil | NF-e is the #1 blocker |
| Totvs Escape Artist | Brazil | R$10K-50K/month captive market |
| Arabic Digital Transformer | MENA | RTL print is the real gap |
| GoBD Compliant | Germany | ERPNext violates German law |
| Mandate Chaser | Global | Build before deadline hits |

---

## Step 6: Writing the Market Report

For each region, write `market-research/[region].md`:

### Market Report Template

```markdown
# ERPNext [Country] Market Research

**Date:** [Date]
**Market:** [Country]

## Community Infrastructure
[Telegram channels, GitHub repos, partner directory, events]

## Market Fundamentals
[Dominant competitors, ERPNext adoption, implementation partners]

## Compliance Requirements
[Country-specific compliance: e-invoicing, tax, banking]

## Localization Gaps
[What exists vs. what's missing]

## Opportunity Analysis

### OPP-[REGION]-01: [Name]
**Priority: CRITICAL/HIGH/MEDIUM** | **Confidence: X/10**

[What it solves]

**What's needed:**
- [Technical requirements]
- [Local partner needed?]

**Build difficulty:** [Easy/Medium/Very High]

**Pricing:** [Price range]

**Evidence:** [Source, topic IDs, forum posts]

## Competitive Landscape
[What ERPNext competitors exist]

## New Personas Identified
[List any regional personas created]

## Key Risks
[What could go wrong]

## Assessment
[Should a solo founder pursue this market?]
```

---

## Telegram Access Methods

### Method 1: Web Telegram (No API Required)
- Go to web.telegram.org
- Search for channel name
- View recent messages and member count
- Limited historical depth (~100 messages)

### Method 2: Telegram Bot API (With Bot Token)
```python
import telegram

bot = telegram.Bot(token="YOUR_BOT_TOKEN")
# Get updates from a channel (bot must be admin)
updates = bot.get_updates()
```

**Note:** A bot can only read messages if it's a member/admin of the channel.

### Method 3: Telegram Data Scraping (Third-Party)
Services like TGStat or Telegram Analytics provide channel statistics:
- Subscriber counts
- Growth rates
- Post reach
- Audience demographics

### Method 4: Community Directory
- t.me/erpnext (official channel)
- t.me/erpnext_jobs (job board)
- t.me/erpnext_freelancers (freelance market)
- t.me/erpnext_[country] (country-specific)

---

## Key Sources Per Region

### India
- Forum: discuss.frappe.io (search "india", "gst-india", "tally")
- Telegram: t.me/erpnext_india, t.me/erpnext_in, t.me/erpnext_freelance_india
- GitHub: resilient-tech/india-compliance, laxmantandon/express_tally
- Events: Frappeverse India (annual)
- Key partner: Resilient Software Services (Vadodara)

### Brazil
- GitHub: Intelligence8official/ERPNext_Brazil, techmaxsolucoes
- Telegram: t.me/erpnext_brazil
- Key repo: ERPNext_Brazil_NF (NF-e receive)
- Gap: NF-e emit (NOT built)

### Germany
- GitHub: alyf-de/erpnext_germany (80 stars)
- Telegram: t.me/erpnext_de, t.me/frappe_de
- Forum: discuss.frappe.io (German community)
- Gap: DATEV export (7+ years unsolved)

### MENA
- Telegram: t.me/erpnext_arabic (466 members), t.me/frappe_mena
- Country channels: UAE, Saudi, Egypt, Qatar, Kuwait, Oman, etc.
- Key mandate: Saudi ZATCA Phase 2/3 (active)

### Africa
- Telegram: t.me/erpnext_africa
- Key gap: Nigeria FIRS (deadline past, no solution)
- Events: Frappeverse Africa (annual)
- OHADA: 17 countries, zero ERPNext implementations

### China
- Gitee: yuzelin/erpnext_chinese (202 stars)
- GitHub: SolutionAlliance/erpnext_chinese
- Key gap: Fapiao management (NOT built)
- Infrastructure: Alibaba Cloud deployment

### Southeast Asia
- Telegram: t.me/erpnext_singapore, t.me/erpnext_vietnam, t.me/erpnext_thailand, t.me/erpnext_indonesia
- GitHub: agile-technica/erpnext-indonesia-localization (40 stars)
- Key mandates: Malaysia LHDN MyInvois (upcoming), Indonesia e-Faktur

### Latin America
- Telegram: t.me/erpnextmexico, t.me/erpnext_argentina, t.me/erpnext_colombia, t.me/erpnext_chile
- Key gaps: Mexico CFDI, Argentina AFIP, Colombia DIAN, Chile SII
- El Salvador: from corpus Topics 156731/156865

---

## Compliance Research Quick Reference

### E-Invoicing Mandates by Region

| Region | Key Countries | Mandate Status |
|--------|-------------|---------------|
| Europe | Belgium (PEPPOL Jan 2026), Germany (DATEV) | Active/Upcoming |
| MENA | Saudi (ZATCA Phase 3), UAE, Morocco | Active/Upcoming |
| Africa | Nigeria (FIRS past), Kenya (KRA upcoming) | Active/Upcoming |
| LatAm | Mexico (CFDI), Brazil (NF-e), Argentina | Active |
| Asia | India (active), Malaysia (upcoming), Indonesia | Active/Upcoming |

### Standard Accounting Frameworks

| Framework | Countries | ERPNext Support |
|-----------|-----------|----------------|
| OHADA | 17 African countries | ZERO implementations |
| DATEV | Germany, Austria | CSV export only |
| SPED | Brazil | Receive only, emit NOT built |
| SKR03/SKR04 | Germany | Partial JSON |
| Chart of Accounts | Most countries | Missing |

---

## Non-English Research Quality Notes

1. **Telegram channels provide community signals, not deep topic analysis** — member count and recent activity indicate market interest, but not specific pain points.

2. **GitHub stars are approximate indicators** — a repo with 50 stars indicates community interest, not necessarily market size.

3. **Compliance deadlines shift** — always verify with primary government sources before making business decisions.

4. **Pricing data is estimated** — implementation partner websites and job postings provide pricing signals, but actual market prices may vary.

5. **Language barriers** — non-English content (Chinese Gitee repos, Arabic Telegram channels) required translation or estimation.
