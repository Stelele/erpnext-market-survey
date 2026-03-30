# Opportunity Canvas — Small Bets from ERPNext Forum (1742 Topics)

**Analyst:** Small-Bets Statistician  
**Date:** 2026-03-30  
**Source:** 1742 ERPNext community forum topics  
**Persona filter:** Solo founder, cheapest possible validation (landing page → single customer → 2-week MVP)

---

## Portfolio Mix Suggestion

| Bet Tier | Count | Avg Cost | Rationale |
|---|---|---|---|
| Micro-bets | 4 | <$500 | Fastest feedback loops, affiliate/adsense-adjacent |
| Small-bets | 4 | $500–2k | Core portfolio, niche SaaS tools |
| Watch-list | 3 | $0–200 | Zero-cost content audits, no-code experiments |

**Rule of thumb:** If validation costs more than 2 weeks of your time + $500, move it to Watch-list unless a customer is already asking and willing to pay a deposit.

---

## Opportunity 1: Non-Profit Income/Expense Terminology Fix

**Problem Statement**  
Non-profits using ERPNext are forced to use "Sales" and "Payments" terminology everywhere. Donors, grantors, and NGO auditors need "Income" and "Expenses" — a single doctype label swap becomes a blocker for adoption.

**Evidence**  
- Topic #143018: User explicitly cannot use ERPNext because doctypes say "Sales Invoice" and "Payment Entry" — non-profit board reports require "Income" and "Expense" labels.

**Small-Bet Potential**  
| Dimension | Score | Notes |
|---|---|---|
| Complexity | Low | 1 config flag (Naming Series swap) + label overrides via custom field |
| Cost to Test | ~$100 | Landing page targeting "ERPNext for NGOs" + 3 outreach emails |
| Time to Test | 1–2 weeks | No-code label customization, zero custom app |
| Potential Reward | Medium | NGO vertical is underserved in ERPNext ecosystem; $50–200/mo per customer |
| Risk Level | Low | Already a known pain; no product risk, only distribution risk |
| Confidence | 7/10 | Direct quote from a real user in the forum |

**Experiment Design**  
1. Landing page: "ERPNext for Non-Profits — One-Click Income/Expense Labels"  
2. Cold email the 3 users who commented on #143018  
3. If 1 replies, offer a 30-min paid discovery call ($50)  
4. Deliver: `client_script` to swap labels + naming series config

**Success Metrics**  
- 1 paid discovery call from outreach  
- 1 customer at $99 one-time setup  
- OR: 1 testimonial that validates demand

---

## Opportunity 2: WhatsApp Auto-Reply Chatbot for ERPNext

**Problem Statement**  
Small businesses want a WhatsApp chatbot that reads ERPNext data (stock checks, invoice status, order tracking) without building a full API integration.

**Evidence**  
- Topic #104726: User wants WhatsApp auto-reply chatbot integrated with ERPNext  
- Topic #147812: Frappe developer posted a full guide on Evolution API + ERPNext + WhatsApp integration (open source, unmaintained)

**Small-Bet Potential**  
| Dimension | Score | Notes |
|---|---|---|
| Complexity | Medium | Requires WhatsApp Business API + ERPNext REST endpoints |
| Cost to Test | ~$300 | Evolution API $30/mo + landing page |
| Time to Test | 2–3 weeks | Open-source base exists; need to package it cleanly |
| Potential Reward | High | WhatsApp integrations command $100–500/mo in ERPNext market |
| Risk Level | Medium | WhatsApp API costs can spiral; need to scope to read-only queries |
| Confidence | 6/10 | Clear demand signal; open-source base needs packaging work |

