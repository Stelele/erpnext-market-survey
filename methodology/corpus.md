# Data Sources & Corpus Documentation

**Date:** March 2026  
**Scope:** English-language forum, bootstrapper transcript corpus, non-English market research

---

## Primary Data Sources

### 1. Frappe Forum (discuss.frappe.io)

**What:** 1,742 forum topic files in `erpnext-forum/topics/`  
**Format:** JSON — one file per topic  
**Fields per topic:** `id`, `title`, `author`, `created`, `view_count`, `like_count`, `reply_count`, `tags`, `content`  
**Date range:** Topics captured up to March 2026  
**Storage location:** `erpnext-forum/topics/[topic-id].json`

**Content characteristics:**
- Primary language: English
- User base: Global but skews English-speaking
- Topic types: Feature requests, bug reports, how-to questions, implementation advice, plugin recommendations
- Notable topics: Some topics have 4,000+ views indicating broad community interest

**Known biases:**
- Skews toward English-speaking users and Western markets
- India is detectable through content (Tally, GST, Multi-GSTIN discussions) but India-specific Telegram channels are not in the forum corpus
- Very few topics from China, Brazil, Germany, or Africa despite significant ERPNext adoption in those markets
- Implementation advice and consulting signals are common; explicit WTP signals are rare
- Self-hosted vs. Frappe Cloud distinction matters — self-hosted users face different problems than cloud users

**Sample topic structure:**
```json
{
  "id": 150923,
  "title": "Looking for realistic seed data for ERPNext demos",
  "author": "erpnext_implementer",
  "created": "2025-10-15T14:32:00Z",
  "view_count": 847,
  "like_count": 23,
  "reply_count": 12,
  "tags": ["seed-data", "demo", "implementation"],
  "content": "We have a budget of $5,000 USD if someone can provide realistic seed data for demos..."
}
```

**Corpus statistics:**
- Total topics: 1,742
- Topics with 100+ views: ~800
- Topics with 1,000+ views: ~120
- Topics with explicit pricing/WTP signals: ~40
- India-tagged topics: ~60

---

### 2. Bootstrapper Transcript Corpus

**What:** 1,304 transcript files from three sources used to generate the 46 analytical personas  
**Location:** `bootstrappers/`

#### MicroConf (486 transcript files)
**Source:** YouTube video transcripts from MicroConf events  
**Location:** `bootstrappers/MicroConf/`  
**Naming convention:** `[Video Title] [YouTube ID].en.txt`  
**Coverage:** Bootstrapped founder tactics, SaaS growth strategy, marketing, pricing, hiring, exit planning  
**Notable series:** Patrick McKenzie talks, Rob Walling SaaS plateaus, Pieter Levels, Daniel Vassallo

#### Rob Walling (486 transcript files)
**Source:** YouTube video transcripts from Rob Walling's channel and MicroConf appearances  
**Location:** `bootstrappers/RobWalling/`  
**Naming convention:** `[Video Title] [YouTube ID].en.txt`  
**Coverage:** SaaS ideas, pricing strategy, outbound sales, acquisition, exit planning, TinySeed accelerator content  
**Notable:** 486 individual video files covering every conceivable SaaS topic

#### The Bootstrapped Founder (332 transcript files)
**Source:** Podcast episode transcripts from The Bootstrapped Founder (hosted by Arvid Kahl)  
**Location:** `bootstrappers/TheBootstrappedFounder/`  
**Naming convention:** `[Episode Title] [YouTube ID].en.txt`  
**Coverage:** Modern bootstrapping philosophy, AI tools, community building, mental models, founder stories  
**Notable series:** Moat series, productive procrastination, ownership paradox, virality, vanity validation, data flywheel, castle building, constraints navigation

#### Summaries (1 file)
**Location:** `bootstrappers/summaries.md`  
**Content:** 16 fully summarized transcripts with structured analysis  
**Use:** Primary extraction source for persona definitions  
**Format per summary:** Speaker, core thesis, methodology/framework, key quotes, concrete techniques, unique tendencies

