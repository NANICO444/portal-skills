# Hefesto — Skills List

**Total**: 19 universais + 42 específicas = **61 skills**
**Última atualização**: 2026-05-22 (Fase C2 — análise crítica `hermes_codigo_research.md`: adicionados `security-scan` + `codebase-onboarding` + `debugging-hermes-tui-commands`)

> Comandos de instalação são padrão Hermes:
> - Bundled (já vem): nada a fazer, só habilitar via `hermes -p hefesto skills enable <skill>`
> - Hub: `hermes -p hefesto skills install <skill>` ou `hermes -p hefesto skills install official/<category>/<skill>`
> - Custom (a criar): escrita manual em `~/.hermes/profiles/hefesto/skills/<skill>/SKILL.md`

---

## SKILLS UNIVERSAIS (17 — todos os cérebros têm)

> Modulações específicas do Hefesto entre parênteses

| # | Skill | Categoria | Modulação Hefesto |
|---|---|---|---|
| 1 | `tavily-search` | research | 1 key (Apollo+Midas têm 3) |
| 2 | `web-fetch` | research | — |
| 3 | `web-scrape` | research | — |
| 4 | `doc-cache` | research | — |
| 5 | `doc-read` | research | — |
| 6 | `ocr` | media | — |
| 7 | `maton-gateway` | integration | — |
| 8 | `factual-verify` | quality | — |
| 9 | `verification-before-completion` | quality | **RÍGIDO** — build+test+lint+diff sempre |
| 10 | `anti-glaze` | behavior | Forte (focado em review de diff e dependência) |
| 11 | `karpathy-discipline` | behavior | **RÍGIDO por padrão** (Apollo é NORMAL) |
| 12 | `find-skills` | meta | Busca + recomenda. **NÃO instala** |
| 13 | `token-budget-advisor` | meta | — |
| 14 | `council` | reasoning | Sob demanda (dilema técnico ambíguo) |
| 15 | `documentation-lookup` | research | — |
| 16 | `duckduckgo-search` | research | Fallback |
| 17 | `native-mcp` | mcp | MCP client |
| 18 | `critical-thinking` | behavior | **Drive Ultra Prompt v6.2** — universal, todos cérebros |
| 19 | `human-in-the-loop` | behavior | **Drive Ultra Prompt v6.2** — universal, todos cérebros |

> **Origem 18/19**: `~/Desktop/Hermes_Project/05_ultra_prompt_v62_referencia/Ultra Prompt v6.2/skills/common/{critical-thinking.md, human-in-the-loop.md}` — adicionadas após debate Aurora (2026-05-22) por consistência sistêmica.

---

## SKILLS ESPECÍFICAS HEFESTO (39)

### TDD / Testing (3)
| # | Skill | Origem |
|---|---|---|
| 1 | `test-driven-development` | Hermes nativo |
| 2 | `python-testing` | ECC |
| 3 | `ai-regression-testing` | ECC (anti blind-spot) |

### Debug (6)
| # | Skill | Origem |
|---|---|---|
| 4 | `systematic-debugging` | Hermes nativo |
| 5 | `python-debugpy` | Hermes nativo |
| 6 | `node-inspect-debugger` | Hermes nativo |
| 7 | `rest-graphql-debug` | Hermes nativo (optional-skills) |
| 8 | `agent-introspection-debugging` | ECC |
| 9 | `parallel-investigation` | Hermes (hipóteses concorrentes) |

### Review (3)
| # | Skill | Origem |
|---|---|---|
| 10 | `requesting-code-review` | Superpowers/Hermes |
| 11 | `receiving-code-review` | Superpowers |
| 12 | `github-code-review` | Hermes nativo |

### Planning técnico (4)
| # | Skill | Origem |
|---|---|---|
| 13 | `writing-plans` | Hermes nativo |
| 14 | `plan` | Hermes nativo |
| 15 | `spike` | Hermes nativo |
| 16 | `pre-mortem` | Hermes / Custom |

### Crítica e avaliação técnica (2)
| # | Skill | Origem |
|---|---|---|
| 17 | `critique-with-evidence` | Custom (modulada: critica + repassa) |
| 18 | `tool-evaluator` | Custom (modulada: dependência técnica) |

### Execução paralela (3)
| # | Skill | Origem |
|---|---|---|
| 19 | `subagent-driven-development` | Superpowers/Hermes |
| 20 | `using-git-worktrees` | Superpowers |
| 21 | `parallel-tasks` | Superpowers (USAR no JSON) |

### Git / Github (4)
| # | Skill | Origem |
|---|---|---|
| 22 | `github-pr-workflow` | Hermes nativo |
| 23 | `github-repo-management` | Hermes nativo |
| 24 | `finishing-a-development-branch` | Superpowers |
| 25 | `advanced-git-workflows` | Hermes (rebase, cherry-pick, bisect, reflog) |

