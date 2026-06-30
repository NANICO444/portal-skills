---
name: glm-architecture-decision
description: "DECISAO DE ARQUITETURA PESADISSIMA — 15 camadas, 25 criterios, 6 opcoes, 20 stress tests, 20 anti-patterns, 5 niveis de efeitos. Otimizada para GLM 5.2 (1M contexto). Versao GLM da deepseek-architecture-decision, ainda mais pesada."
model: zenmux/z-ai/glm-5.2-free
fallback: [zenmux/deepseek/deepseek-v4-flash-free, zenmux/moonshotai/kimi-k2.7-code-free]
user-invocable: true
allowed-tools: Read, Grep, Glob, Bash, Task, Write, Edit, WebSearch, WebFetch, CodeSearch
---

# 🏛️ GLM Architecture Decision — PESADÍSSIMO MAX

> Skill **ULTRA PREMIUM MAX** — otimizada para **Z.AI GLM 5.2 Free**
>
> Versão GLM da `deepseek-architecture-decision`, porém **mais pesada**:
> - 🧠 1M tokens de contexto (lê o projeto INTEIRO + dependências)
> - 📊 15 camadas de análise (vs 13)
> - 🎯 25 critérios na matriz (vs 20)
> - 🔀 6 opções geradas (vs 5)
> - 🔥 20 stress tests (vs 15)
> - 🚫 20 anti-patterns bloqueados (vs 15)
> - 🌊 5 níveis de efeitos (vs 4)
> - 🆓 Grátis no ZenMux
>
> *"GLM não decide por você. Ele mapeia todas as consequências para que você decida com olhos abertos."*

---

## 📋 Ficha Técnica

| Especificação | Valor |
|---|---|
| **Modelo** | `zenmux/z-ai/glm-5.2-free` |
| **Contexto máximo** | 1.000.000 tokens |
| **Camadas de análise** | **15** |
| **Critérios na matriz** | **25** |
| **Opções geradas** | **6** |
| **Cenários de stress** | **20** |
| **Artefatos gerados** | **10** |
| **Anti-padrões bloqueados** | **20** |
| **Níveis de efeitos** | 5 (1ª, 2ª, 3ª, 4ª, 5ª ordem) |
| **Bias corrigidos** | 7 tipos |

---

## 🎯 Quando Usar

| Situação | Exemplo real |
|---|---|
| 🏢 **Sistema novo do zero** | "Vamos construir um SaaS de pagamentos" |
| 🔄 **Refatoração gigante** | "Monolito de 500K linhas → microsserviços" |
| 🚀 **Mudança de stack** | "Sair de Java legado pra Go/Rust" |
| ☁️ **Migração de cloud** | "On-prem → AWS/GCP/Azure" |
| 🗄️ **Mudança de banco** | "Postgres → CockroachDB ou DynamoDB?" |
| 🧱 **Arquitetura de dados** | "Data lake, stream processing, analytics" |
| 🔐 **Sistema crítico** | "Fintech, health, compliance pesado" |
| 🌐 **Multi-região** | "Expandir pra US/Europa com latency baixa" |
| 🤖 **Sistema de IA/ML** | "LLM em produção, RAG, agents" |
| ⚡ **Real-time pesado** | "Streaming, IoT, milhões de eventos/s" |

---

# 🧩 AS 15 CAMADAS

---

## 🔷 Layer 0 — Pre-Flight Check (Rigorado)

> *Antes de começar, GLM verifica CUIDADOSAMENTE se dá pra decidir.*

**Checklist obrigatório** (se faltar >2 itens, a decisão é adiada):

- [ ] Problema de negócio claro e escrito
- [ ] Stakeholders identificados e disponíveis
- [ ] Budget estimado (construção + 5 anos de operação)
- [ ] Timeline conhecida (não ideal, a real)
- [ ] Time definido (quantos, senioridade, stack atual)
- [ ] Código fonte acessível (se for refatoração)
- [ ] Dados de volume (req/s, armazenamento, picos)
- [ ] SLAs definidos (latência, disponibilidade, RPO/RTO)
- [ ] Restrições de compliance conhecidas
- [ ] Decisão é reversível? (se sim, pode ser mais rápida)
- [ ] Custo de NÃO decidir estimado
- [ ] Consequências de saída (exit strategy) definidas

