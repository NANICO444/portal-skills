# Aurora — Skills + Links de Download

**Total**: 17 universais + 22 específicas = **39 skills**
**Última atualização**: 2026-05-20

> Use este arquivo pra testar download manual das skills da Aurora.
> Cada linha: skill | origem | link/path | comando de instalação.

---

## 🧰 Skills universais (17 — todos os cérebros têm)

Maioria são **toolsets built-in do Hermes** (não são SKILL.md separados) + algumas skills bundled/optional.

| # | Skill | Origem | Link / Path | Como obter |
|---|---|---|---|---|
| 1 | `tavily-search` | Hermes built-in toolset | (sem SKILL.md — é tool no Hermes) | Configurar `TAVILY_API_KEY` no `.env` |
| 2 | `web-fetch` | Hermes built-in toolset | (sem SKILL.md — é tool no Hermes) | Built-in toolset `web` |
| 3 | `web-scrape` | Hermes built-in toolset | (sem SKILL.md — parte de `web_extract`) | Built-in toolset `web` |
| 4 | `doc-cache` | Hermes built-in | (sem SKILL.md) | Cache de docs nativo |
| 5 | `doc-read` | Hermes built-in toolset | (sem SKILL.md — é `read_file`) | Built-in toolset `file` |
| 6 | `ocr` | Hermes-native | https://github.com/NousResearch/hermes-agent/blob/main/skills/productivity/ocr-and-documents/SKILL.md | Bundled (nome real: `ocr-and-documents`) |
| 7 | `maton-gateway` | Hermes-native | https://github.com/NousResearch/hermes-agent/blob/main/skills/integration/api-gateway/SKILL.md | Bundled (nome real: `api-gateway`) — exige `MATON_API_KEY` |
| 8 | `factual-verify` | Built-in behavior | (parte de `verification-before-completion`) | Universal Hermes |
| 9 | `verification-before-completion` | Superpowers | https://github.com/obra/superpowers/blob/main/skills/verification-before-completion/SKILL.md | Clonar superpowers ou copiar skill |
| 10 | `anti-glaze` | Custom-to-create | (sem repo) | A criar — base em post analisado |
| 11 | `karpathy-discipline` | Custom (base externa) | https://github.com/multica-ai/andrej-karpathy-skills | Adaptar `karpathy-guidelines` |
| 12 | `find-skills` | Vercel skills | https://github.com/vercel-labs/skills/tree/main/skills/find-skills | `npx skills add vercel-labs/skills@find-skills` |
| 13 | `token-budget-advisor` | Built-in concept | (sem SKILL.md externa — Hermes tem `context-budget` no ECC) | Universal Hermes + ECC fallback |
| 14 | `council` | ECC | https://github.com/affaan-m/everything-claude-code/blob/main/skills/council/SKILL.md | Copiar `skills/council/SKILL.md` |
| 15 | `documentation-lookup` | ECC | https://github.com/affaan-m/everything-claude-code/blob/main/skills/documentation-lookup/SKILL.md | Copiar `skills/documentation-lookup/SKILL.md` |
| 16 | `duckduckgo-search` | Hermes-optional | https://github.com/NousResearch/hermes-agent/blob/main/optional-skills/research/duckduckgo-search/SKILL.md | `hermes skills install official/research/duckduckgo-search` |
| 17 | `native-mcp` | Hermes-native | https://github.com/NousResearch/hermes-agent/blob/main/skills/mcp/native-mcp/SKILL.md | Bundled |

### Universais novos (adicionados após análise Eficaz)
| # | Skill | Origem | Link / Path | Como obter |
|---|---|---|---|---|
| 18 | `critical-thinking` | Drive Ultra Prompt v6.2 | `C:\Users\MASTER-CHIEF\Desktop\Hermes_Project\05_ultra_prompt_v62_referencia\Ultra Prompt v6.2\skills\common\critical-thinking.md` | Copiar arquivo local |
| 19 | `human-in-the-loop` | Drive Ultra Prompt v6.2 | `C:\Users\MASTER-CHIEF\Desktop\Hermes_Project\05_ultra_prompt_v62_referencia\Ultra Prompt v6.2\skills\common\human-in-the-loop.md` | Copiar arquivo local |

---

## 🎨 Skills específicas Aurora (22)

### Tier S — Núcleo de design (5)