### Arquitetura (1)
| # | Skill | Origem |
|---|---|---|
| 26 | `architecture-patterns` | wshobson/agents (Clean, Hexagonal, DDD) |

### CI/CD (1)
| # | Skill | Origem |
|---|---|---|
| 27 | `github-actions-templates` | wshobson/agents |

> 💡 **Lembrete CI ARM (2026-05-29)**: A VPS é ARM (Graviton). GitHub Actions oferece **runners ARM64** — quando você construir um projeto que justifique CI (testes/lint automáticos a cada PR), use `github-actions-templates` com runner ARM pra pegar incompatibilidade ARM-específica ANTES de chegar na VPS. Complementa a skill `arm64-compatibility-check` do Atlas (que valida na VPS). **Não é obrigatório no MVP** — aplique por-projeto quando fizer sentido (free tier GitHub Actions cobre repo privado pessoal).

### Onboarding (2)
| # | Skill | Origem |
|---|---|---|
| 28 | `codebase-inspection` | Hermes nativo (pygount) |
| 29 | `repomix` | externa (empacotar repo) |

### Lacunas Hermes preenchidas (3)
| # | Skill | Origem |
|---|---|---|
| 30 | `database-migrations` | ECC |
| 31 | `error-handling` | ECC |
| 32 | `api-design` | ECC |

### Security (3)
| # | Skill | Origem |
|---|---|---|
| 33 | `security-review` | ECC |
| 34 | `agent-architecture-audit` | ECC |
| 35 | `oss-forensics` | Hermes nativo (sob demanda) |

### Web QA (1)
| # | Skill | Origem |
|---|---|---|
| 36 | `dogfood` | Hermes nativo |

### Pesquisa técnica/cultura (3)
| # | Skill | Origem |
|---|---|---|
| 37 | `xurl` | Hermes nativo (X/Twitter, Hacker News) |
| 38 | `youtube-content` | Hermes nativo |
| 39 | `gif-search` | Hermes nativo (modulação leve) |

### Raw coding — aproximar Opus/GPT (7 — adicionadas 2026-05-19)
| # | Skill | Origem | Status |
|---|---|---|---|
| 40 | `python-typing` | Hermes (mypy strict, generics) | Bundled |
| 41 | `python-async-patterns` | Hermes (asyncio bem feito) | Bundled |
| 42 | `spec-kit` | GitHub Spec Kit (spec-driven dev) | externa |
| 43 | `typescript-advanced-types` | wshobson (lazy — ativa só se MVP tiver TS) | externa |
| 44 | `property-based-testing` | **A CRIAR** (Hypothesis + fast-check) | custom |
| 45 | `strict-type-checking` | **A CRIAR** (wrapper que força strict) | custom |
| 46 | `code-review-checklist` | **A CRIAR** (checklist anti-blind-spot) | custom |

### Fase C2 — adicionadas após análise crítica `hermes_codigo_research.md` (3 — 2026-05-22)
| # | Skill | Origem | Justificativa |
|---|---|---|---|
| 47 | `security-scan` | ECC | Audita config `.hermes/`, MCP servers, hooks, agent definitions. **DIFERENTE de `security-review`** (que audita código). Crítico pq Hermes VPS Stack é meta-sistema de agentes — config errada = vetor de ataque grande. Adaptar de `.claude/` pra `.hermes/`. |
| 48 | `codebase-onboarding` | ECC | Gera **guia estruturado** de repo desconhecido (architecture map, entry points, conventions, starter HERMES.md). **DIFERENTE de `codebase-inspection`** (só LOC) e `repomix` (só empacotamento). Adaptar saída pra `AGENTS.md`/`HERMES.md` em vez de `CLAUDE.md`. |
| 49 | `debugging-hermes-tui-commands` | Hermes nativo | Específico pra debugar slash commands Hermes (Python + gateway JSON-RPC + frontend Ink/TypeScript). Só ativar quando bug for em comando Hermes/TUI. Manutenção do próprio framework. |

---

## SKILLS BUNDLED OBRIGATÓRIAS DO HERMES (auto)

Estas vêm com o Hermes e são automaticamente carregadas quando o profile é worker do Kanban:

- `kanban-worker` — bundled, sync automático em todo profile
- `kanban-orchestrator` — bundled (Hefesto NÃO usa, mas vem instalado)

---

## SKILLS EXPLICITAMENTE REJEITADAS

