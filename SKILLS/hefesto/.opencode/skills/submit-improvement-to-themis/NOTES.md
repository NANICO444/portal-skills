# NOTES — submit-improvement-to-themis

**Tipo**: 🆕 criar do zero (universal — todos os cérebros)
**Fonte da spec**: common_baseline §3 #20 + themis_skills_list (universal #20 + receiver `improvement-consolidator`).
**Inventário 771**: não consta → criar do zero está correto.

## O que fiz
- Skill universal de ENVIO. Themis é o único receptor (via improvement-consolidator). Estruturei: tipo, pacote com campos (origem/tipo/titulo/descricao/evidencia/impacto/confianca/urgencia), envio, registro.
- Amarrei aos princípios do sistema: não aplicar a mudança sozinho (§15.1 #1), evidência obrigatória (factual-verify + anti-glaze), limite extra do Midas (§15.4 — escala infraestrutura pro Miguel).
- Campo `confianca` usa os marcadores do factual-verify (coerência sistêmica).
- Links: self-improvement-tracker (acumula fricção→proposta), find-skills (descobre→propõe), critique-with-evidence.

## Checklist model-agnóstico
- [x] Sem sintaxe Claude-específica.
- [x] Procedural + template de pacote + exemplo.
- [x] Midas (não Jarvis) — já corrigido na fonte pelo Opus; usei Midas.

## Ajuste do Lote B (aplicado — Opus definiu o contrato)
- ✅ TRANSPORTE definido: `kanban_create(assignee="themis", board="improvements", title=..., body=...)`. Kanban (rastreável) em vez de msg solta.
- ✅ SCHEMA do body fixado (exato, pra casar com improvement-consolidator):
  `origem_cerebro / categoria / problema / sugestao / evidencia / prioridade_sugerida`.
  `categoria` ∈ seguranca|performance|ux|fluxo|skill|custo|outro. `title` = resumo curto.
- Reescrevi a seção "Como fazer" e o exemplo pra produzir EXATAMENTE esse schema.

## Pendências [VALIDAR]
- [VALIDAR: contrato confirmado pelo improvement-consolidator quando criado em S3a] — o contrato foi definido pelo Opus e registrado no projeto; confirmar o casamento final quando o receiver (custom Themis) for implementado.
- [VALIDAR: codinomes de origem] — apollo/midas/hefesto/aurora/atlas/themis. Confirmar nomes técnicos finais (atlas = hermes-vps? themis = hermes-conductor?).
