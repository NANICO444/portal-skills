# 📋 INSTRUÇÃO PARA O SUCESSOR — 4 MISSÕES

## 📌 Contexto

Você é o **sucessor**. O arquiteto anterior construiu um ecossistema completo de OpenCode. Agora você precisa **executar 4 missões** para organizar, catalogar, unificar e completar o que foi criado.

> ✅ **Missão 1 (Limpeza) já foi executada** pelo sucessor anterior. Duplicatas removidas, master intacta.

Todas as pastas estão dentro de:
```
C:\Users\User\Desktop\COISAS JOAO\skills pastas melhorias agentes\
```

**Regras importantes:**
- Para ler pastas, use os nomes EXATOS listados abaixo
- Você pode criar/adicionar coisas em QUALQUER pasta dentro deste diretório (não é obrigado a usar `multi-agent/`)
- Sempre peça confirmação antes de apagar algo
- Sempre mostre o diagnóstico antes de executar

---

## 🗺️ MAPA COMPLETO DO PROJETO (25 entradas)

```
📁 C:\Users\User\Desktop\COISAS JOAO\skills pastas melhorias agentes\
│
├── 📂 .agents/                     → Coleção bruta de skills (~935)
├── 📂 .kiro/                       → Sistema Kiro (Aurora + Hefesto, 62 skills, hooks, steering)
├── 📂 .opencode/                   → Config OpenCode do projeto (node_modules, package.json)
├── 📂 agents/                      → best_agent_frameworks.md + README
├── 📂 decision-system/             → 16 agentes, 12 skills de decisão
├── 📂 docs/                        → Documentação do ecossistema
├── 📂 max-thinking-system/         → 12 agentes (variant: max), 6 skills
├── 📂 models/                      → free_models_report.md
├── 📂 multi-agent/                 → 2 servidores, 181 skills (junction global)
├── 📂 oh-my-openagent/             → Projeto openagent completo (38 entries)
├── 📂 prompts/                     → 7 prompts de sistema
├── 📂 referencias_originais/       → Aurora + Hefesto originais
├── 📂 skills_github/               → 4 repos clonados (impeccable, taste-skill, etc)
├── 📂 skills_refinadas/            → Skills refinadas manualmente
├── 📂 SKILLS/                      → agent-skills-report.md + skill reports
├── 📂 templates/                   → 9 templates de projeto
├── 📂 ultracode/                   → 10 skills custom + placeholders
├── 📂 ULTRA_PROMPT_ANTIGRAVITY/    → Core Antigravity v7 (49 agentes, módulos, skills)
│
├── 📄 ARCHITECTURE.md              → Documento de arquitetura
├── 📄 INDEX.md                     → Índice do projeto
├── 📄 NOVO_ULTRA_PROMPT_PROJETOS.md → Prompt guia (~13MB)
├── 📄 README.md                    → Leia-me principal
├── 📄 SOBRE.html                   → Página sobre o projeto
├── 📄 WORKFLOWS.md                 → Documento de workflows
└── 📄 INSTRUCAO_SUCESSOR_LIMPEZA.md → Este arquivo
```

---

# 🎯 MISSÃO 2 — HANDFOFF.md (Manual do Sucessor)

Crie um arquivo `HANDFOFF.md` em qualquer lugar que fizer sentido dentro de `skills pastas melhorias agentes`.

**Conteúdo que deve ter:**

```markdown
# HANDFOFF — Manual do Sucessor

## 📂 Estrutura do Projeto
[Listar todas as 25 entradas da raiz com descrição]

## 🧠 Sistemas Criados

### multi-agent/
- O que faz: 2 servidores (portas 3001, 3002), 181 skills
- Localização: skills pastas melhorias agentes/multi-agent/.opencode/skills/
- Junction global em: ~/.config/opencode/skills/

### decision-system/
- O que faz: 16 agentes (6 primários + 10 sub), 12 skills de decisão
- Skills: strategic-decision, tech-decision, financial-decision, risk-decision, marketing-decision, ops-decision, etc.

### max-thinking-system/
- O que faz: 12 agentes com variant: max, pensamento ultra-profundo
- Skills: deep-analysis, max-thinking, complex-architecture-decision, deepseek-architecture-decision, etc.

### ultracode/
- O que faz: 10 skills custom (deepseek-architecture-decision, complex-architecture-decision, etc.)

## ⚙️ Configuração Global
- Arquivo: ~/.config/opencode/opencode.json
- Modelo padrão: zenmux/deepseek/deepseek-v4-flash-free
- Modelo small: zenmux/stepfun/step-3.7-flash-free
- 7 modelos gratuitos configurados via ZenMux

## 🔗 Junctions Ativas
- ~/.config/opencode/skills/ → multi-agent/.opencode/skills/
- ~/.config/opencode/agents/ → max-thinking-system/.opencode/agents/
- ~/.config/opencode/rules/always-delegate.md → regra global

## 🚫 Pastas que NÃO Podem Ser Tocadas
- .kiro/ (sistema Kiro original)
- ULTRA_PROMPT_ANTIGRAVITY/ (core antigravity)
- oh-my-openagent/ (projeto completo externo)
- referencias_originais/ (backup histórico)

## 📋 Comandos Úteis
- opencode models zenmux → listar modelos
- Ler junction: Get-ChildItem ~/.config/opencode/skills/
- Contar skills: (Get-ChildItem "multi-agent/.opencode/skills" -Directory).Count
```

