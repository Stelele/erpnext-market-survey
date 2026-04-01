# Research Methodology: Overview

**Corpus:** 1,742 Frappe Forum topics + 1,304 bootstrapper transcripts + 8 non-English market research streams  
**Personas:** 46 independent analytical frameworks  
**Date:** March 2026  
**End buyer assumption:** Solo founder / micro-SaaS builder

---

## Research Objective

The objective was to identify paid business opportunities within the ERPNext/Frappe ecosystem using a structured, persona-driven research methodology. Unlike a typical forum analysis, this project used **independent analytical personas** — each representing a distinct bootstrapped founder methodology — to read the same corpus and surface opportunities from different angles. The hypothesis was that no single analytical lens would capture all opportunities; cross-persona agreement would signal high-confidence opportunities; and cross-persona disagreement would reveal controversial or risky bets.

---

## Phase 1: Discovery

### Objective
Have 38 independent personas each read all 1,742 forum topics and produce an Opportunity Canvas identifying paid pain points, evidence (topic IDs), customer type, WTP signals, competitors, pricing hints, red flags, and confidence.

### Approach

**Step 1 — Persona definition.** Each persona was defined as a markdown file in `research-personas/` with: a description of the founder archetype, their discovery triggers (what signals they look for), their validation threshold (what makes them say "yes, build this"), their red flags (what makes them say "no, avoid this"), and their ERPNext ecosystem lens (how they apply their methodology specifically to ERPNext).

Personas were drawn from three sources:
- **MicroConf transcript corpus:** 486 YouTube video transcript files covering bootstrapped founder tactics, strategy, and philosophy
- **Rob Walling transcript corpus:** 486 YouTube video transcript files covering SaaS growth, pricing, sales, and validation
- **The Bootstrapped Founder corpus:** 332 episode transcript files covering modern bootstrapping, AI, community, and mental models

Primary extraction was from **16 fully summarized transcripts** (`bootstrappers/summaries.md`). The full corpus was then read in rounds to cross-validate and refine persona definitions.

38 personas were created across 6 categories:

| Category | Count | Purpose |
|----------|-------|---------|
| Validation personas | 6 | Finding and validating problems |
| Execution personas | 13 | Building and shipping |
| Psychology personas | 5 | Managing the founder's mind |
| Strategy personas | 7 | Positioning and protecting the business |
| Marketing personas | 7 | Reaching and converting customers |
| Regional personas | 8 | Non-English market analysis |

**Step 2 — Forum corpus preparation.** All 1,742 topics from discuss.frappe.io were downloaded as JSON files and stored in `erpnext-forum/topics/`. Each topic file contained: topic ID, title, author, creation date, view count, like count, reply count, tags, and the full text content of the first post.

**Step 3 — Parallel subagent execution.** Each persona was assigned to an independent subagent. Subagents were given:
- The persona definition file to read
- All 1,742 topic files to analyze
- Instructions to produce an Opportunity Canvas

Subagents ran in batches of 4-8 in parallel to maximize throughput. Each subagent read the persona file first, then consumed the full corpus, then wrote their Opportunity Canvas to `persona-outputs/[persona-name].md`.

**Step 4 — Canvas output.** Each canvas contained:
- Top 3-5 opportunities identified by that persona
- Evidence: specific topic IDs and quotes from the forum
- Customer type: who would pay for this
- WTP signals: what indicated willingness to pay
- Competitors: what alternatives exist
- Pricing hints: what the market appears to bear
- Red flags: what could kill this opportunity
- Confidence: self-assessed 0-10

**Phase 1 outcome:** 38 Opportunity Canvases in `persona-outputs/`. 4 subagents required resumption due to token limits. No canvas was skipped — all 38 were eventually completed.

---

## Phase 2: Strategic Validation

### Objective
Have 7 strategic personas evaluate the Phase 1 outputs — assessing moat strength, exit potential, macro waves, compounding assets, and vertical specialization.

### Approach

