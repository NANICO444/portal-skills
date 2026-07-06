# Aurora Kiro IDE Workspace Package Implementation Plan

> **For agentic workers:** execute this plan task-by-task and verify every generated file before reporting completion.

**Goal:** Montar um pacote portatil de workspace Kiro IDE em que Aurora seja a orientacao principal para design e programacao local.

**Architecture:** O pacote usa `AGENTS.md` e arquivos `.kiro/steering` para comportamento principal, skills para fluxos sob demanda e um subagente markdown opcional. Hooks ficam desativados por padrao para evitar automacoes inesperadas no computador do usuario.

**Tech Stack:** Markdown, YAML frontmatter do Kiro IDE e arquivos JSON `.kiro.hook`.

---

### Tarefa 1: Base e identidade principal

**Arquivos:** `AGENTS.md`, `.kiro/steering/*.md`, `.kiro/agents/aurora.md`

- [x] Criar orientacao permanente, ambiente local e limites de seguranca.
- [x] Criar subagente opcional no formato markdown reconhecido pelo Kiro IDE.

### Tarefa 2: Skills Aurora

**Arquivos:** `.kiro/skills/*/SKILL.md`

- [x] Criar skills de design, frontend, full stack, validacao e entrega.
- [x] Traduzir personas relevantes em skills acionaveis.
- [x] Evitar dependencias de infraestrutura e agentes do sistema original.

### Tarefa 3: Instalacao e rastreabilidade

**Arquivos:** `README_INSTALACAO_E_USO.md`, `referencias/*.md`, `PROMPT_CODEX_INSTALAR_AURORA.md`

- [x] Explicar uso como template copiavel para qualquer projeto.
- [x] Documentar fontes Kiro e mapeamento do Aurora original.
- [x] Criar prompt para instalacao futura assistida por Codex.

### Tarefa 4: Verificacao

- [x] Confirmar estrutura e frontmatter das skills.
- [x] Validar JSON dos hooks.
- [x] Verificar ausencia de termos removidos no conteudo operacional.
- [x] Recalcular hash agregado da origem Hermes e comparar com o valor inicial.
