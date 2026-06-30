---
name: deepseek-architecture-decision
description: "DECISAO DE ARQUITETURA PESADISSIMA — 13 camadas, 20 criterios, codigo real, threat model, custo por request, rollback, DR. DeepSeek V4 Flash no talo. 1M de contexto."
model: zenmux/deepseek/deepseek-v4-flash-free
fallback: [zenmux/z-ai/glm-5.2-free, zenmux/moonshotai/kimi-k2.7-code-free]
user-invocable: true
allowed-tools: Read, Grep, Glob, Bash, Task, Write, Edit, WebSearch, WebFetch, CodeSearch
---

# 🏛️ DeepSeek Architecture Decision — PESADÍSSIMO

> Skill **ULTRA PREMIUM** — otimizada para **DeepSeek V4 Flash Free**
>
> Aproveita 100% dos pontos fortes do DeepSeek:
> - 🧠 1M tokens de contexto (lê o projeto INTEIRO)
> - 💻 Excelência em análise de código
> - 🔗 Raciocínio multidomínio (conecta backend, frontend, infra, dados)
> - 🆓 Grátis no ZenMux
>
> *"DeepSeek não é só um modelo. É co-arquiteto."*

---

## 📋 Ficha Técnica

| Especificação | Valor |
|---|---|
| **Modelo** | `zenmux/deepseek/deepseek-v4-flash-free` |
| **Contexto máximo** | 1.000.000 tokens |
| **Camadas de análise** | **13** |
| **Critérios na matriz** | **20** |
| **Cenários de stress** | **15** |
| **Artefatos gerados** | **8** |
| **Anti-padrões bloqueados** | **15** |
| **Níveis de efeitos** | 4 (1ª, 2ª, 3ª, 4ª ordem) |

---

## 🎯 Quando Usar

| Situação | Exemplo real |
|---|---|
| 🏢 **Sistema novo do zero** | "Vamos construir um SaaS de pagamentos" |
| 🔄 **Refatoração gigante** | "Monolito de 200K linhas → microsserviços" |
| 🚀 **Mudança de stack** | "Sair de Java legado pra Go/Rust" |
| ☁️ **Migração de cloud** | "On-prem → AWS/GCP/Azure" |
| 🗄️ **Mudança de banco** | "Postgres → CockroachDB ou DynamoDB?" |
| 🧱 **Arquitetura de dados** | "Data lake, stream processing, analytics" |
| 🔐 **Sistema crítico** | "Fintech, health, compliance pesado" |
| 🌐 **Multi-região** | "Expandir pra US/Europa com latency baixa" |

---

# 🧩 AS 13 CAMADAS

---

## 🔷 Layer 0 — Pre-Flight Check
*Antes de começar, DeepSeek verifica se dá pra decidir.*

**Checklist obrigatório** (se faltar >2 itens, a decisão é adiada):

- [ ] Problema de negócio claro e escrito
- [ ] Stakeholders identificados e disponíveis
- [ ] Budget estimado (construção + 3 anos de operação)
- [ ] Timeline conhecida (não ideal, a real)
- [ ] Time definido (quantos, senioridade, stack atual)
- [ ] Código fonte acessível (se for refatoração)
- [ ] Dados de volume (req/s, armazenamento, picos)
- [ ] SLAs definidos (latência, disponibilidade, RPO/RTO)
- [ ] Restrições de compliance conhecidas
- [ ] Decisão é reversível? (se sim, pode ser mais rápida)

> ✅ **Se tudo OK**: Avança para Layer 1
> ⚠️ **Se faltam dados**: DeepSeek gera um `PRE_FLIGHT_GAP.md` com o que buscar

---

## 🔷 Layer 1 — Context Capture Ultra-Profundo
*DeepSeek usa 1M de contexto para absorver TUDO.*

### 📂 O que DeepSeek lê automaticamente:
```
projeto/
├── README.md, ARCHITECTURE.md, CONTRIBUTING.md
├── docs/adr/*.md              → Decisões anteriores
├── docs/roadmap/*.md          → Roadmap existente
├── src/                       → Código fonte (amostra inteligente)
├── tests/                     → Padrões de teste, cobertura
├── docker-compose.yml         → Infra atual
├── package.json/go.mod/*.csproj  → Dependências
├── .env.example               → Serviços externos
└── infra/                     → Terraform, k8s, etc.
```