The 7 strategic personas were:
1. **Wave Catcher** — spots macro shifts before they become obvious (regulatory deadlines, technology transitions)
2. **Moat Architect** — evaluates competitive moats from day one
3. **Castle Builder** — owns what compounds, rents what depreciates
4. **Exit Planner** — designs for sellability from day one
5. **Constraints Navigator** — turns resource limits into creative advantages
6. **Data Flywheel Founder** — identifies data as compounding moat from day one
7. **Vertical SaaS Specialist** — deliberately serves industry-specific niches

Each strategic persona was given all 38 Phase 1 canvases to read, then produced a strategic assessment covering:
- Moat evaluation: is this defensible?
- Exit potential: would an acquirer pay for this?
- Macro waves: is this riding a rising tide?
- Compounding assets: does this get better over time?
- Vertical focus: should this be narrowed?

Phase 2 outputs were written to `persona-outputs/` alongside Phase 1 outputs.

---

## Phase 3: Master Synthesis

### Objective
Cross-reference all persona outputs against the 8 pre-built opportunity zones, produce a ranked master opportunity list, and validate or reject each zone.

### Approach

**Step 1 — Zone validation.** Each of the 8 pre-built opportunity zones from `research-personas/synthesis.md` was evaluated against all persona outputs. Zones were marked as VALIDATED, PARTIALLY VALIDATED, or NOT VALIDATED.

**Step 2 — Tier 1 & 2 profiling.** The top 8 opportunities were written as detailed profiles in `synthesis/master-synthesis.md`, each containing: what it solves, strongest evidence in corpus, customer type, pricing model, why it's a moat, red flags, and build path.

**Step 3 — Tier 3 scoring.** All 18 Tier 3 niche opportunities were scored by 9 personas (Stair-Step Market Sizer, Pre-Sale Interrogator, Vanity Rejector, Boring-is-Profitable Founder, Speed-First Concierge, Small Bets Statistician, Founder Fit Analyzer, Agnostic Stack Founder, Exit Planner). Each persona scored each opportunity 0-10 on relevant dimensions.

Scoring was aggregated into:
- **Average score** (across 9 personas)
- **Min score** (red flag if < 3)
- **Max-min spread** (consensus indicator, flagged if > 5 = DIVIDED)
- **Solo-founder rank** within batch

**Step 4 — Priority matrix.** All opportunities were mapped onto a solo-founder priority matrix: Quick Wins (1-2 week builds), Medium Builds (2-4 weeks), Strategic (1-3 months), and Avoid.

**Step 5 — Synthesis write.** `synthesis/master-synthesis.md` was written as the primary deliverable, containing all of the above plus rejected opportunities, the four compounding assets, highest WTP signals, and persona agreement analysis.

---

## Phase 4: Non-English Market Expansion

### Objective
Branch out from the English-only forum corpus to identify opportunities in non-English ERPNext markets.

### Approach

**Step 1 — Community mapping.** Before researching specific markets, a community mapping phase identified all non-English ERPNext communities. This found 50+ country-specific Telegram channels, GitHub localization repositories, and the frappe.io partner directory.

Key Telegram channels discovered:
- 7 India-specific channels (t.me/erpnext_india, t.me/erpnext_freelance_india, etc.)
- 12+ MENA channels (Arabic, UAE, Saudi, Egypt, etc.)
- Brazil, Germany, France, China, Vietnam, Thailand, Indonesia, Mexico, Argentina, Colombia, Chile, Nigeria, Kenya, South Africa, Francophone Africa, and many more

**Step 2 — Parallel market research.** 8 research streams ran in parallel, one per region:

1. **India** — Tally migration (broken built-in tool), Multi-GSTIN accounting, GST compliance, India Compliance app gaps
2. **MENA** — Saudi ZATCA e-invoicing Phase 2/3, Arabic RTL print, UAE VAT, Islamic finance
3. **Brazil** — NF-e emission (hard blocker), SPED export, Brazilian tax calculation engine
4. **Germany** — DATEV bridge (7+ years unsolved), GoBD compliance, KassenSichV/TSE
5. **Africa** — Nigeria FIRS (deadline passed), OHADA accounting (17 countries), Kenya KRA, South Africa SARS
6. **China** — Fapiao management, Alibaba Cloud deployment, WeChat integration
7. **Southeast Asia** — Malaysia LHDN e-invoicing, Indonesia e-Faktur, Singapore GST, Vietnam
8. **Latin America** — Mexico CFDI, Argentina AFIP, Colombia DIAN, Chile SII, Peru SUNAT

