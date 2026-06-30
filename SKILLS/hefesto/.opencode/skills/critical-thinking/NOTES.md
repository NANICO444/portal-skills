# NOTES — critical-thinking

**Tipo**: 🔧 adaptar
**Fonte**: Drive Ultra Prompt v6.2 — `skills/common/critical-thinking.md` (veio no kit em `04_baseline/drive_v62/common/critical-thinking.md`).
**Catálogo**: confirmado origem "Drive Ultra Prompt v6.2" — copiar do pacote local.

## O que adaptei
- Reformatei pro frontmatter Hermes (o original tinha cabeçalho próprio "# SKILL: ... # Versao ...").
- Corrigi acentuação PT-BR (o original estava sem acentos).
- Mantive o núcleo: 3 camadas, 6 regras, alternativas genuínas vs superficiais, criatividade dirigida (SCAMPER, diverge-converge), auto-avaliação, guardrail ético.
- **Condensei**: o original tinha seções extras (escala de qualidade 85-100%, priorização impacto/esforço, pensamento de adversário) — comprimi pra manter a skill focada e abaixo do tamanho ideal. A escala de qualidade e priorização são mais de execução/entrega; o essencial cognitivo ficou. Se Opus quiser, dá pra reexpandir.
- **Adicionei** links Hermes: `[[council]]`, `[[human-in-the-loop]]`, `[[pre-mortem]]` + tabela de modulação por cérebro alinhada ao baseline §2.1.

## Checklist model-agnóstico
- [x] Sem sintaxe Claude-específica.
- [x] Procedural, com checklists e tabelas objetivas.
- [x] Um DeepSeek seguiria sem problema.

## Pendências [VALIDAR]
- [VALIDAR: condensação aceitável?] — cortei escala de qualidade (85/90/95/100%) e matriz impacto×esforço do original v6.2 pra enxugar. Se essas partes forem consideradas essenciais ao "critical-thinking" no Hermes (e não a uma skill de execução separada), reincluir.
- [VALIDAR: "registrar a decisão"] — o original v6.2 dizia "registrar em WAL". Generalizei pra "registrar a decisão" porque WAL é um mecanismo específico que pode não existir igual no Hermes Agent. Confirmar se há um local canônico (WAL? DECISIONS.md? comentário no card?) pra registrar a decisão da Camada 2.
