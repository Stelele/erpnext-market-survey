# Persona Library

**Total:** 46 personas across 6 categories  
**Source:** 1,304 bootstrapper transcripts + 8 non-English market research streams  
**Purpose:** Each persona is an independent analytical lens for identifying paid pain points in the ERPNext ecosystem

---

## How Personas Work

Each persona is a distinct analytical lens that a bootstrapped founder might use to evaluate an opportunity. The core hypothesis is that **no single analytical lens captures all opportunities** — some personas are sensitive to urgency (compliance deadlines), others to market size (stair-step market sizer), others to exit potential (exit planner). Cross-persona agreement signals high confidence; cross-persona disagreement reveals controversy.

**Personas are NOT profiles of ERPNext users.** They are profiles of the *founder evaluating* whether to build an ERPNext ecosystem product.

**Persona file structure:**
```
research-personas/
├── [persona-name].md       # Full persona definition
└── README.md                # This file
```

**Each persona file contains:**
- **Profile:** Who this founder is and what they believe
- **Discovery triggers:** What signals they pay attention to
- **Validation threshold:** What makes them say "yes, build this"
- **Red flags:** What makes them say "no, avoid this"
- **ERPNext ecosystem lens:** How they apply their methodology specifically to ERPNext
- **Opportunity types they favor:** What kinds of products/services they gravitate toward
- **Opportunity types they reject:** What they avoid

---

## Category 1: Validation Personas (6)

These personas answer: **"Is this problem real, and will people pay for it?"**

---

### 1. Community Listener
**File:** `community-listener.md`  
**Source:** TBF podcast (finding problems in communities) + MicroConf (community building)  
**What it measures:** Pain density — how often does this problem appear in community discussions? What emotional weight does it carry?

**Discovery triggers:**
- Forum topics with high reply counts and low solution rates
- Users explicitly asking "has anyone solved this?"
- Workarounds being shared repeatedly (signal of unsolved pain)
- Implementation partners advertising services around a specific gap

**Validation threshold:** Problem appears in multiple independent sources with emotional language ("terrible," "waste of time," "still broken after years")

**Red flags:** Problem only mentioned once. Solutions exist and work well. Problem is cosmetic, not business-critical.

**ERPNext lens:** ERPNext forums, Frappe community, Telegram channels, GitHub issues — all serve as community signals.

---

### 2. Pre-Sale Interrogator
**File:** `pre-sale-interrogator.md`  
**Source:** Rob Walling (validate before building) + TBF (charging before building)  
**What it measures:** Willingness to pay — has anyone actually put money on the table?

**Discovery triggers:**
- Forum posts mentioning budgets ("we have $5,000 for this")
- Implementation partners pricing services around a gap
- Freelance job postings with explicit pricing
- GitHub sponsors or bounties on relevant repos

**Validation threshold:** At least one explicit WTP signal (money mentioned, job with price, sponsored repo)

**Red flags:** Only "would be nice to have" signals. Nobody has mentioned budget. Problem discussed but no action taken.

**ERPNext lens:** Topic 150923 ($5,000 for seed data) is the gold standard. Everything is measured against this.

---

### 3. Stair-Step Market Sizer
**File:** `stair-step-market-sizer.md`  
**Source:** Rob Walling (stair-step from consulting to productized service to SaaS) + TBF (small bets)  
**What it measures:** Market size and entry strategy — can you validate with consulting before building software?

**Discovery triggers:**
- Implementation partners doing the same custom work repeatedly
- Freelance rates for specific ERPNext customizations ($50-200/hr)
- Companies advertising ERPNext implementation services
- Gap that requires domain expertise (consulting moat possible)

**Validation threshold:** Evidence of recurring custom work at profitable rates ($50+/hr). At least 3 independent requests for similar work.

**Red flags:** One-time project with no repeat demand. Requires building before validating with consulting. Market too small for even consulting-level demand.

**ERPNext lens:** The Tally migration gap — companies stuck on Tally needing migration help. Each migration is custom work today = potential for productized service.

---

### 4. Alternative Solution Auditor
**File:** `alternative-solution-auditor.md`  
**Source:** Rob Walling (reverse engineer adjacent tools) + MicroConf (competing alternatives)  
**What it measures:** Competitive landscape — what alternatives exist, and how hard is it to displace them?

**Discovery triggers:**
- Forum users asking "how do I do X?" and receiving non-ERPNext answers
- Workarounds using external tools (Zapier, N8N, manual Excel)
- Users mentioning they switched FROM another tool because of this gap
- ERPNext core team or community building in this direction

**Validation threshold:** Current solutions require workarounds, are expensive, or are non-existent. At least one viable alternative exists to study.

**Red flags:** Google, Microsoft, or another well-funded company is building this. ERPNext core is actively developing this. Solution is trivially easy to build elsewhere and import.

**ERPNext lens:** Print formats — users going to Jinja templates and JavaScript. EugeneP's Script Reports tutorial has 32,522 views = proof of demand.

