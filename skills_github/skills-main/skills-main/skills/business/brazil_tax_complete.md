# SKILL: Brazil Tax Complete — Todos os Regimes Tributários
# Versao: 1.0.0 | Para: modules_strategy, modules_data, modules_personal_v2 | Fase: 2-5
# Criada em: 2026-05-17 | Sessao: sess_20260517_2226_biz
# Pesquisa: Tavily + GitHub + skills.sh (validado em 2026-05-17)
# AVISO: Legislação em transição 2026-2032 — validar com contador para decisões

---

## ÍNDICE
1. Panorama dos 5 Regimes Tributários + Lucro Arbitrado
2. MEI — Microempreendedor Individual
3. Simples Nacional (com tabelas 2025 e Fator-R)
4. Lucro Presumido (percentuais completos IRPJ/CSLL)
5. Lucro Real (LALUR, trimestral vs anual, créditos PIS/COFINS)
6. Empresa de Capital Aberto (SA — CVM, B3, IFRS)
7. Empresa de Capital Estrangeiro (IED, RDE, Transfer Pricing)
8. CNAE × Regime Tributário (vedações, atividade mista, Fator-R)
9. CLT × Regime Tributário (encargos por regime, CPRB, custo real)
10. Tópicos Especiais (ICMS-ST, ISS Fixo, Holding, Reforma 2026)
11. Comparativo Final — Decisor de Regime
12. Armadilhas & Checklist de Auditoria

---

## 1. PANORAMA — 5 REGIMES + ARBITRADO

```
REGIME          | LIMITE RECEITA | OBRIG.    | COMPLEXIDADE | QUANDO
----------------|---------------|-----------|--------------|-------------------
MEI             | R$81K/ano     | Mínima    | ★☆☆☆☆       | Solo, 1 func. max
Simples Nacional| R$4.8M/ano    | Média     | ★★☆☆☆       | PME, geral
Lucro Presumido | R$78M/ano     | Alta      | ★★★☆☆       | Margem alta, previsível
Lucro Real      | Sem limite    | Muito alta| ★★★★★       | Margem baixa, créditos
SA/Capital Aberto| Sem limite   | Máxima    | ★★★★★       | Captação pública
Lucro Arbitrado | —             | Emergência| ★★★★☆       | RF aplica; evitar
```

---

## 2. MEI — MICROEMPREENDEDOR INDIVIDUAL

### Regras e limites
```
FATURAMENTO MÁXIMO: R$81.000/ano (R$6.750/mês)
FUNCIONÁRIOS: máximo 1 (salário mínimo ou piso da categoria)
SÓCIOS: não permitido
FILIAIS: não permitido

DAS MENSAL 2026 (valores aproximados):
  Comércio/Indústria: INSS(R$73,10) + ICMS(R$5,00) = R$78,10/mês
  Serviços:           INSS(R$73,10) + ISS(R$5,00)  = R$78,10/mês
  Comércio+Serviços:  INSS(R$73,10) + ICMS(R$5,00) + ISS(R$5,00) = R$83,10/mês
  (Base: INSS = 5% do salário mínimo = 5% × R$1.518 = R$75,90 em 2025)

OBRIGAÇÕES:
  [ ] DAS mensal (vencimento dia 20)
  [ ] DASN-SIMEI anual (até 31/maio)
  [ ] Notas fiscais (guardar 5 anos)
  [ ] Emitir NFS-e para CNPJ (obrigatório desde 2023)

VEDAÇÕES (não pode ser MEI):
  - Sócio ou titular de outra empresa
  - Atividades regulamentadas sem permissão específica
  - Venda de bebidas alcoólicas (exceto artesanal)
  - Açougue, peixaria, casa de carnes
  - Atividades financeiras (seguros, crédito)
  - Guarda de automóveis

LIMITE DE SUBEXCESSO: até 20% acima (R$97.200) → proporcionalidade
ULTRAPASSOU 20%: desenquadrado retroativamente ao início do ano
```

---

## 3. SIMPLES NACIONAL

### Critérios de enquadramento
```
REQUISITOS:
  + Receita Bruta ≤ R$4.800.000/ano
  + Não ter sócio PJ
  + Não ter sede no exterior
  + Não ter débito com a RFB/PGFN (salvo parcelado)
  + CNAE não vedado (ver Seção 8)
  + Capital social adequado

VEDAÇÕES SOCIETÁRIAS:
  × Sócio PJ (qualquer percentual)
  × Sócio com > 10% em empresa já no Lucro Real
  × Bancos, financeiras, seguradoras, corretoras
  × Factoring, câmbio, planos de saúde
  × Cooperativas (exceto crédito)
  × Entidades sem fins lucrativos
```

### Fator-R — Definição do Anexo III vs V
```
FATOR-R = FSPA (folha 12 meses) / RBT12 (receita 12 meses)

Folha = pró-labore + salários + encargos (exceto FGTS)
RBT12 = receita bruta acumulada 12 meses anteriores

Fator-R ≥ 28%  →  Anexo III  (menor carga tributária)
Fator-R < 28%  →  Anexo V    (maior carga tributária)

ESTRATÉGIA: Para empresas no Anexo V com margem alta,
aumentar pró-labore dos sócios pode reduzir a carga total.
Calcular ponto ótimo: ganho no Fator-R vs custo INSS/IR extra.

QUEM PODE USAR FATOR-R: Anexos III e V apenas (LC 123/2006, art. 18)
Atividades: TI, publicidade, engenharia, arquitetura, medicina (algumas)
```

