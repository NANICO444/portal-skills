# SKILL: Brazil Tax Reform 2026-2032 — Guia Completo
# Versao: 1.0.0 | Para: modules_strategy, modules_data, modules_personal_v2 | Fase: 3-5
# Criada em: 2026-05-17 | Sessao: sess_20260517_2226_biz
# Base Legal: EC 132/2023, LC 214/2025, PL 1087/2025
# Pesquisa: Tavily (2026-05-17) — acompanhar regulamentacoes do Comite Gestor do IBS

---

## QUANDO USAR
- Ao planejar qualquer empresa que terá contratos de médio-longo prazo (2026-2033)
- Ao calcular precificação de produtos/serviços para os próximos 7 anos
- Ao estruturar sócios e distribuição de lucros (impacto IRPF Mínimo)
- Ao revisar cláusulas tributárias de contratos existentes
- Ao auditar se a empresa está preparada para a transição fiscal

---

## 1. VISÃO GERAL DA REFORMA TRIBUTÁRIA

```
BASE LEGAL: Emenda Constitucional 132/2023 + Lei Complementar 214/2025
ESCOPO: Maior reforma tributária brasileira desde a CF/1988
PERÍODO: Transição 2026-2032, sistema novo pleno a partir de 2033

O QUE MUDA:
  SISTEMA ATUAL (até 2025)         → SISTEMA NOVO (pleno em 2033)
  ─────────────────────────────────────────────────────────────
  PIS (federal)         }          → CBS — Contribuição sobre
  COFINS (federal)      } → CBS      Bens e Serviços (federal)
  ─────────────────────────────────────────────────────────────
  ICMS (estadual)       }          → IBS — Imposto sobre Bens
  ISS (municipal)       } → IBS      e Serviços (estadual/munic)
  ─────────────────────────────────────────────────────────────
  IPI (federal)         → IMPOSTO SELETIVO (IS) parcialmente
                          (mantido para ZFM; IS cobre setor específico)

NOVIDADE: IMPOSTO SELETIVO (IS)
  Imposto extrafiscal federal sobre bens/serviços prejudiciais à saúde
  ou ao meio ambiente. NÃO substitui ICMS/ISS — é um tributo adicional.
  Incide sobre: tabaco, bebidas alcoólicas/açucaradas, veículos (por
  emissão de carbono/potência), bens minerais.
```

---

## 2. CRONOGRAMA OFICIAL DE TRANSIÇÃO (2026-2033)

```
ANO   | CBS    | IBS ESTADO | IBS MUNI | PIS/COFINS | ICMS | ISS  | FASE
------|--------|------------|----------|------------|------|------|------
2026  | 0,90%  | 0,05%      | 0,05%    | mantido    | mant.| mant.| TESTE
2027  | CBS*   | 0,05%      | 0,05%    | EXTINTO    | mant.| mant.| CBS plena
2028  | CBS    | 0,05%      | 0,05%    | —          | mant.| mant.| CBS plena
2029  | CBS    | -10% ICMS  | -10% ISS | —          | -10% | -10% | Transição
2030  | CBS    | -20% ICMS  | -20% ISS | —          | -20% | -20% | Transição
2031  | CBS    | -40% ICMS  | -40% ISS | —          | -40% | -40% | Transição
2032  | CBS    | -60% ICMS  | -60% ISS | —          | -60% | -60% | Transição
2033  | CBS    | IBS pleno  | IBS pleno| —          | ZERO | ZERO | COMPLETO

*CBS plena: alíquota a ser definida pelo Comitê Gestor (estimativa: 8-9%)
*IBS pleno: soma estados + municípios (estimativa: 17-19% total combinado)
*Alíquota referência total (CBS+IBS): estimativa ~25-28% (detalhe abaixo)

ATENÇÃO 2026 — DUPLA OBRIGAÇÃO:
  Em 2026 a empresa PAGA ambos os sistemas simultaneamente:
  → PIS + COFINS (sistema antigo, alíquotas normais)
  → CBS 0,9% + IBS 0,1% (sistema novo, alíquota de teste)
  → O governo concede crédito tributário do pagamento duplo
  Impacto no caixa: provisionar 1% extra sobre faturamento em 2026

FGTS e folha: NÃO são afetados pela reforma (INSS/CLT mantidos)
```

---

## 3. CBS — CONTRIBUIÇÃO SOBRE BENS E SERVIÇOS