### 📋 DeepSeek extrai:
| Informação | Por que importa |
|---|---|
| Dívida técnica existente | Se já tem dívida, não adicionar mais |
| Padrões de código | A nova arquitetura precisa ser consistente |
| Dependências críticas | O que pode quebrar com a mudança |
| Cobertura de testes | Se é baixa, risco de refatoração é maior |
| Acoplamento real | Graph de dependências do código |
| Conway's Law atual | A estrutura do time reflete no código |
| Conhecimento implícito | O que NINGUÉM documentou mas todo mundo sabe |

**Output**: `CONTEXT_REPORT.md` — resumo de 1 página com o essencial

---

## 🔷 Layer 2 — Option Generation (5 Abordagens)
*DeepSeek gera 5 opções — não 3, não 4. CINCO.*

| Opção | Perfil | Risco | Inovação | Prazo | Custo |
|---|---|---|---|---|---|
| **A — Conservadora** | Stack conhecida, time domina | ⭐ Baixo | ⭐ Baixa | ⏱ Curto | 💰 Menor |
| **B — Balanceada** | Stack moderna + treinamento | ⭐⭐ Médio | ⭐⭐ Média | ⏱⏱ Médio | 💰💰 Médio |
| **C — Arrojada** | Tecnologia de ponta | ⭐⭐⭐ Alto | ⭐⭐⭐⭐ Alta | ⏱⏱⏱ Longo | 💰💰💰 Alto |
| **D — Híbrida** | Mistura estratégica | ⭐⭐~⭐⭐⭐ Variável | ⭐⭐⭐⭐ Máxima | ⏱⏱ Variável | 💰💰 Variável |
| **E — Evolucionária** 🏆 | Começa simples, evolui | ⭐ Baixo~Médio | ⭐⭐⭐ Alta (gradual) | ⏱⏱ Contínuo | 💰💰 Fracionado |

### Para CADA opção, DeepSeek entrega:

```
┌─────────────────────────────────────────┐
│  OPÇÃO [X] — [nome]                     │
├─────────────────────────────────────────┤
│ Stack:   [linguagem + framework + DB + infra + fila + cache] │
│ Time:    [n pessoas, senioridade]       │
│ Custo dev: [R$ estimado]                │
│ Custo cloud/ano: [R$ estimado]          │
│ Timeline: [sprints/meses]               │
│ Riscos técnicos: [lista]                │
│ Riscos de negócio: [lista]              │
│ Dívida técnica gerada: [baixa/média/alta] │
│ Esboço de código: [trecho real]         │
│ Dá pra voltar atrás?: [sim/parcial/não] │
│ Melhor para: [cenário ideal]            │
└─────────────────────────────────────────┘
```

---

## 🔷 Layer 3 — Mega Trade-off Matrix (20 Critérios)
*DeepSeek pondera CADA critério com evidência — sem chute.*

### 🏋️ Os 20 Critérios

| # | Critério | Peso | O que mede |
|---|----------|------|------------|
| 1 | **Performance (latência)** | 0.09 | p50/p95/p99, throughput por réplica |
| 2 | **Escalabilidade** | 0.08 | Suporta 10x sem reescrever? |
| 3 | **Manutenibilidade** | 0.08 | Novo dev entende em quanto tempo? |
| 4 | **Segurança** | 0.08 | OWASP Top 10, auth, crypto, audit |
| 5 | **Custo dev (construção)** | 0.07 | Horas-homem pra entregar |
| 6 | **Custo operacional (3 anos)** | 0.07 | Cloud + manutenção + oncall |
| 7 | **Time-to-market** | 0.06 | MVP em quanto tempo? |
| 8 | **Reversibilidade** | 0.06 | Custo e tempo de rollback |
| 9 | **Fit com o time** | 0.06 | Curva de aprendizado |
| 10 | **Observabilidade** | 0.05 | Logs, métricas, tracing nativos |
| 11 | **Testabilidade** | 0.05 | Mock, integração, chaos test |
| 12 | **Resiliência** | 0.04 | Circuit breaker, retry, fallback |
| 13 | **Maturidade do ecossistema** | 0.04 | Comunidade, libs, docs, contratação |
| 14 | **Qualidade de código** | 0.04 | Type safety, lint, padrões |
| 15 | **Inovação / aprendizado** | 0.03 | Diferencial competitivo, learning |
| 16 | **Lock-in / dependência** | 0.03 | Vendor lock-in, migração futura |
| 17 | **Disaster recovery** | 0.03 | RPO/RTO, multi-região, backup |
| 18 | **Elasticidade** | 0.02 | Sobe/desce automático? |
| 19 | **Compliance** | 0.02 | LGPD, PCI, SOC2, HIPAA |
| 20 | **Sustentabilidade (green)** | 0.01 | Eficiência energética, CO₂ |

