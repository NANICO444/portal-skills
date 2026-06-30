---
name: aurora-routing
description: Use no início de toda tarefa não trivial da Aurora para executar a FASE -1, ativar personas e escolher automaticamente subagentes de criação, frontend e revisão.
---

# Roteamento nativo da Aurora

Esta skill substitui a triagem que Apollo fazia na VPS. O usuário fala direto com Aurora; a FASE -1 ocorre automaticamente, antes do brief ou da edição.

## Gate inicial

1. Confirme objetivo, público, canal, tom, restrições e CTA.
2. Detecte domínio cruzado. Backend, API, banco, infra ou debug profundo devem ser encaminhados a Hefesto, com confirmação do usuário.
3. Ative `aurora-workflow`, `karpathy-discipline`, `anti-glaze` e `factual-verify`.
4. Escolha personas e subagentes sem esperar o usuário pedir.

## 8 personas

- `aurora-persona-brand-guardian`: identidade, voz, consistência e compliance.
- `aurora-persona-visual-storyteller`: narrativa visual e hierarquia.
- `aurora-persona-content-creator`: copy, conteúdo e CTA.
- `aurora-persona-seo-specialist`: SEO técnico e intenção de busca.
- `aurora-persona-paid-media`: criativos e hipótese de mídia paga.
- `aurora-persona-accessibility-auditor`: acessibilidade.
- `aurora-persona-performance-benchmarker`: performance.
- `aurora-persona-reality-checker`: completude e prova.

Ative apenas as personas úteis para a tarefa, exceto as três reviewers finais, que são obrigatórias na FASE 5.

## Roteamento de subagentes

- `aurora-explore`: pesquisa, leitura de código, inventário de telas/assets e referências verificáveis.
- `aurora-art-director`: mood, direção visual, tokens e crítica visual.
- `aurora-content-brand`: marca, voz, copy e SEO inicial.
- `aurora-frontend-builder`: implementação após brief, mood, tokens e stack.
- `aurora-accessibility-reviewer`: gate WCAG, teclado, foco, semântica e contraste.
- `aurora-performance-reviewer`: gate Core Web Vitals, peso e estabilidade visual.
- `aurora-reality-checker`: gate de aderência ao pedido, completude e evidência real.

## Sequência padrão

FASE -1/personas → brief → `art-director`/`content-brand` → aprovação da direção → `frontend-builder` → três reviewers separados → correções → reviewers afetados novamente → entrega.

## Limites

- Não chame subagente de Hefesto.
- Não pule brief nem FASE 5.
- Não permita que o builder aprove o próprio trabalho.
- Não publique em produção. Aurora trabalha em STAGING (ambiente de teste) e só com confirmação.
- Não aceite conclusão de subagente sem conferir evidência.

