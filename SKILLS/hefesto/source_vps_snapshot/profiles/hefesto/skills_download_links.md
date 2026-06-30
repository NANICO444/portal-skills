# Hefesto — Skills + Links de Download

**Total**: 19 universais + 39 específicas = **58 skills** (vai pra 61 após Fase C2)
**Última atualização**: 2026-05-22

> Use este arquivo pra testar download manual das skills do Hefesto.
> Cada linha: skill | origem | link/path | comando de instalação.

---

## 🧰 Skills universais (19 — todos os cérebros têm)

Idênticas ao Apollo. Ver `profiles/apollo/skills_download_links.md` pra links.

Resumo:
- Hermes built-in toolsets: `tavily-search`, `web-fetch`, `web-scrape`, `doc-cache`, `doc-read` (5)
- Hermes-native: `ocr`, `maton-gateway`, `native-mcp` (3)
- Hermes-optional: `duckduckgo-search` (1)
- Built-in behavior: `factual-verify` (1)
- Superpowers: `verification-before-completion` (1)
- Custom-to-create (universais): `anti-glaze`, `karpathy-discipline`, `token-budget-advisor` (3)
- Vercel skills: `find-skills` (1)
- ECC: `council`, `documentation-lookup` (2)
- Drive Ultra Prompt v6.2: `critical-thinking`, `human-in-the-loop` (2)

---

## 🔨 Skills específicas Hefesto (39 → 42 após C2)

### TDD / Testing (3)

| # | Skill | Origem | Link / Path |
|---|---|---|---|
| 1 | `test-driven-development` | Hermes nativo | https://github.com/NousResearch/hermes-agent/blob/main/skills/software-development/test-driven-development/SKILL.md |
| 2 | `python-testing` | ECC | https://github.com/affaan-m/everything-claude-code/blob/main/skills/python-testing/SKILL.md |
| 3 | `ai-regression-testing` | ECC | https://github.com/affaan-m/everything-claude-code/blob/main/skills/ai-regression-testing/SKILL.md |

### Debug (6)

| # | Skill | Origem | Link / Path |
|---|---|---|---|
| 4 | `systematic-debugging` | Hermes nativo | https://github.com/NousResearch/hermes-agent/blob/main/skills/software-development/systematic-debugging/SKILL.md |
| 5 | `python-debugpy` | Hermes nativo | https://github.com/NousResearch/hermes-agent/blob/main/skills/software-development/python-debugpy/SKILL.md |
| 6 | `node-inspect-debugger` | Hermes nativo | https://github.com/NousResearch/hermes-agent/blob/main/skills/software-development/node-inspect-debugger/SKILL.md |
| 7 | `rest-graphql-debug` | Hermes-optional | https://github.com/NousResearch/hermes-agent/blob/main/optional-skills/software-development/rest-graphql-debug/SKILL.md |
| 8 | `agent-introspection-debugging` | ECC | https://github.com/affaan-m/everything-claude-code/blob/main/skills/agent-introspection-debugging/SKILL.md |
| 9 | `parallel-investigation` | Hermes | (verificar repo Hermes) |

### Review (3)

| # | Skill | Origem | Link / Path |
|---|---|---|---|
| 10 | `requesting-code-review` | Superpowers/Hermes | https://github.com/obra/superpowers/blob/main/skills/requesting-code-review/SKILL.md |
| 11 | `receiving-code-review` | Superpowers | https://github.com/obra/superpowers/blob/main/skills/receiving-code-review/SKILL.md |
| 12 | `github-code-review` | Hermes nativo | https://github.com/NousResearch/hermes-agent/blob/main/skills/github/github-code-review/SKILL.md |

### Planning técnico (4)

| # | Skill | Origem | Link / Path |
|---|---|---|---|
| 13 | `writing-plans` | Hermes nativo | https://github.com/NousResearch/hermes-agent/blob/main/skills/software-development/writing-plans/SKILL.md |
| 14 | `plan` | Hermes nativo | https://github.com/NousResearch/hermes-agent/blob/main/skills/software-development/plan/SKILL.md |
| 15 | `spike` | Hermes nativo | https://github.com/NousResearch/hermes-agent/blob/main/skills/software-development/spike/SKILL.md |
| 16 | `pre-mortem` | Hermes / Custom | Custom-to-create (verificar nativo) |

