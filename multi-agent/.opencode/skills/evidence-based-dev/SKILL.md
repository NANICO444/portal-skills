---
name: evidence-based-dev
description: "DESENVOLVIMENTO BASEADO EM EVIDENCIA - cada decisao com prova, cada resultado verificado. Sem achismo."
user-invocable: true
allowed-tools: Read, Bash
---

# Desenvolvimento Baseado em Evidencia

## Principio

> **Afe vs. Evidencia:** "deve funcionar" nao eh prova. `npm test output` eh prova.

## Quando Usar

- Toda tarefa de codigo
- Decisoes de design
- Validacao de feature completa
- Antes de commitar/mergear/deploy

## Tipos de Evidencia

### Evidencia de Comportamento
- Output de teste automatizado
- Log de execucao real
- Screenshot/GIF de UI funcionando
- Curl/wget para API funcionando

### Evidencia de Performance
- Benchmark com numero
- Profiler (CPU, memoria) com grafico
- Lighthouse score
- Bundle size em KB

### Evidencia de Seguranca
- Output de `npm audit`
- Output de `bandit` / `snyk` / `trivy`
- Penetration test report
- Code review por humano

### Evidencia de Compatibilidade
- Test em 3+ browsers
- Test em mobile
- Screenshot em diferentes resolucoes
- CI matrix com 5+ OS

## Anti-Padroes

❌ "Funciona na minha maquina" → Onde esta a evidencia?
❌ "Ta pronto" → Onde esta o output do teste?
❌ "Vai escalar" → Onde esta o benchmark?
❌ "Eh seguro" → Onde esta o audit?
❌ "Otimizei" → Onde esta a metrica ANTES e DEPOIS?

## Antes de Dizer "Pronto"

Checklist obrigatorio:
- [ ] Testes passam (mostre output)
- [ ] Lint passa (mostre output)
- [ ] Type check passa (mostre output)
- [ ] Build compila (mostre output)
- [ ] Feature testada manualmente (descreva como)
- [ ] Sem regressao (compare com antes)

## Format de Resposta "Pronto"

```
FEATURE CONCLUIDA: [nome]

TESTES:
- Unit: 124 passed, 0 failed
- Integration: 12 passed, 0 failed
- E2E: 3 passed, 0 failed

LINT: 0 errors, 0 warnings
TYPECHECK: 0 errors
BUILD: success (24.5s)

TESTE MANUAL:
- Cenário 1: PASS
- Cenário 2: PASS
- Cenário 3: PASS

PERFORMANCE:
- Antes: 250ms
- Depois: 180ms
- Ganho: 28%

REGRESSAO:
- Nenhuma feature quebrou
- Output comparativo anexado

ARTEFATOS:
- PR: link
- Screenshots: [anexo]
- Logs: [anexo]
```

## Quando Pedir Mais Evidencia

Se a "evidencia" eh vaga:
- "Funciona" → Mostre o output
- "Rápido" → Mostre o numero
- "Testado" → Mostre os tests
- "Sem bugs" → Mostre 0 issues