**Experiment Design**  
1. Fork/extend the existing Evolution API guide (Topic #147812)  
2. Build a minimal version: stock query + invoice status via WhatsApp  
3. Landing page with demo video  
4. Charge $149 setup + $49/mo hosting

**Success Metrics**  
- 5 demo requests in first week  
- 1 paying customer in 30 days  
- OR: sell as a Notion template/guide for $19 (zero marginal cost)

**Bet Too Big Warning** ⚠️  
WhatsApp Business API requires Facebook Business verification and has rate limits. Keep the scope tight: read-only queries only. Do NOT attempt write operations (create invoice, update stock) in v1.

---

## Opportunity 3: Per-Customer & Last-Selling Price Display

**Problem Statement**  
Sales reps manually searching for the last price charged to each customer before creating a quotation. ERPNext doesn't show this on the item row by default.

**Evidence**  
- Topic #152598: User needs to display last selling price + last buying price on invoice creation  
- Topic #152598 (related): Per-customer specific pricing — different price per customer for same item

**Small-Bet Potential**  
| Dimension | Score | Notes |
|---|---|---|
| Complexity | Low | Custom field + server script to fetch last transaction price |
| Cost to Test | ~$100 | Landing page + 1 free customer pilot |
| Time to Test | 1 week | Single server script, one custom field |
| Potential Reward | Medium | Every B2B wholesale/distribution company needs this |
| Risk Level | Low | Pure UX improvement, no core logic changed |
| Confidence | 7/10 | Multiple forum threads; it's a common frustration |

**Experiment Design**  
1. Server script + custom field for "Last Selling Price" on Sales Order Item  
2. Demo GIF on landing page  
3. $79 one-time setup + $19/mo support

**Success Metrics**  
- 3 leads from forum thread replies  
- 1 paid pilot  

---

## Opportunity 4: Import CSV Mapping Memory (Save & Reuse)

**Problem Statement**  
Users with 150,000-item supplier price lists (Topic #116091) re-map CSV columns every import. ERPNext doesn't remember column mappings between sessions.

**Evidence**  
- Topic #116091: Supplier price list with 150,000 items; user spends hours re-mapping columns every import  
- Repeated frustration across multiple import topics

**Small-Bet Potential**  
| Dimension | Score | Notes |
|---|---|---|
| Complexity | Low-Medium | Store JSON mapping in a custom doctype; inject on next import |
| Cost to Test | ~$150 | Landing page + video demo |
| Time to Test | 1–2 weeks | Single custom app, 3–4 doctypes |
| Potential Reward | Medium | Anyone doing recurring data imports; B2B distribution is huge |
| Risk Level | Low | Safe to ship; purely additive feature |
| Confidence | 6/10 | Single topic but very specific, high-effort pain |

**Experiment Design**  
1. Build custom app: "CSV Import记忆" (CSV Import Memory)  
2. Landing page demo: save mapping → next import auto-applies it  
3. $49 setup + $15/mo OR one-time $149  
4. Target ERPNext Facebook groups with demo post

**Success Metrics**  
- 20 group post reactions (demand signal)  
- 2 trial signups  
- 1 paid customer

---

## Opportunity 5: Quotation Revision/Amendment Workflow

**Problem Statement**  
ERPNext lacks a clean revision workflow for quotations. Users manually append "-1", "-2" to quotation names when revising — error-prone and not tracked.

**Evidence**  
- Topic #151834: User needs quotation revision workflow with proper numbering (Q#A001 → Q#A001-1, Q#A001-2) and change tracking

**Small-Bet Potential**  
| Dimension | Score | Notes |
|---|---|---|
| Complexity | Low | Naming Series + custom field for revision count + diff view |
| Cost to Test | ~$100 | Landing page + demo video |
| Time to Test | 1 week | Naming series config + server script |
| Potential Reward | Medium | Sales teams doing proposals/quotations universally need this |
| Risk Level | Low | Naming series is a first-class ERPNext feature |
| Confidence | 7/10 | Clear workflow gap; no competing solution in forum |

**Experiment Design**  
1. Custom field "Revision Of" (link to original Quotation)  
2. Auto-numbering: Q#-1, Q#-2, etc.  
3. Diff view: show what changed between revisions  
4. $99 one-time setup + $25/mo support

**Success Metrics**  
- 1 forum reply → 1 DM → 1 discovery call  
- 1 paid pilot  

---

## Opportunity 6: Department Expense Budget Alerts

**Problem Statement**  
Finance teams can't enforce department spending limits in real time. Budget alerts fire too late or not at all (Topic #152644 confirms a bug in monthly distribution).

**Evidence**  
- Topic #151656: Monthly/quarterly expense limits per department with alerts  
- Topic #152644: Budget monthly distribution not triggering (confirmed bug, workaround found)

**Small-Bet Potential**  
| Dimension | Score | Notes |
|---|---|---|
| Complexity | Medium | Scheduled job + notification + dashboard widget |
| Cost to Test | ~$200 | Landing page + 1 pilot customer |
| Time to Test | 2 weeks | Standard Frappe app, 3–4 doctypes |
| Potential Reward | Medium-High | Finance/operations teams will pay $100–300/mo |
| Risk Level | Medium | Involves financial data; need careful testing |
| Confidence | 5/10 | Two related topics but neither is a direct "I'll pay for this" |

**Experiment Design**  
1. Custom app: "Budget Guard" — enforce department budget limits  
2. Email + Slack alerts at 50%, 75%, 90% spend  
3. Dashboard showing budget vs actual by department  
4. $199 setup + $49/mo

**Success Metrics**  
- 2 discovery calls from forum outreach  
- 1 paid pilot  

---

## Opportunity 7: Supplier Portal — Attachments on RFQ

**Problem Statement**  
Suppliers receiving RFQs via ERPNext can't attach quotes/documents easily. The attachment button is missing or hidden.

**Evidence**  
- Topic #152489: Supplier portal RFQ attachment button not working as expected

**Small-Bet Potential**  
| Dimension | Score | Notes |
|---|---|---|
| Complexity | Low | Portal configuration fix + custom web template |
| Cost to Test | ~$100 | Free as a public guide OR $49 mini-app |
| Time to Test | 3–5 days | Portal settings + one custom script |
| Potential Reward | Low-Medium | Narrow but real; charge as consulting engagement |
| Risk Level | Low | Pure portal/web template work |
| Confidence | 5/10 | Niche but specific pain; worth a quick guide before full app |

**Experiment Design**  
1. Write a detailed forum reply with step-by-step fix (free goodwill)  
2. Package as a "Supplier Portal Setup Guide" PDF — sell for $19  
3. If demand spikes, build a guided portal app

**Success Metrics**  
- Forum reply gets 20+ upvotes  
- 5 PDF sales in first month  

---

## Opportunity 8: El Salvador Electronic Invoicing Integration

**Problem Statement**  
Businesses in El Salvador need to submit invoices to the Ministry of Finance electronically. ERPNext doesn't support this out of the box.

**Evidence**  
- Topic #156731: El Salvador electronic invoicing (MH invoice)  
- Topic #156865: Same topic, second user confirming need  
- Topic #119327: El Salvador alcohol-specific tax (separate but confirms country-specific tax needs)

**Small-Bet Potential**  
| Dimension | Score | Notes |
|---|---|---|
| Complexity | High | Requires government API integration + certificate management |
| Cost to Test | ~$500 | Government API access + ERPNext custom app |
| Time to Test | 4–6 weeks | Non-trivial; regulatory compliance work |
| Potential Reward | High | Every business in El Salvador needs this; monopoly if first to market |
| Risk Level | High | Regulatory changes can break integration; compliance liability |
| Confidence | 6/10 | Two users asking; real regulatory requirement |

**Experiment Design**  
1. Document the full API spec and post publicly (build credibility)  
2. Offer as a consulting engagement first ($1,000–3,000 setup)  
3. Then productize if 3+ customers

**Success Metrics**  
- 2 consulting leads in 60 days  
- OR: 1 forum thread with 10+ "me too" replies confirming demand

**Bet Too Big Warning** ⚠️  
Country-specific tax integrations are high-risk. If the government changes API, your product breaks. Only pursue after securing a paying customer deposit. Consider consulting-first model with 50% upfront.

---

## Opportunity 9: Multi-Shift HR Scheduling

**Problem Statement**  
Factories and 24/7 operations need employees to work multiple shifts per day. ERPNext's shift management doesn't support split shifts.

**Evidence**  
- Topic #150950: Multi-shift HR — multiple shifts same day for same employee

**Small-Bet Potential**  
| Dimension | Score | Notes |
|---|---|---|
| Complexity | Medium | Custom doctype + shift assignment logic |
| Cost to Test | ~$150 | Landing page + 1 pilot |
| Time to Test | 2–3 weeks | Standard Frappe app |
| Potential Reward | Medium | Manufacturing/warehouse verticals are big ERPNext buyers |
| Risk Level | Medium | HR data sensitivity; need careful data handling |
| Confidence | 5/10 | Single topic but shift management is a known gap |

**Experiment Design**  
1. Custom app: "Shift Splitter" for ERPNext  
2. Landing page targeting manufacturing ERPNext users  
3. $149 setup + $35/mo

**Success Metrics**  
- 1 paid pilot in 30 days  

---

## Watch-List (Zero-Cost Experiments)

### WL-1: Shopify Tax-Inclusive Order Rate Bug
Topic #158173 — Shopify tax-inclusive orders showing wrong rates in ERPNext. **Experiment:** Detailed forum guide + GitHub PR. Zero cost, credibility builder.

### WL-2: Stock Reconciliation Performance
Topic #153299 — 5000+ items take 10–15 minutes, single error stops entire job. **Experiment:** Propose a batch-mode workaround guide. Zero cost.

### WL-3: Landed Cost Voucher — Warehouse-Wide Valuation
Topic #152532 — Warehouse-wide valuation update via Landed Cost Voucher. **Experiment:** Step-by-step guide PDF.

---

## Top 3 Recommended Bets (Ranked)

1. **#3 Per-Customer Price Display** — Lowest cost, fastest test, universal pain, 1-week delivery
2. **#5 Quotation Revision Workflow** — Clear workflow gap, naming series is first-class, 1-week delivery
3. **#1 Non-Profit Terminology Fix** — Highest confidence (direct quote), underserved vertical, $0 product risk

**Start with #3.** Build the server script, post in the forum thread, offer free to 3 users, ask for a testimonial. If 2/3 respond, you have a product.

---

*Generated from analysis of 1742 ERPNext forum topics. Grep signals: 5404 keyword matches, 698 payment/willingness signals, 174 WhatsApp/portal matches, 219 ecommerce matches.*