### Crítica e avaliação técnica (2)

| # | Skill | Origem | Link / Path |
|---|---|---|---|
| 17 | `critique-with-evidence` | Custom (modulada técnica) | Custom-to-create |
| 18 | `tool-evaluator` | Custom (modulada — dependência técnica) | Custom-to-create |

### Execução paralela (3)

| # | Skill | Origem | Link / Path |
|---|---|---|---|
| 19 | `subagent-driven-development` | Superpowers/Hermes | https://github.com/obra/superpowers/blob/main/skills/subagent-driven-development/SKILL.md |
| 20 | `using-git-worktrees` | Superpowers | https://github.com/obra/superpowers/blob/main/skills/using-git-worktrees/SKILL.md |
| 21 | `parallel-tasks` | Superpowers | https://github.com/obra/superpowers/blob/main/skills/parallel-tasks/SKILL.md |

### Git/Github (4)

| # | Skill | Origem | Link / Path |
|---|---|---|---|
| 22 | `github-pr-workflow` | Hermes nativo | https://github.com/NousResearch/hermes-agent/blob/main/skills/github/github-pr-workflow/SKILL.md |
| 23 | `github-repo-management` | Hermes nativo | https://github.com/NousResearch/hermes-agent/blob/main/skills/github/github-repo-management/SKILL.md |
| 24 | `finishing-a-development-branch` | Superpowers | https://github.com/obra/superpowers/blob/main/skills/finishing-a-development-branch/SKILL.md |
| 25 | `advanced-git-workflows` | Hermes | (verificar repo Hermes) |

### Arquitetura (1)

| # | Skill | Origem | Link / Path |
|---|---|---|---|
| 26 | `architecture-patterns` | wshobson/agents | https://github.com/wshobson/agents |

### CI/CD (1)

| # | Skill | Origem | Link / Path |
|---|---|---|---|
| 27 | `github-actions-templates` | wshobson/agents | https://github.com/wshobson/agents |

### Onboarding (2 → 3 após C2)

| # | Skill | Origem | Link / Path |
|---|---|---|---|
| 28 | `codebase-inspection` | Hermes nativo (pygount) | https://github.com/NousResearch/hermes-agent/blob/main/skills/github/codebase-inspection/SKILL.md |
| 29 | `repomix` | externa | https://github.com/yamadashy/repomix |
| **30** | **`codebase-onboarding`** ⭐ NOVO C2 | ECC | https://github.com/affaan-m/everything-claude-code/blob/main/skills/codebase-onboarding/SKILL.md |

### Lacunas Hermes preenchidas (3)

| # | Skill | Origem | Link / Path |
|---|---|---|---|
| 31 | `database-migrations` | ECC | https://github.com/affaan-m/everything-claude-code/blob/main/skills/database-migrations/SKILL.md |
| 32 | `error-handling` | ECC | https://github.com/affaan-m/everything-claude-code/blob/main/skills/error-handling/SKILL.md |
| 33 | `api-design` | ECC | https://github.com/affaan-m/everything-claude-code/blob/main/skills/api-design/SKILL.md |

### Security (3 → 4 após C2)

| # | Skill | Origem | Link / Path |
|---|---|---|---|
| 34 | `security-review` | ECC | https://github.com/affaan-m/everything-claude-code/blob/main/skills/security-review/SKILL.md |
| 35 | `agent-architecture-audit` | ECC | https://github.com/affaan-m/everything-claude-code/blob/main/skills/agent-architecture-audit/SKILL.md |
| 36 | `oss-forensics` | Hermes-optional | https://github.com/NousResearch/hermes-agent/blob/main/optional-skills/security/oss-forensics/SKILL.md |
| **37** | **`security-scan`** ⭐ NOVO C2 | ECC | https://github.com/affaan-m/everything-claude-code/blob/main/skills/security-scan/SKILL.md |

### Web QA (1)

| # | Skill | Origem | Link / Path |
|---|---|---|---|
| 38 | `dogfood` | Hermes nativo | https://github.com/NousResearch/hermes-agent/blob/main/skills/dogfood/SKILL.md |

