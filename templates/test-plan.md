# Test Plan — Feature X

## Objetivo

<!-- O que esse test plan cobre -->

## Scope

### Dentro do escopo
- [ ] Item 1
- [ ] Item 2

### Fora do escopo
- Item A
- Item B

## Tipos de Teste

### Unit Tests
- Funcao 1: [casos]
- Funcao 2: [casos]
- Edge cases: [lista]

### Integration Tests
- Modulo A + Modulo B: [cenario]
- DB + API: [cenario]

### End-to-End Tests
- Fluxo completo: [passo 1, 2, 3]
- Multi-user: [cenario]

### Performance Tests
- Load: X req/s
- Stress: Y req/s
- Latency: < Z ms

### Security Tests
- SQL Injection
- XSS
- CSRF
- Auth bypass

### Compatibility Tests
- Chrome, Firefox, Safari
- Mobile, Tablet, Desktop
- Win, Mac, Linux

## Casos de Teste

### Caso 1: [nome]
- **Pre-condicao:** [estado]
- **Acao:** [passos]
- **Esperado:** [resultado]
- **Atual:** [resultado]
- **Status:** PASS / FAIL / BLOCKED

### Caso 2: [nome]
- ...

## Edge Cases

- [ ] Input vazio
- [ ] Input muito grande (>1MB)
- [ ] Unicode/charset especial
- [ ] Concurrency (multi-user)
- [ ] Network failure mid-operation
- [ ] Disk full
- [ ] Out of memory

## Criterios de Saida (Definition of Done)

- [ ] All unit tests passing
- [ ] All integration tests passing
- [ ] Coverage >= X%
- [ ] No critical bugs
- [ ] No security vulnerabilities
- [ ] Performance meets SLO
- [ ] Documentation updated
- [ ] Stakeholder review

## Riscos de Teste

- Risco 1: [descricao]
- Risco 2: [descricao]

## Ferramentas

- Test runner: [pytest, vitest, jest, etc]
- Coverage: [coverage.py, c8, etc]
- E2E: [playwright, cypress, etc]
- Performance: [k6, artillery, etc]