```
NATUREZA: Federal (substitui PIS e COFINS)
GESTÃO: Receita Federal do Brasil
ALÍQUOTA 2026: 0,90% (fase de teste)
ALÍQUOTA PLENA (estimativa): 8-9% sobre receita bruta

MODELO: IVA (Imposto sobre Valor Agregado) — não cumulativo
  → Empresa cobra CBS nas vendas
  → Empresa se credita de CBS paga nas compras (insumos, serviços)
  → Recolhe apenas a DIFERENÇA (CBS saídas - CBS entradas)

COMPARAÇÃO COM PIS/COFINS ATUAL:
  PIS/COFINS atual (Lucro Real, não cumulativo): 9,25%
  CBS estimada: 8-9%
  → Aparentemente similar, mas a BASE de crédito é muito mais ampla

CRÉDITOS CBS — MUITO MAIS AMPLOS QUE PIS/COFINS:
  Permitem crédito de CBS sobre:
  [ ] Insumos diretos (como hoje)
  [ ] Serviços contratados (AMPLIADO — antes havia restrições)
  [ ] Aluguel de imóveis para operação (NOVO)
  [ ] Energia elétrica (NOVO — antes vedado)
  [ ] Fretes (AMPLIADO)
  [ ] Ativos imobilizados (crédito imediato ou parcelado — AMPLIADO)
  [ ] Telecom e internet usados no negócio (NOVO)

IMPACTO NA MARGEM POR SETOR:
  Setor com muita compra de insumos (indústria, varejo físico):
    → Mais créditos → CBS efetiva MENOR que PIS/COFINS atual
    → BENEFICIADOS pela reforma

  Setor de serviços com poucos insumos (profissional liberal, SaaS):
    → Menos créditos → CBS pode ser MAIOR que ISS atual (2-5%)
    → PREJUDICADOS — precificação deve ser revisada

  Alimentos e medicamentos: REDUÇÃO DE 60% na alíquota CBS
    → Alíquota reduzida: ~3,2-3,6%

ALÍQUOTAS SETORIAIS CBS (aplicação das reduções constitucionais):
  Categoria                              | Redução | Alíquota efetiva estimada
  ---------------------------------------|---------|---------------------------
  Alimentos (cesta básica nacional)      | 100%    | ZERO (isento)
  Medicamentos essenciais                | 60%     | ~3,2-3,6%
  Saúde e educação                       | 60%     | ~3,2-3,6%
  Transporte público coletivo            | 100%    | ZERO
  Bens do agronegócio (in natura)        | 100%    | ZERO
  Insumos agropecuários                  | 60%     | ~3,2-3,6%
  Bens de capital                        | A definir regulamentação
  Serviços em geral                      | 0%      | ~8-9% (alíquota plena)
  Software, TI, SaaS                     | 0%      | ~8-9% (ISS era 2-5%)
```

---

## 4. IBS — IMPOSTO SOBRE BENS E SERVIÇOS

```
NATUREZA: Subnacional (substitui ICMS estadual + ISS municipal)
GESTÃO: Comitê Gestor do IBS (novo ente criado pela EC 132/2023)
ALÍQUOTA 2026: 0,10% (fase de teste: 0,05% estado + 0,05% município)
ALÍQUOTA PLENA (estimativa): 17-19% (soma estado + município)

PRINCÍPIO: DESTINO (não mais origem)
  Hoje (ICMS/ISS): tributo vai para o estado/município de ORIGEM
  Com IBS: tributo vai para o estado/município de DESTINO (onde está o consumidor)

IMPACTO DO PRINCÍPIO DE DESTINO:
  Empresa que vende para todo o Brasil:
    → Hoje: recolhe ICMS para o estado onde está sediada
    → 2033: recolhe IBS para cada estado/município dos clientes
  → Elimina guerra fiscal entre estados
  → Elimina necessidade de DIFAL (diferencial de alíquota)
  → Elimina benefícios de ICMS de alguns estados — impacto nas filiais

SPLIT PAYMENT (mecânica de arrecadação):
  Inovação crítica da reforma:
  → Quando o pagamento é processado (cartão, PIX, boleto),
    o IBS e CBS são automaticamente desviados para o fisco
  → A empresa NÃO recebe o tributo e depois paga — já é separado na fonte
  → Impacto no fluxo de caixa: empresa não usa tributo como capital de giro
  → CAIXA REDUZIDO comparado com sistema atual (ICMS a recolher era giro)

COMITÊ GESTOR DO IBS:
  Novo ente federativo criado para administrar o IBS
  Composto por: 27 estados + 5.570 municípios (representados)
  Responsável por: regulamentação, fiscalização, contencioso do IBS
  → Implica uniformização das regras — fim de conflitos estado vs município
```

