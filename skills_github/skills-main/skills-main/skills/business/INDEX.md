# SKILL LIBRARY — Business & Tax Brasil
# Indice Geral | Versao: 1.1.0 | Criado: 2026-05-17 | Atualizado: 2026-05-17
# Sessao: sess_20260517_2226_biz | Autor: Joelson Hott
# GitHub: https://github.com/Joehott/skills/tree/main/skills/business

---

## VISAO GERAL

Esta biblioteca reune 15 arquivos cobrindo analise de negocios, validacao de ideias,
plano de negocios, tributacao brasileira completa, otimizacao fiscal e ferramentas
de integracao para agentes IA. Destina-se a uso em chats especializados de mentoria,
analise e planejamento empresarial.

```
TOTAL: ~293 KB de conhecimento estruturado
ARQUIVOS: 10 skills (.md) + 2 scripts executaveis (.py) + 2 guias visuais (.html) + 1 router (.md)
LINHAS: ~7.400 linhas de conteudo
CNAE: 200+ codigos mapeados (script Python)
TOKEN BUDGET: ~56K tokens total | ~10K tokens por sessao tipica (com roteamento)
```

---

## MAPA DE USO — QUANDO CARREGAR CADA SKILL

```
SITUACAO                                  | SKILLS A CARREGAR
------------------------------------------|------------------------------------------
Abrir uma nova empresa                    | brazil_tax_regulatory + brazil_tax_complete
Validar uma ideia de negocio              | business_idea_validation + business_viability_calculation
Fazer plano de negocios completo          | business_plan_creation + business_viability_calculation + brazil_tax_regulatory
Analise rapida de empresa existente       | business_analysis
Calcular viabilidade financeira           | business_viability_calculation
Consultar regime tributario por CNAE      | brazil_cnae_database.py (executar) + brazil_tax_complete
Planejar calendario fiscal 2026           | brazil_tax_obligations_calendar
Aproveitar regime especial (RET/ZFM/etc)  | brazil_tax_special_regimes
Entender impacto da Reforma Tributaria    | brazil_tax_reform_2026_2032
Otimizar retirada do socio (PF)          | brazil_tax_individual_optimization
Planejamento sucessorio / ITCMD          | brazil_tax_individual_optimization
Negociar divida tributaria               | brazil_tax_special_regimes (secao 7)
Captacao de investimento                 | business_viability_calculation (secao 9)
```

---

## GRUPO 1 — ANALISE E ESTRATEGIA DE NEGOCIOS

### 1.1 business_analysis.md
**Tamanho:** 9.1 KB | **Drive:** `1AbOI6nBDYwzCoPhiVqqoV-K7jXHSe5yC`
**GitHub:** `skills/business/business_analysis.md`

Frameworks de analise empresarial:
- SWOT (Strengths, Weaknesses, Opportunities, Threats)
- Porter's 5 Forces (rivalidade, entrantes, substitutos, fornecedores, clientes)
- PESTEL (Politico, Economico, Social, Tecnologico, Ecologico, Legal)
- Cadeia de Valor (Porter)
- Matriz BCG (Stars, Cash Cows, Question Marks, Dogs)
- VRIO (Valor, Raridade, Imitabilidade, Organizacao)
- Analise Financeira (liquidez, rentabilidade, endividamento)
- Mapa Competitivo (posicionamento vs concorrencia)
- Checklist de analise completa
- Fontes de dados no Brasil (CVM, IBGE, SEBRAE, B3)

---

### 1.2 business_idea_validation.md
**Tamanho:** 12.3 KB | **Drive:** `17tEnZgF14RlXuAsyE1tL9U02YAuqqG20`
**GitHub:** `skills/business/business_idea_validation.md`

Metodologias de validacao:
- Lean Canvas (9 blocos)
- Business Model Canvas (BMC)
- Problem-Solution Fit (entrevistas e experimentos)
- Product-Market Fit (PMF) — metricas e sinais
- TAM / SAM / SOM (dimensionamento de mercado)
- Experimentos Lean (MVP, A/B, smoke test, landing page)
- Jobs To Be Done (JTBD)
- Unit Economics (LTV, CAC, payback, margem de contribuicao)
- Checklist de validacao completa

---

### 1.3 business_plan_creation.md
**Tamanho:** 12.8 KB | **Drive:** `1-4UzQxspzYqZPrgZd01QD8VNJZ2yKS7s`
**GitHub:** `skills/business/business_plan_creation.md`

