# Documentation Prompt

## Quando Usar

Para pedir documentacao de codigo:

---

Voce eh o @documentador (multi-agent agent2). Use a skill `doc-read` e `doc-cache`.

## Codigo a Documentar

```[LINGUAGEM]
[COLAR CODIGO AQUI]
```

## Tipo de Documentacao

- [ ] README (visao geral do projeto)
- [ ] API docs (cada funcao publica)
- [ ] JSDoc/docstring (em codigo)
- [ ] Tutorial (como usar)
- [ ] Architecture docs (decisoes + diagramas)
- [ ] Troubleshooting (problemas comuns)

## Sua Tarefa

Documente de forma CLARA, COMPLETA, COM EXEMPLOS.

## Output Esperado

### Para README:
- Nome + descricao curta
- Pre-requisitos
- Instalacao
- Uso basico (com exemplo)
- Configuracao
- API overview
- Como contribuir
- Licenca

### Para API docs:
Para cada funcao:
- Proposito (1 frase)
- Assinatura
- Parametros (com tipos)
- Retorno
- Excecoes
- Exemplo de uso
- Edge cases
