---
name: skill-creator
description: "Skill oficial Anthropic para criar, testar e aprimorar outras skills. Inclui avaliacoes e benchmarking."
user-invocable: true
allowed-tools: Read, Write, Bash
---

# Anthropic Skill Creator

## O que e

Skill oficial da Anthropic para **criar, testar e melhorar outras skills**. Inclui workflow de avaliacao e benchmarking.

## Quando usar

- Antes de criar uma nova skill (validar que ela eh util)
- Para melhorar skills existentes
- Quando quiser comparar performance entre versoes de uma skill

## Instalacao

```bash
# Via CLI de skills
npx skills add https://github.com/anthropics/skills --skill skill-creator
```

## Git

- Repo: https://github.com/anthropics/skills
- Skill: https://github.com/anthropics/skills/tree/main/skills/skill-creator

## Processo de uso (3 fases)

### Fase 1: Descobrir
- Qual problema a skill resolve?
- Quem vai usar?
- Em que contexto?

### Fase 2: Implementar
- Criar SKILL.md com frontmatter YAML
- Escrever corpo markdown
- Adicionar exemplos

### Fase 3: Avaliar
- Criar casos de teste
- Rodar benchmark
- Comparar versoes
- Iterar

## Prompt de exemplo

```
Quero criar uma skill para code review de arquivos .vue.
Use a skill skill-creator para:
1. Descobrir o escopo (componentes, composables, directives?)
2. Implementar a skill seguindo o template
3. Criar 5 casos de teste para validar
```

## Estrutura de uma skill boa (do skill-creator)

```markdown
---
name: kebab-case-name
description: "Verbo + objeto + condicao. < 200 chars."
---

# Nome da Skill

## When to Use
[condicoes claras]

## How to Use
[passos numerados]

## Examples
[3+ exemplos concretos]

## Anti-Patterns
[o que NAO fazer]
```

## Beneficios

- Skills consistentes (padrao Anthropic)
- Avaliaveis (benchmark)
- Menos duplicacao
- Melhor qualidade media
