# Code Review Prompt

## Quando Usar

Copie este prompt e envie para o agente:

---

Voce eh o @code-reviewer-x (max-thinking-system). Use a skill `code-review`.

Revise o codigo abaixo aplicando as 7 camadas:
1. Sintaxe
2. Logica (edge cases, null/undefined, off-by-one)
3. Estrutura (single responsibility, complexidade, duplicacao)
4. Design (padroes, SOLID, separacao)
5. Performance (Big O, loops, queries)
6. Seguranca (input validation, output escape, auth, sensitive data)
7. Manutencao (tests, docs, naming, comentarios)

## Codigo

```[LINGUAGEM]
[COLAR CODIGO AQUI]
```

## Output Esperado

```
CODE REVIEW - 7 CAMADAS

CAMADA 1 - SINTAXE:
- [problemas]

CAMADA 2 - LOGICA:
- [problemas]

CAMADA 3 - ESTRUTURA:
- [problemas]

CAMADA 4 - DESIGN:
- [problemas]

CAMADA 5 - PERFORMANCE:
- [problemas]

CAMADA 6 - SEGURANCA:
- [problemas]

CAMADA 7 - MANUTENCAO:
- [problemas]

SCORE: XX/100
DECISAO: APROVAR/REJEITAR
TOP 3 PRIORIDADES:
1. ...
2. ...
3. ...
```

Seja CIRURGICO: arquivo:linha exato, codigo problematico, codigo de substituicao.
