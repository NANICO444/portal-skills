# SKILL: Business Viability Calculation
# Versao: 1.0.0 | Para: modules_strategy, modules_data, modules_personal_v2, modules_programming_v2 | Fase: 3-5
# Criada em: 2026-05-17 | Sessao: sess_20260517_2226_biz
# CONTEXTO: Calcular viabilidade econômico-financeira de negócios no Brasil

---

## QUANDO USAR
- Ao calcular se um negócio é viável ANTES de abri-lo
- Ao avaliar se vale o investimento (TIR vs Taxa Mínima de Atratividade)
- Ao estruturar projeções para buscar financiamento (BNDES, banco, investidor)
- Ao fazer mentoria financeira e identificar alavancas de crescimento

---

## 1. ESTUDO DE VIABILIDADE ECONÔMICA — ESTRUTURA COMPLETA

```
ESTUDO DE VIABILIDADE — [Nome do Negócio] — [Data]

PREMISSAS BASE:
- Receita média mensal esperada (Ano 1): R$ ___
- Crescimento mensal esperado (Ano 1): ___%
- Margem bruta: ___%
- Regime tributário: ___
- Alíquota efetiva: ___%
- Capital inicial necessário: R$ ___
- Taxa Mínima de Atratividade (TMA): ___% ao ano
  (Referência Brasil 2025: SELIC 10,5-13,75% + prêmio de risco ~5% = 15-20%)

INDICADORES A CALCULAR:
→ Payback Simples
→ Payback Descontado
→ VPL (Valor Presente Líquido)
→ TIR (Taxa Interna de Retorno)
→ Ponto de Equilíbrio (Break-even)
→ Margem de Segurança
```

---

## 2. PONTO DE EQUILÍBRIO (Break-Even)

```
TIPOS DE BREAK-EVEN:

A) CONTÁBIL (quando não há mais prejuízo):
PE = Custos Fixos / Margem de Contribuição (%)
PE = R$___ / ___% = R$___/mês

B) FINANCEIRO (quando gera caixa suficiente para obrigações):
PE_fin = (Custos Fixos - Depreciação) / MC%

C) ECONÔMICO (quando remunera o capital adequadamente):
PE_econ = (Custos Fixos + Retorno Mínimo Esperado) / MC%

TEMPLATE:
Custos Fixos Mensais:
  Aluguel:           R$ ___
  Folha (CLT):       R$ ___
  Pró-labore sócios: R$ ___
  Contabilidade:     R$ ___
  Marketing fixo:    R$ ___
  Serviços/SaaS:     R$ ___
  Outros:            R$ ___
  TOTAL CF:          R$ ___

Margem de Contribuição:
  Preço de venda:    R$ ___
  (-) Custos var.:   R$ ___  (matéria-prima, comissão, frete, impostos variáveis)
  = MC Unitária:     R$ ___
  MC%:               ___%

Break-even Contábil = R$___ CF / ___% MC = R$ ___ /mês
Break-even em unidades = R$___ CF / R$___ MC unitária = ___ unidades/mês

MARGEM DE SEGURANÇA:
MS% = (Receita Atual - Break-even) / Receita Atual × 100
MS% = ___% (meta: >20%)
```

---

## 3. PAYBACK

```
PAYBACK SIMPLES:
Payback = Investimento Inicial / Lucro Líquido Médio Mensal
Payback = R$___ / R$___ = ___ meses

Interpretação:
- < 12 meses: excelente (baixo risco)
- 12-24 meses: bom
- 24-36 meses: aceitável
- > 36 meses: alto risco, exige retorno compensador

PAYBACK DESCONTADO (considera o valor do dinheiro no tempo):
Investimento: R$50.000
TMA mensal: 1,5% (≈18% a.a.)

Mês | FC       | FC Desc. (÷ (1+1.5%)^n) | Acumulado
  0 | -50.000  | -50.000                  | -50.000
  1 | +5.000   | +4.926                   | -45.074
  2 | +5.500   | +5.340                   | -39.734
  3 | +6.000   | +5.736                   | -34.000
  ...
  N | +X.XXX   | +X.XXX                   | 0 → PAYBACK DESCONTADO

FÓRMULA GERAL:
Payback Desc. = n quando ∑(FCt / (1+i)^t) = 0
```

---

## 4. VPL — VALOR PRESENTE LÍQUIDO