### Tabelas Simples Nacional 2025 — Completa

#### Fórmula:
```
Alíq. Efetiva = (RBT12 × Alíq.Nominal - Parcela.Deduzir) / RBT12
```

#### ANEXO I — Comércio
```
Faixa | RBT12 (12 meses)               | Alíq.Nom.| Ded.       | Alíq.Ef.Teto
  1   | Até R$180.000                   |  4,00%   | R$0        | 4,00%
  2   | R$180.001 – R$360.000           |  7,30%   | R$5.940    | 5,65%
  3   | R$360.001 – R$720.000           |  9,50%   | R$13.860   | 7,57%
  4   | R$720.001 – R$1.800.000         | 10,70%   | R$22.500   | 9,45%
  5   | R$1.800.001 – R$3.600.000       | 14,30%   | R$87.300   | 11,87%
  6   | R$3.600.001 – R$4.800.000       | 19,00%   | R$378.000  | 10,54%
```

#### ANEXO II — Indústria (fábrica/produção)
```
Faixa | RBT12                           | Alíq.Nom.| Ded.
  1   | Até R$180.000                   |  4,50%   | R$0
  2   | R$180.001 – R$360.000           |  7,80%   | R$5.940
  3   | R$360.001 – R$720.000           | 10,00%   | R$13.860
  4   | R$720.001 – R$1.800.000         | 11,20%   | R$22.500
  5   | R$1.800.001 – R$3.600.000       | 14,70%   | R$85.500
  6   | R$3.600.001 – R$4.800.000       | 30,00%   | R$720.000
```

#### ANEXO III — Serviços (INSS incluso, Fator-R ≥ 28%)
```
Faixa | RBT12                           | Alíq.Nom.| Ded.
  1   | Até R$180.000                   |  6,00%   | R$0
  2   | R$180.001 – R$360.000           | 11,20%   | R$9.360
  3   | R$360.001 – R$720.000           | 13,20%   | R$17.640
  4   | R$720.001 – R$1.800.000         | 16,00%   | R$35.640
  5   | R$1.800.001 – R$3.600.000       | 21,00%   | R$125.640
  6   | R$3.600.001 – R$4.800.000       | 33,00%   | R$648.000
```

#### ANEXO IV — Serviços (INSS patronal separado, não incluso no DAS)
*Construção civil, vigilância, limpeza, advocacia, serviços de limpeza*
```
Faixa | RBT12                           | Alíq.Nom.| Ded.
  1   | Até R$180.000                   |  4,50%   | R$0
  2   | R$180.001 – R$360.000           |  9,00%   | R$8.100
  3   | R$360.001 – R$720.000           | 10,20%   | R$12.420
  4   | R$720.001 – R$1.800.000         | 14,00%   | R$39.780
  5   | R$1.800.001 – R$3.600.000       | 22,00%   | R$183.780
  6   | R$3.600.001 – R$4.800.000       | 33,00%   | R$828.000
ATENÇÃO: adicionar INSS patronal (20% sobre folha) ao custo total
```

#### ANEXO V — Serviços (alta remuneração, Fator-R < 28%)
*TI, publicidade, arquitetura, engenharia, auditoria (quando Fator-R baixo)*
```
Faixa | RBT12                           | Alíq.Nom.| Ded.
  1   | Até R$180.000                   | 15,50%   | R$0
  2   | R$180.001 – R$360.000           | 18,00%   | R$4.500
  3   | R$360.001 – R$720.000           | 19,50%   | R$9.900
  4   | R$720.001 – R$1.800.000         | 20,50%   | R$17.100
  5   | R$1.800.001 – R$3.600.000       | 23,00%   | R$62.100
  6   | R$3.600.001 – R$4.800.000       | 30,50%   | R$540.000
```

---

## 4. LUCRO PRESUMIDO

### Visão geral
```
LIMITE: R$78.000.000/ano (R$6.5M/mês)
OBRIGATÓRIO PARA: nenhum (é opcional abaixo do limite)
VANTAGEM: cálculo simples, sem escrituração LALUR
DESVANTAGEM: paga IR mesmo com prejuízo; PIS/COFINS cumulativos
```

### Percentuais de Presunção IRPJ e CSLL

```
ATIVIDADE                             | IRPJ (%) | CSLL (%)
--------------------------------------|----------|----------
Comércio e indústria                  |    8     |   12
Revenda de combustíveis               |    1,6   |   12
Transporte de cargas                  |    8     |   12
Transporte de passageiros             |   16     |   12
Serviços hospitalares/amb./lab.       |    8     |   12
Serviços em geral                     |   32     |   32
Intermediação de negócios/corretagem  |   32     |   32
Administração, locação de imóveis     |   32     |   32
Factoring                             |   32     |   32
Ativ. financeiras (juros, etc.)       |   100    |  100
Construção civil (mão de obra)        |   32     |   32
Construção civil (materiais incluso)  |    8     |   12

EXCEÇÃO: receita > R$5M → acréscimo de 10pp nos percentuais de presunção
(Regra 2025 — verificar se mantida)
```