> ✅ **Se tudo OK**: Avança para Layer 1
> ⚠️ **Se faltam dados**: GLM gera um `PRE_FLIGHT_GAP.md` com o que buscar

---

## 🔷 Layer 1 — Context Capture Ultra-Profundo MAX

> *GLM usa 1M de contexto para absorver TUDO — inclusive dependências externas.*

### 📂 O que GLM lê automaticamente:

```
projeto/
├── README.md, ARCHITECTURE.md, CONTRIBUTING.md, ADRs
├── docs/adr/*.md              → Decisões anteriores
├── docs/roadmap/*.md          → Roadmap existente
├── src/                       → Código fonte (amostra inteligente)
├── tests/                     → Padrões de teste, cobertura
├── docker-compose.yml         → Infra atual
├── package.json/go.mod/*.csproj  → Dependências
├── .env.example               → Serviços externos
├── infra/                     → Terraform, k8s, etc.
├── .github/workflows/         → CI/CD atual
└── node_modules/vendor/       → Amostra de libs reais usadas
```

### 📋 GLM extrai:

| Informação | Por que importa |
|---|---|
| Dívida técnica existente | Se já tem dívida, não adicionar mais |
| Padrões de código | A nova arquitetura precisa ser consistente |
| Dependências críticas | O que pode quebrar com a mudança |
| Cobertura de testes | Se é baixa, risco de refatoração é maior |
| Acoplamento real | Graph de dependências do código |
| Conway's Law atual | A estrutura do time reflete no código |
| Conhecimento implícito | O que NINGUÉM documentou mas todo mundo sabe |
| Histórico de incidentes | O que já pegou fogo antes |
| Padrões de deploy | Frequência, rollback, golden path |
| Cultura de teste | TDD? Test-after? Sem teste? |

**Output**: `CONTEXT_REPORT.md` — resumo de 1 página com o essencial

---

## 🔷 Layer 2 — Option Generation (6 Abordagens)

> *GLM gera 6 opções — não 3, não 5. SEIS.*

| Opção | Perfil | Risco | Inovação | Prazo | Custo |
|---|---|---|---|---|---|
| **A — Conservadora** | Stack conhecida, time domina | ⭐ Baixo | ⭐ Baixa | ⏱ Curto | 💰 Menor |
| **B — Balanceada** | Stack moderna + treinamento | ⭐⭐ Médio | ⭐⭐ Média | ⏱⏱ Médio | 💰💰 Médio |
| **C — Arrojada** | Tecnologia de ponta | ⭐⭐⭐ Alto | ⭐⭐⭐⭐ Alta | ⏱⏱⏱ Longo | 💰💰💰 Alto |
| **D — Híbrida** | Mistura estratégica | ⭐⭐~⭐⭐⭐ Variável | ⭐⭐⭐⭐ Máxima | ⏱⏱ Variável | 💰💰 Variável |
| **E — Evolucionária** 🏆 | Começa simples, evolui | ⭐ Baixo~Médio | ⭐⭐⭐ Alta (gradual) | ⏱⏱ Contínuo | 💰💰 Fracionado |
| **F — Anti-frágil** 🛡️ | Feita pra crescer com caos | ⭐⭐ Médio | ⭐⭐⭐⭐⭐ Máxima | ⏱⏱⏱ Longo | 💰💰💰 Alto |

### Para CADA opção, GLM entrega:

```
┌─────────────────────────────────────────────┐
│  OPÇÃO [X] — [nome]                          │
├─────────────────────────────────────────────┤
│ Stack:   [linguagem + framework + DB + infra]│
│ Time:    [n pessoas, senioridade]            │
│ Custo dev: [R$ estimado]                     │
│ Custo cloud/ano: [R$ estimado]               │
│ Timeline: [sprints/meses]                    │
│ Riscos técnicos: [lista]                     │
│ Riscos de negócio: [lista]                   │
│ Dívida técnica gerada: [baixa/média/alta]    │
│ Esboço de código: [trecho real]              │
│ Dá pra voltar atrás?: [sim/parcial/não]      │
│ Melhor para: [cenário ideal]                 │
│ Pior para: [cenário em que falha]            │
│ Maturidade: [produtivo/staging/experimental] │
└─────────────────────────────────────────────┘
```