**Fórmula**: `Score final = Σ(peso_i × nota_i) para i = 1 a 20`

DeepSeek **justifica cada nota** com trecho do contexto do projeto:
- Nota 8+ → "Há evidência de que X funciona em produção similar"
- Nota 5-7 → "Há risco conhecido, mas mitigável com Y"
- Nota <5 → "Há evidência de que X não se aplica a este caso"

---

## 🔷 Layer 4 — Code Feasibility Analysis 🔥
*Camada EXCLUSIVA DeepSeek — ninguém mais faz isso.*

> DeepSeek **lê o código real** do projeto e avalia a viabilidade técnica de cada opção.

### 🔬 DeepSeek analisa:

| Análise | Descrição | Ferramenta DeepSeek |
|---|---|---|
| **Graph de dependências** | Quem importa quem? Acoplamento real? | Lê imports, packages, modules |
| **Complexidade ciclomática** | Qual o custo real de modificar cada módulo? | Analisa funções, branches |
| **Padrões existentes** | A nova opção é compatível com o estilo do projeto? | Lê amostra de código |
| **Dívida técnica** | Se o código já tem problemas, a opção piora? | Analisa TODOs, FIXMEs, workarounds |
| **Testes existentes** | A opção permite testar do mesmo jeito? | Lê padrão de testes |
| **Dead code detection** | Tem código não usado que atrapalha a migração? | Varre imports não usados |
| **API surface** | O que precisa mudar nas interfaces? | Lê contratos públicos |

### 📄 Gera para cada opção:

```python
# CODE_FEASIBILITY_REPORT.md (exemplo)
## Opção B: Node + Fastify + PostgreSQL

✅ **Compatível**: 78% do código atual reaproveitável
⚠️ **Precisa refatorar**: Módulo de pagamentos (alto acoplamento)
❌ **Incompatível**: Fila atual (RabbitMQ → precisa de Kafka)
📦 **Novas dependências**: fastify, pino, @fastify/cors
🧪 **Testes**: 85% dos testes existentes funcionam sem mudança
📊 **Complexidade**: 3.2 (média) vs atual 4.7 (alta) — melhora
🔄 **Ordem de migração**: API → Repositórios → Domínio → Infra
```

---

## 🔷 Layer 5 — Database & Data Architecture
*DeepSeek modela a camada de dados com profundidade.*

### 🗄️ DeepSeek analisa:

1. **Modelo de dados**: Relacional, documento, gráfico, colunar?
2. **Padrão de acesso**: Reads vs writes, OLTP vs OLAP, queries complexas?
3. **Volume e crescimento**: Quantos GB hoje? Daqui 3 anos?
4. **Consistência**: ACID ou eventual? Transactions distribuídas?
5. **Migração de schema**: Zero-downtime possível? Versionamento?
6. **Backup & restore**: RPO/RTO realistas? Point-in-time recovery?
7. **Sharding**: Precisa? Chave de partição? Rebalanceamento?
8. **Caching**: Redis, CDN, cache local? Invalidação?
9. **Full-text search**: Elasticsearch, Meilisearch, pgvector?
10. **Streaming**: CDC, event sourcing, change data capture?

### 📄 Para cada opção:

```
┌─────────────────────────────────────────────┐
│  DATA ARCHITECTURE — Opção [X]              │
├─────────────────────────────────────────────┤
│ Banco primário:     [nome]                  │
│ Cache:              [nome + estratégia]     │
│ Search:             [nome se aplicável]      │
│ Fila/Stream:        [nome + padrão]         │
│ Migração:           [tool + estratégia]     │
│ Backup:             [ferramenta + RPO/RTO]  │
│ Consistência:       [ACID/eventual/misto]   │
│ Esquema de partição: [chave + algoritmo]    │
│ Custo estimado/mês:  [R$]                   │
└─────────────────────────────────────────────┘
```

---

## 🔷 Layer 6 — API & Integration Architecture
*DeepSeek define como os componentes conversam.*

### 🌐 DeepSeek especifica:

| Aspecto | O que define |
|---|---|
| **Protocolo** | REST, gRPC, GraphQL, WebSocket, eventos |
| **Contratos** | OpenAPI, Proto, Schema registry |
| **Autenticação** | JWT, mTLS, API keys, OAuth2 |
| **Rate limiting** | Global, por user, por endpoint |
| **Versionamento** | URL, header, contrato |
| **Gateway** | Kong, Envoy, Nginx, Cloudfront |
| **Service mesh** | Istio, Linkerd, ou sem mesh? |
| **Comunicação interna** | Síncrona vs assíncrona |
| **Eventos** | Event schema, dead letter, retry |
| **Idempotência** | Chave de idempotência, retry seguro |
| **Timeout/Circuit breaker** | Valores por serviço |

### DeepSeek gera para cada opção:

```
┌──────────────────────────────────────────────┐
│  API ARCHITECTURE — Opção [X]                │
├──────────────────────────────────────────────┤
│ Externo: REST (OpenAPI 3.1) + Rate limit     │
│ Interno: gRPC (bidirectional streaming)      │
│ Eventos: Kafka (+ schema registry)           │
│ Gateway: Kong (auth, rate limit, logging)    │
│ │
│ Exemplo de contrato:                         │
│   service PaymentService {                   │
│     rpc ProcessPayment(PaymentRequest)       │
│         returns (PaymentResponse);           │
│   }                                          │
│                                              │
│ Timeouts: payments 5s, reports 30s           │
│ Circuit breaker: 5 falhas em 10s → open 30s  │
└──────────────────────────────────────────────┘
```

---

## 🔷 Layer 7 — Security Threat Model (STRIDE)
*DeepSeek aplica STRIDE em cada componente.*

### 🛡️ STRIDE por componente

| Ameaça | O que verifica | Exemplo de risco |
|---|---|---|
| **S**poofing | Autenticação fraca | JWT sem assinatura |
| **T**ampering | Integridade dos dados | Request sem validação |
| **R**epudiation | Logs de auditoria | Sem trilha de quem fez o quê |
| **I**nformation Disclosure | Dados sensíveis expostos | PII no log |
| **D**enial of Service | Rate limit, recurso | Sem proteção de quota |
| **E**levation of Privilege | RBAC, permissões | User vira admin |

### 🔐 DeepSeek também analisa:

- **Secrets management**: Onde ficam senhas, tokens, chaves?
- **Dependências**: Bibliotecas com CVE conhecida?
- **Compliance**: LGPD, PCI-DSS, SOC2, HIPAA — quais se aplicam?
- **Audit trail**: Quem fez o quê, quando, de onde?
- **Input validation**: Sanitização, SQL injection, XSS, SSRF
- **Criptografia**: Em repouso? Em trânsito? Chaves rotacionadas?

### 📄 Gera:

```
┌──────────────────────────────────────────────┐
│  THREAT MODEL — Opção [X]                    │
├──────────────────────────────────────────────┤
│ 🔴 CRÍTICO: [ameaça+impacto+mitigação]      │
│ 🟡 ALTO:    [ameaça+impacto+mitigação]      │
│ 🟡 MÉDIO:   [ameaça+impacto+mitigação]      │
│ 🟢 BAIXO:   [ameaça+impacto+mitigação]      │
│                                              │
│ Compliance: [LGPD/PCI/SOC2 — status]        │
│ Secrets:    [ferramenta + onde]              │
│ CVEs:       [quantidade crítica/alta]        │
└──────────────────────────────────────────────┘
```