| # | Skill | Origem | Link / Path | Como obter |
|---|---|---|---|---|
| 1 | `impeccable` | pbakaus/impeccable (original) | https://github.com/pbakaus/impeccable | Clonar repo, copiar `skill/` ou os 23 comandos individualmente |
| 2 | `palette` | Drive Ultra Prompt v6.2 | `C:\Users\MASTER-CHIEF\Desktop\Hermes_Project\05_ultra_prompt_v62_referencia\Ultra Prompt v6.2\skills\site\palette.md` | Copiar arquivo local |
| 3 | `component-library` | Drive Ultra Prompt v6.2 | `C:\Users\MASTER-CHIEF\Desktop\Hermes_Project\05_ultra_prompt_v62_referencia\Ultra Prompt v6.2\skills\site\component-library.md` | Copiar arquivo local |
| 4 | `content-generation` | Drive Ultra Prompt v6.2 | `C:\Users\MASTER-CHIEF\Desktop\Hermes_Project\05_ultra_prompt_v62_referencia\Ultra Prompt v6.2\skills\site\content.md` | Copiar arquivo local |
| 5 | `accessibility-audit` | Drive Ultra Prompt v6.2 | `C:\Users\MASTER-CHIEF\Desktop\Hermes_Project\05_ultra_prompt_v62_referencia\Ultra Prompt v6.2\skills\site\accessibility-audit.md` | Copiar arquivo local |

### Tier A — Site essencial (5)

| # | Skill | Origem | Link / Path | Como obter |
|---|---|---|---|---|
| 6 | `frontend-stack-decision` | Drive Ultra Prompt v6.2 | `C:\Users\MASTER-CHIEF\Desktop\Hermes_Project\05_ultra_prompt_v62_referencia\Ultra Prompt v6.2\skills\site\frontend.md` | Copiar arquivo local |
| 7 | `performance-web-vitals` | Drive Ultra Prompt v6.2 | `C:\Users\MASTER-CHIEF\Desktop\Hermes_Project\05_ultra_prompt_v62_referencia\Ultra Prompt v6.2\skills\site\performance.md` | Copiar arquivo local |
| 8 | `browser-testing` | Drive Ultra Prompt v6.2 | `C:\Users\MASTER-CHIEF\Desktop\Hermes_Project\05_ultra_prompt_v62_referencia\Ultra Prompt v6.2\skills\site\testing.md` | Copiar arquivo local |
| 9 | `design-md` | Hermes-native | https://github.com/NousResearch/hermes-agent/blob/main/skills/creative/design-md/SKILL.md | Bundled |
| 10 | `design-brief` | Open Design (Nexu) | https://github.com/nexu-io/open-design/blob/main/plugins/_official/examples/design-brief/SKILL.md | Copiar do repo Open Design |

### Tier B — Publicação/integração (4)

| # | Skill | Origem | Link / Path | Como obter |
|---|---|---|---|---|
| 11 | `seo-advanced` | Drive Ultra Prompt v6.2 | `C:\Users\MASTER-CHIEF\Desktop\Hermes_Project\05_ultra_prompt_v62_referencia\Ultra Prompt v6.2\skills\site\seo-advanced.md` | Copiar arquivo local |
| 12 | `api-integration` | Drive Ultra Prompt v6.2 | `C:\Users\MASTER-CHIEF\Desktop\Hermes_Project\05_ultra_prompt_v62_referencia\Ultra Prompt v6.2\skills\site\api-integration.md` | Copiar arquivo local |
| 13 | `deploy-protocol` | Drive Ultra Prompt v6.2 | `C:\Users\MASTER-CHIEF\Desktop\Hermes_Project\05_ultra_prompt_v62_referencia\Ultra Prompt v6.2\skills\site\deploy.md` | Copiar arquivo local |
| 14 | `error-recovery-design` | Drive Ultra Prompt v6.2 | `C:\Users\MASTER-CHIEF\Desktop\Hermes_Project\05_ultra_prompt_v62_referencia\Ultra Prompt v6.2\skills\site\recovery.md` | Copiar arquivo local |

### Tier C — Inspiração/biblioteca (4)

| # | Skill | Origem | Link / Path | Como obter |
|---|---|---|---|---|
| 15 | `html-anything` | Joehott/html-anything (app, não skill) | https://github.com/Joehott/html-anything | Clonar repo — usar 75 templates como referência (não SKILL.md) |
| 16 | `popular-web-designs` | Hermes-native | https://github.com/NousResearch/hermes-agent/blob/main/skills/creative/popular-web-designs/SKILL.md | Bundled |
| 17 | `design-extract` | Open Design (Nexu) | https://github.com/nexu-io/open-design/blob/main/plugins/_official/atoms/design-extract/SKILL.md | Copiar do repo Open Design |
| 18 | `baoyu-infographic` | Hermes-native | https://github.com/NousResearch/hermes-agent/blob/main/skills/creative/baoyu-infographic/SKILL.md | Bundled |

### Tier D — Frontend dev específico (3)

