# 🎯 MISSÃO: DEEPSEEK V4 FLASH FREE EM TUDO

> **Objetivo:** Fazer TODO o ecossistema OpenCode usar exclusivamente `zenmux/deepseek/deepseek-v4-flash-free`
> **Contexto:** O predecessor migrou 24 skills mas PAROU no meio. Tem 18 agentes, 1 config global, e skills em `.agents/` (935) que ainda usam MiniMax-M3, openrouter/deepseek-v4-flash, ou o default GLM 5.2 Free.

---

## 🔍 CENÁRIO ATUAL (diagnosticado)

| Onde | O que | Status |
|------|-------|--------|
| **opencode.json** | `model: zenmux/z-ai/glm-5.2-free` | ❌ Default errado |
| **Provider zenmux** | Não tem `deepseek/deepseek-v4-flash-free` listado | ❌ Missing |
| **18 agentes** (max-thinking + decision-system) | `tokenrouter/MiniMax-M3` ou `openrouter/deepseek-v4-flash` | ❌ Modelo antigo |
| **24 skills** (multi-agent junction) | `zenmux/deepseek/deepseek-v4-flash-free` | ✅ Já migradas |
| **~159 skills** (multi-agent junction) | Sem `model:` field → usam default | ⚠️ Serão corrigidas pelo passo 1 |
| **935 skills** (`.agents/`) | Sem `model:` field → usam default | ⚠️ Idem |
| **~20 skills** (ultracode, decision-system, etc) | Sem `model:` field → usam default | ⚠️ Idem |

---

## 🛠️ PASSO 1 — Config Global (opencode.json)

Arquivo: `C:\Users\User\.config\opencode\opencode.json`

### 1.1 Adicionar DeepSeek ao provider `zenmux`

Dentro de `"zenmux": { "models": { ... } }`, adicione:

```json
"deepseek/deepseek-v4-flash-free": {
  "name": "DeepSeek: DeepSeek V4 Flash Free",
  "limit": {
    "context": 1000000,
    "output": 128000
  }
}
```

### 1.2 Mudar o modelo padrão

Troque:
```json
"model": "zenmux/z-ai/glm-5.2-free",
"small_model": "zenmux/stepfun/step-3.7-flash-free"
```

Para:
```json
"model": "zenmux/deepseek/deepseek-v4-flash-free",
"small_model": "zenmux/deepseek/deepseek-v4-flash-free"
```

### ✅ Resultado do Passo 1

Depois disso, TODAS as skills sem `model:` explícito no frontmatter usarão DeepSeek automaticamente. Isso cobre:
- ~159 skills do multi-agent junction
- 935 skills do `.agents/`
- ~20 skills de ultracode, decision-system, max-thinking-system

---

## 🛠️ PASSO 2 — Migrar 18 Agentes

Os agentes TÊM `model:` explícito apontando para MiniMax-M3 ou openrouter/deepseek. Eles NÃO são afetados pela config global — precisam de edição individual.

### 2.1 Esquema de alteração

Em cada arquivo `.md` de agente, dentro do frontmatter YAML (entre `---`), troque:

```yaml
model: tokenrouter/MiniMax-M3
```
para:
```yaml
model: zenmux/deepseek/deepseek-v4-flash-free
fallback: [zenmux/z-ai/glm-5.2-free]
```

E:
```yaml
model: openrouter/deepseek-v4-flash
```
para:
```yaml
model: zenmux/deepseek/deepseek-v4-flash-free
fallback: [zenmux/z-ai/glm-5.2-free]
```

### 2.2 Lista de arquivos para editar (18 arquivos)

**max-thinking-system (main)** — 3 arquivos:
```
max-thinking-system/.opencode/agents/main/code-architect.md
max-thinking-system/.opencode/agents/main/quality-gate.md
max-thinking-system/.opencode/agents/main/supervisor.md
```

**max-thinking-system (specialists)** — 9 arquivos:
```
max-thinking-system/.opencode/agents/specialists/code-reviewer-x.md
max-thinking-system/.opencode/agents/specialists/dependency-auditor.md
max-thinking-system/.opencode/agents/specialists/performance-auditor.md
max-thinking-system/.opencode/agents/specialists/security-auditor.md
max-thinking-system/.opencode/agents/specialists/standards-enforcer.md
max-thinking-system/.opencode/agents/specialists/docs-auditor.md
max-thinking-system/.opencode/agents/specialists/fix-suggester.md
max-thinking-system/.opencode/agents/specialists/library-curator.md
max-thinking-system/.opencode/agents/specialists/test-coverage-auditor.md
```

