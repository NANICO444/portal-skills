# HANDFOFF — Manual do Sucessor

> Gerado em: 25/06/2026
> Propósito: Documentar todo o ecossistema OpenCode para o próximo sucessor

---

## 📂 ESTRUTURA DO PROJETO (25 entradas na raiz)

```
📁 C:\Users\User\Desktop\COISAS JOAO\skills pastas melhorias agentes\
```

| # | Pasta/Arquivo | Descrição |
|---|---------------|-----------|
| 1 | `.agents/` | Coleção bruta de skills (~935 diretórios). Repositório raw do ecossistema Vercel Labs. |
| 2 | `.kiro/` | Sistema Kiro (Aurora + Hefesto). 62 skills, hooks, steering. **NÃO TOCAR.** |
| 3 | `.opencode/` | Config OpenCode local do projeto (node_modules se houver, package.json). |
| 4 | `agents/` | `best_agent_frameworks.md` + README sobre frameworks de agentes. |
| 5 | `decision-system/` | 16 agentes, 3 skills de decisão (`decision-skills`, `decision-system-master`, `ultra-powerful`). |
| 6 | `docs/` | Documentação geral do ecossistema. |
| 7 | `max-thinking-system/` | 12 agentes com `variant: max`, 6 skills de pensamento profundo. |
| 8 | `models/` | `free_models_report.md` — relatório de modelos gratuitos. |
| 9 | `multi-agent/` | Junction global. 2 servidores headless, **181 skills** (+1 = 182). |
| 10 | `oh-my-openagent/` | Projeto openagent completo. Plugin profissional OpenCode. **NÃO TOCAR.** |
| 11 | `prompts/` | 7 prompts de sistema. |
| 12 | `referencias_originais/` | Aurora + Hefesto originais (backup histórico). **NÃO TOCAR.** |
| 13 | `skills_github/` | 4 repositórios clonados (impeccable, taste-skill, etc.). |
| 14 | `skills_refinadas/` | Skills refinadas manualmente. |
| 15 | `SKILLS/` | `agent-skills-report.md` + reports individuais de skills. |
| 16 | `templates/` | 9 templates de projeto (React, Next.js, Vue, etc.). |
| 17 | `ultracode/` | 10 skills custom + `placeholders/` (diretório reserva). |
| 18 | `ULTRA_PROMPT_ANTIGRAVITY/` | Core Antigravity v7 — 49 agentes, módulos, skills. **NÃO TOCAR.** |
| 19 | `ARCHITECTURE.md` | Documento de arquitetura do ecossistema. |
| 20 | `INDEX.md` | Índice das 50 skills mais úteis de 181, organizadas por cenário. |
| 21 | `NOVO_ULTRA_PROMPT_PROJETOS.md` | Prompt guia para projetos (~13MB). |
| 22 | `README.md` | Leia-me principal. |
| 23 | `SOBRE.html` | Página HTML sobre o projeto. |
| 24 | `WORKFLOWS.md` | Documento de workflows. |
| 25 | `INSTRUCAO_SUCESSOR_LIMPEZA.md` | Instruções para esta sessão de trabalho. |

---

## 🧠 SISTEMAS CRIADOS

### multi-agent/ — Sistema Multi-Agente Principal
| Item | Valor |
|------|-------|
| **O que faz** | 2 servidores headless (portas 3001, 3002), 182 skills |
| **Skills** | `multi-agent/.opencode/skills/` — junction global |
| **Agentes Agent 1** (north-mini-code-free): orquestrador, code-reviewer, testador, debugger, refatorador, security-auditor, otimizador |
| **Agentes Agent 2** (gpt-oss-120b:free): orquestrador-conhecimento, pesquisador, documentador, arquiteto, devops |
| **Junction** | `~/.config/opencode/skills/` → `.../multi-agent/.opencode/skills/` (junction real, confirmada via fsutil) |

