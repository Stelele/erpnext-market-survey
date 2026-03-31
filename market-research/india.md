# ERPNext India Market Research

**Corpus:** Web research + existing corpus (582 India matches in detailed_topics.json)
**Date:** March 2026
**Market:** India — largest non-English ERPNext market

---

## Community Infrastructure

| Platform | Channel/Group | URL | Activity |
|----------|--------------|-----|----------|
| Telegram | ERPNext India | t.me/erpnext_india | Very High |
| Telegram | ERPNext India (alt) | t.me/erpnext_in | Very High |
| Telegram | ERPNext India Jobs | t.me/erpnext_india_jobs | High |
| Telegram | ERPNext Freelance India | t.me/erpnext_freelance_india | High |
| Telegram | ERPNext Partner India | t.me/erpnext_partner_india | Medium |
| Telegram | ERPNext Implementor India | t.me/erpnext_implementor_india | Medium |
| Telegram | ERPNext India (Hybrowlabs) | t.me/erpnext_hybro | High |
| Forum | discuss.frappe.io | discuss.frappe.io | High (582 India matches) |
| Event | Frappeverse India 2025 | September 11-12, 2025 | Major annual conference |
| Event | Frappeverse Africa | Community cross-pollination | Growing |

**Key community leaders:** Hybrowlabs (paid courses), Resilient Software Services (Vadodara, Gujarat — India Compliance app maintainers)

---

## India Market Fundamentals

### Dominant Competitors (Switching FROM)
- **Tally** — ~10M+ users, dominant in SMB/mid-market accounting. THE accounting software of India.
- **Zoho Books** — growing SaaS competitor, strong India presence
- **Busy** — mid-market, Windows-based
- **QuickBooks India** — limited penetration
- **SAP Business One** — enterprise
- **Tally Prime** — latest version, subscription model, price hike driving migration interest

### ERPNext India Adoption
- Concentrated in: tech startups, manufacturing, trading companies, and companies with international operations
- SMB adoption increasing but Tally dependency is the biggest blocker
- Implementation partners: 7+ active on Telegram, plus Resilient Software (official partner)

### Key Events
- **Frappeverse India 2025** (September): 160+ attendees, community awards, workshops
- India Compliance app (`resilient-tech/india-compliance`) — maintained by Resilient Software Services LLP

---

## Opportunity Analysis

### OPP-IN-01: Tally → ERPNext Migration Toolkit
**Priority: CRITICAL** | **Confidence: 10/10**

Tally is THE dominant accounting software in India (~10M+ users). The built-in Tally migration tool is **broken since v13/v15** (Topic 83499, 4,789 views — highest engagement migration topic in entire corpus).

**What exists:**
- `express_tally` (GitHub: laxmantandon/express_tally) — unmaintained since 2022, "likely dead"
- Community workarounds: manual data entry, custom CSV imports
- Forum posts from 2024 still referencing broken migration

**What's needed:**
- Working Tally to ERPNext data migrator (ledgers, vouchers, inventory, GST data)
- Tally 9 / Tally Prime compatibility
- Chart of accounts mapping with GST states
- Opening balance preservation
- Voucher/transaction history migration

**Build difficulty:** Medium. Tally data format is proprietary but partially reverse-engineered. Requires India-specific accounting knowledge.

**Pricing:** $500-3,000 per migration + toolkit licensing. Consulting engagements: $175-600 per moderate project.

**WTP signals:**
- 4,789 views on Topic 83499 (broken tool)
- 20+ migration-relevant topics across corpus
- Freelance projects advertised on ERPNext India Telegram channels

**Competitors:** None with working product. Local implementation partners doing custom migrations manually.

---

### OPP-IN-02: Multi-GSTIN Multi-State Accounting Solution
**Priority: HIGH** | **Confidence: 9/10**

Indian companies operating across multiple states need separate GST registrations per state. ERPNext's India Compliance app doesn't support state-wise GST accounts natively.

**Evidence:**
- Topic 160127: "Single company with multiple GSTIN setup" — active Feb-March 2026
- Topic 153619: "E-Waybill for Internal Transfers" — feature request
- Topic 161555: "ISD (Input Service Distributor) Invoice Support" — under development

