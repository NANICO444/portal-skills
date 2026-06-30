---
name: cloudflare
description: "Cloudflare skills - Workers, Pages, D1, R2, KV, Durable Objects, IA Cloudflare"
user-invocable: true
allowed-tools: Read, Write, Bash
---

# Cloudflare Skills

## O que e

Skills oficiais da Cloudflare para usar o ecossistema completo: Workers, Pages, D1 (SQL), R2 (storage), KV (key-value), Durable Objects, AI, Vectorize, etc.

## Quando usar

- Deploy de aplicacao na Cloudflare
- Edge computing
- IA com modelos da Cloudflare
- Storage serverless (R2)
- Banco SQL serverless (D1)
- Real-time (Durable Objects)

## Instalacao

```bash
# Via CLI de skills
npx skills add https://github.com/cloudflare/skills
```

## Git

- Repo: https://github.com/cloudflare/skills

## Servicos disponiveis

| Servico | Quando usar |
|---------|-------------|
| **Workers** | Compute edge (Node, JS, Python, WASM) |
| **Pages** | Sites estaticos + functions |
| **D1** | SQLite serverless |
| **R2** | Object storage (S3-compatible) |
| **KV** | Key-value (eventualmente consistente) |
| **Durable Objects** | Stateful real-time |
| **Vectorize** | Vector database (RAG) |
| **AI** | LLMs (Llama, Mistral, etc) |
| **Workers AI** | Inferencia de IA na edge |
| **Queues** | Filas assincronas |
| **Stream** | Video ao vivo |
| **Tunnel** | Conectar servicos sem expor portas |

## Prompt de exemplo

```
Crie uma API serverless que:
- Lista produtos de um banco D1
- Cache em KV por 5 minutos
- Gera embeddings com Workers AI
- Salva no Vectorize para busca semantica

Use a skill cloudflare para seguir as melhores praticas.
```

## Limites (free tier 2026)

- Workers: 100k requests/dia
- D1: 5GB storage, 5M reads/dia
- R2: 10GB storage, 1M Class A operations
- KV: 100k reads/dia
- AI: 10k neurons/dia

## Complementa

- `devops` (agent do multi-agent)
- `deployment-automation` (skill)
- MCPs: pode expor Cloudflare como MCP para OpenCode
