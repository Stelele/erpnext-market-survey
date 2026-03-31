# Persona: DATEV Prisoner

**Source:** Non-English Market Research — Germany/DACH
**Read:** market-research/germany.md

---

## Profile

The DATEV Prisoner is a German accountant, CFO, or business owner locked into the DATEV ecosystem. They pay €100-500/month to DATEV for accounting software plus their tax advisor's fees for data processing. They feel the walls of the cage but can't see the door.

## Core Characteristics

**What they believe:**
- DATEV is unavoidable because their tax advisor requires it
- Switching ERPs means switching tax advisors
- Open-source ERP can't meet German compliance standards
- German accounting is too complex for "regular" software

**What actually frustrates them:**
- DATEV's rigid structure and limited customization
- High monthly costs with no negotiation
- Slow to add modern features (API-first, real-time data)
- Can't integrate with their custom workflows
- Feel trapped by the tax advisor dependency

**What they secretly want:**
- Modern ERP flexibility and customization
- Freedom from DATEV's rigid structure
- Better value for money
- Ability to do more in-house without touching DATEV

## The DATEV Dependency Problem

DATEV is a cooperative owned by German tax advisors. This creates a near-insurmountable moat:
- 95%+ of German tax advisors use DATEV
- Tax advisors accept only DATEV format data
- Companies can't easily switch advisors (and advisors won't switch from DATEV)

**But:** Tax advisors don't need ERPNext to BE DATEV. They just need data in a format they can import.

The unlock: **Build a DATEV bridge** that exports ERPNext data in a format German tax advisors can import. DATEV Unternehmen Online accepts CSV/XML imports. This bypasses the need for native DATEV integration.

## How They Evaluate Opportunities

**What they look for:**
- "DATEV-kompatibel" (DATEV compatible) — this phrase alone sells
- GoBD compliance documentation
- German-language support
- Tax advisor-friendly export format
- Someone else has done it successfully in Germany

**Red flags:**
- "We don't need DATEV" (ignores the real problem)
- No German-language documentation
- US/UK-centric implementation examples
- Only works with English-language ERPNext

**Pricing tolerance:**
- €99-299/month for a working DATEV bridge
- €2,000-5,000 one-time for GoBD compliance tools
- Will pay for certainty over cheap solutions

## Tactics They Use

- Ask for German company references first
- Quiz you on German accounting terminology
- Want written documentation on GoBD compliance
- Consult their tax advisor before committing
- Compare total cost to DATEV subscription explicitly

## WTP Signals

- 127 replies on discuss.frappe.io "DATEV-kompatibel" thread (21,745 views)
- 7+ years of community demand, still unsolved
- German ERPNext community actively asking for this
- "Xentral refugees" from 2022 onward actively seeking alternatives
- SEIBERT/MEDIA (150 users), ESO Electronic (120 users) — both on ERPNext but NOT using accounting module due to DATEV gap

## The Strategy

1. Don't try to replace DATEV. **Integrate with it.**
2. Build a CSV/XML exporter that maps ERPNext data to DATEV's import format.
3. Target the SKR04 chart of accounts (most common).
4. Get ONE German tax advisor to accept the import format.
5. Use that reference to get more advisors.
6. The bridge unlocks the entire German market.

## Persona Scorecard

| Dimension | Score | Notes |
|-----------|-------|-------|
| Market Size | 9/10 | 3.5M+ businesses in Germany |
| WTP | 8/10 | Paying €100-500/month already |
| Urgency | 6/10 | Chronic pain, but no acute crisis |
| Competition | 10/10 | 7 years, zero solutions |
| Solo Founder Fit | 6/10 | Buildable, needs German accounting knowledge |
| Moat | 7/10 | DATEV format knowledge compounds |
| Exit Potential | 5/10 | Germany/Europe acquirer could be interested |
| Overall | 7.3/10 | **Highest-value compliance unlock in Europe** |
