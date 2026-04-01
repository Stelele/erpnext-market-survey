# Replication Guide

**Purpose:** Step-by-step instructions for replicating this research on a new opportunity corpus  
**Time estimate:** 2-3 days of compute time (parallel subagents)  
**Budget estimate:** ~$50-200 in LLM API costs depending on corpus size and parallelism

---

## Prerequisites

### Data Access
- **Forum data:** Access to discuss.frappe.io (web scraping with BeautifulSoup/Playwright, or unofficial API)
- **Alternative:** Any forum, community platform, or Q&A site can substitute for discuss.frappe.io
- **Data format:** JSON — one file per topic/thread

### LLM API Access
- **OpenAI API** (GPT-4o recommended) or **Anthropic API** (Claude Sonnet)
- Budget: ~$50-200 for full Phase 1 + Phase 2 (depending on parallelism)
- Subagents run in parallel — more parallelism = higher per-minute cost but shorter wall clock time

### Infrastructure
- File storage for JSON topic files (~15-20MB for 1,742 topics)
- LLM API access for subagents
- No specialized infrastructure required

---

## Phase 1: Discovery — Persona Canvas Generation

### Step 1: Prepare the Persona Definitions

For each persona you want to use:

1. Create a markdown file in `research-personas/` named `[persona-name].md`
2. Define the persona with at minimum:
   - **Profile** — who this founder is
   - **Discovery triggers** — what signals they look for
   - **Validation threshold** — what makes them say "build this"
   - **Red flags** — what makes them say "avoid this"
   - **ERPNext ecosystem lens** — how they apply to the specific ecosystem being studied

**Minimum viable persona count:** 6 (Validation personas: Community Listener, Pre-Sale Interrogator, Stair-Step Market Sizer, Alternative Solution Auditor, Customer Discovery Specialist, Founder Fit Analyzer)

**Recommended persona count:** 12-20 (add Execution + Strategy personas)

**Full persona count (as used in this research):** 38

### Step 2: Parse Forum Topics into JSON

```python
import json
import requests
from bs4 import BeautifulSoup
import time

BASE_URL = "https://discuss.frappe.io"
TOPICS_PER_PAGE = 30

def fetch_topic(topic_id):
    url = f"{BASE_URL}/t/topic/{topic_id}.json"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    if response.status_code == 200:
        data = response.json()
        return {
            "id": data.get("id"),
            "title": data.get("title"),
            "author": data.get("username"),
            "created": data.get("created_at"),
            "view_count": data.get("views"),
            "like_count": data.get("like_count", 0),
            "reply_count": data.get("reply_count", 0),
            "tags": [t.get("name") for t in data.get("tags", [])],
            "content": data.get("cooked", ""),  # HTML content
        }
    return None

def save_topics(start_id, end_id, output_dir):
    for topic_id in range(start_id, end_id + 1):
        topic = fetch_topic(topic_id)
        if topic:
            with open(f"{output_dir}/{topic_id}.json", "w") as f:
                json.dump(topic, f)
        time.sleep(1)  # Rate limiting

# Fetch topics 100079 to 161685 (adjust range as needed)
```

**Note:** discuss.frappe.io uses Discourse forum software. The Discourse API endpoint is `/t/topic/{id}.json`. You may need a Discourse API key for higher rate limits.

### Step 3: Write the Subagent Prompt Template

Create a prompt that each persona subagent will receive:

