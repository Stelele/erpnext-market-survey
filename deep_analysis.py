import json
import re
from collections import defaultdict

# Load structured topics
with open(r"C:\Users\Gifts Laptop\Documents\code-projects\sidehustles\opportunity-analysis\structured_topics.json", 'r', encoding='utf-8') as f:
    topics = json.load(f)

print(f"Loaded {len(topics)} structured topics")

# ====== DEEP DIVE: ERPNext module friction analysis ======
# Category 6 = ERPNext, 7 = Frappe Framework, 8 = Email, 9 = Installation, 11 = Docker, 19 = Setup, 26 = Performance
# Let's categorize by topic content for modules

module_keywords = {
    'Accounting & Finance': ['accounting', 'journal entry', 'payment entry', 'invoice', 'payment', 'ledger', 'accounts', 'finance', 'tax', 'gst', 'tds', 'tcs', 'fiscal', 'coa', 'chart of accounts', 'asset', 'depreciation', 'cost center', 'budget', 'bank reconciliation'],
    'Sales & CRM': ['crm', 'customer', 'lead', 'opportunity', 'contact', 'quotation', 'sales order', 'sales invoice', 'customer portal', 'selling', 'territory', 'campaign', 'newsletter'],
    'Buying & Procurement': ['purchase', 'purchase order', 'purchase invoice', 'supplier', 'buying', 'material request', 'request for quotation', 'rfq', 'procurement', 'supplier quotation'],
    'Stock & Inventory': ['stock', 'inventory', 'warehouse', 'stock entry', 'material', 'item', 'stock reconciliation', 'stock balance', 'serial no', 'batch', 'bin', 'uom', 'valuation'],
    'Manufacturing': ['bom', 'manufacturing', 'work order', 'production', 'job card', 'subcontracting', 'subcontract', 'production plan', 'routing', 'operation'],
    'Projects & HRM': ['project', 'task', 'timesheet', 'hr', 'payroll', 'employee', 'leave', 'attendance', 'salary', 'recruitment', 'onboarding', 'appraisal', 'expense claim', 'advance', 'holiday'],
    'Website & Portal': ['website', 'portal', 'web page', 'blog', 'webform', 'ecommerce', 'shopping cart', 'marketplace'],
    'ERPNext Setup & Config': ['setup', 'configuration', 'company', 'fiscal year', 'system', 'permission', 'workflow', 'print format', 'letter head', 'custom field'],
    'Frappe Development': ['doctype', 'custom script', 'client script', 'server script', 'app', 'frappe app', 'bench', 'python', 'javascript', 'api', 'webhook', 'workspace'],
    'Infrastructure & Hosting': ['install', 'docker', 'kubernetes', 'server', 'hosting', 'nginx', 'redis', 'database', 'mariadb', 'postgres', 'backup', 'migration', 'upgrade', 'v14', 'v15', 'v16'],
    'Integrations': ['integration', 'woocommerce', 'shopify', 'api', 'webhook', 'zapier', 'tally', 'quickbooks', 'gmail', 'imap', 'email sync', 'payment gateway', 'razorpay', 'stripe'],
    'PDF & Print': ['pdf', 'print', 'wkhtmltopdf', 'print format', 'letter head', 'invoice format', 'delivery note'],
    'Reports & Analytics': ['report', 'dashboard', 'analytics', 'script report', 'query report', 'pivot', 'chart', 'bi', 'power bi', 'tableau'],
    'Banking & Payments': ['bank', 'banking', 'reconciliation', 'bank statement', 'payment gateway', 'payment entry', 'payment request', 'pos'],
}

module_counts = defaultdict(list)
for t in topics:
    text = (t.get('title_plain', '') + ' ' + t.get('posts_text', '')).lower()
    for module, keywords in module_keywords.items():
        for kw in keywords:
            if kw in text:
                module_counts[module].append(t['topic_id'])
                break