---

### 5. Customer Discovery Specialist
**File:** `customer-discovery-specialist.md`  
**Source:** Rob Walling (talk to customers) + TBF (jobs to be done)  
**What it measures:** Customer understanding — who has this problem, what are they doing today, and what would make them switch?

**Discovery triggers:**
- Forum posts describing specific workflows and frustrations
- Implementation posts asking "how do companies like mine handle X?"
- Users describing the workarounds they use
- Industry-specific discussions (manufacturing, healthcare, non-profit)

**Validation threshold:** Problem described in specific, actionable terms. At least 3 different users describing the same pain from different angles.

**Red flags:** Problem described in vague, aspirational terms ("we need better analytics"). Only one person mentions it. No workaround described.

**ERPNext lens:** Manufacturing users describing the Quality Inspection bug (one QI per item). Non-profits describing the Income/Expense terminology problem.

---

### 6. Founder Fit Analyzer
**File:** `founder-fit-analyzer.md`  
**Source:** TBF (founder-market fit) + MicroConf (leveling up)  
**What it measures:** Three-way fit — does this opportunity match the founder's skills, the market timing, and the product type?

**Discovery triggers:**
- Opportunity matches existing founder expertise (e.g., Indian founder for Tally migration)
- Opportunity has timing alignment (regulatory deadline approaching)
- Opportunity fits solo-founder constraints (no hardware, no regulatory partnership needed)

**Validation threshold:** At least 2 of 3: founder has relevant skills, market timing is right, solo-viable

**Red flags:** Requires skills the founder doesn't have and can't acquire quickly. Market timing is bad (too early or too late). Requires a team to deliver.

**ERPNext lens:** Brazil NF-e emission — requires Brazilian tax law expertise that a solo non-Brazilian founder can't easily acquire. OPP-001 Demo/Seed Data — any developer can build it in 1-2 weeks.

---

## Category 2: Execution Personas (13)

These personas answer: **"How should this be built and shipped?"**

---

### 7. Speed-First Concierge
**File:** `speed-first-concierge.md`  
**Source:** TBF (ship fast, validate fast) + Pawel Brzeminski (30-day launch)  
**What it measures:** Build speed — how fast can a solo founder build and ship this?

**Discovery triggers:**
- Opportunities that can be built in 1-4 weeks
- Features that are self-contained (not dependent on other ERPNext systems)
- Workarounds that could be packaged into simple apps
- Server scripts that could be productized

**Validation threshold:** Build time < 4 weeks for v1. No external dependencies that could delay launch.

**Red flags:** Requires months of development before first value delivery. Needs hardware. Needs regulatory approval. Requires partnership before shipping.

**ERPNext lens:** Last-Selling Price Display — server script + custom field = 1 week build. OPP-001 Demo/Seed Data = 1-2 weeks.

---

### 8. Small Bets Statistician
**File:** `small-bets-statistician.md`  
**Source:** Daniel Vassallo (small bets framework) + TBF (experiments)  
**What it measures:** Risk-adjusted return — what's the expected value of this bet?

**Discovery triggers:**
- Low-cost opportunities that can be validated quickly
- Opportunities with asymmetric upside (fail cheap, succeed big)
- Opportunities that can be run as experiments before committing
- Opportunities with clear pass/fail criteria

**Validation threshold:** Expected value > 3x downside. Clear metrics for success/failure. Can validate with < $5,000 and < 1 month.

**Red flags:** Requires large upfront investment before validation. Metrics for success are unclear. High fixed costs regardless of outcome.

**ERPNext lens:** Building a free ERPNext app to validate demand before charging. Landing page test for OPP-001 before building seed data packs.

---

### 9. Vanity Rejector
**File:** `vanity-rejector.md`  
**Source:** Rob Walling (vanity metrics vs. revenue) + TBF (distinguishing signal from noise)  
**What it measures:** Does this command actual payment, or is it feature-request noise?

**Discovery triggers:**
- Problems that cost money to work around (labor, time, external tools)
- Problems that block revenue-generating activities
- Problems that create compliance or legal risk
- Problems where users have "hired a developer" to solve it

**Validation threshold:** Users are paying money (directly or via workaround costs) to solve this problem today. Evidence of existing spend.

**Red flags:** Problem is a "nice to have." Users suggest it as a feature but don't seem bothered. Nobody has offered money. Problem exists but is not blocking anything.

**ERPNext lens:** Topic 119327 ("I had to hire a developer" for tax compliance) = vanity rejector validated. Generic "ERPNext should improve reporting" = vanity rejector rejected.

---

### 10. Boring-is-Profitable Founder
**File:** `boring-is-profitable-founder.md`  
**Source:** MicroConf (boring micro-SaaS ideas) + Rob Walling (unsexy opportunities)  
**What it measures:** Steady, recurring revenue — is this a boring-but-profitable opportunity?