### decision-system/ — Sistema de Decisão Rápida
| Item | Valor |
|------|-------|
| **O que faz** | 6 decisores primários + 10 sub-agentes, 3 skills de decisão |
| **Skills** | `decision-system/.opencode/skills/` |
| **Skills disponíveis** | `decision-system-master`, `decision-skills`, `ultra-powerful` |
| **Modelo padrão** | MiniMax-M3 (via tokenrouter) — tem API key configurada |
| **Observação** | Skills estão incompletas (2 sem SKILL.md, 1 sem model field) |

### max-thinking-system/ — Sistema de Pensamento Profundo
| Item | Valor |
|------|-------|
| **O que faz** | 12 agentes com `variant: max`, 6 skills, pensamento ultra-profundo |
| **Skills** | `max-thinking-system/.opencode/skills/` — 6 skills |
| **Agentes** | `max-thinking-system/.opencode/agents/` — 8 agentes |
| **Agentes disponíveis** | `code-review`, `deep-analysis`, `fix-suggester`, `library-curator`, `max-thinking`, `supervisor`, `main`, `specialists` |
| **Junction agents** | `~/.config/opencode/agents/` → `.../max-thinking-system/.opencode/agents/` |
| **Modelo padrão** | MiniMax-M3 (tokenrouter) / DeepSeek (openrouter) — misturado |

### ultracode/ — Skills Custom
| Item | Valor |
|------|-------|
| **O que faz** | 10 skills custom + `placeholders/` |
| **Skills** | `cloudflare`, `composio`, `frontend-design`, `mcp-builder`, `python-pro`, `react-best-practices`, `skill-creator`, `stop-slop`, `superpowers`, `webapp-testing` |
| **Observação** | Nenhuma tem modelo explícito no frontmatter. `placeholders/` e `superpowers/` não têm SKILL.md. |

---

## ⚙️ CONFIGURAÇÃO GLOBAL

### Arquivo: `~/.config/opencode/opencode.json`

```json
{
  "model": "zenmux/z-ai/glm-5.2-free",
  "small_model": "zenmux/stepfun/step-3.7-flash-free"
}
```

### Provedores Configurados

| Provedor | Tipo | Modelos |
|----------|------|---------|
| **tokenrouter** | OpenAI-compatible | Minimax-M3 (com API key) |
| **meuprovedor** | B.AI (tokenrouter) | Minimax-M3 |
| **meu** | tokenrouter custom | Minimax-M3 |
| **zenmux** | Proxy multi-modelo | 7 modelos FREE: GLM 5.2 Free (1M ctx), Step 3.7 Flash Free, Kimi K2.7 Code Free, Xiaomi MiMo V2 Flash Free, GLM 4.6V Flash Free, KAT Coder Pro V1 Free, Gemini 3 Flash Preview Free (1M ctx) |

### Regras Globais

| Arquivo | Descrição |
|---------|-----------|
| `~/.config/opencode/rules/always-delegate.md` | Regra permanente: classificar tarefa → escolher sistema → delegar → supervisionar |
| `~/.config/opencode/rules/main` | Regras principais |
| `~/.config/opencode/rules/specialists` | Regras para especialistas |

### Regra Permanente (always-delegate.md)
- **SEMPRE** classifique a tarefa primeiro
- **NUNCA** execute tarefa técnica diretamente — delegue
- **SEMPRE** carregue a skill relevante antes de responder
- **SEMPRE** chame @supervisor depois de qualquer código

---

## 🔗 JUNCTIONS ATIVAS

| Ponto de Junção | Destino | Tipo |
|-----------------|---------|------|
| `~/.config/opencode/skills/` | `.../multi-agent/.opencode/skills/` | Junction (reparse point) |
| `~/.config/opencode/agents/` | `.../max-thinking-system/.opencode/agents/` | Copiado (não junction) |
| `~/.config/opencode/rules/always-delegate.md` | Arquivo físico direto | Arquivo direto |

