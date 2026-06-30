---
name: risk-decision
description: "DECISAO DE RISCO RAPIDA — Para @risk-manager. Classifique e aja em segundos."
model: zenmux/deepseek/deepseek-v4-flash-free
fallback: [zenmux/z-ai/glm-5.2-free]
user-invocable: true
allowed-tools: Read, Bash, Grep
---

# Risk Decision — Fast

## Regra de Ouro
Todo risco tem 1 de 4 acoes:
- **BLOQUEAR** (parar tudo, agora)
- **MITIGAR** (reduzir antes de prosseguir)
- **TRANSFERIR** (seguro, contrato, SLA)
- **ACEITAR** (assumir, orcar para isso)

## Classificacao Rapida (10 segundos)

Para cada risco identificado, pontue 1-5:
- **Probabilidade**: 1=improvavel, 5=quase certo
- **Impacto**: 1=insignificante, 5=existencial
- **Velocidade**: 1=demora, 5=imediato
- **Deteccao**: 5=invisivel, 1=obvio

**SCORE = (Prob × Impacto × Velocidade) / Deteccao**

## Matriz de Decisao

| Score | Acao |
|-------|------|
| >= 50 | BLOQUEAR |
| 20-49 | MITIGAR antes de prosseguir |
| 10-19 | TRANSFERIR (seguro/contrato) |
| 5-9 | ACEITAR com monitoramento |
| < 5 | IGNORAR |

## Quando Usar
"Faz sentido fazer X dado os riscos?"
"Devo bloquear Y?"
"Esse risco eh grande?"

## Output Esperado

```
RISCOS IDENTIFICADOS:

1. [Nome do risco]
   Prob: X/5, Imp: Y/5, Vel: Z/5, Det: W/5
   SCORE: XX
   ACAO: BLOQUEAR/MITIGAR/TRANSFERIR/ACEITAR
   MITIGACAO: [acao especifica]
   OWNER: [quem]
   DEADLINE: [data]

2. ...

DECISAO GERAL: [Prosseguir / Bloquear / Com mitigacoes]
```

## Quando Pedir Mais Analise
- Multiplos riscos correlacionados (efeito cascata)
- Score maximo >= 50 (critico)
- Ambiente regulado (saude, financas, dados pessoais)
- Nesses casos: delegue para ultra-powerful/multi-factor-risk-assessment
