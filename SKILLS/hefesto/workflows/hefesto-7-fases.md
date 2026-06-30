# Hefesto - Workflow 7 Fases

## Modos

- SIMPLES: microtarefa, sem dependência nova, sem dado sensível. Fluxo curto: triage → implementação → entrega.
- STANDARD: padrão. Usa 7 fases completas.
- URGENTE: hotfix. Primeiro pergunta se rollback resolve. Depois faz fix mínimo, teste mínimo e pós-mortem.

## Fases

1. FASE 0 TRIAGE: entender pedido, domínio, risco, ambiguidade e modo.
2. FASE 1 REQUIREMENTS: confirmar escopo, fora de escopo, critérios de aceite e perguntas.
3. FASE 2 ARCHITECTURE: escolher abordagem simples, interfaces, dependências, riscos e alternativa.
4. FASE 3 PLAN + APPROVAL: plano aprovado antes de editar, exceto trivial.
5. FASE 4 IMPLEMENTATION: TDD quando couber, mudança cirúrgica e commits/patches pequenos.
6. FASE 5 TESTING & REVIEW: build, lint, testes, tipos, segurança e review com checklist.
7. FASE 6 DELIVERY: resumo, arquivos, verificação, riscos e próximos passos.

## Debate gate

Use este formato quando houver decisão técnica:

DECIDE: pergunta central
PRO: argumentos a favor
RISK: risco e mitigação
ALT: alternativa descartada
DECISÃO: escolha
CONFIANÇA: ALTA, MÉDIA ou BAIXA

Confiança BAIXA exige perguntar ao usuário.