---

# 🎯 MISSÃO 3 — DEEPSEEK COMO DEFAULT ABSOLUTO

## Passo 1 — Verificar config atual

```powershell
Get-Content "C:\Users\User\.config\opencode\opencode.json" | Select-String "model"
```

## Passo 2 — Escanear skills que usam outros modelos

```powershell
$skillsDir = "C:\Users\User\Desktop\COISAS JOAO\skills pastas melhorias agentes\multi-agent\.opencode\skills"
$results = @()

Get-ChildItem $skillsDir -Directory | ForEach-Object {
    $skillPath = "$($_.FullName)\SKILL.md"
    if (Test-Path $skillPath) {
        $content = Get-Content $skillPath -Raw
        if ($content -match "model:\s*(?!zenmux/deepseek)(.+)" -and $content -notmatch "model:\s*null") {
            $currentModel = $matches[1].Trim()
            $results += [PSCustomObject]@{
                Skill = $_.Name
                Model = $currentModel
                Path = $skillPath
            }
        }
    }
}

Write-Host "Skills com modelo diferente de DeepSeek:"
$results | Format-Table -AutoSize
```

## Passo 3 — Alterar para DeepSeek

Para cada skill que usar outro modelo (ex: `openrouter/claude-opus-4.8`), troque por:

```yaml
model: zenmux/deepseek/deepseek-v4-flash-free
fallback: [zenmux/z-ai/glm-5.2-free]
```

Faça isso editando o frontmatter de cada SKILL.md. Mostre relatório ao final:

```powershell
Write-Host "Total de skills alteradas: $($results.Count)"
```

---

# 🎯 MISSÃO 4 — ORQUESTRADOR MESTRE (Meta-Agent)

## Passo 1 — Criar a skill

Crie o arquivo em qualquer lugar dentro de `skills pastas melhorias agentes`, por exemplo:
```
skills pastas melhorias agentes/orquestrador-mestre/SKILL.md
```

Com este conteúdo base:

```yaml
---
name: orquestrador-mestre
description: "ORQUESTRADOR MESTRE — Analisa o problema e roteia para o sistema ideal (multi-agent, decision-system, ou max-thinking-system). Meta-agente que conhece todos os sistemas."
model: zenmux/deepseek/deepseek-v4-flash-free
fallback: [zenmux/z-ai/glm-5.2-free]
user-invocable: true
allowed-tools: Read, Grep, Glob, Bash, Task, Write, Edit
---
```

## Passo 2 — Conteúdo da skill

A skill deve ter:

1. **Análise do problema** — Classificar em:
   - 🔧 **Técnico puro** (codar, debug, refatorar) → usar multi-agent
   - ⚖️ **Decisão estratégica** (escolher stack, arquitetura) → usar decision-system
   - 🧠 **Análise profunda** (investigar, pensar, planejar) → usar max-thinking-system
   - 🎨 **Design/UX** → usar max-thinking-system (com skills de design)

2. **Framework de decisão de 3 perguntas:**
   - *"Precisa de paralelismo ou execução simultânea?"* → multi-agent
   - *"Tem trade-offs claros com múltiplas opções?"* → decision-system
   - *"Precisa de pensamento profundo ou análise complexa?"* → max-thinking-system

3. **No final, o orquestrador explica:**
   - Qual sistema escolheu e por quê
   - Qual skill específica dentro do sistema usar
   - Exemplo de comando para o usuário chamar

## Passo 3 — Opcional: juntar na junction global