print("\n=== MODULE FRICTION MAP ===")
for module, tids in sorted(module_counts.items(), key=lambda x: -len(x[1])):
    print(f"{module}: {len(tids)} topics")

# ====== DEEP DIVE: Reporting & Analytics ======
print("\n\n=== REPORTING & ANALYTICS DEEP DIVE ===")
for t in topics:
    text = (t.get('title_plain', '') + ' ' + t.get('posts_text', '')).lower()
    if any(kw in text for kw in ['report', 'dashboard', 'analytics', 'pivot', 'chart', 'script report', 'query report']):
        t['_relevance'] = sum(1 for kw in ['report builder', 'custom report', 'dashboard', 'analytics', 'pivot', 'bi tool', 'power bi', 'tableau', 'script report', 'query report'] if kw in text)

reporting_topics = [t for t in topics if t.get('_relevance', 0) > 0]
reporting_topics.sort(key=lambda x: -x.get('views', 0))
for t in reporting_topics[:20]:
    print(f"\n[{t['topic_id']}] views={t.get('views',0)} replies={t.get('reply_count',0)}")
    print(f"  {t['title'][:100]}")
    # Find the most relevant snippet
    text = t['posts_text']
    for line in text.split('\n'):
        if any(kw in line.lower() for kw in ['report builder', 'custom report', 'dashboard', 'analytics', 'pivot', 'bi', 'script report', 'query report']):
            print(f"  > {line[:200]}")
            break

# ====== DEEP DIVE: Compliance/GST ======
print("\n\n=== COMPLIANCE/TAX DEEP DIVE ===")
compliance_keywords = ['gst', 'e-invoice', 'e-way bill', 'peppol', 'tds', 'tcs', 'compliance', 'tax return', 'gst return', 'vat', 'belgian', 'india compliance']
for t in topics:
    text = (t.get('title_plain', '') + ' ' + t.get('posts_text', '')).lower()
    t['_compliance_relevance'] = sum(1 for kw in compliance_keywords if kw in text)

compliance_topics = [t for t in topics if t.get('_compliance_relevance', 0) > 0]
compliance_topics.sort(key=lambda x: -x.get('views', 0))
for t in compliance_topics[:20]:
    print(f"\n[{t['topic_id']}] views={t.get('views',0)} replies={t.get('reply_count',0)}")
    print(f"  {t['title'][:100]}")
    text = t['posts_text']
    for line in text.split('\n'):
        if any(kw in line.lower() for kw in compliance_keywords):
            print(f"  > {line[:200]}")
            break

# ====== DEEP DIVE: Data Migration ======
print("\n\n=== DATA MIGRATION DEEP DIVE ===")
migration_keywords = ['migrate', 'migration', 'import data', 'data import', 'bulk import', 'csv import', 'excel import', 'from tally', 'from quickbooks', 'from sap', 'from zoho', 'from dolibarr', 'from odoo']
for t in topics:
    text = (t.get('title_plain', '') + ' ' + t.get('posts_text', '')).lower()
    t['_migration_relevance'] = sum(1 for kw in migration_keywords if kw in text)

migration_topics = [t for t in topics if t.get('_migration_relevance', 0) > 0]
migration_topics.sort(key=lambda x: -x.get('views', 0))
for t in migration_topics[:15]:
    print(f"\n[{t['topic_id']}] views={t.get('views',0)} replies={t.get('reply_count',0)}")
    print(f"  {t['title'][:100]}")
    text = t['posts_text']
    for line in text.split('\n'):
        if any(kw in line.lower() for kw in migration_keywords):
            print(f"  > {line[:200]}")
            break

# ====== DEEP DIVE: Integration ======
print("\n\n=== INTEGRATION ECOSYSTEM DEEP DIVE ===")
integration_keywords = ['woocommerce', 'shopify', 'zapier', 'webhook', 'api', 'tally', 'quickbooks', 'razorpay', 'stripe', 'payment gateway', 'twilio', 'slack', 'discord']
for t in topics:
    text = (t.get('title_plain', '') + ' ' + t.get('posts_text', '')).lower()
    t['_integration_relevance'] = sum(1 for kw in integration_keywords if kw in text)