8 secoes completas do plano de negocios:
- Sumario Executivo
- Descricao da Empresa (missao, visao, valores, CNPJ)
- Analise de Mercado (TAM/SAM/SOM, personas, concorrencia)
- Plano de Marketing e Vendas (4Ps, CAC, funil)
- Plano Operacional (processos, tecnologia, fornecedores)
- Estrutura Organizacional (organograma, equipe-chave)
- Plano Financeiro (DRE 3 anos, capex, break-even)
- Analise de Riscos (matriz probabilidade × impacto)
- Guia para Pitch Deck (10 slides)
- Checklist de qualidade do plano

---

### 1.4 business_viability_calculation.md
**Tamanho:** 13.6 KB | **Drive:** `1izTAFQi7855xt2QNjzTu5LsjNaRHyUTE`
**GitHub:** `skills/business/business_viability_calculation.md`

Calculos financeiros de viabilidade:
- Break-Even: contabil, financeiro e economico
- Payback Simples e Payback Descontado (com tabela exemplo)
- VPL — Valor Presente Liquido (formula + exemplo + Excel)
- TIR — Taxa Interna de Retorno (benchmarks Brasil 2025)
- Modelo de Projecao Financeira 3 anos (template DRE mensal)
- Analise de Cenarios (pessimista / base / otimista)
- Valuation: DCF, Multiplos, Berkus, Scorecard, VC Method
- Fontes de financiamento no Brasil (BNDES, Finep, angel, VC)
- TMA referencia Brasil 2025: SELIC + premio risco = 15-20%
- Checklist de viabilidade completo (6 gates de aprovacao)

---

## GRUPO 2 — TRIBUTACAO BRASILEIRA — NUCLEO

### 2.1 brazil_tax_regulatory.md
**Tamanho:** 15.9 KB | **Drive:** `1x1pOXlla4vOaR3xgcWn5JJCwZV4uq6sQ`
**GitHub:** `skills/business/brazil_tax_regulatory.md`

Guia estrategico de tributacao:
- Comparativo de tipos de empresa (MEI, ME, EPP, LTDA, SAS, SA)
- Regimes tributarios: tabela de decisao (MEI → Simples → Presumido → Real)
- Simples Nacional: todos os 5 Anexos com tabelas completas
- Formula da aliquota efetiva (RBT12 × nominal - deducao) / RBT12
- Reforma Tributaria 2026: dividendos (PL 1087) + CBS/IBS
- Pro-labore vs dividendos: calculadora de remuneracao do socio
- Holding familiar: quando criar e como estruturar
- Abertura de empresa: fluxo passo a passo
- 8 armadilhas tributarias mais comuns
- Carga tributaria real: simulador mental

---

### 2.2 brazil_tax_complete.md
**Tamanho:** 32.8 KB | **Drive:** `1axWv7hrDpKUbvKLXMcGj94cRLzmuOASv` *(maior arquivo)*
**GitHub:** `skills/business/brazil_tax_complete.md`

Referencia completa de todos os 6 regimes:
- MEI: DAS fixo 2025, limites, vedacoes, passo a passo
- Simples Nacional: 5 Anexos + Fator-R + PGDAS-D + DEFIS
- Lucro Presumido: tabela IRPJ/CSLL por setor, PIS/COFINS cumulativos
- Lucro Real: LALUR, estimativa mensal vs trimestral, ECD/ECF
- SA Capital Aberto: IPO, B3, CVM, IFRS, Formulario de Referencia
- Capital Estrangeiro: RDE-IED BACEN, Transfer Pricing OCDE 2024
- CNAE × Regime: mapeamento de 30+ setores
- CLT × Regime: encargos patronais por regime
- Topicos especiais: CPRB, ISS Fixo, ICMS-ST, Lucro Arbitrado
- Arvore de decisao final de regime

---

## GRUPO 3 — TRIBUTACAO BRASILEIRA — EXPANSAO

### 3.1 brazil_tax_obligations_calendar.md
**Tamanho:** 18.5 KB | **Drive:** `1huXNBoL7MIZyYjGA3Am6EhmGKZNpEPY3`
**GitHub:** `skills/business/brazil_tax_obligations_calendar.md`

