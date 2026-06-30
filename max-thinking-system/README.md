# Max Thinking System — Sistema de Supervisao com Pensamento Maximo

> **Sistema que APROVA ou REJEITA codigo. Ve TUDO. Pensa MAXIMO. Nenhum codigo escapa.**

## Visao Geral

Sistema multi-agente OpenCode onde o **`@supervisor`** eh o chefe. Ele ve TODO o codigo, TODOS os agentes, TODAS as skills. Sua missao: aprovar ou rejeitar codigo com revisao CIRURGICA, dizendo **O QUE APAGAR, O QUE ADICIONAR, O QUE FAZER, O QUE BAIXAR** (ate bibliotecas).

### Diferenca dos outros sistemas

| Aspecto | multi-agent | decision-system | **max-thinking-system** |
|---------|-------------|-----------------|------------------------|
| Foco | Codigo + Conhecimento | Decisoes rapidas | **Supervisao profunda** |
| Thinking | Normal | Minimal | **MAX (maximo)** |
| Aprovacao | Distribuida | Cada agente decide | **Centralizada (supervisor)** |
| Skills | 161+ | 11 | **6 ultra-especializadas** |
| Agentes | 10 | 16 | **12 (1 supervisor + 11 specialists)** |

## Arquitetura

### 3 Agentes Principais (Primary)

1. **`@supervisor`** — O CHEFE. Ve tudo. Aprova/rejeita codigo.
2. **`@code-architect`** — Design de sistema profundo.
3. **`@quality-gate`** — Aprovacao final multi-aspecto.

### 9 Sub-Agentes (Specialists)

| Agente | Modelo | Foco |
|--------|--------|------|
| `code-reviewer-x` | MiniMax-M3 max | Revisao de codigo 7 camadas |
| `fix-suggester` | DeepSeek V4 max | O que apagar/adicionar/fazer/baixar |
| `library-curator` | DeepSeek V4 max | Escolher biblioteca |
| `dependency-auditor` | MiniMax-M3 max | CVEs, desatualizadas |
| `standards-enforcer` | MiniMax-M3 max | Convencoes, estilo |
| `security-auditor` | MiniMax-M3 max | OWASP Top 10 |
| `performance-auditor` | MiniMax-M3 max | Big O, memoria, I/O |
| `test-coverage-auditor` | DeepSeek V4 max | Gaps de teste |
| `docs-auditor` | DeepSeek V4 max | Documentacao |

**TODOS com `variant: max`** = pensamento maximo em cada chamada.

## 6 Skills Ultra-Especializadas

### Core
- **`supervisor`** — A SKILL SUPERVISORA. Ve tudo. Aprova/rejeita.
- **`code-review`** — 7 camadas de revisao
- **`max-thinking`** — Raciocinio 7 camadas
- **`deep-analysis`** — Analise 5 camadas de sistema
- **`fix-suggester`** — Framework 4-acoes
- **`library-curator`** — Framework 7-criterios

## Como o Supervisor Trabalha

### Fluxo de Revisao
```
@supervisor ativado
    │
    ├─→ @code-reviewer-x (revisao geral)
    ├─→ @security-auditor (OWASP)
    ├─→ @performance-auditor (Big O)
    ├─→ @test-coverage-auditor (gaps)
    ├─→ @docs-auditor (docs)
    ├─→ @dependency-auditor (CVEs)
    └─→ @standards-enforcer (padroes)
    │
    └─→ SINTETIZA
        ├── VEREDITO (APROVADO/RESSALVAS/REJEITADO)
        ├── SCORE (0-100)
        ├── O QUE APAGAR
        ├── O QUE ADICIONAR
        ├── O QUE FAZER
        └── O QUE BAIXAR (npm install ...)
```

### Output Padrao do Supervisor