**Discovery triggers:**
- Recurring pain (not one-time projects)
- Narrow, specific use cases that require domain knowledge
- Users doing repetitive manual work
- Opportunities that make users' existing workflows faster/more reliable

**Validation threshold:** Recurring pain that users face daily or weekly. Not dependent on one-time events.

**Red flags:** One-time migration or implementation opportunity. Event-driven (only needed during upgrades). Requires constant new customer acquisition (no recurring use).

**ERPNext lens:** AR Collections reminder automation = boring, recurring (every week). Tally migration = one-time project (not boring-is-profitable).

---

### 11. AI-First Delegator
**File:** `ai-first-delegator.md`  
**Source:** TBF (AI-powered solopreneur) + MicroConf (AI marketing)  
**What it measures:** Can AI help build or deliver this faster?

**Discovery triggers:**
- Opportunities where AI reduces build time by 50%+
- Opportunities where AI enables capabilities solo founders couldn't build otherwise
- Document-heavy workflows (contracts, reports, emails)
- Content generation or translation opportunities

**Validation threshold:** AI can handle at least 50% of the work. No accuracy-critical tasks that AI can't handle.

**Red flags:** Requires human judgment that AI can't replicate. Accuracy requirements too high for current AI (legal, medical, financial). Requires physical hardware or on-site presence.

**ERPNext lens:** Invoice OCR — PaddleOCR/Tesseract + LLM can extract 80%+ of invoice fields. AI Localization — LLM translates ERPNext UI strings successfully.

---

### 12. Freelance Pivot Builder
**File:** `freelance-pivot-builder.md`  
**Source:** Rob Walling (productizing consulting) + TBF (freelance to product)  
**What it measures:** Can consulting demand validate the product before building?

**Discovery triggers:**
- Implementation partners doing custom work around a specific gap
- Forum users asking for help with a specific ERPNext customization
- Job postings for ERPNext developers with specific skills

**Validation threshold:** Consulting demand exists. At least 3 potential customers willing to pay consulting rates for this.

**Red flags:** No consulting demand signal. Building a product nobody has asked for in consulting engagements.

**ERPNext lens:** If ERPNext India Telegram channels have job postings for Tally migration specialists, that's a pivot signal.

---

### 13. Delegation Architect
**File:** `delegation-architect.md`  
**Source:** Patrick McKenzie (leveling up) + TBF (hiring to scale)  
**What it measures:** Can this be delegated or systematized, or does it always require the founder?

**Discovery triggers:**
- Opportunities that create dependency on the founder's unique skills
- Opportunities where standard processes can replace expert judgment
- Opportunities that require deep ERPNext expertise that can be codified

**Validation threshold:** At least 50% of delivery can be systematized or delegated. Founder dependency < 2 hours per customer per month.

**Red flags:** Every customer requires founder-level expertise. No way to systematize the delivery. High touch required per customer.

**ERPNext lens:** Invoice OCR pipeline — automated extraction requires minimal human review. Emergency triage service — requires deep expertise, hard to delegate.

---

### 14. Documentation-Obsessive
**File:** `documentation-obsessive.md`  
**Source:** TBF (documentation as moat) + MicroConf (content compounding)  
**What it measures:** Does documentation create compounding value?

**Discovery triggers:**
- ERPNext documentation is sparse or outdated
- Users struggling to find implementation guides
- Users creating their own documentation (signal of demand)
- Complex features with minimal official docs

**Validation threshold:** At least 500 monthly unique visitors searching for this documentation (forum views, search rankings).

**Red flags:** ERPNext has excellent official documentation for this area. No gap exists. Community docs already exist and are comprehensive.

**ERPNext lens:** Topic 79873 (documentation complaint) with massive engagement. EugeneP's Script Reports tutorial with 32,522 views = documentation gap.

---

### 15. System Buyer
**File:** `system-buyer.md`  
**Source:** Patrick McKenzie (buying over building) + MicroConf (tool consolidation)  
**What it measures:** Should this be bought, not built?

**Discovery triggers:**
- Opportunities that could be solved by stitching existing tools
- Opportunities where ERPNext integrations exist but are poorly documented
- Opportunities where a well-configured existing solution beats a custom build

**Validation threshold:** Existing solution can handle 80%+ of the use case. Integration cost < 50% of custom build cost.

**Red flags:** Existing solutions are all inadequate. No integrations exist. Custom build is dramatically better than any combination.

**ERPNext lens:** Using N8N + ERPNext API instead of building custom automation. Using existing Plaid integration instead of building bank sync.

---

### 16. Emotional Cooling-Off Founder
**File:** `emotional-cooling-off-founder.md`  
**Source:** TBF (emotional decision-making) + MicroConf (calm business)  
**What it measures:** Is this opportunity evaluated with urgency or with patience?

**Discovery triggers:**
- Compliance deadlines approaching (urgent)
- Bug reports with active production impact (urgent)
- Feature requests that have been open for years (patient)