integration_topics = [t for t in topics if t.get('_integration_relevance', 0) > 0]
integration_topics.sort(key=lambda x: -x.get('views', 0))
for t in integration_topics[:20]:
    print(f"\n[{t['topic_id']}] views={t.get('views',0)} replies={t.get('reply_count',0)}")
    print(f"  {t['title'][:100]}")
    text = t['posts_text']
    for line in text.split('\n'):
        if any(kw in line.lower() for kw in integration_keywords):
            print(f"  > {line[:200]}")
            break

# ====== DEEP DIVE: Performance ======
print("\n\n=== PERFORMANCE DEEP DIVE ===")
perf_keywords = ['slow', 'performance', 'lagging', 'loading', 'timeout', 'timeout', 'speed', 'not responding', 'stuck', 'takes long', 'heavy', 'large data', 'many users']
for t in topics:
    text = (t.get('title_plain', '') + ' ' + t.get('posts_text', '')).lower()
    t['_perf_relevance'] = sum(1 for kw in perf_keywords if kw in text)

perf_topics = [t for t in topics if t.get('_perf_relevance', 0) > 0]
perf_topics.sort(key=lambda x: -x.get('views', 0))
for t in perf_topics[:15]:
    print(f"\n[{t['topic_id']}] views={t.get('views',0)} replies={t.get('reply_count',0)}")
    print(f"  {t['title'][:100]}")
    text = t['posts_text']
    for line in text.split('\n'):
        if any(kw in line.lower() for kw in perf_keywords):
            print(f"  > {line[:200]}")
            break

# ====== DEEP DIVE: Customization/Development Pain ======
print("\n\n=== CUSTOMIZATION/DEV PAIN DEEP DIVE ===")
custom_keywords = ['custom script', 'client script', 'server script', 'doctype', 'custom field', 'workspace', 'custom app', 'frappe app', 'bench', 'python script', 'api', 'webhook']
for t in topics:
    text = (t.get('title_plain', '') + ' ' + t.get('posts_text', '')).lower()
    t['_custom_relevance'] = sum(1 for kw in custom_keywords if kw in text)

custom_topics = [t for t in topics if t.get('_custom_relevance', 0) > 0]
custom_topics.sort(key=lambda x: -x.get('views', 0))
for t in custom_topics[:20]:
    print(f"\n[{t['topic_id']}] views={t.get('views',0)} replies={t.get('reply_count',0)}")
    print(f"  {t['title'][:100]}")
    text = t['posts_text']
    for line in text.split('\n'):
        if any(kw in line.lower() for kw in custom_keywords):
            print(f"  > {line[:200]}")
            break

# ====== DEEP DIVE: AI Integration ======
print("\n\n=== AI INTEGRATION DEEP DIVE ===")
ai_keywords = ['ai', 'openai', 'gpt', 'chatgpt', 'llm', 'artificial intelligence', 'machine learning', 'automation', 'agent', 'copilot']
for t in topics:
    text = (t.get('title_plain', '') + ' ' + t.get('posts_text', '')).lower()
    t['_ai_relevance'] = sum(1 for kw in ai_keywords if kw in text)

ai_topics = [t for t in topics if t.get('_ai_relevance', 0) > 0]
ai_topics.sort(key=lambda x: -x.get('views', 0))
for t in ai_topics[:25]:
    print(f"\n[{t['topic_id']}] views={t.get('views',0)} replies={t.get('reply_count',0)}")
    print(f"  {t['title'][:100]}")
    text = t['posts_text']
    for line in text.split('\n'):
        if any(kw in line.lower() for kw in ai_keywords):
            print(f"  > {line[:200]}")
            break