---

## 5. IMPOSTO SELETIVO (IS)

```
NATUREZA: Federal, extrafiscal (objetivo é desestimular, não arrecadar)
BASE LEGAL: Art. 153, VIII da CF/1988 (inserido pela EC 132/2023)

BENS E SERVIÇOS SUJEITOS AO IS:
  Categoria                  | Alíquota prevista
  ---------------------------|------------------
  Produtos fumígenos         | Alta (a regulamentar)
  Bebidas alcoólicas         | Moderada-alta
  Bebidas açucaradas         | Moderada
  Veículos automotores       | Baseado em emissão CO2 + potência + ef. energética
  Embarcações e aeronaves    | A regulamentar
  Bens minerais              | Baixa (zero se insumo industrial)
  Jogos/apostas              | A regulamentar (inclui bets online)

IMPORTANTE: IS incide SOBRE o IBS e CBS (entra na base de cálculo)
  → Efeito cascata: IS aumenta a base para IBS e CBS
  → Impacto real no preço final é maior que a alíquota nominal do IS

IMPACTO NO AGRONEGÓCIO:
  Defensivos agrícolas: potencialmente sujeitos ao IS
  (em discussão na regulamentação — pressão do setor)

IMPACTO EM VEÍCULOS:
  Carro zero (combustão): IS baseado em emissão CO2
  Veículo elétrico: IS reduzido ou zero
  → Tendência: encarecimento de combustão, incentivo a EVs
```

---

## 6. PL 1087/2025 — IRPF MÍNIMO E TRIBUTAÇÃO DE DIVIDENDOS

```
BASE LEGAL: PL 1087/2025 (aprovado na Câmara, em análise Senado)
VIGÊNCIA: A partir de 1º de janeiro de 2026

---

### 6.1 ISENÇÃO IRPF ATÉ R$5.000/MÊS

  Renda mensal tributável | Situação
  ------------------------|------------------------
  Até R$5.000/mês         | ISENTO de IRPF
  R$5.001 a R$7.000/mês   | Desconto progressivo (redução gradual)
  Acima de R$7.000/mês    | Tabela progressiva normal (até 27,5%)

  Impacto: ~16 milhões de brasileiros que hoje pagam IR deixam de pagar.
  Custo fiscal estimado: R$25-35 bilhões/ano para a União.

---

### 6.2 IRPF MÍNIMO (para renda > R$600.000/ano = R$50.000/mês)

CONCEITO:
  Toda pessoa física com renda total acima de R$600.000/ano
  deve pagar IRPF de no mínimo 10% sobre toda a renda
  (incluindo dividendos, JCP, rendimentos isentos).

  CÁLCULO DO IRPF MÍNIMO:
  1. Calcule 10% de toda a renda (inclusive isentos, dividendos)
  2. Subtraia o IRPF que já pagou normalmente (salário, aluguéis, etc.)
  3. A diferença (se positiva) é o IRPF Mínimo a pagar

  EXEMPLO:
  Sócio com renda total de R$1.200.000/ano:
    → Pró-labore: R$120.000/ano → IRPF já pago: ~R$27.000
    → Dividendos: R$1.080.000/ano → antes IRPF = R$0
    → IRPF Mínimo devido: R$1.200.000 × 10% = R$120.000
    → IRPF já pago: -R$27.000
    → IRPF Mínimo a complementar: R$93.000/ano

---

### 6.3 IRRF 10% SOBRE DIVIDENDOS (retenção na fonte)

  REGRA:
  Dividendos pagos a pessoas físicas acima de R$50.000/mês:
  → IRRF de 10% na fonte (empresa retém na hora do pagamento)
  → O valor retido entra como crédito no cálculo do IRPF Mínimo anual

  DIVIDENDOS ATÉ R$50.000/MÊS: ainda isentos (IRRF = 0%)

  TABELA PRÁTICA:
  Distribuição mensal | IRRF na fonte | Observação
  --------------------|---------------|---------------------------
  Até R$50.000        | 0%            | Mantida isenção histórica
  R$50.001 a R$99.999 | 10% s/ excedente | Só sobre o que ultrapassar
  R$100.000+          | 10% s/ total  | Retido na fonte

---

### 6.4 ESTRATÉGIAS DE ADAPTAÇÃO 2026+

  ESTRATÉGIA 1 — Manter distribuição até R$50.000/mês por sócio
    → Abaixo do gatilho do IRRF 10%
    → Para sócios com renda total < R$600K/ano: sem IRPF Mínimo
    → Mais sócios na empresa pode distribuir mais sem imposto

  ESTRATÉGIA 2 — Reinvestimento ao invés de distribuição
    → Lucro reinvestido na empresa: sem IRPF
    → Empresa pode fazer reservas, expandir ou pagar dividendos futuros
    → Especialmente útil se empresa tem plano de crescimento

  ESTRATÉGIA 3 — Estrutura via Holding
    → Dividendos de PJ para PJ: ISENTOS (participation exemption)
    → Sócio recebe lucro da holding sem passar pelo IRRF
    → ATENÇÃO: IRPF Mínimo ainda incide sobre a renda total (incluindo
      dividendos distribuídos da holding para o sócio PF)

  ESTRATÉGIA 4 — Pró-labore otimizado vs dividendo
    → Com IRPF Mínimo, a vantagem do dividendo cai para renda >R$600K/ano
    → Calcular ponto de indiferença fiscal individualmente com contador

  ESTRATÉGIA 5 — JCP (Juros sobre Capital Próprio)
    → JCP: 15% IRRF na fonte (sem alteração no PL 1087)
    → Para Lucro Real: JCP dedutível do IRPJ → reduz base de cálculo
    → Em alguns casos, JCP pode ser mais eficiente que dividendo

  CÁLCULO DO PONTO DE INDIFERENÇA (2026):
  Via dividendo > R$50K/mês: 10% IRRF + IRPF Mínimo potencial
  Via pró-labore: tabela progressiva (15% ou 27,5%) + INSS 11%
  → Para renda total entre R$600K-R$1,2M/ano: análise case a case
  → Para renda total > R$1,2M/ano: diferença entre estratégias cai
```

