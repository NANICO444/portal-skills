---
name: mcp-builder
description: "Guia Anthropic para criar servidores MCP em TypeScript ou Python. Cobre Zod/Pydantic e testes de avaliacao."
user-invocable: true
allowed-tools: Read, Write, Bash
---

# MCP Builder (Anthropic)

## O que e

Guia oficial para **criar servidores MCP (Model Context Protocol)** de alta qualidade. Cobre design de API, schemas (Zod/Pydantic), e testes de avaliacao.

## Quando usar

- Criar um servidor MCP novo
- Melhorar um MCP existente
- Auditar seguranca de um MCP
- Quando precisa integrar OpenCode/Claude com servico externo

## Instalacao

```bash
# Via CLI de skills
npx skills add https://github.com/anthropics/skills --skill mcp-builder
```

## Git

- Repo: https://github.com/anthropics/skills
- Skill: https://github.com/anthropics/skills/tree/main/skills/mcp-builder

## Processo de uso (4 fases)

### 1. Planejar a API
- Quais tools/resources o MCP expoe?
- Quais schemas?
- Qual granularidade?

### 2. Implementar

**Em TypeScript:**
```typescript
import { z } from "zod";
import { createServer } from "@modelcontextprotocol/sdk/server/stdio";

const server = createServer({...});

server.tool("search", {
  query: z.string().describe("Search query"),
  limit: z.number().optional().default(10)
}, async ({ query, limit }) => {
  // ...
});
```

**Em Python:**
```python
from mcp.server import Server
from pydantic import BaseModel, Field

app = Server("my-mcp")

@app.tool()
async def search(query: str, limit: int = 10) -> list[dict]:
    """Search for items."""
    # ...
```

### 3. Testar
- Casos de borda
- Schemas validos/invalidos
- Erros de rede
- Timeouts

### 4. Publicar
- npm publish (TS)
- PyPI (Python)
- Documentar tools e schemas

## Prompt de exemplo

```
Crie um servidor MCP em TypeScript que expoe ferramentas para:
- Buscar produtos (query, limit)
- Adicionar ao carrinho (productId, quantity)
- Ver carrinho atual

Use a skill mcp-builder para seguir as melhores praticas de design de API.
```

## Boas praticas

- Schemas descritivos (use `.describe()` ou `Field(description=...)`)
- Mensagens de erro claras
- Logs estruturados
- Rate limiting
- Autenticacao (se aplicavel)
- README com exemplos de uso

## Complementa

- O projeto ja tem `.opencode/mcps/mcp.json` com 9 MCPs pre-configurados
- Esta skill ajuda a CRIAR novos MCPs customizados
