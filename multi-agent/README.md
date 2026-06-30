# multi-agent

> **Sistema 1: codigo com servidores headless + 164 skills.**

## O que e

O sistema multi-agent tem 2 servidores headless rodando:
- **Agent 1 (porta 3001):** opencode/north-mini-code-free — codigo
- **Agent 2 (porta 3002):** openrouter/openai/gpt-oss-120b:free — conhecimento

**Nao roda mais os scripts dentro do OpenCode.** Os servidores ficam de pe como servico, e o OpenCode conecta neles.

## Como iniciar

```powershell
.\start-agents.ps1
```

Aguarda ~5 segundos e mostra "ONLINE" se subiu OK.

## Como parar

```powershell
.\stop-agents.ps1
```

## Status

```powershell
.\status-agents.ps1
```

## Delegar tarefa

```powershell
.\delegar.ps1 code-reviewer "Revise o arquivo src/auth.ts"
```

## Sub-agentes

### Agent 1 (codigo)

| Sub-agente | Foco |
|------------|------|
| `orquestrador` | Orquestra os sub-agentes |
| `code-reviewer` | Review de codigo |
| `testador` | Testes e TDD |
| `debugger` | Debug |
| `refatorador` | Refatoracao |
| `security-auditor` | Seguranca |
| `otimizador` | Performance |

### Agent 2 (conhecimento)

| Sub-agente | Foco |
|------------|------|
| `orquestrador-conhecimento` | Orquestra os sub-agentes |
| `pesquisador` | Pesquisa de tecnologia |
| `documentador` | Documentacao tecnica |
| `arquiteto` | Arquitetura |
| `devops` | CI/CD, infra |

## Documentacao

- `INSTRUCAO_OPENCODE.md` — manual completo de uso (16.5 KB)
- `agentes-info.txt` — referencia rapida

## Skills

164 skills instaladas em `.opencode/skills/`. Veja `INDEX.md` na raiz do projeto.

## Regra

`.omo/rules/always-use-agents.md` — sempre delegue para o sub-agente certo.
