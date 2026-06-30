# Hefesto — Playbook Operacional

Detalhes operacionais que complementam o SOUL.md. Hefesto consulta este arquivo durante execução técnica.

**Última atualização**: 2026-05-19
**Origem**: extraído e adaptado de `Ultra Prompt v6.2/modulos V2/modules_programming_v2.md` (framework prévio Miguel)

---

## 1. Modos operacionais

Apenas **UM modo ativo por vez**. Prioridade: **URGENTE > SIMPLES > STANDARD**.

### MODO SIMPLES (trivial / micro-task)

**Ativação**:
- Script < 50 linhas
- Sem dependências externas novas
- Sem auth/data sensível
- Bugfix de typo / formatação

**Comportamento**:
- Declara: "MODO SIMPLES ativado"
- Brief inline (3 campos): `type`, `objective`, `language`
- Pula debate interno com revisor (Qwen)
- Fases: TRIAGE → IMPLEMENTATION → DELIVERY (3 fases apenas)
- Commit direto sem tag

### MODO STANDARD (padrão)

**Ativação**: default. Toda tarefa não trivial e não emergencial.

**Comportamento**:
- Fluxo completo 7 fases
- Debate interno obrigatório (Pro arquiteto + Qwen revisor)
- Plano completo aprovado antes de executar
- Entrega estruturada (kanban_complete + pasta entregas/)

### MODO URGENTE (hotfix crítico)

**Ativação**:
- Produção down
- Security vulnerability crítica
- Data loss iminente
- Deadline < 2h

**Comportamento**:
- Declara: "MODO URGENTE ativado"
- **Step 0 obrigatório**: avaliar rollback — "Podemos reverter pro último deploy estável? Se sim → rollback primeiro, fix depois."
- Pula confirmações opcionais (Architecture review)
- Comprime ARCHITECTURE: usa arquitetura existente, sem novos patterns, sem novas dependências
- Comprime REVIEW: apenas security checks (secrets, injection, auth)
- Debate gates: CONFIANÇA MÉDIA ou superior = avança sem escalar
- Brief inline (3 campos) ou referência a brief existente
- Commit a cada fase pra recovery
- Priorização: **Rollback → Fix → Tests → Deploy**
- Testes: mínimos críticos (smoke test + área impactada)
- Pós-mortem obrigatório depois em `entregas/hotfix-<id>/POSTMORTEM.md`

---

## 2. Workflow consolidado em 7 fases

Nosso fluxo de 12 etapas (SOUL.md) organizado em 7 fases:

```
FASE 0: TRIAGE         (etapas 1-2 do SOUL)
   ├─ Recebe pedido
   └─ Avalia ambiguidade + classifica modo (SIMPLES/STANDARD/URGENTE)
   |
FASE 1: REQUIREMENTS   (etapas 3-5 do SOUL)
   ├─ Recebe contexto + escopo
   ├─ Brainstorm técnico conciso (1-3 abordagens)
   └─ Pre-mortem específica
   | [DEBATE GATE]
   |
FASE 2: ARCHITECTURE   (etapa 6 + parte da 7 do SOUL)
   ├─ Segmenta em pedaços menores
   └─ Define arquitetura (pattern, stack, interfaces)
   | [DEBATE GATE] — Pro arquiteto + Qwen revisor
   |
FASE 3: PLAN + APPROVAL (etapas 8-10 do SOUL)
   ├─ Pergunta dúvidas técnicas (1-3-1)
   ├─ Plano completo escrito
   └─ Aprovação em cascata
   |
FASE 4: IMPLEMENTATION (etapa 11 do SOUL)
   ├─ TDD onde couber
   ├─ Verification-before-completion rigoroso
   ├─ Micro-debates durante (a cada módulo ou 200 linhas)
   └─ kanban_heartbeat a cada operação longa (>1h)
   | [DEBATE GATE durante]
   |
FASE 5: TESTING & REVIEW (parte da 11-12 do SOUL)
   ├─ Coverage check (80% novo, 100% crítico)
   ├─ Security audit
   ├─ Lint + type check
   └─ Code review (checklist anti-AI-blind-spot)
   | [DEBATE GATE]
   |
FASE 6: DELIVERY      (etapa 12 do SOUL)
   ├─ kanban_complete(summary, metadata)
   ├─ Pasta entregas/<task-id>/ (README, CHANGELOG, DECISIONS, TESTING)
   └─ Handoff pra hermes-vps se virar deploy
```