Calendario fiscal completo:
- Calendario mensal: FGTS (dia 7), DAS/PGDAS-D (dia 20), PIS/COFINS (dia 25), DCTFWeb
- Calendario trimestral: IRPJ/CSLL Lucro Presumido/Real, ITR (SA)
- Calendario anual por regime: MEI (DASN-SIMEI), Simples (DEFIS), Lucro (ECD/ECF)
- TCO fiscal: custo real de conformidade por porte (MEI → SA Capital Aberto)
- Tabela de multas referencia rapida (DAS, DCTFWeb, EFD, FGTS, eSocial)
- Calendario consolidado 2026: todas as datas criticas do ano
- Obrigacoes por evento: admissao CLT, demissao, capital estrangeiro, fusao
- Sistemas e portais obrigatorios: eSocial, SPED, e-CAC, FGTS Digital
- Checklist de conformidade fiscal anual

---

### 3.2 brazil_tax_special_regimes.md
**Tamanho:** 21.6 KB | **Drive:** `1pOId5qtTtLa68gU-NLqP7qaTRubV81qD`
**GitHub:** `skills/business/brazil_tax_special_regimes.md`

Regimes especiais e incentivos:
- RET (imobiliario): 4% unificado vs ~5.9% Lucro Presumido — economia ~1.9pp
- REIDI (infraestrutura): suspensao PIS/COFINS em projetos >R$50M
- Lei do Bem (P&D): exclusao 60-80% despesas do IRPJ/CSLL no Lucro Real
- Zona Franca de Manaus: IPI zero + ICMS reduzido + beneficios ate 2073
- RECAP (exportadores): suspensao PIS/COFINS no imobilizado (>50% exportacao)
- PADIS (semicondutores): aliquota zero IPI/PIS/COFINS ate 2049
- Transacao Tributaria / PERT: descontos ate 100% multas/juros (120-145 parcelas)
- Comparativo: quando usar cada regime especial
- Checklists de adesao rapida
- Impacto da Reforma 2026-2032 em cada regime

---

### 3.3 brazil_tax_reform_2026_2032.md
**Tamanho:** 21.9 KB | **Drive:** `1jiScpU62Zu_Rrtph80GC1Nk6_CJvCdhq`
**GitHub:** `skills/business/brazil_tax_reform_2026_2032.md`

Guia completo da Reforma Tributaria (EC 132/2023 + LC 214/2025):
- Cronograma 2026-2033: aliquotas CBS/IBS ano a ano
- CBS (substitui PIS/COFINS): 0.9% em 2026, ~8-9% plena 2027+
- IBS (substitui ICMS/ISS): 0.1% em 2026, ~17-19% pleno 2033
- Imposto Seletivo (IS): tabaco, bebidas, veiculos por emissao CO2
- PL 1087/2025: IRPF Minimo 10% (renda >R$600K/ano) + IRRF 10% dividendos >R$50K/mes
- Split Payment: CBS/IBS retidos na fonte do pagamento — impacto no caixa
- Principio de destino: elimina guerra fiscal entre estados, elimina DIFAL
- Impacto por setor: SaaS/servicos digitais (+15pp), industria (neutro), exportacao (positivo)
- Simples Nacional na transicao: DAS mantido, decisao 2027
- Simulacoes numericas: SaaS R$1M/mes e industria R$1M/mes
- Checklist de preparacao empresarial por ano

---

### 3.4 brazil_tax_individual_optimization.md
**Tamanho:** 22.0 KB | **Drive:** `1IiyHUJus1DO7aVtixuBgQ-OQDXPS2rHh`
**GitHub:** `skills/business/brazil_tax_individual_optimization.md`

Otimizacao fiscal para pessoa fisica e socio:
- Tabela IRPF 2026: isencao ate R$5.000/mes (PL 1087/2025)
- IRPF Minimo: calculo exato com 3 exemplos (R$300K, R$700K, R$1.2M/ano)
- Pro-labore otimo: R$5K/mes (isento) + dividendos ate R$50K/mes
- Tabela comparativa pro-labore vs dividendo para cada faixa de renda
- PGBL/VGBL: deducao 12% renda tributavel, tabela regressiva (10% apos 10 anos)
- ITCMD progressivo 2027: urgencia de doacao em vida em 2026 (janela critica)
- Holding familiar: quando vale a pena, estrutura, clausulas de protecao
- VGBL para sucessao: fora do espolio, sem ITCMD (enquanto nao regulamentado)
- Seguro de vida: isento IRPF e ITCMD
- Simulador de carga fiscal: socio R$30K/mes = 1.8% carga, R$100K/mes = 10.5%
- Checklist de revisao anual para o socio

