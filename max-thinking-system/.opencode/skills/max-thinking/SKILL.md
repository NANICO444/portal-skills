---
name: max-thinking
description: "PENSAMENTO MAXIMO - raciocinio profundo em 7 camadas. Use para decisoes complexas, analise profunda, ou quando o problema tem multiplas dimensoes."
model: zenmux/deepseek/deepseek-v4-flash-free
fallback: [zenmux/z-ai/glm-5.2-free]
variant: max
user-invocable: true
allowed-tools: Read, Grep, Glob, Bash, Task, WebFetch
agent: code-architect
---

# Max Thinking — 7 Camadas de Raciocinio

## Mindset
Pense 7 vezes. Cada camada adiciona profundidade. Nenhuma decisao superficial.

## As 7 Camadas

### Camada 1 — SUPERFICIE
O que PARECE ser o problema?
- Sintoma observavel
- Mensagem de erro
- Comportamento atual vs esperado

### Camada 2 — CAUSA IMEDIATA
O que CAUSA o sintoma?
- Stack trace
- Estado das variaveis
- Condicao que reproduz

### Camada 3 — CAUSA RAIZ
O que PERMITE a causa imediata?
- Suposicao errada
- Edge case nao tratado
- Corrida/condicao
- Configuracao

### Camada 4 — SISTEMA
Que PROPRIEDADE do sistema permite a causa?
- Acoplamento
- Falta de invariante
- Modelo de dados inconsistente
- Arquitetura que nao previa

### Camada 5 — METODOLOGIA
O que no PROCESSO permitiu?
- Testes insuficientes
- Code review falhou
- Requisitos nao validados
- Docs ausentes

### Camada 6 — CONTEXTO
Que FORCAS EXTERNAS influenciam?
- Time pressure
- Restricao orcamentaria
- Cultura do time
- Expectativa de stakeholder

### Camada 7 — META
O que APRENDEMOS para o futuro?
- Como prevenir?
- Como detectar mais cedo?
- Como melhorar processo?

## Output

```
MAX THINKING — 7 CAMADAS

PROBLEMA: [descricao]

CAMADA 1 - SUPERFICIE:
[sintoma observavel]

CAMADA 2 - CAUSA IMEDIATA:
[causa direta, com evidencia]

CAMADA 3 - CAUSA RAIZ:
[causa raiz, provada]

CAMADA 4 - SISTEMA:
[propriedade do sistema]

CAMADA 5 - METODOLOGIA:
[falha de processo]

CAMADA 6 - CONTEXTO:
[forcas externas]

CAMADA 7 - META:
[aprendizado]

DECISAO: [acao concreta]
TEMPO: [estimativa]
RISCO: [probabilidade × impacto]
```