---

## 🔷 Layer 3 — Mega Trade-off Matrix (25 Critérios)

> *GLM pondera CADA critério com evidência — sem chute.*

### 🏋️ Os 25 Critérios

| # | Critério | Peso | O que mede |
|---|----------|------|------------|
| 1 | **Performance (latência)** | 0.08 | p50/p95/p99, throughput por réplica |
| 2 | **Escalabilidade** | 0.07 | Suporta 10x sem reescrever? |
| 3 | **Manutenibilidade** | 0.07 | Novo dev entende em quanto tempo? |
| 4 | **Segurança** | 0.07 | OWASP Top 10, auth, crypto, audit |
| 5 | **Custo dev (construção)** | 0.06 | Horas-homem pra entregar |
| 6 | **Custo operacional (5 anos)** | 0.06 | Cloud + manutenção + oncall |
| 7 | **Time-to-market** | 0.05 | MVP em quanto tempo? |
| 8 | **Reversibilidade** | 0.05 | Custo e tempo de rollback |
| 9 | **Fit com o time** | 0.05 | Curva de aprendizado |
| 10 | **Observabilidade** | 0.05 | Logs, métricas, tracing nativos |
| 11 | **Testabilidade** | 0.04 | Mock, integração, chaos test |
| 12 | **Resiliência** | 0.04 | Circuit breaker, retry, fallback |
| 13 | **Maturidade do ecossistema** | 0.04 | Comunidade, libs, docs, contratação |
| 14 | **Qualidade de código** | 0.04 | Type safety, lint, padrões |
| 15 | **Inovação / aprendizado** | 0.03 | Diferencial competitivo, learning |
| 16 | **Lock-in / dependência** | 0.03 | Vendor lock-in, migração futura |
| 17 | **Disaster recovery** | 0.03 | RPO/RTO, multi-região, backup |
| 18 | **Elasticidade** | 0.02 | Sobe/desce automático? |
| 19 | **Compliance** | 0.02 | LGPD, PCI, SOC2, HIPAA |
| 20 | **Sustentabilidade (green)** | 0.01 | Eficiência energética, CO₂ |
| 21 | **Documentação** | 0.02 | Qualidade da doc oficial |
| 22 | **Comunidade** | 0.02 | Stack Overflow, Discord, GitHub |
| 23 | **Futuro da tecnologia** | 0.02 | Tendência de adoção, roadmap |
| 24 | **Debugabilidade** | 0.03 | Facilidade de achar bugs |
| 25 | **Onboarding de dev** | 0.02 | Tempo até primeiro PR aceito |

**Fórmula**: `Score final = Σ(peso_i × nota_i) para i = 1 a 25`

GLM **justifica cada nota** com trecho do contexto do projeto:
- Nota 8+ → "Há evidência de que X funciona em produção similar"
- Nota 5-7 → "Há risco conhecido, mas mitigável com Y"
- Nota <5 → "Há evidência de que X não se aplica a este caso"

---

## 🔷 Layer 4 — Code Feasibility Analysis 🔥

> *Camada EXCLUSIVA — GLM lê o código real e avalia viabilidade técnica.*

### 🔬 GLM analisa:

| Análise | Descrição |
|---|---|
| **Graph de dependências** | Quem importa quem? Acoplamento real? |
| **Complexidade ciclomática** | Custo real de modificar cada módulo? |
| **Padrões existentes** | A opção é compatível com o estilo do projeto? |
| **Dívida técnica** | Se o código já tem problemas, a opção piora? |
| **Testes existentes** | A opção permite testar do mesmo jeito? |
| **Dead code detection** | Tem código não usado que atrapalha a migração? |
| **API surface** | O que precisa mudar nas interfaces? |
| **Hot paths** | Quais trechos são críticos de performance? |
| **Mutation testing** | Os testes realmente pegam bugs? |

### 📄 Gera para cada opção:

```python
# CODE_FEASIBILITY_REPORT.md
## Opção B: Node + Fastify + PostgreSQL

✅ **Compatível**: 78% do código atual reaproveitável
⚠️ **Precisa refatorar**: Módulo de pagamentos (alto acoplamento)
❌ **Incompatível**: Fila atual (RabbitMQ → precisa de Kafka)
📦 **Novas dependências**: fastify, pino, @fastify/cors
🧪 **Testes**: 85% dos testes existentes funcionam sem mudança
📊 **Complexidade**: 3.2 (média) vs atual 4.7 (alta) — melhora
🔄 **Ordem de migração**: API → Repositórios → Domínio → Infra
⚡ **Hot paths**: 3 endpoints críticos precisam de cache
```

---

## 🔷 Layer 5 — Database & Data Architecture

> *GLM modela a camada de dados com profundidade.*

### 🗄️ GLM analisa:

1. **Modelo de dados**: Relacional, documento, gráfico, colunar?
2. **Padrão de acesso**: Reads vs writes, OLTP vs OLAP?
3. **Volume e crescimento**: Quantos GB hoje? Daqui 5 anos?
4. **Consistência**: ACID ou eventual? Transactions distribuídas?
5. **Migração de schema**: Zero-downtime possível? Versionamento?
6. **Backup & restore**: RPO/RTO realistas? PITR?
7. **Sharding**: Precisa? Chave de partição? Rebalanceamento?
8. **Caching**: Redis, CDN, cache local? Invalidação?
9. **Full-text search**: Elasticsearch, Meilisearch, pgvector?
10. **Streaming**: CDC, event sourcing, change data capture?
11. **Data governance**: Linage, catálogo, qualidade de dado?
12. **Privacy by design**: Anonimização, pseudonimização?

### 📄 Para cada opção:

```
┌─────────────────────────────────────────────┐
│  DATA ARCHITECTURE — Opção [X]              │
├─────────────────────────────────────────────┤
│ Banco primário:     [nome]                  │
│ Cache:              [nome + estratégia]     │
│ Search:             [nome se aplicável]     │
│ Fila/Stream:        [nome + padrão]         │
│ Migração:           [tool + estratégia]     │
│ Backup:             [ferramenta + RPO/RTO]  │
│ Consistência:       [ACID/eventual/misto]   │
│ Esquema de partição:[chave + algoritmo]     │
│ Custo estimado/mês: [R$]                    │
│ Data governance:    [sim/não + ferramenta]  │
└─────────────────────────────────────────────┘
```

---

## 🔷 Layer 6 — API & Integration Architecture

> *GLM define como os componentes conversam.*

### 🌐 GLM especifica:

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
| **API versioning** | Breaking change policy |

---

## 🔷 Layer 7 — Security Threat Model (STRIDE + LINDDUN)

> *GLM aplica STRIDE + LINDDUN (privacy) em cada componente.*

### 🛡️ STRIDE por componente

| Ameaça | O que verifica |
|---|---|
| **S**poofing | Autenticação fraca |
| **T**ampering | Integridade dos dados |
| **R**epudiation | Logs de auditoria |
| **I**nformation Disclosure | Dados sensíveis expostos |
| **D**enial of Service | Rate limit, recurso |
| **E**levation of Privilege | RBAC, permissões |

### 🔐 LINDDUN (Privacy)

| Ameaça | O que verifica |
|---|---|
| **L**inkability | Dados podem ser correlacionados? |
| **I**dentifiability | Usuário identificável? |
| **N**on-repudiation | Negar ação? |
| **D**etectability | Presença detectável? |
| **D**isclosure of info | Informação vazada? |
| **U**nawareness | Usuário sabe o que coletamos? |
| **N**on-compliance | LGPD/GDPR? |

### 🔐 GLM também analisa:

- **Secrets management**: Onde ficam senhas, tokens, chaves?
- **Supply chain security**: SBOM, SLSA, signed artifacts?
- **Dependências**: Bibliotecas com CVE conhecida?
- **Compliance**: LGPD, PCI-DSS, SOC2, HIPAA — quais se aplicam?
- **Audit trail**: Quem fez o quê, quando, de onde?
- **Zero Trust**: Cada request autenticada?

---

## 🔷 Layer 8 — Performance & Cost Budget (5 anos)

> *GLM calcula custo por request + infra em horizonte de 5 anos.*

### ⚡ Performance budget