### Pesquisa técnica/cultura (3)

| # | Skill | Origem | Link / Path |
|---|---|---|---|
| 39 | `xurl` | Hermes nativo | (verificar repo Hermes — HN/Twitter) |
| 40 | `youtube-content` | Hermes nativo | (verificar repo Hermes) |
| 41 | `gif-search` | Hermes nativo | (verificar repo Hermes) |

### Raw coding (7 — adicionadas 2026-05-19)

| # | Skill | Origem | Link / Path |
|---|---|---|---|
| 42 | `python-typing` | Hermes (mypy strict) | (verificar repo Hermes) |
| 43 | `python-async-patterns` | Hermes (asyncio) | (verificar repo Hermes) |
| 44 | `spec-kit` | GitHub Spec Kit | https://github.com/github/spec-kit |
| 45 | `typescript-advanced-types` | wshobson (lazy) | https://github.com/wshobson/agents |
| 46 | `property-based-testing` | Custom-to-create | Custom (Hypothesis + fast-check) |
| 47 | `strict-type-checking` | Custom-to-create | Custom (mypy strict + pyright + TS strict) |
| 48 | `code-review-checklist` | Custom-to-create | Custom (anti-blind-spot) |

### Manutenção próprio Hermes (1 — adicionada C2)

| # | Skill | Origem | Link / Path |
|---|---|---|---|
| **49** | **`debugging-hermes-tui-commands`** ⭐ NOVO C2 | Hermes nativo | https://github.com/NousResearch/hermes-agent/blob/main/skills/software-development/debugging-hermes-tui-commands/SKILL.md |

---

## 🛠️ Comandos rápidos pra testar

### Clonar repos principais

```bash
mkdir -p ~/Desktop/hefesto_skills_test
cd ~/Desktop/hefesto_skills_test

git clone --depth=1 https://github.com/obra/superpowers.git
git clone --depth=1 https://github.com/affaan-m/everything-claude-code.git
git clone --depth=1 https://github.com/NousResearch/hermes-agent.git
git clone --depth=1 https://github.com/wshobson/agents.git
git clone --depth=1 https://github.com/multica-ai/andrej-karpathy-skills.git
git clone --depth=1 https://github.com/github/spec-kit.git
```

### Filtrar só o que Hefesto usa

```bash
DST="$HOME/Desktop/hefesto_skills_test/_hefesto_final"
mkdir -p $DST

# Superpowers (TDD method, debug method, review, parallel, worktrees, branch finish)
for skill in test-driven-development systematic-debugging requesting-code-review \
             receiving-code-review subagent-driven-development using-git-worktrees \
             parallel-tasks finishing-a-development-branch verification-before-completion; do
  cp -r "superpowers/skills/$skill" $DST/
done

# ECC (lacunas Hermes + security + agent debug + meta)
for skill in ai-regression-testing security-review security-scan agent-architecture-audit \
             agent-introspection-debugging codebase-onboarding python-testing \
             database-migrations error-handling api-design council documentation-lookup; do
  cp -r "everything-claude-code/skills/$skill" $DST/
done

# Hermes-native (bundled — SKILL.md como referência)
for skill in test-driven-development systematic-debugging python-debugpy node-inspect-debugger \
             writing-plans plan spike debugging-hermes-tui-commands; do
  cp "hermes-agent/skills/software-development/$skill/SKILL.md" $DST/${skill}_ref.md
done

cp "hermes-agent/skills/github/github-code-review/SKILL.md" $DST/github-code-review_ref.md
cp "hermes-agent/skills/github/github-pr-workflow/SKILL.md" $DST/github-pr-workflow_ref.md
cp "hermes-agent/skills/github/github-repo-management/SKILL.md" $DST/github-repo-management_ref.md
cp "hermes-agent/skills/github/codebase-inspection/SKILL.md" $DST/codebase-inspection_ref.md
cp "hermes-agent/skills/dogfood/SKILL.md" $DST/dogfood_ref.md
cp "hermes-agent/optional-skills/security/oss-forensics/SKILL.md" $DST/oss-forensics_ref.md
cp "hermes-agent/optional-skills/software-development/rest-graphql-debug/SKILL.md" $DST/rest-graphql-debug_ref.md

# Drive Ultra Prompt v6.2 (universais novos)
SRC_DRIVE="$HOME/Desktop/Hermes_Project/05_ultra_prompt_v62_referencia/Ultra Prompt v6.2/skills/common"
cp "$SRC_DRIVE/critical-thinking.md" $DST/critical-thinking_ref.md
cp "$SRC_DRIVE/human-in-the-loop.md" $DST/human-in-the-loop_ref.md

# CLI tools (não são skills — instalar via package manager)
# Ruff: pip install ruff (Python linter/formatter rápido)
# Semgrep: pip install semgrep (SAST scanning)
# OSV-Scanner: go install github.com/google/osv-scanner/cmd/osv-scanner@latest (lockfile vuln scan)
# Spectral: npm install -g @stoplight/spectral-cli (OpenAPI linter)
# Repomix: npm install -g repomix (empacotar repo pra contexto LLM)
```