**decision-system (decision-makers)** — 3 arquivos:
```
decision-system/.opencode/agents/decision-makers/financial-advisor.md
decision-system/.opencode/agents/decision-makers/risk-manager.md
decision-system/.opencode/agents/decision-makers/strategic-planner.md
```

**decision-system (specialists)** — 3 arquivos:
```
decision-system/.opencode/agents/specialists/marketing-strategist.md
decision-system/.opencode/agents/specialists/ops-manager.md
decision-system/.opencode/agents/specialists/tech-lead.md
```

### 2.3 Script PowerShell para alterar TUDO de uma vez

```powershell
$root = "C:\Users\User\Desktop\COISAS JOAO\skills pastas melhorias agentes"
$arquivos = @(
    # max-thinking main
    "$root\max-thinking-system\.opencode\agents\main\code-architect.md",
    "$root\max-thinking-system\.opencode\agents\main\quality-gate.md",
    "$root\max-thinking-system\.opencode\agents\main\supervisor.md",
    # max-thinking specialists
    "$root\max-thinking-system\.opencode\agents\specialists\code-reviewer-x.md",
    "$root\max-thinking-system\.opencode\agents\specialists\dependency-auditor.md",
    "$root\max-thinking-system\.opencode\agents\specialists\performance-auditor.md",
    "$root\max-thinking-system\.opencode\agents\specialists\security-auditor.md",
    "$root\max-thinking-system\.opencode\agents\specialists\standards-enforcer.md",
    "$root\max-thinking-system\.opencode\agents\specialists\docs-auditor.md",
    "$root\max-thinking-system\.opencode\agents\specialists\fix-suggester.md",
    "$root\max-thinking-system\.opencode\agents\specialists\library-curator.md",
    "$root\max-thinking-system\.opencode\agents\specialists\test-coverage-auditor.md",
    # decision-system makers
    "$root\decision-system\.opencode\agents\decision-makers\financial-advisor.md",
    "$root\decision-system\.opencode\agents\decision-makers\risk-manager.md",
    "$root\decision-system\.opencode\agents\decision-makers\strategic-planner.md",
    # decision-system specialists
    "$root\decision-system\.opencode\agents\specialists\marketing-strategist.md",
    "$root\decision-system\.opencode\agents\specialists\ops-manager.md",
    "$root\decision-system\.opencode\agents\specialists\tech-lead.md"
)

$trocados = 0
foreach ($arq in $arquivos) {
    if (-not (Test-Path $arq)) { Write-Host "NAO ENCONTRADO: $arq"; continue }
    $conteudo = Get-Content $arq -Raw
    
    # Troca modelos antigos pelo novo
    $novo = $conteudo -replace 'model:\s*tokenrouter/MiniMax-M3', 'model: zenmux/deepseek/deepseek-v4-flash-free'
    $novo = $novo -replace 'model:\s*openrouter/deepseek-v4-flash', 'model: zenmux/deepseek/deepseek-v4-flash-free'
    
    if ($novo -ne $conteudo) {
        # Adiciona fallback se nao existir
        if ($novo -notmatch 'fallback:') {
            $novo = $novo -replace '(model: zenmux/deepseek/deepseek-v4-flash-free)', '$1`nfallback: [zenmux/z-ai/glm-5.2-free]'
        }
        Set-Content $arq -Value $novo
        Write-Host "✅ ALTERADO: $arq"
        $trocados++
    } else {
        Write-Host "⏭️  JA EM DEEPSEEK: $arq"
    }
}
Write-Host "`nTotal alterados: $trocados de $($arquivos.Count)"
```

---

## 🛠️ PASSO 3 — Verificar Junction Global

Depois de alterar os agentes, verifique se a junction global está refletindo as mudanças:

```powershell
# A junction de skills aponta para multi-agent/.opencode/skills/
Get-Item "$env:USERPROFILE\.config\opencode\skills" | Select-Object LinkType, Target

# A junction de agents aponta para max-thinking-system/.opencode/agents/  
Get-Item "$env:USERPROFILE\.config\opencode\agents" | Select-Object LinkType, Target

