---
description: "REGRA SUPERVISORA - SEMPRE passe pelo supervisor antes de aprovar codigo. Ele ve tudo, decide tudo."
mode: primary
user-invocable: false
alwaysApply: true
---

# Regra Supervisora — Sempre Supervisar

## Em qualquer trabalho de codigo, siga este fluxo:

### 1. IMPLEMENTAR
Dev implementa a mudanca.

### 2. INVOCAR SUPERVISOR
Apos implementacao, SEMPRE invoque `@supervisor` para revisao.

### 3. SUPERVISOR CHAMA SUB-AGENTES
Em paralelo:
- `@code-reviewer-x` — revisao geral
- `@security-auditor` — seguranca
- `@performance-auditor` — performance
- `@test-coverage-auditor` — testes
- `@docs-auditor` — documentacao
- `@dependency-auditor` — dependencias
- `@standards-enforcer` — padroes

### 4. SUPERVISOR SINTETIZA
Output estruturado:
- VEREDITO: APROVADO / RESSALVAS / REJEITADO
- SCORE 0-100
- O QUE APAGAR (linhas especificas)
- O QUE ADICIONAR (codigo novo)
- O QUE FAZER (proximos passos)
- O QUE BAIXAR (bibliotecas com comando)

### 5. DECISAO
- APROVADO: pode commitar/mergear/deploy
- RESSALVAS: commitar mas resolver em < 1 semana
- REJEITADO: NAO commitar, voltar para implementacao

## Excecao
Apenas mudanças triviais (typo, comentario, formatacao) podem pular supervisor.

## Anti-Padroes
❌ Commitar sem passar pelo supervisor
❌ "Esta funcionando" nao eh qualidade
❌ "Refatorar depois" sem lista do que
❌ Pular checagem de seguranca