```
═══════════════════════════════════════════════════════
        REVISAO SUPERVISORA - 2026-06-18 14:30
═══════════════════════════════════════════════════════

VEREDITO: REJEITADO
SCORE: 62/100

1. O QUE APAGAR (3):
   - src/auth.ts:42-50 - logica de sessao duplicada
   - src/auth.ts:88 - console.log esquecido
   - src/utils.ts:1-30 - funcao nao usada

2. O QUE ADICIONAR (2):
   - src/auth.ts:55 - try/catch em login
   - tests/auth.test.ts - suite de testes

3. O QUE FAZER (3):
   - Extrair logica de sessao em classe
   - Adicionar validacao de input
   - Renomear funcao foo() para algo descritivo

4. O QUE BAIXAR (1):
   - npm install zod (validacao de schema)
     Motivo: input nao validado permite injection
     Uso: const Schema = z.object({ ... })

═══════════════════════════════════════════════════════
```

## Estrutura de Pastas

```
max-thinking-system/
├── opencode.json              # Config (12 agentes, todos max)
├── README.md
├── .opencode/
│   ├── agents/
│   │   ├── main/              # 3 primary (.md)
│   │   │   ├── supervisor.md
│   │   │   ├── code-architect.md
│   │   │   └── quality-gate.md
│   │   └── specialists/       # 9 sub-agents (.md)
│   │       ├── code-reviewer-x.md
│   │       ├── fix-suggester.md
│   │       ├── library-curator.md
│   │       ├── dependency-auditor.md
│   │       ├── standards-enforcer.md
│   │       ├── security-auditor.md
│   │       ├── performance-auditor.md
│   │       ├── test-coverage-auditor.md
│   │       └── docs-auditor.md
│   ├── skills/                # 6 skills
│   │   ├── supervisor/        # A PRINCIPAL
│   │   ├── code-review/
│   │   ├── max-thinking/
│   │   ├── deep-analysis/
│   │   ├── fix-suggester/
│   │   └── library-curator/
│   ├── lsp/lsp.json           # 14 LSP servers
│   └── mcps/mcp.json          # 14 MCP servers
├── plugins/
│   ├── plugins.json           # 9 plugins customizados
│   └── custom/                # (vazio - reservado)
├── workspace/
│   ├── reviews/               # Historico de revisoes
│   ├── library-db/            # DB de bibliotecas conhecidas
│   └── changes/               # Log de mudancas
└── .omo/rules/
    └── always-supervise.md    # Regra permanente
```

## Como Usar

### Abrir o Sistema
```bash
opencode --dir "skills pastas melhorias agentes\max-thinking-system"
```

### Pedir Supervisao
```
"Revise o codigo que acabei de escrever"
"Posso fazer deploy deste PR?"
"Audite a feature X"
```

O supervisor vai:
1. Carregar todos os sub-agentes
2. Rodar revisao paralela
3. Sintetizar veredito
4. Salvar em `workspace/reviews/`

### Forcar Pensamento Maximo
Todos os agentes ja estao com `variant: max`. Para forcar MAIS ainda:
- Use `use skill:max-thinking` explicitamente
- Use `use skill:deep-analysis` para sistemas

## Plugins Customizados (9 poderosos, criados especificamente)

1. **`supervisor-engine`** — Motor supervisor que automatiza o fluxo completo
2. **`code-archeologist`** — Acha codigo morto, TODOs antigos, deps orfas
3. **`library-recommender`** — Detecta quando uma lib seria util
4. **`deep-analyzer`** — Analise 5 camadas automatica
5. **`metrics-collector`** — Metricas de uso/thinking
6. **`auto-fix-safe`** — Auto-fix SEGURO (soh low-severity)
7. **`knowledge-graph`** — Grafo de conhecimento do projeto
8. **`code-archaeology`** — Git history + blame
9. **`smell-detector`** — Code smells (long method, god class, etc)

## Modelos

| Modelo | Uso |
|--------|-----|
| **MiniMax-M3** (tokenrouter) | Supervisor, code-architect, quality-gate, e 5 specialists |
| **DeepSeek V4 Flash** (OpenRouter free) | Fix-suggester, library-curator, test-coverage-auditor, docs-auditor |
| **Claude Opus 4.8** | Disponivel para upgrade via plugin model-router |

Todos com `variant: max`.

## Proximos Passos

1. Adicionar API keys para MCPs que precisam (GitHub, Sentry, etc)
2. Configurar regras de pre-commit para auto-invocar supervisor
3. Criar webhooks para revisao automatica em PRs
4. Integrar com CI/CD para bloquear merge se REJEITADO