### Cálculo do IRPJ no Lucro Presumido
```
PASSO A PASSO (trimestral):

1. Receita Bruta Trimestral = R$___
2. Base IRPJ = R$___ × percentual (ex: 32% para serviços) = R$___
3. IRPJ = R$___ × 15% = R$___
4. Adicional IRPJ = (Base - R$60.000) × 10% = R$___  [se base > R$60K]
5. CSLL = Receita × percentual_CSLL × 9% = R$___

VENCIMENTOS:
  Trimestre Jan-Mar  → DARF até 30/abril
  Trimestre Abr-Jun  → DARF até 31/julho
  Trimestre Jul-Set  → DARF até 31/outubro
  Trimestre Out-Dez  → DARF até 31/janeiro
```

### PIS e COFINS no Lucro Presumido (cumulativo)
```
REGIME CUMULATIVO (sem créditos):
  PIS:    0,65% sobre faturamento bruto
  COFINS: 3,00% sobre faturamento bruto
  TOTAL:  3,65% — SIMPLES, SEM DIREITO A CRÉDITOS

Vencimento: até dia 25 do mês seguinte
```

### Distribuição de Lucros (Lucro Presumido)
```
REGRA ESPECIAL:
Pode distribuir sem imposto (até 2025) o valor:
  = Receita × percentual_presunção - IRPJ - CSLL - outras deduções

OU, se tiver contabilidade completa:
  = Lucro Contábil (o que for maior)

ATENÇÃO 2026: Nova regra de dividendos (PL 1087) aplica acima de R$50K/mês
```

---

## 5. LUCRO REAL

### Obrigatoriedade e visão geral
```
OBRIGATÓRIO SE:
  + Receita > R$78M/ano, OU
  + Bancos, financeiras, seguradoras, leasing, factoring, OU
  + Empresa com lucros/rendimentos/ganhos do exterior, OU
  + Usou benefícios fiscais (isenção ou redução IRPJ), OU
  + Pagou estimativas mensais no ano anterior

VANTAGEM:
  + Paga IR só sobre lucro real (se tiver prejuízo, não paga)
  + PIS/COFINS não-cumulativos (créditos amplos)
  + Pode compensar prejuízos fiscais (limitado a 30%/período)

DESVANTAGEM:
  + Alta complexidade: ECF, ECD, SPED, LALUR, EFD-Contribuições
  + Custo contábil elevado: R$1.500-5.000/mês
```

### LALUR — Livro de Apuração do Lucro Real
```
ESTRUTURA DO LALUR (via ECF):

Lucro Líquido Contábil (antes do IRPJ/CSLL):    R$___
(+) ADIÇÕES: despesas não dedutíveis
    Multas punitivas:                             R$___
    Provisões não dedutíveis:                     R$___
    Brindes/doações (exceto permitidas):          R$___
    Despesas com sócios sem comprovação:          R$___
    15% das despesas com royalties ao exterior:   R$___
(-) EXCLUSÕES: receitas não tributáveis
    Resultado de equivalência patrimonial:        R$___
    Dividendos recebidos (PJ domiciliada no BR):  R$___
    Reversão de provisões não deduzidas:          R$___
(=) LUCRO REAL (Base IRPJ/CSLL):                 R$___

IRPJ = Lucro Real × 15% + (Lucro Real - R$20K/mês) × 10%
CSLL = Lucro Real × 9%
```

### Apuração: Trimestral vs Anual (Estimativa)
```
TRIMESTRAL:
  + Mais simples, paga por período
  - Sem compensação inter-trimestres no mesmo ano
  - Prejuízo de um trimestre não compensa lucro do próximo
  Vencimento: último dia útil do 1º mês após o trimestre

ANUAL (com estimativa mensal):
  + Compensa lucros e prejuízos durante o ano
  + Ajuste final em 31/dezembro
  - Obrigação de pagar estimativa mensalmente (por receita ou balanço)
  Estimativa via RECEITA: Receita × percentual (como Lucro Presumido) × 15%
  Estimativa via BALANÇO: apura lucro real parcial (mais trabalhoso, pode reduzir pagamento)

RECOMENDAÇÃO: Anual quando a empresa tem sazonalidade ou trimestres negativos
```

### PIS e COFINS no Lucro Real (não-cumulativo)
```
REGIME NÃO-CUMULATIVO (com créditos):
  PIS:    1,65% sobre faturamento
  COFINS: 7,60% sobre faturamento
  TOTAL:  9,25% — MAS COM DIREITO A CRÉDITOS

CRÉDITOS (deduzem do PIS/COFINS a pagar):
  - Mercadorias para revenda
  - Insumos de produção (produtos e serviços)
  - Energia elétrica
  - Aluguel de prédios, máquinas, equipamentos
  - Depreciação de máquinas/equipamentos
  - Fretes de vendas

CÁLCULO:
  PIS/COFINS bruto: R$___ × 9,25%    = R$___
  (-) Créditos:                        = R$___
  = PIS/COFINS LÍQUIDO a pagar:        = R$___

ATENÇÃO: Créditos podem tornar PIS/COFINS do Lucro Real MENOR que o
cumulativo do Lucro Presumido para empresas com muito insumo/energia
```