# ====== DEEP DIVE: Payroll/HR Pain ======
print("\n\n=== PAYROLL/HR PAIN DEEP DIVE ===")
hr_keywords = ['payroll', 'salary', 'leave', 'attendance', 'employee', 'recruitment', 'expense claim', 'advance', 'holiday', 'appraisal', 'onboarding']
for t in topics:
    text = (t.get('title_plain', '') + ' ' + t.get('posts_text', '')).lower()
    t['_hr_relevance'] = sum(1 for kw in hr_keywords if kw in text)

hr_topics = [t for t in topics if t.get('_hr_relevance', 0) > 0]
hr_topics.sort(key=lambda x: -x.get('views', 0))
for t in hr_topics[:20]:
    print(f"\n[{t['topic_id']}] views={t.get('views',0)} replies={t.get('reply_count',0)}")
    print(f"  {t['title'][:100]}")
    text = t['posts_text']
    for line in text.split('\n'):
        if any(kw in line.lower() for kw in hr_keywords):
            print(f"  > {line[:200]}")
            break

# ====== DEEP DIVE: Backup/Export ======
print("\n\n=== BACKUP/EXPORT/PORTABILITY DEEP DIVE ===")
backup_keywords = ['backup', 'export data', 'data portability', 'data export', 'download data', 'json export', 'csv export', 'migrate data']
for t in topics:
    text = (t.get('title_plain', '') + ' ' + t.get('posts_text', '')).lower()
    t['_backup_relevance'] = sum(1 for kw in backup_keywords if kw in text)

backup_topics = [t for t in topics if t.get('_backup_relevance', 0) > 0]
backup_topics.sort(key=lambda x: -x.get('views', 0))
for t in backup_topics[:15]:
    print(f"\n[{t['topic_id']}] views={t.get('views',0)} replies={t.get('reply_count',0)}")
    print(f"  {t['title'][:100]}")
    text = t['posts_text']
    for line in text.split('\n'):
        if any(kw in line.lower() for kw in backup_keywords):
            print(f"  > {line[:200]}")
            break

# ====== DEEP DIVE: PDF/Print issues ======
print("\n\n=== PDF/PRINT DEEP DIVE ===")
pdf_keywords = ['pdf', 'wkhtmltopdf', 'print', 'print format', 'invoice format']
for t in topics:
    text = (t.get('title_plain', '') + ' ' + t.get('posts_text', '')).lower()
    t['_pdf_relevance'] = sum(1 for kw in pdf_keywords if kw in text)

pdf_topics = [t for t in topics if t.get('_pdf_relevance', 0) > 0]
pdf_topics.sort(key=lambda x: -x.get('views', 0))
for t in pdf_topics[:15]:
    print(f"\n[{t['topic_id']}] views={t.get('views',0)} replies={t.get('reply_count',0)}")
    print(f"  {t['title'][:100]}")
    text = t['posts_text']
    for line in text.split('\n'):
        if any(kw in line.lower() for kw in pdf_keywords):
            print(f"  > {line[:200]}")
            break

# ====== DEEP DIVE: POS ======
print("\n\n=== POS DEEP DIVE ===")
for t in topics:
    text = (t.get('title_plain', '') + ' ' + t.get('posts_text', '')).lower()
    if 'pos' in text:
        t['_pos_relevance'] = 1

pos_topics = [t for t in topics if t.get('_pos_relevance', 0) > 0]
pos_topics.sort(key=lambda x: -x.get('views', 0))
for t in pos_topics[:15]:
    print(f"\n[{t['topic_id']}] views={t.get('views',0)} replies={t.get('reply_count',0)}")
    print(f"  {t['title'][:100]}")
    text = t['posts_text']
    for line in text.split('\n'):
        if 'pos' in line.lower():
            print(f"  > {line[:200]}")
            break

# ====== DEEP DIVE: Multi-company ======
print("\n\n=== MULTI-COMPANY DEEP DIVE ===")
for t in topics:
    text = (t.get('title_plain', '') + ' ' + t.get('posts_text', '')).lower()
    if any(kw in text for kw in ['multi-company', 'multiple company', 'consolidation', 'consolidated report', 'multi company']):
        t['_multicompany'] = 1

