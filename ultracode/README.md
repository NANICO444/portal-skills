# ultracode — As Melhores Skills de 2026

> **Curadoria das melhores skills de codificacao disponiveis em 2026.**
> Cada skill aqui documentada tem link Git e comando de instalacao.

## 📊 Relatório Completo: AI Skills 2026

O arquivo [`best_ai_skills_2.md`](best_ai_skills_2.md) contém pesquisa aprofundada de **17 categorias** de ferramentas de IA em 2026, com dados de fontes, comparações, benchmarks e recomendações por caso de uso.

**Categorias cobertas:** Raciocínio, Análise de Dados, Decisão, Geração de Código, Debugging, Conversão de Código, Pesquisa Web, Sumarização, Escrita Criativa, Tradução, Imagem, Edição Visual, Visão Computacional, Transcrição de Áudio, TTS, Chatbots, Automação de Tarefas.

## Como usar

1. Escolha a skill que precisa
2. Rode o comando de instalacao
3. Reinicie o OpenCode
4. Use a skill: `use skill:nome-da-skill`

## Skills Instaladas (10 ativas + 5 skills próprias)

### 🚀 Plugin (instalar como plugin, nao como skill)

| Skill | Descricao | Comando |
|-------|-----------|---------|
| [superpowers](superpowers/) | Metodologia completa: planejamento, TDD, revisao com sub-agentes | `Fetch and follow instructions from https://raw.githubusercontent.com/obra/superpowers/refs/heads/main/.opencode/INSTALL.md` |

### 🐍 Python

| Skill | Descricao | Comando |
|-------|-----------|---------|
| [python-pro](python-pro/) | Python 3.12+, async, uv, ruff, FastAPI | `npx skills add https://github.com/rmyndharis/antigravity-skills --skill python-pro` |

### ⚛️ Frontend

| Skill | Descricao | Comando |
|-------|-----------|---------|
| [react-best-practices](react-best-practices/) | Vercel oficial: performance, RSC, SSR para React/Next.js | `npx skills add https://github.com/vercel-labs/agent-skills --skill react-best-practices` |
| [frontend-design](frontend-design/) | Anthropic: design de UI anti-slop para React/Vue/HTML/CSS | `npx skills add https://github.com/anthropics/skills --skill frontend-design` |

### 🛠️ Anthropic Skills (oficiais)

| Skill | Descricao | Comando |
|-------|-----------|---------|
| [skill-creator](skill-creator/) | Cria, testa e melhora outras skills (com avaliacoes) | `npx skills add https://github.com/anthropics/skills --skill skill-creator` |
| [mcp-builder](mcp-builder/) | Guia para criar servidores MCP em TS/Python com Zod/Pydantic | `npx skills add https://github.com/anthropics/skills --skill mcp-builder` |
| [webapp-testing](webapp-testing/) | Tests E2E com Playwright + Python para webapps | `npx skills add https://github.com/anthropics/skills --skill webapp-testing` |

### ☁️ Cloud

| Skill | Descricao | Comando |
|-------|-----------|---------|
| [cloudflare](cloudflare/) | Workers, Pages, D1, R2, KV, Durable Objects, AI | `npx skills add https://github.com/cloudflare/skills` |

### 🔌 Integracao

| Skill | Descricao | Comando |
|-------|-----------|---------|
| [composio](composio/) | Integra OpenCode a 1000+ SaaS (Gmail, Notion, GitHub, etc) | `npx skills add composiohq/skills` + CLI |

### ✍️ Qualidade de Texto

| Skill | Descricao | Comando |
|-------|-----------|---------|
| [stop-slop](stop-slop/) | Remove AI-isms, em dashes, frases genericas de textos | `git clone https://github.com/hardikpandya/stop-slop.git ~/.agents/skills/stop-slop` |

## 🏗️ Skills Próprias (ex-placeholders, agora preenchidos com SKILL.md real)

Os placeholders foram preenchidos com SKILL.md completos e prontos para uso em qualquer projeto OpenCode. Basta copiar para `~/.config/opencode/skills/`.

| Pasta | Tamanho | Arquitetura | Frameworks |
|-------|---------|-------------|------------|
| [placeholders/java-enterprise](placeholders/java-enterprise/) | SKILL.md ~25KB | 3-layer (Controller→Service→Repository) | Spring Boot 3.x, Jakarta EE, JPA, Spring Security |
| [placeholders/csharp-dotnet](placeholders/csharp-dotnet/) | SKILL.md ~25KB | Clean/MediatR + Minimal APIs | .NET 10, EF Core 10, Aspire, OpenTelemetry |
| [placeholders/go-microservices](placeholders/go-microservices/) | SKILL.md ~22KB | Clean/Hexagonal (Handler→Service→Repo) | Chi/Gin, gRPC, SQLx, Tokio, Docker |
| [placeholders/rust-systems](placeholders/rust-systems/) | SKILL.md ~24KB | Axum Handlers→Services→DB | Tokio, Axum, Tonic, SQLx, Clap, Tracing |
| [placeholders/kotlin-android](placeholders/kotlin-android/) | SKILL.md ~26KB | MVVM + Clean (UI→VM→UC→Repo→DS) | Jetpack Compose, Hilt, Room, Retrofit, MD3 |

## Instalacao das Skills Proprias

As 5 skills abaixo estao completas e prontas para uso. Basta copiar:

```bash
# Criar diretorios
mkdir -p ~/.config/opencode/skills/java-enterprise
mkdir -p ~/.config/opencode/skills/csharp-dotnet
mkdir -p ~/.config/opencode/skills/go-microservices
mkdir -p ~/.config/opencode/skills/rust-systems
mkdir -p ~/.config/opencode/skills/kotlin-android

# Copiar skills
cp ultracode/placeholders/java-enterprise/SKILL.md ~/.config/opencode/skills/java-enterprise/
cp ultracode/placeholders/csharp-dotnet/SKILL.md ~/.config/opencode/skills/csharp-dotnet/
cp ultracode/placeholders/go-microservices/SKILL.md ~/.config/opencode/skills/go-microservices/
cp ultracode/placeholders/rust-systems/SKILL.md ~/.config/opencode/skills/rust-systems/
cp ultracode/placeholders/kotlin-android/SKILL.md ~/.config/opencode/skills/kotlin-android/
```

Ou use junctions (Windows):
```powershell
New-Item -ItemType Junction -Path "$env:USERPROFILE\.config\opencode\skills\java-enterprise" -Target "$PWD\ultracode\placeholders\java-enterprise"
New-Item -ItemType Junction -Path "$env:USERPROFILE\.config\opencode\skills\csharp-dotnet" -Target "$PWD\ultracode\placeholders\csharp-dotnet"
New-Item -ItemType Junction -Path "$env:USERPROFILE\.config\opencode\skills\go-microservices" -Target "$PWD\ultracode\placeholders\go-microservices"
New-Item -ItemType Junction -Path "$env:USERPROFILE\.config\opencode\skills\rust-systems" -Target "$PWD\ultracode\placeholders\rust-systems"
New-Item -ItemType Junction -Path "$env:USERPROFILE\.config\opencode\skills\kotlin-android" -Target "$PWD\ultracode\placeholders\kotlin-android"
```

## Instalacao em Lote (externas)

Para instalar todas as skills externas principais de uma vez:

```bash
# Python
npx skills add https://github.com/rmyndharis/antigravity-skills --skill python-pro

# React/Next
npx skills add https://github.com/vercel-labs/agent-skills --skill react-best-practices

# Anthropic skills (5)
npx skills add https://github.com/anthropics/skills --skill skill-creator
npx skills add https://github.com/anthropics/skills --skill frontend-design
npx skills add https://github.com/anthropics/skills --skill mcp-builder
npx skills add https://github.com/anthropics/skills --skill webapp-testing

# Cloudflare
npx skills add https://github.com/cloudflare/skills

# Composio
npx skills add composiohq/skills
curl -fsSL https://composio.dev/install | bash
composio login
composio init

# Superpowers (plugin separado)
Fetch and follow instructions from https://raw.githubusercontent.com/obra/superpowers/refs/heads/main/.opencode/INSTALL.md

# Stop Slop
mkdir -p ~/.agents/skills && git clone https://github.com/hardikpandya/stop-slop.git ~/.agents/skills/stop-slop
```

## Relacao com skills ja instaladas

Estas skills de ultracode **podem complementar** skills ja existentes no projeto, ou **substituir** se voce preferir padronizar.

| Skill ultracode | Skills similares ja no projeto | Recomendacao |
|-----------------|--------------------------------|--------------|
| `python-pro` | `python-testing`, `python-async-patterns` | Usar `python-pro` como padrao, manter as outras como referencia |
| `react-best-practices` | `frontend-patterns`, `react-doctor`, `taste-skill` | Mais autoritativo para Next.js |
| `frontend-design` | `taste-skill`, `design-brief`, `minimalist-skill` | Complementar, nao substituir |
| `webapp-testing` | `test-driven-development`, `python-testing` | Adiciona E2E (complementar) |
| `mcp-builder` | (nenhuma) | Skill NOVA |
| `skill-creator` | (nenhuma) | Skill NOVA |
| `stop-slop` | `anti-glaze` | `stop-slop` = texto, `anti-glaze` = UX |
| `superpowers` | `code-review`, `plan`, `tDD` | SUBSTITUI (decida se quer padronizar) |
| `cloudflare` | (nenhuma) | Skill NOVA |
| `composio` | MCPs manuais em `mcp.json` | SUBSTITUI varios MCPs |
| **Skills proprias** | | |
| `java-enterprise` | (nenhuma no projeto) | Skill NOVA — Spring Boot corporativo |
| `csharp-dotnet` | (nenhuma no projeto) | Skill NOVA — .NET 10 moderno |
| `go-microservices` | (nenhuma no projeto) | Skill NOVA — Go cloud-native |
| `rust-systems` | (nenhuma no projeto) | Skill NOVA — Rust seguro |
| `kotlin-android` | (nenhuma no projeto) | Skill NOVA — Android moderno |

## Configuracao pos-instalacao

Apos instalar `superpowers`, adicione em `~/.config/opencode/opencode.jsonc`:

```jsonc
{
  "plugin": [
    "superpowers"
  ]
}
```

## Pre-requisitos

- `npx` (Node.js 18+)
- `git` para stop-slop
- `curl` para Composio
- Para Python: `uv` (https://docs.astral.sh/uv/)
- Para Cloudflare: conta Cloudflare + `wrangler` CLI

## Como contribuir

1. Encontrou uma skill nova? Adicione aqui
2. Atualizou uma skill? Atualize a versao
3. Encontrou um bug? Documente na pasta