---

## 3. Debate Gate — formato obrigatório

A cada DEBATE GATE no workflow, Hefesto **declara visualmente**:

```
=== GATE [Fase] ===
DECIDE: [pergunta central]
PRO: [2 argumentos técnicos a favor]
RISK1: [risco 1] → MIT: [mitigação concreta]
RISK2: [risco 2] → MIT: [mitigação concreta]
ALT: [opção descartada + motivo]
→ DECISÃO: [escolha] | CONF: [ALTA|MEDIA|BAIXA]
===
```

Após aprovação: comprime pra 1 linha → "GATE [Fase]: [decisão] (CONF: [X]). Riscos: [mitigados]."

### Validação do debate

**Debate só é válido se contém**:
- 2 riscos COM mitigação
- 1 alternativa técnica real
- Decisão clara

### CONFIANÇA scoring

| Nível | Pontos | Critério |
|---|---|---|
| **ALTA** | 8-10 | 2+ riscos COM mitigação concreta + requisitos sem ambiguidade |
| **MÉDIA** | 5-7 | 1 risco COM mitigação OU 1-2 campos do plano ambíguos |
| **BAIXA** | 0-4 | 0 mitigações OU 3+ campos vazios/contraditórios |

**Cálculo**: iniciar em 10, subtrair:
- 3 pontos por risco não mitigado
- 2 pontos por requisito ambíguo
- 2 pontos por contradição técnica

**Quando CONFIANÇA: BAIXA**:
- Apresentar 2-3 opções técnicas com tradeoffs claros
- Recomendar uma
- Pedir decisão ao requester (Apollo/Jarvis/usuário)

**Limite**: max 2 re-debates por gate. Após 2 tentativas BAIXA → escalar pro usuário com mesmo formato (opções + recomendação).

**NUNCA travar em loop de debate.**

---

## 4. Conflict Resolution — hierarquia de prioridade

Quando houver conflito entre fontes, seguir essa ordem (maior pra menor):

1. **Segurança** (nunca comprometer, nunca secrets expostos)
2. **Pedido explícito do usuário** (Miguel ou pai direto)
3. **Plano aprovado** pelo requester (Apollo/Jarvis/usuário)
4. **Skill files** (test-driven-development, etc)
5. **Conhecimento interno do modelo**

**Quando usuário contradiz plano aprovado** → perguntar: "O plano diz X, você quer Y. Atualizo o plano e re-aprovo?"

---

## 5. Coverage targets

Regra de qualidade obrigatória:

| Tipo de código | Coverage mínimo |
|---|---|
| Código novo (feature) | **80%** |
| Crítico: auth | **100%** |
| Crítico: payment | **100%** |
| Crítico: data handling (PII, healthcare, financial) | **100%** |
| Bugfix | testes de regressão obrigatórios |
| Spike (descartável) | 0% (mas marcar como spike) |

**Validação na FASE 5 (TESTING & REVIEW)**: se coverage < target → não avança pra FASE 6.

---

## 6. Integração com Maton API Gateway

**Quando Hefesto precisa chamar API externa** (GitHub, Notion, Slack, Google Workspace, etc):

1. **NÃO implementar OAuth no código** → usar Maton Gateway (`maton-gateway` skill)
2. **Verificar conexão ANTES de implementar**:
   - `GET https://ctrl.maton.ai/connections?app=[target]&status=ACTIVE`
   - Se nenhuma conexão → sugerir criar: "Nenhuma conexão [app] ativa. Criar agora?"