```
# Persona: [PERSONA NAME]

## Profile
[Copy from persona definition file]

## Discovery Triggers
[Copy from persona definition file]

## Validation Threshold
[Copy from persona definition file]

## Red Flags
[Copy from persona definition file]

## ERPNext Ecosystem Lens
[Copy from persona definition file]

## Your Task

You are [PERSONA NAME]. Read all 1,742 forum topic files in the `erpnext-forum/topics/` directory.

For each topic, apply your analytical lens as [PERSONA NAME]:
- Does this topic reveal a problem that fits your discovery triggers?
- Is there evidence of willingness-to-pay (WTP)?
- Are there red flags that would make you reject this opportunity?
- What is the customer type and pricing hint?

After reading all topics, identify your TOP 3-5 opportunities.

For each opportunity, write:
- **Opportunity name**: Clear, one-line description
- **Evidence**: Specific topic IDs and quotes from the forum
- **Customer type**: Who would pay for this
- **WTP signals**: What indicates people will pay
- **Competitors**: What alternatives exist
- **Pricing hints**: What the market appears to bear
- **Red flags**: What could kill this opportunity
- **Confidence**: Self-assessed 0-10

Write your full Opportunity Canvas to `persona-outputs/[persona-name].md`.

Be specific. Quote actual forum content. Avoid generic recommendations. Be willing to reject opportunities that don't meet your validation threshold.
```

### Step 4: Launch Parallel Subagents

Launch subagents in batches of 4-8 in parallel. Each subagent:
1. Reads its persona definition file
2. Reads all 1,742 topic JSON files
3. Writes its Opportunity Canvas to `persona-outputs/[persona-name].md`

```python
# Example orchestration (pseudo-code)
import asyncio
from openai import AsyncOpenAI

async def run_persona(persona_name):
    client = AsyncOpenAI()
    
    # Read persona definition
    with open(f"research-personas/{persona_name}.md") as f:
        persona_def = f.read()
    
    # Read all topic files
    topics = []
    for f in glob("erpnext-forum/topics/*.json"):
        with open(f) as tf:
            topics.append(json.load(tf))
    
    # Build prompt
    prompt = PERSONA_TEMPLATE.format(persona=persona_def, topics=topics)
    
    # Call LLM
    response = await client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    
    # Write output
    output = response.choices[0].message.content
    with open(f"persona-outputs/{persona_name}.md", "w") as f:
        f.write(output)

async def main():
    personas = glob("research-personas/*.md")
    personas = [p for p in personas if not p.endswith("README.md")]
    
    # Run in batches of 6
    for batch in chunks(personas, 6):
        await asyncio.gather(*[run_persona(p) for p in batch])

asyncio.run(main())
```

### Step 5: Handle Failures