```
CONCEITO:
VPL = -I₀ + FC₁/(1+i)¹ + FC₂/(1+i)² + ... + FCn/(1+i)ⁿ

Onde:
- I₀ = Investimento inicial
- FC = Fluxo de Caixa líquido de cada período
- i = TMA (taxa de desconto)
- n = horizonte de análise (geralmente 3-5 anos)

INTERPRETAÇÃO:
VPL > 0: projeto cria valor (acima da TMA) → APROVADO
VPL = 0: projeto cobre exatamente a TMA → indiferente
VPL < 0: projeto destrói valor → REPROVADO (a menos que haja razão estratégica)

EXEMPLO PRÁTICO (negócio de serviços, Brasil):
Investimento: R$80.000
TMA: 18% a.a. (1,39% a.m.)
Projeção de fluxo de caixa:

Período | FC Bruto | Impostos(14%) | FC Líquido | FC Descontado
  0     | -80.000  | —             | -80.000    | -80.000
  Ano1  | +24.000  | -3.360        | +20.640    | +17.491
  Ano2  | +36.000  | -5.040        | +30.960    | +22.277
  Ano3  | +48.000  | -6.720        | +41.280    | +25.224
  Ano4  | +60.000  | -8.400        | +51.600    | +26.754
  Ano5  | +72.000  | -10.080       | +61.920    | +27.234
                                    VPL = +38.980 → VIÁVEL

CÁLCULO NO EXCEL:
=VPL(TMA; FC1; FC2; ...; FCn) - Investimento_Inicial
=VPL(18%;20640;30960;41280;51600;61920) - 80000
```

---

## 5. TIR — TAXA INTERNA DE RETORNO

```
CONCEITO:
É a taxa que faz VPL = 0. Se TIR > TMA → projeto é viável.

REGRA DE DECISÃO:
TIR > TMA: APROVADO (gera retorno acima do custo de oportunidade)
TIR < TMA: REPROVADO (melhor deixar no CDB/Tesouro)
TIR = TMA: indiferente

PARÂMETROS DE REFERÊNCIA BRASIL 2025:
- SELIC: ~10,5-13,75% a.a.
- CDB 100% CDI líquido: ~9-11% a.a.
- Tesouro IPCA+: IPCA + 6% ≈ 12-14% a.a.
- Negócios de baixo risco: TMA 15-18% a.a.
- Startups/alto risco: TMA 25-50% a.a.
- VC/PE: TMA 30-40% a.a.

FAIXAS DE AVALIAÇÃO:
TIR < 15%: evitar (menos que aplicação financeira + risco)
TIR 15-25%: negócio conservador (ok se baixo risco)
TIR 25-40%: negócio atrativo
TIR 40-60%: excelente
TIR > 60%: extraordinário (verificar premissas)

CÁLCULO NO EXCEL:
=TIR({-80000; 20640; 30960; 41280; 51600; 61920})
→ resultado: ~30% a.a. (viável com TMA 18%)

ARMADILHA: TIR múltipla quando o fluxo troca de sinal mais de uma vez.
Nesses casos, usar TIRM (TIR Modificada):
=MTIR(fluxos; custo_financiamento; TMA_reinvestimento)
```

---

## 6. MODELO DE PROJEÇÃO FINANCEIRA — 3 ANOS

```
PLANILHA DE PROJEÇÃO (mensal Ano 1, trimestral Ano 2-3)

RECEITAS:
                    Jan    Fev    Mar    ...  Dez   ANO1   ANO2   ANO3
Produto/Serv. A     ___    ___    ___         ___   ___    ___    ___
Produto/Serv. B     ___    ___    ___         ___   ___    ___    ___
RECEITA BRUTA       ___    ___    ___         ___   ___    ___    ___
(-) Impostos(%)     ___    ___    ___         ___   ___    ___    ___
= RECEITA LÍQUIDA   ___    ___    ___         ___   ___    ___    ___

CUSTOS VARIÁVEIS:
(-) CMV/CPV (%)     ___    ___    ___         ___   ___    ___    ___
(-) Comissões       ___    ___    ___         ___   ___    ___    ___
= MARGEM BRUTA      ___    ___    ___         ___   ___    ___    ___
  Margem Bruta %    ___%   ___%   ___%        ___%  ___%   ___%   ___%

CUSTOS FIXOS:
(-) Folha+encargos  ___    ___    ___         ___   ___    ___    ___
(-) Aluguel         ___    ___    ___         ___   ___    ___    ___
(-) Marketing       ___    ___    ___         ___   ___    ___    ___
(-) Tecnologia      ___    ___    ___         ___   ___    ___    ___
(-) Contabilidade   ___    ___    ___         ___   ___    ___    ___
(-) Outros CF       ___    ___    ___         ___   ___    ___    ___
= EBITDA            ___    ___    ___         ___   ___    ___    ___
  EBITDA %          ___%   ___%   ___%        ___%  ___%   ___%   ___%

(-) Depreciação     ___    ___    ___         ___   ___    ___    ___
= EBIT              ___    ___    ___         ___   ___    ___    ___
(-) Juros/IOF       ___    ___    ___         ___   ___    ___    ___
= LAIR               ___    ___    ___         ___   ___    ___    ___
(-) IR+CSLL         ___    ___    ___         ___   ___    ___    ___
= LUCRO LÍQUIDO     ___    ___    ___         ___   ___    ___    ___

FLUXO DE CAIXA:
Saldo inicial       ___    ___    ___         ___
+ Recebimentos      ___    ___    ___         ___
- Pagamentos        ___    ___    ___         ___
= SALDO FINAL       ___    ___    ___         ___
```

