# ERPNext Brazil Market Research

**Date:** March 2026
**Market:** Brazil (Portuguese-speaking) — massive compliance gaps, monopoly opportunity

---

## Community Infrastructure

| Platform | Channel | Activity |
|----------|---------|----------|
| Telegram | t.me/erpnext_brazil | Active Brazilian community |
| Telegram | t.me/erpnextbr | Secondary |
| GitHub | Intelligence8official/ERPNext_Brazil | Primary localization developer |
| GitHub | Intelligence8official/ERPNext_Brazil_NF | NF-e integration |
| GitHub | techmaxsolucoes/SPEDIR-DOCS | SPED documentation |
| GitHub | techmaxsolucoes/motor_tributario_py | Tax calculation library (7 stars) |

**Key developer:** Intelligence8 (Brazilian company) — most organized localization effort. TechMax Soluções (48 public repos, SPED focus).

---

## Dominant Competitors (Switching FROM)

- **Totvs** — dominant domestic ERP, ~50%+ market share. Full Brazilian compliance built-in. High licensing costs (R$5,000-50,000+/month for larger firms).
- **Senior** — mid-to-large enterprises, strong in South Brazil
- **Sankhya** — popular SMB, excellent Brazilian tax compliance, monthly subscription
- **e-Cont** — accounting-focused SMEs
- **SAP** — large enterprises, expensive
- **Domi** (Totvs subsidiary) — entry-level SMB

**Switching signal:** Companies paying high Totvs fees are the primary ERPNext migration target.

---

## Compliance Requirements Assessment

### Critical Compliance Matrix

| Requirement | ERPNext Status | Impact |
|-------------|---------------|--------|
| NF-e Receive/Import | ✅ Implemented | Can process supplier invoices |
| **NF-e Emit (Generate)** | ❌ NOT IMPLEMENTED | **Blocker** — can't legally sell |
| **SPED (ECD/ECF)** | ❌ NOT IMPLEMENTED | **Blocker** — mandatory for most companies |
| **Tax Calculation (ICMS, PIS, COFINS, IPI)** | ❌ NOT IMPLEMENTED | **Blocker** — can't compute taxes |
| NFS-e Emit | ❌ NOT IMPLEMENTED | Blocker for service companies |
| CT-e Emit | ❌ NOT IMPLEMENTED | Blocker for logistics |
| MDF-e | ❌ NOT IMPLEMENTED | Gap for freight |
| Brazilian Chart of Accounts | ❌ NOT standardized | Manual setup required |
| CNPJ/CPF validation | ⚠️ Partial | Basic fields exist |

### NF-e (Nota Fiscal Eletrônica) — THE Blocker

ERPNext can **receive** NF-e from suppliers via `ERPNext_Brazil_NF` (Intelligence8):
- DF-e Distribution API integration (SEFAZ)
- XML parsing for all Brazilian tax fields
- Auto-creation of Suppliers and Items
- Purchase Invoice matching with scoring

But ERPNext **cannot emit** (generate and authorize) NF-e for outgoing invoices. This requires:
- SEFAZ API integration
- Digital certificate signing (A1 certificate)
- Specific XML schema per state
- Authorization workflow

**Without NF-e emission, no Brazilian company can legally sell.**

### SPED (Sistema Público de Escrituração Digital)

Brazil's mandatory digital bookkeeping system. Components:
- **ECD** (Escrituração Contábil Digital) — digital accounting book
- **ECF** (Escrituração Contábil Fiscal) — digital tax book
- **EFD-ICMS/IPI** — detailed inventory/fiscal records
- **EFD-Contribuições** — contribution records

**No functional SPED export exists in any public ERPNext app.** TechMax is building `SPEDIR` but it's in documentation phase only.

### Tax Calculation Engine

ERPNext cannot calculate Brazilian taxes. All tax computation must be done manually or via external systems.

TechMax has `motor_tributario_py` (Python tax calculation library) but it's not integrated with ERPNext.

---

## Portuguese Localization

- ERPNext supports Portuguese (`pt`) and Brazilian Portuguese (`pt-BR`)
- Core translations exist but **incomplete** — many fields remain in English
- Brazilian accounting terminology gaps (Nota Fiscal vs. Fatura, etc.)
- Brazilian chart of accounts: not standardized, no community standard