---

## 7. IMPACTO POR REGIME/SETOR

```
SETOR / REGIME     | ANTES (2025)  | DEPOIS (2033) | IMPACTO | AÇÃO
-------------------|---------------|---------------|---------|---------------------
Serviços digitais  | ISS 2-5%      | CBS+IBS ~26%  | ALTO +  | Revisar preços AGORA
(SaaS, Plataformas)|               |               | pressão | para contratos longos

Varejo físico/e-com| ICMS 12-18%   | IBS ~17-19%   | NEUTRO/ | Calcular créditos novos
                   | + PIS/COFINS  | + CBS ~8-9%   | MELHOR  | em frete, energia, logist

Industria geral    | IPI+ICMS+PIS/ | CBS+IBS+IS    | MELHOR  | Maximizar créditos CBS
                   | COFINS        | mais créditos |         | em toda cadeia produtiva

Agronegócio        | Isento em geral| Isenção manut.| NEUTRO/ | Atenção ao IS em
                   |               | na maioria    | CUIDADO | defensivos — regulament

Imobiliário        | ISS 2-5% cons.| CBS+IBS pleno | ALTO +  | Contratos futuros:
                   | ICMS obras    |               | INCERTO | incluir cláusula de reajuste

Profissional liberal| ISS 2-5%     | CBS+IBS pleno | ALTO +  | Precificação de serviços
(médico, adv, eng) |               | ~26%          | pressão | deve subir gradualmente

Simples Nacional   | DAS (incluso) | DAS mantido   | CUIDADO | Em 2027 avaliar se
                   |               | + opção CBS   | ATENÇÃO | fica no DAS ou opta CBS/IBS

Exportação         | Imune ICMS/ISS| Mantida imun. | NEUTRO/ | Créditos CBS em insumos
                   |               | para exportac.| MELHOR  | serão amplos — vantagem
```

---

## 8. SIMPLES NACIONAL NA REFORMA