---

## 7. ANÁLISE DE CENÁRIOS

```
MATRIZ DE CENÁRIOS (obrigatório para qualquer plano de negócio sério):

VARIÁVEL           | PESSIMISTA  | BASE        | OTIMISTA
-------------------|-------------|-------------|----------
Crescimento MoM    | -20% do base| base        | +30% do base
Ticket médio       | -15%        | base        | +10%
Churn (se SaaS)    | +50%        | base        | -30%
CAC                | +40%        | base        | -20%
Prazo de pagamento | +30 dias    | base        | à vista
Taxa Simples       | +2pp        | base        | -1pp

RESULTADO:
                   | PESS.       | BASE        | OTI.
Receita Ano 1      | R$___       | R$___       | R$___
EBITDA Ano 1       | R$___       | R$___       | R$___
Payback            | ___ meses   | ___ meses   | ___ meses
TIR (3 anos)       | ___%        | ___%        | ___%
VPL (3 anos)       | R$___       | R$___       | R$___

GATE DE APROVAÇÃO:
[ ] Cenário pessimista ainda tem VPL > 0? (ideal)
[ ] Cenário pessimista: empresa sobrevive? (mínimo aceitável)
[ ] Payback no cenário base < 36 meses?
[ ] TIR no cenário base > TMA escolhida?
```

---

## 8. VALUATION — MÉTODOS PARA O MERCADO BRASILEIRO

```
MÉTODO 1 — DCF (Fluxo de Caixa Descontado) — mais rigoroso
Usar quando: empresa tem histórico de receita (>2 anos)
Fórmula:
  Valor = ∑(FCFt / (1+WACC)^t) + Valor Terminal
  Valor Terminal = FCF_último × (1+g) / (WACC - g)
  g = taxa de crescimento perpétuo (2-4% para Brasil)
  WACC = custo médio ponderado de capital

MÉTODO 2 — Múltiplos de Mercado — mais prático
Usar quando: há comparáveis públicos ou transações recentes
Faixas Brasil 2024-2025:
  SaaS B2B crescendo >50%/ano: 5-10x ARR
  SaaS B2B crescendo 20-50%/ano: 2-5x ARR
  E-commerce: 0.5-2x Receita Anual
  Serviços tradicionais: 4-8x EBITDA
  Varejo: 4-7x EBITDA
  Tech/Plataforma early-stage: 5-15x ARR

MÉTODO 3 — Berkus Method — para pré-receita
Máximo R$2.5 milhões total:
  Ideia com valor verificado:        até R$500K
  Protótipo funcional:               até R$500K
  Time de qualidade:                 até R$500K
  Relacionamentos estratégicos:      até R$500K
  Produto lançado / primeiras vendas:até R$500K

MÉTODO 4 — Scorecard (Seed/Angel) — pré-seed Brasil
Base: valuação média de startups comparáveis no Brasil (~R$2-5M pré-seed)
Fatores multiplicadores:
  Time fundador (0.0-1.5x): peso 30%
  Oportunidade de mercado (0.0-1.5x): peso 25%
  Produto/tecnologia (0.0-1.5x): peso 15%
  Concorrência (0.0-1.5x): peso 10%
  Marketing/canais (0.0-1.5x): peso 10%
  Necessidade de investimento adicional (0.0-1.0x): peso 5%
  Outros (0.0-1.0x): peso 5%

MÉTODO 5 — VC Method — seed/série A
Valuação pré-money = Retorno esperado / (1 + ROI esperado)^anos
Onde:
  Retorno esperado = Exit value × % participação do fundo
  ROI VC típico Brasil: 10-30x em 5-7 anos
```