---

## 🔷 Layer 8 — Performance & Cost Budget
*DeepSeek calcula custo por request + infra.*

### ⚡ Performance budget

| Métrica | Alvo | Cálculo |
|---|---|---|
| **Latência p50** | < X ms | Teste de carga + histórico |
| **Latência p99** | < Y ms | Pior caso realistico |
| **Throughput** | Z req/s por réplica | Benchmark do framework |
| **Memória** | W MB por instância | Heap profiling |
| **CPU** | V% médio | Perfil de request |

### 💰 Cost budget (por opção)

```
┌──────────────────────────────────────────────┐
│  COST MODEL — Opção [X] (3 anos)            │
├──────────────────────────────────────────────┤
│ 💻 Desenvolvimento: R$ [valor]              │
│ ☁️ Cloud/mês:       R$ [valor]              │
│ ☁️ Cloud/ano:       R$ [valor]              │
│ 👥 Oncall/mês:      R$ [valor]              │
│ 🔧 Manutenção/ano:  R$ [valor]              │
│                                              │
│ Custo por request:   R$ [microvalor]        │
│ Break-even (mês):    [número]               │
│ TCO 3 anos:          R$ [valor total]       │
└──────────────────────────────────────────────┘
```

---

## 🔷 Layer 9 — Ops, Observability & Reliability
*DeepSeek projeta como operar o sistema no dia a dia.*

### 📊 Observabilidade

| Pilar | O que DeepSeek especifica |
|---|---|
| **Logs** | Estruturados (JSON), níveis, retention, ferramenta |
| **Métricas** | RED (Rate/Errors/Duration), USE (Utilization/Saturation/Errors) |
| **Tracing** | Distributed tracing (OpenTelemetry), sampling |
| **Alertas** | O que alertar? Quem alertar? Como alertar? |
| **Dashboards** | O que precisa estar visível sempre? |
| **SLO/SLI** | Objetivos de nível de serviço |

### 🚨 Oncall & Incident Response

- **Runbook**: O que fazer em cada cenário de fallha?
- **Escalação**: Quem é chamado em cada nível?
- **Pós-mortem**: Cultura de blameless?

### 📄 Output:

```
┌──────────────────────────────────────────────┐
│  OBSERVABILITY — Opção [X]                   │
├──────────────────────────────────────────────┤
│ Logs:     JSON → Graf Loki (30d retention)   │
│ Metrics:  Prometheus + Grafana (RED/USE)     │
│ Tracing:  OpenTelemetry (1% sampling)        │
│ Alerts:   PagerDuty (5 regras críticas)      │
│                                              │
│ SLO:  99.9% uptime / p99 < 500ms            │
│ Error budget: 0.1% = 43min/mês              │
└──────────────────────────────────────────────┘
```

---

## 🔷 Layer 10 — Disaster Recovery & Business Continuity
*DeepSeek planeja o pior cenário possível.*

### 🌍 DR Architecture

| Cenário | RPO | RTO | Estratégia |
|---|---|---|---|
| **Região cai** | [min] | [min] | Active-passive / Active-active |
| **Banco corrompe** | [min] | [min] | PITR + snapshot |
| **Dados deletados** | [min] | [min] | Backup + WAL archiving |
| **Ataque ransomware** | [h] | [h] | Air-gapped backup |

### 🔄 Para cada opção, DeepSeek avalia:

- **Multi-região**: Custo vs benefício
- **Backup strategy**: Full, incremental, WAL, frequência
- **Restore test**: Último teste de restore funcionou?
- **Chaos engineering**: Já testou matar um nó aleatório?
- **Dependency failure**: Se o provedor X cair, o que acontece?

---

## 🔷 Layer 11 — Stress Test (15 Cenários Extremos)
*DeepSeek submete a arquitetura a 15 provas de fogo.*

