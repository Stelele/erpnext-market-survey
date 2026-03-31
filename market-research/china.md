# ERPNext China Market Research

**Date:** March 2026
**Market:** China — unique challenges, infrastructure barriers, Gitee ecosystem

---

## Community Infrastructure

| Platform | Channel | Language |
|----------|---------|----------|
| Telegram | t.me/erpnext_china | Chinese |
| Telegram | t.me/frappe_cn | Chinese |
| GitHub | github.com/SolutionAlliance/erpnext_chinese | 2 stars |
| GitHub | github.com/berquip/erpnext_chinese | — |
| Gitee | gitee.com/yuzelin/erpnext_chinese | 202 stars, 173 forks |
| Gitee | gitee.com/yuzelin/erpnext_china | Active Chinese localization |
| GitHub | github.com/guinanlin/erpnext-zh-doc | ERPNext中文手册 |

**Key community member:** 余则霖 (szufisher) — Gitee maintainer with significant contribution history

---

## Market Fundamentals

### ERPNext Adoption in China
- Minimal penetration vs. local ERPs
- Concentrated among: foreign subsidiaries in China, tech companies, companies with international operations
- Self-hosted only — Frappe Cloud not accessible in China

### Dominant Competitors
- **Kingdee (金蝶):** ~15% market share, cloud/SaaS ERP, dominant in SMB
- **Yonyou (用友):** ~20% market share, enterprise focus
- **Baiyong (用友优普):** Enterprise
- **SAP (China):** Large enterprises, expensive
- **Infor:** Some presence
- **Neusoft (东软):** Manufacturing focus

---

## Chinese Localization Repos

### gitee.com/yuzelin/erpnext_chinese
- **202 stars, 173 forks** — most popular Chinese localization
- Contains: UI translation, Chinese language files
- Active development
- Contact: 余则霖 (szufisher)

### gitee.com/yuzelin/erpnext_china
- Active Chinese localization project
- Same maintainer as above

### github.com/guinanlin/erpnext-zh-doc
- ERPNext中文手册 (Chinese manual)
- Documentation project
- Stars unknown

### What these repos contain:
- Chinese (Simplified) UI translations
- Basic Chinese language pack
- **What's missing:** Chinese compliance, Fapiao, Golden Tax, WeChat integration

---

## Compliance Requirements

### Fapiao (发票) — THE Critical Gap
Fapiao is China's electronic invoice system. It's mandatory for:
- Deducting business expenses
- VAT input credit
- Audit compliance

**Fapiao types:**
- **VAT Fapiao (增值税发票):** Standard business invoice
- **Receipt Fapiao (普通发票):** Simplified for small purchases
- **Special Fapiao (专用发票):** For VAT input credit

**ERPNext Fapiao status:** NOT IMPLEMENTED. This is a hard blocker for Chinese companies.

### Golden Tax System (金税工程)
China's tax authority computer system:
- Connects to SAT (State Administration of Taxation)
- Real-time monitoring of VAT
- Cross-references with invoice data

**ERPNext Golden Tax integration:** NOT IMPLEMENTED. Would require government partnership.

### Baiwang (百望) / Other E-Invoice Providers
Third-party Fapiao service providers:
- Baiwang (百望云)
- Baijijine (百鸡金鹅)
- Wotu (我图)

These provide Fapiao API access for a fee. ERPNext integration with these is NOT built.

---

## Infrastructure Challenges

### The Great Firewall Problem
- **Frappe Cloud:** Not accessible in China
- **GitHub:** Accessible but slow
- **Gitee:** Chinese alternative to GitHub, accessible in China

**Implication:** Chinese ERPNext deployments must be self-hosted on Chinese cloud infrastructure.

### Chinese Cloud Infrastructure
- **Alibaba Cloud (阿里云):** Most popular, ERPNext deployable
- **Tencent Cloud (腾讯云):** Second largest
- **Baidu Cloud (百度云):** Less relevant for business
- **Huawei Cloud (华为云):** Growing

ERPNext deployment on Alibaba Cloud: feasible but non-trivial. Docker + custom server setup required.

### WeChat Integration
WeChat is ubiquitous in China for business communication:
- **WeChat Work (企业微信):** Like Slack for business
- **WeChat Pay:** Dominant payment method
- **Mini Programs:** Lightweight apps

ERPNext-WeChat integration: NOT built. This is a major gap for Chinese market fit.