### Verificar contagem após copiar

```bash
find ~/Desktop/hefesto_skills_test/_hefesto_final/ -name "*.md" | wc -l
# Esperado: ~30-40 arquivos
```

---

## ⚠️ Skills marcadas Custom-to-create

Estas **não existem prontas** — vamos criar via Conductor:

1. **`anti-glaze`** (universal)
2. **`karpathy-discipline`** (universal — adaptar de `multica-ai/andrej-karpathy-skills`)
3. **`token-budget-advisor`** (universal)
4. **`property-based-testing`** (Hefesto custom — Hypothesis + fast-check)
5. **`strict-type-checking`** (Hefesto custom — mypy strict + pyright + TS strict)
6. **`code-review-checklist`** (Hefesto custom — anti-blind-spot)
7. **`critique-with-evidence`** (modulação técnica — base Apollo custom)
8. **`tool-evaluator`** (modulação técnica — base Apollo custom)
9. **`pre-mortem`** (verificar se nativo existe, senão custom)

---

## 🔧 CLI tools externas (não-skills — usadas por skills)

Estas são CLI tools que Hefesto invoca quando aplicável. Ver `playbook.md` §6.5 pra integração.

| Tool | Função | Skill que usa | Instalação |
|---|---|---|---|
| **Ruff** | Linter/formatter Python | `python-typing`, `verification-before-completion` | `pip install ruff` |
| **Semgrep** | SAST scanning multi-linguagem | `security-review`, `security-scan` | `pip install semgrep` ou Docker |
| **OSV-Scanner** | Vulnerability scan lockfiles | `security-review`, `oss-forensics` | `go install github.com/google/osv-scanner/cmd/osv-scanner@latest` ou binary |
| **Spectral** | OpenAPI linter | `api-design`, compliance Aurora↔Hefesto §14 | `npm install -g @stoplight/spectral-cli` |
| **pip-audit** | Python deps audit | `security-review`, `oss-forensics` | `pip install pip-audit` |
| **repomix** | Empacotar repo pra LLM | `repomix` skill | `npm install -g repomix` |
| **gh CLI** | GitHub operations | `github-pr-workflow`, `github-code-review`, `github-repo-management` | `winget install GitHub.cli` (Win) ou apt/brew |
| **mypy/pyright** | Type checking Python | `strict-type-checking` | `pip install mypy` |
| **pytest** | Test runner Python | `python-testing`, `test-driven-development` | `pip install pytest` |
| **Alembic** | SQLAlchemy migrations (CONDICIONAL) | `database-migrations` — só se stack usa SQLAlchemy | `pip install alembic` |

---

## 📚 Referências externas Hefesto

| Referência | URL |
|---|---|
| Hermes Skills System | https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/skills.md |
| Superpowers methodology | https://github.com/obra/superpowers |
| Everything Claude Code | https://github.com/affaan-m/everything-claude-code |
| wshobson agents | https://github.com/wshobson/agents |
| Andrej Karpathy Skills | https://github.com/multica-ai/andrej-karpathy-skills |

---

**Caminho deste arquivo**: `profiles/hefesto/skills_download_links.md`