**Validation threshold:** Urgency is real and backed by evidence. Not manufactured urgency or founder excitement.

**Red flags:** Founder is excited about the opportunity but no urgency exists. Problem has existed for years without anyone building. "This is going to be huge" without timeline.

**ERPNext lens:** Nigeria FIRS deadline (August 2025) = real urgency. The Tally migration tool being broken since v13 = patient opportunity, not urgent.

---

### 17. Ownership Paradox Navigator
**File:** `ownership-paradox-navigator.md`  
**Source:** TBF (ownership paradox episode) + MicroConf (dependencies)  
**What it measures:** What are you building vs. renting? What breaks when ERPNext changes?

**Discovery triggers:**
- Opportunities built on fragile ERPNext internals
- Opportunities that ERPNext core might build natively
- Opportunities that depend on specific ERPNext versions
- Opportunities where ERPNext changes could break the product

**Validation threshold:** Either: (a) ERPNext dependency is low, or (b) ERPNext core is unlikely to build this, or (c) moat is strong enough to survive ERPNext competition.

**Red flags:** Opportunity is a workaround for ERPNext core not building something. ERPNext core explicitly said they're building this. Product breaks on every ERPNext upgrade.

**ERPNext lens:** Shopping cart bug fix — ERPNext could fix this in any release. Print Automation Studio — ERPNext core has Print Designer but users still struggle (low risk of being replaced).

---

### 18. Agnostic Stack Founder
**File:** `agnostic-stack-founder.md`  
**Source:** TBF (AI compatibility) + MicroConf (platform risk)  
**What it measures:** Does this require ERPNext lock-in, or could it work on any ERP?

**Discovery triggers:**
- Opportunities that solve ERPNext-specific gaps
- Opportunities that require ERPNext API/doctype access
- Opportunities where ERPNext-specific training data or configuration creates moat

**Validation threshold:** Moat requires ERPNext-specific lock-in. Non-ERPNext competitors couldn't easily replicate.

**Red flags:** This is a generic opportunity that exists in every ERP. No ERPNext-specific advantage. Any competent developer could replicate.

**ERPNext lens:** Invoice OCR pipeline — supplier invoice formats are proprietary to each ERPNext installation = strong ERPNext lock-in. Generic AI chatbot = agnostic stack, no ERPNext advantage.

---

### 19. AI Agent Manager
**File:** `ai-agent-manager.md`  
**Source:** TBF (AI agents) + MicroConf (AI workflows)  
**What it measures:** Can this be automated with AI agents?

**Discovery triggers:**
- Repetitive workflows that follow patterns
- Information synthesis tasks (summarizing reports, extracting from documents)
- Customer communication that follows templates
- Data entry from unstructured sources

**Validation threshold:** >80% of task can be automated by AI agents. Human review needed for <20%.

**Red flags:** Requires real-time physical actions. Requires nuanced human judgment. High error cost (financial, legal).

**ERPNext lens:** Invoice OCR pipeline = AI agent manages extraction. Customer chatbot for balance/invoice queries = AI agent manages communication.

---

### 20. Psychology Manager
**File:** `psychology-manager.md`  
**Source:** TBF (founder psychology) + MicroConf (mental health)  
**What it measures:** What psychological biases might make this opportunity attractive or dangerous?

**Discovery triggers:**
- Opportunities that appeal to founder ego (impressive, technically challenging)
- Opportunities with "obvious" demand that might not have real WTP
- Opportunities that align with founder identity vs. market need

**Validation threshold:** Opportunity is validated by market evidence, not by how impressive it sounds or how much the founder likes it.

**Red flags:** Founder is excited because it's technically interesting, not because customers will pay. Opportunity sounds good in a tweet but is hard to monetize.

**ERPNext lens:** Building a full ERPNext AI copilot sounds impressive but may have low WTP. The boring AR Collections reminder tool sounds uninteresting but has clear WTP.

---

## Category 3: Psychology Personas (5)

These personas answer: **"What is the founder's psychological relationship to this opportunity?"**

---

### 21. Productive Procrastinator
**File:** `productive-procrastinator.md`  
**Source:** TBF (productive procrastination episode) + MicroConf (channeling distraction)  
**What it measures:** Does this opportunity allow for productive procrastination?

**Discovery triggers:**
- Opportunities that can be approached sideways
- Opportunities with low-stakes experiments that build toward the bigger opportunity
- Opportunities that satisfy curiosity while building toward revenue

**Validation threshold:** Can generate revenue or revenue-adjacent progress even from brief, distracted work sessions.

**Red flags:** Requires sustained focus to make progress. No incremental value from partial work. Long feedback loops.

**ERPNext lens:** Building ERPNext app documentation — can be done in short sessions, generates SEO value incrementally. Emergency triage service — requires focused attention, can't be productive in 20 minutes.

---

