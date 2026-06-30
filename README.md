# Skills Pastas Melhorias Agentes

> **Projeto de kit de super-poderes para OpenCode.**
> Fontes absorvidas, sintetizadas, e organizadas em 3 sistemas especializados.

---

## O que é este projeto

Este projeto é um **kit curado de skills, agentes, e ferramentas para OpenCode**. Ele reune:

- **9 pastas-fonte de conhecimento** absorvidas (kiro, vercel-labs, ULTRA_PROMPT_NEXUS, oh-my-openagent, aurora, hefesto, taste-skill, impeccable, etc.)
- **181+ skills sintetizadas** em formato OpenCode (frontmatter YAML + markdown)
- **35+ agentes especializados** distribuidos em 3 sistemas
- **3 regras de comportamento** que o OpenCode aplica automaticamente

**Origem das fontes** (NÃO MODIFICADAS):
| Pasta | Conteudo | Tamanho estimado |
|-------|----------|------------------|
| `.kiro/` | Steering specs do Kiro | pequeno |
| `.agents/` | Vercel-labs AI skills (scripts + workflows) | medio |
| `ULTRA_PROMPT_ANTIGRAVITY/` | Sistema Nexus (CORE + 75 skills + 49 agentes) | grande (40+MB) |
| `SKILLS/` | Aurora (54) + Hefesto (71) skills | medio |
| `oh-my-openagent/` | Plugin OpenCode completo | medio |
| `referencias_originais/` | Documentos fonte | pequeno |
| `skills_github/` | Impeccable + taste-skill + superdesign | medio |
| `skills_refinadas/` | Skills finais | medio |
| `NOVO_ULTRA_PROMPT_PROJETOS.md` | Spec grande | 1 arquivo |

---

## Os 3 sistemas criados

Cada sistema tem proposito claro. Use o que faz sentido para sua tarefa.

### 1. `multi-agent/` — Codigo com servidores headless

**Quando usar:** Trabalho de codigo, code review, debug, implementacao.

**Config:** 2 servidores headless rodando (portas 3001, 3002).

| Agente primario | Modelo | Sub-agentes |
|-----------------|--------|-------------|
| `orquestrador` | opencode/north-mini-code-free | 6 (code-reviewer, testador, debugger, refatorador, security-auditor, otimizador) |
| `orquestrador-conhecimento` | openrouter/openai/gpt-oss-120b:free | 4 (pesquisador, documentador, arquiteto, devops) |

**Arquivos uteis:**
- `INSTRUCAO_OPENCODE.md` (16.5 KB) — manual completo de uso
- `agentes-info.txt` — referencia rapida
- Scripts: `start-agents.ps1`, `stop-agents.ps1`, `status-agents.ps1`, `delegar.ps1`

### 2. `decision-system/` — Decisoes rapidas

**Quando usar:** Precisa decidir SIM/NAO rapido, ou responder em 30-60 segundos.

**Config:** Nao roda como servidor; usa o config global.

| Agente primario | Modelo | Tempo de resposta |
|-----------------|--------|-------------------|
| `strategic-planner` | MiniMax-M3 (variant minimal) | 60s |
| `financial-advisor` | MiniMax-M3 (variant minimal) | 30s |
| `risk-manager` | MiniMax-M3 (variant minimal) | 30s |
| `tech-lead` | DeepSeek V4 Flash (variant minimal) | 30s |
| `marketing-strategist` | DeepSeek V4 Flash (variant minimal) | 30s |
| `ops-manager` | DeepSeek V4 Flash (variant minimal) | 30s |

**Skills uteis:**
- 6 skills de decisao rapida (uma por agente)
- 5 skills ultra-poderosas (exigem Opus 4.8)

### 3. `max-thinking-system/` — Supervisao profunda

**Quando usar:** Code review rigoroso, decisoes criticas, analise profunda.

**Config:** Default global. `variant: max` em todos.

**3 agentes principais:**
- `@supervisor` — ve TUDO, aprova/rejeita codigo
- `@code-architect` — design de sistema
- `@quality-gate` — aprovacao final

**9 sub-agentes de auditoria:** code-reviewer-x, fix-suggester, library-curator, dependency-auditor, standards-enforcer, security-auditor, performance-auditor, test-coverage-auditor, docs-auditor.

