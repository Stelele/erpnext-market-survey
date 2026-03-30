# Alternative Solution Auditor: Opportunity Canvas

**Persona:** Alternative Solution Auditor — The founder who researches non-SaaS alternatives before building anything.
**Date:** March 30, 2026
**Source:** ERPNext Community Forum (1,742 topics audited)

---

## Insight: ERPNext's Gaps Create Spreadsheet/Alternative Overlays

ERPNext is being widely adopted — but users repeatedly hit gaps where the platform **cannot do what they need**, forcing them to patch ERPNext with external tools. The result is the same fragmented data problem ERPNext was supposed to solve. This is where **build opportunities** live: solve the gap, eliminate the workaround, own the workflow.

---

## Opportunity 1: Reporting & Analytics Workarounds (ZONE 1 — #1 Spreadsheet Workaround)

**Severity: CRITICAL**

### Evidence

- **Topic #79873** (Script Report/Chart Tutorial) — 160 likes, 32,522 views, 2021-present. A non-developer power-user created a tutorial on Python/JavaScript scripting just to build custom reports. Official documentation: *"borderline useless."* Users spend hours learning to write custom report code because ERPNext's built-in reporting is insufficient. This single tutorial has been read 1,684+ times and continues to be referenced years later.
- **Topic #131682** (Child Table Limitations) — 29 likes, 1,834 views. A developer building a Provident Fund module had his CTO say: *"Why does an advanced web application framework like Frappe have such a limitation, only allowing us to show 10 columns of data in a child table?"* Even Frappe's own developers admit the grid needs a complete rewrite. Third parties are building paid custom apps (nesscale-com/frappe_enhanced_gridview) to solve this.
- **Topic #143390** (Cabinet Shop, Belgium). User explicitly says they need Frappe Insights for reporting needs. A consultant recommends: *"ERPNext has project and timesheet tools... For reporting needs, you can use Frappe Insights."* Frappe Insights itself is a separate paid tool — not core ERPNext.

### The Workaround Pattern
Users need: custom columns in tables, multi-dimensional reports, better data visualization, cross-module analytics.

They get: Script Reports (write Python), custom apps (hire developers), or Frappe Insights (pay more).

### What People Are Bypassing ERPNext With
- Custom Python/JS Script Reports (developer-dependent)
- Frappe Insights (separate paid app)
- Third-party grid view apps
- Excel exports for manual analysis

### Build Opportunity
A no-code/low-code **reporting and analytics layer** that works natively within ERPNext. Drag-and-drop report builder, custom table views, cross-module dashboards, and one-click pivot/chart exports. Eliminate the need for scripting, third-party apps, or Excel exports.

---

## Opportunity 2: Manufacturing Estimating & Job Costing (ZONE 2)

**Severity: HIGH**

### Evidence

- **Topic #143390** (Cabinet Shop, Netherlands) — 596 views, active discussion. A custom furniture manufacturer explicitly states: *"Currently, we are using Excel for estimations."* They also use ClickUp for project planning, Gekko.nl for invoicing, and their accountant's custom platform. Their pain is explicit: **"a collection of apps and data that are not centralized or easily analyzable."** They chose ERPNext specifically to replace this patchwork, but ERPNext doesn't have a native job costing / estimating module that handles custom manufacturing. Consultant recommends ERPNext's project and timesheet tools + Frappe Insights — essentially bolting two more tools to the patchwork.

### The Workaround Pattern
Custom manufacturers (make-to-order, engineer-to-order) need: BOMs with variable materials, multi-level routing, cost estimation before production, actual-vs-estimated cost tracking.

They get: Excel for pre-production estimating, ERPNext's limited Project module for job tracking, and spreadsheets to compare estimates vs. actuals.

### What People Are Bypassing ERPNext With
- Excel for job estimating and cost calculation
- ClickUp or Monday.com for project management
- Google Sheets for cross-team data sharing

### Build Opportunity
A **Manufacturing Estimating & Job Costing module** that integrates natively with ERPNext's BOM and production modules. Quote generation with material/labor/routing costs, side-by-side estimated vs. actual cost tracking, and configurable cost sheets. Eliminate the Excel dependency entirely.

---

## Opportunity 3: Lending & Borrowing Financial Management (ZONE 3)

**Severity: MEDIUM-HIGH**

### Evidence

- **Topic #106913** (Private Money Lender) — 684 views, active through 2026. A private money lender who borrows from people and lends to others finds ERPNext's Loan Management (now "Lending" standalone app) handles the lending side but **completely ignores the borrowing side**. They ask ChatGPT for help and get the answer: *"You can maintain a separate accounting system to track the money you borrow. This could be as simple as using a spreadsheet or utilizing accounting software like QuickBooks or Xero."* A community member recommends dedicated loan management software like Finanta. The poster never finds a resolution within ERPNext.

### The Workaround Pattern
Lending businesses (P2P lending, microfinance, private money lending) need: full dual-sided loan tracking (loans received + loans given), interest accrual on liabilities, repayment scheduling for borrowed funds, margin tracking.

They get: QuickBooks or Xero as a parallel system, spreadsheets for tracking borrowed funds, or expensive dedicated loan software.

### What People Are Bypassing ERPNext With
- QuickBooks for borrowing-side accounting
- Xero for dual tracking
- Dedicated platforms like Finanta (expensive, not open-source)
- Spreadsheets for manual tracking