---

## Chinese Localization Gaps

### Current Status
- Basic UI translation: EXISTS (yuzelin/erpnext_chinese on Gitee)
- Chinese accounting terminology: PARTIAL
- Fapiao management: NOT IMPLEMENTED
- Golden Tax integration: NOT IMPLEMENTED
- Chinese chart of accounts: NOT STANDARDIZED
- WeChat integration: NOT IMPLEMENTED
- DingTalk integration: NOT IMPLEMENTED
- Alipay/WeChat Pay: NOT IMPLEMENTED
- ICP license handling: NOT DOCUMENTED

---

## Opportunity Analysis

### OPP-CN-01: Fapiao Management Module
**Priority: CRITICAL** | **Confidence: 9/10**

Fapiao is mandatory for business operations in China. ERPNext has zero Fapiao support.

**What's needed:**
- Fapiao issuance (output)
- Fapiao receipt (input) management
- Fapiao verification via Baiwang/Wotu API
- Fapiao archive
- VAT calculation matching Fapiao data

**Build difficulty:** Very High. Requires Baiwang or similar API partnership.

**Pricing:** ¥500-2,000/month SaaS. ¥10,000-50,000 one-time.

---

### OPP-CN-02: Chinese Cloud Deployment Toolkit
**Priority: HIGH** | **Confidence: 8/10**

ERPNext is hard to deploy on Chinese cloud infrastructure.

**What's needed:**
- One-click ERPNext deployment on Alibaba Cloud ECS
- Docker image optimized for Chinese networks
- Nginx/SSL configuration for Chinese SSL requirements
- Backup to OSS (Alibaba Object Storage)
- One-click Frappe Cloud alternative for China

**Pricing:** ¥200-500/month managed hosting in China. ¥5,000-15,000 setup.

---

### OPP-CN-03: WeChat Work / DingTalk Integration
**Priority: MEDIUM** | **Confidence: 7/10**

Chinese businesses live in WeChat Work/DingTalk.

**What's needed:**
- ERPNext notifications to WeChat Work/DingTalk
- Approval workflows via WeChat Work
- Employee directory sync
- Document sharing to WeChat

**Pricing:** ¥500-2,000/month integration.

---

### OPP-CN-04: Chinese Accounting Template Pack
**Priority: MEDIUM** | **Confidence: 7/10**

Standard Chinese chart of accounts based on Chinese accounting standards.

**What's needed:**
- Chinese accounting standard (CAS/ASBE) compliant chart of accounts
- Chinese financial statement formats
- Tax account mapping (VAT, Corporate Income Tax, Individual Income Tax)

---

### OPP-CN-05: Alipay / WeChat Pay Integration
**Priority: MEDIUM** | **Confidence: 6/10**

Payment integration for Chinese customers who overwhelmingly use Alipay and WeChat Pay.

**What's needed:** ERPNext payment gateway integration for Alipay and WeChat Pay.

---

## Why ERPNext in China Is Hard

1. **Compliance is government-mandated** — Fapiao, Golden Tax are not optional
2. **Infrastructure is isolated** — no Frappe Cloud, GitHub slow
3. **Local ERP lock-in** — Kingdee/Yonyou have 20+ years of China-specific development
4. **Language barrier** — ERPNext community has minimal Chinese presence
5. **ICP license** — websites in China need ICP license (months to obtain)

---

## Realistic Assessment

**China is the hardest market to enter** but potentially the largest.

**Best approach for solo founder:** Not China. The compliance requirements (Fapiao, Golden Tax) require government partnerships or years of development. Better to focus on markets where ERPNext can be adapted without needing state-level integrations.

**Exception:** Chinese cloud deployment toolkit (OPP-CN-02) is buildable by a solo developer without government dependencies.

---

## New Personas Identified

1. **Great Firewall Escapee** — Chinese company seeking international-standard ERP for cross-border operations. Needs Chinese UI but foreign-standard accounting.
2. **Fapiao Manager** — Chinese accounting specialist obsessed with Fapiao compliance. Cannot recommend ERPNext without Fapiao support.
3. **WeChat-First Founder** — building WeChat/DingTalk-integrated ERPNext tools. Evaluates every product on WeChat compatibility.
4. **Alibaba Cloud Native** — developer comfortable only with Chinese cloud infrastructure (Alibaba Cloud, Tencent Cloud).
