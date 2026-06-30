---
name: ops-decision
description: "DECISAO OPERACIONAL RAPIDA — Para @ops-manager. Eficiencia primeiro."
model: zenmux/deepseek/deepseek-v4-flash-free
fallback: [zenmux/z-ai/glm-5.2-free]
user-invocable: true
allowed-tools: Read, Bash, Grep
---

# Ops Decision — Fast

## Regra de Ouro
Toda decisao operacional responde a:
- Economiza tempo/dinheiro?
- Escala ou quebra?
- Quem faz e quando?

## Quando Usar
"Como organizar processo X?"
"Quem faz Y?"
"Automatizar ou fazer manual?"

## Framework (5 Perguntas, 30 segundos)

### Q1 — Frequencia?
- Diaria: alta prioridade para automacao
- Semanal: media
- Mensal ou menos: manter manual ou documentar bem

### Q2 — Tempo atual?
- Medir: quanto tempo leva hoje
- Custo: horas * custo-hora-equipe

### Q3 — Pode ser automatizado?
- Script simples: SIM
- Workflow complex: depende
- Decisao humana: NAO automatizar

### Q4 — Custo da automacao?
- Tempo para construir
- Manutencao continua
- Risco de quebrar

### Q5 — ROI da automacao?
- ROI = (tempo_economizado * 12 - custo_construcao) / custo_construcao
- ROI > 100% em 6 meses = AUTOMATIZAR
- ROI < 50% = MANTER MANUAL
- Entre: depende do risco

## Output Esperado

```
PROCESSO: [nome]

FREQUENCIA: [diaria/semanal/mensal]
TEMPO ATUAL: X horas/vezes
CUSTO ATUAL: R$ Y/mes

AUTOMATIZAVEL: [sim/parcial/nao]
CUSTO AUTOMACAO: R$ Z (construcao) + R$ W/mes (manutencao)
ROI AUTOMACAO: P%

DECISAO: [AUTOMATIZAR / MANTER MANUAL / DOCUMENTAR]

OWNER: [quem implementa]
DEADLINE: [data]
METRICAS: [tempo economizado, erros reduzidos]
```

## Quando Pedir Mais Analise
- Mudanca de organograma
- Processo regulado/compliance
- Decisao de build vs buy para ferramenta
- Nesses casos: delegue para ultra-powerful/complex-architecture-decision
