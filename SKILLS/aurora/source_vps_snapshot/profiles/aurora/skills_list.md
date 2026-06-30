# Aurora — Skills List

**Total**: 17 universais + 22 específicas = **39 skills**
**Última atualização**: 2026-05-21

> Comandos de instalação são padrão Hermes:
> - Bundled (já vem): nada a fazer, só habilitar via `hermes -p aurora skills enable <skill>`
> - Hub: `hermes -p aurora skills install official/<category>/<skill>`
> - Externa: copiar `SKILL.md` do repo origem
> - Custom: escrita manual em `~/.hermes/profiles/aurora/skills/<skill>/SKILL.md`
>
> Links completos de download em `skills_download_links.md`.

---

## SKILLS UNIVERSAIS (17 — todos os cérebros têm)

Mesmas do Apollo/Hefesto/Midas, com modulações Aurora:

| # | Skill | Tipo | Modulação Aurora |
|---|---|---|---|
| 1 | `tavily-search` | Hermes built-in toolset | 1 key |
| 2 | `web-fetch` | Hermes built-in toolset | — |
| 3 | `web-scrape` | Hermes built-in toolset | — |
| 4 | `doc-cache` | Hermes built-in | — |
| 5 | `doc-read` | Hermes built-in toolset | — |
| 6 | `ocr` | Hermes-native | — |
| 7 | `maton-gateway` | Hermes-native | **CRÍTICO** — GitHub/Vercel/Drive/Notion via Maton |
| 8 | `factual-verify` | Built-in behavior | — |
| 9 | `verification-before-completion` | Superpowers | Aplicado em build + a11y + visual diff |
| 10 | `anti-glaze` | Custom-to-create | **Forte** — cita Impeccable quando rejeita |
| 11 | `karpathy-discipline` | Custom (base externa) | **"Criativo"** — liberdade com função |
| 12 | `find-skills` | Vercel skills | Busca + recomenda. NÃO instala |
| 13 | `token-budget-advisor` | Built-in concept | — |
| 14 | `council` | ECC | Sob demanda (decisão visual ambígua) |
| 15 | `documentation-lookup` | ECC | — |
| 16 | `duckduckgo-search` | Hermes-optional | Fallback |
| 17 | `native-mcp` | Hermes-native | — |

### Universais adicionados (Drive Ultra Prompt v6.2)

| # | Skill | Tipo | Modulação |
|---|---|---|---|
| 18 | `critical-thinking` | Drive | Universal — todos cérebros |
| 19 | `human-in-the-loop` | Drive | Universal — todos cérebros |

> Implica adicionar 18 + 19 ao Apollo + Hefesto + Midas também.

---

## SKILLS ESPECÍFICAS AURORA (22)

### Tier S — Núcleo de design (5)

| # | Skill | Origem |
|---|---|---|
| 1 | **`impeccable`** | repo `pbakaus/impeccable` (23 comandos: craft/shape/critique/audit/polish/typeset/layout/colorize/animate/harden/etc) |
| 2 | **`palette`** | Drive Ultra Prompt v6.2 — design contract (paleta+tipo+contraste+dark) |
| 3 | **`component-library`** | Drive Ultra Prompt v6.2 — Tier 1/2/3 componentes |
| 4 | **`content-generation`** | Drive Ultra Prompt v6.2 — copy contextual por seção |
| 5 | **`accessibility-audit`** | Drive Ultra Prompt v6.2 — WCAG + remediação |

### Tier A — Site essencial (5)

| # | Skill | Origem |
|---|---|---|
| 6 | **`frontend-stack-decision`** | Drive Ultra Prompt v6.2 |
| 7 | **`performance-web-vitals`** | Drive Ultra Prompt v6.2 — Core Web Vitals |
| 8 | **`browser-testing`** | Drive Ultra Prompt v6.2 — protocolo gate pré-entrega |
| 9 | **`design-md`** | Hermes nativo — tokens persistentes |
| 10 | **`design-brief`** | adaptar Open Design (Nexu) — bloqueia criação sem brief |

### Tier B — Publicação/integração (4)

| # | Skill | Origem |
|---|---|---|
| 11 | **`seo-advanced`** | Drive Ultra Prompt v6.2 |
| 12 | **`api-integration`** | Drive Ultra Prompt v6.2 — forms/Stripe/CMS/Maton |
| 13 | **`deploy-protocol`** | Drive Ultra Prompt v6.2 — Vercel/Netlify staging-only |
| 14 | **`error-recovery-design`** | Drive Ultra Prompt v6.2 — DT-01 a DT-06 |