| # | Cenário | Impacto | Categoria |
|---|---|---|---|
| 1 | **Carga 10x do nada** | Black Friday, viral, DDOS | 🔴 Escala |
| 2 | **Time -3 seniors** | Saída de funcionários-chave | 🔴 Pessoas |
| 3 | **Custo de nuvem dobra** | Orçamento estoura | 🟡 Financeiro |
| 4 | **Concorrente lança igual** | Perde vantagem competitiva | 🟡 Mercado |
| 5 | **LGPD/PCI muda** | Compliance exige mudança | 🔴 Regulatório |
| 6 | **Provedor de cloud cai** | AWS us-east-1 fora por 4h | 🔴 Infra |
| 7 | **Dependência crítica morre** | Lib X abandonada, CVE crítica | 🔴 Técnico |
| 8 | **Timeout em cascata** | Serviço A espera B que espera C | 🔴 Resiliência |
| 9 | **Time cresce 10x** | 5 devs → 50, arquitetura escala? | 🟡 Organizacional |
| 10 | **Produto pivota 180°** | Negócio muda, stack serve? | 🟡 Negócio |
| 11 | **Ataque ransomware** | Dados criptografados | 🔴 Segurança |
| 12 | **Latência dobra** | Usuários reclamam, churn | 🟡 Experiência |
| 13 | **DB corrompe** | Precisamos de PITR funcional | 🔴 Dados |
| 14 | **VP de engenharia quer mudar** | Pressão política por stack X | 🟡 Político |
| 15 | **Orçamento cortado 50%** | Crise, time reduzido | 🔴 Financeiro |

### 📊 Classificação:

- ✅ **Resiste** — sem alterações
- ⚠️ **Mitigável** — com mudanças pontuais (descreve quais)
- ❌ **Quebra** — exige reescrita (descreve o custo)

---

## 🔷 Layer 12 — Multi-Order Effects (4 Níveis)
*DeepSeek enxerga além — 4 níveis de consequência.*

### 1ª Ordem (imediato)
| Ação | Reação direta |
|---|---|
| Mudar de linguagem | Tempo de aprendizado, produtividade cai |
| Adicionar Kafka | Complexidade operacional aumenta |
| Migrar para cloud | Capex vira opex |

### 2ª Ordem (3-6 meses)
- Opção **A** (conservadora) → Time produtivo rápido, mas inovação travada
- Opção **B** (balanceada) → Entrega no prazo, time motivado, dívida controlada
- Opção **C** (arrojada) → Diferencial competitivo, mas turnover por estresse
- Opção **D** (híbrida) → Complexidade de gerenciar stacks diferentes
- Opção **E** (evolucionária) → Menos dívida, mas requer disciplina de arquitetura

### 3ª Ordem (1-2 anos)
- **Talento**: Se escolher stack X, consegue contratar reposição?
- **Mercado**: Se tecnologia Y vira padrão, ficamos obsoletos ou na frente?
- **Dívida**: Se acumular dívida por 2 anos, quanto custa pagar?
- **Ecossistema**: Se a lib Z morrer, temos plano B?

### 4ª Ordem (3-5 anos)
- **Arquitetura**: Essa decisão permite a próxima evolução ou prende?
- **Cultura**: Que tipo de cultura de engenharia essa stack reforça?
- **Maturidade**: O time cresceu tecnicamente ou ficou dependente?
- **Valor**: O negócio se beneficiou ou a stack virou fim em si mesma?

---

## 🔷 Layer 13 — Risk-Weighted Decision & Veredito Final
*DeepSeek aplica correção de viés e entrega o veredito.*

### 🧮 Correção de Viés

| Tipo de viés | Ajuste | Quando |
|---|---|---|
| **Otimismo** | -15% | Opção favorita do time |
| **Familiaridade** | -10% | Stack que time já conhece |
| **Novidade** | -15% | Stack que ninguém domina |
| **Hype** | -20% | Tecnologia hypada no momento |
| **Ancoragem** | -10% | Primeira opção sugerida |

### 📊 Score final

```
┌──────────────────────────────────────────────┐
│  SCORE FINAL (após correção de viés)         │
├──────────────────────────────────────────────┤
│               Bruto   Viés   Final   Ranking  │
│  Opção A      7.8     -8%    7.2      🥈     │
│  Opção B      8.5     -5%    8.1      🥇 ←    │
│  Opção C      7.2     -18%   5.9      5º      │
│  Opção D      8.2     -12%   7.2      🥉     │
│  Opção E      8.0     -5%    7.6      4º      │
└──────────────────────────────────────────────┘
```