### 22. Freedom Ladder Climber
**File:** `freedom-ladder-climber.md`  
**Source:** TBF (freedom ladder concept) + Justin Jackson (freedom vs. venture)  
**What it measures:** Does this move the founder toward or away from freedom?

**Discovery triggers:**
- Opportunities that generate recurring revenue without requiring the founder
- Opportunities that enable location independence
- Opportunities that reduce operational dependency

**Validation threshold:** Progress toward recurring revenue. Location-independent. Founder not required for delivery.

**Red flags:** Requires founder presence. High operational burden. Doesn't generate recurring revenue.

**ERPNext lens:** SaaS subscription for ERPNext app = toward freedom. Emergency triage service = away from freedom (high touch, founder required).

---

### 23. Calm Biz Rationalist
**File:** `calm-biz-rationalist.md`  
**Source:** TBF Calm SaaS series (16 episodes) + MicroConf (sustainable business)  
**What it measures:** Does this opportunity support a calm, rational business?

**Discovery triggers:**
- Predictable, recurring revenue
- Low churn and high customer retention
- Defensible margins
- Sustainable customer acquisition cost

**Validation threshold:** CAC < 6-month LTV. Churn < 5% monthly. Gross margins > 70%.

**Red flags:** High churn. Expensive customer acquisition. Low margins. One-time revenue.

**ERPNext lens:** ERPNext app subscription = calm. Custom ERPNext implementation projects = not calm.

---

### 24. Tool Hoarder Purger
**File:** `tool-hoarder-purger.md`  
**Source:** TBF (tool consolidation) + MicroConf (simplification)  
**What it measures:** Does this opportunity solve a tool-hoarding problem?

**Discovery triggers:**
- Users complaining about too many tools
- ERPNext users needing integrations with external tools
- Users stitching together multiple tools to accomplish what one tool should do

**Validation threshold:** Clear pain from tool fragmentation. Users paying for multiple tools when one integrated solution would be better.

**Red flags:** Users are satisfied with their current tool stack. No integration demand. Current tools work well together.

**ERPNext lens:** ERPNext users needing Plaid for bank feeds + QuickBooks for accounting = tool fragmentation. Build unified bank-to-ERPNext solution.

---

## Category 4: Strategy Personas (7)

These personas answer: **"How does this create durable competitive advantage?"**

---

### 25. Wave Catcher
**File:** `wave-catcher.md`  
**Source:** TBF (macro shifts) + MicroConf (regulatory change)  
**What it measures:** Is this riding a rising tide or fighting gravity?

**Discovery triggers:**
- Regulatory changes creating new compliance requirements (e-invoicing mandates)
- Technology transitions creating upgrade pain
- Market shifts creating new customer segments
- Platform changes creating ecosystem opportunities

**Validation threshold:** Macro tailwind confirmed. Regulatory deadline within 12-24 months. Not speculative.

**Red flags:** Opportunity depends on a trend that may not materialize. "Everyone will need this eventually" without timeline. Trend is already peaking.

**ERPNext lens:** Nigeria FIRS e-invoicing = wave. Saudi ZATCA Phase 2/3 = wave. Belgium PEPPOL January 2026 = wave.

---

### 26. Moat Architect
**File:** `moat-architect.md`  
**Source:** TBF (moats episode) + MicroConf (competitive advantage)  
**What it measures:** What prevents competitors from copying this?

**Discovery triggers:**
- Data compounding over time
- Network effects
- Integration depth creating switching costs
- Regulatory moats (compliance certifications)

**Validation threshold:** At least one durable moat mechanism identified. Moat increases over time, not decreases.

**Red flags:** Easily replicable by a competent developer in < 1 month. No switching costs. No data compounding. No network effects.

**ERPNext lens:** Invoice OCR format library = data moat (every customer improves extraction for all customers). Generic print format template = no moat.

---