| Métrica | Alvo |
|---|---|
| **Latência p50** | < X ms |
| **Latência p99** | < Y ms |
| **Throughput** | Z req/s por réplica |
| **Memória** | W MB por instância |
| **CPU** | V% médio |

### 💰 Cost budget (5 anos)

```
┌──────────────────────────────────────────────┐
│  COST MODEL — Opção [X] (5 anos)            │
├──────────────────────────────────────────────┤
│ 💻 Desenvolvimento: R$ [valor]              │
│ ☁️ Cloud/mês:       R$ [valor]              │
│ ☁️ Cloud/ano:       R$ [valor]              │
│ ☁️ Cloud/5 anos:    R$ [valor]              │
│ 👥 Oncall/mês:      R$ [valor]              │
│ 🔧 Manutenção/ano:  R$ [valor]              │
│ 📈 Escalada (3x):   R$ [valor]              │
│                                              │
│ Custo por request:   R$ [microvalor]        │
│ Break-even (mês):    [número]               │
│ TCO 5 anos:          R$ [valor total]       │
│ Custo por usuário:   R$ [valor]             │
└──────────────────────────────────────────────┘
```

---

## 🔷 Layer 9 — Ops, Observability & Reliability

> *GLM projeta como operar o sistema no dia a dia.*

### 📊 Observabilidade (3 pilares + 1)

| Pilar | O que GLM especifica |
|---|---|
| **Logs** | Estruturados (JSON), níveis, retention |
| **Métricas** | RED (Rate/Errors/Duration), USE |
| **Tracing** | Distributed tracing (OpenTelemetry) |
| **Profiles** | Continuous profiling (Pyroscope, pprof) |

### 🚨 Oncall & Incident Response

- **Runbook**: O que fazer em cada cenário de falha?
- **Escalação**: Quem é chamado em cada nível?
- **Pós-mortem**: Cultura de blameless?
- **Chaos engineering**: Game days programados?

### 📄 Output:

```
┌──────────────────────────────────────────────┐
│  OBSERVABILITY — Opção [X]                   │
├──────────────────────────────────────────────┤
│ Logs:     JSON → Graf Loki (30d retention)   │
│ Metrics:  Prometheus + Grafana (RED/USE)     │
│ Tracing:  OpenTelemetry (1% sampling)        │
│ Profiles: Pyroscope (continuous)             │
│ Alerts:   PagerDuty (5 regras críticas)      │
│                                              │
│ SLO:  99.9% uptime / p99 < 500ms            │
│ Error budget: 0.1% = 43min/mês              │
│ Chaos: Game day trimestral                   │
└──────────────────────────────────────────────┘
```

---

## 🔷 Layer 10 — Disaster Recovery & Business Continuity

> *GLM planeja o pior cenário possível — multi-cenário.*

### 🌍 DR Architecture

| Cenário | RPO | RTO | Estratégia |
|---|---|---|---|
| **Região cai** | [min] | [min] | Active-passive / Active-active |
| **Banco corrompe** | [min] | [min] | PITR + snapshot |
| **Dados deletados** | [min] | [min] | Backup + WAL archiving |
| **Ataque ransomware** | [h] | [h] | Air-gapped backup |
| **Provedor falência** | [h] | [h] | Multi-cloud |
| **Bug destrói dados** | [min] | [min] | PITR + testes |
| **Config ruim em prod** | [min] | [min] | Git revert + redeploy |

### 🔄 Para cada opção, GLM avalia:

- **Multi-região**: Custo vs benefício
- **Backup strategy**: Full, incremental, WAL, frequência
- **Restore test**: Último teste de restore funcionou?
- **Chaos engineering**: Já testou matar um nó aleatório?
- **Dependency failure**: Se o provedor X cair, o que acontece?
- **Tabletop exercise**: Simulação de desastre feita?

---

## 🔷 Layer 11 — Stress Test (20 Cenários Extremos)

> *GLM submete a arquitetura a 20 provas de fogo.*