| Skill | Motivo |
|---|---|
| `kanban-orchestrator` | Apollo orquestra; Hefesto executa (mesmo bundled, NÃO habilitar) |
| `humanizer` | Texto de código precisa precisão, não suavização |
| `llm-wiki` | Hefesto pergunta, não consulta KB |
| `honcho` (skill) | Cross-session memory é Apollo |
| `brainstorming` (Superpowers) | Apollo brainstorm intenção; Hefesto recebe escopo pronto |
| `feynman-check` | Apollo |
| `self-improvement-tracker` | Apollo |
| `briefing-sintetizador` | Apollo |
| `darwinian-evolver` | Apollo |
| `notion` | Apollo |
| `jupyter-live-kernel` | Apollo |
| `adversarial-ux-test` | Apollo |
| `one-three-one-rule` | Padrão de comunicação (herdado), não skill dedicada |
| `react-doctor` | Aurora |
| `hermes-agent-skill-authoring` | Não relevante (Hefesto não cria skills) |
| `literate-programming-skill` | Substituído por regra de entrega |
| `hermes-curator-evolver` | Conductor |
| `1password` | Miguel usa Maton |
| `sql-optimization` | Sob demanda, não justifica skill registrada agora |
| `api-documentation` | Coberto naturalmente por `api-design` |
| `python-performance` | Otimização prematura é overengineering |
| `docker-management` | MVP não confirmado se usa Docker |
| `fastmcp`, `mcporter` | Cobertos por `native-mcp` |
| `refactoring-patterns` | Implícito em `using-git-worktrees` + review |
| `database-schema-design` | Coberto por `database-migrations` |
| `changelog-maintenance` | Coberto pela regra de entrega |

---

## INSTRUÇÕES DE INSTALAÇÃO

Em S3a (Hefesto criação), executar nesta ordem:

### 1. Skills bundled (automáticas — verificar)
```bash
hermes -p hefesto skills list | grep -E "kanban-worker|test-driven|systematic-debugging"
```

### 2. Skills do hub
```bash
hermes -p hefesto skills install official/software-development/test-driven-development
hermes -p hefesto skills install official/software-development/systematic-debugging
hermes -p hefesto skills install official/software-development/python-debugpy
hermes -p hefesto skills install official/software-development/node-inspect-debugger
hermes -p hefesto skills install official/software-development/spike
hermes -p hefesto skills install official/software-development/requesting-code-review
hermes -p hefesto skills install official/software-development/writing-plans
hermes -p hefesto skills install official/software-development/plan
hermes -p hefesto skills install official/software-development/subagent-driven-development
hermes -p hefesto skills install official/github/codebase-inspection
hermes -p hefesto skills install official/github/github-code-review
hermes -p hefesto skills install official/github/github-pr-workflow
hermes -p hefesto skills install official/github/github-repo-management
hermes -p hefesto skills install official/security/oss-forensics
hermes -p hefesto skills install official/software-development/rest-graphql-debug
hermes -p hefesto skills install official/dogfood/dogfood
hermes -p hefesto skills install official/software-development/debugging-hermes-tui-commands   # C2
# ... continuar pra todas
```

### 3. Skills externas (ECC, Superpowers, wshobson)
Clonar repos e copiar via `hermes -p hefesto skills install --from-path <path>`:
- `affaan-m/everything-claude-code` → `python-testing`, `ai-regression-testing`, `agent-introspection-debugging`, `database-migrations`, `error-handling`, `api-design`, `security-review`, `agent-architecture-audit`, **`security-scan`** (C2), **`codebase-onboarding`** (C2)
- `obra/superpowers` → `receiving-code-review`, `using-git-worktrees`, `parallel-tasks`, `finishing-a-development-branch`
- `wshobson/agents` → `architecture-patterns`, `github-actions-templates`, `advanced-git-workflows`, `typescript-advanced-types`

### 3.5 Skills universais do Drive Ultra Prompt v6.2

```bash
SRC="$HOME/Desktop/Hermes_Project/05_ultra_prompt_v62_referencia/Ultra Prompt v6.2/skills/common"
DST="$HOME/.hermes/profiles/hefesto/skills"
mkdir -p $DST/critical-thinking $DST/human-in-the-loop
cp "$SRC/critical-thinking.md" $DST/critical-thinking/SKILL.md
cp "$SRC/human-in-the-loop.md" $DST/human-in-the-loop/SKILL.md
```

### 4. Skills custom (a CRIAR pelo Conductor)
- `property-based-testing` — Hypothesis (Python) + fast-check (TS)
- `strict-type-checking` — mypy strict + pyright + TS strict
- `code-review-checklist` — anti-blind-spot do modelo médio

### 5. Pin skills custom (anti auto-archive do Curator)
```bash
hermes -p hefesto curator pin property-based-testing
hermes -p hefesto curator pin strict-type-checking
hermes -p hefesto curator pin code-review-checklist
```

---

## VALIDAÇÃO PÓS-INSTALAÇÃO

```bash
hermes -p hefesto skills list                     # confere total
hermes -p hefesto doctor                          # health check
hermes -p hefesto chat -q "/tdd hello world"      # smoke test trigger
```

Esperado: 61 skills habilitadas, doctor OK, trigger responde com plan TDD.