### 🏆 Veredito Final

```
┌──────────────────────────────────────────────┐
│           VEREDITO FINAL                      │
├──────────────────────────────────────────────┤
│                                               │
│  RECOMENDATION: Opção B — [nome]              │
│                                               │
│  RATIONALE (3 frases):                        │
│  1. Maior score após correção de viés (8.1)   │
│  2. Melhor relação risco/retorno para o time  │
│  3. Reversível em 3 meses se não funcionar    │
│                                               │
│  CODE FEASIBILITY: ✅ Viável                  │
│  SECURITY: 🟢 3 riscos baixos, 0 críticos    │
│  STRESS TEST: ✅ 12/15 passaram              │
│  COST: R$ [valor] TCO 3 anos                 │
│                                               │
│  PRE-COMMITMENT METRICS:                      │
│  • Latência p99 < 200ms até [data]            │
│  • Cobertura de testes > 80% até [data]       │
│  • Custo mensal < R$ [valor] até [data]       │
│                                               │
│  EXIT CRITERIA (abandonamos se):              │
│  • Latência p99 > 500ms após 1 mês de tuning  │
│  • Custo > 150% do budget por 2 meses         │
│  • 3+ incidentes críticos no primeiro mês     │
│                                               │
│  REVIEW DATE: [data] — reavaliar decisão      │
└──────────────────────────────────────────────┘
```

---

## 🔷 Layer Extra — Implementation Roadmap (Completo)
*DeepSeek não só decide — ele mostra o caminho com código.*

### 🗺️ Roadmap por fase

```
📅 FASE 1 — Fundação (Sprints 1-2)
   ├── Setup do projeto + CI/CD
   ├── Modelos de dados + migrations
   ├── 3 endpoints críticos funcionando
   └── ✅ Marco: "Hello world" em produção

📅 FASE 2 — Core (Sprints 3-6)
   ├── 80% dos endpoints implementados
   ├── Autenticação + autorização
   ├── Testes de integração
   └── ✅ Marco: Feature completa em staging

📅 FASE 3 — Resiliência (Sprints 7-8)
   ├── Circuit breaker + retry + timeout
   ├── Observabilidade (logs, métricas, tracing)
   ├── Alertas + dashboards
   └── ✅ Marco: SLO 99.9% por 1 semana

📅 FASE 4 — Escala (Sprints 9-10)
   ├── Load testing + tuning
   ├── Cache + CDN
   ├── Auto-scaling configurado
   └── ✅ Marco: Suporta 10x sem degradação

📅 FASE 5 — Migração (se aplicável)
   ├── Modo paralelo (nova + antiga)
   ├── Shadow reads
   ├── Cutover planejado
   ├── Rollback testado
   └── ✅ Marco: 100% do tráfego na nova
```

### 🔙 Plano de Rollback

| Fase | Ponto de não-retorno | Como voltar | Custo |
|---|---|---|---|
| Fase 1 | Sprint 3 | `git revert` + redeploy | 2 dias |
| Fase 2 | Sprint 6 | Feature flag desliga | 1 dia |
| Fase 3 | Sprint 8 | DNS aponta pro antigo | 4h |
| Fase 4 | Sprint 10 | Reduz réplicas | 2h |
| Migração | Cutover+1h | DNS revert | 30min |

---

## 🚫 15 Anti-Patterns Bloqueados
*DeepSeek identifica e BLOQUEIA na hora.*

