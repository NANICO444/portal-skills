---
name: small-diffs
description: "PEQUENOS DIFFS - cada commit/mudanca faz UMA coisa. Facil de revisar, reverter, e entender."
user-invocable: true
allowed-tools: Bash, Read
---

# Pequenos Diffs

## Principio

> **Um diff de 50 linhas eh melhor que um de 500. Cada commit faz UMA coisa.**

## Quando Usar

- Todo commit
- Todo PR
- Toda mudanca em arquivo
- Toda conversa sobre "como fazer"

## Tamanho Ideal

| Tamanho | Veredito |
|---------|----------|
| < 50 linhas | ✅ Perfeito |
| 50-200 linhas | ✅ Bom |
| 200-500 linhas | ⚠️ Considere dividir |
| 500-1000 linhas | ❌ Divida |
| > 1000 linhas | ❌ Muito grande |

## Como Fazer Diffs Pequenos

### Dividir por Camada
1. Primeiro commit: schema/modelo
2. Segundo commit: logica de negocio
3. Terceiro commit: UI/frontend
4. Quarto commit: testes
5. Quinto commit: docs

### Dividir por Feature
1. Primeiro commit: helper function (sem uso)
2. Segundo commit: chamada do helper
3. Terceiro commit: teste do helper
4. Quarto commit: feature usando helper

### Dividir por Tipo
- Setup/Config (separado)
- Logica (separado)
- Tests (separado)
- Docs (separado)

## Anti-Padroes

❌ "Vou commitar tudo junto" → Dificulta review e revert
❌ "Feature com refactor junto" → 2 commits
❌ "Mudanca + cleanup de arquivos" → 2 commits
❌ "Format + logica" → 2 commits
❌ "Squash everything" → Perde historico

## Boas Praticas

### Mensagens de Commit Boas

```
[tipo]: descricao curta

Corpo: por que foi feito, contexto, decisoes.

Refs: #123
```

Tipos:
- `feat`: nova feature
- `fix`: correcao de bug
- `refactor`: refatoracao sem mudar comportamento
- `docs`: documentacao
- `test`: testes
- `chore`: build, deps, config
- `style`: formatacao
- `perf`: performance

### Exemplo Real

```
refactor: extract validateEmail function from UserService

UserService tinha 150 linhas com 3 responsabilidades
distintas. Extrai validateEmail para um helper separado
para facilitar testes e reuso em outros lugares.

Nenhuma mudanca de comportamento. Cobertura mantida.

Refs: #456
```

## Output Esperado de um Commit

```
ARQUIVOS MUDADOS: 1-3
LINHAS ADICIONADAS: < 50
LINHAS REMOVIDAS: < 50

O QUE MUDA: [1 frase]
POR QUE: [contexto]
COMO TESTAR: [passo]
```
