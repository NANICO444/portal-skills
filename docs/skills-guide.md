# Guia de Skills

> **Como as 188 skills funcionam, e como escolher a certa.**

## Anatomia de uma Skill

Cada skill eh um arquivo `SKILL.md` com:

```markdown
---
name: nome-da-skill              # Obrigatorio
description: "..."               # Obrigatorio
model: tokenrouter/MiniMax-M3    # Opcional (sobrescreve default)
variant: max|minimal|high       # Opcional
user-invocable: true|false      # Opcional (default true)
allowed-tools: Read, Bash, ...  # Opcional
agent: nome-do-agent            # Opcional
alwaysApply: true|false         # Opcional
---

# Titulo da Skill

## Quando Usar
[quando invocar]

## Framework
[passos, processo]

## Output
[template de saida]

## Anti-Padroes
[o que NAO fazer]
```

## Tipos de Skills

### 1. Skills de Processo
Definem um **processo** a seguir. Ex: `safe-refactor`, `investigate-before-edit`.

Quando usar: precisa de metodo para fazer algo.

### 2. Skills de Decisao
Ajudam a **decidir**. Ex: `financial-decision`, `risk-decision`.

Quando usar: tem opcoes e precisa escolher.

### 3. Skills de Framework
Dão um **framework** mental. Ex: `think-max-protocol` (5 camadas), `systematic-debugging` (reproduzir-hipotese-fixar).

Quando usar: problema eh estruturado.

### 4. Skills de Curadoria
Recomendam **ferramentas/bibliotecas**. Ex: `library-curator`.

Quando usar: precisa escolher tecnologia.

### 5. Skills de Anti-Padrao
Definem o que **NAO fazer**. Ex: `anti-glaze-ux`, `small-diffs`, `rollback-strategy`.

Quando usar: precisa resistir a um mau padrao.

### 6. Skills de Output
Definem **formato de saida**. Ex: `supervisor` (veredito + score + 4 listas).

Quando usar: precisa de output estruturado.

## Como Escolher a Skill Certa

### Passo 1: Identifique o tipo de problema

| Pergunta | Tipo | Skill sugerida |
|----------|------|----------------|
| Como fazer X? | Processo | safe-refactor, investigate-before-edit |
| Devo fazer X? | Decisao | strategic-decision, financial-decision |
| O que esta errado? | Framework | systematic-debugging, think-max-protocol |
| Qual lib usar? | Curadoria | library-curator, factual-verify |
| Como evitar ma pratica? | Anti-Padrao | anti-glaze-ux, small-diffs |
| Como reportar? | Output | supervisor, review |

### Passo 2: Carregue a skill

No OpenCode, use a skill pelo nome:
- "use a skill safe-refactor"
- "use a skill library-curator"

Ou invoque pelo slash-command se existir.

### Passo 3: Siga o framework

Cada skill tem framework. Siga os passos.

## Skills Mais Importantes (Top 20)

1. **supervisor** — Revisao rigorosa, output estruturado
2. **code-review** — 7 camadas de revisao
3. **systematic-debugging** — Metodo cientifico
4. **safe-refactor** — Refatorar sem quebrar
5. **investigate-before-edit** — Antes de editar
6. **think-max-protocol** — 5 camadas de pensamento
7. **library-curator** — Escolher biblioteca
8. **small-diffs** — Commits atomicos
9. **rollback-strategy** — Plano de reversao
10. **evidence-based-dev** — Sem achismo
11. **anti-glaze-ux** — Sem dark patterns
12. **kiro-engineering-process** — 6 passos Hefesto
13. **kiro-design-process** — 6 passos Aurora
14. **kiro-data-security** — Dados, seguranca, API
15. **kiro-verification** — Checklist de entrega
16. **adr-architecture-decision** — Documentar decisao
17. **critical-thinking** — Pensamento critico
18. **council** — Multiplas perspectivas
19. **karpathy-discipline** — Simplicidade
20. **impeccable-quality** — Framework de qualidade

## Skills de Decisao Rapida (6)

Quando precisa decidir AGORA (30-60s):

- `strategic-decision` — estrategia
- `financial-decision` — ROI/custo
- `risk-decision` — risco
- `tech-decision` — stack
- `marketing-decision` — publico/canal
- `ops-decision` — processo/recurso

## Skills Ultra-Poderosas (5)

Para decisoes CRITICAS (precisam Opus 4.8):

- `complex-architecture-decision` — 7 camadas
- `multi-factor-risk-assessment` — cascata de riscos
- `cross-domain-optimization` — pareto
- `adversarial-decision-analysis` — red team
- `long-term-strategic-forecast` — 2-10 anos

## Como Criar uma Nova Skill

1. Crie a pasta: `multi-agent/.opencode/skills/minha-skill/`
2. Crie o arquivo: `SKILL.md`
3. Use o frontmatter padrao
4. Salve
5. **Aparece no OpenCode global** (junction)

## Skills que NAO Devem Ser Criadas

- Skills duplicadas (ja existe)
- Skills vazias (sem conteudo)
- Skills muito especificas (so 1 caso de uso)
- Skills sem frontmatter
- Skills sem framework definido
