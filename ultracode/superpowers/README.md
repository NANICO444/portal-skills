# Superpowers

## O que e

Metodologia completa de planejamento, TDD e workflows com sub-agentes. Auto-aplica brainstorming, TDD (red-green-refactor) e revisao de codigo.

> **Instalar como PLUGIN** no `opencode.json` (nao como skill comum).

## Quando usar

- Todo projeto de codigo serio
- Quando voce quer que o agente siga metodo (TDD, planning, code review)
- Para garantir qualidade consistente entre sessoes

## Instalacao

```bash
# Comando oficial (instala o plugin completo)
Fetch and follow instructions from https://raw.githubusercontent.com/obra/superpowers/refs/heads/main/.opencode/INSTALL.md
```

## Configuracao pos-instalacao

Adicionar em `~/.config/opencode/opencode.jsonc`:

```jsonc
{
  "plugin": [
    "superpowers"
  ]
}
```

## Git

- Repo: https://github.com/obra/superpowers
- Skills fonte: https://github.com/obra/superpowers/tree/main/skills

## Prompt de exemplo

```
Crie uma API REST para gerenciamento de tarefas.
Use o plugin superpowers para seguir o metodo:
1. Brainstorm primeiro
2. Escreva plano
3. TDD (red-green-refactor)
4. Code review antes de commitar
```

## Status

- [ ] Plugin instalado em `~/.config/opencode/`
- [ ] Configurado em `opencode.jsonc` no `plugin: []`
- [ ] Skills do superpowers visiveis no OpenCode

## Notas

- Nao duplicar com skills existentes. O superpowers cobre `code-review`, `test-driven-development`, `plan`, etc.
- Se ja tem `code-review` em outro lugar, ele sera SOBRESCRITO pelo superpowers (last-wins no OpenCode).