**What's needed:**
- Per-GSTIN party (supplier/customer) management with state-wise addresses
- State-wise tax ledgers
- GST Payment tracking by state
- GSTR-2A/2B reconciliation by GSTIN
- ISD invoice support (input service distributor)

**Build difficulty:** High. Requires deep India tax law knowledge.

**Pricing:** $500-2,000 setup + $100-300/month support

---

### OPP-IN-03: TDS Catch-Up Automation
**Priority: HIGH** | **Confidence: 8/10**

When companies go-live mid-financial-year, they need TDS (Tax Deducted at Source) entries for prior months. ERPNext won't create backdated TDS Journal Entries.

**Evidence:** Active forum pain point. No good workaround exists.

**What's needed:** Automated TDS catch-up journal entries for April-September, triggered on mid-year go-live.

**Pricing:** $200-500 one-time + included in implementation engagements

---

### OPP-IN-04: E-Waybill for Internal Transfers
**Priority: MEDIUM** | **Confidence: 7/10**

ERPNext India Compliance doesn't generate e-waybills for internal stock transfers between branches. Topic 153619 documents this gap.

**What's needed:** E-waybill generation for internal transfers, sub-contracting scenarios.

---

### OPP-IN-05: Indian Vertical Seed Data Packs
**Priority: HIGH** | **Confidence: 9/10**

Extension of OPP-001 (Demo/Seed Data Generator) for Indian verticals:
- Indian trading company with GST states, Tally chart of accounts
- Indian manufacturing plant with GST rates, HSN codes
- Indian kirana store with GST-compliant price lists
- Indian pharmacy with batch/expiry tracking, HSN codes

**Evidence:** ERPgulf proved regional demand with Saudi Riyal seed data. Same model applies to India.

---

## India-Specific GitHub Repos

| Repo | Focus | Stars | Last Update |
|------|-------|-------|-------------|
| `resilient-tech/india-compliance` | GST, E-invoice, E-waybill core | Active | Ongoing |
| `laxmantandon/express_tally` | Tally migration (broken) | - | 2022 |
| `resilient-tech/gst_erpnext` | Legacy GST app | - | - |

---

## Hindi/Regional Language Gaps

- ERPNext Hindi translation: partial, community-maintained
- Regional languages (Tamil, Telugu, Bengali, Marathi): minimal coverage
- LLM-powered translation: proven viable (Topic 157758)
- **Opportunity:** Hindi ERPNext UI — large market, real adoption blocker

---

## Implementation Pricing (India Market)

| Service | Price Range |
|---------|-------------|
| ERPNext setup + training | ₹1,00,000-3,00,000 ($1,200-3,600) |
| Tally migration (manual, current) | ₹25,000-1,00,000 ($300-1,200) |
| GST compliance setup | ₹50,000-2,00,000 ($600-2,400) |
| Custom app development | ₹5,000-15,000/day ($60-180/day) |
| Monthly support | ₹5,000-25,000/month ($60-300/month) |

---

## Competitive Landscape

- Resilient Software Services: India Compliance maintainers, full-service
- Hybrowlabs: ERPNext training courses, consulting
- Freelance market: active on Telegram channels
- No focused Tally migration product exists

---

## Key Risks

1. **Tally is deeply embedded** — switching cost is real, not just technical
2. **India tax law changes frequently** — compliance apps need constant updates
3. **Price sensitivity** — Indian market is price-sensitive; $500/mo SaaS may be too expensive for many SMBs
4. **Local competition** — implementation partners will resist products that cannibalize their consulting revenue

---

## New Personas Identified

1. **Tally Survivor** — Indian accountant who has used Tally for 10+ years, resistant to change but frustrated by price hikes and limited features
2. **GST Warrior** — Indian compliance specialist obsessed with India's complex tax system (GST, TDS, TCS, E-waybill)
3. **SMB Localizer** — serving small Indian businesses with Hindi UI, regional language support, and Tally-style UX familiarity