### Compensação de Prejuízos Fiscais
```
REGRA:
  - Prejuízo Fiscal pode ser compensado em períodos futuros
  - LIMITE: 30% do Lucro Real de cada período (trava dos 30%)
  - SEM prazo de validade (diferente do prejuízo contábil)
  - Fica registrado no LALUR Parte B

EXEMPLO:
  Ano 1: Prejuízo Fiscal = -R$500.000 (acumula no LALUR)
  Ano 2: Lucro Real = R$300.000
    Compensação máx.: R$300.000 × 30% = R$90.000
    Lucro Real tributável: R$210.000
    Saldo do prejuízo: R$500.000 - R$90.000 = R$410.000 (fica para Ano 3)
```

---

## 6. EMPRESA DE CAPITAL ABERTO (SA LISTADA)

### Requisitos para IPO e listagem na B3
```
ETAPAS DO IPO:
  1. Decisão e preparação (12-24 meses antes)
     - Contratação de advisors (banco coordenador, advogados, auditores)
     - Migração para IFRS (se ainda não estiver)
     - Reestruturação societária/governança
     - Due diligence completa

  2. Registro na CVM (4-6 meses)
     - Formulário de Referência
     - DFP (3 anos auditados em IFRS)
     - ITR mais recente
     - Pedido de registro de companhia aberta (Categoria A ou B)

  3. Roadshow e precificação (4-8 semanas)
  4. Liquidação e listagem na B3

CUSTOS DO IPO:
  Comissão coordenador/underwriter: 3-5% do valor captado
  Advogados (emissor + underwriter): R$2-6M
  Auditores (KPMG/Deloitte/PwC/EY): R$500K-2M
  CVM + B3 (taxas):                   ~0,5% do valor
  Roadshow/marketing:                 R$300K-1M
  TOTAL TÍPICO:                       R$5-15M para uma captação de R$100M

CUSTOS ANUAIS RECORRENTES (manutenção como SA aberta):
  Auditoria externa: R$1-5M/ano
  RI (Relações com Investidores): R$500K-2M/ano
  Comitê de Auditoria/Conselho: R$300K-1M/ano
  Compliance/CVM: R$200-500K/ano
  TOTAL: R$2-8M/ano
```

### Obrigações contínuas de SA aberta
```
OBRIGAÇÕES PERIÓDICAS (CVM Instrução 480):
  ITR (Info Trimestral):  45 dias após o trimestre (IFRS + notas)
  DFP (Demo Fin. Padron.): 3 meses após 31/dez (IFRS auditado)
  Formulário de Referência: até 5 meses após 31/dez (doc. de 50-100 pgs)
  Fatos relevantes:        imediatamente após ocorrência
  Comunicados ao mercado: previamente a operações material

GOVERNANÇA OBRIGATÓRIA (Novo Mercado B3):
  [ ] Conselho de Administração (mín. 5 membros, 20% independentes)
  [ ] Comitê de Auditoria Estatutário (recomendado)
  [ ] Auditor externo independente (Big Four ou equivalente)
  [ ] Política de divulgação de informações
  [ ] Código de conduta público
  [ ] Tag along: 100% para ações ordinárias
  [ ] Free float mínimo: 25%
  [ ] Apenas ações ordinárias (ON) no Novo Mercado

SEGMENTOS B3:
  Novo Mercado:  maior governança, maior liquidez
  Nível 2:       permite PN com direitos extras
  Nível 1:       free float mínimo 25%
  Bovespa Mais:  PMEs (menor volume)
  SOMA:          empresas médias

TRIBUTAÇÃO SA ABERTA:
  Mesma do Lucro Real (obrigatório ou presumido se < R$78M)
  Ganho de capital em venda de ações:
    - Pessoa física: isento até R$20K/mês; acima: 15-22,5%
    - Pessoa jurídica: tributado normalmente pelo regime da PJ
  JCP (Juros sobre Capital Próprio):
    - IRRF 15% sobre valor pago
    - Dedutível da base IRPJ/CSLL
    - Limitado a TJLP × Patrimônio Líquido
```

---

## 7. EMPRESA DE CAPITAL ESTRANGEIRO

### Registro obrigatório — BACEN/RDE-IED
```
RDE-IED: Registro Declaratório Eletrônico — Investimento Estrangeiro Direto
  Sistema: SISBACEN → módulo RDE-IED
  Prazo: 30 dias após a integralização do capital
  Quem declara: empresa brasileira receptora do investimento
  Obrigação: sempre que houver aporte, lucro retido, ou transferência

DCBE (Declaração de Capitais Brasileiros no Exterior):
  Para empresas BR que TÊM ativos no exterior
  Prazo: anualmente até 5 de abril
  Obrigatório se: ativos > USD 1 milhão
  Multa por omissão: R$1.500 a R$250.000

CBE ANUAL: R$1 a 100M → até 5/abril
CBE TRIMESTRAL: > R$100M → trimestral
```