| # | Skill | Origem | Link / Path | Como obter |
|---|---|---|---|---|
| 19 | `frontend-patterns` | ECC | https://github.com/affaan-m/everything-claude-code/blob/main/skills/frontend-patterns/SKILL.md | Copiar `skills/frontend-patterns/SKILL.md` |
| 20 | `react-doctor` | CLI externa (não skill) | https://github.com/aidenbai/react-doctor | `npx -y react-doctor@latest .` — invocar via terminal |
| 21 | `motion-foundations + motion-patterns` | ECC | https://github.com/affaan-m/everything-claude-code/blob/main/skills/motion-foundations/SKILL.md + https://github.com/affaan-m/everything-claude-code/blob/main/skills/motion-patterns/SKILL.md | Copiar ambas |

### Tier E — Suplementos (2)

| # | Skill | Origem | Link / Path | Como obter |
|---|---|---|---|---|
| 22 | `excalidraw` | Hermes-native | https://github.com/NousResearch/hermes-agent/blob/main/skills/creative/excalidraw/SKILL.md | Bundled |
| 23 | `make-interfaces-feel-better` | ECC | https://github.com/affaan-m/everything-claude-code/blob/main/skills/make-interfaces-feel-better/SKILL.md | Copiar |

---

## 🎭 Personas Aurora (10 — modulações de tom)

**NÃO são skills** — são modulações de personalidade. Mas têm origem externa:

| Persona | Origem | Link / Path |
|---|---|---|
| UI Designer (default) | Joehott/agency-agents | `C:\Users\MASTER-CHIEF\Desktop\RELATORIO_AGENT_IA_EFICAZ_2026-05-19\repos_github\agency-agents\design\design-ui-designer.md` |
| UX Architect (default) | Joehott/agency-agents | `C:\Users\MASTER-CHIEF\Desktop\RELATORIO_AGENT_IA_EFICAZ_2026-05-19\repos_github\agency-agents\design\design-ux-architect.md` |
| Brand Guardian (sob demanda) | Joehott/agency-agents | `C:\Users\MASTER-CHIEF\Desktop\RELATORIO_AGENT_IA_EFICAZ_2026-05-19\repos_github\agency-agents\design\` |
| Visual Storyteller (sob demanda) | Joehott/agency-agents | (mesma pasta) |
| Content Creator (sob demanda) | Joehott/agency-agents | `C:\Users\MASTER-CHIEF\Desktop\RELATORIO_AGENT_IA_EFICAZ_2026-05-19\repos_github\agency-agents\marketing\` |
| SEO Specialist (sob demanda) | Joehott/agency-agents | (marketing) |
| Paid Media Creative Strategist | Joehott/agency-agents | `C:\Users\MASTER-CHIEF\Desktop\RELATORIO_AGENT_IA_EFICAZ_2026-05-19\repos_github\agency-agents\paid-media\` |
| Accessibility Auditor (reviewer) | Joehott/agency-agents | `C:\Users\MASTER-CHIEF\Desktop\RELATORIO_AGENT_IA_EFICAZ_2026-05-19\repos_github\agency-agents\testing\` |
| Performance Benchmarker (reviewer) | Joehott/agency-agents | (testing) |
| Reality Checker (reviewer) | Joehott/agency-agents | (testing) |

Repo no GitHub: https://github.com/Joehott/agency-agents

---

## 📚 Referências externas Aurora (8 URLs + Eficaz)

Não são skills — são leituras de referência que vão pro `playbook.md`:

| Referência | URL |
|---|---|
| Smartmentors UI principles | https://www.smartmentors.net/ui-design-principles-color-theory-typography-layouts/ |
| Netboost typography+color | https://netboost.ie/blog/webdesign/typography-and-color-theory-in-web-design/ |
| Imagely brand color | https://www.imagely.com/brand-color-matters/ |
| Jasmine Directory color psychology 2026 | https://www.jasminedirectory.com/blog/the-psychology-of-color-in-2026-digital-advertising/ |
| Pixelstorm psychology web design | https://pixelstorm.com.au/news/psychology-web-design-colors-fonts-layouts/ |
| IxDF Gestalt principles | https://ixdf.org/literature/topics/gestalt-principles |
| Ashlyn Writes AI copywriter prompts | https://ashlynwrites.com/the-ai-copywriters-toolkit-5-go-to-chatgpt-prompts-for-supercharged-copywriting/ |
| Berkeley CMR Prompt imperative advertising | https://cmr.berkeley.edu/2025/11/the-prompt-imperative-how-generative-ai-is-rewriting-the-rules-of-advertising/ |
| **Eficaz Controle de Pragas (caso de uso real)** | `C:\Users\MASTER-CHIEF\Desktop\RELATORIO_AGENT_IA_EFICAZ_2026-05-19\RELATORIO_ULTRA_DETALHADO_AGENTE_IA.md` |

---

## 🛠️ Comandos rápidos pra testar

### Clonar repos principais (de uma vez)
```bash
mkdir -p ~/Desktop/aurora_skills_test
cd ~/Desktop/aurora_skills_test

