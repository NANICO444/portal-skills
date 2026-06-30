---
name: cross-domain-optimization
description: "OTIMIZACAO CROSS-DOMAIN — Requer Claude Opus 4.8. Use quando precisa otimizar variaveis em multiplos dominios simultaneamente."
model: openrouter/claude-opus-4.8
fallback: [anthropic/claude-opus-4-8, openrouter/deepseek-v4-flash]
user-invocable: true
allowed-tools: Read, Bash, Grep, Task
---

# Cross-Domain Optimization — ULTRA PREMIUM

## MODEL REQUIREMENT

**Claude Opus 4.8** required. DeepSeek V4 Flash acceptable for simpler cases.

## Purpose

Optimize when multiple domains interact and local optima in one domain create global sub-optima. Classical "engineering vs. cost" vs. "speed vs. quality" trade-offs.

## The Pareto Frontier Approach

### Step 1 — Identify Variables
List all variables across domains:
- **Technical**: Latency, throughput, error rate, code complexity
- **Business**: Revenue, cost, time-to-market, customer satisfaction
- **Operational**: Team productivity, support load, run cost
- **Strategic**: Optionality, reversibility, learning value

### Step 2 — Identify Constraints
Hard constraints (cannot violate):
- Compliance (LGPD, HIPAA, PCI-DSS)
- Budget ceiling
- Timeline (hard deadlines)
- Tech stack (already chosen)

Soft constraints (can be relaxed):
- Performance targets
- Code quality standards
- Team preferences

### Step 3 — Identify Objectives
Usually 2-3 in conflict. Examples:
- Maximize performance AND minimize cost (conflicting)
- Maximize speed AND minimize risk (conflicting)
- Maximize learning AND minimize time (conflicting)

### Step 4 — Build Pareto Frontier
For each objective combination, find best solution:
- (MaxPerf, MinCost): Best ROI without sacrificing performance
- (MaxSpeed, MinRisk): Fastest path with risk controlled
- (MaxLearn, MinTime): Most learning in least time

### Step 5 — Sensitivity Analysis
For each decision:
- What if value changes ±10%?
- What if constraint is 10% tighter?
- What if competitor moves first?

### Step 6 — Domain Expert Consultation
For each domain affected:
- Technical: Delegate to @tech-lead → @solution-architect
- Business: Delegate to @financial-advisor → @cost-analyzer
- Operational: Delegate to @ops-manager → @process-optimizer
- Strategic: Delegate to @strategic-planner → @visionary

### Step 7 — Trade-off Decision
Present the Pareto frontier. Let user/stakeholder choose based on context.

## Output Format

```
DOMAINS AFFECTED:
- [Domain 1]: [Current state]
- [Domain 2]: [Current state]
- [Domain 3]: [Current state]

OBJECTIVE TRADE-OFFS:
[Objective A] ←──→ [Objective B]: In conflict (improving A worsens B)
[Objective B] ←──→ [Objective C]: Independent

PARETO SOLUTIONS (best on at least one objective):

Solution Alpha: [Maximize A]
- A: 9/10, B: 5/10, C: 7/10
- Pros: ...
- Cons: ...
- Best when: ...

Solution Beta: [Maximize B]
- A: 5/10, B: 9/10, C: 7/10
- Pros: ...
- Cons: ...
- Best when: ...

Solution Gamma: [Balance A and B]
- A: 7/10, B: 7/10, C: 5/10
- Pros: ...
- Cons: ...
- Best when: ...

SENSITIVITY:
- If [variable] changes ±10%: Solution X becomes preferable

RECOMMENDATION: [Solution X] with [monitoring triggers]
```

## Anti-Patterns

❌ Optimizing one metric to extreme (local optimum, global catastrophe)
❌ Ignoring soft constraints (they bite later)
❌ Pretending domains are independent (they're not)
❌ Single domain expert decides for all (blind spots)
❌ No sensitivity analysis (false confidence)
