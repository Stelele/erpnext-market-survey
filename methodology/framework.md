# Opportunity Scoring Framework

**Purpose:** Aggregate independent persona assessments into ranked, comparable scores  
**Method:** Multi-persona scoring with aggregation rules and flag detection  
**Confidence level:** Tier 1 (9+ personas), Tier 2 (9 personas × batch), Tier 3 (9 personas × 18 opportunities)

---

## Overview

The scoring framework was applied in two contexts:

**Context 1 — Qualitative Synthesis (Tier 1 & 2):** 38 personas each produced a qualitative Opportunity Canvas. Opportunities were synthesized by reading all canvases and identifying convergence (which opportunities appeared across multiple independent personas) and divergence (which opportunities were controversial).

**Context 2 — Quantitative Scoring (Tier 3):** 9 personas each scored 18 Tier 3 opportunities 0-10 on relevant dimensions. Scores were aggregated into average, min, spread, and flag indicators.

---

## Scoring System

### Persona Selection for Quantitative Scoring

9 personas were selected for Tier 3 scoring based on their relevance to solo-founder opportunity evaluation:

| # | Persona | Dimension Measured |
|---|---------|-------------------|
| 1 | Stair-Step Market Sizer | Market size, TAM |
| 2 | Pre-Sale Interrogator | Willingness to pay |
| 3 | Vanity Rejector | Revenue potential vs. feature-request noise |
| 4 | Boring-is-Profitable Founder | Recurring revenue, steady demand |
| 5 | Speed-First Concierge | Build time, solo-founder viability |
| 6 | Small Bets Statistician | Risk-adjusted return |
| 7 | Founder Fit Analyzer | Solo-founder fit, no local partner needed |
| 8 | Agnostic Stack Founder | ERPNext-specific lock-in |
| 9 | Exit Planner | Acqui-hire value, M&A attractiveness |

### Scoring Scale

Each persona scored each opportunity 0-10 on their primary dimension:

| Score | Meaning |
|-------|---------|
| 0-2 | Red flag — serious concern on this dimension |
| 3-4 | Below average — notable concern |
| 5 | Baseline — neutral, neither strong nor weak |
| 6-7 | Above average — solid on this dimension |
| 8-9 | Strong — notable strength |
| 10 | Exceptional — this dimension is a standout feature |

### Scoring Rules

1. **Base score starts at 5/10** — neutral default
2. **Each persona adjusts +/- 2-3 points** based on their analytical lens
3. **Min score < 3 triggers REJECT flag** — red flag indicator
4. **Spread (max - min) > 5 triggers DIVIDED flag** — controversial
5. **Solo-founder rank** assigned within batch (1 = best within batch of 4-5 opportunities)

### Scoring Example

```
Opp 22 (App Upgrade Service) scored by 9 personas:

market_sizer: 8   (+3 from base — v15→v16 is happening NOW)
pre_sale:    7   (+2 — $1K-5K per migration)
vanity:      8   (+3 — recurring, high engagement)
boring:      8   (+3 — consulting is boring/steady)
speed:       8   (+3 — 1-3 days per app audit)
small_bets:  5   (0 — lumpy revenue, not small bets)
founder_fit: 8   (+3 — solo-viable, consulting)
agnostic:    4   (-1 — ERPNext-specific, no lock-in)
exit:        2   (-3 — service business, poor exit)

Average: 6.40
Min: 2 (exit)
Max: 8
Spread: 6 (8 - 2)
Flag: DIVIDED (spread > 5)
Solo-rank: 1 (within batch)
```

---

## Aggregation Rules

### Primary Metrics

| Metric | Formula | Threshold | Meaning |
|--------|---------|----------|---------|
| **Average** | Mean of all 9 persona scores | > 6.5 = Tier 1 candidate |
| **Min** | Minimum score across all personas | < 3 = REJECT flag |
| **Max** | Maximum score across all personas | — | Strongest persona endorsement |
| **Spread** | Max - Min | > 5 = DIVIDED flag |
| **Solo-rank** | Rank within batch (1-4 or 1-5) | 1 = best within batch |

### Confidence Thresholds