### Tributação de dividendos para não-residentes
```
HISTÓRICO (até 31/12/2025):
  - Lucros e dividendos de resultados a partir de 01/01/1996: ISENTOS de IRRF
  - Remessa ao exterior: livre, sem restrição

MUDANÇA 2026 (Lei nº 15.270/2025 — PL 1087):
  - Dividendos > R$50.000/mês para não-residentes: IRRF 10%
  - Aplica-se a lucros apurados a partir de 01/01/2026
  - Tratados contra dupla tributação podem reduzir a alíquota
  (Brasil tem tratados com: Japão, Holanda, França, Suécia, etc.)

ROYALTIES E SERVIÇOS TÉCNICOS (remessa ao exterior):
  IRRF padrão: 15%
  Por tratado: pode ser 10% ou menos
  CIDE-Tecnologia: 10% (sobre royalties/serviços técnicos)
  IOF sobre câmbio: 0,38%

JUROS SOBRE EMPRÉSTIMO EXTERIOR:
  IRRF: 15% (padrão)
  Para paraísos fiscais: 25%
  Thin Capitalization: razão máxima D/E 2:1 (geral) ou 0.3:1 (paraíso)
```

### Transfer Pricing — Novas Regras OCDE (vigência 2024)
```
CONTEXTO:
  Antes (até 2023): regras brasileiras próprias, muito divergentes da OCDE
  A partir de 2024: alinhamento ao padrão OCDE (arm's length)

PRINCÍPIO ARM'S LENGTH:
  Transações entre partes relacionadas devem ser feitas
  como se fossem partes independentes de mercado.

QUEM É AFETADO:
  - Empresas com matriz/subsidiária no exterior
  - Exportações/importações entre empresas do mesmo grupo
  - Pagamentos de royalties, licenças, serviços para o grupo
  - Contratos de financiamento intragrupo

MÉTODOS ACEITOS (OCDE):
  CUP: Preço comparável não controlado
  RPM: Método de preço de revenda
  CPM: Método de custo mais lucro
  TNMM: Margem líquida da transação
  PSM: Método de divisão de lucro

DOCUMENTAÇÃO OBRIGATÓRIA (Instrução Normativa RFB):
  - Masterfile (informações do grupo)
  - Local File (empresa brasileira)
  - Country-by-Country Report (grupos > R$2.26B)
  Prazo: junto com ECF anual

MULTAS: 75% sobre diferença (dolo/fraude: 150%)
```

### Estrutura societária com capital estrangeiro
```
VEÍCULOS COMUNS:
  LTDA: mais usado (simples, flexível)
  SA:   necessário para captação pública ou BNDES
  SCP:  Sociedade em Conta de Participação (investidor oculto)

CAPITAL MÍNIMO: não há obrigação legal geral
  (exceto para setores regulados: bancos, seguradoras, etc.)

INCENTIVOS PARA CAPITAL ESTRANGEIRO:
  - Tratados de Investimento (TBIs): proteção contra expropriação
  - Zonas de Processamento de Exportação (ZPE): incentivos fiscais
  - Regimes especiais BNDES: acesso a financiamentos
  - Parque tecnológico/startup: benefícios setoriais

RESTRIÇÕES SETORIAIS (capital estrangeiro limitado/vedado):
  × Rádio e TV: vedado
  × Jornais e revistas: vedado estrangeiros diretos
  × Empresas aéreas: limitado a 49% estrangeiro (salvo exceção)
  × Terras rurais/fronteira: restrições
  × Saúde: restrições (hospitais podem)
  × Mineração: permite, mas com restrições
```

---

## 8. CNAE × REGIME TRIBUTÁRIO

### Lógica de escolha do CNAE correto
```
CNAE PRINCIPAL: atividade que gera maior receita
CNAE SECUNDÁRIO: atividades complementares (pode ter vários)

IMPACTO DO CNAE:
  1. Define se pode entrar no Simples Nacional
  2. Define qual ANEXO do Simples (I, II, III, IV ou V)
  3. Define alíquota do ISS (municipal — CNAE de serviço)
  4. Define regime ICMS (estadual — CNAE de comércio/indústria)
  5. Define NF a emitir: NF-e (produto) vs NFS-e (serviço)
  6. Define licenças e alvarás necessários
```

### CNAEs vedados no Simples Nacional (categorias)
```
CATEGORIA                      | EXEMPLOS DE CNAE VEDADO
-------------------------------|-------------------------------------------
Financeiro                     | Bancos, financeiras, seguros, previdência
Cooperativas (exceto crédito)  | 9430-8, 9412-0
Sindicatos e associações       | 9420-1, 9492-8
Partidos políticos             | 9491-0
Organizações religiosas        | 9491-0
Algumas profissões reg.        | Consultar lista RFB (leilão, notarial)
Álcool combustível             | CNAEs de distribuição
Importação de cigarros         | CNAEs específicos
Holding PJ com participação    | Empresa com outra PJ como sócia

COMO VERIFICAR:
  Portal Simples Nacional → Consulta CNAE:
  receita.fazenda.gov.br/SimplesNacional → Serviços → CNAE

ATIVIDADE MISTA (múltiplos CNAEs):
  Regra: cada atividade paga pelo seu ANEXO correspondente
  DAS é calculado proporcionalmente por atividade
  Se CNAE principal vedado: empresa INTEIRA fica fora do Simples
```

