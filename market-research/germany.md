# ERPNext Germany/DACH Market Research

**Date:** March 2026
**Market:** Germany, Austria, Switzerland (DACH) — high-cost, compliance-critical

---

## Community Infrastructure

| Platform | Channel | Activity |
|----------|---------|----------|
| Telegram | t.me/erpnext_de | German community |
| Telegram | t.me/frappe_de | Frappe Germany |
| Telegram | t.me/erpnext_austria | Austrian community |
| Telegram | t.me/erpnext_switzerland | Swiss community |
| Forum | discuss.frappe.io/c/community/german-community/50 | ~30+ threads |
| Wiki | doku.phamos.eu | German documentation |
| Event | German Chapter meetings | Historical (2019) |

**Official Frappe Partners in DACH:** 3 (all Germany)

---

## Market Fundamentals

### ERPNext Adoption
- **Estimated German users: <500 companies** (vs. millions using DATEV/Lexware)
- Largest documented: SEIBERT/MEDIA GmbH (150 employees, since 2018)
- Other: ESO Electronic (120 users, multi-country), K&K Software AG (27 users)
- <0.1% market share

### Dominant Competitors
- **DATEV**: €1.51 billion revenue (2024), 40,264 tax professional members, ~80% of German tax advisors use DATEV. Near-monopoly.
- **Lexware**: Haufe Group subsidiary, SMB market, ~€100M+ revenue, €15-100/month
- **Sevdesk**: ~€20M ARR, 50,000+ customers, modern SaaS
- **SAP Business One**: enterprise segment

---

## Compliance Requirements Assessment

### GoBD (Grundsätze zur ordnungsmäßigen Führung und Aufbewahrung von Büchern)

German requirements for proper accounting records:

| Requirement | ERPNext Status | Severity |
|-------------|---------------|----------|
| Unalterable records (Unveränderlichkeit) | ❌ NOT IMPLEMENTED | **Critical** |
| Complete audit trail | ⚠️ Partial | High |
| Tamper-proof storage | ❌ No cryptographic signing | **Critical** |
| Data integrity checks | ❌ No hash verification | High |
| Archival requirements | ⚠️ Export possible | Medium |

**Legal risk:** ERPNext allows editing submitted documents, violating GoBD's Unveränderlichkeit requirement.

### DATEV Integration — THE Critical Gap

DATEV dominates German accounting. 7+ years of community discussion, still not solved.

**Current state:**
- SKR04 JSON: partial (`alyf-de/SKR04`, 3 stars)
- SKR03 JSON: partial (`spritelite/SKR03`, 6 stars)
- DATEV CSV export: manual workarounds only
- DATEV XML/API: NOT IMPLEMENTED

**Timeline of community effort:**
- 2018: German Chapter formed, DATEV interest group initiated
- Dec 2018: Video conference to discuss DATEV compatibility
- 2019: SKR04/SKR03 JSON files created
- 2026: **Still no production DATEV integration**

**This 7+ year gap is a massive opportunity.** DATEV's format is documented. The missing piece is development investment.

**Approach:** Build a DATEV bridge that exports accounting data in CSV/XML format that German tax advisors can import. Tax advisors don't need ERPNext to be DATEV-native — they just need importable data.

### KassenSichV / TSE (Cash Register Security)

| Requirement | ERPNext Status |
|-------------|---------------|
| TSE (Technische Sicherheitseinrichtung) | ❌ NOT IMPLEMENTED |
| DSFinV-K Export | ❌ NOT IMPLEMENTED |
| Cash register serial numbers | ❌ NOT IMPLEMENTED |

Any German hospitality/retail business using ERPNext POS cannot comply with German law. Thread with 27 replies acknowledges this gap since 2020.

A developer (felix_will) announced in Jan 2024 they were implementing TSE with a certified provider.

### ELSTER Integration

German tax authority communication system. **No ERPNext-ELSTER integration exists.** DATEV, Lexware, and Sevdesk all offer native ELSTER.

### Other Gaps
- **Intrastat reporting:** NOT IMPLEMENTED
- **Zusammenfassende Meldung (ZM):** Basic report in `erpnext_germany`
- **German balance sheet formats (HGB §266, §275):** Not native
- **FinTS banking:** Archived repo (`jHetzer/erpnextfints`, 35 stars)

---

## German Localization

### Translation Status
- UI Translation: 70-80% coverage
- Business terminology: Inconsistent (mix of German/English)
- Accounting terms: Basic terms exist, professional terms missing
- Legal document formats: NOT IMPLEMENTED

### Key Apps

