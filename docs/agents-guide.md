# Guia de Agentes

> **Os 35 agentes, suas funcoes, e quando usar cada um.**

## Taxonomia dos Agentes

### Camada 1: Primary (decisor/orquestrador)

Estes agentes podem ser escolhidos como default no opencode.json.

| Agente | Sistema | Modelo | Foco |
|--------|---------|--------|------|
| `supervisor` | max-thinking | MiniMax-M3 max | Aprovar/rejeitar codigo |
| `code-architect` | max-thinking | MiniMax-M3 max | Design de sistema |
| `quality-gate` | max-thinking | MiniMax-M3 max | Qualidade maxima |
| `orquestrador` | multi-agent | north-mini-code | Coordenar agentes de codigo |
| `strategic-planner` | decision-system | MiniMax-M3 minimal | Estrategia rapida |
| `financial-advisor` | decision-system | MiniMax-M3 minimal | Decisao financeira |
| `risk-manager` | decision-system | MiniMax-M3 minimal | Avaliacao de risco |
| `tech-lead` | decision-system | DeepSeek V4 minimal | Decisao tecnica |
| `marketing-strategist` | decision-system | DeepSeek V4 minimal | Marketing rapido |
| `ops-manager` | decision-system | DeepSeek V4 minimal | Operacoes |

### Camada 2: Specialist (sub-agente de codigo - multi-agent)

| Agente | Foco | Skills |
|--------|------|--------|
| `code-reviewer` | Revisao de codigo | code-review, code-review-checklist |
| `testador` | Testes e TDD | test-driven-development |
| `debugger` | Debug sistematico | systematic-debugging, node-inspect-debugger |
| `refatorador` | Refatoracao | safe-refactor |
| `security-auditor-multiagent` | Seguranca | security-review, security-scan |
| `otimizador` | Performance | property-based-testing |

### Camada 3: Specialist (sub-agente de conhecimento - multi-agent)

| Agente | Foco |
|--------|------|
| `orquestrador-conhecimento` | Coordena agentes de conhecimento |
| `pesquisador` | Pesquisa de tecnologia |
| `documentador` | Documentacao tecnica |
| `arquiteto` | Arquitetura |
| `devops` | CI/CD, deploy |

### Camada 4: Specialist (max-thinking - auditoria)

| Agente | Foco |
|--------|------|
| `code-reviewer-x` | Review 7 camadas (EXTREMO) |
| `fix-suggester` | O QUE APAGAR/ADICIONAR/FAZER/BAIXAR |
| `library-curator` | Recomendar biblioteca |
| `dependency-auditor` | CVEs, desatualizadas |
| `standards-enforcer` | Convencoes, estilo |
| `security-auditor` | OWASP Top 10 |
| `performance-auditor` | Big O, memoria, I/O |
| `test-coverage-auditor` | Gaps de teste |
| `docs-auditor` | Documentacao |

### Camada 5: Specialist (decision-system - sub-decisores)

| Agente | Foco |
|--------|------|
| `visionary` | Pensamento 5 anos |
| `prioritizer` | Ranking rapido |
| `cost-analyzer` | Decompor custos |
| `revenue-predictor` | Forecasting receita |
| `threat-scanner` | Vulnerabilidades |
| `solution-architect` | Design tecnico |
| `integrator` | Integracao sistemas |
| `campaign-optimizer` | ROI marketing |
| `process-optimizer` | Eficiencia processos |
| `resource-allocator` | Alocar recursos |

## Quando Usar Cada Agente

### Por Tipo de Tarefa

```
TAREFA                            AGENTE
────────────────────────────────────────────────────────
Revisar codigo rapido             @code-reviewer (multi-agent)
Revisar codigo rigoroso            @code-reviewer-x (max-thinking)
Auditar seguranca                 @security-auditor (max-thinking)
Auditar seguranca rapido          @security-auditor-multiagent (multi-agent)
Implementar testes                @testador (multi-agent)
Cobrir gaps de teste              @test-coverage-auditor (max-thinking)
Corrigir bug                      @debugger (multi-agent)
Refatorar                         @refatorador (multi-agent)
Refatorar com seguranca           @safe-refactor (skill)
Otimizar performance              @otimizador (multi-agent)
Auditar performance               @performance-auditor (max-thinking)
Pesquisar tecnologia              @pesquisador (multi-agent agent2)
Escolher biblioteca               @library-curator (max-thinking)
Criar documentacao                @documentador (multi-agent agent2)
Auditar documentacao              @docs-auditor (max-thinking)
Desenhar arquitetura              @arquiteto (multi-agent agent2)
Desenhar arquitetura rigoroso     @code-architect (max-thinking)
CI/CD                             @devops (multi-agent agent2)
Aprovar/rejeitar codigo           @supervisor (max-thinking)
Aprovar final                     @quality-gate (max-thinking)
Decisao estrategia                @strategic-planner (decision-system)
Decisao financeira                @financial-advisor (decision-system)
Decisao risco                     @risk-manager (decision-system)
Decisao stack                     @tech-lead (decision-system)
Decisao marketing                 @marketing-strategist (decision-system)
Decisao operacoes                 @ops-manager (decision-system)
```

## Como Delegar

No OpenCode:
```
@code-reviewer-x "Revise src/auth/login.ts para SQL injection"
@supervisor "Audite este PR #123"
@financial-advisor "Devo investir R$ 30k em marketing?"
@library-curator "Qual lib de audio para Python?"
```

## Quando Combinar Multiplos Agents

### Fan-out (paralelo)
```
@code-reviewer-x "Revise codigo"
@test-coverage-auditor "Encontre gaps"
@security-auditor "Audite seguranca"
@performance-auditor "Analise performance"
```

Use quando sub-tarefas sao independentes.

### Sequencial
```
1. @pesquisador "Pesquise bibliotecas de auth"
2. @arquiteto "Avalie as opcoes do pesquisador"
3. @code-reviewer "Revise a recomendacao final"
```

Use quando ha dependencia entre resultados.

### Conselho
```
@arquiteto "Analise arquitetura"
@security-auditor "Analise seguranca"
@otimizador "Analise performance"
[consolida com critical-thinking]
```

Use para decisoes criticas.

## Limites de Cada Agente

| Agente | NAO use para |
|--------|--------------|
| @debugger | Decisoes de design |
| @testador | Implementar feature |
| @code-reviewer | Decidir stack |
| @pesquisador | Implementar |
| @supervisor | Tarefas triviais |
| @financial-advisor | Decisoes tecnicas |
| @strategic-planner | Implementar |

## Onde Sao Definidos

- **opencode.json** (global) tem 35 agents
- **max-thinking-system/.opencode/agents/** tem 12 .md files
- **decision-system/.opencode/agents/** tem 6 .md files
- **multi-agent/** NAO tem .md files (definidos no opencode.json apenas)

## Como Adicionar um Novo Agent

1. Crie em `multi-agent/.opencode/agents/CATEGORIA/NOME.md` OU adicione direto no `~/.config/opencode/opencode.jsonc`
2. Defina: name, model, mode, prompt, description
3. Opcional: variant, allowed-tools, permission
4. Reinicie o OpenCode
