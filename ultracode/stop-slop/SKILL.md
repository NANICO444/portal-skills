---
name: stop-slop
description: "Limpa textos gerados por IA em docs, READMEs e notas. Remove phrases genericas, em dashes, e AI-isms."
user-invocable: true
allowed-tools: Read, Write, Edit
---

# Stop Slop

## O que e

Skill que **limpa textos gerados por IA**, removendo:
- Em dashes (—)
- Phrases genericas ("In today's fast-paced world...")
- AI-isms ("Let's dive in", "It's worth noting")
- Listas de bullet excessivas
- Tom corporativo vazio

## Quando usar

- Apos gerar qualquer texto longo (README, doc, commit)
- Antes de publicar conteudo
- Para melhorar qualidade de documentacao
- Em revisores de PR

## Instalacao

```bash
mkdir -p ~/.agents/skills && git clone https://github.com/hardikpandya/stop-slop.git ~/.agents/skills/stop-slop
```

## Git

- Repo: https://github.com/hardikpandya/stop-slop

## Processo de uso (3 etapas)

### 1. Detectar
Procure por:
- Em dashes (—)
- "Certainly", "It's worth noting", "Let's dive in"
- "In conclusion", "To summarize"
- "Navigate the complexities"
- "Robust", "seamless", "cutting-edge" sem contexto

### 2. Remover
- Reescreva sem o AI-speak
- Use linguagem direta
- Conecte ideias com palavras simples

### 3. Validar
- Leia em voz alta
- Pergunte: "humano diria isso?"
- Corta o que nao agrega

## Antes/Depois

**Antes (AI-generated):**
> In today's fast-paced digital landscape, navigating the complexities of modern web development can be a daunting task. It's worth noting that robust solutions are essential for success.

**Depois (limpo):**
> Web development eh complexo. Solucoes robustas sao essenciais.

## Prompt de exemplo

```
Revise este README e remova todos os AI-isms.
Use a skill stop-slop para garantir:
- Sem em dashes
- Sem frases genericas
- Linguagem direta
- Tom humano
```

## Complementa

- `anti-glaze` (ja temos) - similar, focado em UX enganoso
- `karpathy-discipline` (ja temos) - simplicidade
- `impeccable-quality` (ja temos) - qualidade geral

Stop-slop eh especificamente sobre TEXTO, nao sobre codigo ou UX.