---

## Opportunity Analysis

### OPP-BR-01: NF-e Emission Module
**Priority: CRITICAL** | **Confidence: 10/10**

ERPNext cannot legally issue invoices in Brazil without NF-e emission. This is the single biggest blocker for the entire Brazil market.

**What's needed:**
- SEFAZ API integration (federal + 27 state-specific APIs)
- Digital certificate (A1) management
- NF-e XML generation per SPED/NF-e technical manual
- Authorization workflow and retry logic
- Invoice cancellation and correction events
- NFC-e (consumer nota) for retail/POS

**Build difficulty:** Very High. Requires deep knowledge of Brazilian fiscal law, SEFAZ APIs, and digital certificates. Estimated 3-6 months for experienced developer.

**Pricing:**
- SaaS: R$500-2,000/month ($100-400/month)
- One-time: R$15,000-50,000 ($3,000-10,000)
- Per-invoice processing: R$0.50-1.50

**WTP:** Any company operating in Brazil needs this. Forced willingness-to-pay.

**Competitors:** None in ERPNext ecosystem. Traditional ERPs (Totvs, Sankhya) have this built-in.

---

### OPP-BR-02: Brazilian Tax Calculation Engine
**Priority: CRITICAL** | **Confidence: 9/10**

ERPNext cannot compute ICMS, PIS, COFINS, IPI, or ISS. This makes any sales/purchase transaction incomplete.

**Build on:** TechMax's `motor_tributario_py` exists — integration project, not rebuild.

**What's needed:**
- Integration of motor_tributario_py with ERPNext doctypes
- ICMS, ICMS-ST, PIS, COFINS, IPI calculation at point of transaction
- ISS calculation for services
- NCM/CEST-based tax rules
- State-to-state ICMS differentials

**Pricing:** R$10,000-30,000 setup. R$200-500/month maintenance.

---

### OPP-BR-03: SPED Export Module (ECD/ECF)
**Priority: HIGH** | **Confidence: 8/10**

Mandatory digital accounting books for most Brazilian companies.

**Build difficulty:** High. SPED formats are complex and change frequently.

**Pricing:** R$15,000-40,000 setup. R$300-800/month maintenance.

---

### OPP-BR-04: Brazilian Seed Data / Demo Packs
**Priority: MEDIUM** | **Confidence: 8/10**

Brazilian companies need realistic demo data:
- CNPJ-valid company data
- Brazilian product catalog with NCM codes
- Brazilian chart of accounts (SPED-compliant)
- Sample NF-e XML files
- State-wise tax configurations

---

### OPP-BR-05: Brazilian Payroll Module
**Priority: MEDIUM** | **Confidence: 7/10**

Brazilian payroll is extremely complex:
- INSS, IRRF calculations
- FGTS (Fundo de Garantia do Tempo de Serviço)
- 13th salary, vacation accrual
- Collective bargaining agreements (CCTs)
- ESocial integration (mandatory government reporting)

**What's needed:** Full Brazilian payroll engine integrated with ERPNext HR.

---

## Key Insight: The Chicken-and-Egg Problem

**ERPNext in Brazil has a fundamental adoption blocker:**
- Companies can't use ERPNext without Brazilian compliance (NF-e, SPED, tax calculation)
- Building compliance modules requires significant investment
- But investment is risky without confirmed market demand
- Market demand can't be confirmed without trying the product

**Solution:** Build NF-e emission first. It's the single highest-value, most universal need. One working module unlocks the entire market.

---

## New Personas Identified

1. **SPED Compliance Navigator** — Brazilian accounting specialist/consultant. Cannot recommend ERPNext to clients because SPED is not implemented. Opportunity: become the go-to ERPNext-Brazil compliance expert.
2. **Totvs Escape Artist** — business owner paying high Totvs fees (R$5,000-50,000+/month), wants out. Reality check: can't fully switch until NF-e emission exists.
3. **ERPNext Brazil Developer** — Frappe developer building Brazilian localization in isolation. Opportunity: become core maintainer, charge for implementation, get community sponsorship.
4. **Motor Tributário Integrator** — developer who connects TechMax's tax calculation library to ERPNext.