---

### 3. Non-English Market Research

**What:** Web research, GitHub repository analysis, and Telegram community mapping for 8 regions  
**No new forum data** was added for non-English markets — research was conducted via web search and community mapping.

**Sources used:**
- Telegram (public channels — country-specific ERPNext communities)
- GitHub/Gitee (localization repositories per country)
- Frappe.io Partner Directory
- discuss.frappe.io (India-tagged discussions only)
- Web search (regulatory requirements, e-invoicing mandates, compliance deadlines)
- Company websites (implementation partner pricing, services offered)

**Regions researched:**
| Region | Primary Sources | GitHub Repos Found | Telegram Channels Found |
|--------|--------------|------------------|----------------------|
| India | Forum, GitHub, Web | 3+ repos | 7 channels |
| Brazil | GitHub, Web | 5 repos | 2 channels |
| Germany | GitHub, Web | 6 repos | 4 channels |
| MENA | GitHub, Web | 2 repos | 12+ channels |
| Africa | GitHub, Web | 5 repos | 5 channels |
| China | Gitee, GitHub, Web | 4 repos | 2 channels |
| Southeast Asia | GitHub, Web | 1 repo | 6 channels |
| Latin America | GitHub, Web | 0 repos | 7 channels |

**Limitations of non-English research:**
- Telegram channels provide community signals but not deep topic content
- GitHub repos indicate development activity but not user demand volume
- Compliance requirements were researched via web search, not primary sources
- Pricing data for non-English markets is estimated from implementation partner websites and job postings, not confirmed sales

---

## Persona Provenance

The 46 personas were generated from the bootstrapper transcript corpus through a structured extraction process:

**Step 1 — Full summaries read.** 16 transcripts were fully summarized in `bootstrappers/summaries.md` (523 lines). These covered:
- The Bootstrapped Founder episodes on: AI solopreneurs, biggest opportunities, data moats
- Daniel Vassallo on small bets
- Rob Walling on tactics, SaaS plateaus, SaaS ideas
- Patrick McKenzie on marketing, leveling up
- Pawel Brzeminski on validation, speed
- MicroConf series on boring micro-SaaS ideas
- Podscan on profitability, dream customer strategy
- Multiple episodes on moats, calm SaaS, productive procrastination, virality, ownership paradox

**Step 2 — Persona pattern identification.** Across the 16 summaries, 6 recurring founder archetypes were identified as particularly well-suited for opportunity analysis:
1. Community Listener — finds pain through forum/community immersion
2. Pre-Sale Interrogator — validates with money before building
3. Stair-Step Market Sizer — consulting → productized service → SaaS
4. Alternative Solution Auditor — researches all alternatives before building
5. Customer Discovery Specialist — structured research from every customer conversation
6. Founder Fit Analyzer — validates three-way market/founder/product fit

**Step 3 — Expanded persona set.** Each of the 6 was expanded into related archetypes:
- Validation: +Alternative Solution Auditor, +Customer Discovery Specialist, +Founder Fit Analyzer
- Execution: Speed-First Concierge, Small Bets Statistician, Vanity Rejector, AI-First Delegator, Freelance Pivot Builder, Boring-is-Profitable Founder, Delegation Architect, Documentation-Obsessive, System Buyer, Emotional Cooling-Off Founder, Ownership Paradox Navigator, Agnostic Stack Founder
- Psychology: Psychology Manager, Productive Procrastinator, Freedom Ladder Climber, Calm Biz Rationalist, Tool Hoarder Purger
- Strategy: Wave Catcher, Moat Architect, Castle Builder, Constraints Navigator, Exit Planner, Data Flywheel Founder, Vertical SaaS Specialist
- Marketing: Slow Burn Marketer, Engineering Marketer, Anti-Virality Purist, Pricing Psychologist, Small Army Builder, Data Defender
- Regional: Tally Survivor, DATEV Prisoner, FIRS Deadline Fighter, SPED Compliance Navigator, Totvs Escape Artist, Arabic Digital Transformer, GoBD Compliant, Mandate Chaser