| # | Cenário | Impacto | Categoria |
|---|---|---|---|
| 1 | **Carga 10x do nada** | Black Friday, viral, DDOS | 🔴 Escala |
| 2 | **Carga 100x do nada** | Mega viral, ataque | 🔴 Escala |
| 3 | **Time -3 seniors** | Saída de funcionários-chave | 🔴 Pessoas |
| 4 | **Custo de nuvem dobra** | Orçamento estoura | 🟡 Financeiro |
| 5 | **Concorrente lança igual** | Perde vantagem competitiva | 🟡 Mercado |
| 6 | **LGPD/PCI muda** | Compliance exige mudança | 🔴 Regulatório |
| 7 | **Provedor de cloud cai** | AWS us-east-1 fora por 4h | 🔴 Infra |
| 8 | **Dependência crítica morre** | Lib X abandonada, CVE crítica | 🔴 Técnico |
| 9 | **Timeout em cascata** | Serviço A espera B que espera C | 🔴 Resiliência |
| 10 | **Time cresce 10x** | 5 devs → 50, arquitetura escala? | 🟡 Organizacional |
| 11 | **Produto pivota 180°** | Negócio muda, stack serve? | 🟡 Negócio |
| 12 | **Ataque ransomware** | Dados criptografados | 🔴 Segurança |
| 13 | **Latência dobra** | Usuários reclamam, churn | 🟡 Experiência |
| 14 | **DB corrompe** | Precisamos de PITR funcional | 🔴 Dados |
| 15 | **VP de engenharia quer mudar** | Pressão política por stack X | 🟡 Político |
| 16 | **Orçamento cortado 50%** | Crise, time reduzido | 🔴 Financeiro |
| 17 | **Vazamento de dados** | Brecha, multa LGPD | 🔴 Segurança |
| 18 | **Supply chain attack** | Lib comprometida | 🔴 Segurança |
| 19 | **AI/LLM shutdown** | Provedor de IA fecha | 🟡 Dependência |
| 20 | **Guerra/regulamentação geo** | Bloqueio regional | 🟡 Geo |

### 📊 Classificação:

- ✅ **Resiste** — sem alterações
- ⚠️ **Mitigável** — com mudanças pontuais (descreve quais)
- ❌ **Quebra** — exige reescrita (descreve o custo)

---

## 🔷 Layer 12 — Multi-Order Effects (5 Níveis)

> *GLM enxerga além — 5 níveis de consequência.*

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
- Opção **E** (evolucionária) → Menos dívida, mas requer disciplina
- Opção **F** (anti-frágil) → Cresce com falhas, mas setup complexo

### 3ª Ordem (1-2 anos)
- **Talento**: Se escolher stack X, consegue contratar reposição?
- **Mercado**: Se tecnologia Y vira padrão, ficamos obsoletos?
- **Dívida**: Se acumular dívida, quanto custa pagar?
- **Ecossistema**: Se a lib Z morrer, temos plano B?

### 4ª Ordem (3-5 anos)
- **Arquitetura**: Essa decisão permite a próxima evolução ou prende?
- **Cultura**: Que tipo de cultura essa stack reforça?
- **Maturidade**: O time cresceu tecnicamente ou ficou dependente?
- **Valor**: O negócio se beneficiou ou a stack virou fim em si?

### 5ª Ordem (5-10 anos) 🆕
- **Legado**: Essa decisão vira o próximo "sistema legado" a ser migrado?
- **Reputação técnica**: A empresa vira referência ou "lugar com stack ruim"?
- **Sustentabilidade**: O sistema consome recursos do planeta de forma responsável?
- **Evolução da IA**: Como LLMs/agents mudam a relevância dessa stack?

---

## 🔷 Layer 13 — Team & Organizational Fit (Conway's Law)

> *GLM avalia o encaixe com a organização real.*

### 👥 GLM analisa:

- **Conway's Law**: A arquitetura reflete a estrutura de comunicação do time?
- **Reverse Conway**: Precisamos reorganizar o time para a arquitetura?
- **Skill gap**: Quanto treinamento é necessário?
- **Hiring market**: Dá pra contratar gente com essa stack?
- **Team morale**: O time vai amar ou odiar essa stack?
- **Bus factor**: Se 1 pessoa sair, o sistema para?
- **Cognitive load**: Quanto o time consegue absorver?

---

## 🔷 Layer 14 — Risk-Weighted Decision & Veredito Final

> *GLM aplica correção de viés e entrega o veredito.*

### 🧮 Correção de Viés (7 tipos)