> 💡 **Lembrete staging + CI ARM (2026-05-29)**: Staging = **Vercel** (padrão MVP — casa do Next.js + Maton pronto), Cloudflare Pages como alternativa se bater bandwidth. STAGING ONLY (D47 — você nunca publica produção). E se construir projeto que justifique CI: GitHub Actions tem **runner ARM64** — útil pra testar frontend em ARM antes da VPS Graviton. **Não obrigatório no MVP** — aplique por-projeto. Free tier cobre.

### Tier C — Inspiração/biblioteca (4)

| # | Skill | Origem |
|---|---|---|
| 15 | **`html-anything`** | repo `Joehott/html-anything` — biblioteca 75 templates de superfícies |
| 16 | **`popular-web-designs`** | Hermes nativo — 54 design systems referência (Stripe/Linear/Vercel) |
| 17 | **`design-extract`** | Open Design (Nexu) — extrair tokens de screenshot/Figma/código |
| 18 | **`baoyu-infographic`** | Hermes nativo — 21 layouts × 21 estilos infográfico |

### Tier D — Frontend dev específico (3)

| # | Skill | Origem |
|---|---|---|
| 19 | **`frontend-patterns`** | ECC — React/Next patterns, state, forms |
| 20 | **`react-doctor`** | CLI externa `aidenbai/react-doctor` — debug React |
| 21 | **`motion-foundations + motion-patterns`** | ECC — motion com propósito + reduce-motion |

### Tier E — Suplementos (2)

| # | Skill | Origem |
|---|---|---|
| 22 | **`excalidraw`** | Hermes nativo — wireframes early-stage |
| 23 | **`make-interfaces-feel-better`** | ECC — polimento última milha |

---

## SKILLS BUNDLED OBRIGATÓRIAS (auto)

- `kanban-worker` — bundled, sync automático (todos cérebros)
- `kanban-orchestrator` — bundled (Aurora NÃO usa — Apollo orquestra)

---

## SKILLS EXPLICITAMENTE REJEITADAS

| Skill | Motivo |
|---|---|
| `kanban-orchestrator` | Apollo orquestra; Aurora executa cards recebidos |
| `humanizer` | Aurora não escreve em prosa (Content Creator persona faz se necessário) |
| `llm-wiki` | Apollo escreve, Aurora só lê quando necessário |
| `honcho` (skill) | Cross-session memory é Apollo |
| `brainstorming` (Superpowers) | Apollo brainstorm estratégico; Aurora recebe brief pronto |
| `feynman-check` | Apollo |
| `self-improvement-tracker` | Apollo |
| `briefing-sintetizador` | Apollo |
| `darwinian-evolver` | Apollo |
| `notion` (skill genérica) | Aurora usa Notion via Maton, não skill genérica |
| `jupyter-live-kernel` | Apollo (Aurora não faz análise de dados) |
| `adversarial-ux-test` | Apollo |
| `one-three-one-rule` | Padrão de comunicação herdado, não skill dedicada |
| `test-driven-development`, `systematic-debugging`, `python-debugpy`, `node-inspect-debugger`, `rest-graphql-debug` | Hefesto (Aurora não faz backend nem debug profundo) |
| `requesting-code-review`, `github-code-review`, `github-pr-workflow`, `github-repo-management` | Hefesto (Aurora segue padrão simplificado de PR via Opção C híbrida) |
| `database-migrations`, `error-handling`, `api-design` | Hefesto |
| `security-review`, `agent-architecture-audit`, `oss-forensics` | Hefesto |
| `architecture-patterns`, `github-actions-templates`, `advanced-git-workflows` | Hefesto |
| `python-typing`, `python-async-patterns`, `spec-kit`, `property-based-testing`, `strict-type-checking`, `code-review-checklist` | Hefesto (Aurora frontend simples — não precisa rigor backend) |
| `1password` | Miguel usa Maton |
| `direction-picker` (Open Design) | Coberto por `shape` do Impeccable + Visual Storyteller |
| `tweaks` (Open Design) | Coberto por Impeccable + iteração natural |
| `token-map` (Open Design) | `palette` já normaliza |
| `critique` (Open Design) | Impeccable `critique` cobre |
| `dashboard-builder` (ECC) | HTML Anything tem `dashboard` template |
| `frontend-slides` (ECC) | HTML Anything tem `deck-*` templates |
| `design-system` (ECC) | Substituído por `component-library` |
| `frontend-design-direction` (ECC) | `frontend-stack-decision` + Visual Storyteller modulação |
| `concept-diagrams` (Hermes) | Coberto por `excalidraw` + `baoyu-infographic` |
| `gif-search` (universal Apollo) | Não é tom da Aurora |
| `nv-clip` | Cortado — sem NVIDIA build no MVP |