**Step 4 — Cross-validation against full corpus.** Persona definitions were refined by spot-checking against the full transcript corpus. For example, the "Vanity Rejector" persona was refined based on patterns seen across multiple Rob Walling and MicroConf transcripts about distinguishing feature requests from paying customers.

**Step 5 — Regional personas added.** The 8 regional personas were not derived from the bootstrapper corpus. They were generated from the non-English market research in Phase 4, based on patterns observed in country-specific GitHub repos, compliance requirements, and community structures.

---

## Data Quality Notes

### Forum Corpus Quality
- All topics were manually reviewed for relevance during initial corpus building
- Topics with purely promotional content (advertising services, job postings without pain signals) were excluded
- Topics from discuss.frappe.io only — GitHub issues, Stack Overflow, and other ERPNext discussion platforms were not included
- The corpus is a snapshot, not a live feed. New topics are created daily on discuss.frappe.io

### Transcript Corpus Quality
- All 486 MicroConf and 486 Rob Walling files are YouTube auto-transcripts — accuracy varies, especially for technical terms and names
- The Bootstrapped Founder transcripts are from the podcast audio — generally higher accuracy than YouTube auto-transcripts
- File naming contains YouTube video IDs — transcripts can be cross-referenced with the actual videos for verification
- The 16 summarized transcripts in `summaries.md` represent curated highlights, not the full depth of each transcript

### Non-English Research Quality
- GitHub repository stars/forks are approximate indicators of community interest, not market size
- Telegram channel member counts are point-in-time and may have changed since research
- Compliance deadline dates were researched via web search — always verify with primary sources (government tax authority websites) before making business decisions
- Pricing data for non-English markets is estimated from implementation partner websites, not confirmed sales data

---

## Corpus Comparison

| Source | Topics/Episodes | Format | Language | Geographic Coverage |
|--------|----------------|--------|----------|-------------------|
| Frappe Forum | 1,742 topics | JSON | English | Global (English-skewed) |
| MicroConf | 486 transcripts | TXT | English | Global |
| Rob Walling | 486 transcripts | TXT | English | Global |
| TBF Podcast | 332 transcripts | TXT | English | Global |
| Non-English Research | 8 regions | MD reports | Mixed | India, MENA, Brazil, Germany, Africa, China, SEA, LatAm |

---

## Replication Data Requirements

To replicate this research, you would need:

**Forum data:**
- Access to discuss.frappe.io (web scraping or API)
- Approximately 1,742 topics × ~5-10KB per topic = ~15-20MB raw data
- Update mechanism for keeping corpus current

**Transcript data:**
- 486 MicroConf YouTube video IDs (provided in `bootstrappers/MicroConf/` filenames)
- 486 Rob Walling YouTube video IDs (provided in `bootstrappers/RobWalling/` filenames)
- 332 TBF episode IDs (provided in `bootstrappers/TheBootstrappedFounder/` filenames)
- YouTube transcript API access or a transcript scraping service (YouTube auto-generates transcripts for most videos)

**Non-English research:**
- Web search API access
- GitHub API access
- Telegram web interface access (web.telegram.org) for public channel research
- Google search for regulatory requirements per country

---

## Corpus Completeness Assessment

| Source | Completeness | Notes |
|--------|-------------|-------|
| Frappe Forum | ~70% | Covers most English discussions; misses Telegram, GitHub issues |
| MicroConf | ~80% | Most recent videos transcribed; older archive incomplete |
| Rob Walling | ~90% | Comprehensive coverage of channel content |
| TBF Podcast | ~85% | Most episodes transcribed; some gaps in early episodes |
| Non-English Research | ~40% | Community signals only; no deep forum data |
