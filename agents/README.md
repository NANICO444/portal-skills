# agents/ — Frameworks de Agentes 2026

> **Curadoria dos melhores frameworks para construir agentes autônomos com LLMs.**
> Pesquisa completa em [`best_agent_frameworks.md`](best_agent_frameworks.md)

## Conteúdo

| Arquivo | Tamanho | Descrição |
|---------|---------|-----------|
| `best_agent_frameworks.md` | ~35KB | Relatório completo: 15 frameworks analisados, comparativos, tabelas, recomendações |

## Frameworks Cobertos

| # | Framework | Tipo | Melhor Para |
|---|-----------|------|-------------|
| 1 | **LangChain / LangGraph / Deep Agents** | Ecossistema completo | Workflows stateful complexos, observabilidade |
| 2 | **CrewAI** | Multi-agent role-based | Prototipagem rápida, papéis definidos |
| 3 | **Microsoft Agent Framework** | Unificado (AutoGen+SK) | Empresas .NET/Azure, governança |
| 4 | **OpenAI Agents SDK** | Provider-native | OpenAI-first, handoffs leves |
| 5 | **Google ADK** | Provider-native | GCP, multimodal, A2A |
| 6 | **Claude Agent SDK** | Provider-native | Agentes de código, acesso a OS |
| 7 | **AWS Strands Agents** | Provider-native | Lambda, serverless, AWS |
| 8 | **Mastra** | TypeScript-first | Next.js, web apps full-stack |
| 9 | **Smolagents (Hugging Face)** | Minimalista code-first | Experimentos, GAIA #1 open-source |
| 10 | **LlamaIndex Workflows** | RAG-first | Recuperação de dados |
| 11 | **PydanticAI** | Type-safe Python | Outputs validados |
| 12 | **Agno (ex-Phidata)** | Tool-centric | APIs e bases de dados |
| 13 | **AG2 (AutoGen fork)** | Conversacional | Pesquisa multi-agente |
| 14 | **Dify** | Visual/no-code | Equipes não-técnicas |
| 15 | **AutoGPT** | Autônomo | Experimentação histórica |

## Recomendação Rápida

| Seu Perfil | Framework |
|------------|-----------|
| Protótipo rápido multi-agente | **CrewAI** |
| Workflow production complexo | **LangGraph** |
| Empresa .NET / Microsoft | **Microsoft Agent Framework** |
| Google Cloud | **Google ADK** |
| AWS | **AWS Strands** |
| Agente que edita código/acessa OS | **Claude Agent SDK** |
| OpenAI-first | **OpenAI Agents SDK** |
| TypeScript / Next.js | **Mastra** |
| Aprendizado / experimentos | **Smolagents** |

## Notas

- Nenhum framework foi instalado automaticamente. Consulte `best_agent_frameworks.md` para instruções de instalação.
- Frameworks com MCP nativo podem ser integrados diretamente no `opencode.jsonc` como servidores MCP.
- O Claude Agent SDK tem a maior compatibilidade com OpenCode por compartilhar o mesmo harness do Claude Code.