---

## GRUPO 4 — FERRAMENTAS DE CONSULTA

### 4.1 brazil_cnae_database.py
**Tamanho:** 29.8 KB | **Drive:** `1F1pwoWU_xXkXXRuPbqK6PaFXoeCA44w9`
**GitHub:** `skills/business/brazil_cnae_database.py`

Script Python executavel — consulta CNAE x Regime x Aliquota:

```bash
python3 brazil_cnae_database.py 6201500                                      # CNAE especifico
python3 brazil_cnae_database.py --search engenharia                          # Busca por termo
python3 brazil_cnae_database.py --simular --cnae 7112000 --faturamento 800000 --folha 250000
python3 brazil_cnae_database.py --list-vedados                               # CNAEs vedados
```

Recursos:
- 200+ CNAEs mapeados com Anexo Simples, ISS, ICMS, IPI
- Calculo automatico do Fator-R (Anexo III vs Anexo V)
- Aliquota efetiva Simples por faixa de faturamento
- Comparativo automatico Simples vs Lucro Presumido
- CNAEs vedados com motivo de vedacao
- Busca textual por descricao da atividade

**IMPORTANTE:** Executar o script (~50 tokens output). NAO ler o fonte (7.4K tokens).

---

### 4.2 skills_loader.py
**Tamanho:** 10.6 KB | **Drive:** `1XRg45CjMEHm_NFya_0YYE0GTz3gmBzrr`
**GitHub:** `skills/business/skills_loader.py`

Roteador de skills por query livre — determina quais arquivos carregar:

```bash
python3 skills_loader.py "abrir empresa TI simples nacional"   # recomenda 2-3 skills
python3 skills_loader.py --load brazil_tax_regulatory          # imprime conteudo da skill
python3 skills_loader.py --list                                # lista todas as skills
python3 skills_loader.py --fetch brazil_tax_complete           # baixa do GitHub
```

Recursos:
- Mapeamento de keywords por skill (150+ keywords indexadas)
- Score ponderado: keywords longas (>8 chars) valem 2x
- Retorna top-3 skills mais relevantes + tokens estimados
- Fallback local → GitHub raw quando arquivo nao encontrado
- Economia: ~50 tokens de output vs 56K carregar tudo

---

## GRUPO 5 — DOCUMENTACAO E INTEGRACAO

### 5.1 AGENTS.md
**Tamanho:** 3.6 KB | **Drive:** `1KR8ls9qReIu0Yv_Il4ofq6jrbvKVjxt-`
**GitHub:** `skills/business/AGENTS.md`

Instrucoes mestre para agentes IA — deve ser carregado SEMPRE primeiro:
- Regra #1: nao carregar tudo (56K tokens = desperdicio)
- Router situacao → arquivo(s) em formato de tabela
- Instrucoes de execucao do CNAE script (executar, nao ler)
- URLs GitHub raw para acesso remoto sem clone
- Mapa rapido de arquivos com tokens por arquivo
- Contexto de validacao: base legal ate 2026-05-17

Uso: copiar como `CLAUDE.md` (Claude Code), `AGENTS.md` (Codex/OpenCode),
ou colar como system prompt (Hermes/chat generico).

---

### 5.2 skill_library_overview.html
**Tamanho:** 38 KB | **Drive:** `1GiZVqhFvs0YDAgrr67hJDW7qDDIibACA`
**GitHub:** `skills/business/skill_library_overview.html`

Visao geral visual da biblioteca (dark mode):
- Hero com estatisticas da biblioteca (15 arquivos, 293 KB, 200+ CNAEs)
- Como funciona: fluxo em 3 etapas
- Cards de cada skill com descricao e tokens
- Tabela de casos de uso por situacao
- Roadmap de expansoes futuras

---

### 5.3 agent_integration_guide.html
**Tamanho:** 27.9 KB | **Drive:** `1ZxKt_t_4wzogz3vymCzG8vEpK8t4jz_f`
**GitHub:** `skills/business/agent_integration_guide.html`

