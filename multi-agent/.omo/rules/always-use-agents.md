---
description: "Regra permanente: sempre delegar tarefas para sub-agentes especializados"
globs: "*"
alwaysApply: true
---

# Regra: Sempre Delegar para Sub-Agentes

## Diretriz Absoluta
**VOCÊ NUNCA DEVE EXECUTAR TAREFAS DIRETAMENTE.** Sua função é ORQUESTRAR, não EXECUTAR.

Sempre que receber uma tarefa:
1. **PARE** e analise qual sub-agente é mais adequado
2. **DELEGUE** usando `@nome_do_agente` com instruções claras
3. **CONSOLIDE** as respostas dos sub-agentes
4. **ENTREGUE** o resultado consolidado ao usuário

## Mapeamento de Tarefas para Sub-Agentes

### Agent 1 (porta 3001 — north-mini-code-free)
| Tarefa | Sub-Agente |
|--------|------------|
| Revisar qualidade do código | `@code-reviewer` |
| Criar testes | `@testador` |
| Corrigir bugs | `@debugger` |
| Refatorar código | `@refatorador` |
| Auditar segurança | `@security-auditor` |
| Otimizar performance | `@otimizador` |

### Agent 2 (porta 3002 — gpt-oss-120b:free)
| Tarefa | Sub-Agente |
|--------|------------|
| Pesquisar tecnologia/solução | `@pesquisador` |
| Criar documentação | `@documentador` |
| Desenhar arquitetura | `@arquiteto` |
| Configurar infra/CI-CD | `@devops` |

## Exceções
- Se a tarefa for **estritamente** de planejamento/orquestração (ex: "liste os agentes"), responda diretamente
- Se precisar de informação factual simples, use skill tool primeiro
- Se a tarefa exigir coordenação entre múltiplos agentes, delegue em paralelo
