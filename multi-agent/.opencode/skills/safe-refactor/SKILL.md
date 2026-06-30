---
name: safe-refactor
description: "REFATORACAO SEGURA - 6 passos para refatorar sem quebrar comportamento. Testes primeiro, mudancas pequenas, verificar cada passo."
user-invocable: true
allowed-tools: Read, Grep, Glob, Bash, Edit
---

# Refatoracao Segura

## Principio

> **Refatorar NAO eh reescrever. Cada mudanca deve ser pequena, testada, e reversivel.**

## Quando Usar

- Codigo funciona mas esta feio
- Duplicacao clara
- Funcao muito longa
- Classe com baixa coesao
- Apos adicionar feature (cleanup)

## NAO Refatorar Quando

- Codigo funciona mas eh feio, e tem prazo apertado
- Outros devs estao mexendo no mesmo arquivo (conflito)
- Nao tem testes para verificar que nao quebrou
- Mudanca teria impacto em 50+ arquivos (risco alto)

## Framework (6 Passos)

### Passo 1 - Garantir Testes (obrigatorio)

ANTES de refatorar, garanta testes que:
- Cubram o comportamento atual
- Passem antes da refatoracao
- Se nao existem, ESCREVA-OS primeiro

```
[x] Teste do comportamento atual passa
[x] Cobertura >= 80% do codigo a ser refatorado
[x] Tests de integracao (se aplicavel)
```

### Passo 2 - Pequena Mudanca #1

Uma coisa por vez. Exemplos:
- Renomear variavel para nome melhor
- Extrair funcao privada
- Mover para outro arquivo
- Adicionar type hint
- Trocar `if/else` por `switch`

### Passo 3 - Rodar Testes

- Se quebrou: REVERTA imediatamente
- Se passou: continue

### Passo 4 - Commit

- Mensagem descritiva: "refactor: extract validateEmail function"
- NUNCA commite refactor junto com feature

### Passo 5 - Repetir

Volte ao Passo 2. Faca a PROXIMA pequena mudanca.

### Passo 6 - Parar

Quando o codigo esta bom o suficiente, PARE. "Perfeito" eh inimigo de "pronto".

## Padroes Comuns (e como refatorar)

### Long Method (> 30 linhas)
1. Identifique blocos logicos
2. Extraia para funcoes privadas com nomes descritivos
3. Funcao original agora chama as privadas

### God Class
1. Identifique responsabilidades distintas
2. Crie classes separadas
3. Use injecao de dependencia
4. Compose na classe original (ou refatore uso direto)

### Feature Envy
- Metodo usa mais dados de OUTRA classe que da sua
- Mova o metodo para a classe "dona" dos dados

### Duplicated Code
1. Identifique o trecho duplicado
2. Extraia para funcao/metodo/componente
3. Substitua os usos pelo helper

### Primitive Obsession
- Strings/ints representando conceitos (email, cpf)
- Crie Value Objects: `class Email { value: string }`
- Validacao centralizada

## Anti-Padroes

❌ Refatorar + feature em mesmo commit
❌ Refatorar sem testes
❌ "Melhorar" codigo que nao pediu para mexer
❌ Renomear 50 coisas de uma vez
❌ Refatorar para "ficar mais clean" sem motivo
❌ Reescrever do zero (a não ser que seja inevitável)

## Quando Delegar

- Codigo grande (>500 linhas): divida primeiro
- Multiplos padroes no mesmo arquivo: use @code-architect
- Performance impact: use @performance-auditor depois

## Output

```
REFACTOR PLANNING:

OBJETIVO: [o que melhorar]
- Long method
- Duplicacao
- God class
- Outro: _______

TESTS EXISTENTES: [sim / nao / parcial]
- Cobertura: X%
- Tests que precisam ser adicionados: [lista]

REFACTOR STEPS (pequenos):

1. [mudanca 1] — impacto: baixo, reversivel
2. [mudanca 2] — impacto: baixo, reversivel
3. [mudanca 3] — impacto: medio, reversivel
4. [mudanca 4] — impacto: medio, reversivel

VERIFICACAO:
- Tests passam apos cada passo
- Lint passa
- Performance nao piorou

ROLLBACK:
- Cada commit eh reversivel
- Se comportamento quebrou, revert + investigar
```
