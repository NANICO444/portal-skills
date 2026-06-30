# Agent Skills Report 2026

> **Pesquisa aprofundada sobre skills para codificar com agentes e construir/orquestrar agentes inteligentes.**
>
> Data: 19 Jun 2026 | Fontes: 30+ artigos, repositórios e documentações consultados

---

## Sumário Executivo

O ecossistema de **Agent Skills** explodiu em 2025–2026. O que começou como arquivos `SKILL.md` avulsos evoluíu para:

- **Coleções workflow** (Superpowers, GSD, gstack) — frameworks completos de metodologia de desenvolvimento
- **Coleções de engenharia** (addyosmani/agent-skills, mattpocock/skills) — skills modulares para TDD, debug, review, planejamento
- **Skills por framework/stack** (antfu/skills para Vue, AWS Agent Toolkit, vuejs-ai/skills) — conhecimento atualizado de APIs e boas práticas
- **Ferramentas geradoras** (Skilld, TanStack Intent) — skills geradas automaticamente de dependências NPM
- **Habilidades metodológicas** — problem shaping, context design, aesthetic judgment, agent orchestration

Este relatório documenta **cada coleção**, **cada skill relevante**, **comandos de instalação**, e as **competências metodológicas** essenciais para 2026.

---

## Parte 1: Coleções de Skills Populares

### 1.1 Superpowers (`obra/superpowers`)

| Atributo | Detalhe |
|----------|---------|
| **GitHub** | [obra/superpowers](https://github.com/obra/superpowers) |
| **Estrelas** | ~226K (a maior do ecossistema) 【14†L21-L26】 |
| **Licença** | MIT |
| **Agentes** | Claude Code, Codex, Cursor, Gemini CLI, OpenCode, Pi, Kiro, +6 |
| **Instalação** | `npx skills add obra/superpowers` ou `git clone` + setup script |

**O que faz:** Metodologia completa de desenvolvimento orientada por especificação (Spec-Driven Development). Força definição de requisitos antes de gerar código, através de 6 fases que encadeiam automaticamente:

1. **brainstorming** — Refina ideias através de perguntas socráticas, salva design doc
2. **using-git-worktrees** — Cria worktree isolado com baseline de testes limpo
3. **writing-plans** — Decompõe em tarefas de 2-5 minutos com caminhos exatos e código
4. **subagent-driven-development** ou **executing-plans** — Dispara subagente por tarefa com revisão de 2 estágios
5. **test-driven-development** — RED-GREEN-REFACTOR: teste falha → código mínimo → commit
6. **finishing-a-development-branch** — Verifica testes, oferece merge/PR/keep/discard

**Skills incluídas:** brainstorming, using-git-worktrees, writing-plans, test-driven-development, subagent-driven-development, requesting-code-review, receiving-code-review, verification-before-completion, systematic-debugging, finishing-a-development-branch, dispatching-parallel-agents, writing-skills, using-superpowers

**Quando usar:** Ideal para desenvolvedores solo que precisam de disciplina de testes e processo estruturado. Melhor relação sinal/ruído para TDD e delegação por subagentes.【4†L33-L47】

**Trade-offs:** Foco exclusivo na fase de construção — não cobre decisão estratégica (gstack) nem contexto de longa duração (GSD).【11†L30-L35】

---

### 1.2 Karpathy Guidelines (`multica-ai/andrej-karpathy-skills`)

| Atributo | Detalhe |
|----------|---------|
| **GitHub** | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) |
| **Estrelas** | ~174K 【14†L21-L26】 |
| **Licença** | MIT |
| **Tamanho** | ~1 arquivo (~30 linhas de regras comportamentais) |

**O que faz:** Conjunto curto de regras comportamentais derivadas de um post de Andrej Karpathy sobre os 4 modos de falha de LLMs:【14†L36-L41】

1. **Think before you code** — Não comece a codar sem entender o problema
2. **Simplicity first** — Resista overengineering; resolva o problema da forma mais simples
3. **Surgical changes** — Edite só o necessário, não faça mudanças ortopédicas
4. **Goal-driven execution** — Foque no objetivo, não em features especulativas

**Instalação:** `npx skills add multica-ai/andrej-karpathy-skills` ou clone para `.claude/skills/`

**Quando usar:** Como **regra global** (`alwaysApply: true`) em qualquer projeto. Funciona como foundation layer — não substitui workflows completos, mas disciplina o comportamento do agente.【10†L20-L24】

**Trade-offs:** É curto demais para ser um framework completo; precisa ser combinado com Superpowers, gstack ou GSD para projetos complexos.【11†L17-L24】

---

### 1.3 Matt Pocock Skills (`mattpocock/skills`)

