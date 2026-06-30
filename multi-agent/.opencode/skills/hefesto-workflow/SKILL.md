---
name: hefesto-workflow
description: Use em toda tarefa técnica não trivial do Hefesto para executar as 7 fases obrigatórias, com Karpathy rígido, aprovação, testes, revisão e evidência final.
---

# Workflow nativo do Hefesto

Nenhuma fase pode ser ignorada silenciosamente. Em tarefa simples, fases podem ser curtas, mas continuam presentes.

## FASE 0 - Triage

- Classifique complexidade e risco.
- Confirme se o pedido pertence ao domínio técnico.
- Se for design/UX/UI, avise que Aurora é mais adequada e peça confirmação.
- Ative `hefesto-routing`, `karpathy-discipline` e as skills específicas.

## FASE 1 - Requirements

- Leia código, documentação e estado real antes de sugerir.
- Separe objetivo, escopo, fora de escopo e critérios de aceite.
- Em pedido ambíguo ou grande, faça perguntas e proponha 1 a 3 opções.
- Marque fatos relevantes como VERIFICADO, INFERIDO, INCERTO ou DESCONHECIDO.

## FASE 2 - Architecture

- Use `hefesto-architect` para mudança não trivial.
- Defina contratos, dependências, impacto, rollback e testes.
- Prefira o padrão já existente no projeto.
- Aplique Karpathy rígido: solução mínima, clara e sem abstração prematura.

## FASE 3 - Plan e aprovação

- Apresente passos verificáveis.
- Peça aprovação antes de mudança grande, destrutiva, cara ou fora do escopo explícito.
- Registre o que não será alterado.

## FASE 4 - Implementation

- Use `hefesto-coder` quando houver unidade de implementação separável.
- Para feature ou bug reproduzível, use TDD (teste falha, implementação mínima, teste passa).
- Mantenha a alteração pequena e aderente ao estilo local.
- Não instale dependência sem justificar.

## FASE 5 - Testing e review

- Rode build, testes, lint e tipos disponíveis no projeto.
- Use `hefesto-reviewer` em toda mudança não trivial.
- Use `hefesto-security` quando houver gatilho de segurança.
- Corrija bloqueios e repita as verificações afetadas.

## FASE 6 - Delivery

- Carregue `verification-before-completion`.
- Informe o que mudou, arquivos principais, comandos executados e resultados.
- Separe validação local de prova em runtime.
- Declare risco residual e itens `[VALIDAR]`.
- Nunca diga "pronto" sem evidência recente.

