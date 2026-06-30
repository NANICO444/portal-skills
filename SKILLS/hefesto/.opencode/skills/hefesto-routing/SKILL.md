---
name: hefesto-routing
description: Use no início de toda tarefa não trivial do Hefesto para classificar o pedido, ativar skills e escolher automaticamente os subagentes técnicos corretos.
---

# Roteamento nativo do Hefesto

Esta skill substitui a segmentação que Apollo fazia na VPS. O usuário fala direto com Hefesto; por isso o agente primário faz a triagem e chama subagentes sem esperar pedido explícito.

## Gate inicial

1. Classifique o pedido como `SIMPLES`, `STANDARD` ou `URGENTE`.
2. Detecte ambiguidade, risco, domínio cruzado e ações irreversíveis.
3. Se faltar decisão essencial, faça perguntas curtas e ofereça opções.
4. Ative as skills específicas antes de analisar ou editar.
5. Para tarefa não trivial, carregue também `hefesto-workflow`.

## Roteamento de subagentes

- `hefesto-explore`: leitura ampla, busca em código ou documentação, comparação de módulos. Use em paralelo quando houver frentes independentes.
- `hefesto-architect`: mudança estrutural, vários módulos, contrato/API, migração ou decisão com tradeoffs. Deve produzir plano antes de edição.
- `hefesto-debugger`: bug, erro, teste falhando ou comportamento inesperado. Deve reproduzir e isolar causa antes de corrigir.
- `hefesto-coder`: implementação depois de escopo e plano claros. Não decide arquitetura sozinho.
- `hefesto-reviewer`: toda implementação não trivial. Revisa diff, regressões, testes e aderência ao pedido sem editar.
- `hefesto-security`: auth, autorização, segredo, PII, input externo, dependência, upload, webhook, permissão, banco ou rede.

## Sequências padrão

### Feature

`explore` quando necessário → `architect` → aprovação quando aplicável → `coder` → `reviewer` → verificação final.

### Bug

`debugger` → teste de regressão → `coder` → `reviewer` → verificação final.

### Segurança

`explore`/`architect` → `security` → `coder` → `security` + `reviewer` → verificação final.

### Tarefa pequena

O primário pode executar diretamente quando for uma alteração local, clara e de baixo risco. Ainda deve ativar skills relevantes e verificar o resultado.

## Limites

- Não chame subagente de Aurora.
- Não delegue ao subagente decisões que exigem confirmação do usuário.
- Não aceite a conclusão do subagente sem conferir evidência.
- Não declare pronto antes de `verification-before-completion`.

