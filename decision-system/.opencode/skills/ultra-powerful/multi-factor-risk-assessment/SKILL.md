---
name: multi-factor-risk-assessment
description: "AVALIACAO MULTI-FATORIAL DE RISCO — Requer Claude Opus 4.8. Use para analise de risco onde multiplos fatores interagem."
model: openrouter/claude-opus-4.8
fallback: [anthropic/claude-opus-4-8, tokenrouter/MiniMax-M3]
user-invocable: true
allowed-tools: Read, Bash, Grep, WebFetch
---

# Multi-Factor Risk Assessment — ULTRA PREMIUM

## MODEL REQUIREMENT

**Claude Opus 4.8** preferred. Falls back to MiniMax-M3 with caveat.

## Purpose

Comprehensive risk analysis where multiple risk factors interact in non-obvious ways. Goes beyond simple probability × impact.

## The Cascade Risk Model

Traditional risk = Probability × Impact. This skill adds:
- **Correlation**: How risks amplify each other
- **Cascading**: How one risk triggers others
- **Velocity**: How fast risk materializes
- **Recovery**: How easy/hard to recover

### Step 1 — Risk Inventory
List ALL possible risks (use 5 categories):
1. **Technical**: Bugs, scaling, security, data loss
2. **Business**: Market change, competitor, pricing
3. **Operational**: Team, vendor, infrastructure
4. **Compliance**: Legal, regulatory, GDPR/LGPD
5. **Reputational**: PR, customer trust, social media

For each risk: ID, name, description.

### Step 2 — Multi-Factor Scoring
Score each risk on 5 dimensions (1-10):
- **Probability**: How likely (1=rare, 10=almost certain)
- **Impact**: How damaging (1=trivial, 10=existential)
- **Velocity**: How fast (1=years, 10=immediate)
- **Recovery**: How easy to recover (1=irreversible, 10=trivial)
- **Detectability**: How easy to detect early (1=invisible, 10=obvious)

### Step 3 — Correlation Matrix
For each pair of risks (R_i, R_j): are they correlated?
- **-1**: Inverse (one prevents the other)
- **0**: Independent
- **+1**: Fully correlated (one triggers the other)

### Step 4 — Cascade Mapping
Build a dependency graph:
```
R1 ──triggers──> R5 ──triggers──> R8
                  │
                  └──triggers──> R12
```

### Step 5 — Risk Score
For each risk, calculate:
```
Score = (Probability × Impact × Velocity) / (Recovery × Detectability)
```

### Step 6 — Portfolio View
Total risk = sum of (individual risk × correlation factors).

### Step 7 — Mitigation Strategy
For top 5 risks:
- **Avoid**: Eliminate the risk entirely
- **Mitigate**: Reduce probability/impact
- **Transfer**: Insurance, contracts, SLA
- **Accept**: Acknowledge and budget for it

## Output Format

```
TOP 5 RISKS:

1. [Risk Name] — Score: X.XX
   Mitigation: [Avoid/Mitigate/Transfer/Accept]
   Action: [Specific action]
   Owner: [Role/Team]
   Deadline: [Date]

2. ...

CASCADE PATH (highest impact):
[Risk A] → [Risk B] → [Risk C]
Likelihood of cascade: XX%

OVERALL RISK SCORE: X.XX/100
RISK TOLERANCE: [Within/Exceeds]
RECOMMENDATION: [Proceed/Proceed with caution/Stop]
```

## Red Flags

❌ Risks assessed in isolation (ignores correlation)
❌ "We'll deal with it if it happens" (no contingency)
❌ Same person assesses and owns mitigation (conflict of interest)
❌ No time-stamped re-evaluation (risks change)
