# Opportunity Canvas: System Buyer Persona
## ERPNext Forum — Buying vs. Building Analysis

**Persona:** System Buyer — evaluating whether to buy an existing ERPNext app/solution or build from scratch.
**Corpus:** discuss.frappe.io forum topics (1,742 total topics examined partially)
**Generated:** 2026-03-30

---

## Discovery Triggers Found

| Trigger Type | Count | Examples |
|---|---|---|
| "Is there an app for X?" | ~12 | PDC/Cheque, Hotel/Hospitality, Push Notifications |
| "Which app should I use?" | ~8 | CRM (ERPNext vs Frappe CRM), Print Designer alternatives |
| App failures / bugs | ~6 | MINT reconciliation bugs, IMAP sync marking as read |
| "No solution found" threads | ~15+ | Keycloak OIDC gaps, Quality Inspection per-row filtering |
| Integration gaps | ~10 | QuickBooks Desktop migration, Gmail group email accounts, Plaid/MINT issues |
| Customization workarounds | ~20+ | Sidebar customization (paid-only), navbar overrides, print format per-company |

---

## Competitive Landscape by Category

### Banking & Payments
| App | Status | Signals |
|---|---|---|
| **MINT** (banking reconciliation) | Active, v1.10 | Bugs with Payment Entry "Payment Form" field (v15/v16); custom field support in progress (per author @nikkothari22); "Transfer" reconciliation fails |
| **Plaid** | Mentioned | Mentioned in combination with MINT; no standalone forum activity |
| **PDC / Cheque Management** | **GAP** | Topic 153289: "Is there any good app for cheque or PDC management because Check Run don't want to be installed?" — no good answer; Check Run exists but is heavy |

### CRM
| App | Status | Signals |
|---|---|---|
| **ERPNext CRM** (built-in) | Default with ERPNext | Many users confused about which to install |
| **Frappe CRM** (standalone) | Actively developed, separate install | Topic 155913: users confused about installing alongside ERPNext; Docker multi-app complexity |
| **Assessment:** Two CRMs cause confusion; no clear "buy this one" guidance; integration between them is unclear | | |

### Hospitality / Hotels
| App | Status | Signals |
|---|---|---|
| **frappe/hospitality** | **ARCHIVED** | No maintenance; Topic 156929 confirmed — no good alternative for hotel management in ERPNext ecosystem |
| **GAP:** No ERPNext-native hotel PMS app | | |

### UI / Theme / Customization
| App | Status | Signals |
|---|---|---|
| **Owl Theme** | Active | Topic 157103 mentioned; no forum activity on it |
| **Frappe Studio** | Active | Topic 157103; visual internal apps builder; no complaints |
| **Sidebar Customization** | **PAID WORKAROUND** | Topic 151216: "this feature is paid and not free"; custom JS workaround shared in thread |
| **Navbar Customization** | Core files only | Topic 102222: cannot override navbar from custom app via standard hooks; requires JS DOM replacement |

### Print & Document Design
| App | Status | Signals |
|---|---|---|
| **Print Designer** | Active | Mentioned in multiple contexts; widely used |
| **Company-wise Print Formats** | GAP | Topic 101767: "how to set print format company-wise?" — no native solution; topic 103596: sales person contact on quotation requires manual field mapping |
| **Assessment:** Multi-company print format management is painful | | |

### Authentication / SSO
| App | Status | Signals |
|---|---|---|
| **Keycloak OIDC** | Broken / partial | Topics 102423, 155480: blank page after login, `access_token` KeyError, no true SSO redirect flow; Frappe uses rauth library which is outdated; single logout not supported |
| **Social Login (generic)** | Partial | Works for login; no logout propagation to IdP |
| **Assessment:** OIDC/SSO with enterprise IdPs (Keycloak, Auth0, Okta) is a known pain point with no polished app solution | | |

### Email / Communication
| App | Status | Signals |
|---|---|---|
| **IMAP Sync** | Buggy | Topic 100079: marks emails as read on IMAP server (2019–2026, still unfixed in some versions); "Initial Sync Count" ignored; wrong date shown in timeline |
| **Gmail Group as Email Account** | No native support | Topic 100539: Google Groups have no password; workaround via single user with aliases is complex |
| **Comment Mention Notifications** | No per-user sender | Topic 157119: mentions go from default email account, not from commenting user |
| **Assessment:** Email infrastructure is a known gap; no marketplace app addressing these pain points | | |