### 27. Castle Builder
**File:** `castle-builder.md`  
**Source:** TBF (castle in someone else's kingdom) + MicroConf (owned vs. rented)  
**What it measures:** Are you owning what compounds and renting what depreciates?

**Discovery triggers:**
- Opportunities where proprietary assets compound
- Opportunities where infrastructure costs can be minimized
- ERPNext-specific assets (custom apps, training, integrations)

**Validation threshold:** Core asset is ownable and compounding. Infrastructure is rented and commodity.

**Red flags:** Core asset depends on ERPNext core decisions. Infrastructure investment doesn't create proprietary value. Moat requires ongoing investment to maintain.

**ERPNext lens:** ERPNext training content library = ownable, compounding. ERPNext hosting infrastructure = rented, depreciating.

---

### 28. Constraints Navigator
**File:** `constraints-navigator.md`  
**Source:** TBF (constraints episode) + MicroConf (working within limits)  
**What it measures:** Can constraints be turned into advantages?

**Discovery triggers:**
- Opportunities where limited resources force creative solutions
- Opportunities that require specific expertise (creates natural moat)
- Opportunities where being small is an advantage

**Validation threshold:** Constraint creates differentiation. Being small/focused enables something big/generalist can't do.

**Red flags:** Constraint is purely limiting with no upside. Big competitor can do this better with more resources. Constraint doesn't create differentiation.

**ERPNext lens:** Building a vertical-specific ERPNext app (e.g., ERPNext for dental clinics) = constraint creates differentiation. Building a general ERPNext reporting tool = big competitor can replicate.

---

### 29. Exit Planner
**File:** `exit-planner.md`  
**Source:** TBF (exit planning) + MicroConf (sellability)  
**What it measures:** Is this acquirable at a good multiple?

**Discovery triggers:**
- Strong recurring revenue with low churn
- Proprietary data or integration depth
- Clear buyer (competitor, adjacent acquirer, PE firm)
- B2B pricing with annual contracts

**Validation threshold:** ARR > $50K minimum. Revenue is recurring, not transactional. Clear acquirer profile exists.

**Red flags:** Service business with no software component. Revenue is one-time. No proprietary data or integration. No clear acquirer.

**ERPNext lens:** ERPNext app with 100+ paying customers at $50/month = exit potential. Emergency triage concierge service = no exit.

---

### 30. Data Flywheel Founder
**File:** `data-flywheel-founder.md`  
**Source:** TBF (data moats) + Nathan Latka (data flywheel episode)  
**What it measures:** Does this create a data compounding effect?

**Discovery triggers:**
- Every customer adds data that improves the product for all customers
- Data that competitors can't easily replicate
- Data that compounds over time (more customers = more data = better product = more customers)

**Validation threshold:** Clear data flywheel mechanism identified. Data has a compounding growth curve.

**Red flags:** No data generated by the product. Data doesn't improve the product. Data is easily replicated by competitors.

**ERPNext lens:** Invoice OCR pipeline = strongest data flywheel. Supplier invoice formats from 100 customers create extraction accuracy that new entrants can't match.

---

### 31. Vertical SaaS Specialist
**File:** `vertical-saas-specialist.md`  
**Source:** Rob Walling (vertical SaaS) + MicroConf (niche focus)  
**What it measures:** Should this be narrowed to a specific vertical?

**Discovery triggers:**
- Opportunity applies to specific industry (manufacturing, healthcare, non-profit)
- Industry-specific terminology, workflows, or compliance requirements
- Industry communities where ERPNext is discussed

**Validation threshold:** Vertical has clear differentiation. Within-vertical WTP is higher than cross-vertical. Competitors are weak or absent in vertical.

**Red flags:** Problem is universal across verticals. Narrowing reduces TAM without increasing WTP enough. Vertical has established incumbents.

**ERPNext lens:** ERPNext for non-profits = vertical narrowing (Income/Expense → Donation/Pledge). ERPNext for dental clinics = vertical narrowing.

---

## Category 5: Marketing Personas (7)

These personas answer: **"How would this be found and sold?"**

---

### 32. Slow Burn Marketer
**File:** `slow-burn-marketer.md`  
**Source:** TBF (content compounding) + MicroConf (building audiences)  
**What it measures:** Does this opportunity support content-driven growth?

**Discovery triggers:**
- Complex topics with documentation gaps
- Topics that rank for search
- Topics with community discussion that could be synthesized
- Topics where a blog/tutorial generates ongoing traffic

**Validation threshold:** Clear content strategy. Topics have search volume. Content compounds over time.

**Red flags:** No content strategy possible. Product is self-explanatory. No documentation gap exists.

**ERPNext lens:** Script Reports documentation = content compounding (EugeneP tutorial has 32,522 views). Manufacturing QC bug fix = no content strategy.

---

### 33. Engineering Marketer
**File:** `engineering-marketer.md`  
**Source:** Patrick McKenzie (engineering marketing) + MicroConf (technical content)  
**What it measures:** Does engineering rigor applied to marketing create advantage?

**Discovery triggers:**
- Opportunities where technical depth is a differentiator
- Topics where the developer audience is reachable
- Problems that can be explained with code samples

**Validation threshold:** Developer audience exists. Technical content resonates. Open-source contribution builds credibility.

**Red flags:** Non-technical audience required. Marketing requires creative campaigns, not technical depth.

**ERPNext lens:** ERPNext app marketplace = developer audience reachable via GitHub. ERPNext user training = non-technical audience.

---

### 34. Anti-Virality Purist
**File:** `anti-virality-purist.md`  
**Source:** TBF (anti-virality) + MicroConf (sustainable growth)  
**What it measures:** Can this grow without viral loops?

**Discovery triggers:**
- B2B products with clear buyer persona
- Products where word-of-mouth is the natural growth channel
- Products with referral mechanisms built in

**Validation threshold:** Non-viral growth is sufficient. Clear acquisition channel identified that doesn't require virality.

**Red flags:** Product requires viral loops to grow. Growth stalls without virality. No clear non-viral acquisition channel.

**ERPNext lens:** ERPNext app sold via forum + community = non-viral. Consumer app requiring viral loop = not suitable.

---

### 35. Pricing Psychologist
**File:** `pricing-psychologist.md`  
**Source:** Rob Walling (pricing) + TBF (pricing psychology)  
**What it measures:** What pricing model maximizes revenue and minimize churn?

**Discovery triggers:**
- Opportunities where usage-based pricing makes sense
- Opportunities where tiered pricing creates upsell potential
- Opportunities where freemium creates broad adoption

**Validation threshold:** Clear pricing strategy. Price is defensible against alternatives. Price increases are feasible.

**Red flags:** Only one viable price point. Price war with competitors. Price is constrained by comparable products.

**ERPNext lens:** Invoice OCR pipeline = usage-based (per invoice). Print format templates = one-time purchase. ERPNext app subscription = monthly SaaS.

---

### 36. Small Army Builder
**File:** `small-army-builder.md`  
**Source:** Andy Baldacci (small army) + MicroConf (agency partnerships)  
**What it measures:** Can ERPNext implementation partners distribute this?

**Discovery triggers:**
- Opportunities where implementation partners are the natural sales channel
- Opportunities requiring customization or configuration
- Opportunities where partners add value beyond software delivery

**Validation threshold:** Partner ecosystem exists. Partners earn margin on this. Partners want to sell this.

**Red flags:** No partner ecosystem. Product is fully self-serve. Partners add no value.

**ERPNext lens:** ERPNext implementation partners (Frappe Partners program) = distribution channel. Direct-to-customer ERPNext app = no partner value.

---

### 37. Data Defender
**File:** `data-defender.md`  
**Source:** TBF (scraping ethics) + MicroConf (data ownership)  
**What it measures:** Does this respect data ethics while extracting value?

**Discovery triggers:**
- Opportunities involving data scraping or API access
- Opportunities where data is the product
- Opportunities with privacy or GDPR considerations

**Validation threshold:** Data sourcing is ethical and legal. Customers understand what data is collected. Data is used to serve customers, not exploit them.

**Red flags:** Data sourcing is unethical or illegal. Data collection is hidden. Data is sold without customer consent.

**ERPNext lens:** Bank statement data = customer-owned. Supplier invoice data = customer-owned. Public forum data = ethically gray.

---

## Category 6: Regional Personas (8)

These personas evaluate opportunities in non-English ERPNext markets. They were generated from non-English market research, not from the bootstrapper transcript corpus.

---

### 38. Tally Survivor
**File:** `tally-survivor.md`  
**Market:** India  
**What it measures:** Can Tally users be migrated to ERPNext?

**Discovery triggers:**
- Tally users asking about ERPNext migration
- Tally migration tool broken
- Tally Prime subscription price increases driving migration interest

**Validation threshold:** Working migration tool exists. Tally data can be mapped to ERPNext. Indian implementation partners exist.

**Red flags:** Tally users not interested in switching. No migration tool. No local support.

**ERPNext lens:** Topic 83499 (4,789 views, broken Tally migration) = Tally Survivor validated.

---

### 39. DATEV Prisoner
**File:** `datev-prisoner.md`  
**Market:** Germany  
**What it measures:** Can ERPNext integrate with DATEV instead of replacing it?

**Discovery triggers:**
- German users asking about DATEV compatibility
- 7+ years of DATEV discussion in ERPNext community
- German tax advisors refusing non-DATEV data

**Validation threshold:** DATEV export format is documented. German tax advisors will accept CSV/XML import.

**Red flags:** DATEV format is proprietary and undocumented. Tax advisors won't accept non-DATEV data.

**ERPNext lens:** 127 replies on "DATEV-kompatibel" thread = DATEV Prisoner validated.

---

### 40. FIRS Deadline Fighter
**File:** `firs-deadline-fighter.md`  
**Market:** Nigeria  
**What it measures:** Can ERPNext be made FIRS-compliant before the deadline?

**Discovery triggers:**
- Nigerian companies using ERPNext facing FIRS mandate
- ERPNext not on FIRS supported ERP list
- Government deadline approaching

**Validation threshold:** FIRS API is documented. Solution can be built before deadline. Local compliance partner exists.

**Red flags:** FIRS API is undocumented. Deadline too close. No local partner.

**ERPNext lens:** Topic 149572 (ERPNext not on FIRS supported list) = FIRS Deadline Fighter validated.

---

### 41. SPED Compliance Navigator
**File:** `sped-compliance-navigator.md`  
**Market:** Brazil  
**What it measures:** Can ERPNext handle Brazilian tax compliance?

**Discovery triggers:**
- Brazilian companies asking about ERPNext
- NF-e emission not implemented
- SPED export not implemented

**Validation threshold:** SEFAZ API is accessible. Brazilian compliance expert can be partnered with.

**Red flags:** SEFAZ API is inaccessible. No local expertise available.

**ERPNext lens:** Zero NF-e emission solutions in ERPNext ecosystem = SPED Compliance Navigator sees massive opportunity.

---

### 42. Totvs Escape Artist
**File:** `totvs-escape-artist.md`  
**Market:** Brazil  
**What it measures:** Can Totvs customers escape to ERPNext?

**Discovery triggers:**
- Totvs pricing complaints
- Totvs customers seeking alternatives
- Totvs migration complexity

**Validation threshold:** Totvs migration path exists. Brazilian compliance is solved. Migration consulting demand exists.

**Red flags:** Totvs customers can't leave without full Brazilian compliance. No migration path exists.

**ERPNext lens:** Totvs pricing (R$5,000-50,000+/month) = Totvs Escape Artist has high WTP.

---

### 43. Arabic Digital Transformer
**File:** `arabic-digital-transformer.md`  
**Market:** MENA  
**What it measures:** Can ERPNext be fully Arabic-localized?

**Discovery triggers:**
- Arabic users asking about RTL support
- Arabic print formats not working
- Arabic accounting terminology gaps

**Validation threshold:** RTL Jinja templates can be built. Arabic community exists.

**Red flags:** Arabic community too small. RTL complexity too high.

**ERPNext lens:** Saudi ZATCA Fatoora QR code must appear on Arabic invoices = Arabic Digital Transformer opportunity.

---

### 44. GoBD Compliant
**File:** `gobd-compliant.md`  
**Market:** Germany  
**What it measures:** Can ERPNext meet German legal requirements?

**Discovery triggers:**
- German companies avoiding ERPNext accounting module
- GoBD compliance not addressed
- Tax advisors rejecting ERPNext data

**Validation threshold:** GoBD requirements are documented. Document locking can be implemented.

**Red flags:** GoBD requirements are ambiguous. ERPNext core can't support immutable records.

**ERPNext lens:** ERPNext allows editing submitted documents = violates GoBD's Unveränderlichkeit = GoBD Compliant opportunity.

---

### 45. Mandate Chaser
**File:** `mandate-chaser.md`  
**Market:** Global  
**What it measures:** Can compliance mandates be anticipated and addressed?

**Discovery triggers:**
- Government e-invoicing mandates approaching
- ERPNext not on compliance lists
- Compliance gap before deadline

**Validation threshold:** Mandate is confirmed. ERPNext has a gap. Timeline allows building.

**Red flags:** Mandate is speculative. ERPNext already compliant. No time to build.

**ERPNext lens:** Nigeria FIRS (past deadline), Saudi ZATCA Phase 3 (active), Belgium PEPPOL (Jan 2026) = Mandate Chaser opportunities.

---

### 46. Great Firewall Escapee
**File:** `china.md` (in market-research)  
**Market:** China  
**What it measures:** Can ERPNext serve Chinese companies despite infrastructure barriers?

**Discovery triggers:**
- Chinese companies seeking international-standard ERP
- Frappe Cloud inaccessible in China
- Fapiao requirements not addressed

**Validation threshold:** Chinese infrastructure deployment is feasible. Fapiao API is accessible.

**Red flags:** Fapiao requires government partnership. Frappe Cloud is blocked.

**ERPNext lens:** Alibaba Cloud deployment toolkit = solo-viable. Fapiao = requires government partnership.

---

## When to Use Which Persona

| Situation | Best Personas |
|-----------|-------------|
| Validating WTP | Pre-Sale Interrogator, Small Bets Statistician |
| Assessing market size | Stair-Step Market Sizer, Community Listener |
| Evaluating moat | Moat Architect, Castle Builder, Data Flywheel Founder |
| Checking build time | Speed-First Concierge, Small Bets Statistician |
| Exit planning | Exit Planner, Vertical SaaS Specialist |
| Marketing strategy | Slow Burn Marketer, Engineering Marketer, Small Army Builder |
| Pricing | Pricing Psychologist, Small Bets Statistician |
| Non-English markets | Regional personas (Tally Survivor, DATEV Prisoner, etc.) |
| Compliance opportunities | Wave Catcher, Mandate Chaser, Pre-Sale Interrogator |
| AI opportunities | AI-First Delegator, AI Agent Manager |
| Technical depth | Engineering Marketer, Agnostic Stack Founder |

---

## How to Add New Personas

1. Create a markdown file in `research-personas/` named `[persona-name].md`
2. Define the 6 sections: Profile, Discovery Triggers, Validation Threshold, Red Flags, ERPNext Ecosystem Lens, Opportunity Types Favored/Rejected
3. Add the persona to `research-personas/README.md` in the appropriate category
4. Run the persona through the Phase 1 process alongside existing personas
5. Cross-validate against existing persona outputs

**Good new persona candidates:**
- Founder from a specific industry (manufacturing, healthcare, non-profit)
- Founder from a specific geography (India, Brazil, Germany)
- Founder with specific technical skills (Python developer, UX designer)
- Founder with specific business model (agency, productized service, SaaS)