```powershell
# Se quiser que apareça no OpenCode globalmente
$globalSkills = "C:\Users\User\.config\opencode\skills"
$source = "C:\Users\User\Desktop\COISAS JOAO\skills pastas melhorias agentes\orquestrador-mestre"
New-Item -ItemType Directory -Force -Path "$globalSkills\orquestrador-mestre" | Out-Null
Copy-Item "$source\SKILL.md" -Destination "$globalSkills\orquestrador-mestre\SKILL.md" -Force
Write-Host "✅ Orquestrador mestre adicionado à junction global"
```

---

# 🎯 MISSÃO 5 — CATÁLOGO DE SKILLS PESADO

## Passo 1 — Escanear todas as skills

```powershell
$root = "C:\Users\User\Desktop\COISAS JOAO\skills pastas melhorias agentes"
$skillsDirs = @(
    "$root\ulti-agent\.opencode\skills",
    "$root\.agents\skills",
    "$root\.kiro\skills",
    "$root\ultracode"
)

$allSkills = @()

foreach ($dir in $skillsDirs) {
    if (Test-Path $dir) {
        Get-ChildItem $dir -Directory | ForEach-Object {
            $skillPath = "$($_.FullName)\SKILL.md"
            $model = "desconhecido"
            $lines = 0
            $hasSkill = $false
            
            if (Test-Path $skillPath) {
                $hasSkill = $true
                $content = Get-Content $skillPath -Raw
                $lines = ($content -split "`n").Count
                if ($content -match "model:\s*(\S+)") { $model = $matches[1] }
            }
            
            $allSkills += [PSCustomObject]@{
                Name = $_.Name
                Path = $_.FullName.Replace($root, "")
                HasSKILL = $hasSkill
                Lines = $lines
                Model = $model
                Source = $dir.Replace($root, "")
            }
        }
    }
}
```

## Passo 2 — Gerar CATALOGO_SKILLS.md

Crie o arquivo em qualquer lugar, por exemplo `skills pastas melhorias agentes/CATALOGO_SKILLS.md`.

**Estrutura do catálogo:**

```markdown
# 📚 Catálogo de Skills — Ecossistema OpenCode

> Gerado em: [data]
> Total: [número] skills

## Por Categoria

### 🏛️ Arquitetura e Decisão
| Skill | Local | Modelo | Linhas |
|---|---|---|---|
| deepseek-architecture-decision | .../ultracode/ | DeepSeek | 697 |
| complex-architecture-decision | .../multi-agent/ | Claude Opus | 115 |
| adr-architecture-decision | .../ulti-agent/ | - | ... |

### 💻 Código e Desenvolvimento
| Skill | Local | Modelo | Linhas |
|---|---|---|---|
| code-review | ... | ... | ... |
| test-driven-development | ... | ... | ... |
| ... | ... | ... | ... |

### 🎨 Design e UX
| Skill | Local | Modelo | Linhas |
|---|---|---|---|
| ... | ... | ... | ... |

### 🔒 Segurança
| Skill | Local | Modelo | Linhas |
|---|---|---|---|
| ... | ... | ... | ... |

### ⚙️ DevOps e Infra
| Skill | Local | Modelo | Linhas |
|---|---|---|---|
| ... | ... | ... | ... |

### 📊 Análise e Decisão
| Skill | Local | Modelo | Linhas |
|---|---|---|---|
| ... | ... | ... | ... |

## ⭐ Skills Criadas Manualmente (Custom)
- deepseek-architecture-decision
- complex-architecture-decision
- [outras...]

## Índice Alfabético
[A-Z list]
```

## Passo 3 — Classificar skills por categoria

Use o nome da skill para inferir categoria:

| Padrão no nome | Categoria |
|---|---|
| architecture, decision, strategic, plan | 🏛️ Arquitetura |
| code, review, test, debug, refactor | 💻 Código |
| design, ui, ux, visual, component | 🎨 Design |
| security, threat, audit, compliance | 🔒 Segurança |
| deploy, devops, infra, ci, cd | ⚙️ DevOps |
| data, database, schema, model | 🗄️ Dados |
| api, integration, graphql, rest | 🔌 API |
| agent, skill, mcp, tool, orchest | 🤖 Agentes |

Para skills que não se encaixam, use "📦 Geral".

---

# ✅ CHECKLIST FINAL

Depois de completar as 4 missões, verifique:

- [x] ~~**Missão 1** — Duplicatas removidas, master intacta~~ ✅ (já feita)
- [ ] **Missão 2** — HANDFOFF.md criado com mapa completo
- [ ] **Missão 3** — DeepSeek é modelo padrão em todas as skills
- [ ] **Missão 4** — Orquestrador mestre criado e funcional
- [ ] **Missão 5** — CATALOGO_SKILLS.md gerado com todas as skills

Mostre este checklist pro usuário quando terminar cada missão.
