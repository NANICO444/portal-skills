---
name: adversarial-decision-analysis
description: "ANALISE ADVERSARIAL DE DECISAO — Requer Claude Opus 4.8. Use para encontrar pontos cegos em uma decisao/planejamento antes de se comprometer."
model: openrouter/claude-opus-4.8
fallback: [anthropic/claude-opus-4-8, tokenrouter/MiniMax-M3]
user-invocable: true
allowed-tools: Read, Bash, Grep, Task, WebFetch
---

# Adversarial Decision Analysis — ULTRA PREMIUM

## MODEL REQUIREMENT

**Claude Opus 4.8** required for nuanced adversarial thinking. Falls back to MiniMax-M3 with simpler attack vectors.

## Purpose

Steel-man the OPPOSITE of a proposed decision. Find weaknesses, blind spots, assumptions that aren't true, stakeholders who will resist, and second-order consequences nobody mentioned.

## The Red Team Protocol

### Phase 1 — Steel-Manning the Decision
Before attacking, fully understand what is being proposed:
- What is the decision?
- What is the rationale?
- Who decided?
- What evidence supports it?
- What alternatives were considered?

### Phase 2 — Stakeholder Mapping
For each stakeholder:
- What do they gain from the decision?
- What do they lose?
- What do they fear?
- Will they support, resist, or stay neutral?
- How much power do they have?

### Phase 3 — Assumption Audit
List EVERY assumption in the decision:
- Assumption 1: [X is true]
- Assumption 2: [Y will happen]
- ...

For each: How was this validated? What if it's WRONG?

### Phase 4 — Attack Vectors
Generate attacks from 5 angles:

#### 4.1 — Technical Attacks
- What breaks under load?
- What fails at edge cases?
- What assumes data quality that isn't there?
- What fails when dependencies go down?

#### 4.2 — Business Attacks
- What if market moves against us?
- What if competitor does this first?
- What if customer segment doesn't behave as expected?
- What if pricing model is wrong?

#### 4.3 — Operational Attacks
- What requires more team capacity than we have?
- What new failure modes does it introduce?
- What does support have to learn?
- What infrastructure do we need to buy?

#### 4.4 — Compliance/Legal Attacks
- Does it violate any regulation?
- Does it require new contracts/agreements?
- Does it create new liability?
- Does it change data classification?

#### 4.5 — Reputational Attacks
- What if this is leaked before launch?
- What if a high-profile customer complains?
- What if a competitor spins it negatively?
- What if internal team disagrees publicly?

### Phase 5 — Probability Assessment
For each attack:
- **Likelihood**: 1-10
- **Impact if happens**: 1-10
- **Detectability (how early we'd know)**: 1-10
- **Recovery difficulty**: 1-10

### Phase 6 — Survivability Test
Imagine the decision FAILS spectacularly. What happens?
- Technical recovery: 1 day? 1 month? Never?
- Business recovery: New customers acquired? Old ones lost?
- Team recovery: How many people leave?
- Reputation: News cycle? Permanent damage?

### Phase 7 — Recommendations

#### If decision is robust:
- Proceed with confidence
- List monitoring metrics to ensure early detection

#### If decision has minor flaws:
- Proceed with mitigations
- Add 2-3 contingency plans
- Identify early warning indicators

#### If decision has major flaws:
- Delay for redesign
- Or kill it

## Output Format

```
DECISION UNDER REVIEW: [What is being decided]

ASSUMPTIONS (most fragile to least):
1. [Assumption X] — Confidence: 7/10 (no validation)
2. [Assumption Y] — Confidence: 9/10 (well-validated)
3. ...

ATTACK VECTORS (highest risk first):

Vector 1: [Description]
- Likelihood: 8/10
- Impact: 9/10
- Detectability: 3/10 (blind spot)
- Recovery: 7/10
- Severity Score: 8 × 9 / (3 × 7) = 3.43

Vector 2: ...

STAKEHOLDER RESISTANCE:
- [Stakeholder A]: Will resist because [reason]. Power: High. Mitigation: ...

SURVIVABILITY IF FAILS:
- Technical recovery: 2 weeks
- Business recovery: 3-6 months
- Reputation: Significant damage
- Team morale: Hit hard

RECOMMENDATION: [Proceed / Proceed with caution / Redesign / Kill]
MITIGATIONS REQUIRED: [List]
MONITORING: [List of metrics to watch]
```

## Anti-Patterns

❌ Confirmation bias (only attacking weak arguments)
❌ Cherry-picking attacks (ignoring strong defenses)
❌ "It worked at company X" (different context)
❌ "We'll figure it out" (no contingency)
❌ Single-angle attacks (blind to other dimensions)