mc_topics = [t for t in topics if t.get('_multicompany', 0) > 0]
mc_topics.sort(key=lambda x: -x.get('views', 0))
for t in mc_topics:
    print(f"\n[{t['topic_id']}] views={t.get('views',0)} replies={t.get('reply_count',0)}")
    print(f"  {t['title'][:100]}")
    text = t['posts_text']
    for line in text.split('\n'):
        if any(kw in line.lower() for kw in ['multi-company', 'multiple company', 'consolidation', 'multi company']):
            print(f"  > {line[:200]}")
            break

# ====== Most unanswered questions ======
print("\n\n=== UNANSWERED / LOW-REPLY HIGH-VIEWS QUESTIONS ===")
for t in topics:
    if t.get('reply_count', 0) <= 2 and t.get('views', 0) >= 1000:
        text = t.get('posts_text', '').lower()
        if any(w in text for w in ['is there', 'any app', 'looking for', 'need a', 'does anyone', 'how do i', 'how can i', 'why does', 'why is']):
            print(f"\n[{t['topic_id']}] views={t.get('views',0)} replies={t.get('reply_count',0)}")
            print(f"  {t['title'][:100]}")
            print(f"  {t['posts_text'][:300]}")

# ====== Emotional hot spots - high engagement + frustration ======
print("\n\n=== EMOTIONAL HOT SPOTS (High views + High replies + Frustration) ===")
frustration_words = ['frustrated', 'annoying', 'tired', 'waste of time', 'broken', 'bug', 'issue', 'problem', 'doesnt work', "doesn't work", 'not working', 'unable to', 'cannot', "can't", 'error', 'desperate', 'helpless', 'horrible', 'awful', 'disappointed', 'unacceptable']

for t in topics:
    text = t.get('posts_text', '').lower()
    t['_frustration_score'] = sum(1 for w in frustration_words if w in text)
    t['_engagement_score'] = t.get('views', 0) + t.get('reply_count', 0) * 10 + t.get('like_count', 0) * 5

hot_topics = [t for t in topics if t.get('_frustration_score', 0) >= 2 and t.get('reply_count', 0) >= 5]
hot_topics.sort(key=lambda x: -x.get('_engagement_score', 0))
for t in hot_topics[:20]:
    print(f"\n[{t['topic_id']}] views={t.get('views',0)} replies={t.get('reply_count',0)} likes={t.get('like_count',0)} frustration={t.get('_frustration_score',0)}")
    print(f"  {t['title'][:100]}")
    # Find frustrating snippets
    for line in t['posts_text'].split('\n'):
        if any(w in line.lower() for w in frustration_words):
            print(f"  FRUSTRATION: {line[:200]}")
            break

# ====== Summary statistics ======
print("\n\n=== SUMMARY STATISTICS ===")
print(f"Total topics: {len(topics)}")
print(f"Total views: {sum(t.get('views',0) for t in topics):,}")
print(f"Total replies: {sum(t.get('reply_count',0) for t in topics):,}")
print(f"Total likes: {sum(t.get('like_count',0) for t in topics):,}")

# Average engagement by category
cats = defaultdict(lambda: {'count': 0, 'views': 0, 'replies': 0, 'likes': 0})
for t in topics:
    cats[t.get('category_id', 0)]['count'] += 1
    cats[t.get('category_id', 0)]['views'] += t.get('views', 0)
    cats[t.get('category_id', 0)]['replies'] += t.get('reply_count', 0)
    cats[t.get('category_id', 0)]['likes'] += t.get('like_count', 0)

print("\nCategory engagement:")
for cat, data in sorted(cats.items(), key=lambda x: -x[1]['views']):
    avg_v = data['views'] / data['count'] if data['count'] else 0
    avg_r = data['replies'] / data['count'] if data['count'] else 0
    print(f"  cat {cat}: {data['count']} topics, {data['views']:,} views (avg {avg_v:.0f}), {data['replies']} replies (avg {avg_r:.1f})")