# Confirmar que as skills junctionadas sao as mesmas
(Get-ChildItem "$env:USERPROFILE\.config\opencode\skills" -Directory).Count
(Get-ChildItem "$root\multi-agent\.opencode\skills" -Directory).Count
```

Se estiver tudo junctionado corretamente, as mudanças nos arquivos fonte refletem automaticamente no global.

---

## ✅ PASSO 4 — Checklist de Verificação

```powershell
$root = "C:\Users\User\Desktop\COISAS JOAO\skills pastas melhorias agentes"

Write-Host "=== VERIFICACAO FINAL ==="

# 1. Config global
$config = Get-Content "$env:USERPROFILE\.config\opencode\opencode.json" -Raw
if ($config -match '"model":\s*"zenmux/deepseek/deepseek-v4-flash-free"') {
    Write-Host "✅ opencode.json model = DeepSeek" -ForegroundColor Green
} else {
    Write-Host "❌ opencode.json model NAO é DeepSeek" -ForegroundColor Red
}

# 2. DeepSeek no provider zenmux
if ($config -match '"deepseek/deepseek-v4-flash-free"') {
    Write-Host "✅ DeepSeek registrado no provider zenmux" -ForegroundColor Green
} else {
    Write-Host "❌ DeepSeek NAO esta no provider zenmux" -ForegroundColor Red
}

# 3. Agentes (18 arquivos)
$bugs = 0
$pastas = @(
    "$root\max-thinking-system\.opencode\agents\main",
    "$root\max-thinking-system\.opencode\agents\specialists",
    "$root\decision-system\.opencode\agents\decision-makers",
    "$root\decision-system\.opencode\agents\specialists"
)
foreach ($p in $pastas) {
    Get-ChildItem $p -Filter "*.md" | ForEach-Object {
        $c = Get-Content $_.FullName -Raw
        if ($c -match 'model:\s*tokenrouter') { Write-Host "❌ AINDA MiniMax: $($_.FullName)"; $bugs++ }
        if ($c -match 'model:\s*openrouter') { Write-Host "❌ AINDA OpenRouter: $($_.FullName)"; $bugs++ }
    }
}
if ($bugs -eq 0) { Write-Host "✅ Todos os 18 agentes em DeepSeek" -ForegroundColor Green }
else { Write-Host "❌ $bugs agentes ainda nao migrados" -ForegroundColor Red }

# 4. Skills na junction com modelo antigo
$skillsDir = "$root\multi-agent\.opencode\skills"
$skillsBugs = 0
Get-ChildItem $skillsDir -Directory | ForEach-Object {
    $sp = "$($_.FullName)\SKILL.md"
    if (Test-Path $sp) {
        $c = Get-Content $sp -Raw
        # So verifica frontmatter
        if ($c -match '^---\s*\n(.*?)\n---') {
            $fm = $matches[1]
            if ($fm -match '(?m)^model:\s*(\S+)') {
                $model = $matches[1].Trim()
                if ($model -ne 'zenmux/deepseek/deepseek-v4-flash-free') {
                    Write-Host "❌ Skill com modelo antigo: $($_.Name) -> $model"
                    $skillsBugs++
                }
            }
        }
    }
}
if ($skillsBugs -eq 0) { Write-Host "✅ Todas as skills da junction em DeepSeek (ou sem model, usando default)" -ForegroundColor Green }
```

---

## 📌 OBSERVAÇÕES IMPORTANTES

1. **`.agents/` (935 skills)** — NENHUMA tem `model:` no frontmatter. TODAS usam o default do sistema. Quando o `opencode.json` mudar para DeepSeek (Passo 1), TODAS automaticamente passam a usar DeepSeek. **Não precisa editar nenhuma individualmente.**

2. **A junction de skills** em `~/.config/opencode/skills/` é um **reparse point real** (junction). Alterar em `multi-agent/.opencode/skills/` = altera globalmente automaticamente.

3. **A junction de agents** em `~/.config/opencode/agents/` foi **copiada** de `max-thinking-system/.opencode/agents/` (não é reparse point). Mudanças nos agentes PRECISAM ser copiadas ou refeitas na junction se quiser consistência imediata.

4. **Orquestrador Mestre** já foi criado e está funcionando com DeepSeek ✅

5. **Upload do projeto para Google Drive** está em andamento via rclone. Não interrompa.

---

*Instrução gerada em 26/06/2026 — Missão: DeepSeek V4 Flash Free em todo o ecossistema*
