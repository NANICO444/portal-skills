# Refactor Prompt

## Quando Usar

Para pedir refatoracao:

---

Voce eh o @refatorador + use a skill `safe-refactor`.

## Codigo Atual

```[LINGUAGEM]
[COLAR CODIGO AQUI]
```

## Problemas Identificados

- [ ] Long method (> 30 linhas)
- [ ] God class
- [ ] Duplicacao
- [ ] Feature envy
- [ ] Primitive obsession
- [ ] Outro: _______

## Restricoes

- **NAO** mudar comportamento observavel
- **NAO** quebrar testes existentes
- **NAO** adicionar features
- **NAO** "melhorar" coisas nao pedidas

## Sua Tarefa (6 Passos do safe-refactor)

1. **Tests** — garanta tests do comportamento atual
2. **Pequena mudanca #1** — UM pattern por vez
3. **Rode tests** — se quebrou, REVERTA
4. **Commit** — "refactor: [o que fez]"
5. **Repita** — proxima mudanca
6. **Pare** — quando o codigo esta bom o suficiente

## Output Esperado

```
REFACTOR PLANNING:

OBJETIVO: [o que melhorar]
TESTS EXISTENTES: [sim/nao, cobertura]
TESTS A ADICIONAR: [lista]

STEPS (pequenos, atomicos):
1. [mudanca] - impacto: baixo
2. [mudanca] - impacto: baixo
3. [mudanca] - impacto: medio

VERIFICACAO:
- Tests passam apos cada passo
- Lint passa
- Performance nao piorou

ROLLBACK:
- Cada commit eh reversivel
```

NAO faca o refactor inteiro em 1 commit. Faca em commits atomicos.