> **Nota:** A junction de skills é real (confirmada via `fsutil reparsepoint`). Alterar em `multi-agent/.opencode/skills/` = alterar globalmente.

---

## 🚫 PASTAS QUE NÃO PODEM SER TOCADAS

| Pasta | Motivo |
|-------|--------|
| `.kiro/` | Sistema Kiro original (Aurora + Hefesto). Integridade do ecossistema. |
| `ULTRA_PROMPT_ANTIGRAVITY/` | Core Antigravity v7 — orquestração Nexus. |
| `oh-my-openagent/` | Projeto completo externo, plugin profissional OpenCode. |
| `referencias_originais/` | Backup histórico dos originais Aurora + Hefesto. |

---

## 📋 COMANDOS ÚTEIS

```powershell
# Listar modelos disponíveis
opencode models zenmux

# Ver junction de skills
fsutil reparsepoint query "$env:USERPROFILE\.config\opencode\skills"

# Contar skills no junction global
(Get-ChildItem "$env:USERPROFILE\.config\opencode\skills" -Directory).Count

# Contar skills no multi-agent
(Get-ChildItem "multi-agent/.opencode/skills" -Directory).Count

# Listar skills com modelo específico
Get-ChildItem "multi-agent/.opencode/skills" -Directory | ForEach-Object {
    $p = "$($_.FullName)\SKILL.md"
    if (Test-Path $p) {
        $c = Get-Content $p -Raw
        if ($c -match "model:\s*(\S+)") { [PSCustomObject]@{Skill=$_.Name; Model=$matches[1]} }
    }
}

# Ver junction da raiz
Get-Item "$env:USERPROFILE\.config\opencode\skills" | Select-Object LinkType, Target
```

---

## 🗺️ MAPA DE DECISÃO DE SISTEMA

```
Usuário pergunta algo?
├── É código (feature, bug, teste, refatorar)?
│   └── ➡️ multi-agent (via @orquestrador)
├── É decisão (stack, custo, risco, estratégia)?
│   └── ➡️ decision-system (via decision-system-master)
├── É análise profunda (investigar, arquitetura, planejar)?
│   └── ➡️ max-thinking-system (via agente especialista)
└── É design/UX?
    └── ➡️ max-thinking-system (skills de design)
```

---

## 📊 RESUMO DE SKILLS POR SISTEMA

| Sistema | Skills | Agentes | Modelo Padrão |
|---------|--------|---------|---------------|
| multi-agent (junction global) | 182 | 12 (2 servidores) | Misto (ver Missão 3) |
| decision-system | 3 | 16 | MiniMax-M3 |
| max-thinking-system | 6 | 12 (8 na pasta) | MiniMax-M3 / DeepSeek |
| ultracode | 11 pastas (10 skills) | — | Nenhum explícito |
| .agents (raw) | ~935 | — | N/A |
| .kiro | 62 | — | N/A |
| **TOTAL (aproximado)** | **~1.200 skills** | **~40 agentes** | — |

---

## ⚠️ PONTOS DE ATENÇÃO

1. **DeepSeek ainda não é o modelo padrão global** — config atual usa `zenmux/z-ai/glm-5.2-free`. Pendente (Missão 3).
2. **DeepSeek não está no `opencode.json`** — precisa ser adicionado ao zenmux se for usar `zenmux/deepseek/deepseek-v4-flash-free`.
3. **Catálogo de skills não existe** — precisa ser gerado (Missão 5).
4. **`master-orquestrador` já existe** — mas é sobre servidores headless antigos. Não é o meta-agent da Missão 4.
5. **Decision-system skills estão incompletas** — `decision-skills` e `ultra-powerful` não têm SKILL.md.
6. **A junction de agents NÃO é junction real** — foi copiada, não linkada via reparse point.

---

*Este documento foi gerado automaticamente pelo sucessor em 25/06/2026 como parte das 4 missões de organização do ecossistema.*
