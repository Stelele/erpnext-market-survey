# Persona: SPED Compliance Navigator

**Source:** Non-English Market Research — Brazil
**Read:** market-research/brazil.md

---

## Profile

The SPED Compliance Navigator is a Brazilian accounting specialist, tax consultant, or ERP implementation lead who understands the full depth of Brazil's tax and compliance requirements. They know that ERPNext cannot currently handle Brazilian compliance, but they want it to.

## Core Characteristics

**What they know:**
- SPED (Sistema Público de Escrituração Digital) — Brazil's mandatory digital bookkeeping
- ECD (Escrituração Contábil Digital) — digital accounting book
- ECF (Escrituração Contábil Fiscal) — digital tax book
- EFD-ICMS/IPI, EFD-Contribuições
- NF-e (Nota Fiscal Eletrônica) — electronic invoice
- ICMS, ICMS-ST, PIS, COFINS, IPI, ISS calculations
- Brazilian accounting standards (CPC, IFRS Brazil)

**What they feel about ERPNext:**
- Interested in the open-source model
- Frustrated that ERPNext doesn't handle Brazilian compliance
- Cannot recommend ERPNext to clients as-is
- Willing to help build the solution if approached seriously

**What they want:**
- Full NF-e emission (not just receipt)
- SPED export (ECD, ECF)
- Brazilian tax calculation engine
- Brazilian chart of accounts
- CNPJ/CPF validation

## The Brazilian Blocker Stack

ERPNext in Brazil has multiple blocking issues stacked on top of each other:

1. **NF-e emission** — can't legally issue invoices without this
2. **Tax calculation** — can't compute ICMS, PIS, COFINS correctly
3. **SPED export** — mandatory for most legal entities
4. **Chart of accounts** — no standard Brazilian template

You need ALL of these for any Brazilian company to adopt ERPNext. Building just one leaves the customer stranded.

## The Chicken-and-Egg Problem

**The problem:**
- Companies won't adopt ERPNext without compliance
- Compliance modules won't be built without confirmed demand
- Demand can't be confirmed without companies trying it

**The unlock:** Build NF-e emission first. It's the single highest-value item that every Brazilian company needs. One working module unlocks the entire market conversation.

## How They Evaluate Opportunities

**What they look for:**
- Deep understanding of Brazilian tax law
- Realistic assessment of what can be built
- Partnership with Brazilian accounting experts
- Phased approach (not "we'll fix everything at once")

**Red flags:**
- Developer who doesn't know what SPED is
- "We'll add Brazilian support" without specifics
- Ignoring NF-e (the #1 blocker)
- Promising everything and delivering nothing

**Pricing tolerance:**
- R$5,000-50,000 one-time for compliance modules
- R$200-800/month for ongoing support
- Will pay premium for working solution

## WTP Signals

- Intelligence8 (Brazilian company) actively building localization
- TechMax Soluções has 48 public repos, building SPED
- TechMax's `motor_tributario_py` tax calculation library (7 stars)
- No premium ERPNext apps on frappe.io marketplace for Brazil
- Entire Brazilian market is greenfield for real compliance solutions

## The Path Forward

1. **Phase 1:** NF-e emission module (highest value, unlocks market)
2. **Phase 2:** Brazilian tax calculation engine (builds on TechMax's work)
3. **Phase 3:** SPED export (required for medium+ enterprises)
4. **Phase 4:** Standard chart of accounts

Each phase funds the next. NF-e emission is the business case for everything else.

## Persona Scorecard

| Dimension | Score | Notes |
|-----------|-------|-------|
| Market Size | 9/10 | Brazil: 215M people, massive ERP market |
| WTP | 9/10 | Forced compliance = maximum WTP |
| Urgency | 6/10 | Chronic pain, no acute crisis yet |
| Competition | 10/10 | Entire market is greenfield |
| Solo Founder Fit | 2/10 | Needs Brazilian compliance expertise |
| Moat | 9/10 | First mover owns entire Brazilian localization |
| Exit Potential | 6/10 | Totvs competitor could acquire |
| Overall | 7.3/10 | **Monopoly opportunity if executed** |
