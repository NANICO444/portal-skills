# NOTES — documentation-lookup

**Tipo**: 🔧 adaptar
**Fonte**: `affaan-m/everything-claude-code` — `skills/documentation-lookup/SKILL.md` (verbatim, GitHub main, 2026-05-29).
**Catálogo**: confirmado origem ECC — copiar `skills/documentation-lookup/SKILL.md`.

## O que adaptei
- PT-BR + frontmatter Hermes.
- Mantive o fluxo Context7 da fonte (resolve-library-id → escolher → query-docs, limite de 3 chamadas, redação de segredos).
- **ADIÇÃO IMPORTANTE — fallback Hermes**: a fonte ECC assume Context7 sempre presente. Não há garantia disso no Hermes. Adicionei um caminho de fallback usando as skills de pesquisa nativas do Hermes (doc-cache, doc-read, tavily-search, web-fetch, duckduckgo-search — todas listadas no baseline §3) com preferência por domínio oficial. Isso torna a skill útil mesmo sem Context7.
- **Integrei** com baseline: marcadores de confiança §2.4 (INCERTO se não achar), protocolo anti-alucinação §15.2 (nunca inventar URL, redigir segredos), link `[[factual-verify]]` e `[[native-mcp]]`.

## Checklist model-agnóstico
- [x] Sem sintaxe Claude-específica.
- [x] Ferramentas descritas por nome funcional (resolve-library-id, query-docs, tavily-search, web-fetch) — Regra #0.
- [x] Um DeepSeek seguiria sem problema.

## Pendências [VALIDAR]
- ⚠️ [VALIDAR: Context7 disponível no Hermes?] — a fonte depende do MCP Context7. Confirmar se algum cérebro Hermes tem Context7 configurado. Se NENHUM tiver, o fluxo preferencial vira morto e o fallback web vira o caminho principal — nesse caso, reescrever pra liderar com o fallback. Se TIVER, está ok como está.
- [VALIDAR: nomes das ferramentas de pesquisa] — usei tavily-search, web-fetch, doc-cache, doc-read, duckduckgo-search exatamente como no baseline §3. Confirmar que são os nomes reais das tools/skills no Hermes runtime.