| App | GitHub | Stars | Purpose |
|-----|--------|-------|---------|
| `alyf-de/erpnext_germany` | github.com/alyf-de/erpnext_germany | 80 | Accounting reports, VAT, company registers |
| `libracore/erpnextswiss` | github.com/libracore/erpnextswiss | 95 | **Model for Germany** — banking, ZUGFeRD, EBICS |
| `alyf-de/gdpr` | github.com/alyf-de/gdpr | 5 | Data protection (archived) |
| `jHetzer/erpnextfints` | github.com/jHetzer/erpnextfints | 35 | Banking (archived) |

**Key insight:** `erpnextswiss` (Switzerland) is the model ERPNextGermany should follow. It includes CAMT bank imports, pain.001/008 payments, QR invoices, ZUGFeRD, and EBICS integration. Germany needs equivalent investment.

---

## Implementation Partners

| Company | Location | Role |
|---------|---------|------|
| **ALYF GmbH** | Germany | Primary German localization developer, DATEV work |
| **Phamos GmbH** | Germany | Bronze partner, documentation focus |
| **K&K Software AG** | Gerolzhofen | 21 years IT, active contributor |
| **SEIBERT/MEDIA GmbH** | Wiesbaden | 150 users, early adopter |
| **tüit GmbH** | Southern Germany | Co-sponsored SKR04 |
| **Itsdave** | Soltau | 7-person IT shop, 2017 production |
| **C4SAM** | Vienna, Austria | Cybersecurity startup |

---

## Opportunity Analysis

### OPP-DE-01: DATEV Bridge / Export
**Priority: CRITICAL** | **Confidence: 9/10**

The #1 blocker for German market adoption. 7+ years of demand, still not solved.

**What's needed:**
- DATEV-importable CSV/XML export
- SKR04/SKR03 account mapping with DATEV account numbers
- Automatic transaction categorization
- Export scheduling
- Compatible with DATEV Unternehmen Online import

**Build difficulty:** Medium. DATEV format is documented. Foundation (SKR04 JSON) exists.

**Pricing:**
- SaaS: €99-299/month
- One-time: €999-2,999 + €29/month support
- Target: German businesses paying €100-500/month to DATEV

**Competitive advantage:** ERPNext + DATEV bridge vs. full DATEV subscription (€100-500/month) = 70-80% cost savings.

---

### OPP-DE-02: GoBD Compliance Suite
**Priority: HIGH** | **Confidence: 8/10**

German businesses need legally compliant accounting records.

**What's needed:**
- Document locking after submission (Unveränderlichkeit)
- Cryptographic hash-chain integrity verification
- Audit log with tamper detection
- Compliance reports for tax advisors
- Export in auditable format

**Pricing:** €199-499/month or €2,000-5,000 one-time

---

### OPP-DE-03: ELSTER Connector
**Priority: HIGH** | **Confidence: 7/10**

Direct ERPNext-to-German-tax-authority submission.

**What's needed:** BZSt API integration for VAT declarations, income tax, trade tax.

**Build difficulty:** High (requires BZSt partnership/API access). 9-12 month project.

---

### OPP-DE-04: ERPNext KassenSuite DE (TSE/KassenSichV)
**Priority: HIGH** | **Confidence: 7/10**

German cash register compliance for hospitality/retail.

**What's needed:**
- TSE-integrated POS
- DSFinV-K export
- Legal receipt format
- Certified TSE provider integration

**Note:** felix_will is working on this (Jan 2024). Opportunity to partner or build alternative.

**Pricing:** €199-399/month SaaS including TSE service, or €2,000-5,000 + €50-100/month TSE.

---

### OPP-DE-05: German Translation Polish
**Priority: MEDIUM** | **Confidence: 7/10**

ERPNext's German translation is 70-80% complete but inconsistent.

**What's needed:**
- Professional accounting terminology review
- DIN 5008 document format
- German legal document templates
- Consistent field labels throughout

**Pricing:** Volunteer contribution via Weblate, or €5,000-15,000 for professional polish.

---

## New Personas Identified

1. **DATEV Prisoner** — German accountant/CFO locked into DATEV ecosystem. Their tax advisor only accepts DATEV format. High subscription costs, limited customization. Needs automated DATEV export.
2. **GoBD Compliant** — German GmbH needing legally defensible accounting records. Works with tax advisor who requires GoBD compliance. Needs document locking, audit trails, tamper-proof records.
3. **DSGVO Defender** — German privacy officer needing data subject request handling, retention policies, processing activity logging in ERPNext.
4. **KassenSichV Casualty** — German restaurant/retail owner wanting ERPNext POS but blocked by TSE requirements.
5. **ELSTER Evangelist** — German business owner frustrated with separate ELSTER submission process. Wants unified ERP-to-tax workflow.