git clone --depth=1 https://github.com/pbakaus/impeccable.git
git clone --depth=1 https://github.com/Joehott/html-anything.git
git clone --depth=1 https://github.com/Joehott/agency-agents.git
git clone --depth=1 https://github.com/nexu-io/open-design.git
git clone --depth=1 https://github.com/affaan-m/everything-claude-code.git
git clone --depth=1 https://github.com/NousResearch/hermes-agent.git
```

### Filtrar só o que Aurora usa

Após clonar, copiar pasta-a-pasta:
```bash
# Impeccable (Tier S #1)
cp -r impeccable/skill/ ~/Desktop/aurora_skills_test/_aurora_final/impeccable/

# Open Design (Tier S #6 + #10 + Tier C #17)
cp -r open-design/plugins/_official/examples/design-brief/ ~/Desktop/aurora_skills_test/_aurora_final/
cp -r open-design/plugins/_official/atoms/design-extract/ ~/Desktop/aurora_skills_test/_aurora_final/

# ECC (Tier S #14 + #15 + outros)
cp -r everything-claude-code/skills/council/ ~/Desktop/aurora_skills_test/_aurora_final/
cp -r everything-claude-code/skills/documentation-lookup/ ~/Desktop/aurora_skills_test/_aurora_final/
cp -r everything-claude-code/skills/frontend-patterns/ ~/Desktop/aurora_skills_test/_aurora_final/
cp -r everything-claude-code/skills/motion-foundations/ ~/Desktop/aurora_skills_test/_aurora_final/
cp -r everything-claude-code/skills/motion-patterns/ ~/Desktop/aurora_skills_test/_aurora_final/
cp -r everything-claude-code/skills/make-interfaces-feel-better/ ~/Desktop/aurora_skills_test/_aurora_final/

# Hermes-native (bundled — só copiar SKILL.md como referência)
cp hermes-agent/skills/creative/design-md/SKILL.md ~/Desktop/aurora_skills_test/_aurora_final/design-md_ref.md
cp hermes-agent/skills/creative/popular-web-designs/SKILL.md ~/Desktop/aurora_skills_test/_aurora_final/popular-web-designs_ref.md
cp hermes-agent/skills/creative/excalidraw/SKILL.md ~/Desktop/aurora_skills_test/_aurora_final/excalidraw_ref.md
cp hermes-agent/skills/creative/baoyu-infographic/SKILL.md ~/Desktop/aurora_skills_test/_aurora_final/baoyu-infographic_ref.md

# Drive Ultra Prompt v6.2 (Tier S #2-#5 + Tier A #6-#8 + Tier B #11-#14)
SRC="$HOME/Desktop/Hermes_Project/05_ultra_prompt_v62_referencia/Ultra Prompt v6.2/skills/site"
DST="$HOME/Desktop/aurora_skills_test/_aurora_final/drive_skills"
mkdir -p $DST
cp "$SRC/palette.md" $DST/
cp "$SRC/component-library.md" $DST/
cp "$SRC/content.md" $DST/
cp "$SRC/accessibility-audit.md" $DST/
cp "$SRC/frontend.md" $DST/
cp "$SRC/performance.md" $DST/
cp "$SRC/testing.md" $DST/
cp "$SRC/seo-advanced.md" $DST/
cp "$SRC/api-integration.md" $DST/
cp "$SRC/deploy.md" $DST/
cp "$SRC/recovery.md" $DST/
```

### Verificar contagem após copiar
```bash
find ~/Desktop/aurora_skills_test/_aurora_final/ -name "*.md" | wc -l
# Esperado: ~20-25 arquivos
```

---

## ⚠️ Skills marcadas Custom-to-create

Estas **não existem prontas** — vamos criar do zero. Sem link de download:

1. **`anti-glaze`** (universal) — base em post analisado
2. **`critique-with-evidence`** (Apollo custom) — anti-glaze full + scoring
3. **`feynman-check`** (Apollo custom)
4. **`tool-evaluator`** (Apollo custom)
5. **`self-improvement-tracker`** (Apollo custom)
6. **`adversarial-ux-test`** (Apollo custom)
7. **`briefing-sintetizador`** (Apollo custom)
8. **`github-repo-eval`** (Apollo custom)
9. **`context-snapshot`** (Apollo custom)

Aurora **não tem skills custom-to-create próprias** — todas dela têm origem confirmada.

---

**Caminho deste arquivo**: `profiles/aurora/skills_download_links.md`