| Tipo de viés | Ajuste | Quando |
|---|---|---|
| **Otimismo** | -15% | Opção favorita do time |
| **Familiaridade** | -10% | Stack que time já conhece |
| **Novidade** | -15% | Stack que ninguém domina |
| **Hype** | -20% | Tecnologia hypada no momento |
| **Ancoragem** | -10% | Primeira opção sugerida |
| **Sunk cost** | -15% | Já investimos em X |
| **Authority** | -10% | Especialista influente sugeriu |

### 📊 Score final

```
┌──────────────────────────────────────────────┐
│  SCORE FINAL (após correção de viés)         │
├──────────────────────────────────────────────┤
│               Bruto   Viés   Final   Ranking  │
│  Opção A      7.8     -8%    7.2      🥉     │
│  Opção B      8.5     -5%    8.1      🥇 ←    │
│  Opção C      7.2     -18%   5.9      6º      │
│  Opção D      8.2     -12%   7.2      4º      │
│  Opção E      8.0     -5%    7.6      🥈     │
│  Opção F      8.3     -10%   7.5      5º      │
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
│  PRIVACY: 🟢 LGPD compliant                   │
│  STRESS TEST: ✅ 17/20 passaram              │
│  COST: R$ [valor] TCO 5 anos                 │
│  TEAM FIT: 🟢 Time domina 70% da stack       │
│                                               │
│  PRE-COMMITMENT METRICS:                      │
│  • Latência p99 < 200ms até [data]            │
│  • Cobertura de testes > 80% até [data]       │
│  • Custo mensal < R$ [valor] até [data]       │
│                                               │
│  EXIT CRITERIA (abandonamos se):              │
│  • Latência p99 > 500ms após 1 mês            │
│  • Custo > 150% do budget por 2 meses         │
│  • 3+ incidentes críticos no primeiro mês     │
│                                               │
│  REVIEW DATE: [data] — reavaliar decisão      │
└──────────────────────────────────────────────┘
```

---

## 🔷 Layer 15 — Implementation Roadmap & Rollback (Completo)

> *GLM não só decide — ele mostra o caminho com código.*

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

📅 FASE 6 — Anti-frágil 🆕
   ├── Chaos engineering programado
   ├── Game days trimestrais
   ├── Postmortem blameless
   └── ✅ Marco: Sobrevive a 3 falhas injetadas