---

## SKILLS CUSTOM-TO-CREATE (universais — não específicas Aurora)

Estas vão ser criadas em S3a pelo Conductor (não existem prontas):

1. **`anti-glaze`** (universal) — base em post analisado, sem repo
2. **`karpathy-discipline`** (universal) — adaptar de `multica-ai/andrej-karpathy-skills`

> Aurora não tem skills custom-to-create PRÓPRIAS dela — todas têm origem confirmada.

---

## INSTRUÇÕES DE INSTALAÇÃO

Em S3a (Aurora criação), executar nesta ordem:

### 1. Skills bundled (automáticas — verificar)
```bash
hermes -p aurora skills list | grep -E "kanban-worker|design-md|popular-web-designs|excalidraw|baoyu-infographic"
```

### 2. Skills do hub Hermes
```bash
hermes -p aurora skills install official/creative/design-md
hermes -p aurora skills install official/creative/popular-web-designs
hermes -p aurora skills install official/creative/excalidraw
hermes -p aurora skills install official/creative/baoyu-infographic
hermes -p aurora skills install official/research/duckduckgo-search
hermes -p aurora skills install official/integration/api-gateway        # Maton
# ... outros conforme universais
```

### 3. Skills externas (clonar repos e copiar)

```bash
# Setup
mkdir -p ~/aurora_skills_install
cd ~/aurora_skills_install

# Repos
git clone --depth=1 https://github.com/pbakaus/impeccable.git
git clone --depth=1 https://github.com/Joehott/html-anything.git
git clone --depth=1 https://github.com/nexu-io/open-design.git
git clone --depth=1 https://github.com/affaan-m/everything-claude-code.git
git clone --depth=1 https://github.com/obra/superpowers.git
git clone --depth=1 https://github.com/Joehott/agency-agents.git  # personas

# Tier S (impeccable + open design)
hermes -p aurora skills install --from-path impeccable/skill/
hermes -p aurora skills install --from-path open-design/plugins/_official/examples/design-brief/

# Tier C (open design extract)
hermes -p aurora skills install --from-path open-design/plugins/_official/atoms/design-extract/

# Tier D (ECC)
hermes -p aurora skills install --from-path everything-claude-code/skills/frontend-patterns/
hermes -p aurora skills install --from-path everything-claude-code/skills/motion-foundations/
hermes -p aurora skills install --from-path everything-claude-code/skills/motion-patterns/
hermes -p aurora skills install --from-path everything-claude-code/skills/make-interfaces-feel-better/

# Universais — ECC
hermes -p aurora skills install --from-path everything-claude-code/skills/council/
hermes -p aurora skills install --from-path everything-claude-code/skills/documentation-lookup/

# Universais — Superpowers
hermes -p aurora skills install --from-path superpowers/skills/verification-before-completion/

# Universais — Vercel
npx skills add vercel-labs/skills@find-skills
```

### 4. Skills do Drive Ultra Prompt v6.2 (locais)

```bash
SRC="$HOME/Desktop/Hermes_Project/05_ultra_prompt_v62_referencia/Ultra Prompt v6.2/skills"
DST="$HOME/.hermes/profiles/aurora/skills"
mkdir -p $DST

# Tier S
cp -r "$SRC/site/palette.md" $DST/palette/SKILL.md
cp -r "$SRC/site/component-library.md" $DST/component-library/SKILL.md
cp -r "$SRC/site/content.md" $DST/content-generation/SKILL.md
cp -r "$SRC/site/accessibility-audit.md" $DST/accessibility-audit/SKILL.md

# Tier A
cp -r "$SRC/site/frontend.md" $DST/frontend-stack-decision/SKILL.md
cp -r "$SRC/site/performance.md" $DST/performance-web-vitals/SKILL.md
cp -r "$SRC/site/testing.md" $DST/browser-testing/SKILL.md

# Tier B
cp -r "$SRC/site/seo-advanced.md" $DST/seo-advanced/SKILL.md
cp -r "$SRC/site/api-integration.md" $DST/api-integration/SKILL.md
cp -r "$SRC/site/deploy.md" $DST/deploy-protocol/SKILL.md
cp -r "$SRC/site/recovery.md" $DST/error-recovery-design/SKILL.md

# Universais
cp -r "$SRC/common/critical-thinking.md" $DST/critical-thinking/SKILL.md
cp -r "$SRC/common/human-in-the-loop.md" $DST/human-in-the-loop/SKILL.md
```