| Average Score | Confidence Band | Interpretation |
|--------------|---------------|---------------|
| 8.0 - 10.0 | Very High | Near-unanimous endorsement |
| 7.0 - 7.9 | High | Strong consensus with minor concerns |
| 6.0 - 6.9 | Medium-High | Generally positive, some disagreement |
| 5.0 - 5.9 | Medium | Mixed signals, proceed with caution |
| 4.0 - 4.9 | Low-Medium | Notable concerns, below average |
| < 4.0 | Low | Significant red flags across personas |

### Flag Rules

| Flag | Condition | Action |
|------|-----------|---------|
| **REJECT** | Min score < 3 | Do not pursue without addressing the red flag dimension |
| **DIVIDED** | Spread > 5 | Controversial — validate with additional personas or primary research |
| **FLAT** | All scores within 1 point of each other | No differentiation — opportunity is mediocre on all dimensions |
| **PEAKED** | One score 8+, rest < 5 | One persona loves it, rest reject — investigate why |

---

## Tier Definitions

| Tier | Definition | Scoring Method | Examples |
|------|-----------|---------------|---------|
| **Tier 1** | Top opportunities with strong cross-persona agreement | Qualitative synthesis (38 personas) | OPP-001 Demo/Seed Data, OPP-002 Invoice OCR |
| **Tier 2** | High-value opportunities with partial validation | Qualitative synthesis (38 personas) | OPP-009 WhatsApp AI Hub, OPP-014 DB Recovery |
| **Tier 3** | Niche opportunities needing comparison | Quantitative scoring (9 personas × 18 opps) | OPP-16 through OPP-33 |
| **Rejected** | Opportunities flagged REJECT or insufficient signal | Persona red flags | Generic automation builder, Zone 7/8 as subscriptions |

---

## Scoring Batch Structure

Tier 3 scoring was organized into parallel batches of 4-5 opportunities each:

**Batch 1 (Opp 16-19):**
- Manufacturing Click-Reduction
- AR Collections
- Vertical Starter Packs
- Managed Hosting

**Batch 2 (Opp 20-23):**
- Non-Profit Terminology
- Role-Based Sidebar
- App Upgrade Service
- Quotation Revision

**Batch 3 (Opp 24-28):**
- Last-Selling Price
- Work Order Auto-Scheduling
- AI Localization
- Multi-Company Setup
- E-Commerce Cart Bug

**Batch 4 (Opp 29-33):**
- Lending Module
- Healthcare Booking
- HR Multi-Shift
- Supplier Portal RFQ
- El Salvador E-Invoice

Each batch was scored independently, then all 18 were ranked by average score across the full set.

---

## Final Rankings (Tier 3)

| Rank | Opportunity | Average | Min | Spread | Flags |
|------|-----------|---------|-----|--------|-------|
| 1 | AI Localization | 6.89 | 5 | 3 | — |
| 2 | App Upgrade Service | 6.40 | 2 | 6 | DIVIDED |
| 3 | Role-Based Sidebar | 5.90 | 3 | 6 | DIVIDED |
| 4 | Non-Profit Terminology | 5.80 | 3 | 6 | DIVIDED |
| 5 | Lending Module | 5.80 | 4 | 3 | — |
| 6 | Work Order Auto-Scheduling | 5.67 | 4 | 4 | — |
| 7 | Last-Selling Price | 5.67 | 3 | 5 | DIVIDED |
| 8 | AR Collections | 5.30 | 3 | 5 | DIVIDED |
| 9 | HR Multi-Shift | 5.30 | 4 | 3 | — |
| 10 | Manufacturing Click-Reduction | 5.20 | 3 | 4 | — |
| 11 | E-Commerce Cart Bug | 5.22 | 2 | 6 | DIVIDED |
| 12 | Vertical Starter Packs | 5.20 | 4 | 3 | — |
| 13 | El Salvador E-Invoice | 5.60 | 3 | 5 | DIVIDED |
| 14 | Supplier Portal RFQ | 5.60 | 3 | 5 | DIVIDED |
| 15 | Healthcare Booking | 5.10 | 4 | 3 | — |
| 16 | Managed Hosting | 4.60 | 3 | 4 | — |
| 17 | Quotation Revision | 4.80 | 2 | 7 | DIVIDED |
| 18 | Multi-Company Setup | 4.11 | 2 | 5 | REJECT, DIVIDED |