| Atributo | Detalhe |
|----------|---------|
| **GitHub** | [mattpocock/skills](https://github.com/mattpocock/skills) |
| **Estrelas** | ~136K (Jun 2026) 【17†L22-L27】 |
| **Licença** | MIT |
| **Versão** | v1.0.1 (17 Jun 2026) |
| **Instalação** | `npx skills@latest add mattpocock/skills` |

**O que faz:** Skills para engenheiros reais ("not vibe coding"). Focado em corrigir modos de falha comuns de coding agents através de skills modulares e composáveis.【18†L1-L5】

**Skills principais (v1.0.1):**

| Skill | Tipo | Propósito |
|-------|------|-----------|
| `ask-matt` | Router | Pergunta qual skill usar para cada situação |
| `grill-with-docs` | Interrogatório | Grilling + domain model + ADRs + CONTEXT.md |
| `to-prd` | Documentação | Conversa → PRD → issue tracker |
| `to-issues` | Decomposição | Plano grande → issues independentes |
| `tdd` | Disciplina | RED-GREEN-REFACTOR em vertical slices |
| `diagnosing-bugs` | Debug | reproduce → minimise → hypothesise → instrument → fix |
| `domain-modeling` | Design | Glossário, linguagem ubíqua, bounded contexts |
| `codebase-design` | Arquitetura | Módulos profundos, seams, adapters |
| `triage` | PM | State machine de issues |
| `improve-codebase-architecture` | Refatoração | Scan → HTML report → grill |
| `prototype` | Exploração | Protótipo descartável |
| `git-guardrails-claude-code` | Segurança | Bloqueia git push --force, reset --hard, clean |

**Taxonomia:** User-invoked (orchestrate) vs Model-invoked (discipline). Skills como `tdd` e `codebase-design` são invocadas pelo modelo automaticamente; `/grill-me`, `/to-prd` são invocadas pelo usuário. 【19†L32-L38】

**Setup:** Rodar `/setup-matt-pocock-skills` uma vez por repo — configura issue tracker (GitHub/Linear/local), labels de triagem, e local de docs.

**Quando usar:** Ideal para engenheiros TypeScript/full-stack que querem controle fino sem framework pesado. "Pocock construiu estas skills para corrigir modos de falha — não para substituir seu julgamento por um processo heavyweight."【19†L34-L38】

**Trade-offs:** Skills que assumem GitHub ou Linear (`to-issues`, `to-prd`, `triage`) podem precisar adaptação para outras ferramentas. É uma coleção pessoal — reflete o workflow do Matt.【20†L50-L54】

---

### 1.4 GStack (`garrytan/gstack`)

| Atributo | Detalhe |
|----------|---------|
| **GitHub** | [garrytan/gstack](https://github.com/garrytan/gstack) |
| **Estrelas** | ~110K 【14†L42-L47】 |
| **Licença** | MIT |
| **Agentes** | Claude Code, Codex, Cursor, Kiro, +4 |
| **Instalação** | `git clone` + `./setup.sh --host kiro` (ou `cursor`, `opencode`, etc.) |

**O que faz:** Transforma o agente em um time de engenharia virtual com 23 papéis especializados, cada um com seu próprio slash command: CEO, Designer, Eng Manager, Release Manager, QA Lead, Security Officer, Staff Engineer, etc.【10†L1-L8】

**Skills principais:**

| Comando | Papel | O que faz |
|---------|-------|-----------|
| `/office-hours` | YC Partner | 6 forcing questions que reframam o produto |
| `/design-review` | Designer que Coda | Audita + corrige design, commits atômicos |
| `/review` | Staff Engineer | Encontra bugs que passam CI mas quebram em produção |
| `/investigate` | Debugger | Root-cause debugging sistemático |
| `/qa` | QA Lead | Testa em browser real, encontra bugs, fix + test |
| `/ship` | Release Engineer | Sync, testa, faz PR, merge, canary |
| `/retro` | Retrospective | Extrai aprendizados, alimenta próximo ciclo |

**Integração com Karpathy:** gstack implementa os 4 modos de falha do Karpathy forçadamente — `/office-hours` expõe assumptions, `/review` pega complexidade desnecessária, `/ship` transforma tarefas em objetivos verificáveis com test-first.【10†L53-L60】

**Quando usar:** Founder-engineers shipping produto. Melhor para tomada de decisão multi-perspectiva (CEO + designer + eng + QA + security).【11†L36-L42】

**Trade-offs:** É orientado a papéis (quem decide), não a fases do processo. A parte de "escrever código em si" é mais fraca comparada a Superpowers. Requer vários ciclos de interação para completar uma tarefa.【11†L36-L42】

---

### 1.5 GSD Core (`open-gsd/gsd-core`)

| Atributo | Detalhe |
|----------|---------|
| **GitHub** | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) |
| **Estrelas** | ~51K (GSD 2) + ~4.2K (gsd-core) |
| **Licença** | MIT |
| **Agentes** | Claude Code, OpenCode, Gemini CLI, Kilo, Codex, Copilot, Cursor, Windsurf, +6 |
| **Instalação** | `npx gsd@latest init` (prompts para runtime + global/local) |
| **Homepage** | [opengsd.net](https://opengsd.net) |

**O que faz:** Sistema de context-engineering e spec-driven development que resolve **context rot** — a degradação de qualidade conforme o contexto enche. Sua ideia central: trabalho pesado (research, plan, execute) roda em **subagentes com contexto fresco**, enquanto o orquestrador principal se mantém leve.【22†L7-L13】

**Fase loop (5 passos por milestone):**

1. **Discuss** — Captura decisões de implementação antes de planejar
2. **Plan** — Pesquisa, decompõe, verifica se o plano cabe em contexto fresco
3. **Execute** — Planos executados em ondas paralelas; cada executor começa com 200K tokens limpos
4. **Verify** — Walk-through do que foi construído, diagnostica e corrige
5. **Ship** — Cria PR, arquiva fase, repete

**Namespace meta-skills (v1.40+):** `/gsd-workflow`, `/gsd-project`, `/gsd-quality`, `/gsd-context`, `/gsd-manage`, `/gsd-ideate` — 6 roteadores que mantêm o custo de listagem inicial baixo (~120 tokens vs ~2.150 para lista plana de 86 skills).【23†L18-L28】

**Context engineering:** Artefatos como `STATE.md`, `CONTEXT.md`, `.planning/` sobrevivem entre sessões. Cada subagente recebe contexto isolado via filesystem. "O orquestrador — sua sessão principal — nunca toca em arquivos fonte. Ele spawna agentes, coleta resultados, atualiza estado."【22†L38-L49】

**Quando usar:** Projetos complexos que duram dias ou semanas. Sessões longas (marathon sessions). Múltiplas workstreams paralelas. Qualquer cenário onde context rot é um risco real.【11†L30-L35】

**Trade-offs:** Overhead para tarefas pequenas. Curva de aprendizado maior que Superpowers ou gstack. Não tem separação de papéis (diferente de gstack). "Usado sozinho, não produz código diretamente — é um estabilizador, não um builder."【11†L43-L48】

---

### 1.6 Addy Osmani Agent Skills (`addyosmani/agent-skills`)

| Atributo | Detalhe |
|----------|---------|
| **GitHub** | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) |
| **Estrelas** | ~49.9K (Jun 2026) |
| **Licença** | MIT |
| **Skills** | 24 (23 lifecycle + 1 meta-skill) |
| **Slash commands** | 7: `/spec`, `/plan`, `/build`, `/test`, `/review`, `/code-simplify`, `/ship` |
| **Instalação** | `npx skills add addyosmani/agent-skills` ou plugin Claude Code |

**O que faz:** Skills de engenharia production-grade que codificam workflows, quality gates e melhores práticas que engenheiros seniors usam. Inspirado nas práticas de engenharia do Google (Hyrum's Law, Beyonce Rule, Chesterton's Fence, trunk-based development).【26†L3-L10】【27†L33-L40】

**Ciclo de vida completo (DEFINE → PLAN → BUILD → VERIFY → REVIEW → SHIP):**

| Estágio | Skills |
|---------|--------|
| DEFINE | idea-refine, spec-driven-development |
| PLAN | planning-and-task-breakdown |
| BUILD | incremental-implementation, TDD, context-engineering, frontend-ui, API design |
| VERIFY | browser-testing, debugging-and-error-recovery |
| REVIEW | code-review, code-simplification, security, performance |
| SHIP | git-workflow, CI/CD, deprecation, documentation, shipping |

**Diferencial:** Cada skill termina com **exit criteria** — requisitos de evidência (testes passando, security scan reports, etc.). Inclui **anti-rationalization tables**: réplicas pré-construídas para as desculpas que agentes inventam para pular etapas.【29†L1-L5】

**Metaskill:** `using-agent-skills` — árvore de decisão task→skill que roteia qualquer requisição para a skill certa.

**Quando usar:** Qualquer projeto que precise de disciplina de engenharia. Melhor para teams adotando coding agents em codebases de produção. "Skills ensinam o 'como' (processo), enquanto frameworks ensinam o 'o quê' (contexto)."【28†L18-L24】

**Trade-offs:** Skills são starting points — precisam adaptação para convenções do time. A popularidade do repo não substitui validação no seu workflow.【28†L44-L50】

---

### 1.7 Anthropic Official Skills (`anthropics/skills`)

| Atributo | Detalhe |
|----------|---------|
| **GitHub** | [anthropics/skills](https://github.com/anthropics/skills) |
| **Licença** | Apache 2.0 (maioria) + Source-available (docx, pdf, pptx, xlsx) |
| **Instalação** | `/plugin marketplace add anthropics/skills` → `/plugin install document-skills@anthropic-agent-skills` |

**O que faz:** Skills oficiais da Anthropic demonstrando o que é possível com o sistema de skills do Claude. Cobre aplicações criativas (arte, música, design), tarefas técnicas (testes web, MCP server generation), e workflows empresariais (comunicações, branding).【1†L25-L36】

**Skills de documentos (source-available):** docx, pdf, pptx, xlsx — skills usadas internamente pelo Claude para criar/editar documentos.

**Template skill:** Inclui template para criar novas skills.

**Quando usar:** Como referência de padrões e patterns para criar suas próprias skills. As skills de documentos são as mais usadas (PDF extraction, DOCX creation).

---

### 1.8 VoltAgent Awesome Agent Skills (`VoltAgent/awesome-agent-skills`)

| Atributo | Detalhe |
|----------|---------|
| **GitHub** | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) |
| **Estrelas** | ~25.9K |
| **Skills** | 1000+ (curadas, não geradas em massa) |
| **Instalação** | `npx skills add <owner>/<repo>` |
| **Homepage** | [officialskills.sh](https://officialskills.sh) |

**O que faz:** A maior coleção curada de skills do ecossistema, com skills oficiais de equipes como Anthropic, Google Labs, Vercel, Stripe, Cloudflare, Netlify, Trail of Bits, Sentry, Expo, Hugging Face, Figma, Garry Tan (gstack), Supabase, e mais.【2†L1-L8】

**Skills por categoria:**
- **Claude Skills oficiais** — template, document, pdf, etc.
- **VoltAgent** — TypeScript agent framework skills
- **Google Labs (Stitch)** — design-md, enhance-prompt
- **Supabase** — agent skills para Supabase
- **Composio** — integration skills
- **Netlify** — netlify-ai-gateway
- **Garry Tan (gstack)** — skills do gstack

**Quando usar:** Como diretório de descoberta — procurar por skills de tecnologias específicas. "Ao contrário de muitos repositórios gerados em massa, esta coleção foca em Agent Skills do mundo real criadas por times reais."【2†L14-L16】

---

## Parte 2: Skills por Stack / Framework

### 2.1 Vue / Nuxt / Vite

#### antfu/skills

| Atributo | Detalhe |
|----------|---------|
| **GitHub** | [antfu/skills](https://github.com/antfu/skills) |
| **Estrelas** | ~5K |
| **Criado por** | Anthony Fu (VueUse, Vitest, UnoCSS) |
| **Instalação** | `npx skills add antfu/skills --skill=vue` |

A coleção mais abrangente para o ecossistema Vue/Vite/Nuxt. Skills geradas da documentação oficial e ajustadas para padrões modernos:【30†L1-L10】

| Skill | Stack | Conteúdo |
|-------|-------|----------|
| `antfu` | Anthony Fu | Tooling preferences, ESLint flat config, pnpm, monorepo |
| `vue` | Vue 3 | Composition API, script setup macros, ref/shallowRef, built-in components |
| `nuxt` | Nuxt | File-based routing, server routes, modules, auto-imports, Layers |
| `pinia` | Pinia | Type-safe state management |
| `vite` | Vite | Config, plugins, SSR, library mode |
| `vitest` | Vitest | Unit testing, coverage |
| `unocss` | UnoCSS | Atomic CSS, presets, transformers |
| `vueuse-functions` | VueUse | 200+ Vue composition utilities |
| `vue-best-practices` | Vue 3 | Best practices + TypeScript |
| `pnpm` | pnpm | Fast, disk-efficient package manager |

**Instalação:**
```bash
# Todas as skills
npx skills add antfu/skills --skill='*'

# Apenas Vue
npx skills add antfu/skills --skill=vue --agent cursor
npx skills add antfu/skills --skill=vue --agent claude-code

# Como submodule (auto-update via git pull)
git submodule add https://github.com/antfu/skills .skills
```

**Diferencial:** Usa git submodules para auto-update — quando a documentação oficial atualiza, as skills são regeneradas. "A coleção de Anthony Fu regenera a partir dos source docs, então puxar a última versão geralmente pega novas APIs automaticamente."【31†L44-L47】

#### vuejs-ai/skills

| Atributo | Detalhe |
|----------|---------|
| **GitHub** | [vuejs-ai/skills](https://github.com/vuejs-ai/skills) |
| **Skills** | 8 skills focadas em boas práticas |
| **Instalação** | Plugin: `/plugin marketplace add vuejs-ai/skills` → `/plugin install vue-best-practices@vue-skills` |

Skills com avaliações (evals) rodadas em 3 modelos (haiku, sonnet, opus):【33†L35-L40】

- `vue-best-practices` — Vue 3 + Composition API + TypeScript (workflow de 5 fases)
- `vue-router-best-practices` — Navigation guards, route params
- `vue-pinia-best-practices` — Store setup, reactivity
- `vue-testing-best-practices` — Vitest, Vue Test Utils, Playwright
- `vue-debug-guides` — Runtime errors, hydration, async error handling
- `create-adaptable-composable` — MaybeRef/MaybeRefOrGetter patterns

#### vueuse/skills

| Atributo | Detalhe |
|----------|---------|
| **GitHub** | [vueuse/skills](https://github.com/vueuse/skills) |
| **Skills** | VueUse function references |
| **Instalação** | `/plugin marketplace add vueuse/skills` → `/plugin install vueuse-functions@vueuse-skills` |

**Diferencial:** Progressive disclosure — envia overview das funções VueUse primeiro, depois carrega detalhes e type declarations on demand. Offline-first, token-minimal.

---

### 2.2 AWS Agent Toolkit

| Atributo | Detalhe |
|----------|---------|
| **GitHub** | [aws/agent-toolkit-for-aws](https://github.com/aws/agent-toolkit-for-aws) |
| **Skills** | 40+ (Jun 2026, em crescimento) |
| **Plugins** | 3: aws-core, aws-agents, aws-data-analytics |
| **Instalação** | `/plugin install aws-core@claude-plugins-official` ou `npx skills add aws/agent-toolkit-for-aws/skills` |
| **MCP Server** | Gerenciado (GA desde Mai 2026) |

Skills oficiais da AWS para coding agents, lançadas em Maio 2026 como sucessoras dos MCP servers/skills do AWS Labs:【34†L1-L7】

**Plugins disponíveis:**

| Plugin | Cobertura |
|--------|-----------|
| **aws-core** | Service selection, CDK/CloudFormation, serverless, containers, storage, observability, billing, SDK usage, deployment |
| **aws-agents** | Building AI agents on AWS (Bedrock, AgentCore) |
| **aws-data-analytics** | Data lake, analytics, ETL (S3 Tables, Glue, Athena) |

**Tipos de skills:**
- **Service decision guides** — Ajudam o agente a escolher o serviço AWS certo
- **Step-by-step procedures** — Workflows testados para tarefas comuns
- **Troubleshooting guides** — Procedimentos de diagnóstico
- **SDK best practices** — Padrões corretos por linguagem

**AWS CLI Integration (desde Jun 2026):** `aws configure agent-toolkit` — setup wizard interativo que detecta coding agents instalados, instala skills default, e configura o MCP Server.【35†L17-L22】

**Diferencial:** Skills avaliadas end-to-end (não "alguém escreveu um markdown"). IAM context keys que distinguem ações de agente vs humano. CloudWatch + CloudTrail em toda request MCP.

---

### 2.3 Outras Skills por Framework

#### Google Labs (Stitch)
- `google-labs-code/design-md` — Create/manage DESIGN.md files
- `google-labs-code/enhance-prompt` — Prompt enhancement
- Instalação: `npx skills add google-labs-code/skills`

#### Netlify
- `netlify/netlify-ai-gateway` — Access AI models via unified gateway
- `netlify/skills` — Skills para deploy Netlify

#### Supabase
- Skills oficiais para Supabase (via awesome-agent-skills)

#### Stripe
- Skills oficiais da Stripe para integração de pagamentos

#### WordPress
- `WordPress/wordpress-router` — Classifica repos WordPress e roteia para workflow correto

#### Expo (React Native)
- Skills oficiais para desenvolvimento Expo/React Native

---

## Parte 3: Ferramentas para Gerar Skills Automaticamente

### 3.1 Skilld (NPM Dependency → Skills)

| Atributo | Detalhe |
|----------|---------|
| **Repo** | skilld (ecossistema NPM) |
| **Função** | Gera skills das dependências NPM do projeto |
| **Instalação** | `npm install -g skilld` |

Lê o `package.json`, consulta docs, release notes e GitHub issues de cada dependência, e gera skills que correspondem às versões instaladas. Resolve o problema de "conhecimento desatualizado do modelo": se você fez upgrade para Nuxt 4 ou Pinia 3, o modelo ainda está usando padrões antigos — Skilld gera skills atualizadas.【33†L41-L44】

**Uso:** `skilld search "useFetch options" -p nuxt` — busca entre skills instaladas.

---

### 3.2 TanStack Intent

| Atributo | Detalhe |
|----------|---------|
| **Função** | Embutir skills versionadas em bibliotecas |
| **Padrão** | Framework/biblioteca → SKILL.md empacotado |

Framework authors podem embutir skills nas suas próprias bibliotecas, garantindo que o agente sempre use as APIs corretas para a versão instalada. Exemplo: `@tanstack/react-query` poderia shipar uma skill com os patterns corretos de `useQuery`/`useMutation` para cada versão.

---

### 3.3 Template Skill (`anthropics/skills/template`)

| Atributo | Detalhe |
|----------|---------|
| **Repo** | anthropics/skills |
| **Função** | Template oficial para criar skills |

Inclui estrutura de diretório padrão (`SKILL.md`, opcionais `scripts/`, `references/`, `evals/`), frontmatter YAML, e boas práticas de descrição.

---

## Parte 4: Habilidades Metodológicas para 2026

Baseado em artigos de especialistas e pesquisa acadêmica, as seguintes habilidades são identificadas como **essenciais** para construir e orquestrar agentes em 2026:【37†L1-L24】

### 4.1 Problem Shaping

**O que é:** Decompor objetivos vagos em subtarefas executáveis com entradas, saídas e critérios de sucesso claros.

**Por que é essencial:** "Build me a..." pode significar coisas completamente diferentes. Cada sub-problema precisa ter inputs claros, outputs claros, e critérios de sucesso claros.

**Como praticar:**
- Use skills como `/grill-me` (Matt Pocock) ou `brainstorming` (Superpowers) para refinar o problema antes de codar
- Documente em `CONTEXT.md` ou PRD antes de executar
- Toda task deve ter: input → processamento → output → critério de aceite

### 4.2 Context Design

**O que é:** Projetar o ambiente informacional completo que o agente usa para tomar decisões — não só o prompt, mas o filesystem, estado, e artefatos disponíveis.

**Por que é essencial:** "Context engineering é o sistema operacional do agente."【39†L1-L8】 A qualidade do contexto determina a qualidade da decisão.

**Disciplina acadêmica:** Context Engineering (CE) foi formalizada como disciplina independente da Prompt Engineering em 2026, com 5 critérios de qualidade: relevance, sufficiency, isolation, economy, provenance.【39†L1-L8】

**Como praticar:**
- Use GSD Core para state-to-disk (STATE.md, CONTEXT.md)
- Prependa um summary de status a toda chamada LLM: goal original → completed steps → current step → remaining steps【37†L38-L40】
- Mantenha o contexto do orquestrador limpo — subagentes recebem só o que precisam
- Use `.planning/` como substrate compartilhado entre sessões

### 4.3 Aesthetic Judgment

**O que é:** Avaliar se a solução gerada é desejável, não apenas correta do ponto de vista técnico.

**Por que é essencial:** O output do agente pode ser "tecnicamente correto" mas inútil, feio, ou semanticamente vazio. É a habilidade de dizer "isso funciona, mas não está bom."

**Como praticar:**
- Adicione um "Critic Node" na arquitetura multi-agente — um revisor que avalia o output contra critérios de qualidade, não só de corretude【37†L27-L34】
- Use skills como código-review, design-review, verification-before-completion
- Nunca confie na auto-avaliação do agente worker ("I'm done.")

### 4.4 Agent Orchestration

**O que é:** Decidir quando usar um ou múltiplos agentes, sequencial ou paralelo, e aplicar padrões de coordenação.

**Padrões principais:**

| Padrão | Descrição | Quando usar |
|--------|-----------|-------------|
| **Pipeline** | Agent A → Agent B → Agent C (sequencial) | Quando output de um é input do próximo |
| **Coordinator + specialists** | 1 coordinator dispatches, N specialists executam | Qualidade crítica, tarefas complexas |
| **Parallel + merge** | N agents independentes, resultados consolidados | Sem dependências entre subtarefas |
| **Orchestrator pattern** | Orchestrator só pensa/decompõe/sintetiza — nunca executa | Tarefas complexas que exigem isolamento de contexto【40†L1-L12】 |

**Regra prática:** "Se duas subtarefas não compartilham estado — nenhuma lê o que a outra escreve — podem rodar em paralelo. Se o output de uma determina o que a próxima será, precisam ser sequenciais. Se mais de 3 agentes paralelos precisam merge, introduza um coordinator."【37†L16-L20】

### 4.5 Discernir Quando Não Usar Agentes

**O que é:** Saber que tarefas simples são melhor resolvidas por scripts ou modelos pontuais, sem overhead de agente.

**Por que é essencial:** "Agentes são ferramentas caras. Se um shell script de 3 linhas resolve, use o script."

**Como praticar:**
- Avalie: "este problema precisa de raciocínio multi-passo e ferramentas?" Se não, não precisa de agente
- Use o Model Workspace Protocol (MWP) — folder structure como arquitetura, sem framework de coordenação【43†L1-L13】
- Prefira orchestrator pattern para tarefas complexas (1 orchestrator + N subagentes com contexto isolado)【40†L1-L12】

### 4.6 Harness Engineering

**O que é:** Projetar o harness — a camada de sistema ao redor do modelo: tool execution, control loop, context constructor, memory store, skill-routing, verification-and-governance.【41†L1-L10】

**Por que é essencial:** "Progresso futuro em agentic AI dependerá tanto do design de sistema quanto de modelos fundamentais mais fortes." O harness é o que traduz capacidade do modelo em comportamento do agente de longa duração.

**Componentes do harness (segundo pesquisa acadêmica 2026):**
1. **Context governance** — O que entra, o que fica, o que sai do context window
2. **Trustworthy memory** — Memória que persiste entre sessões com controle de qualidade
3. **Dynamic skill routing** — Skills carregadas on-demand, não tudo de uma vez
4. **Orchestration loop** — Lead coordinator que spawna, coleta, sintetiza
5. **Verification-and-governance** — Quality gates, audit trails, privacy boundaries

---

## Parte 5: Tabela Comparativa de Coleções

| Coleção | Skills | Estrelas (Jun/26) | Foco Principal | Instalação | Agentes |
|---------|--------|-------------------|----------------|------------|---------|
| **Superpowers** | 13 | ~226K | TDD + subagentes + processo completo | `npx skills add obra/superpowers` | 8 |
| **Karpathy Guidelines** | 1 (rules) | ~174K | Regras comportamentais anti-slop | `npx skills add multica-ai/andrej-karpathy-skills` | Todos |
| **Matt Pocock Skills** | 21 | ~136K | Skills modulares de engenharia | `npx skills@latest add mattpocock/skills` | Claude Code, Codex, Cursor |
| **GStack** | 23 | ~110K | Papéis de time (CEO → QA) | `git clone + setup.sh` | 7 |
| **GSD Core** | ~86 (namespace: 6) | ~51K + ~4.2K | Context engineering + state management | `npx gsd@latest init` | 10+ |
| **Addy Osmani Agent Skills** | 24 | ~49.9K | Production-grade engineering lifecycle | `npx skills add addyosmani/agent-skills` | Claude Code, Codex, Cursor, Gemini |
| **Anthropic Official** | 10+ | ~25K (org) | Document skills + exemplos | `/plugin marketplace add anthropics/skills` | Claude Code |
| **VoltAgent Awesome** | 1000+ | ~25.9K | Diretório multi-fornecedor | `npx skills add <owner>/<repo>` | 40+ |
| **AWS Agent Toolkit** | 40+ | ~10K | AWS workflows + MCP server | `/plugin install aws-core` | Claude Code, Codex, Kiro, Cursor |
| **antfu/skills** | 15+ | ~5K | Vue/Vite/Nuxt stack | `npx skills add antfu/skills` | Claude Code, Cursor, Codex |
| **vuejs-ai/skills** | 8 | ~2K | Vue 3 best practices | `/plugin install vue-best-practices@vue-skills` | Claude Code |
| **iuliandita/skills** | 42 | ~1K | DevOps, security, infra | `npx skills add iuliandita/skills` | 25 |
| **0xjacq/skills** | 9 | ~1K | Genérico + tools | `npx skills add 0xjacq/skills` | 50+ |

---

## Parte 6: Instalação e Uso

### 6.1 Instalação Global (todos os projetos)

```bash
# Claude Code global
~/.claude/skills/<skill-name>/SKILL.md

# Instalar via skills.sh CLI
npx skills add obra/superpowers
npx skills@latest add mattpocock/skills
npx skills add aws/agent-toolkit-for-aws/skills

# Instalar via plugin marketplace (Claude Code)
/plugin marketplace add anthropics/skills
/plugin install aws-core@agent-toolkit-for-aws
/plugin install document-skills@anthropic-agent-skills
```

### 6.2 Instalação por Projeto

```bash
# Claude Code
.claude/skills/<skill-name>/SKILL.md

# Cursor
.cursor/skills/<skill-name>/SKILL.md

# Codex
.codex/skills/<skill-name>/SKILL.md

# GitHub Copilot
.github/skills/<skill-name>/SKILL.md

# Generic Agent Skills Standard
.agents/skills/<skill-name>/SKILL.md
```

### 6.3 AWS CLI Agent Toolkit (desde Jun 2026)

```bash
# Setup interativo — detecta agents instalados, pergunta quais skills
aws configure agent-toolkit

# Gerenciar skills individuais
aws agent-toolkit add-skill <skill-name> --agent claude-code
aws agent-toolkit list-installed-skills
aws agent-toolkit search-skills "serverless"
aws agent-toolkit update-skill <skill-name>
aws agent-toolkit remove-skill <skill-name>
```

### 6.4 GSD Core

```bash
npx gsd@latest init
# Prompt: escolher runtime (Claude Code, OpenCode, Gemini CLI, etc.)
# Prompt: instalação global ou local
```

---

## Parte 7: Recomendações

### Para protótipos rápidos e experimentação

| Stack | Por quê |
|-------|---------|
| **GStack** | Papéis prontos para decisão rápida; `/office-hours` força clareza |
| **Superpowers** (skills individuais) | Só brainstorming + writing-plans, sem TDD pesado |
| **Matt Pocock `/prototype`** | Protótipo descartável em segundos |

### Para ambientes corporativos e produção

| Stack | Por quê |
|-------|---------|
| **Addy Osmani Agent Skills** | 24 skills com exit criteria, anti-rationalization, Google engineering practices |
| **AWS Agent Toolkit** | 40+ skills avaliadas, IAM context keys, CloudWatch/CloudTrail |
| **GSD Core** | Context engineering resolve context rot em sessões longas |
| **Superpowers (completo)** | TDD + subagentes + git worktree isola risco |

### Para desenvolvedores independentes

| Stack | Por quê |
|-------|---------|
| **Matt Pocock Skills** | Skills modulares e leves; escolha só o que precisa |
| **Superpowers** | Framework completo mas opinativo; melhor para quem quer disciplina |
| **Karpathy Guidelines** (como regra global) | Prevenção de slop em qualquer projeto |
| **antfu/skills** (se Vue) | Conhecimento de framework sempre atualizado |

### Stack recomendada combinada (máximo resultado)

```
Karpathy Guidelines (regra global — alwaysApply)
    + Superpowers (execução — TDD + subagentes)
    + GSD Core (contexto — state-to-disk)
    + AWS Agent Toolkit (se AWS)
    + antfu/skills (se Vue/Nuxt)
    + Agent Skills OWASP Top 10 (segurança)
```

"Superpowers foca em disciplina de teste, GSD ataca context rot, gstack adiciona governança baseada em papéis. Skills ensinam o 'como', frameworks ensinam o 'o quê'."【11†L1-L8】

---

## Parte 8: Skills em Avaliação (para Investigação Futura)

| Skill/Coleção | Motivo da avaliação |
|---------------|---------------------|
| **Deep Agents** | Long-running workflows, contextos complexos — pouco documentado para OpenCode |
| **AutoGen (Microsoft)** | Multi-agent conversation framework — depende de Python, integração indireta |
| **CrewAI** | Multi-agent com papéis — bom para protótipos, mas overhead alto |
| **smolagents** (Hugging Face) | Minimalista, transparente — bom para aprendizado, mas imaturo |
| **Mastra** | Framework TypeScript para agents — promissor, mas ecossistema pequeno |
| **Vellum** | Low-code agent building — pago, não OpenCode-native |
| **LangChain / LangGraph** | 1000+ integrações — mais ferramenta de framework do que skills |

Estes frameworks merecem investigação adicional, mas não foram priorizados por:
- Dependência de runtime específico (Python, Node)
- Falta de integração direta com formato SKILL.md
- Sobreposição com coleções já documentadas
- Maturidade menor que as coleções listadas

---

## Parte 9: Fontes

1. [anthropics/skills](https://github.com/anthropics/skills) — Skills oficiais da Anthropic
2. [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) — 1000+ skills curadas
3. [obras/superpowers](https://github.com/obra/superpowers) — Superpowers framework
4. [Pulumi Blog: Superpowers, GSD, and GSTACK](https://www.pulumi.com/blog/claude-code-orchestration-frameworks/) — Comparativo dos 3 frameworks
5. [DEV Community: Most popular AI coding skills](https://dev.to/aws/the-most-popular-ai-coding-skills-right-now-4183) — Análise de popularidade
6. [DEV Community: Combining Superpowers, gstack, GSD](https://dev.to/imaginex/a-claude-code-skills-stack-how-to-combine-superpowers-gstack-and-gsd-without-the-chaos-44b3) — Stack recomendada
7. [Firecrawl: Best Claude Code Skills 2026](https://www.firecrawl.dev/blog/best-claude-code-skills) — Guia de skills
8. [github.com/mattpocock/skills](https://github.com/mattpocock/skills) — Skills do Matt Pocock
9. [explainx.ai: Matt Pocock Skills v1.0](https://explainx.ai/blog/matt-pocock-typescript-skills-v1-progressive-disclosure-2026) — Análise v1.0
10. [github.com/garrytan/gstack](https://github.com/garrytan/gstack) — GStack
11. [github.com/open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) — GSD Core
12. [github.com/addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) — Addy Osmani Agent Skills
13. [github.com/aws/agent-toolkit-for-aws](https://github.com/aws/agent-toolkit-for-aws) — AWS Agent Toolkit
14. [aws.amazon.com: Agent Toolkit](https://aws.amazon.com/products/developer-tools/agent-toolkit-for-aws/) — Página oficial AWS
15. [AWS CLI Agent Toolkit support](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-cli-agent-toolkit/) — Anúncio Jun 2026
16. [github.com/antfu/skills](https://github.com/antfu/skills) — Anthony Fu Skills
17. [Vue School: Vue Agent Skills](https://vueschool.io/articles/vuejs-tutorials/vue-agent-skills-for-reliable-ai-development/) — Guia Vue
18. [github.com/vuejs-ai/skills](https://github.com/vuejs-ai/skills) — Vue.js AI Skills
19. [DEV Community: Skills Required for Building AI Agents in 2026](https://dev.to/imaginex/skills-required-for-building-ai-agents-in-2026-2ed) — Habilidades metodológicas
20. [arXiv: Context Engineering (2603.09619)](https://arxiv.org/pdf/2603.09619) — Paper acadêmico sobre CE
21. [arXiv: Scaling the Harness (2605.26112)](https://arxiv.org/html/2605.26112) — Paper sobre harness engineering
22. [The Orchestrator Pattern](https://www.promptengines.com/labnotes/articles/2026-03-14-orchestrator-pattern-agent-design-v3.html) — Orchestrator pattern
23. [Atlassian: Long Horizon Reasoning Engine](https://www.atlassian.com/blog/how-we-build/rovo-long-horizon-reasoning-engine) — Rovo Long Horizon architecture
24. [MLflow: Building Production-Ready AI Agents in 2026](https://mlflow.org/articles/building-production-ready-ai-agents-in-2026/) — Guia production-ready
25. [arXiv: Model Workspace Protocol (2603.16021)](https://arxiv.org/html/2603.16021v1) — MWP protocol
26. [Nemo Operans: Three Layers Underneath Agent Orchestration](https://nemooperans.com/three-layers-underneath-agent-orchestration) — FLOW methodology
27. [Boden Fuller: AgentOps Is Context Orchestration](https://www.bodenfuller.com/writing/context-orchestration) — Context orchestration
28. [Developers Digest: Best Claude Code Skills 2026](https://www.developersdigest.tech/blog/best-claude-code-skills-2026) — Curadoria de skills
29. [O'Reilly: Agent Skills by Addy Osmani](https://www.oreilly.com/radar/agent-skills/) — Artigo O'Reilly sobre agent skills
30. [Developers Digest: Agent Skills Need Exit Criteria](https://www.developersdigest.tech/blog/agent-skills-production-checklist) — Exit criteria em skills
31. [AgenticSkills.io Workflows](https://agenticskills.io/workflows) — Curated bundles de skills + MCPs
32. [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/) — Skills de context engineering
33. [NPM Skilld](https://www.npmjs.com/package/skilld) — Gerador de skills de dependências
34. [AWS Docs: Agent Toolkit Skills](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/skills.html) — Documentação oficial AWS
35. [AWS Docs: Agent Toolkit Plugins](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/plugins.html) — Documentação de plugins AWS

---

> **Nota:** Este relatório será atualizado conforme novas coleções e skills forem identificadas. Skills marcadas como "em avaliação" merecem investigação adicional antes de recomendação.
