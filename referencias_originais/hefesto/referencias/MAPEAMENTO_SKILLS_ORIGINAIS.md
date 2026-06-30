# Mapeamento Das Capacidades Originais Para Kiro IDE

## Observacao Importante

O arquivo original `skills_list.md` declara 19 skills universais e 42 especificas, totalizando 61. Entretanto, a numeracao exibida no proprio material chega a 49 skills especificas. Como essa contagem e inconsistente, este pacote nao afirma reproduzir uma instalacao exata.

Foram criadas **31 skills locais do Kiro IDE** que cobrem as capacidades uteis para Hefesto operar sozinho em um PC comum.

## Capacidades Adaptadas

| Area Do Original | Skills Locais Correspondentes |
|---|---|
| Fluxo, plano e especificacao | `hefesto-engineering-workflow`, `hefesto-technical-plan`, `hefesto-spec-driven` |
| Leitura e arquitetura do projeto | `hefesto-codebase-onboarding`, `hefesto-architecture` |
| Implementacao | `hefesto-feature-implementation`, `hefesto-python-engineering`, `hefesto-typescript-engineering` |
| Testes e tipos | `hefesto-tdd`, `hefesto-test-strategy`, `hefesto-property-testing`, `hefesto-strict-type-checking` |
| Diagnostico | `hefesto-systematic-debugging`, `hefesto-parallel-investigation` |
| Revisao e verificacao | `hefesto-code-review`, `hefesto-receiving-review`, `hefesto-verification` |
| API, dados e erros | `hefesto-api-design`, `hefesto-database-migration`, `hefesto-error-handling` |
| Seguranca e dependencias | `hefesto-security-review`, `hefesto-config-security`, `hefesto-dependency-evaluation` |
| Git e entrega | `hefesto-git-workflow`, `hefesto-branch-delivery`, `hefesto-ci-cd` |
| Interface, desempenho e documentacao | `hefesto-web-qa`, `hefesto-performance`, `hefesto-documentation` |
| Pesquisa tecnica | `hefesto-research-verify` |
| Futuro repasse manual de contratos | `hefesto-manual-contract-export` |

## O Que Foi Removido Ou Limitado

- Comandos e caminhos especificos do Hermes nao foram transferidos.
- Dependencias de servidor remoto ou comunicacao automatica com agentes nao foram transferidas.
- Integracoes externas nao foram tratadas como obrigatorias.
- Deploy, dados reais, credenciais e mudancas globais dependem de confirmacao do usuario.
