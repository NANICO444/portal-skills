# NOTES — human-in-the-loop

**Tipo**: 🔧 adaptar
**Fonte**: Drive Ultra Prompt v6.2 — `skills/common/human-in-the-loop.md` (veio no kit em `04_baseline/drive_v62/common/`).
**Catálogo**: confirmado origem "Drive Ultra Prompt v6.2" — copiar do pacote local.

## O que adaptei
- Frontmatter Hermes + acentuação PT-BR corrigida.
- Mantive integralmente o núcleo: árvore perguntar-vs-decidir, tabela de exemplos, batching, níveis de confirmação, timeout, feedback mid-execution, escalonamento.
- **Adicionei** integração Hermes: aprovação em cascata (baseline §16) com `kanban_block`, modo crítico (§14), e links `[[critical-thinking]]`, `[[council]]`, `[[pre-mortem]]`, `[[context-snapshot]]`.
- Generalizei "compactação iminente → salvar estado" apontando pra context-snapshot (skill do Lote B) em vez de detalhe de mecanismo.

## Checklist model-agnóstico
- [x] Sem sintaxe Claude-específica.
- [x] Procedural (árvore de decisão, tabelas, templates).
- [x] Um DeepSeek seguiria sem problema.

## Pendências [VALIDAR]
- [VALIDAR: `kanban_block` assinatura] — usei `kanban_block(reason="...")` conforme baseline §16. Confirmar nome/assinatura exata da ferramenta no Hermes Agent.
- [VALIDAR: janela de 24h] — o "sem resposta em 24h → block" vem do baseline §16. Confirmar se esse SLA é fixo ou modulável por cérebro.
- Link `[[context-snapshot]]` aponta pra skill do Lote B (ainda não gerada) — esperado, é forward-link.
