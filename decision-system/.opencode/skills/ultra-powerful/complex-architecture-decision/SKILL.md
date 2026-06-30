---
name: complex-architecture-decision
description: "DECISAO DE ARQUITETURA COMPLEXA — Esta skill TECNICAMENTE requer Claude Opus 4.8 (Ultra Premium). Use para decisoes de sistema com multiplas variaveis interconectadas."
model: openrouter/claude-opus-4.8
fallback: [anthropic/claude-opus-4-8, tokenrouter/MiniMax-M3, openrouter/deepseek-v4-flash]
user-invocable: true
allowed-tools: Read, Grep, Glob, Bash, Task
---

# Complex Architecture Decision — ULTRA PREMIUM

## MODEL REQUIREMENT

This skill REQUIRES **Claude Opus 4.8** (or fallback to Anthropic Opus 4.8).

If neither is available, the system falls back to MiniMax-M3 with reduced confidence.

## When to Use

For architecture decisions involving:
- 5+ interconnected components
- Multiple trade-offs (cost, latency, complexity, team skills)
- Long-term impact (>2 years)
- High cost of reversal (>6 months to undo)
- Cross-domain considerations (technical + business + operational)

## The 7-Layer Decision Framework

### Layer 1 — Context Capture
- What problem are we solving?
- Who are the stakeholders?
- What's the budget ceiling?
- What's the timeline?
- What constraints exist (team, tech, compliance)?

### Layer 2 — Option Generation
Generate AT LEAST 3 distinct approaches:
- **Option A**: Conservative (proven, lower risk)
- **Option B**: Balanced (mix of new + proven)
- **Option C**: Aggressive (innovative, higher reward/risk)

For each: tech stack, team requirements, cost, timeline, risks.

### Layer 3 — Trade-off Matrix
Build a matrix:
| Criterion | Weight | Option A | Option B | Option C |
|-----------|--------|----------|----------|----------|
| Performance | 0.20 | X/10 | Y/10 | Z/10 |
| Maintainability | 0.20 | X/10 | Y/10 | Z/10 |
| Cost (TCO) | 0.15 | X/10 | Y/10 | Z/10 |
| Time-to-market | 0.15 | X/10 | Y/10 | Z/10 |
| Reversibility | 0.10 | X/10 | Y/10 | Z/10 |
| Team fit | 0.10 | X/10 | Y/10 | Z/10 |
| Innovation | 0.10 | X/10 | Y/10 | Z/10 |

Weighted score = sum(criterion_weight * option_score).

### Layer 4 — Stress Test
- What if user load is 10x current?
- What if 2 key engineers leave?
- What if compliance changes?
- What if competitor launches similar feature first?
- What if cost doubles?

### Layer 5 — Second-Order Effects
- What does Option A enable that's not obvious?
- What does Option B block in the future?
- What does Option C require culturally?

### Layer 6 — Decision
Pick ONE option with:
- Clear rationale (max 3 sentences)
- Pre-commitment to specific metrics (we'll measure X at Y date)
- Exit criteria (we'll abandon if Z happens)

### Layer 7 — Documentation
- ADR (Architecture Decision Record)
- Communicated to all stakeholders
- Linked to roadmap

## Anti-Patterns

❌ "Let's just go with what's popular"
❌ "We don't have time for analysis" (you don't have time NOT to analyze)
❌ Single option considered
❌ Decision deferred "until later"
❌ Reversibility ignored
❌ Team input not sought

## Output Format

```
RECOMMENDATION: [Option B]

RATIONALE (3 sentences max):
1. [Why this option wins on weighted score]
2. [Why the trade-offs are acceptable]
3. [Why we can execute it]

PRE-COMMITMENT METRICS:
- [Metric 1]: [Target] by [Date]
- [Metric 2]: [Target] by [Date]

EXIT CRITERIA (we abandon if):
- [Trigger 1]
- [Trigger 2]

ADR LINK: [path to ADR]
```

## Reusability

After execution, save the framework + decision to:
- `workspace/decisions/YYYY-MM-DD-<topic>.md`
- Indexed in `workspace/decisions/README.md`