### Mapa CNAE × Anexo (principais atividades)
```
ATIVIDADE                                   | ANEXO  | FATOR-R?
--------------------------------------------|--------|----------
Comércio varejista (loja, e-commerce)       |  I     | Não
Fabricação/indústria                        |  II    | Não
Instalação/manutenção/reparos               |  III   | Não
Academias/salão de beleza/lavanderia        |  III   | Não
Medicina/odontologia/veterinária            |  III   | Não
Serviços de TI/software (folha ≥ 28%)      |  III   | Sim
Transporte rodoviário de cargas             |  III   | Não
Construção civil (com materiais)            |  II    | Não
Construção civil (só mão de obra)          |  IV    | Não
Vigilância/segurança/limpeza               |  IV    | Não
Advocacia                                   |  IV    | Não
Serviços de TI/software (folha < 28%)      |  V     | Sim
Publicidade/propaganda (folha < 28%)        |  V     | Sim
Arquitetura/engenharia (folha < 28%)        |  V     | Sim
Auditoria/contabilidade (folha < 28%)       |  V     | Sim
Jornalismo/comunicação (folha < 28%)        |  V     | Sim
```

---

## 9. CLT × REGIME TRIBUTÁRIO

### Encargos por regime — comparativo completo
```
ENCARGO                    | SIMPLES NACIONAL | LUCRO PRES./REAL
---------------------------|------------------|------------------
INSS Patronal (CPP)        | INCLUSO no DAS   | 20% sobre folha
RAT/SAT (acidente trab.)   | INCLUSO no DAS   | 1-3% sobre folha
Terceiros (SESC/SENAC etc) | INCLUSO no DAS   | 5,8% sobre folha
SUBTOTAL PATRONAL INSS     | INCLUSO          | ~26,8-28,8%
FGTS                       | 8%               | 8%
FGTS multa rescisão (prov.)| 4%               | 4%
13º salário (provisão)     | 8,33%            | 8,33%
Férias (1/3 inc.) (prov.)  | 11,11%           | 11,11%
TOTAL ENCARGOS S/ SALÁRIO  | ~31% (simplific.)| ~58-62%

CUSTO REAL DO FUNCIONÁRIO:
Simples: salário bruto × 1,31 (+ benefícios)
Lucro Real/Pres.: salário bruto × 1,60-1,80 (+ benefícios)

BENEFÍCIOS OBRIGATÓRIOS (todos os regimes):
  Vale-transporte: custo empresa = valor - 6% do salário do funcionário
  Vale-refeição: não obrigatório por lei (exceto se CCT exige)
  Plano de saúde: não obrigatório (mas custo se CCT exige)
```

### CPRB — Contribuição Previdenciária sobre Receita Bruta
```
O QUE É: Substitui INSS patronal 20% por alíquota sobre faturamento
VIGÊNCIA: criada em 2011, prorrogada, extinção gradual até 2028
QUEM PODE USAR: 17 setores específicos (opt-in por decreto)

SETORES BENEFICIADOS (principais):
  Tecnologia da Informação:          2,5%
  Call Center:                       2%
  Comunicação:                       2%
  Construção Civil:                  4,5%
  Calçados e têxteis:                1%
  Manutenção e reparação naval:      3,5%
  Confecção e vestuário:             1%
  Fabricação de automóveis:          1,5%

QUANDO VANTAJOSO:
  CPRB% sobre receita < INSS 20% sobre folha
  Exemplo: empresa tech com receita R$500K e folha R$50K
    INSS tradicional: R$50K × 20% = R$10K/mês
    CPRB 2,5%: R$500K × 2,5% = R$12,5K/mês
    → Neste caso, INSS tradicional é mais barato
    → Verificar ponto de equilíbrio: receita/folha = 8x (para tech 2,5%)

CRONOGRAMA DE EXTINÇÃO (2025-2028):
  2025: alíquota base mantida
  2026: início da transição gradual
  2028: retorno integral ao sistema normal (20% folha)
```

### eSocial e obrigações trabalhistas digitais
```
ESOCIAL — obrigações:
  S-2200: admissão de empregado
  S-2206: alteração de contrato
  S-2299: desligamento
  S-1200: folha de pagamento
  S-1210: pagamentos
  S-2400: benefício previdenciário
  Prazo: vencimentos variáveis por evento (maioria antes do fato)

PRAZOS CRÍTICOS:
  Admissão: informar ATÉ 1 dia antes do início do trabalho
  Folha: até dia 7 do mês seguinte (ou dia 20 para pequenas)
  Rescisão: 10 dias corridos após o aviso-prévio

MULTAS (CLT + eSocial):
  Admissão sem registro: R$3.000 + R$1.500/mês por empregado
  FGTS não recolhido: 100% do valor + SELIC + multa 50%
  GFIP/eSocial com erro: R$20/registro errado (mín. R$500)
```