Each stream used web searches, GitHub repository analysis, and Telegram community research to surface:
- What compliance requirements exist
- What ERPNext support exists (if any)
- What gaps remain unaddressed
- What willingness-to-pay signals exist

**Step 3 — New persona creation.** 8 regional personas were created based on market-specific archetypes:
- Tally Survivor (India)
- DATEV Prisoner (Germany)
- FIRS Deadline Fighter (Nigeria)
- SPED Compliance Navigator (Brazil)
- Totvs Escape Artist (Brazil)
- Arabic Digital Transformer (MENA)
- GoBD Compliant (Germany)
- Mandate Chaser (Global)

**Step 4 — Market reports.** 8 market reports were written to `market-research/` covering each region's opportunities, compliance requirements, GitHub repos, Telegram communities, and strategic recommendations.

**Step 5 — Synthesis integration.** The non-English market findings were integrated into `synthesis/master-synthesis.md` as a new section covering the global market opportunity map, mandate calendar, and cross-market patterns.

---

## Research Limitations

1. **English-only forum bias:** discuss.frappe.io is the primary corpus, which skews toward English-speaking users. India, China, Brazil, and other non-English markets are underrepresented in the forum data, though India-specific signals were detectable through forum content.

2. **Telegram communities not in corpus:** 50+ country-specific Telegram channels exist but were not included in the forum topic corpus. Non-English opportunity signals may be undercounted. Phase 4 partially addressed this via web research.

3. **Corpus date:** Forum topics were captured up to March 2026. Compliance deadlines (Nigeria FIRS, Saudi ZATCA Phase 3, Belgium PEPPOL January 2026) may have shifted since capture.

4. **No primary research validation:** The synthesis recommends interviewing ERPNext implementers and monitoring Telegram channels to validate WTP with actual transaction volume. This was not conducted.

5. **Solo-founder bias:** The end-buyer assumption was explicitly a solo founder. Some opportunities (e.g., Brazil NF-e emission, China Fapiao) require local compliance expertise and may not be solo-viable.

6. **Persona coverage:** 38 personas is a large number but represents a subset of possible analytical lenses. Founder personas from non-Western markets, specific industry verticals, and technicalspecialties were not modeled.

---

## What Worked

- **Parallel subagent execution** maximized throughput — 38 personas completed in a fraction of sequential time.
- **Independent analysis before synthesis** preserved dissenting views — Pre-Sale Interrogator rejected Zone 7/8 as subscription products while Speed-First Concierge validated them as concierge services. Both views were preserved.
- **Multi-persona scoring** (9 personas × 18 Tier 3 opportunities) produced nuanced rankings where consensus and controversy were both visible.
- **Regional personas** (8 new) validated that non-English markets have fundamentally different opportunity structures than the English-speaking market.

## What Didn't Work

- **4 subagents got stuck** during Phase 1 and required manual resumption. Stair-step-market-sizer, boring-is-profitable-founder, trust-architect, productive-procrastinator, and freelance-pivot-builder all required task resumption.
- **Tier 3 scoring required 4 sequential batches** rather than parallel — the 9-persona × 18-opportunity scoring was too large for a single subagent context window.
- **Nigeria FIRS warning was issued but nobody built it** — the research identified the FIRS deadline as critical but no solution was built before the deadline passed. This is the cautionary tale for all compliance opportunities: identify early, build early.

---

## Output Summary

| Phase | Output | Count |
|-------|--------|-------|
| Phase 1 | Opportunity Canvases | 38 |
| Phase 2 | Strategic Assessments | 7 |
| Phase 3 | Master Synthesis | 1 |
| Phase 3 | Tier 3 Rankings | 18 scored, 18 ranked |
| Phase 4 | Market Reports | 8 |
| Phase 4 | Regional Personas | 8 |
| **Total** | | **80 outputs** |

**Primary deliverable:** `synthesis/master-synthesis.md`
**Replication guide:** `methodology/replication-guide.md`
**Full persona library:** `research-personas/`
