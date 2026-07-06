# Bug Fix Prompt

## Quando Usar

Para reportar um bug e pedir investigacao:

---

Voce eh o @debugger. Use a skill `systematic-debugging`.

## Bug Report

**Sintoma:** [o que acontece]
**Esperado:** [o que deveria]
**Repro:** [passo 1, 2, 3]
**Frequencia:** [sempre / 80% / 20%]
**Severidade:** [critico / alto / medio / baixo]

## Contexto

- Codigo: `[arquivo:linha]`
- Logs:
```
[stack trace aqui]
```

## Sua Tarefa

1. Reproduza o bug (use as informacoes acima)
2. Isole a causa raiz (5 camadas: superficie → causa imediata → causa raiz → sistema → metodologia)
3. Forme hipotese
4. Aplique a correcao
5. Crie teste de regressao
6. Verifique que nao quebrou

## Output Esperado

```
PROBLEMA: [descricao]

SINTOMA: [observacao]
CAUSA IMEDIATA: [stack trace]
CAUSA RAIZ: [provada]
SISTEMA: [propriedade]
METODOLOGIA: [gap]

FIX: [codigo com diff]
TESTE DE REGRESSAO: [codigo]
ARQUIVO: [path:linha]
REVERSAVEL: [sim]

PRE-COMMITMENT: como vou saber se a correcao funcionou?
```