```

### 🔙 Plano de Rollback

| Fase | Ponto de não-retorno | Como voltar | Custo |
|---|---|---|---|
| Fase 1 | Sprint 3 | `git revert` + redeploy | 2 dias |
| Fase 2 | Sprint 6 | Feature flag desliga | 1 dia |
| Fase 3 | Sprint 8 | DNS aponta pro antigo | 4h |
| Fase 4 | Sprint 10 | Reduz réplicas | 2h |
| Migração | Cutover+1h | DNS revert | 30min |
| Anti-frágil | Contínuo | N/A (incremental) | — |

---

## 🚫 20 Anti-Patterns Bloqueados

> *GLM identifica e BLOQUEIA na hora.*

| # | Anti-Pattern | GLM Detection |
|---|---|---|
| 🚫 1 | **"Vai na hype"** | "Essa tecnologia resolve SEU problema?" |
| 🚫 2 | **"Sempre fizemos assim"** | "A zona de conforto é onde a inovação morre." |
| 🚫 3 | **"Não temos tempo"** | "Não ter tempo é o MAIOR risco." |
| 🚫 4 | **1 opção só** | "Decisão sem alternativa é dogma. Gere 6." |
| 🚫 5 | **Decisão adiada** | "Adiar é decidir por padrão." |
| 🚫 6 | **Ignorar reversibilidade** | "Toda decisão tem custo de rollback." |
| 🚫 7 | **Time não consultado** | "Quem implementa precisa ser ouvido." |
| 🚫 8 | **Stack única pra tudo** | "One-size-fits-all raramente funciona." |
| 🚫 9 | **"Depois refatora"** | "Refatoração postergada é dívida eterna." |
| 🚫 10 | **Ignorar observabilidade** | "Se não dá pra medir, não dá pra operar." |
| 🚫 11 | **Superestimar time** | "Heróis não escalam." |
| 🚫 12 | **Subestimar dados** | "Dados sempre crescem mais que o esperado." |
| 🚫 13 | **Ignorar segurança** | "Segurança no final sai mais caro." |
| 🚫 14 | **Plano sem rollback** | "Se não tem volta, é aposta, não decisão." |
| 🚫 15 | **Decisão sem data de revisão** | "Toda decisão técnica tem prazo de validade." |
| 🚫 16 | **Ignorar Conway's Law** 🆕 | "A arquitetura segue o time, não o contrário." |
| 🚫 17 | **Sunk cost fallacy** 🆕 | "O que já investimos não justifica continuar." |
| 🚫 18 | **Ignorar privacidade** 🆕 | "LGPD/GDPR no final é multa certa." |
| 🚫 19 | **Supply chain cego** 🆕 | "Dependência sem SBOM é bomba-relógio." |
| 🚫 20 | **Anti-frágil ignorado** 🆕 | "Sistema que não aprende com falhas é frágil." |

---

## 📦 Artefatos Gerados (10)

GLM gera **10 artefatos** completos ao final:

```
📁 docs/
├── adr/
│   ├── YYYY-MM-DD-<topic>-decision.md      → Decisão principal
│   ├── YYYY-MM-DD-<topic>-code-report.md   → Análise de código
│   ├── YYYY-MM-DD-<topic>-threat-model.md  → Modelo de ameaças
│   ├── YYYY-MM-DD-<topic>-privacy-model.md → Modelo de privacidade
│   └── YYYY-MM-DD-<topic>-data-arch.md     → Arquitetura de dados
│
├── roadmap/
│   └── YYYY-MM-DD-<topic>-implementation.md → Roadmap completo
│
├── cost/
│   └── YYYY-MM-DD-<topic>-tco.md           → Modelo de custo 5 anos
│
├── ops/
│   └── YYYY-MM-DD-<topic>-observability.md → Observabilidade + SLO
│
└── decisions/
    ├── README.md                             → Índice de decisões
    ├── YYYY-MM-DD-<topic>-review.md         → Data de revisão futura
    └── YYYY-MM-DD-<topic>-exit.md           → Estratégia de saída
```

---

## 📊 Comparativo: DeepSeek vs GLM Pesadíssimo

| Aspecto | DeepSeek Pesadíssimo | **GLM Pesadíssimo MAX** |
|---|---|---|
| **Camadas** | 13 + extra | **15** |
| **Critérios** | 20 | **25** |
| **Opções** | 5 | **6** |
| **Stress tests** | 15 | **20** |
| **Anti-patterns** | 15 | **20** |
| **Efeitos** | Até 4ª ordem | **Até 5ª ordem** |
| **Bias corrigidos** | 5 | **7** |
| **Threat model** | STRIDE | **STRIDE + LINDDUN** |
| **Cost model** | 3 anos | **5 anos** |
| **Artefatos** | 8 | **10** |
| **Conway's Law** | ❌ | ✅ **Layer dedicada** |
| **Anti-frágil** | ❌ | ✅ **Opção F + Fase 6** |
| **Privacy (LGPD)** | Compliance | ✅ **LINDDUN dedicado** |
| **Supply chain** | ❌ | ✅ **SBOM/SLSA** |
| **Modelo** | DeepSeek V4 Flash | **GLM 5.2 Free** |
| **Contexto** | 1M | **1M tokens** |

---

## 🧬 GLM Advantage — Por que ele?

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│   Z.AI GLM 5.2 Free × ZenMux                           │
│                                                         │
│   ✅ 1M de contexto → Lê o PROJETO INTEIRO              │
│   ✅ Grátis → Pode usar sem medo                        │
│   ✅ Raciocínio profundo → Análise 15 camadas            │
│   ✅ Excelente em código → Gera esboços reais            │
│   ✅ Visão de longo prazo → 5ª ordem de efeitos          │
│   ✅ Multi-cultural → Treinado em dados globais          │
│   ✅ Anti-frágil nativo → Pensa em caos                  │
│                                                         │
│   O modelo grátis mais pesado para decisão de           │
│   arquitetura que existe.                                │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

> *"Arquitetura não é sobre acertar de primeira. É sobre mapear todas as consequências — até a 5ª ordem — antes de escolher."*
> — GLM Architecture Decision Skill