### Pró-labore — regras definitivas 2026
```
OBRIGATORIEDADE:
  - Sócio-administrador que exerce atividade: OBRIGATÓRIO
  - Sócio que não trabalha (apenas investidor): não obrigatório

VALOR MÍNIMO:
  - Não há valor mínimo legal explícito
  - Recomendado: salário mínimo vigente (R$1.518 em 2025)
  - Prática: 1-2 salários mínimos para não chamar atenção da RF

INSS DO SÓCIO (sobre o pró-labore):
  Alíquota: 11% (código de recolhimento 1872)
  Teto: contribuição máxima ~R$932/mês (teto INSS 2025: ~R$8.157 bruto)

IR DO SÓCIO (sobre o pró-labore) — NOVA REGRA 2026:
  Isenção até R$5.000/mês (Lei 15.270/2025)
  Desconto gradual R$5.001 a R$7.350/mês
  Tabela progressiva normal acima de R$7.350:
    Até R$2.259: 0%
    R$2.260 – R$2.826: 7,5%
    R$2.827 – R$3.751: 15%
    R$3.752 – R$4.664: 22,5%
    Acima R$4.664: 27,5%

ESTRATÉGIA ÓTIMA 2026:
  - Mínimo de pró-labore = salário mínimo (INSS + isento de IR)
  - Dividendos até R$50K/mês por sócio (isentos)
  - Acima de R$50K/mês: 10% IRRF sobre o excedente
  - Para sócios de alta renda: estrutura com holding + planejamento
```

---

## 10. TÓPICOS ESPECIAIS

### ICMS — Substituição Tributária (ST)
```
O QUE É: Uma empresa da cadeia (geralmente o fabricante/importador)
         recolhe o ICMS de TODA a cadeia antecipadamente.

COMO FUNCIONA:
  Fabricante → Distribuidor → Varejista
       ↑
  Recolhe ICMS por todos (via ST)

IMPACTO NO SIMPLES NACIONAL:
  Produtos com ST: empresa Simples NÃO paga ICMS pelo DAS
  (já foi pago pelo substituto tributário)
  DAS é recalculado excluindo o % de ICMS do Simples

SETORES COMUNS COM ST:
  Combustíveis, cigarros, bebidas, autopeças, material de construção,
  medicamentos, produtos de higiene, eletrodomésticos (por estado)

MVA (Margem de Valor Agregado):
  Define a base do ICMS-ST = Preço do fabricante × (1 + MVA%)
  Varia por produto e por estado (convênios CONFAZ)

RESTITUIÇÃO: Se o produto é vendido abaixo da base ST,
             pode haver restituição do ICMS-ST excedente (varia por estado)
```

### ISS Fixo — Sociedades Uniprofissionais
```
O QUE É: Tributação fixa de ISS por profissional habilitado,
         independente do faturamento.

QUEM PODE:
  Sociedades de profissionais (não empresariais, sem caráter empresarial)
  Médicos, dentistas, advogados, engenheiros, arquitetos, psicólogos,
  fisioterapeutas, contadores, economistas

VALOR: por profissional habilitado (varia por município)
  Exemplo SP: ~R$200-600/mês por profissional
  Versus ISS normal: 2-5% sobre faturamento

VANTAGEM BRUTAL:
  Empresa com 3 médicos faturando R$300K/mês:
  ISS normal (3%): R$9.000/mês
  ISS fixo (3 × R$500): R$1.500/mês
  ECONOMIA: R$7.500/mês = R$90.000/ano

CONDIÇÕES:
  - Todos os sócios devem ser profissionais habilitados na mesma área
  - Não pode ter caráter empresarial (não pode explorar mão de obra em escala)
  - Forma jurídica: Sociedade Simples (não LTDA empresarial, em alguns municípios)
  - Debate jurídico: LTDAs uniprofissionais ainda é caso a caso por município
```

### Lucro Arbitrado — quando e como
```
QUANDO É APLICADO:
  Pela Receita Federal quando a empresa:
  - Não tem escrituração contábil adequada (Lucro Real obrigatório)
  - Recusou exame da documentação fiscal
  - Tem omissão de receitas (>90% do total)
  - Livros ilegíveis, extraviados, deteriorados

PELO CONTRIBUINTE (voluntário):
  Quando não tem como apurar o Lucro Real no prazo

PERCENTUAIS DE ARBITRAMENTO (base sobre receita conhecida):
  Mais 20% sobre os percentuais do Lucro Presumido
  Comércio/indústria: 9,6% (8% × 1,2)
  Serviços: 38,4% (32% × 1,2)
  Transporte: 19,2% (16% × 1,2)

CONSEQUÊNCIA: É punição + custo maior. EVITAR.
  Diferença vs Lucro Presumido: +20% na base = ~20% mais IRPJ/CSLL
```

---