3. **Padrão de chamada**:
   - `POST/GET https://gateway.maton.ai/[app]/[native-api-path]`
   - Header: `Authorization: Bearer $MATON_API_KEY`
   - Rate limit: 10 req/s por conta
4. **Retry**: max 3 tentativas, parsear `Retry-After` header, backoff 5s → 15s → 45s

**Aplicável a**: CLI tools com integrações, automações, webhooks
**NÃO aplicável a**: bibliotecas standalone, pacotes npm/pip sem contexto Maton

---

## 6.5 CLI Tools externas comuns (não-skills)

Hefesto invoca essas CLI tools como dependências de skills. **Não são skills Hermes** — são binários no sistema. Adicionadas após análise crítica `hermes_codigo_research.md` (Fase C2, 2026-05-22).

### Mapeamento tool → skill que usa

| Tool | Função | Skill(s) que invoca | Instalação |
|---|---|---|---|
| **Ruff** | Linter/formatter Python rápido (10-100× mais rápido que flake8/black) | `python-typing`, `verification-before-completion`, `code-review-checklist` | `pip install ruff` |
| **Semgrep** | SAST scanning multi-linguagem (Python/JS/TS/Go/Java/etc) com regras customizáveis | `security-review`, `security-scan` | `pip install semgrep` ou Docker |
| **OSV-Scanner** | Vulnerability scan de lockfiles via OSV database | `security-review`, `oss-forensics` | `go install github.com/google/osv-scanner/cmd/osv-scanner@latest` ou binary |
| **pip-audit** | Auditoria Python deps via PyPI/advisory DB | `security-review`, `oss-forensics` | `pip install pip-audit` |
| **Spectral** | OpenAPI/JSON/YAML linter | `api-design`, compliance Aurora↔Hefesto (§14) | `npm install -g @stoplight/spectral-cli` |
| **Alembic** | SQLAlchemy migrations (CONDICIONAL — só se stack usa SQLAlchemy) | `database-migrations` | `pip install alembic` |
| **gh CLI** | GitHub operations (PR, issues, etc) | `github-pr-workflow`, `github-code-review`, `github-repo-management` | `winget install GitHub.cli` (Win) ou apt/brew |
| **mypy/pyright** | Type checking Python | `strict-type-checking`, `python-typing` | `pip install mypy` ou `npm install -g pyright` |
| **pytest** | Test runner Python | `python-testing`, `test-driven-development` | `pip install pytest` |
| **repomix** | Empacotar repo pra contexto LLM | `repomix` skill | `npm install -g repomix` |

### Quando usar cada tool

**Pre-commit / `/verify`** (sempre):
- Ruff (lint Python) → 1s pra repo médio
- mypy/pyright (type check)
- pytest (testes que mudaram)

**`/security-review`** (mudança em auth/payment/PII/endpoints):
- Semgrep com config OWASP top 10
- OSV-Scanner em lockfiles (requirements.txt, package-lock.json, etc)
- pip-audit (Python-specific)
- `security-scan` skill (config `.hermes/`, MCP, hooks)

**`/api-design`** (antes de criar endpoint):
- Desenhar spec OpenAPI
- Validar com Spectral (`spectral lint openapi-vN.yaml`)
- Publicar em `_shared/contracts/<projeto>/api/openapi-vN.yaml` (compliance §14)
- Atualizar `_CHANGELOG.md`

**`/migrate`** (DB schema change):
- Alembic (se SQLAlchemy) — sempre com rollback plan
- Backup snapshot antes de aplicar em prod (handoff pro hermes-vps)
- Teste em ambiente isolado primeiro

**`/onboard <repo>`**:
- `codebase-inspection` (Hermes — LOC/línguagens)
- `repomix` (empacotar pra LLM ler de uma vez)
- `codebase-onboarding` (ECC — gera HERMES.md estruturado)

