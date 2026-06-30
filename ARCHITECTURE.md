# Arquitetura dos 3 Sistemas

> **Mapa detalhado do que cada sistema faz, quando usar, e como se relacionam.**

## Visao Geral

```
┌────────────────────────────────────────────────────────────┐
│  SISTEMA 1: multi-agent/ (SOM ATIVO)                       │
│  Codigo + Servidores Headless + 164 skills sintetizadas    │
│  Quando: trabalho de codigo, code review, implementacao   │
├────────────────────────────────────────────────────────────┤
│  SISTEMA 2: decision-system/                               │
│  Decisao rapida em 30-60s + 6 decisores + 5 ultra-poderosos│
│  Quando: pergunta SIM/NAO, decisao rapida, ROI            │
├────────────────────────────────────────────────────────────┤
│  SISTEMA 3: max-thinking-system/ (DEFAULT GLOBAL)          │
│  Supervisao com pensamento maximo + 12 agents              │
│  Quando: code review rigoroso, decisao critica, auditoria  │
└────────────────────────────────────────────────────────────┘
```

## Decisao rapida: qual sistema usar

| Sua tarefa... | Sistema |
|---------------|---------|
| Escrever/revisar codigo | multi-agent OU max-thinking |
| Decidir entre opcoes rapido | decision-system |
| Aprovar um PR com rigor | max-thinking |
| Pesquisar tecnologia | multi-agent (agent2) |
| Corrigir bug | multi-agent (debugger) |
| Fazer deploy / CI/CD | multi-agent (devops) |
| Auditoria completa | max-thinking |
| Pergunta de negocio (ROI, custo) | decision-system (financial) |
| Calcular risco | decision-system (risk) |

## Sistema 1: multi-agent (mais antigo, ja testado)

### Infraestrutura
- 2 servidores headless rodando (portas 3001, 3002)
- Scripts de gerencia: `start/stop/status/delegar`
- `.opencode/node_modules/` ja foi removido (48 MB de lixo)

### Agentes
- **Agent 1 (3001):** `orquestrador` + 6 sub-agentes de codigo (code-reviewer, testador, debugger, refatorador, security-auditor, otimizador)
- **Agent 2 (3002):** `orquestrador-conhecimento` + 4 sub-agentes (pesquisador, documentador, arquiteto, devops)

### Skills instaladas (164)
- 49 Hefesto (engenharia)
- 35 Aurora (design)
- 13 oh-my-openagent
- 13 taste-skill
- 22 skills refinadas
- 12 universais
- 10 skills sintetizadas dos fontes (kiro + ULTRA_PROMPT + impeccable)
- 10 outras

### Quando NAO usar
- Para decisao rapida (use decision-system)
- Para code review rigoroso (use max-thinking)

## Sistema 2: decision-system (decisao rapida)

### Infraestrutura
- Nao roda como servidor; usa o OpenCode CLI diretamente
- 16 agents definidos (6 primary + 10 sub)
- 12 skills (6 decisao + 5 ultra + 1 master)

### Agentes primarios (todos com variant: minimal = resposta rapida)
- `strategic-planner` (MiniMax-M3) — visao, direcao
- `financial-advisor` (MiniMax-M3) — ROI, custo
- `risk-manager` (MiniMax-M3) — risco, compliance
- `tech-lead` (DeepSeek V4 Flash) — stack
- `marketing-strategist` (DeepSeek V4 Flash) — publico, canal
- `ops-manager` (DeepSeek V4 Flash) — processo, recurso

### Sub-agentes
10 distribuidos: visionary, prioritizer, cost-analyzer, revenue-predictor, threat-scanner, solution-architect, integrator, campaign-optimizer, process-optimizer, resource-allocator.

### Skills notaveis
- `complex-architecture-decision` (exige Opus 4.8) — 7 camadas
- `multi-factor-risk-assessment` (exige Opus 4.8) — cascata de riscos
- `cross-domain-optimization` (exige Opus 4.8) — pareto
- `adversarial-decision-analysis` (exige Opus 4.8) — red team
- `long-term-strategic-forecast` (exige Opus 4.8) — 2-10 anos

### Quando NAO usar
- Para implementacao de codigo (use multi-agent)
- Para code review rigoroso (use max-thinking)

## Sistema 3: max-thinking-system (supervisor de codigo)

### Infraestrutura
- Default global do OpenCode
- Todos os 12 agents com `variant: max` (maximo pensamento)
- 6 skills especializadas + 1 skill supervisora

### Agentes
- **3 principais:**
  - `supervisor` (MiniMax-M3 max) — ve TUDO, aprova/rejeita
  - `code-architect` (MiniMax-M3 max) — design
  - `quality-gate` (MiniMax-M3 max) — qualidade
- **9 specialists:** code-reviewer-x, fix-suggester, library-curator, dependency-auditor, standards-enforcer, security-auditor, performance-auditor, test-coverage-auditor, docs-auditor

### Skill principal: `supervisor`
Quando invocada, retorna output estruturado com:
- VEREDITO (APROVADO / RESSALVAS / REJEITADO)
- SCORE 0-100
- O QUE APAGAR (linhas especificas)
- O QUE ADICIONAR (codigo novo)
- O QUE FAZER (proximos passos)
- O QUE BAIXAR (bibliotecas com comando de install)

### Quando NAO usar
- Para tarefas triviais (formulas, one-liners)
- Para brainstorming livre (use multi-agent)

## Relacao entre os sistemas

```
multi-agent (codigo com servidores)
    ↓ usa skills
164 skills sintetizadas
    ↓ skills compartilhadas
tambem disponiveis em max-thinking
    ↓ decisao rapida chama
decision-system
    ↑ se tarefa for critica
max-thinking (supervisao)
```

## Sobreposicoes conhecidas (e porque foram mantidas)

| Recurso | Aparece em | Justificativa |
|---------|------------|---------------|
| `code-reviewer` | multi-agent + max-thinking (como code-reviewer-x) | multi-agent: rapido, max-thinking: rigoroso |
| `security-auditor` | multi-agent + max-thinking | multi-agent: aviso geral, max-thinking: auditoria OWASP |
| `arquiteto` | multi-agent (agent2) + decision-system | multi-agent: knowledge, decision-system: decisao |
| LSP/MCP | todos os 3 sistemas | Cada sistema eh independente; cada um tem seu .opencode/ |

## Sobreposicoes removidas (curadoria)

- `node_modules` (48 MB) do multi-agent — removido
- `server.log/err` antigos — removido
- Multiplos INSTRUCAO_*.md — agora `INSTRUCAO_OPENCODE.md` (multi-agent) + `README.md` global + `README.md` em cada sistema
- Multiplas regras always-* — em breve consolidadas em 1
