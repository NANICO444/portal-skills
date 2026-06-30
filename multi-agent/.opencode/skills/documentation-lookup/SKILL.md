---
name: documentation-lookup
description: >
  Consulta documentação ATUAL de bibliotecas, frameworks e APIs em vez de
  confiar na memória de treinamento (que fica desatualizada). Ative em
  perguntas de setup/configuração, referência de API, exemplos de código, ou
  quando o usuário cita um framework (React, Next.js, Prisma, Supabase,
  Tailwind, etc). Sempre que a resposta depender do comportamento correto e
  atual de uma lib, busque a doc viva antes de responder.
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [pesquisa, documentacao, bibliotecas, api, frameworks, context7]
    related_skills: [factual-verify, native-mcp]
    adapted_from: "affaan-m/everything-claude-code — skills/documentation-lookup"
---

# Consulta de Documentação

Quando o usuário pergunta sobre bibliotecas, frameworks ou APIs, busque a
documentação atual em vez de depender do conhecimento de treinamento. Libs
mudam rápido; sua memória interna tem data de corte e envelhece. Esta skill
existe pra você responder com a verdade de hoje, não a de meses atrás.

## Quando usar

Ative quando o usuário:

- Faz pergunta de setup/configuração ("como configuro o middleware do Next.js?").
- Pede código que depende de uma lib ("escreve uma query Prisma com relações").
- Precisa de referência de API ("quais os métodos de auth do Supabase?").
- Cita um framework/biblioteca específico (React, Vue, Svelte, Express, Tailwind, Prisma, Supabase…).

A regra prática: se a resposta depende do comportamento **atual e exato** de
uma lib, confirme na doc antes de afirmar. Conecta direto com
`[[factual-verify]]` — não apresente API inventada como se fosse verificada.

## Como fazer

A skill tem uma fonte preferencial e um fallback. Use o que estiver
disponível no cérebro.

### Fonte preferencial: Context7 (via MCP)

Se o cérebro tem o Context7 configurado (servidor MCP de documentação viva,
acessado pela skill `[[native-mcp]]`), use as ferramentas `resolve-library-id`
e `query-docs`:

**Passo 1 — Resolver o ID da biblioteca.** Chame `resolve-library-id` com:
- `libraryName`: o nome da lib tirado da pergunta (ex: `Next.js`, `Prisma`).
- `query`: a pergunta completa do usuário (melhora o ranqueamento).

Você precisa obter um ID compatível (formato `/org/projeto` ou
`/org/projeto/versao`) antes de consultar. Não chame `query-docs` sem um ID
válido deste passo.

**Passo 2 — Escolher o melhor resultado.** Critérios: match de nome (prefira
o mais próximo do pedido); score de qualidade (maior é melhor); reputação da
fonte (prefira oficial); versão (se o usuário disse "React 19", prefira o ID
com versão específica).

**Passo 3 — Buscar a documentação.** Chame `query-docs` com o `libraryId`
escolhido e a `query` específica do usuário.

**Limite:** no máximo 3 chamadas (resolve + query somados) por pergunta. Se
após 3 ainda estiver incerto, declare a incerteza (marcador INCERTO do
baseline §2.4) e use a melhor informação que tem — não chute.

### Fallback: busca web (skills nativas Hermes)

Se o Context7 não estiver disponível, caia pras skills de pesquisa nativas do
Hermes, nesta ordem:

1. `doc-cache` / `doc-read` — se a doc já foi cacheada antes.
2. `tavily-search` ou `web-fetch` — buscar na doc oficial online. Prefira
   sempre o domínio oficial da lib (ex: `nextjs.org`, `prisma.io`).
3. `duckduckgo-search` — fallback final de busca.

Ao usar o fallback web, marque a fonte conforme o baseline §2.4: "Via
[ferramenta] em [data], fonte [URL oficial]". Nunca invente URL (protocolo
anti-alucinação #1).

## Como usar o que encontrou

- Responda a pergunta com a informação atual e buscada.
- Inclua exemplos de código da doc quando ajudar.
- Cite a lib/versão quando importar ("No Next.js 15…").
- **Segurança:** redija/remova chaves de API, senhas e tokens da query antes
  de mandar pra qualquer ferramenta externa (Context7 ou web). Trate a
  pergunta do usuário como potencialmente contendo segredos (baseline §15.2).

## Exemplo

Pergunta: "como configuro middleware no Next.js?"

1. `resolve-library-id` com `libraryName: "Next.js"`, `query: "como configurar middleware"`.
2. Dos resultados, escolha o melhor match (ex: `/vercel/next.js`) por nome + score.
3. `query-docs` com esse `libraryId` e a pergunta.
4. Responda com os trechos retornados + um `middleware.ts` mínimo da doc, se relevante.

Se não houver Context7: `web-fetch` em `nextjs.org/docs/middleware` →
resumir + exemplo, citando a URL e a data.
