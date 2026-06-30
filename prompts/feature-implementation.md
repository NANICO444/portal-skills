# Feature Implementation Prompt

## Quando Usar

Para pedir implementacao de uma feature completa:

---

Voce eh o @orquestrador (multi-agent) + @supervisor (max-thinking).

## Feature

**Nome:** [nome]
**Problema:** [dor do usuario]
**Criterios de Aceitacao:**
- [ ] [criterio 1]
- [ ] [criterio 2]
- [ ] [criterio 3]

## Restricoes

- Stack: [ex: Node + TypeScript]
- Performance: [ex: < 200ms p95]
- Compatibilidade: [ex: Node 18+]
- Escopo: [ex: apenas backend, sem UI]
- NAO fazer: [ex: nao mexer no DB]

## Sua Tarefa (Workflow)

1. **Planeje** — use `investigate-before-edit` para entender o codigo
2. **Implemente** — menor mudanca coerente
3. **Teste** — TDD se possivel (skill `test-driven-development`)
4. **Revise** — use `safe-refactor` se preciso
5. **Superevisione** — chame @supervisor para revisao final
6. **Documente** — atualize docs + ADRs

## Output Esperado por Etapa

### Plano (5-10 itens)
- Item 1: [acao]
- Item 2: [acao]

### Implementacao
- [diff do codigo]

### Testes
- [codigo de teste]

### Supervisão
- VEREDITO: [APROVADO/REJEITADO]
- SCORE: XX
- O QUE FAZER (se rejeitado)

### Docs
- [mudancas em docs]
- [ADR se aplicavel]