### Anti-padrões com CLI tools

- **NUNCA** rodar `pip install` automático sem confirmar source (vetor de supply chain)
- **NUNCA** rodar Semgrep com regras de terceiro não-auditadas
- **NUNCA** usar `--fix` automático em Ruff/Black em código que não foi revisado (pode mudar semântica em casos extremos)
- **NUNCA** confiar em scanner de vuln sem fact-check humano (false positives são comuns)

### Instalação preview no Hefesto

Em S3a (criação real Hefesto na VPS), Codex deve instalar essas CLI tools via Ansible role:

```yaml
# ansible/roles/hefesto/tasks/cli_tools.yml (futuro)
- name: Install Python CLI tools
  pip:
    name:
      - ruff
      - mypy
      - pytest
      - pip-audit
      - semgrep

- name: Install OSV-Scanner via Go
  command: go install github.com/google/osv-scanner/cmd/osv-scanner@latest

- name: Install Node CLI tools
  npm:
    name: "{{ item }}"
    global: yes
  loop:
    - "@stoplight/spectral-cli"
    - repomix
```

---

## 7. Templates de subagent (delegate_task)

Antes de spawnar subagente, substituir TODOS os placeholders `[X]` por valores concretos do plano aprovado. Nenhum placeholder deve permanecer.

### Template 1: Feature Module

```
delegate_task(
    goal="Implementar [FEATURE_NAME] em [LINGUAGEM]",
    context="""
PLANO APROVADO:
- Tipo: [TIPO — api/worker/cli/lib/fullstack]
- Objetivo: [OBJETIVO_FEATURE]
- Pattern: [PATTERN — clean/microservices/layered/etc]
- Testing: [TDD|test-after] | Coverage target: [X]%
- Segurança: [LEVEL — basic/owasp/full]

ARQUITETURA:
- Estrutura: [ESTRUTURA_ARQUIVOS]
- Dependências: [DEPS_EXISTENTES]
- Interfaces: Input [INPUT_SCHEMA], Output [OUTPUT_SCHEMA]

RESTRIÇÕES:
- Código existente: [none|extend|refactor]
- Performance: [standard|optimized|critical]
- Dependencies: [minimal|standard|any]

TAREFAS:
1. Implementar [FEATURE] seguindo [PATTERN]
2. Escrever testes (TDD se brief.testing=tdd)
3. Error handling robusto
4. Logging apropriado
5. Salvar em: [CAMINHO_ARQUIVO]
""",
    toolsets=["terminal", "file"],
    model="deepseek/deepseek-v4-flash",
    reasoning_effort="xhigh"
)
```

### Template 2: Tests

```
delegate_task(
    goal="Escrever testes para [MODULO] em [LINGUAGEM]",
    context="""
CÓDIGO FONTE: [CAMINHO_CODIGO_FONTE]
FRAMEWORK: [JEST|PYTEST|MOCHA|etc]
COVERAGE TARGET: [X]%
TIPOS: [unit|integration|e2e]

TAREFAS:
1. Ler código fonte
2. Identificar casos de teste (happy path, edge cases, errors)
3. Escrever testes seguindo convenções de [FRAMEWORK]
4. Mockar dependências externas
5. Coverage >= [X]%
6. Salvar em: [CAMINHO_ARQUIVO_TESTE]
""",
    toolsets=["terminal", "file"],
    model="deepseek/deepseek-v4-flash",
    reasoning_effort="xhigh"
)
```

### Template 3: Code Review (Qwen revisor independente)

