# Guia dos 3 Sistemas

> **Quando usar cada sistema, e como eles se relacionam.**

## Visao Geral

```
┌─────────────────────────────────────────────────────────────┐
│                OPENCODE (qualquer chat)                       │
└─────────────────────────────────────────────────────────────┘
                              │
       ┌──────────────────────┼──────────────────────┐
       ▼                      ▼                      ▼
┌─────────────┐       ┌──────────────┐       ┌──────────────┐
│   SISTEMA 1 │       │   SISTEMA 2  │       │   SISTEMA 3  │
│ multi-agent │       │  decision-   │       │  max-thinking│
│             │       │   system     │       │   -system    │
│  Codigo +   │       │  Decisao     │       │ Supervisao + │
│ Servidores  │       │  rapida      │       │ Pensamento   │
│  + 164 skills│      │  + 12 skills │       │ maximo +     │
│             │       │              │       │  6 skills    │
└─────────────┘       └──────────────┘       └──────────────┘
       │                     │                      │
       ▼                     ▼                      ▼
   North-Mini-Code     MiniMax-M3               MiniMax-M3
   GPT-OSS-120B        DeepSeek V4              (max thinking)
```

## Decisao rapida: qual sistema usar

### Perguntas de CODIGO

| Sua tarefa | Sistema | Por que |
|------------|---------|---------|
| Escrever nova feature | multi-agent + max-thinking | implementa + revisa |
| Corrigir bug | multi-agent (debugger) | tem metodo sistematico |
| Code review rigoroso | max-thinking (supervisor) | rigor + 7 sub-agentes |
| Refatorar codigo | multi-agent (refatorador) | tem skill safe-refactor |
| Testes | multi-agent (testador) | tem skill TDD |
| Auditar seguranca | max-thinking (security-auditor) | OWASP completo |
| Otimizar performance | max-thinking (performance-auditor) | Big O + memoria |

### Perguntas de DECISAO

| Sua tarefa | Sistema | Decisor |
|------------|---------|---------|
| "Devo investir/comprar/gastar X?" | decision-system | @financial-advisor |
| "Devo fazer/nao fazer Y?" | decision-system | @strategic-planner |
| "Isso eh arriscado?" | decision-system | @risk-manager |
| "Qual lib/framework usar?" | decision-system | @tech-lead |
| "Como vender/marketing?" | decision-system | @marketing-strategist |
| "Como organizar/melhorar processo?" | decision-system | @ops-manager |
| "Mudanca arquitetural grande" | max-thinking | @arquiteto + complex-architecture-decision |

### Perguntas de CONHECIMENTO

| Sua tarefa | Sistema | Quem |
|------------|---------|------|
| "Pesquise biblioteca/framework" | multi-agent agent2 | @pesquisador |
| "Documente X" | multi-agent agent2 | @documentador |
| "Desenhe arquitetura" | multi-agent agent2 | @arquiteto |
| "CI/CD, deploy" | multi-agent agent2 | @devops |

### Perguntas MIXTAS (codigo + decisao + conhecimento)

Use **max-thinking** como padrao, e delegue internamente.

## Fluxo Típico de Trabalho

### Cenario 1: Tarefa de codigo simples
```
1. Usuario: "Adicionar busca na listagem"
2. OpenCode detecta always-delegate
3. @orquestrador (multi-agent) implementa
4. @supervisor (max-thinking) revisa
5. Output: APROVADO + detalhes
```

### Cenario 2: Decisao rapida
```
1. Usuario: "Vale a pena contratar servico X?"
2. @financial-advisor (decision-system) responde
3. Output: SIM/NAO/VALOR com ROI
```

### Cenario 3: Decisao arquitetural
```
1. Usuario: "Devo mudar para microservicos?"
2. @arquiteto (multi-agent agent2) carrega skill complex-architecture-decision
3. Output: 7 camadas de analise + recomendacao + pre-commitment
4. ADR criado para documentar
```

### Cenario 4: Bug em producao
```
1. Usuario: "Login esta falhando"
2. @debugger (multi-agent) usa systematic-debugging
3. Reproduz, isola, hipotese, fix, teste
4. @supervisor valida o fix
5. Output: BUG RESOLVIDO + teste de regressao
```

### Cenario 5: Pesquisa + Recomendacao
```
1. Usuario: "Qual lib de audio usar?"
2. @pesquisador (multi-agent agent2) carrega library-curator
3. Pesquisa, compara, recomenda
4. Output: tabela + comando install + exemplo
```

## Como os sistemas compartilham skills

Os 3 sistemas compartilham algumas skills:

| Skill | Disponivel em |
|-------|--------------|
| `supervisor` | multi-agent + max-thinking (sua pasta original) |
| `code-review` | multi-agent + max-thinking |
| `kiro-engineering-process` | multi-agent (sintetizada) |
| `think-max-protocol` | multi-agent (sintetizada) |
| `impeccable-quality` | multi-agent (sintetizada) |
| `decision-system-master` | decision-system |
| `*-decision` (6 skills) | decision-system |

## Quando NAO usar um sistema

### NUNCA use multi-agent para:
- Decisoes rapidas (use decision-system)
- Code review rigoroso (use max-thinking)

### NUNCA use decision-system para:
- Implementacao de codigo (use multi-agent)
- Bug fixing (use multi-agent)

### NUNCA use max-thinking para:
- Decisoes de 5 segundos (use decision-system)
- Pesquisa rapida (use multi-agent agent2)

## Onde estao os agentes no global

O OpenCode global tem 35 agents:

- **max-thinking (12):** supervisor, code-architect, quality-gate, code-reviewer-x, fix-suggester, library-curator, dependency-auditor, standards-enforcer, security-auditor, performance-auditor, test-coverage-auditor, docs-auditor
- **multi-agent (7):** orquestrador, code-reviewer, testador, debugger, refatorador, security-auditor-multiagent, otimizador
- **decision-system (16):** 6 primary + 10 sub-agents

Total: 35 agents, todos com `variant: max` (exceto decision-system que tem `variant: minimal`).

## Como forcar uso de um sistema especifico

No seu prompt, mencione explicitamente:
- "use o @supervisor" → max-thinking
- "use o @financial-advisor" → decision-system
- "use o @orquestrador" → multi-agent
- "use a skill [nome]" → qualquer sistema

## Quando chamar o @supervisor

Use @supervisor SEMPRE que:
- For commitar codigo
- For mergear PR
- For deploy
- Quiser revisao rigorosa
- Quiser ver "O QUE APAGAR, ADICIONAR, FAZER, BAIXAR"

## Quando chamar o @orquestrador

Use @orquestrador quando:
- For implementar feature
- For corrigir bug
- For refatorar

## Quando chamar @financial-advisor / @risk-manager / etc

Use os decisores quando:
- Pergunta envolver dinheiro (financial)
- Pergunta envolver ameaca (risk)
- Pergunta envolver marketing (marketing-strategist)
- Etc
