# NOTES — verification-before-completion

**Tipo**: 🔧 adaptar
**Fonte**: `obra/superpowers` — `skills/verification-before-completion/SKILL.md` (buscado verbatim do GitHub main em 2026-05-29). Licença do repo: MIT (verificar no repo).
**Catálogo**: confirmado origem Superpowers em `06_catalogo_skills/skills_origem_lookup.md`.

## O que adaptei (não copiei cego)
- Traduzi tudo pra PT-BR (regra #3).
- Mantive a estrutura forte do original (Lei de Ferro, gate function, tabelas de evidência, prevenção de racionalização) — é o coração da skill e funciona.
- **Removido**: a seção "From 24 failure memories" e a citação "If you lie, you'll be replaced" (eram específicas do contexto/persona do autor original do Superpowers). Substituí por uma seção "Por que isso importa" ancorada no sistema de pontos do Hermes.
- **Adicionei** integração Hermes: campo `metadata.verification` do `kanban_complete` (baseline §12), link com factual-verify, e a modulação de rigor por cérebro (baseline §3 tabela — Hefesto/Aurora/vps RÍGIDO).
- Generalizei pra model-agnóstico: nenhuma sintaxe Claude-específica. Exemplos são comandos genéricos (pytest, build, lint) que qualquer LLM segue.

## Checklist model-agnóstico
- [x] Sem `<thinking>` / tags Anthropic.
- [x] Sem referência a capacidade exclusiva de modelo.
- [x] Linguagem procedural (passos numerados, tabelas, critérios objetivos).
- [x] Um DeepSeek seguiria sem saber que um Claude escreveu.

## Pendências [VALIDAR]
- [VALIDAR: formato frontmatter Hermes vs Anthropic] — segui o formato dos exemplos bundled reais (`honcho_SKILL.md`, `ocr-and-documents_SKILL.md`): campos name, description, version, author: "Hermes Agent", license, platforms, metadata.hermes.{tags, related_skills}. Adicionei chave não-padrão `metadata.hermes.adapted_from` pra rastrear a fonte — confirmar se o Hermes Agent aceita campos extras em metadata.hermes (provavelmente sim, é namespace livre, mas Opus confirma).
- [VALIDAR: nome exato do campo no kanban_complete] — usei `metadata.verification` conforme baseline §12.1. Confirmar que é esse o nome no Hermes runtime.