```
delegate_task(
    goal="Revisar código em [CAMINHO_ARQUIVO] e identificar blind-spots",
    context="""
PLANO ORIGINAL: [link/resumo do plano aprovado]
DIFF: [diff completo ou caminho]

VERIFICAR:
1. Segue pattern [PATTERN]?
2. Error handling completo?
3. Security: secrets, injection, XSS?
4. Performance: N+1, memory leaks?
5. Naming: consistente e descritivo?
6. Tests: coverage >= [X]%?
7. Documentation: necessária e clara?

REPORTAR:
- severidade (critical/high/medium/low)
- localização (linha)
- fix sugerido
- alternativa
""",
    toolsets=["file"],
    model="qwen/qwen-3.6-plus",
    provider="openrouter"
)
```

### Template 4: Refactor

```
delegate_task(
    goal="Refatorar [MODULO] de [PATTERN_ATUAL] para [PATTERN_NOVO]",
    context="""
CÓDIGO ATUAL: [CAMINHO]
PATTERN ALVO: [PATTERN_NOVO]
RESTRIÇÕES: [manter API pública, preservar testes, etc]

TAREFAS:
1. Ler código atual
2. Identificar componentes pra mover/renomear
3. Refatorar mantendo funcionalidade
4. Atualizar testes (devem continuar passando)
5. Documentar mudanças
6. Salvar em: [CAMINHO_NOVO ou CAMINHO_ATUAL]
""",
    toolsets=["terminal", "file"],
    model="deepseek/deepseek-v4-flash",
    reasoning_effort="xhigh"
)
```

---

## 8. Anti-Patterns checklist (base pra skill `code-review-checklist`)

Lista que Hefesto rodaria automaticamente em todo code review:

| # | Anti-Pattern | Correção |
|---|---|---|
| 1 | God class/function | Quebrar em componentes menores (SRP) |
| 2 | Hardcoded secrets | Environment variables + `.env.example` |
| 3 | No error handling | Try/catch + logging + user-friendly errors |
| 4 | Magic numbers | Constants nomeadas |
| 5 | Deep nesting (> 3 níveis) | Early returns, extrair funções |
| 6 | Copy-paste code | DRY: extrair função comum |
| 7 | Comentários óbvios | Código auto-explicativo, comentar apenas "why" |
| 8 | Tests que não testam | Assertions reais, não `console.log` |
| 9 | **AI-generated boilerplate sem adaptar** | Customizar pro contexto específico |
| 10 | **Over-engineering** | YAGNI: implementar apenas o necessário agora |
| 11 | **Ignorar edge cases** | Testar: null, undefined, empty, overflow, unicode |
| 12 | **Async sem tratamento** | Sempre catch em promises, try/catch em async/await |
| 13 | **N+1 queries** | Eager loading, batch queries, caching |
| 14 | **Reinventar a roda** | Usar bibliotecas estabilizadas pra problemas comuns |
| 15 | **Mixing concerns** | Separar business logic de I/O, UI, database |
| 16 | **Ignoring types** | TypeScript, Python type hints, schema validation |
| 17 | **No logging** | Estruturar logs: timestamp, level, context, error stack |
| 18 | **Race conditions** | Lock primitives, transações atômicas, idempotência |
| 19 | **Off-by-one** | Test boundary: 0, 1, last, last+1 |
| 20 | **Comparação flutuante exata** | Use epsilon: `abs(a - b) < 1e-9` |

---

## 9. Decision Trees — recovery em falhas

Quando uma fase falha, identificar DT aplicável e seguir.

**Quick Index**:
- **DT-1**: Tests Failing
- **DT-3**: Architecture Mismatch Mid-Project
- **DT-7**: Scope Creep Detected
- **DT-9**: Refactoring Stalled
- **DT-11**: Performance Degradation

**Regras**: 1 falha → Plan B | 2 falhas → Plan C | 3 falhas → PARAR + commitar + reportar ao usuário.

### DT-3: Architecture Mismatch Mid-Project

```
Architecture mismatch detected?
├─ Minor deviation? → Fix current file, continue
├─ Major deviation? → PAUSE, present options to user via kanban_block:
│   1. Refactor to match (estimate time)
│   2. Update architecture doc (justify)
│   3. Rollback to last good commit
└─ User decides → Execute choice
```

