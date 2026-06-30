---
name: react-best-practices
description: "Vercel React Best Practices - performance, memorizacao, SSR, RSC para React/Next.js"
user-invocable: true
allowed-tools: Read, Bash, Edit
---

# React Best Practices (Vercel)

## O que e

Regras oficiais da Vercel para performance, memorizacao, SSR, e React Server Components em React/Next.js.

## Quando usar

- Qualquer projeto React/Next.js
- Performance optimization
- Code review de UI
- Migracao para React Server Components

## Instalacao

```bash
# Via CLI de skills (Vercel-labs)
npx skills add https://github.com/vercel-labs/agent-skills --skill react-best-practices
```

## Git

- Repo: https://github.com/vercel-labs/agent-skills
- Skill: https://github.com/vercel-labs/agent-skills/tree/main/react-best-practices

## Processo de uso

1. Carregue a skill: `use skill:react-best-practices`
2. Aplique as regras em:
   - **Bundle size**: code splitting, dynamic imports
   - **Render**: memo, useMemo, useCallback
   - **Data fetching**: SWR, React Query, RSC
   - **Server Components**: quando usar, quando NAO usar
   - **Streaming**: Suspense, loading.tsx
   - **Image optimization**: next/image
   - **Font optimization**: next/font

## Prompt de exemplo

```
Crie um componente Next.js 15 com App Router que:
- Usa Server Components por padrao
- Client Component so onde precisa de interatividade
- Carrega dados com fetch + cache
- Otimiza imagens com next/image

Use a skill react-best-practices para garantir que segue as recomendacoes Vercel.
```

## Topico-chave: React Server Components (RSC)

| Tipo | Quando usar |
|------|-------------|
| Server Component | Default. Sem estado, sem eventos. Mais rapido. |
| Client Component | Quando tem `useState`, `useEffect`, ou event handlers |

## Performance

- `dynamic(() => import('./Heavy'))` para code splitting
- `next/image` ao inves de `<img>`
- `next/font` ao inves de Google Fonts
- `next/script` para scripts externos
- Streaming com `<Suspense>`

## Complementa skills existentes

- `frontend-patterns` (ja temos)
- `react-doctor` (ja temos)
- `taste-skill` (ja temos)

A skill Vercel pode ser mais autoritativa para projetos Next.js.
