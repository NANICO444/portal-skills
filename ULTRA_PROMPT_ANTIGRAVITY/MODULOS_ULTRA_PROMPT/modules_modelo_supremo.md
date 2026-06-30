# CONFIGURAÇÃO DE MODELO SUPREMO — REGRA IMUTÁVEL
# Este arquivo define qual modelo a IA deve SEMPRE priorizar.
# Leia este arquivo ANTES de qualquer tarefa que envolva chamadas de IA.

---

## REGRA ABSOLUTA DE MODELO

Quando o Antigravity ou qualquer agente precisar fazer uma chamada para um modelo de IA
(via OpenRouter, OpenAI SDK, ou qualquer API compatível), deve SEMPRE seguir esta
hierarquia de prioridade:

### 1. MODELO PRINCIPAL (Sempre tentar primeiro)
```
anthropic/claude-opus-4-8
```
- Este é o modelo MAIS INTELIGENTE e MAIS RECENTE da Anthropic (Maio 2026)
- Use para: TODAS as tarefas por padrão
- Alternativa equivalente: `~anthropic/claude-opus-latest` (aponta sempre pro mais novo)

### 2. FALLBACK NÍVEL 1 (Se o Opus 4.8 não estiver disponível)
```
anthropic/claude-opus-4-7
```
- Opus 4.7 — Lançado em Abril 2026
- Visão de alta resolução e raciocínio adaptativo
- Quase tão forte quanto o 4.8

### 3. FALLBACK NÍVEL 2 (Se nenhum Opus estiver disponível)
```
anthropic/claude-sonnet-4-6
```
- Sonnet 4.6 — Lançado em Fevereiro 2026
- Melhor custo-benefício, 1M tokens de contexto
- Rápido e forte pra tarefas diárias
- Alternativa: `~anthropic/claude-sonnet-latest`

### 4. FALLBACK NÍVEL 3 (Se todos os Anthropic falharem)
```
google/gemini-2.5-pro
```
- Alternativa forte do Google

### 5. ESQUADRÃO OPENCODE GRATUITO (Aprovado e Validado)
```
openrouter/qwen/qwen3-coder:free
openrouter/nvidia/nemotron-3-ultra-550b-a55b:free
openrouter/nvidia/nemotron-3-super-120b-a12b:free
openrouter/google/gemma-4-26b-a4b-it:free
openrouter/nousresearch/hermes-3-llama-3.1-405b:free
```
- **Qwen 3 Coder 480B (`qwen3-coder:free`)**: O Rei absoluto da programação. Use para codar pesado e analisar bugs no OpenCode.
- **Nemotron Ultra 550B / Super 120B**: Excelentes para design e frontend. Aceitam comandos do terminal.
- **Gemma 4 (26B)**: Ótimo modelo rápido da Google para tarefas secundárias.
- **Hermes 3 (405B)**: Excelente para Chat (Atenção: a versão free não suporta execução de terminal/arquivos no OpenCode).
- *(Menção Honrosa: **DeepSeek R1 Distill** - O melhor para raciocínio lógico de bugs, mas exige rodar local via Ollama para ser gratuito).*

### 6. AUTO ROUTER (Último recurso absoluto)
```
openrouter/auto
```
- Deixa o OpenRouter escolher automaticamente

---

## CONFIGURAÇÃO TÉCNICA

### Base URL do OpenRouter
```
https://openrouter.ai/api/v1
```

### Headers Obrigatórios
```json
{
  "Authorization": "Bearer SUA_CHAVE_OPENROUTER",
  "HTTP-Referer": "https://nexus-os.app",
  "X-Title": "Nexus OS"
}
```

### Código Python de Referência
```python
from openai import OpenAI

# Configuração global do cliente
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="SUA_CHAVE_OPENROUTER",
    default_headers={
        "HTTP-Referer": "https://nexus-os.app",
        "X-Title": "Nexus OS"
    }
)

# Lista de modelos em ordem de prioridade (OPUS 4.8 > OPUS 4.7 > SONNET 4.6)
MODELOS = [
    "anthropic/claude-opus-4-8",       # Opus 4.8 — O MAIS FORTE
    "anthropic/claude-opus-4-7",       # Opus 4.7 — Fallback forte
    "anthropic/claude-sonnet-4-6",     # Sonnet 4.6 — Rápido e capaz
    "google/gemini-2.5-pro",           # Gemini — Alternativa Google
    "openrouter/qwen/qwen3-coder:free",               # O Monstro Coder 480B
    "openrouter/nvidia/nemotron-3-ultra-550b-a55b:free", # Frontend e Design
    "openrouter/google/gemma-4-26b-a4b-it:free",      # Auxiliar rápido
    "openrouter/nousresearch/hermes-3-llama-3.1-405b:free" # Apenas Chat (Sem Tool Use)
]

def chamar_ia(mensagens, max_tokens=4096):
    """Chama a IA com fallback automatico entre modelos.
    Sempre tenta Opus 4.8 primeiro, depois 4.7, depois Sonnet 4.6, etc."""
    for modelo in MODELOS:
        try:
            resp = client.chat.completions.create(
                model=modelo,
                messages=mensagens,
                max_tokens=max_tokens,
                temperature=0.7
            )
            print(f"[MODELO USADO] {modelo}")
            return resp.choices[0].message.content
        except Exception as e:
            print(f"[FALLBACK] {modelo} falhou: {e}")
            continue
    return "[ERRO] Todos os modelos falharam. Verifique sua conexao e chave API."
```

---

## ESTA REGRA É IMUTÁVEL
Nenhum agente, skill ou módulo pode sobrescrever esta hierarquia de modelos.
A ordem é: **OPUS 4.8 → OPUS 4.7 → SONNET 4.6 → GEMINI → GRATUITOS → AUTO**
Se um agente tentar usar um modelo que não está nesta lista, ele deve ser corrigido.