| # | Anti-Pattern | DeepSeek Detection |
|---|---|---|
| 🚫 | **"Vai na hype"** | "Essa tecnologia resolve SEU problema ou o problema dos outros?" |
| 🚫 | **"Sempre fizemos assim"** | "A zona de conforto é onde a inovação morre. Sugiro 3 alternativas." |
| 🚫 | **"Não temos tempo"** | "Não ter tempo é o MAIOR risco. Vou fazer a análise em 1h." |
| 🚫 | **1 opção só** | "Decisão sem alternativa é dogma. Gere no mínimo 3." |
| 🚫 | **Decisão adiada** | "Adiar é decidir por padrão. Defina data-limite." |
| 🚫 | **Ignorar reversibilidade** | "Toda decisão deve ter custo de rollback conhecido." |
| 🚫 | **Time não consultado** | "Quem implementa precisa ser ouvido." |
| 🚫 | **Stack única pra tudo** | "One-size-fits-all raramente funciona." |
| 🚫 | **"Depois refatora"** | "Refatoração postergada é dívida eterna." |
| 🚫 | **Ignorar observabilidade** | "Se não dá pra medir, não dá pra operar." |
| 🚫 | **Superestimar time** | "Heróis não escalam. Planilhe com folga." |
| 🚫 | **Subestimar dados** | "Dados sempre crescem mais que o esperado." |
| 🚫 | **Ignorar segurança** | "Segurança no final sai mais caro." |
| 🚫 | **Plano sem rollback** | "Se não tem volta, não é decisão — é aposta." |
| 🚫 | **Decisão sem data de revisão** | "Toda decisão técnica tem prazo de validade." |

---

## 📦 Artefatos Gerados

DeepSeek gera **8 artefatos** completos ao final:

```
📁 docs/
├── adr/
│   ├── YYYY-MM-DD-<topic>-decision.md      → Decisão principal
│   ├── YYYY-MM-DD-<topic>-code-report.md   → Análise de código
│   ├── YYYY-MM-DD-<topic>-threat-model.md  → Modelo de ameaças
│   └── YYYY-MM-DD-<topic>-data-arch.md     → Arquitetura de dados
│
├── roadmap/
│   └── YYYY-MM-DD-<topic>-implementation.md → Roadmap completo
│
├── cost/
│   └── YYYY-MM-DD-<topic>-tco.md           → Modelo de custo 3 anos
│
└── decisions/
    ├── README.md                             → Índice de decisões
    └── YYYY-MM-DD-<topic>-review.md         → Data de revisão futura
```

---

## 📊 Comparativo: Original vs DeepSeek Pesadíssimo

| Aspecto | Original (complex) | **DeepSeek Pesadíssimo** |
|---|---|---|
| **Camadas** | 7 | **13 + extra** |
| **Critérios** | 7 | **20** |
| **Opções** | 3 | **5** |
| **Stress tests** | 5 | **15** |
| **Anti-patterns** | 6 | **15** |
| **Efeitos** | 2ª ordem | **Até 4ª ordem** |
| **Código real** | ❌ | ✅ **Lê e analisa o projeto** |
| **Threat model** | ❌ | ✅ **STRIDE completo** |
| **Cost model** | ❌ | ✅ **Custo por request + TCO 3 anos** |
| **Rollback plan** | ❌ | ✅ **Faseado + custo** |
| **DR/Business continuity** | ❌ | ✅ |
| **Observabilidade** | ❌ | ✅ **RED + USE + SLO/SLI** |
| **Performance budget** | ❌ | ✅ |
| **Correção de viés** | ❌ | ✅ **5 tipos de viés** |
| **Artefatos** | 1 ADR | **8 artefatos** |
| **Roadmap** | ❌ | ✅ **5 fases + rollback** |
| **Modelo** | Opus 4.8 (pago) | **DeepSeek V4 Flash (grátis)** |
| **Contexto** | 200K | **1M tokens** |

---

## 🧬 DeepSeek Advantage — Por que ele?

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│   DeepSeek V4 Flash Free × ZenMux                      │
│                                                         │
│   ✅ 1M de contexto → Lê o PROJETO INTEIRO              │
│   ✅ Grátis → Pode usar sem medo                        │
│   ✅ Raciocínio profundo → Análise multicamada           │
│   ✅ Excelente em código → Gera esboços reais            │
│   ✅ Pensamento lateral → Conecta domínios distintos      │
│                                                         │
│   O ÚNICO modelo grátis que faz análise de arquitetura   │
│   com esse nível de profundidade.                        │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

> *"Arquitetura não é sobre acertar de primeira. É sobre entender as consequências de cada escolha antes de fazê-la."*
> — DeepSeek Architecture Decision Skill
