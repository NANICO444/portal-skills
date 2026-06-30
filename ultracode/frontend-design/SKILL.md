---
name: frontend-design
description: "Skill oficial Anthropic para design de UI em React, Vue, HTML e CSS. Anti-slop, anti-generico."
user-invocable: true
allowed-tools: Read, Write, Bash
---

# Anthropic Frontend Design

## O que e

Skill oficial Anthropic para **design de UI de alta qualidade**. Anti-slop, anti-generico. Direciona estetica e boas praticas para React, Vue, HTML e CSS.

## Quando usar

- Criar nova interface (landing, dashboard, formulario)
- Melhorar UI existente
- Garantir que UI nao parece "AI-generated"
- Code review visual

## Instalacao

```bash
# Via CLI de skills
npx skills add https://github.com/anthropics/skills --skill frontend-design
```

## Git

- Repo: https://github.com/anthropics/skills
- Skill: https://github.com/anthropics/skills/tree/main/skills/frontend-design

## Processo de uso (5 fases)

### 1. Brief
- Publico-alvo
- Tom visual (serio, ludico, tecnico)
- Restricoes (framework, browser, device)
- Referencias

### 2. Estrutura
- Layout base
- Hierarquia visual
- Pontos de atencao

### 3. Tokens
- Cores (paleta funcional)
- Tipografia (escala, espacamento)
- Sombras, borders, radius

### 4. Componentes
- Botoes, inputs, cards
- Estados: hover, focus, active, disabled
- Acessibilidade (WCAG AA)

### 5. Polish
- Micro-interacoes
- Loading states
- Empty states
- Error states

## Prompt de exemplo

```
Crie um dashboard de analytics para um SaaS B2B.
- Publico: gerentes de produto
- Tom: profissional mas acessivel
- Stack: React + Tailwind
- Restricoes: WCAG AA, responsivo

Use a skill frontend-design para garantir qualidade visual.
```

## Anti-Slop

A skill ajuda a evitar:
- Gradientes genericos
- Stock photos
- Lorem ipsum
- Cores cliche
- Cards quadrados sem personalidade
- "AI-isms" (preenchimento excessivo, sem opiniao)

## Complementa skills existentes

- `taste-skill` (ja temos) - similar, focado em nao-generico
- `minimalist-skill` (ja temos)
- `design-brief` (ja temos)

A skill Anthropic pode complementar (nao substituir) as existentes.