### Build Opportunity
An **Extended Lending module** that handles both sides of lending operations: loans received (liabilities) and loans disbursed (assets), with full interest calculations, repayment schedules, and margin reports. Close the gap that forces users to QuickBooks or Xero as a parallel accounting system.

---

## Opportunity 4: Healthcare Patient-Facing Booking (ZONE 4)

**Severity: MEDIUM**

### Evidence

- **Topic #147315** (Healthcare Booking Calendar) — 426 views, 4 likes, active 2025. A user building a healthcare practice says: *"For some reason, I can't find any documentation or ways to create a customer-facing custom page that allows all visitors (registered or not) to see the schedule/availability of doctors or maybe filter by services they provide."* The built-in `book_appointment` page is *"beyond limited"* — it can't filter by doctor, service, or specialty. A third-party app (frappe-appointment by rtCamp) exists but is Google Calendar-centric and not integrated with ERPNext's Healthcare module. Another user echoes: *"I tried installing and it has no connection to Practitioner Schedule or Patient Appointment forms — it's not made for Healthcare module."* The user notes: *"self-hosted open-source medical ERP solution that can connect its backend to the client-facing frontend will be the first one."*

### The Workaround Pattern
Healthcare practices need: a public-facing booking page where patients select doctor, service, and time slot; real-time availability sync; PIPEDA/GDPR-compliant hosting (on-premises required).

They get: Build custom apps (developer-dependent), use third-party scheduling tools, or rely on the broken built-in appointment system.

### What People Are Bypassing ERPNext With
- Custom apps (frappe-appointment — Google Calendar dependent)
- Third-party scheduling platforms (Calendly, Acuity, etc.)
- Manual appointment coordination

### Build Opportunity
A **Healthcare Patient Portal & Booking module** with a public-facing, filterable booking page (doctor, service, specialty), live availability from Practitioner Schedule, and native integration with Patient Appointment forms. On-premises deployable for PIPEDA/GDPR compliance.

---

## Opportunity 5: US Bank Transaction Integration (ZONE 5)

**Severity: MEDIUM**

### Evidence

- **Topic #137696** (Plaid Setup) — 1,500 views, active through 2025. A user migrating from Odoo says: *"Coming from Odoo, it was so simple. I just clicked to add my bank and it just worked. I am not experiencing that here."* They had to navigate Plaid's complex developer dashboard, answer security questions, configure products, and wait for account approval. The ERPNext Plaid integration broke after Plaid changed its API in 2024, and **"we have already been waiting for more than six months (after the Plaid API changed) without any updates."** A user explicitly says: *"I want to go to an ERP to automate things and get away from manual importing of data."* They came to ERPNext to escape manual work and found themselves doing MORE manual work.

### The Workaround Pattern
US-based businesses need: automatic bank transaction import for reconciliation, minimal friction setup.

They get: Complex Plaid configuration, manual CSV imports, or reverting to manual bookkeeping.

### What People Are Bypassing ERPNext With
- Manual CSV imports of bank statements
- QuickBooks for bank feeds (as a parallel system)
- Tally or other regional accounting software with better bank integration

### Build Opportunity
A **simplified US bank connection layer** with one-click Plaid setup (or alternative aggregator), automatic transaction categorization, and seamless bank reconciliation. Make it as easy as Odoo — "click to add your bank and it just works."

---

## Cross-Cutting Pattern: The "Too Small" Gap

**Topic #143390** surfaces another recurring theme: businesses feel ERPNext is either **too complex/costly** (SAP, NetSuite) or **too incomplete** for their needs. They don't fit the SaaS mold but can't afford the enterprise ERP. ERPNext targets mid-market, but the gap below mid-market (small businesses with 5-50 employees, $500K-$5M revenue) is served by patchwork solutions: Excel + ClickUp + QuickBooks + a dozen Google Sheets.

The opportunity: **packaged industry solutions** that pre-configure ERPNext for specific verticals (custom manufacturing, healthcare clinics, lending operations) with the missing modules built in, reducing implementation time from months to days.

---

## Synthesis: Where to Build

| Priority | Opportunity | Confidence | Effort |
|----------|-------------|-----------|--------|
| 1 | Reporting & Analytics Layer | VERY HIGH — 160+ likes, 32K views on workaround tutorial | HIGH — requires deep ERPNext framework knowledge |
| 2 | Manufacturing Estimating & Job Costing | HIGH — explicit pain in multiple threads | MEDIUM |
| 3 | Lending (Dual-Sided) Module | MEDIUM — niche but no open-source competitor | MEDIUM |
| 4 | Healthcare Patient Booking Portal | MEDIUM — clear gap, existing third-party partially addresses | MEDIUM |
| 5 | US Bank Integration (Simplified) | MEDIUM — Odoo comparison is damning | MEDIUM |

---

## Source Topic References

| Topic ID | Title | Key Evidence |
|----------|-------|--------------|
| #79873 | Script Report/Chart Tutorial | 160 likes, 32K views — reporting workaround |
| #143390 | Users from Belgium & Netherlands | Excel for estimations, multi-tool pain |
| #106913 | Loan Management (Lending) | QuickBooks/Xero recommended as workaround |
| #147315 | Healthcare Booking Calendar | No customer-facing booking, forced to build custom |
| #137696 | Plaid Setup and Configuration | Odoo comparison, manual import fallback |
| #131682 | Child Table Limitations | CTO disappointment, third-party apps needed |
| #114965 | Automation/CRM | Mautic mentioned as external tool alongside ERPNext |
| #147275 | Manufacturing BOM | Complex production planning gaps |