```
O SIMPLES NACIONAL NÃO É EXTINTO. O DAS continua existindo.

SITUAÇÃO EM 2026 (fase de teste):
  → Empresas do Simples: NÃO recolhem CBS 0,9% / IBS 0,1% separado
  → Continuam no DAS normalmente
  → 2026 é apenas período de testes e adaptação de sistemas

MUDANÇA A PARTIR DE 2027:
  O Simples Nacional terá que OPTAR:
  Opção A (DAS aprimorado): continua com DAS, porém alíquota do DAS
    será ajustada para incorporar CBS e IBS proporcionalmente.
    Empresa não emite CBS/IBS separados — tudo no DAS.
    Crédito concedido ao comprador: limitado (% definido por lei)

  Opção B (CBS/IBS separado): empresa sai do DAS para CBS/IBS e
    contribuição previdenciária em separado.
    Maior crédito para compradores, mas maior complexidade.

IMPACTO NA COMPETITIVIDADE DO SIMPLES:
  B2B (vende para empresa que quer crédito):
    → Comprador de empresa do Simples terá crédito reduzido de CBS/IBS
    → PRESSÃO para Simples dar crédito pleno → pode forçar migração
    → Empresas B2B do Simples com receita >R$1-2M devem simular a saída

  B2C (vende direto ao consumidor final):
    → Consumidor não se preocupa com crédito
    → Simples mantém vantagem para B2C

LIMITE DO SIMPLES: R$4,8M/ano — MANTIDO (sem alteração na reforma)
LIMITE MEI: R$81.000/ano — MANTIDO

ESTRATÉGIA SIMPLES 2027+:
  Hoje fatura quanto no Simples? | Recomendação
  -------------------------------|-----------------------------------
  < R$500K, B2C                  | Ficar no DAS — baixa pressão
  R$500K-R$2M, B2B               | Simular saída do Simples p/ 2027
  > R$2M, B2B ou indústria       | Quase certo sair do Simples em 2027
```

---

## 9. CHECKLIST DE PREPARAÇÃO EMPRESARIAL

```
AÇÕES IMEDIATAS (2026 — fase de teste):
[ ] Entender se seu ERP já emite NF com CBS/IBS (obrigatório a partir de 2026)
[ ] Cadastrar empresa no portal do Comitê Gestor do IBS (quando disponível)
[ ] Calcular o impacto do "custo duplo" de 2026 (1% extra no faturamento)
[ ] Mapear fornecedores e cadeia de suprimentos para calcular créditos CBS futuros
[ ] Revisar contratos de longo prazo com cláusula de reajuste tributário

AÇÕES 2027 (CBS plena, IPI reduzido):
[ ] Migrar completamente o processamento de NF para CBS
[ ] Calcular créditos de CBS sobre aluguel, energia, telecom, fretes
[ ] Decidir: ficar no Simples (DAS) ou migrar para CBS/IBS separado
[ ] Revisar precificação de serviços (especialmente serviços digitais)
[ ] Avaliar impacto do IRPF Mínimo na distribuição de dividendos

AÇÕES 2028-2032 (transição gradual IBS):
[ ] Monitorar redução anual de ICMS/ISS e aumento de IBS
[ ] Ajustar benefícios fiscais regionais (muitos irão desaparecer)
[ ] Revisar operações interestaduais (DIFAL será eliminado)
[ ] Recalcular capital de giro (split payment reduz tributo disponível)

AÇÕES 2033+ (sistema pleno):
[ ] Operação 100% no novo sistema
[ ] Benefícios de ICMS extintos — revisar localização de operações
[ ] Simples Nacional rediscutir estratégia B2B

SINAL DE ALERTA — CONTRATOS COM CLIENTES:
  Se você tem contrato plurianual (2026-2030) sem cláusula de revisão fiscal:
  → RISCO: em 2027 sua carga tributária muda significativamente
  → AÇÃO: renegociar ou incluir cláusula de revisão baseada na
    variação da alíquota CBS/IBS vigente
```

---

## 10. SIMULAÇÃO NUMÉRICA — ANTES E DEPOIS

