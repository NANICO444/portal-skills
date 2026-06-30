---
name: python-pro
description: "Python 3.12+ com async, performance, e ferramentas modernas (uv, ruff, FastAPI). Para AI, ciencia de dados, automacao, backend."
user-invocable: true
allowed-tools: Read, Bash, Edit
---

# Python Pro

## O que e

Skill focada em **Python moderno (3.12+)** com async, otimizacao de performance, e ferramentas atuais (uv, ruff, FastAPI, Pydantic).

## Quando usar

- Projetos Python novos
- Refatoracao de codigo Python legado
- AI/ML, ciencia de dados, automacao
- Backend API (FastAPI, Django, Flask)
- Scripts e ferramentas CLI

## Instalacao

```bash
# Via CLI de skills (Vercel-labs)
npx skills add https://github.com/rmyndharis/antigravity-skills --skill python-pro
```

## Git

- Repo: https://github.com/rmyndharis/antigravity-skills
- Skill: https://github.com/rmyndharis/antigravity-skills/tree/main/skills/python-pro

## Processo de uso

1. Carregue a skill: `use skill:python-pro`
2. Aplique as recomendacoes em:
   - Versao do Python (3.12+)
   - Type hints (PEP 604, 695)
   - Async (asyncio, anyio)
   - Packaging (uv, poetry, hatch)
   - Lint (ruff)
   - Test (pytest)
   - Framework web (FastAPI + Pydantic)

## Prompt de exemplo

```
Crie um endpoint FastAPI que recebe um JSON, valida com Pydantic v2, 
e retorna o resultado. Use async, type hints modernos, e testes pytest.
Use a skill python-pro para seguir as melhores praticas.
```

## Complementa skills existentes

- `test-driven-development` (ja temos)
- `python-testing` (ja temos)
- `python-async-patterns` (ja temos)
- `python-typing` (ja temos)

A skill `python-pro` pode sobrescrever/substituir essas se voce quiser padronizar.

## Stack recomendada (2026)

- **Gerenciador**: uv (substitui pip + poetry + venv)
- **Lint/Format**: ruff (substitui flake8 + black + isort)
- **Test**: pytest + pytest-asyncio + httpx
- **Web**: FastAPI + Pydantic v2 + Uvicorn
- **Async**: anyio (substitui asyncio direto)
- **Data**: polars (substitui pandas em performance)
