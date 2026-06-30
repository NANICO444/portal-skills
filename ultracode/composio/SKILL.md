---
name: composio
description: "Composio - integra OpenCode a 1000+ SaaS via MCP, CLI e triggers. Para automacoes com Gmail, Notion, GitHub, etc."
user-invocable: true
allowed-tools: Read, Bash
---

# Composio Skills + CLI

## O que e

Plataforma de integracao que conecta OpenCode/Claude a **mais de 1000 SaaS** via MCP, CLI e triggers. Inclui Gmail, Notion, GitHub, Slack, HubSpot, Salesforce, etc.

## Quando usar

- Integrar OpenCode com servicos externos
- Automatizar tarefas (enviar email, criar tarefa, atualizar planilha)
- Triggers de eventos (webhook → acao)
- Workflows multi-app

## Instalacao

```bash
# 1. Instalar skills
npx skills add composiohq/skills

# 2. Instalar CLI
curl -fsSL https://composio.dev/install | bash

# 3. Login
composio login

# 4. Inicializar projeto
composio init
```

## Git

- Repo: https://github.com/composiohq/skills

## Apps Suportados (exemplos)

- Gmail
- Notion
- GitHub
- GitLab
- Slack
- Discord
- HubSpot
- Salesforce
- Google Drive
- Google Calendar
- Trello
- Asana
- Linear
- Jira
- Stripe
- Shopify
- Airtable
- Sheets
- Docs
- ... 1000+

## Exemplo de uso

```python
# Conectar OpenCode ao Gmail via Composio
from composio import Composio

composio = Composio()
connection = composio.connections.create(app="gmail")

# Em uma skill do OpenCode:
"Encontre o ultimo email de joao@empresa.com e adicione ao Notion"
```

## Prompt de exemplo

```
Conecte OpenCode ao meu Gmail. Quando eu receber um email com anexo PDF,
salve o anexo no Google Drive e me avise no Slack.
Use a skill composio para configurar.
```

## Triggers

Composio suporta triggers (eventos que disparam acoes):
- Email recebido
- Mensagem no Slack
- Issue criada no GitHub
- Pagamento no Stripe
- ... e mais

## Complementa

- `.opencode/mcps/mcp.json` ja tem 9 MCPs (filesystem, github, git, etc)
- Composio adiciona 1000+ via um unico MCP
- Pode substituir varios MCPs manuais

## Precos (2026)

- Free: 1000 actions/mes
- Pro: 10k actions/mes
- Enterprise: custom