### Data Migration
| App | Status | Signals |
|---|---|---|
| **QuickBooks Migrator** | Online QB only | Topic 156990: Desktop QB migration has no solution; user built custom utility; community consensus: don't migrate historic transactions |
| **Assessment:** Desktop accounting software migration (QuickBooks Desktop, Sage, Tally) is a significant gap | | |

### Project Management
| App | Status | Signals |
|---|---|---|
| **ERPNext Projects / Tasks** | Built-in, basic | Topic 101004: Task progress auto-update from timesheet doesn't work; topic 156481: "Is ERPNext enough or do I need Asana/Jira?" |
| **Assessment:** Project management is considered insufficient for complex PMO use cases | | |

### HR / Employee Management
| App | Status | Signals |
|---|---|---|
| **Employee Gift / Item Issuance** | No clean solution | Topic 100230: "give an item to an employee as a gift" — requires custom Stock Entry + custom field workarounds |
| **Attendance Status Renaming** | Fragile | Topic 156538: renaming "Work from Home" breaks unless using Translation doctype |
| **Assessment:** Employee gift/asset issuance tracking is a gap | | |

### Education / Fees
| App | Status | Signals |
|---|---|---|
| **frappe/education** | Active | Topic 156851: Fees outstanding not reducing after payment allocation — regression bug reported |
| **Assessment:** Education module has active bugs; no alternative apps | | |

### Quality Management
| App | Status | Signals |
|---|---|---|
| **Quality Inspection** | Built-in | Topic 101498: creates QI for ALL items even when only some have "quality inspection required" checked; bug unfixed since 2023 |
| **Assessment:** Per-row QI filtering is a gap | | |

### Other Notable Apps Mentioned
- **Scan Me** (QR/barcode generation) — newly released, topic 157854
- **Frappe Wiki** — mentioned as companion app
- **Frappe LMS** — mentioned in passing
- **CSF_TZ** (Cairo School Foundation) — custom ERPNext variant for compliance
- **eu_einvoice** — e-invoicing compliance app

---

## Market Gap Analysis

### High-Demand, Low-Supply Gaps (Buy Opportunity)

1. **PDC / Cheque Management App**
   - Unmet need: Lightweight alternative to Check Run for post-dated cheque tracking
   - Signal strength: Direct question with no answer, 1 confirmed thread
   - Verticals: Middle East, South Asia (high cheque usage)

2. **Hotel / Hospitality PMS App**
   - Unmet need: Replace archived `frappe/hospitality`; ERPNext-native hotel management
   - Signal strength: Archived official app + forum question with no resolution
   - Verticals: Hospitality, tourism

3. **OIDC / Enterprise SSO Connector App**
   - Unmet need: Clean Keycloak/Auth0/Okta integration with true SSO redirect flow and logout propagation
   - Signal strength: Multiple threads (2019–2026), known issues with rauth library, no marketplace solution
   - Verticals: Enterprise, regulated industries requiring IdP-based auth

4. **ERPNext Email Stack Fixer App**
   - Unmet need: Fix IMAP sync (marking as read), Gmail Group support, per-user sender for notifications
   - Signal strength: Multiple long-running threads, still unfixed in 2026
   - Verticals: Any org with email-centric workflows

5. **Multi-Company Print Format Manager**
   - Unmet need: Assign print formats per company without custom scripts
   - Signal strength: Recurring question with no clean answer
   - Verticals: Holding companies, multi-entity businesses

6. **Desktop Accounting Migration App**
   - Unmet need: QuickBooks Desktop, Sage, Tally migration utilities
   - Signal strength: Forum thread shows someone building custom solution; no marketplace app
   - Verticals: Any SMB migrating from legacy accounting software

7. **Employee Gift / Asset Issuance App**
   - Unmet need: Track items given to employees (gifts, equipment) with HR + accounting integration
   - Signal strength: Topic 100230 with manual workaround, no clean solution
   - Verticals: HR-heavy organizations

8. **Sidebar / Workspace Customization App**
   - Unmet need: Custom sidebar with links, icons, conditional display — without paid developer
   - Signal strength: Topic 151216: "this feature is paid and not free"
   - Verticals: Any non-technical end user wanting UX improvements

### Moderate Gaps

9. **Task Progress Auto-Update App** — Timesheet-to-task progress sync
10. **Quality Inspection Row Filter App** — Only create QI for items with flag set
11. **Education Module Bug Fix Pack** — Fees outstanding reconciliation issues
12. **Push Notification App** — Topic 151169; PWA + push notifications for ERPNext

