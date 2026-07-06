# Best AI Agent Frameworks 2026 — Relatório Completo

> **Data da pesquisa**: Junho 2026  
> **Frameworks analisados**: 15  
> **Fontes**: Artigos comparativos, benchmarks, documentação oficial, posts técnicos  
> **Formato de citação**: `【fonte→título】`

---

## Sumário Executivo

O ecossistema de frameworks de agentes amadureceu dramaticamente entre 2024 e 2026. De um punhado de bibliotecas experimentais, evoluiu para **três categorias principais**:

1. **SDKs nativos de provedores** — Claude Agent SDK, OpenAI Agents SDK, Google ADK, AWS Strands, Microsoft Agent Framework  
2. **Frameworks independentes multi-provedor** — LangChain/LangGraph, CrewAI, LlamaIndex, Mastra  
3. **Frameworks leves/especializados** — Smolagents, PydanticAI, Agno, Dify, AutoGPT  

"Nenhum framework de IA agêntica é universalmente correto. LangGraph vence em orquestração stateful. CrewAI vence em tempo-para-primeiro-agente. Semantic Kernel vence dentro de shops .NET."【Inductivee→Agentic AI Frameworks 2026】

---

## Índice

1. [LangChain / LangGraph / Deep Agents (Ecossistema LangChain)](#1-ecossistema-langchain)
2. [CrewAI](#2-crewai)
3. [Microsoft Agent Framework](#3-microsoft-agent-framework)
4. [OpenAI Agents SDK](#4-openai-agents-sdk)
5. [Google ADK (Agent Development Kit)](#5-google-adk)
6. [Claude Agent SDK (Anthropic)](#6-claude-agent-sdk)
7. [AWS Strands Agents](#7-aws-strands-agents)
8. [Mastra](#8-mastra)
9. [Smolagents (Hugging Face)](#9-smolagents)
10. [LlamaIndex Workflows](#10-llamaindex-workflows)
11. [PydanticAI](#11-pydanticai)
12. [Agno (ex-Phidata)](#12-agno)
13. [AG2 (AutoGen Community Fork)](#13-ag2)
14. [Dify](#14-dify)
15. [AutoGPT](#15-autogpt)
16. [Comparativo Final](#16-comparativo-final)
17. [Como Integrar ao OpenCode](#17-integração-com-opencode)

---

## 1. Ecossistema LangChain

### LangChain
| Atributo | Detalhe |
|----------|---------|
| **Tipo** | LLM application framework |
| **Linguagens** | Python, TypeScript |
| **Licença** | MIT |
| **GitHub** | 131.7k stars, 223.8M PyPI downloads/mês |
| **Criado por** | LangChain Inc. |

**O que faz**: Framework mais estabelecido para construção de aplicações LLM. Oferece milhares de integrações com modelos, ferramentas, vectores stores e sistemas externos. Ideal para prototipagem rápida de fluxos agenticos complexos. "Choose LangChain if you need an open-source framework for rapid prototyping across model providers."【LangChain→Best AI agent frameworks 2026】

**Quando usar**: Prototipagem rápida, troca frequente de modelos, necessita de amplo ecossistema de integrações.

**Trade-offs**: Não é otimizado para stateful workflows complexos (para isso existe LangGraph). "LangChain... não é a melhor escolha para fluxos com branches, loops e checkpointing."【Alice Labs→Open Source AI Agent Frameworks Comparison 2026】

### LangGraph
| Atributo | Detalhe |
|----------|---------|
| **Tipo** | Agent runtime / State machine |
| **Linguagens** | Python, TypeScript |
| **Licença** | MIT |
| **GitHub** | 16k+ stars |
| **Melhor para** | Workflows stateful complexos |

**O que faz**: LangGraph modela sistemas agênticos como grafos direcionados. Cada nó é uma função ou subagente; as arestas carregam estado tipado. Oferece checkpointing com time-travel replay — o padrão ouro para durabilidade em produção. "LangGraph is the strongest choice for complex stateful workflows with branching, checkpointing, and human-in-the-loop."【Inductivee→Agentic AI Frameworks 2026】 "LangGraph wins on stateful control and observability via LangSmith."【Alice Labs→Open Source AI Agent Frameworks Comparison 2026】

**Quando usar**: Fluxos com branches, paralelismo, retry, aprovação humana, observabilidade profunda.

**Trade-offs**: "You write more code per feature — there is no `Crew([researcher, writer])` shorthand here." [Agent Guides→AI Agent Frameworks 2026] Curva de aprendizado mais alta.

### Deep Agents
| Atributo | Detalhe |
|----------|---------|
| **Tipo** | Agent harness (opinionated) |
| **Linguagens** | Python, TypeScript |
| **Licença** | MIT |
| **GitHub** | 24.4k stars |

**O que faz**: "Deep Agents is an opinionated agent harness that runs out of the box — planning, context management, and multi-agent orchestration for long-running tasks."【GitHub→langchain-ai/deepagents】 Construído sobre LangGraph, oferece defaults para tarefas de longo horizonte.

**Quando usar**: "Use Deep Agents when you want the full harness — planning, context management, delegation — out of the box." Long-running workflows como research e análise multi-step.

### Instalação
```bash
# LangChain
pip install langchain
npm install langchain

# LangGraph
pip install langgraph
npm install @langchain/langgraph

# Deep Agents
pip install deepagents
```

### Integração OpenCode
```jsonc
// opencode.jsonc — MCP para LangGraph
{
  "mcpServers": {
    "langgraph-platform": {
      "type": "url",
      "url": "https://your-langgraph-cloud-url.com"
    }
  }
}
```

---

## 2. CrewAI

| Atributo | Detalhe |
|----------|---------|
| **Tipo** | Multi-agent orchestration framework |
| **Linguagens** | Python |
| **Licença** | MIT |
| **GitHub** | 52.4k+ stars, 6.39M PyPI downloads/mês |
| **Melhor para** | Prototipagem rápida de agentes baseados em papéis |

**O que faz**: CrewAI permite definir agentes com papéis (roles), tarefas (tasks) e processos (crews). A abstração role/task mapeia diretamente para como equipes de produto descrevem trabalho — cada agente tem `role`, `goal`, `backstory`, e as tarefas são atribuídas aos agentes. "CrewAI wins on time-to-first-agent and role-based clarity."【Inductivee→Agentic AI Frameworks 2026】

**Quando usar**: "Best framework for prototypes, demos, and pipelines where the flow is roughly linear."【Agent Guides→AI Agent Frameworks 2026】 Projetos onde o trabalho se decompõe naturalmente em papéis (pesquisador, escritor, revisor).

**Trade-offs**: "CrewAI is production-ready for bounded, role-based multi-agent workflows... For more complex stateful workflows that require explicit branching, checkpointing, and deep observability, LangGraph is currently a more robust choice."【Inductivee→Agentic AI Frameworks 2026】 Muitos deployments enterprise migram para LangGraph quando a complexidade cresce.

### Instalação
```bash
pip install crewai
pip install 'crewai[tools]'
```

### Integração OpenCode
```jsonc
// opencode.jsonc — usar CrewAI como skill
{
  "skills": {
    "crewai-agent": {
      "description": "Cria e executa crews de agentes multi-papéis"
    }
  }
}
```

```python
# Exemplo: crew para pesquisa + escrita
from crewai import Agent, Task, Crew

researcher = Agent(role="Pesquisador", goal="Encontrar informação relevante")
writer = Agent(role="Escritor", goal="Sintetizar em relatório claro")

research_task = Task(description="Pesquisar tópico X", agent=researcher)
write_task = Task(description="Escrever relatório", agent=writer)

crew = Crew(agents=[researcher, writer], tasks=[research_task, write_task])
result = crew.kickoff()
```

---

## 3. Microsoft Agent Framework

| Atributo | Detalhe |
|----------|---------|
| **Tipo** | Multi-agent orchestration framework (unificado) |
| **Linguagens** | Python, .NET (C#) |
| **Licença** | MIT |
| **Versão** | 1.0 GA (abril 2026) |
| **Sucessor de** | AutoGen + Semantic Kernel |

**O que faz**: "Microsoft Agent Framework is the unified successor to AutoGen and Semantic Kernel, built by the same teams. It combines AutoGen's conversational multi-agent abstractions with Semantic Kernel's enterprise features (session-based state management, middleware, telemetry, and type safety) and adds graph-based workflows for explicit control over multi-agent execution paths."【LangChain→Best AI agent frameworks 2026】

"Version 1.0 represents the features we've battle-tested, stabilized, and committed to supporting with full backward compatibility."【Microsoft DevBlogs→Microsoft Agent Framework Version 1.0】

**Recursos principais**:
- Graph-based workflows (sequential, concurrent, handoff, group chat, Magentic-One)
- Checkpointing, human-in-the-loop, pause/resume
- Multi-provider (Azure OpenAI, OpenAI, Anthropic, AWS Bedrock, Ollama)
- Middleware para interceptação de ações
- OpenTelemetry nativo
- Suporte a A2A, AG-UI e MCP

**Quando usar**: "Choose Microsoft Agent Framework if you're on the Microsoft stack and want the unified successor to AutoGen and Semantic Kernel." Ambientes enterprise .NET, compliance, governança.

**Trade-offs**: Fora do ecossistema Microsoft, LangGraph ou CrewAI oferecem vantagens. "Semantic Kernel is less capable than LangGraph or CrewAI for complex multi-agent orchestration."【AI Agent Brief→LangChain vs CrewAI vs AutoGen vs Semantic Kernel 2026】

### Instalação
```bash
# Python
pip install microsoft-agent-framework

# .NET
dotnet add package Microsoft.Agent.Framework
```

### Integração OpenCode
```jsonc
// opencode.jsonc
{
  "mcpServers": {
    "microsoft-agent-framework": {
      "type": "command",
      "command": "python",
      "args": ["-m", "agent_framework.mcp_server"]
    }
  }
}
```

---

## 4. OpenAI Agents SDK

| Atributo | Detalhe |
|----------|---------|
| **Tipo** | Multi-agent workflow SDK |
| **Linguagens** | Python, TypeScript |
| **Licença** | MIT |
| **GitHub** | ~25.9k stars |
| **Melhor para** | Lightweight handoff chains, integração OpenAI |

**O que faz**: "OpenAI Agents SDK is the fastest way from zero to working agent."【Pockit→OpenAI Agents SDK vs Google ADK vs LangGraph 2026】 Oferece handoffs entre agentes, guardrails de três níveis, sandbox execution e suporte a 100+ modelos via Responses API. "OpenAI Agents SDK offers the cleanest multi-agent delegation model with its handoff system and three-tier guardrails."【DeepResearch Ninja→AI Agent Frameworks Comparative Analysis 2026】

**Recursos**: Computer Use tool (GA), Tool Search (dynamic loading), WebSocket transport, MCP integration. "Assistants API sunset announced for August 2026, pushing everyone toward the Responses API + Agents SDK stack."【Pockit→OpenAI Agents SDK vs Google ADK vs LangGraph 2026】

**Quando usar**: Times comprometidos com OpenAI, protótipos rápidos, fluxos lineares de delegação.

**Trade-offs**: Otimizado para ecossistema OpenAI. Handoffs mais simples que LangGraph. "For more complex stateful workflows, LangGraph offers more control."【Pockit→OpenAI Agents SDK vs Google ADK vs LangGraph 2026】

### Instalação
```bash
pip install openai-agents
npx openai-agents
```

### Integração OpenCode
```jsonc
// opencode.jsonc
{
  "mcpServers": {
    "openai-agents": {
      "type": "command",
      "command": "python",
      "args": ["-m", "openai_agents.mcp"]
    }
  }
}
```

---

## 5. Google ADK

| Atributo | Detalhe |
|----------|---------|
| **Tipo** | Agent development framework |
| **Linguagens** | Python, TypeScript, Java, Go, Kotlin (Android) |
| **Licença** | Apache 2.0 |
| **Versão** | v1.0 Python/TS/Java/Go (early 2026) |
| **Melhor para** | Equipes GCP, multimodal, A2A |

**O que faz**: "Google ADK gives you explicit orchestration with Sequential, Parallel, and Loop agents — plus a built-in web debugger that makes reasoning visible."【Particula Tech→Google ADK vs AWS Strands Agents】 "ADK agents can process text, images, video, and audio in the same workflow."【Pockit→OpenAI Agents SDK vs Google ADK vs LangGraph 2026】

**Diferenciais**: 
- Native A2A (Agent-to-Agent) protocol — agentes ADK podem descobrir e comunicar com agentes de outros frameworks
- Quatro SDKs de linguagem (único com Java e Go nativos)
- Vertex AI Agent Engine para deployment gerenciado
- Suporte multimodal nativo (texto, imagem, vídeo, áudio)

**Quando usar**: "Choose Google ADK when deeply integrated with Google Cloud — enterprises leveraging Vertex AI, Gemini, BigQuery, and Apigee."【DataOpsLabs→AI Agent Framework Selection Guide】 Equipes GCP, necessidades multimodais, interoperabilidade cross-framework.

**Trade-offs**: "Deep integration with GCP can be a lock-in concern." "ADK's Cloud Run deployment requires a FastAPI backend and sees cold starts of 50 seconds to a minute."【Particula Tech→Google ADK vs AWS Strands Agents】

### Instalação
```bash
pip install google-adk
npm install @google/adk
```

### Integração OpenCode
```jsonc
// opencode.jsonc
{
  "mcpServers": {
    "google-adk": {
      "type": "command",
      "command": "python",
      "args": ["-m", "google_adk.mcp_server"]
    }
  }
}
```

---

## 6. Claude Agent SDK

| Atributo | Detalhe |
|----------|---------|
| **Tipo** | Provider-native agent SDK |
| **Linguagens** | Python, TypeScript |
| **Licença** | Proprietária (Anthropic) |
| **Pacote** | `@anthropic-ai/claude-agent-sdk` / `claude-agent-sdk` |
| **Melhor para** | Agentes de codificação, acesso a sistema operacional |

**O que faz**: "The Agent SDK gives you the same tools, agent loop, and context management that power Claude Code, programmable in Python and TypeScript."【Claude Code Docs→Agent SDK overview】 Inclui ferramentas built-in: Read, Write, Edit, Bash, Monitor, Glob, Grep, WebSearch, WebFetch, AskUserQuestion. "The key design principle behind the Claude Agent SDK is to give your agents a computer, allowing them to work like humans do."【Anthropic→Building agents with Claude Agent SDK】

**Recursos exclusivos**:
- Acesso direto a sistema de arquivos e shell
- Subagentes com contexto isolado (paralelização nativa)
- Hooks lifecycle (PreToolUse, PostToolUse, SessionStart, etc.)
- Compact automático de contexto (sumarização quando o limite é atingido)
- Integração MCP mais profunda do mercado

**Quando usar**: "Claude Agent SDK for coding agents with deep OS access."【Morph→AI Agent Frameworks 2026】 Agentes que precisam interagir com o sistema operacional, editar código, executar comandos.

**Trade-offs**: "Locked to Anthropic models."【Morph→AI Agent Frameworks 2026】 Apenas modelos Claude.

### Instalação
```bash
# TypeScript
npm install @anthropic-ai/claude-agent-sdk

# Python
pip install claude-agent-sdk

# Necessário: ANTHROPIC_API_KEY no .env
```

### Integração OpenCode
```python
# Exemplo: agente Claude que busca, analisa e reporta
from claude_agent_sdk import ClaudeAgent

agent = ClaudeAgent(
    system_prompt="You are a research agent. Search the web, analyze findings, write a report."
)

async for message in agent.query(
    "Search for latest AI trends and write a summary",
    options={"allowedTools": ["WebSearch", "Read", "Write", "Edit"]}
):
    print(message)
```

O Claude Agent SDK é o **mais compatível com OpenCode** por compartilhar o mesmo harness do Claude Code.

---

## 7. AWS Strands Agents

| Atributo | Detalhe |
|----------|---------|
| **Tipo** | Model-driven agent framework |
| **Linguagens** | Python |
| **Licença** | Apache 2.0 |
| **Lançamento** | v1.0 julho 2025 |
| **Melhor para** | Deploy serverless (Lambda), ecossistema AWS |

**O que faz**: "AWS Strands takes a fundamentally different approach: let the foundation model handle orchestration. Instead of hardcoding workflows, developers define a system prompt and provide tools — the LLM autonomously chains reasoning steps using the ReAct pattern."【DataOpsLabs→AI Agent Framework Selection Guide】 "Strands' model-driven autonomy ships in seconds on Lambda with 5-second cold starts."【Particula Tech→Google ADK vs AWS Strands Agents】

**Recursos**:
- Deploy nativo em Lambda e Fargate
- Suporte MCP nativo
- Integração Bedrock AgentCore
- OpenTelemetry para observabilidade
- Multi-provedor (Bedrock, Anthropic, OpenAI, LiteLLM, Ollama)

**Quando usar**: "Choose AWS Strands when embracing AWS-native serverless — event-driven architectures, Lambda/Fargate deployments, and MCP standardization."【DataOpsLabs→AI Agent Framework Selection Guide】 Times AWS, workloads event-driven, deploy serverless.

**Trade-offs**: Menos controle explícito que LangGraph ou ADK. "ADK's explicit orchestration gives you deterministic control; Strands' model-driven autonomy is faster but less auditable."【Particula Tech→Google ADK vs AWS Strands Agents】

### Instalação
```bash
pip install strands-agents
```

### Integração OpenCode
```jsonc
// opencode.jsonc
{
  "mcpServers": {
    "aws-strands": {
      "type": "command",
      "command": "strands",
      "args": ["mcp-server"]
    }
  }
}
```

---

## 8. Mastra

| Atributo | Detalhe |
|----------|---------|
| **Tipo** | AI agent application framework |
| **Linguagens** | TypeScript (principal) |
| **Licença** | Apache 2.0 |
| **GitHub** | ~24.8k stars |
| **Melhor para** | TypeScript / Next.js full-stack |

**O que faz**: "Mastra, built by the creators of Gatsby, is a JavaScript-first framework aimed at frontend developers. It allows LLM agents to be directly embedded into web environments."【Solansync→Agentic AI Frameworks Compared】 "Mastra fills the gap for TypeScript teams building production custom agents."【LangChain→Best AI agent frameworks 2026】

**Recursos**: Memória de trabalho + recall semântico, Next.js native, OpenTelemetry nativo, MCP bidirecional.

**Quando usar**: Times TypeScript, projetos Next.js, agentes embedados em web apps.

**Trade-offs**: Ecossistema menor que Python-based frameworks.

### Instalação
```bash
npm install mastra
npx mastra init
```

### Integração OpenCode
```jsonc
// opencode.jsonc
{
  "skills": {
    "mastra-agent": {
      "description": "Cria agentes Mastra em TypeScript para web apps"
    }
  }
}
```

---

## 9. Smolagents

| Atributo | Detalhe |
|----------|---------|
| **Tipo** | Minimalist agent framework (code-first) |
| **Linguagens** | Python |
| **Licença** | Apache 2.0 |
| **GitHub** | ~27.7k stars |
| **Melhor para** | Agentes code-first, experimentos, HF Hub |

**O que faz**: "Smolagents is Hugging Face's minimal agent framework. It works by having the LLM write Python code to complete tasks rather than using JSON function calls."【Firecrawl→Best open source frameworks for building AI agents 2026】 "Scored #1 on GAIA with CodeAgent (open-source division). Minimal codebase (~1,000 lines of core) designed for modification, not configuration."【ChatForest→Best AI Agent Frameworks 2026】

**Quando usar**: "Start with smolagents for single-agent automation scripts and research workflows." Aprendizado, PoCs, experimentos com modelos locais.

**Trade-offs**: "Not designed for multi-agent orchestration or enterprise state management."【Firecrawl→Best open source frameworks for building AI agents 2026】

### Instalação
```bash
pip install smolagents
```

### Integração OpenCode
```python
# Exemplo: agente que escreve código
from smolagents import CodeAgent, HfApiModel

agent = CodeAgent(
    model=HfApiModel("Qwen/Qwen2.5-72B-Instruct"),
    tools=[],
    add_base_tools=True
)

agent.run("Analyze the data in data.csv and create a visualization")
```

---

## 10. LlamaIndex Workflows

| Atributo | Detalhe |
|----------|---------|
| **Tipo** | Agent workflow framework (RAG-first) |
| **Linguagens** | Python, TypeScript |
| **Licença** | MIT |
| **GitHub** | 48.2k stars, 10.09M PyPI downloads/mês |
| **Melhor para** | RAG-heavy workflows, data-centric agents |

**O que faz**: LlamaIndex Workflows oferece um sistema event-driven para construir agentes centrados em recuperação de dados. Ideal quando RAG é o core do produto. "LlamaIndex when retrieval and document workflows dominate."【Cordum→Best AI Agent Frameworks 2026】

**Quando usar**: Produtos RAG-first, pipelines de dados com agentes.

**Trade-offs**: Fora de RAG, LangGraph ou CrewAI são mais apropriados.

### Instalação
```bash
pip install llama-index
```

### Integração OpenCode
```jsonc
// opencode.jsonc
{
  "mcpServers": {
    "llamaindex": {
      "type": "command",
      "command": "python",
      "args": ["-m", "llama_index.mcp_server"]
    }
  }
}
```

---

## 11. PydanticAI

| Atributo | Detalhe |
|----------|---------|
| **Tipo** | Type-safe Python agent framework |
| **Linguagens** | Python |
| **Licença** | MIT |
| **Melhor para** | Outputs validados, type safety |

**O que faz**: "PydanticAI is a Python agent framework for building agents with type-safe structured outputs, validation, and production-grade tool calling." Framework focado em type safety com modelos Pydantic.

**Quando usar**: "Choose PydanticAI if you prioritize Python type safety and validated outputs." Quando a validação de output é crítica.

**Trade-offs**: Sem suporte multi-agente nativo. Ecossistema menor.

### Instalação
```bash
pip install pydantic-ai
```

---

## 12. Agno (ex-Phidata)

| Atributo | Detalhe |
|----------|---------|
| **Tipo** | Lightweight Python agent framework |
| **Linguagens** | Python |
| **Licença** | MIT |
| **Melhor para** | Agentes com foco em dados e APIs |

**O que faz**: "Agno (formerly Phidata) is a lightweight agent framework that provides plug-and-play abstractions for building production agents with built-in memory, knowledge bases, and tool integration."【JetBrains→Top Agentic Frameworks 2026】 

**Quando usar**: "Building production agents that primarily interact with APIs, databases, and external systems rather than complex multi-step orchestration." Foco em tool-centric agents.

**Trade-offs**: Menos adequado para orquestração multi-agente complexa.

### Instalação
```bash
pip install agno
```

---

## 13. AG2 (AutoGen Community Fork)

| Atributo | Detalhe |
|----------|---------|
| **Tipo** | Conversational multi-agent framework |
| **Linguagens** | Python |
| **Licença** | Apache 2.0 |
| **GitHub** | ~4.5k stars (AG2) |
| **Status** | Community fork do AutoGen original |

**O que faz**: "AG2 is the Apache 2.0 community fork of Microsoft's AutoGen, maintained after Microsoft shifted focus to the unified Agent Framework."【ChatForest→Best AI Agent Frameworks 2026】 Oferece nine orchestration patterns (GroupChat, Society-of-Mind, etc.).

**Quando usar**: "AG2 for conversational multi-agent collaboration." Pesquisa, experimentos com múltiplos agentes conversacionais.

**Trade-offs**: Menos suporte que LangGraph ou CrewAI. Microsoft recomenda migrar para Agent Framework.

### Instalação
```bash
pip install ag2
```

---

## 14. Dify

| Atributo | Detalhe |
|----------|---------|
| **Tipo** | Visual/no-code AI agent platform |
| **Linguagens** | Web (self-hosted) |
| **Licença** | Apache 2.0 |
| **GitHub** | 144k stars |
| **Melhor para** | Criação visual de agentes, não-técnicos |

**O que faz**: Dify é uma plataforma visual para criar aplicações LLM e agentes sem código. Oferece drag-and-drop de workflows, publicação de APIs, e integração com múltiplos modelos. "Dify leads in GitHub stars (144k)."【Firecrawl→Best open source frameworks 2026】

**Quando usar**: Equipes não-técnicas, prototipagem visual, publicação rápida de assistentes.

**Trade-offs**: Menos flexível que frameworks code-first para workflows complexos.

### Instalação
```bash
# Docker
docker run -d -p 3000:3000 -p 5001:5001 langgenius/dify
```

---

## 15. AutoGPT

| Atributo | Detalhe |
|----------|---------|
| **Tipo** | Autonomous agent platform |
| **Linguagens** | Python |
| **Licença** | MIT/Polyform |
| **GitHub** | 184k stars |
| **Melhor para** | Agentes autônomos visuais, no-code |

**O que faz**: AutoGPT foi pioneiro no conceito de agentes autônomos. Em 2026, evoluiu para incluir construção visual de agentes (no-code/low-code). "AutoGPT is mostly historical now as a research project."【GitHub→framework-analysis】 Ainda relevante para experimentação.

**Trade-offs**: "Mostly historical" — frameworks mais modernos como LangGraph e CrewAI o superaram em maturidade de produção.

### Instalação
```bash
git clone https://github.com/Significant-Gravitas/AutoGPT.git
```

---

## 16. Comparativo Final

### Matriz Decisão por Cenário

| Seu cenário | Framework #1 | Framework #2 (runner-up) | Por que |
|-------------|-------------|-------------------------|---------|
| **Workflow stateful complexo** | LangGraph | Microsoft Agent Framework | Checkpointing, HITL, time-travel |
| **Prototipagem multi-agente rápida** | CrewAI | OpenAI Agents SDK | Role/task clarity, tempo-para-PoC |
| **Empresa .NET / Microsoft** | Microsoft Agent Framework | Semantic Kernel | Governança, middleware, telemetria |
| **Ecossistema Google Cloud** | Google ADK | LangGraph | Vertex AI, A2A, multimodal |
| **Ecossistema AWS** | AWS Strands | LangGraph | Lambda, Bedrock, serverless |
| **Agentes de código/OS** | Claude Agent SDK | Smolagents | Arquivos, shell, MCP profundo |
| **OpenAI-first** | OpenAI Agents SDK | LangChain | Handoffs, guardrails, Responses API |
| **RAG-first** | LlamaIndex Workflows | Haystack | Recuperação, documentos |
| **TypeScript / Next.js** | Mastra | Vercel AI SDK | Web-first, memória, streaming |
| **Type safety Python** | PydanticAI | LangChain + Pydantic | Outputs validados |
| **Iniciante / aprendizado** | Smolagents | CrewAI | ~1000 linhas de core, código simples |
| **Visual / no-code** | Dify | AutoGPT | Drag-and-drop |

### Matriz de Capacidades

| Framework | Multi-Agente | MCP | A2A/ACP | HITL | Memória | Checkpoint | Observab. | Deploy Gerenciado |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| LangChain/LangGraph | ✅ | Via adapter | ❌ | ✅ Forte | ✅ | ✅ (time-travel) | ✅ LangSmith | ✅ LangGraph Cloud |
| CrewAI | ✅ Roles | ✅ Nativo | ✅ A2A | Limitado | ❌ | ❌ | ⚠️ Enterprise | ⚠️ Enterprise |
| MS Agent Framework | ✅ Graph | ✅ Nativo | ✅ A2A | ✅ Forte | ✅ Session | ✅ | ✅ OpenTelemetry | ✅ Azure |
| OpenAI Agents SDK | ✅ Handoffs | ✅ Adotado | ❌ | ✅ Guardrails | ✅ Session | ❌ | ⚠️ API logs | ✅ OpenAI |
| Google ADK | ✅ Hierárquico | Via adapter | ✅ Nativo | ✅ | ✅ Vertex | ✅ | ✅ Vertex | ✅ Agent Engine |
| Claude Agent SDK | ✅ Subagentes | ✅ Profundo | ❌ | ✅ (modos) | ✅ Compact | ❌ | ⚠️ | ❌ |
| AWS Strands | ✅ SOPs | ✅ Nativo | ❌ | Limitado | ✅ Built-in | ✅ | ✅ OpenTelemetry | ✅ Lambda/Fargate |
| Mastra | ⚠️ Parcial | ✅ Bidirec. | ❌ | Limitado | ✅ Nativo | ❌ | ✅ OpenTelemetry | ❌ |
| Smolagents | Limitado | ✅ Suportado | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| LlamaIndex | Limitado | Via adapter | ❌ | Moderado | ✅ Forte | ❌ | ✅ | ❌ |
| PydanticAI | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Agno | Limitado | ✅ | ❌ | ❌ | ✅ Built-in | ❌ | ⚠️ | ❌ |

### Categorias por Perfil de Desenvolvedor

**Para protótipos rápidos (horas a dias)**:
1. **CrewAI** — Defina papéis, atribua tarefas, execute. Tempo recorde para primeiro agente funcional.
2. **OpenAI Agents SDK** — Se você já usa OpenAI, 5 linhas de código.
3. **Smolagents** — Para experimentos code-first, ~1000 linhas de core.

**Para ambientes corporativos (semanas a meses)**:
1. **LangGraph + LangSmith** — Padrão ouro para produção: observabilidade, checkpointing, HITL.
2. **Microsoft Agent Framework** — Se você é .NET/Azure. Governança, middleware, telemetria.
3. **Google ADK** — Se você é GCP. Multimodal, A2A, Vertex AI.
4. **AWS Strands** — Se você é AWS. Lambda, Bedrock, serverless.

**Para desenvolvedores independentes / Indie hackers**:
1. **Claude Agent SDK** — Acesso total a OS, arquivos, shell.
2. **Mastra** — Se você é TypeScript/Next.js.
3. **LangGraph** — Gratuito, open source, ecossistema vasto.
4. **CrewAI** — Rápido, intuitivo, open source.

### Tendências 2026

1. **Consolidação**: AutoGen e Semantic Kernel → Microsoft Agent Framework. O ecossistema está se consolidando em torno de poucos frameworks dominantes. "The past eighteen months changed everything. Anthropic shipped a general-purpose Agent SDK. AWS open-sourced Strands. OpenAI evolved Swarm into a production-grade Agents SDK."【QubitTool→2026 AI Agent Framework Showdown】

2. **MCP como padrão**: "MCP has become the de facto standard for connecting agents to tools. OpenAI, Microsoft, Google, and Amazon all adopted it. 6,400+ MCP servers in the official registry."【Saladi→Agent Frameworks 101】

3. **A2A para interoperabilidade**: Google ADK e Microsoft Agent Framework lideram o protocolo A2A (Agent-to-Agent). "AgentCore Runtime supports agents built with any framework using A2A for communication."【Particula Tech→Google ADK vs AWS Strands Agents】

4. **Provider SDKs vs Independentes**: SDKs nativos (Claude, OpenAI, Google) oferecem integração mais profunda; frameworks independentes (LangGraph, CrewAI) oferecem flexibilidade multi-modelo. "Neither category is universally better. The right choice depends on whether you prioritize depth of integration or model flexibility."【Morph→AI Agent Frameworks 2026】

---

## 17. Integração com OpenCode

### Via MCP (Model Context Protocol)

A forma mais direta de integrar agent frameworks ao OpenCode é via MCP. Todos os frameworks modernos suportam MCP, seja nativamente ou via adaptadores.

```jsonc
// ~/.config/opencode/opencode.jsonc
{
  "mcpServers": {
    "crewai": {
      "type": "command",
      "command": "python",
      "args": ["-m", "crewai_mcp"]
    },
    "langgraph": {
      "type": "url",
      "url": "https://api.langchain.xyz/mcp"
    }
  }
}
```

### Via Skills

Crie skills OpenCode que encapsulam padrões comuns de agentes:

```markdown
---
name: agent-crew-research
description: >
  Usa CrewAI para montar uma crew de pesquisa: researcher + writer + reviewer.
  Executa pesquisa web, sintetiza e valida.
---

# Agent Crew: Pesquisa Multi-Papéis

Execute uma crew de agentes para pesquisa completa:
1. **Researcher**: Busca informações na web
2. **Writer**: Sintetiza em relatório
3. **Reviewer**: Valida fontes e qualidade

## Comando
```python
from crewai import Agent, Task, Crew
# ...
```
```

### Via Claude Agent SDK (compatibilidade máxima)

O Claude Agent SDK compartilha o mesmo harness do Claude Code/OpenCode. Agentes construídos com ele podem ser invocados diretamente via herramientas do OpenCode:

```python
# Agente OpenCode usando Claude Agent SDK
from claude_agent_sdk import ClaudeAgent

async def agent_pesquisa():
    agent = ClaudeAgent(
        system_prompt="Você é um agente de pesquisa. Busque, analise e reporte."
    )
    async for msg in agent.query("Pesquise o tópico X e gere relatório"):
        yield msg
```

---

## Glossário

| Termo | Definição |
|-------|-----------|
| **MCP** | Model Context Protocol — padrão para conectar agentes a ferramentas |
| **A2A** | Agent-to-Agent — protocolo para agentes de diferentes frameworks se comunicarem |
| **HITL** | Human-in-the-Loop — aprovação humana em pontos críticos do workflow |
| **Checkpointing** | Salvamento de estado para retomada após falha |
| **Time-travel** | Replay de execuções anteriores para debugging |
| **Handoff** | Passagem de controle entre agentes (OpenAI SDK) |
| **ReAct** | Reasoning + Acting — padrão onde o modelo raciocina e age em loop |
| **RAG** | Retrieval-Augmented Generation — recuperação de dados + geração |

---

## Fontes

- Inductivee, abril 2026, "Agentic AI Frameworks in 2026: LangGraph vs CrewAI vs..."
- Agent Guides, maio 2026, "AI Agent Frameworks 2026 — 10 Tested, Reviewed and Compared"
- Alice Labs, 2026, "Open Source AI Agent Frameworks Comparison 2026"
- LangChain, junho 2026, "The best AI agent frameworks in 2026"
- Morph, junho 2026, "AI Agent Frameworks (2026 Update): 8 SDKs Compared"
- JetBrains, junho 2026, "Top Agentic Frameworks for Building Applications 2026"
- Firecrawl, abril 2026, "The best open source frameworks for building AI agents in 2026"
- Particula Tech, março 2026, "Google ADK vs AWS Strands Agents"
- Pockit, março 2026, "OpenAI Agents SDK vs Google ADK vs LangGraph 2026"
- Microsoft DevBlogs, abril 2026, "Microsoft Agent Framework Version 1.0"
- Claude Code Docs, 2026, "Agent SDK overview"
- Anthropic Engineering, 2025, "Building agents with the Claude Agent SDK"
- ChatForest, maio 2026, "Best AI Agent Frameworks in 2026 — 14 Frameworks Compared"
- QubitTool, maio 2026, "2026 AI Agent Framework Showdown"
- Saladi, abril 2026, "Agent Frameworks 101: The Complete Guide"
- DataOpsLabs, janeiro 2026, "AI Agent Framework Selection Guide"

---

*Relatório gerado em Junho 2026. Preços, versões e classificações podem variar. Sempre verifique a documentação oficial antes de adotar um framework.*
