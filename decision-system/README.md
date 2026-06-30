# Decision System — Sistema de Decisoes Rapidas

> **Sistema de 6 agentes + 10 sub-agentes para decisoes em 30-60 segundos, sem pensar demais.**

## Visao Geral

Sistema multi-agente OpenCode focado em **tomar decisoes rapidas e inteligentes**. Cada agente tem uma habilidade especifica de decisao.

### 6 Agentes Principais (Decision-Makers)

| Agente | Modelo | Habilidade | Quando Usar |
|--------|--------|-----------|-------------|
| **@strategic-planner** | MiniMax-M3 | Visao, prioridades, direcao | "O que fazer agora?" |
| **@financial-advisor** | MiniMax-M3 | Custos, receita, ROI | "Vale a pena gastar?" |
| **@risk-manager** | MiniMax-M3 | Ameacas, vulnerabilidades | "Isso eh seguro?" |
| **@tech-lead** | DeepSeek V4 Flash | Stack, arquitetura | "Qual lib/framework?" |
| **@marketing-strategist** | DeepSeek V4 Flash | Publico, canais, ROI | "Como vender mais?" |
| **@ops-manager** | DeepSeek V4 Flash | Processos, recursos | "Como organizar?" |

### 10 Sub-Agentes (Specialists)

**Sob MiniMax-M3:**
- `@visionary` (sob strategic-planner) — Pensamento 5 anos
- `@prioritizer` (sob strategic-planner) — Ranking rapido
- `@cost-analyzer` (sob financial-advisor) — Decompor custos
- `@revenue-predictor` (sob financial-advisor) — Forecasting
- `@threat-scanner` (sob risk-manager) — Vulnerabilidades

**Sob DeepSeek V4 Flash:**
- `@solution-architect` (sob tech-lead) — Design tecnico
- `@integrator` (sob tech-lead) — Integracao
- `@campaign-optimizer` (sob marketing-strategist) — ROI marketing
- `@process-optimizer` (sob ops-manager) — Eficiencia
- `@resource-allocator` (sob ops-manager) — Distribuicao

## Skills (11)

### 6 Decision Skills (rapidas, 30-60 segundos)
- `strategic-decision` — Decisao estrategica rapida
- `financial-decision` — Decisao financeira rapida
- `risk-decision` — Decisao de risco rapida
- `tech-decision` — Decisao tecnica rapida
- `marketing-decision` — Decisao de marketing rapida
- `ops-decision` — Decisao operacional rapida

### 5 Ultra-Poderosas (exigem Opus 4.8)
- `complex-architecture-decision` — 7 camadas de analise
- `multi-factor-risk-assessment` — Cascata de riscos
- `cross-domain-optimization` — Pareto frontier
- `adversarial-decision-analysis` — Red team
- `long-term-strategic-forecast` — 2-10 anos

## Estrutura

```
decision-system/
├── .opencode/
│   ├── agents/                  # 6 arquivos .md dos agentes
│   │   ├── decision-makers/    # 3 com MiniMax-M3
│   │   └── specialists/         # 3 com DeepSeek V4 Flash
│   ├── skills/
│   │   ├── decision-skills/     # 6 skills de decisao rapida
│   │   ├── ultra-powerful/      # 5 skills premium (Opus 4.8)
│   │   └── decision-system-master/  # Skill mestre
│   ├── lsp/
│   │   └── lsp.json             # 9 servidores LSP
│   └── mcps/
│       └── mcp.json             # 9 servidores MCP
├── plugins/
│   └── plugins.json             # 6 plugins (metrics, decision-logger, model-router, etc)
├── workspace/
│   └── decisions/               # Historico de decisoes
├── .omo/
│   └── rules/
│       └── always-delegate.md   # Regra permanente
├── opencode.json                # Config principal
└── README.md                    # Este arquivo
```

## Como Usar

### 1. Abrir o TUI no projeto
```bash
opencode --dir decision-system
```

### 2. Pedir uma decisao
```
"Devo investir R$ 30k em marketing de conteudo?"
→ @financial-advisor @marketing-strategist decidem em 30s
```

### 3. Para decisoes criticas
```
"Devo mudar toda a arquitetura para microservicos?"
→ @architect + ultra-powerful/complex-architecture-decision (Opus 4.8)
```

## Modelos

### Tier 1 — Ultra Premium (decisoes criticas)
- **Claude Opus 4.8** — Usado pelas 5 skills ultra-poderosas
- Configuravel via OpenRouter ou Anthropic direto

### Tier 2 — Rapido (decisoes do dia)
- **MiniMax-M3** (tokenrouter) — Decision-makers primarios
- **DeepSeek V4 Flash** (OpenRouter free) — Specialists

## Como o "force Opus 4.8" Funciona

Skills ultra-poderosas tem no frontmatter:
```yaml
model: openrouter/claude-opus-4.8
fallback: [anthropic/claude-opus-4-8, tokenrouter/MiniMax-M3]
```

O plugin `model-router` le isso e:
1. **Se tem API key Opus** → usa Opus 4.8
2. **Se nao tem** → fallback para MiniMax-M3 ou DeepSeek
3. **Sempre registra** qual modelo foi usado

Para ativar Opus real:
```powershell
[Environment]::SetEnvironmentVariable("ANTHROPIC_API_KEY", "sk-...", "User")
[Environment]::SetEnvironmentVariable("OPENROUTER_API_KEY", "sk-...", "User")
```

## LSP e MCP Configurados

### LSP (9 linguagens)
- TypeScript, JavaScript, Python, Rust, Go, HTML, CSS, JSON, YAML, Markdown

### MCP (9 servers)
- filesystem, github, git, fetch, memory, sequential-thinking, puppeteer, brave-search, openrouter

## Plugins (6)
- comment-checker, metrics, decision-logger, model-router, auto-commit

## Proximos Passos

1. Adicionar API key da Anthropic/OpenRouter para Opus 4.8 real
2. Iniciar o sistema: `opencode --dir decision-system`
3. Pedir primeira decisao: `"Devo fazer X?"`
4. Checar historico: `workspace/decisions/`
