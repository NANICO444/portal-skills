---
name: model-router-fallback
description: "Roteamento inteligente de modelos com fallbacks hierárquicos — escolhe o modelo ideal para cada tarefa"
argument-hint: "[tarefa para rotear modelo]"
user-invocable: true
allowed-tools: Task, WebFetch
agent: orquestrador
---

# Model Router — Roteamento com Fallback

Sistema para escolher o modelo de IA ideal para cada tipo de tarefa, com fallback automático.

## Hierarquia de Prioridade

### Nível 1 — Modelos Premium (tarefas críticas)
- **Opus 4.8** — arquitetura, decisões complexas, revisão de segurança
- **Opus 4.7** — design de sistema, code review aprofundado
- **Sonnet 4.6** — implementação, debug, tarefas gerais

### Nível 2 — Modelos Standard (tarefas do dia-a-dia)
- **Gemini 2.5 Pro** — análise de dados, documentação
- **GPT-4.1** — frontend, UI, criatividade
- **Claude 3.7 Sonnet** — implementação geral

### Nível 3 — Modelos Gratuitos (tarefas simples, prototipação)
- **Qwen 3 Coder** — código simples, scripts
- **DeepSeek Coder** — programação geral
- **Nemotron** — tarefas leves
- **Gemma 4** — consultas rápidas
- **Hermes 3** — formatação, análise simples

## Matriz de Roteamento

| Tarefa | Modelo Ideal | Fallback 1 | Fallback 2 |
|--------|-------------|------------|------------|
| Arquitetura/design system | Opus 4.8 | Opus 4.7 | Sonnet 4.6 |
| Code review (segurança) | Opus 4.8 | Sonnet 4.6 | Gemini 2.5 Pro |
| Implementação backend | Sonnet 4.6 | Qwen 3 Coder | DeepSeek Coder |
| Frontend/UI | Sonnet 4.6 | GPT-4.1 | Qwen 3 Coder |
| Testes unitários | Qwen 3 Coder | DeepSeek Coder | Sonnet 4.6 |
| Documentação | Gemini 2.5 Pro | Sonnet 4.6 | Opus 4.7 |
| Pesquisa | Gemini 2.5 Pro | Sonnet 4.6 | Claude 3.7 Sonnet |
| Debug | Sonnet 4.6 | DeepSeek Coder | Qwen 3 Coder |
| Prototipação rápida | Qwen 3 Coder | DeepSeek Coder | Nemotron |
| Formatação/refatoração | Gemini 4 | Hermes 3 | Nemotron |

## Configuração no OpenCode

```jsonc
// agent1-north/opencode.json
{
  "providers": {
    "openrouter": {
      "models": {
        "preferred": ["openrouter/openai/gpt-oss-120b:free"],
        "fallbacks": [
          "openrouter/qwen/qwen-3-coder:free",
          "openrouter/deepseek/deepseek-coder:free"
        ]
      }
    },
    "google": {
      "models": {
        "preferred": ["google/gemini-2.5-pro-exp:free"],
        "fallbacks": ["google/gemma-4:free"]
      }
    }
  }
}
```

## Estratégias de Fallback

### Estratégia 1: Prioridade Fixa
Tente modelo A, se falhar → B, se falhar → C.
**Use quando:** tarefa precisa de qualidade mínima garantida.

### Estratégia 2: Custo Mínimo
Tente o modelo gratuito mais capaz, se falhar → suba um nível.
**Use quando:** orçamento é restrição principal.

### Estratégia 3: Especialização
Cada tipo de tarefa tem modelo designado (ver matriz acima).
**Use quando:** equipe grande com tarefas variadas.

## Regras de Ouro

✅ Documente qual modelo foi usado e por quê.
✅ Fallback não é desculpa para entrega de baixa qualidade.
✅ Se todos os fallbacks falharem, reporte ao usuário com alternativas.
✅ Teste o modelo escolhido antes de comprometer com a tarefa.

❌ Usar modelo gratuito para tarefa crítica (segurança, arquitetura).
❌ Mudar de modelo no meio de uma tarefa complexa sem justificativa.
❌ Ignorar o fallback quando o modelo principal está lento/caro.