```
EMPRESA DE SERVIÇOS TI (SaaS B2B), R$1.000.000/mês, Lucro Presumido:

HOJE (2025):
  PIS (0,65%):             R$6.500/mês
  COFINS (3,00%):         R$30.000/mês
  ISS (5,00% — SP):       R$50.000/mês
  IRPJ (15% s/ 32%):      R$48.000/mês
  CSLL (9% s/ 32%):       R$28.800/mês
  TOTAL FEDERAL+MUNIC.:   R$163.300/mês = 16,3%

EM 2027+ (CBS plena, IBS ainda 0,1% teste):
  CBS (~8,5%):             R$85.000/mês (mas crédito de CBS de insumos)
  IBS (0,1% ainda):        R$1.000/mês
  ISS (mantido ainda):     R$50.000/mês
  IRPJ:                    R$48.000/mês (sem mudança)
  CSLL:                    R$28.800/mês (sem mudança)
  TOTAL:                   R$212.800/mês = 21,3% (antes dos créditos CBS)
  Créditos CBS estimados:  -R$20.000/mês (serviços de TI têm pouco insumo)
  TOTAL LÍQUIDO:           R$192.800/mês = 19,3%
  AUMENTO: +R$29.500/mês = +R$354.000/ano

EM 2033 (IBS pleno, ICMS/ISS extintos):
  CBS (~8,5%):             R$85.000/mês (crédito de insumos)
  IBS (~18%):             R$180.000/mês (crédito de insumos)
  Créditos CBS+IBS:        -R$30.000/mês estimado (TI tem poucos insumos)
  IRPJ + CSLL:             R$76.800/mês
  TOTAL LÍQUIDO:           R$311.800/mês = 31,2%
  AUMENTO vs 2025:         +R$148.500/mês = +R$1.782.000/ano
  → IMPACTO SEVERO em SaaS/serviços digitais sem insumos

EMPRESA INDUSTRIAL (manufatura), R$1.000.000/mês, Lucro Real:

HOJE (2025):
  PIS não-cumulativo:      R$16.500/mês (com créditos ~9K reduz ~R$7K)
  COFINS não-cumul.:       R$76.000/mês (com créditos ~40K reduz ~R$36K)
  ICMS (10%):              R$100.000/mês (com créditos ~70K reduz ~R$30K)
  Carga var. efetiva:      ~R$73.000/mês = 7,3% (após créditos)

EM 2033 (sistema novo):
  CBS+IBS (~26,5%):        R$265.000/mês bruto
  Créditos (indústria tem MUITO insumo): -R$190.000/mês estimado
  Carga efetiva:           ~R$75.000/mês = 7,5%
  → Impacto NEUTRO/LIGEIRAMENTE PIOR para indústria com boa cadeia

LIÇÃO: A reforma é neutra/boa para indústria e ruim para serviços puros.
```

---

## 11. REFORMA E PLANEJAMENTO FINANCEIRO

```
PARA O MODELO FINANCEIRO (DRE projetada 2026-2032):

COMO MODELAR A CARGA TRIBUTÁRIA:
  Ano 2026: carga atual + 1% extra (CBS+IBS teste) — compensado depois
  Ano 2027: CBS plena, ISS mantido, IPI reduzido
  Ano 2028: estável
  Anos 2029-2032: ICMS/ISS cai proporcionalmente, IBS sobe
  Ano 2033: sistema novo pleno

PROXY PRÁTICO PARA PROJEÇÃO:
  Se você é do Simples Nacional: DAS com pequena variação (+1-3%)
  Se você é Lucro Presumido/Real de SERVIÇOS: prever alta de +5-15%
    na carga tributária efetiva até 2033
  Se você é INDÚSTRIA: prever impacto neutro a levemente negativo
  Se você é EXPORTADOR: benefícios mantidos, impacto positivo nos créditos

CONTRATOS DE LONGO PRAZO — CLÁUSULA RECOMENDADA:
  "O preço será reajustado automaticamente na proporção da variação da
  carga tributária efetiva decorrente da transição para CBS/IBS prevista
  na EC 132/2023, calculada pelo método [especificar]."

REAJUSTE DE PREÇOS — ESTRATÉGIA:
  2026: comunicar clientes sobre o início da transição
  2027: reajustar contratos para absorver CBS plena
  2029-2032: reajustes anuais conforme extinção gradual de ICMS/ISS
```

---

## FONTES E VALIDAÇÃO

```
Legislação Base:
  EC 132/2023 (aprovação da reforma)
  LC 214/2025 (regulamentação CBS/IBS/IS)
  PL 1087/2025 (IRPF Mínimo + tributação dividendos)

Portais Oficiais:
  Portal Reforma Tributária: gov.br/reformatributaria
  Comitê Gestor IBS: comitegestor.gov.br (em implantação)
  Receita Federal CBS: receita.fazenda.gov.br/reformatributaria
  Tabela CBS (Informe Técnico 2026.002): publicado 12/05/2026

AVISO: A reforma está em andamento. Alíquotas plenas do CBS/IBS
ainda dependem de regulamentação complementar do Comitê Gestor.
Sempre validar com contador especializado antes de projeções financeiras.
```