Subagents may fail due to token limits, API errors, or context overflow. Monitor for:
- Incomplete outputs (canvas doesn't cover all opportunities)
- Timeouts (subagent ran too long)
- API errors (rate limiting, authentication)

**Failure recovery:** Re-run failed subagents. The work is idempotent — re-running produces the same or better output.

**Common issue:** 4 subagents got stuck during Phase 1 of the original research. They required manual resumption. Budget extra time for this.

### Phase 1 Output

After Phase 1, you should have:
- `persona-outputs/[persona-name].md` for each persona
- Each canvas contains: top opportunities, evidence, WTP signals, red flags, confidence

---

## Phase 2: Strategic Validation

### Step 1: Select Strategic Personas

For Phase 2, use 7 strategic personas:
1. Wave Catcher
2. Moat Architect
3. Castle Builder
4. Exit Planner
5. Constraints Navigator
6. Data Flywheel Founder
7. Vertical SaaS Specialist

These personas evaluate Phase 1 outputs, not raw forum data.

### Step 2: Write the Phase 2 Subagent Prompt

```
# Strategic Persona: [PERSONA NAME]

## Profile
[Copy from persona definition file]

## Your Task

You are [PERSONA NAME]. Read all Phase 1 Opportunity Canvases in `persona-outputs/`.

Your job is to evaluate the Phase 1 outputs through your strategic lens.

For each Phase 1 opportunity that scores high (mentioned by 3+ personas), provide:
- **Moat evaluation**: Is this defensible? (if Moat Architect)
- **Exit potential**: Would an acquirer pay for this? (if Exit Planner)
- **Macro waves**: Is this riding a rising tide? (if Wave Catcher)
- **Compounding assets**: Does this get better over time? (if Data Flywheel Founder)
- **Vertical focus**: Should this be narrowed to a specific industry? (if Vertical SaaS Specialist)

Cross-reference Phase 1 canvases. Identify:
1. Which opportunities have the strongest strategic foundations?
2. Which have weak moats or poor exit potential?
3. Where do personas disagree about strategy?

Write your strategic assessment to `persona-outputs/strategic-[persona-name].md`.
```

### Step 3: Launch Phase 2 Subagents

Run Phase 2 subagents in parallel (7 subagents maximum).

### Phase 2 Output

After Phase 2, you should have:
- 7 strategic assessment files in `persona-outputs/`
- Each assessment covers moat, exit, macro waves, compounding, and vertical focus

---

## Phase 3: Master Synthesis

### Step 1: Extract Top Opportunities

From all Phase 1 + Phase 2 outputs, extract:
1. Opportunities mentioned by 3+ personas (convergence signal)
2. Opportunities with explicit WTP signals (Topic 150923-style)
3. Opportunities with compliance/macro tailwinds

### Step 2: Tier 1 & 2 Profiling

For each Tier 1/2 opportunity, write a detailed profile:

```
### [OPP-NAME]: [One-line description]
**Confidence: X/10** | **Solo-founder viable: YES/PARTIAL/NO** | **Build time: X**

**What it solves:** [Clear problem statement]

**Strongest evidence in corpus:**
- [Topic ID]: "[Quote from forum]"
- [Topic ID]: "[Quote from forum]"

**Customer type:** [Who pays]

**Pricing model:** [Price range]

**Why it's a moat:** [What prevents competitors from copying]

**Red flags:** [What could kill this]

**Build path:** [How to build and launch]
```

### Step 3: Tier 3 Scoring

For Tier 3 opportunities (18 in this research), apply the 9-persona scoring framework:

**Batch prompt template:**

```
# Tier 3 Opportunity Scoring

You are scoring [BATCH SIZE] opportunities using 9 personas.
For each opportunity, apply ALL 9 personas. Each persona scores 0-10.

Personas:
1. STAIR-STEP MARKET SIZER — market size, TAM
2. PRE-SALE INTERROGATOR — willingness-to-pay, real budget
3. VANITY REJECTOR — will this command payment or is it noise?
4. BORING-IS-PROFITABLE — boring, steady, recurring revenue
5. SPEED-FIRST CONCIERGE — how fast can a solo founder build this?
6. SMALL BETS STATISTICIAN — risk-adjusted return
7. FOUNDER FIT ANALYZER — solo-founder viable without local partner?
8. AGNOSTIC STACK FOUNDER — ERPNext-specific lock-in?
9. EXIT PLANNER — exit potential, acqui-hire value

Scoring rules:
- Base score: 5/10
- Each persona adjusts +/- 2-3 points
- Min < 3 = REJECT flag
- Spread (max-min) > 5 = DIVIDED flag

Opportunities to score:

[LIST ALL OPPORTUNITIES IN BATCH]

Output format: JSON
{
  "opp_name": {
    "scores": {"market_sizer": N, "pre_sale": N, ...},
    "average": N.N,
    "min": N,
    "max": N,
    "spread": N,
    "solo_rank": N,
    "flags": ["REJECT" | "DIVIDED" | null],
    "summary": "2-3 sentence synthesis"
  }
}
```

Run 4 batches of 4-5 opportunities each (18 total). Aggregate scores across batches.

### Step 4: Write the Master Synthesis

Compile into `synthesis/master-synthesis.md`:
- Executive summary (3 patterns)
- Top 10 ranked opportunities table
- Tier 1 & 2 detailed profiles
- Tier 3 ranked table (all 18, by average score)
- Validation of pre-built zones
- Solo-founder priority matrix
- Rejected opportunities
- Compounding assets
- Highest WTP signals

---

## Non-English Market Expansion

See `methodology/nonenglish-research.md` for the non-English research methodology.

---

## Budget Estimation

| Phase | Subagents | Time | Estimated Cost |
|-------|---------|------|-------------|
| Phase 1 (38 personas) | 6 parallel | ~4-6 hours | $30-80 |
| Phase 2 (7 personas) | 7 parallel | ~1-2 hours | $10-20 |
| Phase 3 Tier 3 (18 opps) | 4 parallel batches | ~2-3 hours | $15-30 |
| Non-English (8 regions) | 8 parallel | ~3-4 hours | $20-40 |
| **Total** | | **~12-15 hours** | **$75-170** |

Costs assume GPT-4o pricing (~$3-5/M input tokens, $15-25/M output tokens). Claude Sonnet is similar. Actual costs depend on corpus size, topic length, and parallelism.

---

## Common Failure Modes

### Failure 1: Subagent Context Overflow
**Problem:** Reading all 1,742 topics exceeds the context window.  
**Solution:** Pre-process topics into a curated summary file before subagent execution. Group by tags or cluster by similarity. Pass the summary instead of raw topics.

### Failure 2: Inconsistent Canvas Quality
**Problem:** Some personas produce detailed canvases; others produce shallow outputs.  
**Solution:** Include examples of excellent canvas output in the subagent prompt. Add quality gates in the prompt ("If your canvas doesn't include specific topic IDs and quotes, regenerate it").

### Failure 3: Persona Convergence
**Problem:** All personas identify the same 3 opportunities and miss the rest.  
**Solution:** Add persona diversity. Ensure personas have genuinely different analytical lenses. Pre-seed the prompt with "do NOT recommend [top opportunities]" to force discovery of secondary opportunities.

### Failure 4: Subagent Sticking
**Problem:** Subagent hangs or produces incomplete output.  
**Solution:** Implement timeout (30-60 min max per subagent). Monitor for incomplete writes. Re-run failed subagents. In the original research, 4 of 38 subagents required resumption.

### Failure 5: Scoring Inconsistency
**Problem:** Different batches produce inconsistent scores (Batch 1 averages 6.0, Batch 2 averages 7.0).  
**Solution:** Cross-calibrate with one shared opportunity in each batch. If Opp X appears in Batch 1 and Batch 2, its scores should be comparable.

### Failure 6: Synthesizer Bottleneck
**Problem:** The synthesis step (reading all 38 canvases + Phase 2 assessments) exceeds context window.  
**Solution:** Pre-process canvases into structured data (JSON extraction). Use the structured data for synthesis instead of raw markdown.

---

## Adapting for Different Ecosystems

This methodology is not ERPNext-specific. To apply it to a different ecosystem:

1. **Replace the forum corpus** — substitute discuss.frappe.io for any community forum (Stack Overflow, Reddit, Hacker News, niche forums)
2. **Replace the personas** — swap ERPNext-specific personas for ecosystem-relevant ones (e.g., "Magento ecosystem persona" if studying Magento)
3. **Replace the non-English research** — substitute region-specific communities, compliance requirements, and Telegram channels for the target ecosystem
4. **Keep the framework** — 38 personas, Phase 1/2/3 structure, 9-persona scoring, and synthesis are ecosystem-agnostic

---

## File Structure for Replication

```
your-project/
├── research-personas/
│   ├── README.md
│   ├── [persona-1].md
│   ├── [persona-2].md
│   └── ...
├── corpus/
│   └── [topic-id-1].json
│   └── [topic-id-2].json
│   └── ...
├── persona-outputs/
│   ├── [persona-1].md
│   ├── [persona-2].md
│   └── ...
├── synthesis/
│   └── master-synthesis.md
└── methodology/
    ├── overview.md
    ├── corpus.md
    ├── persona-library.md
    ├── framework.md
    └── replication-guide.md
```

---

## Quality Checklist

Before declaring Phase 3 complete, verify:

- [ ] All 38 persona canvases are written and non-empty
- [ ] Each canvas includes at least 2 specific topic IDs with quotes
- [ ] Phase 2 strategic assessments cover all Tier 1 opportunities
- [ ] Tier 3 scores are calculated with correct aggregation (average, min, spread)
- [ ] REJECT and DIVIDED flags are applied correctly
- [ ] Master synthesis includes executive summary, ranked list, and rejected opportunities
- [ ] Non-English research covers at least 3 regions
- [ ] README.md links to synthesis/master-synthesis.md
- [ ] All new personas are documented in research-personas/README.md