---

## Cross-Persona Agreement Analysis

### Most Agreed Opportunities

| Opportunity | Personas Agreeing | Interpretation |
|------------|-----------------|---------------|
| Demo/Seed Data | 6 | Highest cross-persona agreement in entire corpus |
| Migration Toolkit (Tally) | 5 | Strong consensus on India market |
| Compliance Packs | 4 | Compliance urgency recognized broadly |
| Invoice OCR Pipeline | 3 | Strong data flywheel signal |
| WhatsApp AI Hub | 4 | Communication gap well understood |

### Most Disagreed Opportunities

| Opportunity | Lowest | Highest | Spread | Interpretation |
|------------|--------|---------|--------|---------------|
| App Upgrade Service | 2 (Exit) | 8 (Market Sizer) | 6 | Service vs. product divide |
| E-Commerce Cart Bug | 2 (Exit/Agnostic) | 8 (Vanity) | 6 | Speed vs. sustainability |
| Quotation Revision | 2 (Exit) | 9 (Speed) | 7 | Fast build vs. no exit |

**Key insight:** The biggest persona disagreements were consistently between Speed-First Concierge (rates fast-build opportunities at 8-9) and Exit Planner (rates ERPNext-specific bug fixes at 2-3). This reflects the solo-founder tension between speed and long-term asset building.

---

## Confidence Calibration

The confidence scores in the synthesis reflect:

| Score | Evidence Standard |
|-------|-----------------|
| 10/10 | Explicit money on the table (e.g., "$5,000 offer" in Topic 150923). Zero personas rejected. |
| 9/10 | Multiple independent WTP signals. Strong forum engagement. No significant red flags. |
| 8/10 | Reasonable WTP signals. Active community interest. Some concerns but addressable. |
| 7/10 | Moderate WTP signals. Forum discussions present. Some competition or complexity. |
| 6/10 | Weak WTP signals. Niche appeal. More validation needed. |
| < 6/10 | Insufficient signals. Proceed only with primary research. |

---

## Framework Limitations

1. **Persona selection matters:** The 9 personas chosen for Tier 3 scoring bias the results toward solo-founder viability and exit potential. Different personas would produce different rankings.

2. **Ordinal scoring is coarse:** 0-10 scoring with only 9 data points produces noisy averages. A 6.4 vs. 6.3 average difference is not statistically meaningful.

3. **Weighted scoring was not applied:** All personas were weighted equally. In practice, Pre-Sale Interrogator's WTP score might deserve 2x weight compared to Exit Planner's exit score for a founder who doesn't care about exit.

4. **Context not captured:** A 7/10 for "speed" from Speed-First Concierge and a 7/10 for "exit" from Exit Planner are both scored 7 but have very different implications.

5. **REJECT is too strict:** The REJECT flag (min < 3) only triggered on 2 of 18 Tier 3 opportunities. A more nuanced "concern" indicator (min < 4) would surface more actionable flags.

6. **Solo-rank is relative:** Solo-rank is within-batch only. An opportunity ranked 4th out of 5 in a weak batch might still score higher than an opportunity ranked 1st in a strong batch.

---

## Using This Framework for New Opportunities

To score a new opportunity not in the synthesis:

1. **Select 5-9 personas** relevant to your situation (e.g., Pre-Sale Interrogator + Speed-First Concierge + Exit Planner if you care about exit, or Pre-Sale Interrogator + Speed-First Concierge + Founder Fit Analyzer if you're solo)
2. **Provide each persona with** the opportunity description and persona definition
3. **Have each persona score 0-10** on their primary dimension
4. **Calculate average, min, spread**
5. **Apply flags:** REJECT if min < 3, DIVIDED if spread > 5
6. **Compare to synthesis benchmarks:** An opportunity scoring 7+ average with no REJECT flags is comparable to Tier 1/2. 5-7 average is Tier 3. < 5 average needs primary research before pursuing.