### 5. CLIs externas (NÃO são skills — instalar via npm)

```bash
# Repomix (compartilhado com Hefesto)
npm install -g repomix

# React Doctor (executado on-demand)
# Aurora invoca via terminal: npx -y react-doctor@latest .
```

### 6. Personas (Aurora-específico — copiar do repo agency-agents)

```bash
PERSONAS_SRC="$HOME/aurora_skills_install/agency-agents"
PERSONAS_DST="$HOME/.hermes/profiles/aurora/personas"
mkdir -p $PERSONAS_DST

# 2 default (referenciadas no SOUL)
cp $PERSONAS_SRC/design/ui-designer.md $PERSONAS_DST/_ui-designer-source.md
cp $PERSONAS_SRC/design/ux-architect.md $PERSONAS_DST/_ux-architect-source.md

# 8 sob demanda
cp $PERSONAS_SRC/design/brand-guardian.md $PERSONAS_DST/_brand-guardian-source.md
cp $PERSONAS_SRC/marketing/content-creator.md $PERSONAS_DST/_content-creator-source.md
cp $PERSONAS_SRC/marketing/seo-specialist.md $PERSONAS_DST/_seo-specialist-source.md
cp $PERSONAS_SRC/design/visual-storyteller.md $PERSONAS_DST/_visual-storyteller-source.md
cp $PERSONAS_SRC/paid-media/paid-media-creative-strategist.md $PERSONAS_DST/_paid-media-source.md
cp $PERSONAS_SRC/testing/accessibility-auditor.md $PERSONAS_DST/_accessibility-auditor-source.md
cp $PERSONAS_SRC/testing/performance-benchmarker.md $PERSONAS_DST/_performance-benchmarker-source.md
cp $PERSONAS_SRC/testing/reality-checker.md $PERSONAS_DST/_reality-checker-source.md

# Próximo passo: adaptar source → arquivo final (já tem esqueleto na pasta personas/)
```

### 7. Customs a criar (em S3a)

Apenas universais — Aurora não tem custom própria:

- `anti-glaze` (universal)
- `karpathy-discipline` (universal — adaptação de `multica-ai/andrej-karpathy-skills`)

Conductor cria, Aurora habilita.

### 8. Pin skills customizadas (anti auto-archive Curator)

```bash
hermes -p aurora curator pin palette
hermes -p aurora curator pin component-library
hermes -p aurora curator pin content-generation
hermes -p aurora curator pin accessibility-audit
hermes -p aurora curator pin frontend-stack-decision
hermes -p aurora curator pin performance-web-vitals
hermes -p aurora curator pin browser-testing
hermes -p aurora curator pin seo-advanced
hermes -p aurora curator pin api-integration
hermes -p aurora curator pin deploy-protocol
hermes -p aurora curator pin error-recovery-design
hermes -p aurora curator pin critical-thinking
hermes -p aurora curator pin human-in-the-loop
hermes -p aurora curator pin impeccable
```

---

## VALIDAÇÃO PÓS-INSTALAÇÃO

```bash
hermes -p aurora skills list                          # confere 39 skills
hermes -p aurora doctor                               # health check
hermes -p aurora chat -q "/brief-design teste"        # smoke test trigger
```

**Esperado**:
- 39 skills habilitadas
- doctor OK
- Trigger responde pedindo brief

---

## VALIDAÇÃO DAS CONEXÕES MATON (PRÉ-S3A)

Antes de S3a, confirmar que Maton tem essas conexões ATIVAS:

```bash
# Listar conexões do usuário Aurora (Conta Executores)
curl https://ctrl.maton.ai/connections?status=ACTIVE -H "Authorization: Bearer $MATON_API_KEY"
```

Conexões necessárias:
- `google-drive` (entregas finais)
- `github` (repos privados)
- `vercel` (deploy staging)
- `notion` (documentação visual)

Opcionais:
- `netlify` (alternativa Vercel)
- `cloudflare-pages` (alternativa Vercel)

Se faltar alguma → criar via Maton dashboard antes de Aurora rodar.
