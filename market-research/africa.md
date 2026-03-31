# ERPNext Africa Market Research

**Date:** March 2026
**Market:** Africa — massive untapped opportunity, zero comprehensive localization

---

## Community Infrastructure

| Platform | Channel | Activity |
|----------|---------|----------|
| Telegram | t.me/erpnext_africa | Pan-African community |
| Telegram | t.me/frappeuganda | Early African community |
| Event | Frappeverse Africa 2025 | 160+ attendees, 8 sponsors |
| Event | Frappeverse Africa 2026 | March 5, 2026, Kenya School of Government |
| Forum | discuss.frappe.io | Africa-tagged discussions |

**Key community leaders:** Navari (Kenya), Aakvatech (localization), Frappe Club — Chipo Hameja, Arnold Muwanguzi (capacity building)

**Official Frappe Partners in Africa:**
- Tanzania: 4 partners (most)
- Kenya: 3 partners
- Congo (DRC): 1
- Ghana: 1
- Mauritius: 1
- Uganda: 1
- **Nigeria: 0** — CRITICAL GAP
- **South Africa: 0** — CRITICAL GAP
- **Francophone Africa: 0** — CRITICAL GAP

---

## Country-by-Country Analysis

### Nigeria — CRITICAL PRIORITY (OPP-AF-01)
**Largest economy in Africa: ~$450B GDP, 220M+ population**

**FIRS E-Invoicing:**
- ERPNext is **NOT** on FIRS supported ERP list
- No active development found on GitHub for FIRS integration
- `erpnext_payroll_nigeria` (GitHub): last updated March 2022 (4 years old)
- No FIRS e-invoice integration whatsoever

**What's needed:**
1. FIRS e-Invoice API integration (mandatory compliance)
2. TIN (Tax Identification Number) validation
3. Nigerian VAT 7.5% handling
4. Withholding Tax (WHT) calculations
5. Naira (NGN) currency precision
6. Nigerian chart of accounts template
7. Bank integrations (GTBank, Access Bank, UBA, Zenith Bank)

**Warning from corpus:** Nigeria FIRS deadline passed (August 2025) with no solution built. Wave caught community sleeping — same pattern as Nigeria.

---

### South Africa — Most Developed (OPP-AF-02)
**Most mature African market, zero official Frappe partners**

**What's available (GitHub):**
| Repo | Focus | Stars | Status |
|------|-------|-------|--------|
| `frappe/erpnext_south_africa` | Official repo | 3 | 2022 |
| `TinasheErasmus/sa_vat_compliance` | SARS VAT201 | 2 | Jan 2026 (ACTIVE!) |
| `Starktail/csf_za` | SA customizations | 4 | Active v15 |
| `thamimanuel/erpnext_rsa_payroll` | Payroll | 8 | 2017 |

**Key signal:** `sa_vat_compliance` created Jan 2026 — proof of active development.

**What's still needed:**
1. SARS e-Invoicing (mandatory for certain transactions)
2. SAF-T (South African Tax Technical)
3. SCOA (Standard Chart of Accounts) — mandatory for government
4. SARS VAT201 submission enhancements
5. ZAR currency handling

---

### Kenya — East Africa Hub (OPP-AF-03)
**3 official Frappe partners, growing ecosystem**

**What's needed:**
1. KRA iTax integration
2. e-TIMS (Tax Invoice Management System) compliance
3. Kenyan Shilling (KES) handling
4. East African Community VAT (16% standard)
5. Withholding VAT (WHT)
6. Kenyan chart of accounts

---

### Francophone Africa — OHADA Standard (OPP-AF-04)
**17 countries using OHADA accounting standards**

OHADA countries:
- West Africa: Senegal, Ivory Coast, Mali, Burkina Faso, Niger, Togo, Benin
- Central Africa: Cameroon, Chad, CAR, Congo, Gabon, Equatorial Guinea
- North Africa: Morocco, Tunisia (some variation)

**Current status:** ZERO ERPNext OHADA localization
- Generic OHADA repos exist for Odoo, Banana Accounting, Java systems
- No ERPNext-specific implementation

**What's needed:**
1. OHADA-compliant chart of accounts (SYSCOHADA)
2. French interface polish
3. Country-specific tax configurations
4. Multi-currency (XOF, XAF, MAD, TND)
5. Morocco e-invoicing (DGCCIQ mandate active)

---

### Morocco — Francophone Priority
- DGCCIQ e-invoicing mandate
- Moroccan Dirham (MAD) handling
- Moroccan chart of accounts
- Moroccan tax requirements

---

## Opportunity Scoring Matrix

| Country | Market Size | Compliance Urgency | ERPNext Readiness | Score |
|---------|-----------|-------------------|-------------------|-------|
| **Nigeria** | Very High | CRITICAL (FIRS) | 0/10 | **10/10** |
| **South Africa** | High | Medium (SARS) | 5/10 | 7/10 |
| **Kenya** | Medium | High (KRA) | 0/10 | 8/10 |
| **Morocco** | Medium | High (e-invoice) | 0/10 | 8/10 |
| **Ghana** | Medium | Medium | 0/10 | 7/10 |
| **Tunisia** | Low | Medium | 0/10 | 6/10 |
| **Senegal** | Low | Low | 0/10 | 5/10 |
| **Cameroon** | Low | Low | 0/10 | 5/10 |

---

## Pan-African Opportunities

### OPP-AF-05: Pan-African Payment Gateway
**Priority: HIGH** | **Confidence: 8/10**

Africa has unique payment ecosystems:
- **Nigeria:** Flutterwave, Paystack, bank transfers
- **Kenya:** M-Pesa (Safaricom), Flutterwave
- **Ghana:** Mobile Money (MTN, Vodafone), Flutterwave
- **South Africa:** Paystack, Yoco, Zapper
- **Pan-African:** Flutterwave (cross-border), Paystack

**What's needed:** Unified ERPNext integration with Flutterwave, Paystack, M-Pesa, Mobile Money.

**Pricing:** $99-299/month per integration. $500-2,000 setup.

---

### OPP-AF-06: Bank Statement Import (African Banks)
**Priority: MEDIUM** | **Confidence: 7/10**

ERPNext can't import bank statements from African banks (MTN, Airtel Money, M-Pesa, major African banks).

**What's needed:** MT940/CAMT format support for African banks, plus specific parser integrations.

---

### OPP-AF-07: African Seed Data Packs
**Priority: MEDIUM** | **Confidence: 7/10**

Nigerian, Kenyan, South African, Ghanaian demo companies with:
- Local company registration formats
- Local bank details
- Local currency configurations
- Local chart of accounts

---

## New Personas Identified

1. **FIRS Deadline Fighter** — Nigerian CFO/IT Manager facing FIRS compliance. ERPNext not on supported list, forced to switch to SAP/Oracle. Needs FIRS-compliant e-invoicing.
2. **OHADA Accountant** — French-speaking accountant in Ivory Coast/Senegal/Cameroon needing SYSCOHADA-compliant accounting. Price-sensitive market.
3. **Bank Integration Bridge** — Developer connecting ERPNext to Flutterwave, Paystack, M-Pesa. Cross-border payment capabilities.
4. **Mandate Chaser** — Consultant building compliance solutions before African e-invoicing deadlines hit. Very high WTP for first-movers.
5. **Community Builder** — ERPNext enthusiast growing local ecosystem in East/West Africa. Low-medium WTP but passion-driven.
