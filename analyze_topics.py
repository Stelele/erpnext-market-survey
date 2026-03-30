import json
import os
import re
from collections import defaultdict

TOPICS_DIR = r"C:\Users\Gifts Laptop\Documents\code-projects\sidehustles\opportunity-analysis\erpnext-forum\topics"
OUTPUT_DIR = r"C:\Users\Gifts Laptop\Documents\code-projects\sidehustles\opportunity-analysis"

def extract_text_from_html(html):
    """Strip HTML tags to get plain text."""
    if not html:
        return ""
    text = re.sub(r'<[^>]+>', ' ', html)
    text = re.sub(r'\s+', ' ', text)
    text = text.replace('&nbsp;', ' ').replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>').replace('&quot;', '"')
    return text.strip()

def strip_quotes(text):
    """Remove quote blocks from text."""
    lines = text.split('\n')
    result = []
    skip = False
    for line in lines:
        if '<blockquote>' in line or 'quote' in line.lower():
            skip = True
        if '</blockquote>' in line:
            skip = False
            continue
        if not skip:
            result.append(line)
    return '\n'.join(result)

# Load all topics
all_topics = []
files = sorted(os.listdir(TOPICS_DIR), key=lambda x: int(x.replace('.json','')))

for fname in files:
    if not fname.endswith('.json'):
        continue
    fpath = os.path.join(TOPICS_DIR, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    all_topics.append(data)

print(f"Loaded {len(all_topics)} topics")

# Extract all text content from each topic
for topic in all_topics:
    all_text = []
    for post in topic.get('posts', []):
        raw = post.get('cooked', '')
        plain = strip_quotes(extract_text_from_html(raw))
        all_text.append(plain)
    topic['_full_text'] = '\n'.join(all_text)
    topic['_title_plain'] = extract_text_from_html(topic.get('title', ''))

# Basic stats
total_views = sum(t.get('views', 0) for t in all_topics)
total_replies = sum(t.get('reply_count', 0) for t in all_topics)
total_likes = sum(t.get('like_count', 0) for t in all_topics)

print(f"Total views: {total_views:,}")
print(f"Total replies: {total_replies:,}")
print(f"Total likes: {total_likes:,}")

# Category distribution
cats = defaultdict(int)
for t in all_topics:
    cats[t.get('category_id', 0)] += 1
print("\nCategory distribution:")
for cat, count in sorted(cats.items(), key=lambda x: -x[1]):
    print(f"  cat {cat}: {count} topics")

# Top topics by views
print("\nTop 30 topics by views:")
for t in sorted(all_topics, key=lambda x: -x.get('views', 0))[:30]:
    title = t.get('title', '')[:80]
    print(f"  [{t['topic_id']}] views={t.get('views',0)} replies={t.get('reply_count',0)} likes={t.get('like_count',0)} | {title}")

# Top topics by replies
print("\nTop 20 topics by reply_count:")
for t in sorted(all_topics, key=lambda x: -x.get('reply_count', 0))[:20]:
    title = t.get('title', '')[:80]
    print(f"  [{t['topic_id']}] replies={t.get('reply_count',0)} views={t.get('views',0)} | {title}")

# Top topics by likes
print("\nTop 20 topics by likes:")
for t in sorted(all_topics, key=lambda x: -x.get('like_count', 0))[:20]:
    title = t.get('title', '')[:80]
    print(f"  [{t['topic_id']}] likes={t.get('like_count',0)} replies={t.get('reply_count',0)} | {title}")

# Search for key pain patterns
pain_patterns = {
    'reporting/analytics gap': ['report', 'dashboard', 'analytics', 'pivot', 'chart', 'summary report', 'custom report', 'report builder', 'sql report', 'bi tool', 'power bi', 'tableau'],
    'performance': ['slow', 'performance', 'lagging', 'loading', 'timeout', 'timeout', 'speed', 'takes forever', 'not responding', 'stuck'],
    'data migration': ['migration', 'migrate', 'import data', 'data import', 'bulk import', 'csv import', 'excel import', 'from tally', 'from quickbooks', 'from sap', 'from zoho'],
    'integration': ['integrate', 'integration', 'zapier', 'webhook', 'api', 'connect', 'woocommerce', 'shopify', 'tally', 'quickbooks'],
    'backup/export': ['backup', 'export', 'data portability', 'data export', 'download data', 'json export', 'csv export'],
    'compliance/gst/tax': ['gst', 'compliance', 'tax', 'tds', 'tcs', 'e-invoice', 'e-way bill', 'gst return', 'vat', 'pf', 'esi'],
    'email/imap': ['email', 'imap', 'smtp', 'email sync', 'email notification'],
    'ui/ux': ['ui', 'ux', 'user interface', 'confusing', 'hard to use', 'not intuitive', 'layout', 'design'],
    'customization': ['custom', 'customization', 'custom script', 'custom field', 'doctype', 'client script', 'server script', 'workspace'],
    'installation': ['install', 'installation', 'setup', 'docker', 'kubernetes', 'bench', 'upgrade', 'update', 'version upgrade', 'migration'],
    'multi-company': ['multi-company', 'multiple company', 'consolidation', 'consolidated'],
    'manufacturing': ['bom', 'manufacturing', 'work order', 'production', 'job card', 'subcontracting', 'subcontract'],
    'projects': ['project', 'task', 'timesheet', 'project management'],
    'accounting': ['accounting', 'journal entry', 'payment entry', 'invoice', 'payment', 'ledger', 'accounts'],
    'hr/payroll': ['hr', 'payroll', 'employee', 'leave', 'attendance', 'salary', 'recruitment'],
    'buying/selling': ['purchase', 'buying', 'selling', 'sales', 'quotation', 'sales order', 'purchase order'],
    'stock/inventory': ['stock', 'inventory', 'warehouse', 'stock entry', 'material'],
    'ai/openai': ['ai', 'openai', 'gpt', 'chatgpt', 'llm', 'artificial intelligence'],
    'banking': ['bank', 'banking', 'reconciliation', 'bank statement'],
    'print/format': ['print', 'print format', 'print format', 'letter', 'pdf', 'custom print'],
    'workaround/manual': ['workaround', 'manual', 'spreadsheet', 'excel', 'manually', 'outside erpnext', 'outside the system'],
    'is there an app': ['is there an app', 'is there a', 'is there any', 'any app', 'any tool', 'any extension', 'is there anything', 'does anyone know', 'looking for an app', 'looking for a', 'need an app', 'need a tool', 'is there no', 'there is no', 'no app'],
    'frustrated': ['frustrated', 'annoying', 'tired', 'waste of time', 'broken', 'bug', 'issue', 'problem', 'doesnt work', "doesn't work", 'not working', 'unable to', 'cannot', 'can not', 'error'],
    'willing to pay': ['willing to pay', 'ready to pay', 'happy to pay', 'budget', 'paying for', 'would pay', 'paid app', 'premium', 'subscription'],
    'workaround shared': ['i had to', 'workaround', 'manually', 'i use a script', 'i created a', 'i wrote a', 'custom script', 'i built a'],
}

pain_counts = defaultdict(list)

for pattern_name, keywords in pain_patterns.items():
    for t in all_topics:
        text = (t.get('_title_plain', '') + ' ' + t.get('_full_text', '')).lower()
        for kw in keywords:
            if kw.lower() in text:
                pain_counts[pattern_name].append(t['topic_id'])
                break

print("\n\n=== PAIN PATTERN COUNTS ===")
for pattern, topics in sorted(pain_counts.items(), key=lambda x: -len(x[1])):
    print(f"{pattern}: {len(topics)} topics")
    for tid in topics[:5]:
        print(f"  - {tid}")

# Save structured data for further analysis
structured = []
for t in all_topics:
    posts_text = []
    for post in t.get('posts', []):
        raw = post.get('cooked', '')
        plain = strip_quotes(extract_text_from_html(raw))
        if plain:
            posts_text.append(plain)
    structured.append({
        'topic_id': t['topic_id'],
        'title': t.get('title', ''),
        'title_plain': t.get('_title_plain', ''),
        'category_id': t.get('category_id', 0),
        'created_at': t.get('created_at', ''),
        'views': t.get('views', 0),
        'reply_count': t.get('reply_count', 0),
        'like_count': t.get('like_count', 0),
        'posts_text': '\n---\n'.join(posts_text),
    })

with open(os.path.join(OUTPUT_DIR, 'structured_topics.json'), 'w', encoding='utf-8') as f:
    json.dump(structured, f, ensure_ascii=False)

print(f"\nSaved structured topics to {os.path.join(OUTPUT_DIR, 'structured_topics.json')}")

# Keywords by category
print("\n\n=== TOP KEYWORDS IN TITLES ===")
title_words = defaultdict(int)
for t in all_topics:
    words = re.findall(r'\b[a-zA-Z]{4,}\b', t.get('title', '').lower())
    for w in words:
        title_words[w] += 1

for word, count in sorted(title_words.items(), key=lambda x: -x[1])[:60]:
    print(f"  {word}: {count}")

# Find topics with highest emotional weight (many replies + many views + mentions of frustration)
print("\n\n=== HIGH EMOTIONAL WEIGHT TOPICS ===")
for t in sorted(all_topics, key=lambda x: -(x.get('reply_count',0)*2 + x.get('views',0)//100 + x.get('like_count',0)*5)):
    text = t.get('_full_text', '').lower()
    title = t.get('title', '')
    emotional = any(w in text for w in ['frustrated', 'annoying', 'tired', 'waste', 'broken', 'bug', 'problem', 'doesnt work', "doesn't work", 'not working', 'error'])
    if emotional or t.get('reply_count', 0) >= 5:
        print(f"  [{t['topic_id']}] replies={t.get('reply_count',0)} views={t.get('views',0)} likes={t.get('like_count',0)} | {title[:80]}")
        if t.get('reply_count', 0) >= 10:
            print(f"    FIRST POST: {t.get('_full_text','')[:300]}")

# Find "is there an app/tool" topics - highest signal for unmet needs
print("\n\n=== 'IS THERE AN APP/TOOL' TOPICS (Unmet Needs) ===")
is_there_apps = []
for t in all_topics:
    text = (t.get('_title_plain', '') + ' ' + t.get('_full_text', '')).lower()
    if any(w in text for w in ['is there an app', 'is there a', 'is there any', 'any app', 'any tool', 'any extension', 'is there anything', 'does anyone know', 'looking for an app', 'looking for a', 'need an app', 'need a tool', 'is there no', 'there is no', 'no app', 'no tool', 'missing feature', 'lack of', 'no feature', 'feature request']):
        is_there_apps.append(t)

is_there_apps.sort(key=lambda x: -(x.get('views',0) + x.get('reply_count',0)*10))
for t in is_there_apps[:40]:
    print(f"\n[{t['topic_id']}] views={t.get('views',0)} replies={t.get('reply_count',0)}")
    print(f"  TITLE: {t.get('title','')}")
    print(f"  FIRST POST: {t.get('_full_text','')[:400]}")

# Save is_there_apps list
is_there_apps_data = [{'topic_id': t['topic_id'], 'title': t.get('title', ''), 'views': t.get('views',0), 'reply_count': t.get('reply_count',0), 'text': t.get('_full_text','')[:1000]} for t in is_there_apps]
with open(os.path.join(OUTPUT_DIR, 'is_there_apps.json'), 'w', encoding='utf-8') as f:
    json.dump(is_there_apps_data, f, ensure_ascii=False)

print(f"\nSaved is_there_apps to {os.path.join(OUTPUT_DIR, 'is_there_apps.json')}")

# Workaround/workarounds patterns
print("\n\n=== WORKAROUND PATTERNS ===")
workarounds = []
for t in all_topics:
    text = t.get('_full_text', '').lower()
    if any(w in text for w in ['workaround', 'i had to', 'manually', 'i use a script', 'i created a', 'i wrote a', 'custom script', 'i built a', 'i use a python script', 'i wrote a script', 'excel sheet', 'spreadsheet']):
        workarounds.append(t)

workarounds.sort(key=lambda x: -(x.get('views',0) + x.get('reply_count',0)*10))
for t in workarounds[:30]:
    print(f"\n[{t['topic_id']}] views={t.get('views',0)} replies={t.get('reply_count',0)}")
    print(f"  TITLE: {t.get('title','')}")
    # Find relevant snippet
    text = t.get('_full_text', '')
    for snippet in text.split('\n'):
        if any(w in snippet.lower() for w in ['workaround', 'i had to', 'manually', 'custom script', 'spreadsheet']):
            print(f"  SNIPPET: {snippet[:200]}")
            break

print(f"\nTotal workaround topics: {len(workarounds)}")

# Willing to pay signals
print("\n\n=== WILLING TO PAY SIGNALS ===")
willing = []
for t in all_topics:
    text = t.get('_full_text', '').lower()
    if any(w in text for w in ['willing to pay', 'ready to pay', 'happy to pay', 'budget', 'paying for', 'would pay', 'paid app', 'premium app', 'paid solution', 'paid tool']):
        willing.append(t)

for t in willing:
    print(f"\n[{t['topic_id']}] views={t.get('views',0)} replies={t.get('reply_count',0)}")
    print(f"  TITLE: {t.get('title','')}")
    text = t.get('_full_text', '')
    for line in text.split('\n'):
        if any(w in line.lower() for w in ['willing to pay', 'ready to pay', 'happy to pay', 'budget', 'paying', 'would pay', 'paid app', 'premium']):
            print(f"  SIGNAL: {line[:300]}")
            break

print(f"\nTotal willing-to-pay topics: {len(willing)}")
