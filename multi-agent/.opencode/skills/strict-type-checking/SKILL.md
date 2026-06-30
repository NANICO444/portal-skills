---
name: strict-type-checking
description: >
  Configura e FORÇA verificação de tipos em modo estrito — mypy strict + pyright
  em Python, strict mode em TypeScript — e resolve os erros que aparecem, sem
  silenciar com ignores. Ative ao iniciar/endurecer a checagem de tipos de um
  projeto, antes de fechar código que mexe em tipos, ou quando aparecerem erros
  de tipo pra resolver. É o portão de tipos do executor técnico.
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [tipos, mypy, pyright, typescript, strict, hefesto, qualidade]
    related_skills: [verification-before-completion, property-based-testing, code-review-checklist]
    adapted_from: "wshobson/agents — plugins/python-development/skills/python-type-safety (base de conceitos)"
prerequisites:
  python: "mypy, pyright (pip/npm)"
---

# Strict Type Checking

Tipos pegam uma classe inteira de bugs antes de rodar o código — mas só se a
checagem estiver em modo **estrito** e os erros forem **resolvidos**, não
silenciados. Esta skill configura o modo estrito e dá a disciplina de fechar os
erros de forma honesta. (Os conceitos de sistema de tipos — generics, protocols,
narrowing — vêm da base `python-type-safety` do wshobson; aqui o foco é
*forçar e manter* o strict.)

## Quando usar

- Ao iniciar a checagem de tipos de um projeto ou endurecê-la pra strict.
- Antes de fechar código que adiciona/altera tipos (Hefesto em modo RÍGIDO).
- Quando aparecem erros de tipo e a tentação é silenciar com `# type: ignore`.

## Configuração estrita

### Python — mypy strict + pyright

`pyproject.toml`:
```toml
[tool.mypy]
strict = true
warn_unreachable = true
warn_redundant_casts = true
warn_unused_ignores = true        # pega ignores que não são mais necessários
no_implicit_reexport = true

[tool.pyright]
typeCheckingMode = "strict"
```

Rodar: `mypy .` e `pyright`. Use **os dois** — eles pegam coisas diferentes
(pyright é melhor em narrowing/inferência; mypy tem ecossistema de plugins).

### TypeScript — strict mode

`tsconfig.json`:
```json
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitOverride": true,
    "exactOptionalPropertyTypes": true
  }
}
```
Rodar: `tsc --noEmit`.

## Disciplina de resolução (o que diferencia esta skill)

Quando o strict acusa erros, resolva pela ordem de preferência:

1. **Corrija o tipo de verdade** — anote a assinatura, trate o `None`/`undefined`,
   estreite o tipo com guard. É o caminho certo na maioria dos casos.
2. **Refine o tipo** — use o tipo mais preciso (ex: `Literal`, união, `TypedDict`,
   protocol) em vez de `Any`.
3. **`Any` / `cast` deliberado** — só quando a fronteira é genuinamente dinâmica
   (entrada externa não tipada). Documente POR QUÊ num comentário.
4. **`# type: ignore[código]` / `@ts-expect-error`** — último recurso, SEMPRE
   com o código do erro específico e um comentário explicando. Nunca um
   `# type: ignore` solto (mascara erros futuros). `warn_unused_ignores`/
   `ts-expect-error` ajudam a limpar ignores obsoletos.

**Anti-padrão proibido**: relaxar a config (`strict = false`, remover flags) pra
"fazer passar". Isso é desligar o alarme em vez de apagar o fogo. Se precisar
relaxar uma flag por motivo real, documente em DECISIONS.md e pergunte
(`[[human-in-the-loop]]`).

## Como fazer

1. Aplique a config estrita acima.
2. Rode os checkers e leia TODOS os erros (não só o primeiro).
3. Resolva pela ordem de preferência. Agrupe erros similares.
4. Rode de novo até zero erros — sem silenciar indevidamente.
5. A confirmação de "tipos limpos" é do `[[verification-before-completion]]`:
   só afirme depois de `mypy . && pyright` (ou `tsc --noEmit`) com saída limpa.

## Relação com o sistema

- Pareia com `[[property-based-testing]]`: tipos pegam erros de forma; testes de
  propriedade pegam erros de lógica.
- O resultado entra na evidência do `[[verification-before-completion]]`
  (`mypy . (0 erros)` no `metadata.verification` do card).
- Faz parte da régua RÍGIDA do Hefesto (build + test + lint + **types** + diff).