**Skill principal:** `supervisor` — diz O QUE APAGAR, O QUE ADICIONAR, O QUE FAZER, O QUE BAIXAR.

---

## Como usar

### Para OpenCode usar automaticamente em qualquer sessao

O OpenCode global ja tem:
- `~/.config/opencode/skills/` → junction com 181 skills deste projeto
- `~/.config/opencode/agents/` → junction com agentes do max-thinking
- `~/.config/opencode/rules/` → regras always-* aplicadas em todo chat

**Basta reiniciar o OpenCode.** Em qualquer chat novo, ele ja vem com tudo.

### Para abrir o TUI em um sistema especifico

```bash
# Sistema 1: Multi-agent com servidores headless
opencode --dir "skills pastas melhorias agentes\multi-agent"

# Sistema 2: Decision system
opencode --dir "skills pastas melhorias agentes\decision-system"

# Sistema 3: Max-thinking
opencode --dir "skills pastas melhorias agentes\max-thinking-system"
```

### Para gerenciar os servidores (so sistema 1)

```powershell
cd "skills pastas melhorias agentes\multi-agent"
.\status-agents.ps1
.\start-agents.ps1
.\stop-agents.ps1
```

---

## Estrutura completa

```
skills pastas melhorias agentes/
├── README.md                   ← Este arquivo
├── ARCHITECTURE.md             ← Mapa detalhado dos 3 sistemas
├── INDEX.md                    ← Indice de skills principais
├── WORKFLOWS.md                ← Fluxos de uso pratico
├── NOVO_ULTRA_PROMPT_PROJETOS.md (fonte, nao tocado)
│
├── .kiro/                      ← Fonte: Kiro steering (nao tocado)
├── .agents/                    ← Fonte: Vercel-labs skills (nao tocado)
├── ULTRA_PROMPT_ANTIGRAVITY/   ← Fonte: Sistema Nexus (nao tocado)
├── SKILLS/                     ← Fonte: Aurora + Hefesto (nao tocado)
├── oh-my-openagent/            ← Fonte: Plugin completo (nao tocado)
├── referencias_originais/      ← Fonte (nao tocado)
├── skills_github/              ← Fonte: Impeccable + taste (nao tocado)
├── skills_refinadas/           ← Fonte (nao tocado)
│
├── multi-agent/                ← SISTEMA 1
│   ├── INSTRUCAO_OPENCODE.md
│   ├── agentes-info.txt
│   ├── agent1-north/opencode.json
│   ├── agent2-gptoss/opencode.json
│   ├── .opencode/skills/ (164 skills)
│   ├── .opencode/node_modules/ (REMOVIDO - era lixo)
│   ├── .omo/rules/always-use-agents.md
│   ├── start-agents.ps1, stop-agents.ps1, status-agents.ps1, delegar.ps1
│   └── README.md
│
├── decision-system/            ← SISTEMA 2
│   ├── opencode.json
│   ├── README.md
│   ├── .omo/rules/always-delegate.md
│   ├── .opencode/agents/ (6 .md)
│   ├── .opencode/skills/ (12 SKILL.md)
│   ├── .opencode/lsp/lsp.json (9 servers)
│   ├── .opencode/mcps/mcp.json (9 servers)
│   └── plugins/plugins.json
│
├── max-thinking-system/        ← SISTEMA 3
│   ├── opencode.json
│   ├── README.md
│   ├── .omo/rules/always-supervise.md
│   ├── .opencode/agents/ (12 .md)
│   ├── .opencode/skills/ (6 SKILL.md)
│   ├── .opencode/lsp/lsp.json (14 servers)
│   ├── .opencode/mcps/mcp.json (14 servers)
│   └── plugins/plugins.json
│
└── templates/                  ← Templates uteis
    ├── PR.md
    ├── ADR.md
    └── review.md
```

---

## Proximos passos recomendados

1. **Leia `ARCHITECTURE.md`** para entender os 3 sistemas
2. **Leia `INDEX.md`** para encontrar as skills certas rapido
3. **Use `WORKFLOWS.md`** para fluxos de uso pratico
4. **Reinicie o OpenCode** para carregar tudo no global
