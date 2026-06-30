---
name: deep-analysis
description: "ANALISE PROFUNDA - 5 camadas. Use para problemas complexos, decisoes criticas, ou quando precisa entender um sistema inteiro."
model: zenmux/deepseek/deepseek-v4-flash-free
fallback: [zenmux/z-ai/glm-5.2-free]
variant: max
user-invocable: true
allowed-tools: Read, Grep, Glob, Bash, Task
agent: code-architect
---

# Deep Analysis — 5 Camadas

## Mindset
Vai fundo. Nao para na superficie. Cada camada adiciona visao.

## As 5 Camadas

### Camada 1 — OBSERVAVEL
O que esta na superficie?
- Logs, metricas, erros
- Comportamento do usuario
- Resultado esperado vs atual

### Camada 2 — ESTRUTURA
Qual a estrutura?
- Componentes
- Conexoes
- Fluxo de dados
- Estado

### Camada 3 — DINAMICA
Como funciona em movimento?
- Sequencia de eventos
- Interacoes entre componentes
- Concorrência
- Estados possiveis

### Camada 4 — PROPRIEDADES
Que garantias o sistema oferece?
- Invariantes
- Contratos
- Limitacoes
- Restricoes

### Camada 5 — META
O que esta alem do sistema?
- Custo total
- Risco
- Equipe que mantem
- Comunidade

## Output

```
DEEP ANALYSIS — 5 CAMADAS

SISTEMA: [nome]

CAMADA 1 — OBSERVAVEL:
[o que eh visivel]

CAMADA 2 — ESTRUTURA:
[componentes e conexoes]

CAMADA 3 — DINAMICA:
[como funciona em movimento]

CAMADA 4 — PROPRIEDADES:
[garantias e limitacoes]

CAMADA 5 — META:
[custo, risco, manutencao]

INSIGHTS:
1. [insight nao obvio]
2. [insight nao obvio]
3. [insight nao obvio]

ACOES:
1. [acao baseada nos insights]
2. [acao baseada nos insights]
```