## 11. COMPARATIVO FINAL — DECISOR DE REGIME

```
ÁRVORE DE DECISÃO:

É MEI (solo, até R$81K/ano)?
  → MEI ← mais simples do mundo

Fatura > R$78M/ano OU é banco/financeira?
  → LUCRO REAL (obrigatório)

Tem sócio PJ ou CNAE vedado?
  → Lucro Presumido ou Real (fora do Simples)

Fatura ≤ R$4.8M E CNAE permitido?
  → Calcular Simples vs Presumido:

  SIMPLES ganha se:
    Anexo I (comércio): alíquota efetiva < Presumido (8%IRPJ+3.65%PIS-COFINS+INSS)
    Anexo III (serviço): alíquota < 16-18% total
    Quando folha de pagamento é alta (INSS patronal incluso)

  PRESUMIDO ganha se:
    Margem bruta muito alta (>50-60%) em serviços (base CSLL/IRPJ 32% mas baixa)
    Poucos funcionários, baixa folha
    Faturamento próximo a R$4.8M (Simples vira muito caro)
    Sócio quer distribuir grandes lucros isentos

  LUCRO REAL ganha se:
    Margem bruta baixa (<10-15%)
    Grande volume de insumos (créditos PIS/COFINS)
    Prejuízo para compensar
    Benefícios fiscais específicos (Lei do Bem, etc.)

PLANILHA DE DECISÃO (por R$100K de faturamento mensal, serviços):
Regime          | DAS/IRPJ | PIS/COFINS | INSS Pat. | TOTAL
Simples Anexo III| R$14.100 | incluso    | incluso   | ~14%
Simples Anexo V  | R$20.500 | incluso    | incluso   | ~20%
Lucro Presumido  | R$5.500  | R$3.650    | R$6.000   | ~15%
Lucro Real (30%) | R$3.600  | R$4.625*  | R$6.000   | ~14%
                                          *após créditos
```

---

## 12. ARMADILHAS E CHECKLIST DE AUDITORIA TRIBUTÁRIA

```
TOP 10 ARMADILHAS:
1. CNAE errado: empresa no Simples mas CNAE vedado → desenquadramento retroativo
2. Sócio PJ: qualquer PJ como sócia → exclusão do Simples
3. Fator-R não monitorado: empresa no Anexo V sem precisar (paga mais)
4. Distribuição de lucros sem lucro contábil → pró-labore disfarçado → INSS
5. Ultrapassagem do limite Simples (> R$4.8M): exclusão retroativa em janeiro
6. Transfer Pricing (2024+): transações intragrupo sem documentação → multa 75%
7. Capital estrangeiro sem registro BACEN → multa R$1.500 a R$250.000
8. Dividendos ao exterior em 2026 sem retenção 10% → autuação automática
9. CPRB sendo usada por setor não elegível → diferença + multa 75%
10. eSocial atrasado: admissão antes de comunicar → R$3.000 por empregado

CHECKLIST ANUAL DE CONFORMIDADE:
Regime:
[ ] Regime tributário está correto para o faturamento atual?
[ ] CNAE principal e secundários atualizados?
[ ] Fator-R calculado (se Simples III/V)?
[ ] Declarações entregues: DEFIS, ECF, ECD, DIRF, DCTF?

Trabalhista:
[ ] Todos os funcionários com registro atualizado no eSocial?
[ ] FGTS em dia (GFIP/eSocial)?
[ ] Pró-labore sendo pago e INSS recolhido?

Capital estrangeiro:
[ ] RDE-IED atualizado no SISBACEN?
[ ] DCBE entregue (se aplicável)?
[ ] Transfer Pricing documentado (Masterfile + Local File)?

Fiscal:
[ ] NF emitida antes do recebimento (sempre)?
[ ] ICMS-ST calculado corretamente (se comércio)?
[ ] Contribuições previdenciárias em dia?
```

---

## FONTES E REFERÊNCIAS

```
LEGISLAÇÃO PRIMÁRIA:
- LC 123/2006: Estatuto das ME/EPP (Simples Nacional)
- Lei 9.718/1998: Lucro Presumido
- RIR/2018 (Decreto 9.580): Regulamento do IR
- IN RFB 1.700/2017: IRPJ e CSLL
- Lei 6.404/1976: SA (Lei das S.A.)
- Lei 15.270/2025: Nova tributação dividendos (PL 1087)
- LC 214/2025: Reforma tributária CBS/IBS
- IN RFB 2.161/2023: Transfer Pricing (OCDE)

PORTAIS:
- receita.fazenda.gov.br/SimplesNacional
- cvm.gov.br (obrigações SA aberta)
- bcb.gov.br (SISBACEN/RDE)
- esocial.gov.br
- sped.rfb.gov.br

FERRAMENTAS:
- Simulador Simples Nacional (Receita Federal)
- calculadorabrasil.com.br (IRPJ/CSLL)
- SEBRAE planilhas (sebraepr.com.br/planilhas)
- kaue34381210/calculadora-fiscal (GitHub, Python CLI)
- rogeramorim7/calculadora-impostos-br-streamlit (GitHub, Streamlit)
```
