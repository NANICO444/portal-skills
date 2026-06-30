---
name: long-term-strategic-forecast
description: "PREVISAO ESTRATEGICA DE LONGO PRAZO — Requer Claude Opus 4.8. Use para planejar 2+ anos a frente."
model: zenmux/deepseek/deepseek-v4-flash-free
fallback: [zenmux/z-ai/glm-5.2-free]
user-invocable: true
allowed-tools: Read, Bash, Grep, Task, WebFetch
---

# Long-Term Strategic Forecast — ULTRA PREMIUM

## MODEL REQUIREMENT

**Claude Opus 4.8** required for deep pattern recognition over long horizons. Falls back to MiniMax-M3 with reduced confidence intervals.

## Purpose

Strategic foresight over 2-10 year horizons. Where the world/industry/market is going, and what to do about it NOW.

## The Scenario Planning Framework

### Step 1 — Define the Focal Question
What decision needs the long-term view?
Examples:
- Should we build vs. buy vs. partner for capability X?
- Should we invest in technology Y now or wait?
- What new market should we enter?
- What talent should we hire?

### Step 2 — Identify Driving Forces
Forces that shape the future:
- **Technology** (AI, quantum, biotech, energy)
- **Demographics** (aging, urbanization, remote work)
- **Economics** (rates, inflation, supply chains)
- **Regulation** (privacy, antitrust, environment)
- **Social** (values, expectations, behavior)
- **Geopolitics** (trade, conflict, alliances)

For each force: Current trajectory, key uncertainties, signs of change.

### Step 3 — Identify Critical Uncertainties
Which uncertainties have HIGH impact AND HIGH uncertainty?
- High impact + High uncertainty: Scenario-critical
- High impact + Low uncertainty: Plan for it
- Low impact + High uncertainty: Monitor
- Low impact + Low uncertainty: Ignore

### Step 4 — Build 2x2 Scenario Matrix
Pick the 2 most critical uncertainties. Create 4 scenarios:
- (High A, High B): [Name this scenario]
- (High A, Low B): [Name]
- (Low A, High B): [Name]
- (Low A, Low B): [Name]

For each scenario, paint a vivid picture:
- What's daily life like?
- What's the customer's reality?
- What tech exists?
- What dominates the market?

### Step 5 — Stress-Test Each Scenario
For each:
- Does our current strategy work?
- What breaks?
- What's irrelevant that we thought mattered?
- What's critical that we ignored?

### Step 6 — Identify "Robust" Strategies
Strategies that work in MULTIPLE scenarios:
- ✅ Works in 3-4 scenarios: Robust — pursue
- ⚠️ Works in 2 scenarios: Conditional — pursue with hedges
- ❌ Works in 1 scenario: Brittle — avoid

### Step 7 — Identify "Bet-Hedging" Actions
Optionality-preserving moves:
- Small investments in multiple directions
- Partnerships with non-exclusive terms
- Modular architecture (can pivot)
- Talent with transferable skills

### Step 8 — Wild Cards
Low-probability but high-impact events:
- Black swans (totally unexpected)
- Grey rhinos (highly likely but ignored)
- For each: what would we do? Early indicators to watch?

### Step 9 — Recommendations
- **Commit to**: Robust strategies for sure
- **Hedge**: Conditional strategies with monitoring
- **Avoid**: Brittle strategies
- **Monitor**: Wild card early indicators

## Output Format

```
FOCAL QUESTION: [The decision needing long-term view]

HORIZON: [2 / 5 / 10 years]

DRIVING FORCES (most impactful):
1. [Force X] — Trajectory: [increasing/stable/decreasing]
2. ...

CRITICAL UNCERTAINTIES:
1. [Uncertainty Y] — Impact: 9/10, Uncertainty: 8/10
2. ...

SCENARIO MATRIX:

|              | [High B] | [Low B] |
|--------------|----------|---------|
| [High A]     | "Phoenix" | "Steady Growth" |
|              | [Vivid description] | [Description] |
| [Low A]      | "Disruption" | "Decline" |
|              | [Description] | [Description] |

ROBUST STRATEGIES (work in 3-4 scenarios):
1. [Strategy] — Works in: Phoenix, Steady Growth, Decline
   Action: [Specific steps]
   Investment: $X / month
   Reversible: Yes/No

2. ...

HEDGED STRATEGIES (work in 2 scenarios):
1. [Strategy] — Works in: Phoenix, Disruption
   Conditions: Trigger to commit: [indicator]
   Conditions: Trigger to abandon: [indicator]

BRITTLE STRATEGIES TO AVOID:
1. [Strategy] — Only works in Phoenix (single scenario)
   Why avoid: 75% chance of failure

WILD CARDS TO MONITOR:
1. [Wild card] — Probability: 5%, Impact: 10/10
   Early indicators: [List]
   If happens: [Response]

RECOMMENDATIONS:
- Commit now: [Robust strategies]
- Conditional: [Hedged strategies]
- Avoid: [Brittle strategies]
- Quarterly review: [Monitoring triggers]
```

## Anti-Patterns

❌ Single-scenario planning (false confidence)
❌ Linear extrapolation (curveballs are common)
❌ Ignoring weak signals (early warnings)
❌ "Best case" bias (plan for success, ignore failure modes)
❌ Over-commitment to single strategy (no optionality)
❌ Ignoring low-probability high-impact events
