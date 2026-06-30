# NOTES — council

**Tipo**: 🔧 adaptar
**Fonte**: `affaan-m/everything-claude-code` — `skills/council/SKILL.md` (buscado verbatim do GitHub main em 2026-05-29).
**Catálogo**: confirmado origem ECC — copiar `skills/council/SKILL.md`.

## O que adaptei
- PT-BR + frontmatter Hermes.
- Mantive o melhor da fonte ECC: o mecanismo anti-ancoragem (cada voz recebe só pergunta+contexto, não a conversa toda), formar a posição própria PRIMEIRO, guardrails de viés na síntese, o formato compacto de veredito, e a tabela "quando NÃO usar".
- **DIVERGÊNCIA IMPORTANTE nas 4 vozes** — ver [VALIDAR] abaixo. ECC usa Architect/Skeptic/Pragmatist/Critic. O baseline Hermes §13 manda pragmático/cético/idealista/técnico. Segui o baseline (Hermes é autoritativo), mapeando: Pragmático≈Pragmatist, Cético≈Skeptic, Idealista≈Architect (longo prazo/melhor solução), Técnico≈Critic (edge cases/falhas).
- **Removido**: referências a skills específicas do ECC que não existem no Hermes (`santa-method`, `knowledge-ops`, `search-first`, `architecture-decision-records`, `/save-session`, `~/.claude/notes`). Substituí por skills Hermes equivalentes nos links.
- **Generalizei o subagente**: ECC assume subagentes paralelos (Claude Code). Reescrevi pra "se tem subagente disponível, use; senão, raciocine cada papel isolado" — model-agnóstico.

## Checklist model-agnóstico
- [x] Sem sintaxe Claude-específica.
- [x] Não assume tooling de subagente específico (oferece fallback).
- [x] Um DeepSeek seguiria sem problema.

## Pendências [VALIDAR]
- ⚠️ [VALIDAR: nomes das 4 vozes] — usei pragmático/cético/idealista/técnico (baseline §13). A fonte ECC usava Architect/Skeptic/Pragmatist/Critic. Confirmar qual conjunto é o oficial Hermes. Se o baseline §13 for autoritativo (creio que sim), está correto; se preferirem o set ECC, trocar "Idealista"→"Arquiteto" e revisar as lentes.
- [VALIDAR: subagente no Hermes] — Hermes tem `subagent-driven-development` nativo. Confirmar se council deve invocar subagentes reais por padrão (e como) ou se o raciocínio isolado inline é aceitável pro executor DeepSeek.
- [VALIDAR: persistência de decisão] — onde registrar uma decisão de council que vira política? (DECISIONS.md do projeto? memória? card?). Deixei genérico.