---

## 9. ANÁLISE DE FINANCIAMENTO — FONTES NO BRASIL

```
OPÇÕES DE CAPITAL PARA PMEs E STARTUPS:

CAPITAL PRÓPRIO:
- Savings dos sócios: mais simples, sem custo de capital
- Família e amigos (FFF): seed informal, cuidado com relações

CAPITAL DE TERCEIROS (DEBT):
Linha          | Tx.Juros/a.a.| Prazo  | Pra quem
Antecipação AR | 15-30%       | Curto  | Quem tem recebíveis
Giro bancário  | 20-40%       | Curto  | Capital de giro
BNDES Mpme     | 1-3% + IPCA  | 5-10a  | PMEs, indústria
BNDES Procapin | 5-10%        | 5-8a   | Inovação, tech
Finep Startup  | TJLP (~6-8%) | 5-10a  | Inovação, P&D
FGTS/CAIXA    | 4-8%          | 5-20a  | Imóvel produtivo
Fintech (Omie, etc): 2-5%/mês  curto   | PME estabelecida

CAPITAL DE RISCO (EQUITY):
Fase         | Valor típico BR | Quem
Pré-seed     | R$100K-500K    | Angel (amigo), aceleradoras
Seed         | R$500K-3M      | Angel, fundos seed, BNDES Garagem
Série A      | R$3M-20M       | VC (Kaszek, Monashees, etc.)
Série B+     | R$20M+         | VC, PE, CVC

INCENTIVOS E SUBSÍDIOS:
- Lei do Bem (crédito fiscal P&D): desconto 60-80% em despesas P&D
- PADIS (semicondutores): alíquota zero
- Zona Franca de Manaus: incentivos fiscais setoriais
- FAPESP/FAPEMIG/etc: grants para pesquisa (não reembolsável)
- Inovar-Auto, BNDES Produção Sustentável: setoriais

CRITÉRIOS PARA ESCOLHA:
[ ] Tenho histórico de 2+ anos de faturamento? → banco/BNDES mais acessível
[ ] Estou crescendo >20%/mês? → VC pode ter interesse
[ ] Produto inovador/P&D? → Finep, Lei do Bem, Startupsby
[ ] Imóvel próprio? → pode usar como garantia para juros menores
```

---

## 10. CHECKLIST DE VIABILIDADE COMPLETO

```
PRÉ-ANÁLISE:
[ ] Mercado dimensionado (TAM/SAM/SOM calculados)
[ ] Personas definidas com willingness to pay validada
[ ] Concorrentes mapeados com preços e margens estimados

ANÁLISE FINANCEIRA:
[ ] DRE projetada (3 anos, mensal no primeiro ano)
[ ] Fluxo de caixa (capital de giro calculado)
[ ] Investimento inicial detalhado (Capex + capital de giro)
[ ] Break-even calculado (contábil e financeiro)
[ ] Payback calculado (simples e descontado)
[ ] VPL calculado com TMA justificada
[ ] TIR calculada e comparada com TMA
[ ] 3 cenários (pessimista, base, otimista)

TRIBUTÁRIO (Brasil):
[ ] Regime tributário simulado (Simples vs Presumido vs Real)
[ ] Alíquota efetiva calculada para o regime escolhido
[ ] Impacto pró-labore vs dividendos calculado
[ ] Obrigações acessórias mapeadas e custos provisionados
[ ] Impacto Reforma Tributária 2026-2032 avaliado

GATE FINAL DE APROVAÇÃO:
[ ] VPL > 0 no cenário base?
[ ] TIR > TMA + prêmio de risco do setor?
[ ] Payback descontado < vida útil do negócio?
[ ] Caixa negativo máximo < capital disponível?
[ ] Break-even atingível em prazo razoável (<18 meses)?
[ ] Cenário pessimista: empresa sobrevive 12+ meses?

SE TODOS GATES VERDES: NEGÓCIO VIÁVEL → prosseguir para plano de execução
SE 1-2 GATES VERMELHOS: revisar premissas ou pivotar modelo
SE 3+ GATES VERMELHOS: reconsiderar fundamentalmente o negócio
```
