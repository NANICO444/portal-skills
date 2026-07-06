# Relatório: Modelos de IA Gratuitos para Codificação com OpenCode

**Data:** 21 de Junho de 2026  
**Objetivo:** Listar e instruir como adicionar modelos LLM gratuitos ao OpenCode editando apenas `opencode.json`.

---

## Sumário

1. [OpenCode Zen — Modelos Free (Zero Config)](#1-opencode-zen--modelos-free-zero-config)
2. [ZenMux — Modelos Gratuitos via API Key](#2-zenmux--modelos-gratuitos-via-api-key)
3. [Ollama — Modelos Locais (Privacidade Total)](#3-ollama--modelos-locais-privacidade-total)
4. [LM Studio — Modelos Locais com GUI](#4-lm-studio--modelos-locais-com-gui)
5. [Hidden Models — Adicionar Modelos Não Listados](#5-hidden-models--adicionar-modelos-não-listados)
6. [Modelos Open-Weight 2026 para Codificação](#6-modelos-open-weight-2026-para-codificação)
7. [Comparação com Modelos Pagos](#7-comparação-com-modelos-pagos)
8. [Dicas para Testar e Alternar Modelos](#8-dicas-para-testar-e-alternar-modelos)
9. [Privacidade e Limitações](#9-privacidade-e-limitações)

---

## 1. OpenCode Zen — Modelos Free (Zero Config)

### O que é

O **OpenCode Zen** é um conjunto curado de modelos mantido pela equipe do OpenCode. Alguns são **completamente gratuitos** — sem necessidade de API key, cartão de crédito ou GPU local.

### Modelos Free disponíveis (Junho 2026)

| Modelo | ID | Contexto | Melhor Para |
|--------|----|----------|-------------|
| **Big Pickle** | `big-pickle` | 200K | Codificação geral (stealth model, alias do DeepSeek V4 Flash) |
| **DeepSeek V4 Flash Free** | `deepseek-v4-flash-free` | 200K | Tool calling, raciocínio, codificação |
| **MiMo-V2.5 Free** | `mimo-v2.5-free` | 200K | Codificação Xiaomi, contexto longo |
| **North Mini Code Free** | `north-mini-code-free` | 200K | Codificação leve |
| **Nemotron 3 Ultra Free** | `nemotron-3-ultra-free` | 200K | Modelo NVIDIA, tarefas gerais |

> **Atenção:** Todos os modelos free do Zen são **por tempo limitado**. A equipe do OpenCode os oferece para coleta de feedback.

### Como adicionar ao `opencode.json`

Não precisa! Os modelos Zen já vêm embutidos no OpenCode. Basta:

1. Abrir o OpenCode
2. Digitar `/models`
3. Selecionar um modelo que tenha "Free" no nome
4. Começar a usar

Se quiser definir um como padrão:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "model": "opencode/big-pickle",
  "small_model": "opencode/deepseek-v4-flash-free"
}
```

### Via AiDevOps (alternativa com curadoria extra)

```bash
npm install -g aidevops && aidevops update
```

O AiDevOps já configura os modelos free do Zen automaticamente.

---

## 2. ZenMux — Modelos Gratuitos via API Key

### O que é

ZenMux é um provedor que agrega múltiplos modelos com uma única API key. Alguns modelos são gratuitos.

### Modelos Free na ZenMux (Junho 2026)

| Modelo | ID ZenMux | Contexto |
|--------|-----------|----------|
| **Z.AI: GLM 4.6V Flash Free** | `z-ai/glm-4.6v-flash-free` | 131K |
| **Z.AI: GLM 4.7 Flash Free** | `z-ai/glm-4.7-flash-free` | ~200K |
| **Z.AI: GLM 5.2 Free** | `z-ai/glm-5.2-free` | 1M |
| **StepFun: Step 3.7 Flash Free** | `stepfun/step-3.7-flash-free` | 256K |
| **MoonshotAI: Kimi K2.7 Code Free** | `moonshotai/kimi-k2.7-code-free` | 262K |
| **Xiaomi: MiMo V2 Flash Free** | `xiaomi/mimo-v2-flash-free` | 262K |
| **KwaiKAT: KAT Coder Pro V1 Free** | `kuaishou/kat-coder-pro-v1-free` | 262K |
| **Google: Gemini 3 Flash Preview Free** | `google/gemini-3-flash-preview-free` | 1M |

### Configuração no `opencode.json`

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "zenmux": {
      "models": {
        "z-ai/glm-5.2-free": {
          "name": "Z.AI: GLM 5.2 Free - 1M",
          "limit": {
            "context": 1000000,
            "output": 128000
          }
        },
        "stepfun/step-3.7-flash-free": {
          "name": "StepFun: Step 3.7 Flash Free",
          "limit": {
            "context": 256000,
            "output": 128000
          }
        },
        "moonshotai/kimi-k2.7-code-free": {
          "name": "MoonshotAI: Kimi K2.7 Code Free",
          "limit": {
            "context": 262144,
            "output": 128000
          }
        },
        "xiaomi/mimo-v2-flash-free": {
          "name": "Xiaomi: MiMo V2 Flash Free",
          "limit": {
            "context": 262144,
            "output": 128000
          }
        },
        "google/gemini-3-flash-preview-free": {
          "name": "Google: Gemini 3 Flash Preview Free",
          "limit": {
            "context": 1048576,
            "output": 128000
          }
        },
        "z-ai/glm-4.6v-flash-free": {
          "name": "Z.AI: GLM 4.6V Flash Free",
          "limit": {
            "context": 131072,
            "output": 128000
          }
        }
      }
    }
  },
  "model": "zenmux/z-ai/glm-5.2-free",
  "small_model": "zenmux/stepfun/step-3.7-flash-free"
}
```

### Requisitos

- API key da ZenMux (formato `sk-ai-v1-xxx`)
- Conectar via `/connect` dentro do OpenCode

---

## 3. Ollama — Modelos Locais (Privacidade Total)

### O que é

Ollama permite rodar modelos open-source localmente no seu PC. **Zero custo de API, privacidade total.**

### Modelos Recomendados para Codificação Local

| Modelo | Tamanho | RAM Mínima | Contexto | Qualidade |
|--------|---------|------------|----------|-----------|
| **Qwen3-Coder 8B** | 8B | 8 GB | 256K (configurar para 16K+) | Excelente para 7B |
| **Qwen3.6-27B (Q4)** | 27B | 17 GB | 262K | 77.2% SWE-bench, melhor por GB |
| **Qwen3.6-35B-A3B (Q4)** | 35B/3B MoE | 19-22 GB | 262K | ~120 tok/s, 73.4% SWE-bench |
| **GLM-4.7-Flash (Q4)** | 30B/3B MoE | ~15 GB | ~200K | 59.2% SWE-bench |
| **DeepSeek Coder 6.7B** | 6.7B | 8 GB | 128K | Bom para tool calling |
| **Codestral 22B** | 22B | 14 GB | 256K | 95.3% FIM (autocomplete) |

### Configuração no `opencode.json`

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "ollama": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Ollama (local)",
      "options": {
        "baseURL": "http://localhost:11434/v1"
      },
      "models": {
        "qwen3.6-27b:q4_k_m": {
          "name": "Qwen3.6 27B (Q4)"
        },
        "qwen3-coder:8b": {
          "name": "Qwen3 Coder 8B"
        },
        "glm-4.7-flash": {
          "name": "GLM 4.7 Flash"
        }
      }
    }
  }
}
```

### Setup

```bash
# Instalar Ollama
# https://ollama.com

# Fazer pull dos modelos
ollama pull qwen3.6-27b:q4_k_m
ollama pull qwen3-coder:8b
ollama pull glm-4.7-flash

# Aumentar contexto (crítico para OpenCode!)
ollama run qwen3-coder:8b
>>> /set parameter num_ctx 32768
>>> /save qwen3-coder:8b-32k
>>> /bye
```

### Requisitos Mínimos

- **8 GB RAM**: Qwen3-Coder 8B ou GLM-4.7-Flash
- **16 GB RAM**: Qwen3.6-27B (Q4_K_M)
- **24 GB RAM**: Qwen3.6-35B-A3B (Q4_K_M)
- **GPU (opcional)**: RTX 3060+ para aceleração via CUDA

---

## 4. LM Studio — Modelos Locais com GUI

### O que é

LM Studio é um aplicativo desktop (Windows/Mac/Linux) para rodar modelos localmente com interface gráfica. Expõe API compatível com OpenAI.

### Modelos Recomendados

| Modelo | Tamanho | RAM | Contexto | Notas |
|--------|---------|-----|----------|-------|
| **Qwen3.5-9B** | 9B | 8-12 GB | 32K+ | Bom custo-benefício local |
| **Qwen3-Coder-30B-A3B** | 30B/3B MoE | 16-20 GB | 32K+ | MLX eficiente em Apple Silicon |
| **Devstral Small 24B** | 24B | 16 GB | 32K+ | Agentes locais |
| **Gemma-4-31B** | 31B | 20-24 GB | 128K | Google, boa para tool calling |
| **Gemma-4-E4B** | 28B | 18-22 GB | 84K | Versão eficiente da Gemma 4 |
| **Qwen3.5-35B-A3B** | 35B/3B MoE | 20-24 GB | 32K+ | Poder local máximo |

### Configuração no `opencode.json`

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "lmstudio": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "LM Studio (local)",
      "options": {
        "baseURL": "http://127.0.0.1:1234/v1",
        "apiKey": "lmstudio"
      },
      "models": {
        "qwen/qwen3.5-9b": {
          "name": "Qwen3.5 9B",
          "limit": {
            "context": 32768,
            "output": 8192
          }
        },
        "qwen/qwen3-coder-30b": {
          "name": "Qwen3 Coder 30B",
          "limit": {
            "context": 32768,
            "output": 8192
          }
        },
        "gemma-4-e4b-it-mlx": {
          "name": "Gemma 4 E4B",
          "limit": {
            "context": 32768,
            "output": 8192
          }
        }
      }
    }
  }
}
```

### Setup

1. Baixar LM Studio em [lmstudio.ai](https://lmstudio.ai)
2. No app, ir em **Discover** e baixar um modelo (ex: `qwen3.5-9b`)
3. Ir na aba **Developer** (ícone `<->`)
4. Carregar o modelo e clicar **Start Server**
5. Verificar se o servidor está rodando:
   ```bash
   curl http://127.0.0.1:1234/v1/models
   ```
6. Abrir OpenCode — o modelo aparece na lista `/models`

### Alternativa via CLI (`lms`)

```bash
lms load "qwen/qwen3.5-9b" --context-length 32768
```

---

## 5. Hidden Models — Adicionar Modelos Não Listados

### O que é

Você pode adicionar **qualquer modelo** que um provedor já existente no OpenCode suporta, mesmo que não apareça na lista padrão. Basta saber o `provider-id` (diretório em [models.dev](https://models.dev)) e o `model-id` (identificador da API).

### Padrão de Configuração

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "<provider-id>": {
      "models": {
        "<model-id>": {
          "name": "Nome Amigável"
        }
      }
    }
  }
}
```

### Exemplos Reais

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "fireworks-ai": {
      "models": {
        "accounts/fireworks/routers/glm-5-fast": {
          "name": "GLM-5 Fast (Fireworks)"
        }
      }
    },
    "synthetic": {
      "models": {
        "hf:zai-org/GLM-5": {
          "name": "GLM-5 (Synthetic)"
        }
      }
    }
  }
}
```

### Regras

- **Não precisa** de `npm`, `baseURL` ou `name` no nível do provider — esses já vêm do registro.
- O modelo **precisa existir** na API do provedor.
- Você precisa **autenticar** o provedor primeiro (via `/connect`).
- Pode adicionar `limit` (contexto/output) e `options` extras.

---

## 6. Modelos Open-Weight 2026 para Codificação

### Ranking (Junho 2026)

| Rank | Modelo | Tamanho | Contexto | Licença | SWE-bench | Onde Rodar |
|------|--------|---------|----------|---------|-----------|------------|
| 1 | **GLM-5.1/5.2** | 744B-A40B | 200K-1M | MIT | SOTA OSS | ZenMux, Fireworks, Ollama Cloud |
| 2 | **MiniMax M3** | MoE (MSA) | 1M | Open | 59% Pro | OpenCode Zen (pago), LM Studio |
| 3 | **Kimi K2.6** | 1T-A32B | 256K | Modified MIT | 80.2% V | ZenMux, Ollama Cloud |
| 4 | **DeepSeek V4-Pro** | 1.6T-A49B | 1M | MIT | 80.6% V | OpenCode Zen (pago) |
| 5 | **DeepSeek V4-Flash** | 284B/13B | 1M | MIT | — | OpenCode Zen (FREE), Ollama Cloud |
| 6 | **Qwen3-Coder-Next** | 480B-A35B | 256K | Apache 2.0 | 69.6% V | Ollama Cloud, LM Studio |
| 7 | **Qwen3.6-27B** | 27B | 262K | Apache 2.0 | 77.2% V | Local (17 GB RAM) |
| 8 | **Nemotron 3 Ultra** | 253B | 1M | NVIDIA | — | OpenCode Zen (FREE) |
| 9 | **MiMo-V2.5** | MoE | 1M | Open | — | OpenCode Zen (FREE/pago) |

### Disponibilidade Gratuita

| Modelo | Grátis Via | Custo |
|--------|-----------|-------|
| GLM-5.2 Free | ZenMux (API key) | Gratuito (limitado) |
| DeepSeek V4 Flash Free | OpenCode Zen | Completamente grátis |
| MiMo-V2.5 Free | OpenCode Zen | Completamente grátis |
| Nemotron 3 Ultra Free | OpenCode Zen | Completamente grátis |
| Big Pickle | OpenCode Zen | Completamente grátis |
| Qwen3.6-27B | Ollama/LM Studio local | Só hardware |
| Qwen3-Coder 8B | Ollama local | Só hardware |

---

## 7. Comparação com Modelos Pagos

### Modelos Recomendados pelo OpenCode (Pagos)

| Modelo | Input/1M | Output/1M | Melhor Para |
|--------|----------|-----------|-------------|
| **GPT 5.2** | $1.75 | $14.00 | Codificação geral |
| **GPT 5.1 Codex** | $1.07 | $8.50 | Código específico |
| **Claude Opus 4.5** | $5.00 | $25.00 | Raciocínio complexo |
| **Claude Sonnet 4.5** | $3.00 | $15.00 | Balanço qualidade/custo |
| **MiniMax M2.1** | $0.30 | $1.20 | Custo-benefício |
| **Gemini 3 Pro** | ~$2.00 | ~$12.00 | Contexto longo |

### Gratuito vs Pago — Quando Usar Cada Um

| Cenário | Recomendação |
|---------|-------------|
| **Tarefa rápida, exploratória** | Modelo free (Zen, ZenMux) |
| **Codificação séria, produção** | Modelo pago (GPT, Claude) |
| **Privacidade total, sem internet** | Ollama/LM Studio local |
| **Prototipagem, aprendizado** | Modelo free |
| **Refatoração grande, arquitetura** | Modelo pago |
| **Review de segurança** | Modelo pago (Claude Opus) |
| **Autocomplete, tarefas pequenas** | Modelo free ou local |

---

## 8. Dicas para Testar e Alternar Modelos

### Dentro do OpenCode

- `/models` — Abre o seletor de modelos. Use setas para navegar.
- `/model <nome>` — Seleciona modelo diretamente (ex: `/model zenmux/stepfun/step-3.7-flash-free`)
- `/new` — Limpa o contexto da sessão atual (útil ao trocar de modelo)

### Via Config (Padrão)

```json
{
  "model": "zenmux/stepfun/step-3.7-flash-free",
  "small_model": "zenmux/z-ai/glm-5.2-free"
}
```

- `model`: modelo principal para tarefas complexas
- `small_model`: modelo leve para tarefas rápidas (títulos, sumários)

### Múltiplos Provedores no Mesmo Config

Você pode ter **vários provedores** no mesmo `opencode.json` e alternar entre eles no `/models`:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "zenmux": { "models": { ... } },
    "ollama": { "npm": "@ai-sdk/openai-compatible", "name": "Ollama", "options": { "baseURL": "http://localhost:11434/v1" }, "models": { ... } },
    "lmstudio": { "npm": "@ai-sdk/openai-compatible", "name": "LM Studio", "options": { "baseURL": "http://127.0.0.1:1234/v1" }, "models": { ... } }
  }
}
```

### Via Linha de Comando

```bash
opencode --model zenmux/stepfun/step-3.7-flash-free
```

---

## 9. Privacidade e Limitações

### Modelos Hospedados (Zen, ZenMux)

| Serviço | Política de Dados |
|---------|------------------|
| **OpenCode Zen (gratuito)** | Dados **podem** ser usados para melhoria do modelo durante período free |
| **ZenMux** | Zero-retention policy — dados não são armazenados |
| **OpenCode Zen (pago)** | Provedores seguem política de zero retenção |

### Modelos Locais (Ollama, LM Studio)

✅ **Privacidade total** — nada sai da sua máquina  
✅ **Sem custo de API**  
❌ **Requer hardware** (RAM/GPU)  
❌ **Mais lentos** que modelos em nuvem  
❌ **Menor qualidade** que modelos frontier pagos  

### Limitações Gerais dos Modelos Gratuitos

1. **Taxa de limite (rate limit)** — modelos free têm chamadas limitadas
2. **Disponibilidade temporária** — podem ser descontinuados sem aviso
3. **Qualidade inferior** — erram mais que modelos pagos em tarefas complexas
4. **Contexto menor** — alguns modelos free têm contexto reduzido
5. **Sem suporte a multimodal** — a maioria não processa imagens
6. **Latência maior** — filas de prioridade mais baixas

---

## Glossário

| Termo | Significado |
|-------|------------|
| **SWE-bench** | Benchmark de engenharia de software (resolver issues reais) |
| **Tool calling** | Capacidade do modelo de chamar funções/ferramentas |
| **MoE** | Mixture of Experts — arquitetura eficiente que ativa só parte dos parâmetros |
| **Q4_K_M** | Quantização de 4 bits — reduz tamanho do modelo com pouca perda de qualidade |
| **FIM** | Fill-in-the-Middle — preenchimento de código no meio (autocomplete) |
| **Context window** | Quantidade máxima de tokens que o modelo "enxerga" por vez |

---

## Fontes

- [OpenCode Zen Docs](https://opencode.ai/docs/zen/)
- [OpenCode Providers](https://opencode.ai/docs/providers/)
- [OpenCode Config](https://opencode.ai/docs/config/)
- [Ollama + OpenCode](https://docs.ollama.com/integrations/opencode)
- [ZenMux + OpenCode](https://docs.zenmux.ai/best-practices/opencode.html)
- [OpenCode Self-hosted Models](https://opencode-ai-opencode.mintlify.app/advanced/self-hosted-models)
- [Kilo Open-Source Models 2026](https://kilo.ai/open-source-models)
- [AiDevOps + OpenCode (Cloudron Forum)](https://forum.cloudron.io/topic/15277/ai-devops-opencode-make-coding-free-with-zen-models-no-claude-openai-google)
- [Hidden Models Guide (AI Sulat)](https://ai.sulat.com/how-to-add-hidden-models-to-opencode-without-creating-a-new-provider-c102783f3cae)
- [LM Studio + OpenCode Guide](https://getdeploying.com/guides/lm-studio-opencode)
- [Best Open-Weight Coding Models 2026 (Botmonster)](https://botmonster.com/ai/best-open-weight-coding-models-2026/)
