# ERPNext Latin America Market Research

**Date:** March 2026
**Market:** Mexico, Argentina, Colombia, Chile, Peru + El Salvador (from corpus)

---

## Community Infrastructure

| Country | Telegram | Activity |
|---------|----------|----------|
| Brazil | t.me/erpnext_brazil, t.me/erpnextbr | Active |
| Mexico | t.me/erpnextmexico | Medium |
| Argentina | t.me/erpnext_argentina | Medium |
| Colombia | t.me/erpnext_colombia | Medium |
| Chile | t.me/erpnext_chile | Medium |
| Peru | t.me/frappe_peru | Medium |
| Spain | t.me/erpnext_spain | Medium |

**Note from corpus:** No LatAm country modules in ERPNext core. Regional folder has Australia, Italy, South Africa, Turkey, UAE, USA — zero LatAm representation.

---

## Country-by-Country Analysis

### Mexico — HIGH PRIORITY (OPP-LAT-01)
**Most actionable LatAm market after Brazil**

**SAT Requirements:**
- **CFDI (Comprobante Fiscal Digital por Internet):** MANDATORY for all invoices since 2014. ERP must generate CFDI-compliant XML.
- **RFC (Registro Federal de Contribuyentes):** Tax ID validation
- **CSD (Certificado de Sello Digital):** Digital certificates required for signing
- **PAC (Proveedor Autorizado de Certificación):** Certified service for invoice validation
- **Factura 4.0:** Latest CFDI format with complementing requirements

**What's needed:**
- CFDI generation (Factura 4.0)
- PAC integration (Solid, SW Developer, Facturapi, etc.)
- RFC validation
- Mexican SAT tax catalog integration (c_TipoImpuesto, c_FormaPago, etc.)
- Cancellation and substitution workflows

**ERPNext Mexico status:** NOT IMPLEMENTED. This is a hard blocker — Mexican companies cannot legally invoice without CFDI.

**Competitors:** Aspel, ContaPlus, Business Central all have native CFDI support.

---

### Argentina — Complex (OPP-LAT-02)
**Currency chaos + tax complexity**

- Complex tax system: IVA (21% standard), Ganancias (income tax), IVA Percepción
- **Electronic invoice:** AFIP (Administración Federal de Ingresos Públicos) required
- **Currency controls:** Argentine peso (ARS) complexity with official vs. blue rate
- **Mercado Libre integration:** Important for e-commerce
- **Factura Electrónica:** AFIP-compliant e-invoicing

**What's needed:**
- AFIP e-invoice integration (WebService)
- Argentine tax calculation (IVA, Ganancias, Perception)
- ARS currency handling with proper decimal precision
- Argentine chart of accounts
- Factura Electrónica format

**ERPNext Argentina status:** NOT IMPLEMENTED

---

### Colombia — DIAN Compliance (OPP-LAT-03)
- **DIAN (Dirección de Impuestos y Aduanas Nacionales):** Tax authority
- **Electronic invoicing:** Mandatory for companies above threshold
- **NIT validation:** Company tax ID
- **RUT (Registro Único Tributario):** Tax registry
- **Colombian VAT:** 19% standard, varied rates
- **Factura Electrónica:** DIAN-compliant format

**What's needed:**
- DIAN e-invoice integration (API)
- Colombian tax calculation (IVA, ICA, INC)
- NIT validation
- Colombian chart of accounts
- DIAN authorization workflow

**ERPNext Colombia status:** NOT IMPLEMENTED

---

### Chile — SII Requirements (OPP-LAT-04)
- **SII (Servicio de Impuestos Internos):** Tax authority
- **DTE (Documento Tributario Electrónico):** Electronic invoice format
- **Factura Electrónica:** SII-compliant format mandatory
- **Chilean accounting:** NIIF (IFRS) based
- **Boleta Electrónica:** Consumer receipt format

**What's needed:**
- SII DTE integration
- Chilean tax calculation (IVA 19%)
- DTE XML generation
- SII certification process
- Chilean chart of accounts

**ERPNext Chile status:** NOT IMPLEMENTED

---

### Peru — SUNAT Integration (OPP-LAT-05)
- **SUNAT (Superintendencia Nacional de Aduanas y de Administración Tributaria)**
- **Factura Electrónica:** SUNAT-compliant format
- **UBL 2.1:** Peru uses OASIS UBL standard
- **Peruvian VAT:** IGV 18%
- **Boleta de Venta:** Consumer invoice format

**What's needed:**
- SUNAT e-invoice integration
- Peruvian tax calculation (IGV, ISC)
- UBL 2.1 format generation
- Peruvian chart of accounts

**ERPNext Peru status:** NOT IMPLEMENTED

---

### El Salvador — From Corpus (OPP-LAT-06)
**Corpus Topics 156731, 156865**

- MH (Ministerio de Hacienda) integration required
- Electronic invoice mandate active
- ERPNext not on government supported list
- Progress since corpus: UNKNOWN

**Status:** Still needs building. Government mandate = forced WTP.

---

## LatAm Regional Opportunity

### OPP-LAT-07: UBL 2.1 Invoice Generator
**Priority: HIGH** | **Confidence: 7/10**

Multiple LatAm countries use OASIS UBL 2.1 format:
- Peru (confirmed)
- Colombia (migrating to UBL)
- Mexico (CFDI is different)
- Chile (DTE is different)

**What's needed:** ERPNext app that generates UBL 2.1 compliant invoices covering the common subset.

---

### OPP-LAT-08: LatAm Multi-Country Configuration Pack
**Priority: MEDIUM** | **Confidence: 6/10**

Companies operating across multiple LatAm countries need unified ERPNext with per-country configurations.

**What's needed:**
- Per-country tax rates
- Per-country chart of accounts
- Multi-currency (MXN, COP, CLP, PEN, BRL)
- LatAm-specific doctypes

---

## LatAm Common Themes

### E-Invoicing Mandates
Every LatAm country has mandatory e-invoicing. ERPNext has NO native e-invoice support for ANY LatAm country.

### Tax Complexity
LatAm taxes are notoriously complex:
- Multiple tax levels (federal, state, municipal)
- Perception taxes (taxes withheld by customers)
- Special regimes (SIMPLES in Brazil, RÉGIMEN SIMPLIFICADO in Mexico)
- Frequent tax law changes

### NIIF/IFRS
Most LatAm countries use NIIF (Normas Internacionales de Información Financiera / IFRS).

---

## Competitive Landscape

| Country | ERPNext Readiness | Main Competitors |
|---------|------------------|------------------|
| Mexico | 0/10 | Aspel, ContaPlus, Business Central |
| Argentina | 0/10 | SAP, Tango, Bejerman |
| Colombia | 0/10 | SAP, Siigo, Alegra |
| Chile | 0/10 | SAP,记账, Bizerba |
| Peru | 0/10 | SAP, Dynamics, local ERPs |
| Brazil | 3/10 | Totvs, Sankhya, Senior |

---

## New Personas Identified

1. **CFDI Master** — Mexican e-invoicing specialist. Obsessed with SAT compliance, RFC validation, and PAC integration.
2. **Currency Crisis Navigator** — Argentine CFO managing exchange rate chaos, multiple currency valuations, and AFIP complexity.
3. **SUNAT Compliance Officer** — Peruvian tax specialist. Knows UBL 2.1 inside out.
4. **LatAm Tax Navigator** — pan-LatAm consultant building e-invoicing solutions across multiple countries.
5. **UBL Pioneer** — developer building UBL 2.1 invoice generator for multiple LatAm markets.
