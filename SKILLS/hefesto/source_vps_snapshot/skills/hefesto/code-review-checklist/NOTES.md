# NOTES — code-review-checklist

**Tipo**: 🆕 criar do zero (Hefesto)
**Fonte da spec**: hefesto_skills_list #46 "A CRIAR (checklist anti-blind-spot do modelo médio)" + índice "base nos 20 anti-patterns do hefesto/playbook §8".
**Base de princípios**: `wshobson/agents` code-review-excellence (busquei verbatim) — usei os princípios de feedback (específico/educativo/priorizado), não copiei.
**Inventário 771**: não consta → criar do zero correto.

## O que fiz
- Foco no diferencial pedido: **anti-blind-spot** — os pontos cegos que LLM/revisor cansado deixam passar. Checklist organizado por categoria (correção/edge cases, segurança, concorrência, robustez, manutenção) com ⚠️ nas que mais escapam.
- Integrei princípios de feedback da base wshobson (priorizar [crítico]/[importante]/[nit], reconhecer o bom sem bajular).
- Amarrei forte ao baseline: segredos §15.2, código morto §15.3 #15, TODO sem card §10, régua RÍGIDA Hefesto.
- Exemplo de review formatado com bloqueadores vs nits + veredito.

## Checklist model-agnóstico
- [x] Sem sintaxe Claude-específica.
- [x] Procedural + checklist + exemplo.
- [x] Um DeepSeek seguiria sem problema.

## Pendências [VALIDAR]
- ⚠️ [VALIDAR: anti-patterns hefesto/playbook §8] — a spec referencia "20 anti-patterns" do playbook do Hefesto, que NÃO está neste kit. Meu checklist cobre as categorias principais por conhecimento geral de code review, mas precisa ser cruzado com a lista literal do playbook §8 quando disponível, pra garantir cobertura dos 20. Marquei isso na própria skill.
- Nenhum ponto sensível (é review, não executa nada).