---

## App Review Patterns

- **MINT**: Active development (v1.10), but bugs remain (Payment Entry field support, custom field mapping)
- **No app receives explicit "this works great" praise** in the threads examined — most activity is troubleshooting
- **No app comparison threads** found — users generally ask about a specific app, not comparing alternatives
- **MINT author (nikkothari22)** responds publicly on the forum — shows active maintenance
- **Frappe CRM vs ERPNext CRM**: Community is confused, not hostile; opportunity for a comparison/guidance app

---

## Top Opportunity Rankings

| Rank | Opportunity | Confidence | Effort Estimate |
|---|---|---|---|
| 1 | PDC / Cheque Management | Medium | Medium |
| 2 | Hotel / Hospitality PMS | Medium-High | High |
| 3 | OIDC / Enterprise SSO Connector | High | Medium-High |
| 4 | Email Stack Fixer | High | Low-Medium |
| 5 | Multi-Company Print Format Manager | Medium | Low |
| 6 | Desktop Accounting Migration Utility | Medium | High |
| 7 | Employee Gift / Asset Issuance Tracker | Low-Medium | Low-Medium |
| 8 | Sidebar Customization App | Medium | Low |

---

## "Don't Build This" List

- **Another print format app** — Print Designer already exists and is sufficient; focus on print *management* (per-company assignment) instead
- **Another CRM** — Frappe CRM and ERPNext CRM both exist; better to build integration between them
- **Another IMAP/email app** — build on top of existing email, not replace it
- **Project management from scratch** — too many players (Asana, Jira, Monday.com); build connectors instead

---

## "Build This Instead" List

1. **PDC/Cheque Tracker** — lightweight, no Check Run dependency, linked to Payment Entry
2. **Hospitality Essentials** — hotel room management, folio, POS for hotels — fill the void left by archived `frappe/hospitality`
3. **SSO Gateway** — purpose-built OIDC connector for ERPNext with Keycloak/Okta/Auth0 support, logout propagation, and true SSO redirect
4. **Inbox Guardian** — fix IMAP sync behavior, support Gmail Groups, per-user notification sender
5. **Print Format Allocator** — assign and manage print formats per company, per doctype with a UI
6. **Migration Hub** — modular migration tool for QuickBooks Desktop, Sage, Tally with field mapping UI
7. **Employee Gear Locker** — track employee-issued items (gifts, equipment, uniforms) with HR and accounting linkage
8. **Workspace Builder** — no-code sidebar and workspace customization for non-technical users
9. **Task Sync Pro** — auto-update task progress from timesheet entries with dependency awareness
10. **QI Filter** — on Purchase Receipt / Stock Entry: only create Quality Inspection for rows where the flag is set

---

## Raw Signals (Topic IDs Referenced)

| Topic | Signal |
|---|---|
| 100079 | IMAP marks emails as read — unfixed bug |
| 100230 | Employee gift item issuance — no clean solution |
| 100539 | Gmail Group as email account — no native support |
| 101004 | Task progress auto-update — doesn't work |
| 101498 | Quality Inspection creates for all items — bug since 2023 |
| 101767 | Company-wise print format — no native solution |
| 102222 | Navbar customization from custom app — not possible without core hacks |
| 102423 | Keycloak OIDC blank page — known issue |
| 103596 | Sales person contact on quotation — requires manual field mapping |
| 103856 | Migrated doctypes uneditable — `validate_set_only_once` issue |
| 151169 | Push notifications for ERPNext/PWA — no app |
| 151216 | Sidebar customization — "paid feature, not free" |
| 153289 | **PDC/Cheque Management — direct market gap** |
| 155480 | **True SSO redirect flow with Keycloak — known gap** |
| 155913 | ERPNext CRM vs Frappe CRM confusion — no guidance |
| 156481 | Project management — ERPNext not enough for PMO |
| 156538 | Attendance status renaming — fragile workaround only |
| 156701 | Disable menu for website user — minor UX |
| 156851 | Education fees outstanding not reducing — regression bug |
| 156929 | **Hospitality app gap — `frappe/hospitality` archived** |
| 156990 | QuickBooks Desktop migration — no solution |
| 157103 | Owl Theme, Frappe Studio — existing UI options |
| 157119 | Comment mention notifications from wrong sender |
| 157854 | Scan Me app — newly released QR/barcode |
| 158127 | **MINT reconciliation bug — Transfer mode fails** |
