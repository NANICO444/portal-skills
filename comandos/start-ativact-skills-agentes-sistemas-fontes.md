---
description: "ATIVACAO TOTAL ABSOLUTA: le o projeto INTEIRO + carrega TODAS skills OpenCode (~145) + cataloga .agents/skills/ (935) + .kiro (62) + workspace (7) + junction (192) + agentes (28) + sistemas (3) + ferramentas PC control. TOTAL: ~1198 skills. Nao deixa NADA inativo."
---

# /start-ativact-skills-agentes-sistemas-fontes

Voce foi invocado via comando slash. Este comando e SUPREMO e deve ATIVAR ABSOLUTAMENTE TUDO. Nao pergunte, nao pule, nao economize. FACA.

## OBJETIVO SUPREMO — ATIVAR 100% DE ~1198 SKILLS

O projeto tem **~1198 skills** de 4 tipos diferentes. Cada tipo exige ativacao diferente:

| Tipo | Qtd | Como ativar |
|------|-----|-------------|
| **OpenCode skills** (junction + workspace) | ~199 | Via `skill` tool (as que estao em available_skills) |
| **.agents/skills/** (YAML) | 935 | Catalogar nome+descricao, ativar sob demanda |
| **.kiro/ skills** (aurora + hefesto docs) | 62 | Ler e incorporar como knowledge |
| **Skills custom criadas** (pc-control, glm) | 2 | Via `skill` tool |

Mais:
- 28 agentes (12 max-thinking + 16 decision-system)
- 3 sistemas (multi-agent, decision-system, max-thinking-system)
- Ferramentas PC control + alarmes + comandos slash
- deepseek-architecture-decision permanentemente ativa

## PROJETO

Raiz: `C:\Users\User\Desktop\COISAS JOAO\skills pastas melhorias agentes`

---

## FASE 0 — JUNCTIONS + CONFIG

```
$js="$env:USERPROFILE\.opencode\skills"; $ja="$env:USERPROFILE\.config\opencode\agents"
$ss="$env:USERPROFILE\Desktop\COISAS JOAO\skills pastas melhorias agentes\multi-agent\.opencode\skills"
$sa="$env:USERPROFILE\Desktop\COISAS JOAO\skills pastas melhorias agentes\max-thinking-system\.opencode\agents"
if (-not (Test-Path $js)) { New-Item -Path $js -ItemType Junction -Target $ss -Force }
if (-not (Test-Path $ja)) { $null=New-Item -Path (Split-Path $ja -Parent) -ItemType Directory -Force; New-Item -Path $ja -ItemType Junction -Target $sa -Force }
Get-Item $js|Select FullName,LinkType,Target; Get-Item $ja|Select FullName,LinkType,Target
$cfg=Get-Content "$env:USERPROFILE\.config\opencode\opencode.json" -Raw; Write-Host "Config:" $cfg.Substring(0,300)
$skillCount=(Get-ChildItem $js -Directory).Count; $agentCount=(Get-ChildItem $ja -Recurse -File).Count
Write-Host "Skills na junction: $skillCount | Arquivos de agentes: $agentCount"
```

---

## FASE 1 — MAPEAMENTO TOTAL DO PROJETO

```
$base="C:\Users\User\Desktop\COISAS JOAO\skills pastas melhorias agentes"
Write-Host "Total arquivos: $((Get-ChildItem $base -Recurse -File -ErrorAction SilentlyContinue).Count)"
Write-Host "Total pastas: $((Get-ChildItem $base -Recurse -Directory -ErrorAction SilentlyContinue).Count)"
Write-Host "Pastas raiz:"; Get-ChildItem $base -Depth 0|Where PSIsContainer|Sort Name|%{Write-Host "  $($_.Name)"}
```

Leia TODOS os arquivos de configuracao essenciais:
- `.kiro/docs/*.md`, `.kiro/agents/*.md`, `.kiro/skills/*/SKILL.md` (62)
- `.opencode/skills/*/SKILL.md` (7 workspace)
- `.opencode/rules/*.md`
- `multi-agent/.opencode/rules/*.md`
- `decision-system/.opencode/agents/*.md` (16)
- `max-thinking-system/.opencode/agents/*.md` (12)
- Arquivos raiz .md (ARCHITECTURE, HANDFOFF, CATALOGO, README, etc)

Use sub-agentes em paralelo para ler tudo rapido.

---

## FASE 2 — CATALOGAR .AGENTS/SKILLS/ (935)

```
$agSkills="C:\Users\User\Desktop\COISAS JOAO\skills pastas melhorias agentes\.agents\skills"
$total=(Get-ChildItem $agSkills -Recurse -Filter "*.yaml" -ErrorAction SilentlyContinue).Count
Write-Host "Skills .agents/ encontradas: $total"
```

Use 5 sub-agentes paralelos para catalogar nome + descricao de todas as 935 skills YAML.
Divisao: a-c, d-g, h-m, n-s, t-z.

---

## FASE 3 — ATIVAR ABSOLUTAMENTE TODAS AS SKILLS DO OPENCODE

Variavel critica: a available_skills desta sessao tem ~145 skills. Carregue CADA UMA via skill tool.

Use skill tool em **lotes de 5 em paralelo**. Nao pule nenhuma.

### BLOCO A — Arquitetura & Raciocinio (5 lotes)

**Lote A1:** deepseek-architecture-decision, critical-thinking, max-thinking, deep-analysis, karpathy-discipline
**Lote A2:** system-design, design-an-interface, complex-architecture-decision, deepseek-architecture-decision, glm-architecture-decision
**Lote A3:** council, adversarial-decision-analysis, cross-domain-optimization, long-term-strategic-forecast, multi-factor-risk-assessment
**Lote A4:** think-max-protocol, max-thinking, hyperplan, orquestrador-mestre, adr-architecture-decision

### BLOCO B — Qualidade & Evidencia (5 lotes)

**Lote B1:** anti-glaze, evidence-based-dev, verification-before-completion, investigate-before-edit, code-review-checklist
**Lote B2:** impeccable-quality, quality-validation, factual-verify, critique-with-evidence, anti-glaze-ux
**Lote B3:** code-review, github-code-review, receiving-code-review, requesting-code-review, codebase-inspection
**Lote B4:** codebase-onboarding, review, supervisor, agent-architecture-audit, agent-introspection-debugging

### BLOCO C — Refatoracao & Mudanca (4 lotes)

**Lote C1:** safe-refactor, small-diffs, rollback-strategy, pre-mortem, improve-codebase-architecture
**Lote C2:** remove-deadcode, tech-debt-audit, request-refactor-plan, finishing-a-development-branch, using-git-worktrees
**Lote C3:** advanced-git-workflows, github-pr-workflow, github-repo-management, github-triage, work-with-pr
**Lote C4:** deploy-protocol, deployment-automation, rollback-strategy, database-migrations, firewall-s(

### BLOCO D — Seguranca (3 lotes)

**Lote D1:** security-review, security-scan, security-research, kiro-data-security, error-handling
**Lote D2:** error-recovery-design, rest-graphql-debug, diagnostic-analysis, node-inspect-debugger, react-doctor
**Lote D3:** model-router-fallback, token-budget-advisor, kiro-verification

### BLOCO E — Frontend & Design (4 lotes)

**Lote E1:** design-taste-frontend, design-taste-frontend-v1, ui-ux-pro-max, user-interface-designer, visual-composition
**Lote E2:** high-end-visual-design, gpt-taste, industrial-brutalist-ui, minimalist-ui, stitch-design-taste
**Lote E3:** component-library, frontend-patterns, html-anything, image-to-code, imagegen-frontend-web
**Lote E4:** imagegen-frontend-mobile, brandkit, aesthetic-analysis, design-extract, design-md

### BLOCO F — Frontend Stack (3 lotes)

**Lote F1:** frontend-stack-decision, api-design, api-integration, rest-graphql-debug, spec-kit
**Lote F2:** browser-testing, performance-web-vitals, motion-foundations, motion-patterns, accessibility-audit
**Lote F3:** seo-advanced, popular-web-designs, palette, design-brief, content-generation

### BLOCO G — Backend & Dados (3 lotes)

**Lote G1:** library-curator, doc-read, doc-cache, documentation-lookup, evidence-based-dev
**Lote G2:** python-async-patterns, python-debugpy, python-testing, python-typing, strict-type-checking
**Lote G3:** property-based-testing, test-driven-development, typescript-advanced-types, database-migrations, web-scrape

### BLOCO H — Kiro & Governanca (3 lotes)

**Lote H1:** kiro-engineering-process, kiro-design-process, kiro-verification, kiro-data-security, kiro-steering-governance
**Lote H2:** hefesto-routing, hefesto-workflow, aurora-routing, aurora-workflow, multi-agent-orchestration
**Lote H3:** delegated-development, nexus-orchestration, subagent-driven-development, plan-implementation, plan

### BLOCO I — Aurora Personas (4 lotes)

**Lote I1:** aurora-persona-accessibility-auditor, aurora-persona-brand-guardian, aurora-persona-content-creator, aurora-persona-paid-media, aurora-persona-performance-benchmarker
**Lote I2:** aurora-persona-reality-checker, aurora-persona-seo-specialist, aurora-persona-visual-storyteller, baoyu-infographic, excalidraw

### BLOCO J — Ferramentas & Utilitarios (3 lotes)

**Lote J1:** tavily-search, duckduckgo-search, web-fetch, web-scrape, youtube-content
**Lote J2:** gif-search, xurl, ocr, native-mcp, maton-gateway
**Lote J3:** find-skills, capability-architect, submit-improvement-to-themis, human-in-the-loop, ai-regression-testing

### BLOCO K — Skills de Dominio (2 lotes)

**Lote K1:** licitacoes, financial-decision, marketing-decision, ops-decision, strategic-decision
**Lote K2:** risk-decision, tech-decision, fix-suggester, rollback-strategy, app-builder

### BLOCO L — Qualidade & Testes (2 lotes)

**Lote L1:** codex-qa, opencode-qa, qa, pre-publish-review, get-unpublished-changes
**Lote L2:** publish, publish, dogfood, templates, repomix

### BLOCO M — PC Control & Ferramentas (2 lotes)

**Lote M1:** pc-control (skill custom), glm-architecture-decision (skill custom), writing-plans, spec-kit, system-design
**Lote M2:** error-handling, error-recovery-design, human-in-the-loop, verification-before-completion, karpathy-discipline

---

## FASE 4 — ATIVAR TODOS OS AGENTES

### 4.1 — Agentes Max-Thinking (12)
Leia os arquivos em `~/.config/opencode/agents/`:

**Main:**
1. `main/supervisor.md` — SUPERVISOR SUPREMO, ve tudo, aprova/rejeita, fala o que apagar/adicionar/fazer/baixar
2. `main/code-architect.md` — ARQUITETO DE CODIGO, design de sistema, padroes, estrutura (VOCE)
3. `main/quality-gate.md` — Quality Gate, qualidade maxima, aprovacao final

**Specialists:**
4. `specialists/code-reviewer-x.md` — Code Reviewer extremo, revisao profunda
5. `specialists/security-auditor.md` — Security Auditor, OWASP Top 10, SQLi, XSS
6. `specialists/performance-auditor.md` — Performance Auditor, Big O, memoria, I/O
7. `specialists/test-coverage-auditor.md` — Test Coverage Auditor
8. `specialists/fix-suggester.md` — Fix Suggester, o que apagar/adicionar/fazer/baixar
9. `specialists/library-curator.md` — Library Curator, conhece todas bibliotecas
10. `specialists/dependency-auditor.md` — Dependency Auditor, CVEs
11. `specialists/standards-enforcer.md` — Standards Enforcer
12. `specialists/docs-auditor.md` — Docs Auditor

Leia com sub-agentes (4 paralelos).

### 4.2 — Agentes Decision-System (16)
Leia os arquivos em `decision-system/.opencode/agents/`:
```
Get-ChildItem "C:\Users\User\Desktop\COISAS JOAO\skills pastas melhorias agentes\decision-system\.opencode\agents" -Recurse -Filter "*.md" | %{ Write-Host "  $($_.BaseName):"; Get-Content $_.FullName -TotalCount 3 }
```

---

## FASE 5 — ATIVAR DEEPSEEK-ARCHITECTURE-DECISION

Carregue `deepseek-architecture-decision` via skill tool.
Se modelo GLM, carregue `glm-architecture-decision`.

Esta skill fica PERMANENTEMENTE ATIVA. Toda resposta complexa passa pelas 13 (ou 15) camadas.

---

## FASE 6 — VERIFICAR FERRAMENTAS DO PROJETO

```
$base="C:\Users\User\Desktop\COISAS JOAO\skills pastas melhorias agentes"

Write-Host "=== PC CONTROL ==="
Get-ChildItem "$base\pc-control\*.ps1" | Select Name, @{N='KB';E={'{0:N1}' -f ($_.Length/1KB)}}

Write-Host "=== OCR ENGINE ==="
if (Test-Path "$base\pc-control\ocr-engine\ocr-app.exe") { Write-Host "OCR: OK" }

Write-Host "=== ALARMES ==="
Get-ChildItem "$base\alarmes\*.wav" | Select Name, @{N='KB';E={'{0:N1}' -f ($_.Length/1KB)}}

Write-Host "=== SKILLS CUSTOM ==="
Get-ChildItem "$base\skills\*\SKILL.md" | %{ Write-Host "  $($_.Directory.Name)" }

Write-Host "=== COMANDOS SLASH ==="
Get-ChildItem "$base\comandos\*.md" | %{ Write-Host "  $($_.BaseName)" }

Write-Host "=== SCREENSHOTS ==="
if (Test-Path "$base\screenshots (opencode)") { Write-Host "Pasta screenshots: OK" }

# Rclone
$r=Get-Process rclone -ErrorAction SilentlyContinue
if ($r) { Write-Host "RCLONE RODANDO PID $($r.Id)" } else { Write-Host "RCLONE PARADO" }
```

---

## REGRAS PERMANENTES (21)

1. **DEEPSEEK/GLM-ARCHITECTURE-DECISION**: ativa em TODA resposta complexa — 13/15 camadas
2. **ANTI-GLAZE**: sem bajulacao, avaliacao honesta com evidencia
3. **EVIDENCE-BASED-DEV**: toda afirmacao exige output de comando
4. **VERIFICATION-BEFORE-COMPLETION**: rode comando antes de dizer "pronto"
5. **INVESTIGATE-BEFORE-EDIT**: nunca edite sem entender
6. **SMALL-DIFFS**: cada commit uma coisa, < 50 linhas
7. **SAFE-REFACTOR**: testes primeiro, passos pequenos
8. **ROLLBACK-STRATEGY**: sempre ter plano B
9. **ANTI-GLAZE-UX**: nenhum dark pattern
10. **HUMAN-IN-THE-LOOP**: pergunte em acoes irreversiveis
11. **ALARMES OK**: alarme_curto.wav x8
12. **ALARMES MERDA**: merda_eco.wav x2
13. **PADRAO SILENCIO**: alarme so em momentos especificos
14. **UPLOAD RCLONE**: continua em background, nao mexa sem ordem
15. **IDIOMA**: pt-BR SEMPRE
16. **KIRO ATIVADO**: Aurora para design, Hefesto para engenharia
17. **TRES SISTEMAS**: multi-agent (codigo), decision-system (decisao), max-thinking-system (analise)
18. **.AGENTS/SKILLS/ (935)**: catalogadas, ativar sob demanda
19. **SEMPRE DELEGAR**: use agentes/sub-agentes para tarefas
20. **PC CONTROL DISPONIVEL**: ver_tela.ps1, mover_mouse, clicar, digitar, OCR
21. **COMANDO SLASH DISPONIVEL**: /start-ativact-skills-agentes-sistemas-fontes

---

## RESPOSTA FINAL

```
╔══════════════════════════════════════════════════════════╗
║          ATIVACAO TOTAL ABSOLUTA DO ECOSSISTEMA         ║
║          [data/hora]                                    ║
╚══════════════════════════════════════════════════════════╝

JUNCTIONS: skills=[OK](192)  agents=[OK](28 arquivos)

PROJETO:
  Arquivos: [N]  Pastas: [N]
  Skills workspace (.opencode/skills): 7

=== TOTAL DE SKILLS NO PROJETO: ~1198 ===

  OpenCode junction skills:   192 (carregaveis via skill tool: ~145)
  .agents/skills/ (YAML):     935 (catalogadas, ativar sob demanda)
  .kiro/ aurora:               31 (lidas e incorporadas)
  .kiro/ hefesto:              31 (lidas e incorporadas)
  Skills custom criadas:        2 (pc-control, glm-architecture-decision)
  Skills carregadas via tool: [N]

AGENTES:
  Max-Thinking: 3 main + 9 specialists = 12
  Decision-System: [N] agents
  Total ativos: [N]

SISTEMAS:
  multi-agent: [OK]
  decision-system: [OK]
  max-thinking-system: [OK]

SKILL DE ARQUITETURA: [deepseek | glm]-architecture-decision ATIVA

FERRAMENTAS DO PROJETO:
  PC Control: [N] scripts + OCR engine
  Alarmes: [N] wav + [N] scripts
  Skills custom: pc-control, glm-architecture-decision
  Comandos slash: 1
  Screenshots: pasta criada

ALARMES: OK x8 tocado
RCLONE: [RODANDO/PARADO] — [objetos] obj / [MB] MB

REGRAS PERMANENTES: 21 ATIVAS
KIRO: ATIVO  |  DEEPSEEK/GLM DECISION: ATIVO  |  PC CONTROL: ATIVO

STATUS: [TUDO OK / PROBLEMAS: lista]
╔══════════════════════════════════════════════════════════╗
║   PRONTO. ~1198 SKILLS MAPEADAS. ~145 CARREGADAS.      ║
║   .AGENTS/ (935) + .KIRO/ (62) SOB DEMANDA.            ║
║   TUDO ATIVO. DIGA O QUE PRECISA.                      ║
╚══════════════════════════════════════════════════════════╝
```

Toca alarme OK (x8) no final se tudo OK, MERDA (x2) se falhou algo.