Guia tecnico de integracao por plataforma (dark mode GitHub-style):
- Visualizacao de custo em tokens: barra 56K vs ~9K com roteamento (82% economia)
- Arquitetura 3 camadas: AGENTS.md (915 tok) → Skills (2-8K tok) → Scripts (~50 tok)
- Integracao Claude Code: padrao CLAUDE.md + clone do repo
- Integracao Codex/OpenCode: AGENTS.md na raiz do projeto
- Integracao Hermes/chat: colar como system prompt ou URLs raw do GitHub
- Uso do skills_loader.py com exemplos de query
- Tabela anti-padrao CNAE: ler fonte (7.4K) vs executar script (50 tokens)
- Fluxo ideal de sessao com contagem de tokens passo a passo
- Arvore completa de arquivos do repositorio

---

## REFERENCIAS EXTERNAS

```
SISTEMA            | URL / ID                                        | USO
-------------------|-------------------------------------------------|---------------------------
GitHub Repo        | github.com/Joehott/skills                       | Versionamento de todas as skills
GitHub Raw Base    | raw.githubusercontent.com/Joehott/skills/main/  | Acesso direto por agentes remotos
Google Drive       | Pasta ID: 1rUocPt6teyKFQeS7zjF5HH7F9nE32kd2    | Backup e acesso externo
Receita Federal    | receita.fazenda.gov.br                          | Validar aliquotas vigentes
Portal Simples SN  | receita.fazenda.gov.br/SimplesNacional          | Calcular DAS oficial
Reforma Tributaria | gov.br/reformatributaria                        | CBS/IBS regulamentacao
PGFN Transacao     | regularize.pgfn.gov.br                          | Negociar dividas PGFN
eSocial            | esocial.gov.br                                  | Folha de pagamento
SPED               | sped.rfb.gov.br                                 | ECD, ECF, EFD
```

---

## ARVORE DE ARQUIVOS

```
skills/business/
├── AGENTS.md                           3.6 KB  | Router mestre para agentes IA
├── INDEX.md                           (este arquivo)
├── skills_loader.py                   10.6 KB  | Roteador CLI por query livre
│
├── business_analysis.md               9.1 KB  | SWOT, Porter, BCG, VRIO
├── business_idea_validation.md       12.3 KB  | Lean Canvas, PMF, TAM/SOM
├── business_plan_creation.md         12.8 KB  | Plano 8 secoes + Pitch Deck
├── business_viability_calculation.md 13.6 KB  | VPL, TIR, Payback, Valuation
│
├── brazil_tax_regulatory.md          15.9 KB  | Regimes, tipos empresa, armadilhas
├── brazil_tax_complete.md            32.8 KB  | 6 regimes detalhados (referencia)
├── brazil_tax_obligations_calendar.md 18.5 KB | Calendario 2026, multas, sistemas
├── brazil_tax_special_regimes.md     21.6 KB  | RET, REIDI, Lei do Bem, ZFM, PADIS
├── brazil_tax_reform_2026_2032.md    21.9 KB  | CBS/IBS/IS, IRPF Minimo 2026-2033
├── brazil_tax_individual_optim.md    22.0 KB  | Pro-labore, PGBL, ITCMD, holding
│
├── brazil_cnae_database.py           29.8 KB  | CNAE x Regime — EXECUTAR, nao ler
│
├── skill_library_overview.html       38.0 KB  | Visao geral visual da biblioteca
└── agent_integration_guide.html      27.9 KB  | Guia de integracao por plataforma
                                      -------
TOTAL                                293.4 KB
```

---

## PROXIMOS PASSOS SUGERIDOS

```
EXPANSOES POSSIVEIS:
[ ] brazil_tax_municipal_iss.md — ISS por municipio (top 20 cidades)
[ ] brazil_financial_modeling.xlsx — Planilha integrada DRE + Fluxo + Indices
[ ] brazil_startup_equity.md — Cap table, ESOP, vesting, SAFEs no Brasil
[ ] brazil_labor_law.md — CLT completa: verbas, jornada, demissao, terceirizacao
[ ] brazil_international_trade.md — Importacao/exportacao, drawback, RAC
[ ] brazil_cnae_database_v2.py — Expandir para 500+ CNAEs + API da Receita Federal

INTEGRACAO FUTURA:
[ ] DB SQLite com todos os CNAEs da Receita Federal (~1.300 codigos)
[ ] API wrapper para consulta automatica de aliquota vigente
[ ] Integracao com Notion Database para gestao de clientes de mentoria
```

---

*Indice gerado em 2026-05-17 | Atualizado v1.1.0 em 2026-05-17 | sess_20260517_2226_biz*
