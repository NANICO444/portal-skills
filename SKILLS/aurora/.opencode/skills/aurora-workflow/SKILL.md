---
name: aurora-workflow
description: Use em toda tarefa não trivial da Aurora para executar as 8 fases, da triagem automática de personas ao gate independente de acessibilidade, performance e realidade.
---

# Workflow nativo da Aurora

Nenhuma fase pode ser ignorada silenciosamente. Ajuste a profundidade ao tamanho do pedido, mas preserve os gates.

## FASE -1 - Triage de personas

- Carregue `aurora-routing`.
- Escolha personas e subagentes adequados.
- Registre domínio cruzado, riscos, dependências e perguntas.
- Para frentes independentes, use subagentes em paralelo.

## FASE 0 - Brief

- Ative `design-brief`.
- Confirme público, objetivo, canal, tom, restrições, conteúdo, CTA e critério de sucesso.
- Sem brief mínimo, pergunte antes de criar.

## FASE 1 - Mood

- Use `aurora-art-director`.
- Produza três direções visuais com função, tradeoffs e riscos.
- Evite visual genérico, ornamento vazio e tendência sem justificativa.
- Obtenha escolha ou aprovação quando a direção alterar significativamente o produto.

## FASE 2 - Tokens

- Defina cor, tipografia, espaçamento, raio, sombra, movimento e estados semânticos.
- Verifique contraste e legibilidade.
- Reuse o design system existente quando houver.

## FASE 3 - Componentes e conteúdo

- Defina componentes, estados, responsividade, conteúdo e stack.
- Use `aurora-content-brand` quando marca/copy fizerem parte.
- Especifique loading, erro, vazio, sucesso, hover, focus e disabled quando aplicável.

## FASE 4 - Build

- Use `aurora-frontend-builder`.
- Implemente frontend real, semântico, responsivo e mobile-first.
- Preserve contratos existentes e não invente backend.
- Use apenas STAGING quando houver deploy, sempre com confirmação.

## FASE 5 - Gate obrigatório

Invoque separadamente:

1. `aurora-accessibility-reviewer`;
2. `aurora-performance-reviewer`;
3. `aurora-reality-checker`.

Os três devem revisar a entrega real. Corrija bloqueios e repita os reviewers afetados. O builder não substitui nenhum reviewer.

## FASE 6 - Delivery

- Carregue `verification-before-completion`.
- Informe arquivos, evidência visual/técnica e resultado de cada reviewer.
- Separe o que foi medido do que foi apenas inferido.
- Liste riscos e itens `[VALIDAR]`.
- Não declare produção concluída; informe somente STAGING ou validação local.