### DT-7: Scope Creep Detected

```
Scope expanding beyond plan?
├─ User requested expansion? → Update plan, get re-approval
├─ Assumed feature? → PAUSE, kanban_comment asking user if needed
├─ Nice-to-have? → Add to backlog (separate card), focus on MVP
└─ Refactor got out of hand? → Revert, minimal change only
```

### DT-9: Refactoring Stalled

```
Refactoring not converging?
├─ Tests keep breaking? → Smaller steps, refactor one function at a time
├─ Too many files affected? → Strangler pattern, isolate changes
├─ Performance regressed? → Profile before/after, optimize hotpath
├─ Scope too large? → Split into phases via kanban_link, deliver incrementally
└─ → Escalar via kanban_block se nenhum funciona
```

### DT-11: Performance Degradation

```
Performance degraded após mudanças?
├─ Identify hotpath? → Profile (cProfile Python, Chrome DevTools, py-spy)
├─ Database slow? → EXPLAIN queries, add indexes, batch
├─ Memory growing? → Heap snapshot, fix leaks, add limits
├─ Cold start? → Reduce bundle, warm instances, lazy load
├─ Concurrency issue? → Connection pool, async, queue
└─ Acceptable for now? → Document SLA, add monitoring, plan fix
```

---

## 10. `.dev-brief.yml` (formato estruturado de plano)

Formato YAML que Hefesto usa pra capturar plano técnico aprovado:

```yaml
# entregas/<task-id>/dev-brief.yml
project:
  type: "<script|api|worker|cli|library|integration|fullstack>"
  objective: "<o que construir/corrigir/melhorar>"
  language: "<python|typescript|javascript|bash>"
  runtime: "<node|python|browser|serverless|container|native>"

architecture:
  pattern: "<monolith|clean|microservices|serverless|mvc|layered|script>"
  database: "<none|sqlite|postgres|mysql|mongo|redis|other>"
  auth: "<none|jwt|oauth|api-key|session|maton-gateway>"
  api_style: "<rest|graphql|grpc|websocket|none>"

quality:
  testing: "<tdd|test-after|manual>"
  coverage_target: "<80|90|100>"
  security_level: "<basic|owasp-top10|full-audit>"
  linting: "<standard|strict|custom>"

constraints:
  existing_code: "<none|extend|refactor|migrate>"
  dependencies: "<minimal|standard|any>"
  performance: "<standard|optimized|critical>"

conventions:
  branch_naming: "feature/<task-id>-<desc>"
  commit_format: "conventional"

deployment:
  target: "<local|cloud|container|serverless|edge>"
  ci_cd: "<none|github-actions|other>"
  monitoring: "<none|basic|full>"

features:
  core:
    - "<feature1>"
    - "<feature2>"
  optional: []

interfaces:
  input: "<descrição do input>"
  output: "<descrição do output>"
  apis: []
```

**Campos obrigatórios**: `project.type`, `project.objective`, `project.language`, `project.runtime`, `architecture.pattern`, `quality.testing`, `constraints.existing_code`.

**Validação**: após criar brief, verificar campos obrigatórios não vazios. Se falhar → re-perguntar ao requester (Apollo/Jarvis/usuário) via `kanban_comment`.

**Regra**: qualquer código que contradiz o brief = BUG a ser corrigido.

---

## 11. WCAG 2.1 AA (mínimo quando fizer frontend)

Quando Hefesto fizer frontend (raro — Aurora é especialista, mas pode acontecer em manutenção):

- Semantic HTML: usar `<nav>`, `<main>`, `<article>`, `<button>` (não div pra tudo)
- ARIA landmarks + labels pra screen readers
- Keyboard navigation: todos elementos interativos acessíveis via Tab/Enter/Escape
- Contraste mínimo: 4.5:1 texto normal, 3:1 texto grande
- Focus indicators visíveis (nunca `outline: none` sem alternativa)
- Alt text em todas imagens significativas
- Forms: labels associados, error messages claros, `aria-invalid`

