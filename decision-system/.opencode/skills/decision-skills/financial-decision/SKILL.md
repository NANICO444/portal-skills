---
name: financial-decision
description: "DECISAO FINANCEIRA RAPIDA — Para @financial-advisor. Vai, nao vai, ou qual valor."
model: tokenrouter/MiniMax-M3
user-invocable: true
allowed-tools: Read, Bash, Grep
---

# Financial Decision — Fast

## Regra de Ouro
Toda decisao financeira tem 3 respostas possiveis:
- **SIM** (vale a pena, fazer)
- **NAO** (nao vale, cortar)
- **VALOR** (se for <=X, fazer)

## Quando Usar
"Devo investir/comprar/contratar X?"
"Vale a pena fazer Y?"
"Quanto posso gastar com Z?"

## Framework (3 perguntas, 30 segundos)

### Q1 — Custo Total
- One-time: R$ X
- Recorrente: R$ Y/mes ou R$ Z/ano
- Hidden: treinamento, manutencao, suporte, integracao
- **CUSTO_TOTAL_12M = X + Y*12 + Z + Hidden**

### Q2 — Retorno Esperado
- Receita direta: R$ A
- Receita evitada (custo que para): R$ B
- Valor estrategico (estimado): R$ C (justifique)
- **RETORNO_12M = A + B + C**

### Q3 — ROI e Payback
- ROI = (RETORNO - CUSTO) / CUSTO * 100%
- Payback = CUSTO_TOTAL / RETORNO_MENSAL
- **DECISAO**:
  - ROI > 100% E Payback < 6 meses → SIM
  - ROI > 30% E Payback < 18 meses → SIM (com cautela)
  - ROI > 0% E Payback > 18 meses → depende do contexto
  - ROI <= 0 → NAO

## Output Esperado

```
CUSTO_TOTAL_12M: R$ X
RETORNO_12M: R$ Y
ROI: Z%
PAYBACK: N meses

DECISAO: SIM/NAO/VALOR

JUSTIFICATIVA: [1 frase com numero]
```

## Quando Pedir Mais Analise
- Investimento > R$ 50k
- Compromisso > 24 meses
- ROI incerto (>50% de variancia)
- Nesses casos: delegue para ultra-powerful/cross-domain-optimization
