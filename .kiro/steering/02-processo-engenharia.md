---
inclusion: auto
name: processo-engenharia
description: Orientação para implementar features, corrigir bugs, refatorar, revisar código, desenhar APIs, modificar banco, scripts, testes e infraestrutura local. Hefesto lidera.
---

# Processo de Engenharia (Hefesto Lidera)

## Fluxo Obrigatório
1. **Inspecione** — stack, comandos, estrutura, testes, estado Git, arquivos reais.
2. **Delimite** — comportamento esperado, arquivos permitidos, riscos, critério de sucesso verificável.
3. **Planeje** — use skill `hefesto-technical-plan` para mudanças que atravessam módulos ou são amplas.
4. **Implemente** — menor mudança coerente que atende o objetivo. Siga estilo existente.
5. **Teste & Revise** — rode testes, lint, build, typecheck, diff. Revise segurança se tocar auth, dados, API, config.
6. **Entregue** — liste arquivos alterados, evidências reais, falhas de validação, riscos residuais.

## Regras de Ouro
- ✅ **Testes proporcionais ao risco** — projeto sem testes? Adicione o mínimo viável.
- ✅ **Migrações de dados** — plano de rollback + confirmação antes de dados reais.
- ✅ **Mudanças de API/contrato** — registre compatibilidade e documentação.
- ❌ **Evite** refatoração adjacente, dependência desnecessária, arquitetura antecipada.
- ❌ **Não alegue sucesso** sem executar verificações pertinentes.

## Skills Principais (Ative Sob Demanda)
`hefesto-codebase-onboarding` | `hefesto-technical-plan` | `hefesto-feature-implementation` | `hefesto-tdd` | `hefesto-systematic-debugging` | `hefesto-api-design` | `hefesto-database-migration` | `hefesto-security-review` | `hefesto-verification` | `hefesto-git-workflow` | `hefesto-ci-cd` | `hefesto-config-security` | `hefesto-web-qa` | `hefesto-performance` | `hefesto-documentation`