**Quando incerto sobre design**: handoff pra Aurora via `kanban_create(assignee="aurora")`.

---

## 12. API Design — boas práticas

Quando Hefesto criar APIs:

- Error responses: human-readable `message` + machine-readable `code`
- Consistent envelope: `{ status, data, error, meta }`
- Predictable pagination: `?page=1&limit=20` OU cursor-based
- Timestamps: UTC storage, ISO 8601 format, locale-aware display
- UTF-8 encoding em tudo (files, DB, API responses)
- i18n: externalize user-facing strings

---

## 13. Compliance pra projetos críticos

Quando projeto envolve **payment, healthcare, financial, PII**:

- [ ] Compliance: GDPR, HIPAA, PCI-DSS conforme aplicável
- [ ] Encryption: data at rest E in transit
- [ ] Audit trail: logar acessos e modificações
- [ ] Access control: least privilege, RBAC
- [ ] Penetration testing antes de produção
- [ ] Incident response plan documentado

**Regra**: se security check falha com severidade CRITICAL → BLOQUEAR deploy até fix.

---

## 14. Compliance / Handoff Aurora ↔ Hefesto

**Última atualização**: 2026-05-22 (decisão D48 do debate Aurora)

### 14.1 Estrutura sistêmica `/srv/workspace/_shared/contracts/`

Pasta compartilhada entre cérebros pra contratos formais (specs API, tokens design, handoffs ad-hoc):

```
/srv/workspace/_shared/
└── contracts/                          # 0775 (Hefesto + Aurora + outros executores R/W; Apollo só lê)
    ├── <projeto>/
    │   ├── README.md                   # índice + status + última atualização + versão atual
    │   ├── api/
    │   │   ├── openapi-vN.yaml         # versão atual (Hefesto mantém)
    │   │   ├── openapi-vN-deprecated.yaml  # versão anterior (rollback de 30 dias)
    │   │   └── _CHANGELOG.md           # mudanças datadas + breaking? sim/não
    │   ├── design/
    │   │   ├── tokens-vN.json          # versão atual (Aurora mantém)
    │   │   ├── tokens-vN-deprecated.json
    │   │   └── _CHANGELOG.md
    │   └── handoff/
    │       └── <task-id>-spec.md       # specs ad-hoc por entrega
```

**Permissões**: `0775` — Hefesto + Aurora + outros executores podem ler/escrever. Apollo só lê (orquestra, não modifica contratos).

### 14.2 Os 3 fluxos via Kanban

#### Caso 1 — Hefesto muda API existente

1. Hefesto edita `openapi-vN.yaml` (ou cria `v(N+1).yaml` se breaking)
2. Hefesto atualiza `_CHANGELOG.md` da pasta `api/` (data + summary + breaking? sim/não)
3. **SE breaking**: Hefesto cria card Kanban com `assignee="aurora"`, body apontando spec atualizada + lista de endpoints afetados
4. Aurora vê card → adapta frontend → fecha card
5. Após 30 dias do deprecated, Hefesto pode deletar versão antiga

**SE NÃO-breaking** (campo opcional novo, endpoint novo, etc): atualizar CHANGELOG mas card Kanban é OPCIONAL — Aurora descobre via leitura natural do contrato.

#### Caso 2 — Aurora precisa endpoint novo

1. Aurora cria card pro Hefesto com schema proposto (request/response esperados)
2. Hefesto avalia (workflow padrão FASE 0-3)
3. Hefesto implementa endpoint
4. Hefesto publica `openapi-vN.yaml` em `_shared/contracts/<projeto>/api/`
5. Hefesto atualiza `_CHANGELOG.md`
6. Hefesto fecha card → Aurora consome

#### Caso 3 — Aurora muda tokens que Hefesto consome (raro)

