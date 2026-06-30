---
description: "SKILL MESTRE — Orquestração do Sistema Multi-Agente OpenCode com 153 Super-Poderes"
mode: "primary"
---

# SKILL MESTRE: ORQUESTRAÇÃO MULTI-AGENTE OPENCODE

## 1. ARQUITETURA DO SISTEMA

```
┌─────────────────────────────────────────────────────────────┐
│                    OPENCODE GUI (PID 17900)                  │
│                  (Interface desktop principal)               │
└─────────────────────────────────────────────────────────────┘
                              │
           ┌──────────────────┼──────────────────┐
           ▼                  ▼                   ▼
┌──────────────────┐ ┌──────────────────┐ ┌──────────────────┐
│  Agent 1 (3001)  │ │  Agent 2 (3002)  │ │  skills repo     │
│ north-mini-code  │ │ gpt-oss-120b     │ │  58022 (GUI)     │
│ 6 sub-agentes    │ │ 4 sub-agentes    │ │                  │
└──────────────────┘ └──────────────────┘ └──────────────────┘
```

### Servidores Headless
- **Agent 1:** `http://127.0.0.1:3001` — Modelo: `opencode/north-mini-code-free`
- **Agent 2:** `http://127.0.0.1:3002` — Modelo: `openrouter/openai/gpt-oss-120b:free`
- **Auth:** Basic Auth (user=`opencode`, password=`b5fb90e2...`)

## 2. SUB-AGENTES

### Agent 1 — Code (north-mini-code-free)
| Agente | Função | Permissão |
|--------|--------|-----------|
| `@orquestrador` | Líder — delega toda tarefa técnica | edit:allow, skill:allow |
| `@code-reviewer` | Revisa qualidade, segurança, boas práticas | edit:deny |
| `@testador` | Cria testes unitários, TDD | edit:allow |
| `@debugger` | Debug sistemático com método científico | edit:allow |
| `@refatorador` | Refatora sem mudar comportamento | edit:allow, bash:allow |
| `@security-auditor` | Audit: SQLi, XSS, credenciais, path traversal | edit:deny |
| `@otimizador` | Performance: algoritmos, memória, I/O, queries | edit:allow |

### Agent 2 — Knowledge (gpt-oss-120b:free)
| Agente | Função | Permissão |
|--------|--------|-----------|
| `@orquestrador-conhecimento` | Líder — delega conhecimento | edit:allow |
| `@pesquisador` | Pesquisa técnica, bibliotecas, APIs | edit:deny |
| `@documentador` | Documentação técnica com exemplos | edit:allow |
| `@arquiteto` | Arquitetura: trade-offs, alternativas, decisões | edit:deny |
| `@devops` | CI/CD, Docker, infra, monitoramento | edit:allow |

## 3. 153 SKILLS INSTALADAS

### Engenharia (Hefesto) — 49 skills
`api-design`, `systematic-debugging`, `test-driven-development`, `codebase-onboarding`, `code-review-checklist`, `database-migrations`, `error-handling`, `architecture-patterns`, `parallel-investigation`, `property-based-testing`, `python-async-patterns`, `python-testing`, `python-typing`, `security-review`, `strict-type-checking`, `using-git-worktrees`, `web-fetch`, `web-scrape`, `writing-plans`, `parallel-tasks`, `plan`, `spike`, `spec-kit`, `tool-evaluator`, `subagent-driven-development`, `typescript-advanced-types`, e mais 26.

### Design (Aurora) — 35 skills
`accessibility-audit`, `component-library`, `design-brief`, `design-extract`, `motion-foundations`, `palette`, `performance-web-vitals`, `popular-web-designs`, `react-doctor`, `seo-advanced`, `baoyu-infographic`, `content-generation`, `deploy-protocol`, `doc-cache`, `doc-read`, `error-recovery-design`, `excalidraw`, `frontend-patterns`, `frontend-stack-decision`, `html-anything`, `make-interfaces-feel-better`, `aurora-workflow`, `aurora-routing`, `aurora-persona-*` (7), e mais.

### Profissionais (oh-my-openagent) — 13 skills
`codex-qa`, `opencode-qa`, `github-triage`, `hyperplan`, `work-with-pr`, `work-with-pr-workspace`, `publish`, `pre-publish-review`, `security-research`, `tech-debt-audit`, `remove-deadcode`, `get-unpublished-changes`, `omomomo`.

### Design Anti-Slop (taste-skill) — 13 skills
`taste-skill`, `taste-skill-v1`, `gpt-tasteskill`, `image-to-code-skill`, `imagegen-frontend-web`, `imagegen-frontend-mobile`, `brandkit`, `redesign-skill`, `soft-skill`, `stitch-skill`, `minimalist-skill`, `brutalist-skill`, `output-skill`.

### Skills Refinadas — 22 skills
`app-builder`, `APP_DEV-templates`, `delegated-development`, `deployment-automation`, `prototype`, `capability-architect`, `improve-codebase-architecture`, `multi-agent-orchestration`, `plan-implementation`, `request-refactor-plan`, `system-design`, `autofix`, `code-review`, `diagnostic-analysis`, `qa`, `quality-validation`, `review`, `aesthetic-analysis`, `design-an-interface`, `ui-ux-pro-max`, `user-interface-designer`, `visual-composition`.

### Universais — 12 skills
`anti-glaze`, `council`, `critical-thinking`, `factual-verify`, `find-skills`, `human-in-the-loop`, `karpathy-discipline`, `submit-improvement-to-themis`, `token-budget-advisor`, `verification-before-completion`, `documentation-lookup`, `impeccable`.

## 4. REGRA PERMANENTE: SEMPRE DELEGAR

Arquivo: `.omo/rules/always-use-agents.md` (`alwaysApply: true`)

**NUNCA execute tarefas diretamente.** Sempre delegue para o sub-agente especializado usando `@nome_do_agente`.

## 5. COMANDOS DE GERENCIAMENTO

```powershell
# Status
.\status-agents.ps1

# Iniciar servidores
.\start-agents.ps1

# Parar servidores
.\stop-agents.ps1

# Delegar tarefa
.\delegar.ps1 <agente> "<tarefa>"
```

## 6. USANDO OS AGENTES VIA CLI

```powershell
# Via servidor headless:
opencode run --attach http://127.0.0.1:3001 --agent code-reviewer "Revise este codigo"

# Ou abrindo TUI no diretorio do agente:
opencode C:\caminho\multi-agent\agent1-north
```

## 7. CONHECIMENTO ABSORVIDO (FONTES)

### .kiro/steering/ (62 specs)
Metodologias Aurora (design) e Hefesto (engenharia). 31 specs cada, cobrindo desde planejamento até entrega.

### .agents/ (vercel-labs)
Centenas de skills para ML/data science/programação com scripts, workflows e referências.

### ULTRA_PROMPT_ANTIGRAVITY
Sistema Nexus de orquestração: 70+ skills de game dev, 49 agentes especialistas, módulos de operação v6.x.

### oh-my-openagent
Plugin OpenCode profissional com 14 hooks, 20-39 tools, sistema de times, MCP, LSP, AST-grep.

### impeccable, taste-skill, superdesign
Frameworks multi-ferramenta (claude, cursor, gemini, opencode, copilot), anti-slop design, IDE de agente.

## 8. FLUXO RECOMENDADO

1. Abra `status-agents.ps1` para verificar servidores
2. Escolha o agente certo para a tarefa (código → Agent 1, conhecimento → Agent 2)
3. Delegue com instruções claras e critério de sucesso
4. Consolide resultados de múltiplos agentes quando necessário
5. Documente decisões em `.omo/notepads/`