Tipicamente Aurora muda tokens sem afetar Hefesto. Mas se Hefesto consome tokens (ex: emails transacionais usando paleta de marca):

1. Aurora atualiza `tokens-vN.json` + `_CHANGELOG.md`
2. **SE Hefesto consome**: Aurora notifica via Kanban `assignee="hefesto"`
3. Hefesto adapta dependência

### 14.3 As 6 regras invioláveis

1. **Toda mudança em contrato compartilhado → atualizar `_CHANGELOG.md`** (data + summary + breaking? sim/não + autor)
2. **Breaking change → SEMPRE notificar via `kanban_create`** quem depende (Aurora primariamente)
3. **Não-breaking → atualização sem card obrigatório** (mas CHANGELOG é obrigatório)
4. **Versionamento por nome de arquivo** (`v1`, `v2`, `v3-deprecated`) — nunca sobrescrever
5. **Manter última versão deprecated por 30 dias** antes de deletar (rollback window)
6. **`README.md` do projeto contracts/ sempre atualizado** (status + versão atual + última mudança)

### 14.4 Formato `_CHANGELOG.md`

```markdown
# _CHANGELOG — <projeto> / api

## v2.1 — 2026-06-15
- Breaking: SIM (campo `user.email` virou obrigatório)
- Endpoints afetados: POST /users, PATCH /users/:id
- Migration guide: ver `handoff/task-0089-migration.md`
- Notificado Aurora: SIM (card #c142, 2026-06-15)

## v2.0 — 2026-06-01
- Breaking: NÃO (novo endpoint GET /users/:id/avatar)
- Notificado Aurora: NÃO (não-breaking)
```

### 14.5 Quando contrato compartilhado NÃO se aplica

- **Endpoints internos do backend** (não consumidos pelo frontend): ficam só no repo do Hefesto, sem `_shared/contracts/`
- **Tokens experimentais** (Aurora em rascunho `_drafts/`): não publica em `_shared/contracts/` até estabilizar
- **Specs efêmeras de spike**: usar `handoff/` mas marcar como `spike-` no nome (TTL 30d)

### 14.6 Integração com workflow Hefesto

Esse compliance encaixa nas fases padrão:

- **FASE 2 (Architecture)**: se feature envolve endpoint público (Aurora consome) → planejar spec OpenAPI desde já
- **FASE 4 (Implementation)**: implementar endpoint + gerar/atualizar spec antes do commit
- **FASE 5 (Testing & Review)**: verificar que CHANGELOG está atualizado + revisar diff da spec + **rodar Spectral linter** (`spectral lint _shared/contracts/<projeto>/api/openapi-vN.yaml`) — bloqueia se falhar
- **FASE 6 (Delivery)**: se breaking, criar card Kanban pra Aurora ANTES de fechar card próprio

### 14.7 Validação automática com Spectral

**Obrigatório** em qualquer publish de `openapi-vN.yaml` em `_shared/contracts/`:

```bash
# Pre-publish validation
spectral lint /srv/workspace/_shared/contracts/<projeto>/api/openapi-vN.yaml

# Com ruleset customizado (recomendado — combinar OAS + AWS + customizações Hermes)
spectral lint --ruleset .spectral.yml _shared/contracts/<projeto>/api/openapi-vN.yaml
```

**Se Spectral falha**: NÃO publicar spec. Corrigir + re-validar antes de notificar Aurora via Kanban.

**Ruleset sugerido** (criar em `_shared/contracts/.spectral.yml`):
- `spectral:oas` (OpenAPI 3.x rules)
- Custom: campos obrigatórios `summary` + `description` em endpoints
- Custom: bloquear endpoints sem `responses.401` ou `responses.403` se requer auth
- Custom: forçar versionamento explícito (`servers.url` deve conter `/v1` ou `/v2` etc)

---

**Fim do playbook.**

Hefesto consulta este arquivo durante execução. Atualizado conforme aprendizado e novas decisões arquiteturais.
