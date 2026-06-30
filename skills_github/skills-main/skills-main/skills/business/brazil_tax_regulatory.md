# SKILL: Brazil Tax & Regulatory Framework
# Versao: 1.0.0 | Para: modules_strategy, modules_data, modules_automation, modules_personal_v2 | Fase: 2-4
# Criada em: 2026-05-17 | Sessao: sess_20260517_2226_biz
# CONTEXTO: Legislação tributária brasileira — o "sócio silencioso" que precisa ser dominado

---

## AVISO CRÍTICO
> A legislação tributária brasileira é uma das mais complexas do mundo.
> Esta skill é um guia estratégico — SEMPRE validar com contador credenciado antes de decisões finais.
> As informações refletem o estado em 2025-2026, incluindo a Reforma Tributária em andamento.

---

## 1. TIPOS DE EMPRESA — COMPARATIVO ESTRATÉGICO

### Tabela de Decisão
```
TIPO     | FATURAMENTO MÁXIMO | SÓCIOS | REGIME POSSÍVEL      | RESPONSABILIDADE
---------|-------------------|--------|----------------------|------------------
MEI      | R$ 81.000/ano     | 1      | Simples (fixo)       | Ilimitada (EI)
ME       | R$ 360.000/ano    | Livre  | Simples/Presumido    | Limitada (LTDA)
EPP      | R$ 4.800.000/ano  | Livre  | Simples/Presumido    | Limitada (LTDA)
LTDA     | Sem limite        | 2-inf  | Todos                | Limitada
SAS      | Sem limite        | 1+     | Todos                | Limitada
SA Fech. | Sem limite        | 2+     | Lucro Real/Presumido | Limitada
SA Aber. | Sem limite        | 2+     | Lucro Real           | Limitada

REGRA DE OURO:
- Fatura até R$81K e trabalha sozinho → MEI (menor burocracia)
- Fatura até R$4.8M e quer Simples → ME/EPP/LTDA no Simples Nacional
- Precisa de sócios, proteção patrimonial e crescimento → LTDA
- Quer captar investimento (equity) → SA ou SAS
- Startup tech com equity/ESOP → SA ou SAS (facilita cap table)
```

---

## 2. REGIMES TRIBUTÁRIOS — ESCOLHA ESTRATÉGICA

### Comparativo dos 4 Regimes

```
REGIME             | LIMITE        | ALÍQUOTA EFETIVA  | QUANDO ESCOLHER
-------------------|---------------|-------------------|---------------------
MEI                | R$81K/ano     | R$75-160/mês fixo | Só para microempreendedor solo
Simples Nacional   | R$4.8M/ano    | 4% a 33%          | Faturamento baixo-médio, serviços/comércio
Lucro Presumido    | R$78M/ano     | ~13-16% total*    | Margem alta (>32%), receitas previsíveis
Lucro Real         | Sem limite    | Varia (real)      | Prejuízo, margens baixas, créditos PIS/COFINS

*Lucro Presumido: IRPJ(15%)+ADCSL(9%)+PIS(0.65%)+COFINS(3%)+ISS/ICMS/...
```

### Simples Nacional — Tabela Completa 2025

#### Fórmula da Alíquota Efetiva:
```
Alíquota Efetiva = (RBT12 × Alíquota Nominal - Parcela a Deduzir) / RBT12

Onde: RBT12 = Receita Bruta Total nos últimos 12 meses
```

#### ANEXO I — Comércio (revenda de mercadorias)
```
Faixa | RBT12                          | Alíq.Nominal | Ded.    | Alíq.Efetiva (faixa máx.)
  1   | Até R$180.000                  | 4,00%        | R$0     | 4,00%
  2   | R$180.001 – R$360.000          | 7,30%        | R$5.940 | 5,65%
  3   | R$360.001 – R$720.000          | 9,50%        | R$13.860| 7,57%
  4   | R$720.001 – R$1.800.000        | 10,70%       | R$22.500| 9,45%
  5   | R$1.800.001 – R$3.600.000      | 14,30%       | R$87.300| 11,87%
  6   | R$3.600.001 – R$4.800.000      | 19,00%       | R$378.000|10,54% (máx)
```

#### ANEXO II — Indústria (produtos industrializados)
```
Faixa | RBT12                          | Alíq.Nominal | Ded.
  1   | Até R$180.000                  | 4,50%        | R$0
  2   | R$180.001 – R$360.000          | 7,80%        | R$5.940
  3   | R$360.001 – R$720.000          | 10,00%       | R$13.860
  4   | R$720.001 – R$1.800.000        | 11,20%       | R$22.500
  5   | R$1.800.001 – R$3.600.000      | 14,70%       | R$85.500
  6   | R$3.600.001 – R$4.800.000      | 30,00%       | R$720.000
```

#### ANEXO III — Serviços (baixa contribuição INSS patronal)
*Inclui: instalação, reparos, lavanderia, academias, odonto, medicina, TI/tech (algumas), etc.*
```
Faixa | RBT12                          | Alíq.Nominal | Ded.
  1   | Até R$180.000                  | 6,00%        | R$0
  2   | R$180.001 – R$360.000          | 11,20%       | R$9.360
  3   | R$360.001 – R$720.000          | 13,20%       | R$17.640
  4   | R$720.001 – R$1.800.000        | 16,00%       | R$35.640
  5   | R$1.800.001 – R$3.600.000      | 21,00%       | R$125.640
  6   | R$3.600.001 – R$4.800.000      | 33,00%       | R$648.000
```

#### ANEXO IV — Serviços (INSS patronal separado)
*Inclui: construção civil, vigilância, limpeza, advocacia, etc.*
```
Faixa | RBT12                          | Alíq.Nominal | Ded.
  1   | Até R$180.000                  | 4,50%        | R$0
  2   | R$180.001 – R$360.000          | 9,00%        | R$8.100
  3   | R$360.001 – R$720.000          | 10,20%       | R$12.420
  4   | R$720.001 – R$1.800.000        | 14,00%       | R$39.780
  5   | R$1.800.001 – R$3.600.000      | 22,00%       | R$183.780
  6   | R$3.600.001 – R$4.800.000      | 33,00%       | R$828.000
```

#### ANEXO V — Serviços (alta folha de pagamento)
*Serviços de publicidade, engenharia, arquitetura, auditoria, jornalismo*
```
Faixa | RBT12                          | Alíq.Nominal | Ded.
  1   | Até R$180.000                  | 15,50%       | R$0
  2   | R$180.001 – R$360.000          | 18,00%       | R$4.500
  3   | R$360.001 – R$720.000          | 19,50%       | R$9.900
  4   | R$720.001 – R$1.800.000        | 20,50%       | R$17.100
  5   | R$1.800.001 – R$3.600.000      | 23,00%       | R$62.100
  6   | R$3.600.001 – R$4.800.000      | 30,50%       | R$540.000
```

---

## 3. REFORMA TRIBUTÁRIA 2026 — MUDANÇAS CRÍTICAS

### 3.1 Nova Tributação de Dividendos (PL 1087/2025)
```
SITUAÇÃO ATUAL (até 2025):
- Distribuição de lucros/dividendos: ISENTA de IR
- Estratégia clássica: pagar pró-labore mínimo + distribuir lucros (sem IR)

MUDANÇA A PARTIR DE 2026:
- Dividendos > R$50.000/mês → IRRF de 10%
- Pessoas físicas com renda > R$600.000/ano → IRPF Mínimo
- Impacto: quem ganhava R$200K/ano em dividendos pagará ~R$15.000-20.000 a mais

ESTRATÉGIA PARA 2026+:
- Calcular o ponto ótimo: quanto de pró-labore vs quanto de dividendos
- Para dividendos até R$50.000/mês = ainda isento
- Reinvestimento de lucros na empresa pode ser mais vantajoso que distribuição
- Pessoa Jurídica (holding) para sócios de alta renda
```

### 3.2 Reforma do Consumo (LC 214/2025 — CBS/IBS)
```
O QUE MUDOU:
- PIS + COFINS → CBS (Contribuição sobre Bens e Serviços) — esfera federal
- ICMS + ISS → IBS (Imposto sobre Bens e Serviços) — estadual/municipal
- Prazo de transição: 2026-2032 (coexistência dos sistemas)

IMPACTO NO PLANEJAMENTO:
- Sistema dual durante a transição: CALCULAR AMBOS
- Créditos de CBS/IBS são amplos (não cumulatividade real)
- Empresas do Simples Nacional: podem ou não optar pelo IBS/CBS
- Serviços digitais: inclusão no IBS (era ISS municipal antes)

AÇÃO IMEDIATA:
- Mapear toda a cadeia de fornecedores para calcular créditos futuros
- Calcular impacto na margem para os próximos 7 anos
```

---

## 4. OTIMIZAÇÃO FISCAL — ESTRATÉGIAS LEGAIS

### 4.1 Pró-labore vs Distribuição de Lucros (2025 vs 2026)
```
CALCULADORA DE REMUNERAÇÃO DO SÓCIO:

PRÓ-LABORE:
+ Gera benefício INSS (aposentadoria, auxílio, etc.)
+ Dedutível da base do IRPJ (Lucro Real)
- Tributado pelo IRPF (tabela progressiva até 27,5%)
- INSS patronal: 20% (Lucro Real/Presumido) ou incluso (Simples III/V)
- INSS do sócio: 11% até teto (~R$880/mês máx.)

DISTRIBUIÇÃO DE LUCROS (regra 2025):
+ ISENTA de IRPF (historicamente)
+ Sem INSS
- Precisa de lucro contábil real
- Não dedutível do IRPJ

EXEMPLO PRÁTICO (2025 — sócio quer R$20.000/mês líquido):
Via pró-labore: Bruto ~R$28.700 → paga ~R$7.450 impostos
Via dividendos: Bruto R$20.000 → paga R$0 (isento)
ECONOMIA: ~R$7.450/mês = R$89.400/ano

EXEMPLO PRÁTICO (2026 — com nova tributação):
Via dividendos até R$50K/mês: ainda isento
Via dividendos > R$50K/mês: 10% IRRF sobre excedente
ESTRATÉGIA: manter distribuição até R$50K/mês por sócio
```

### 4.2 Planejamento de Regime Tributário
```
DECISÃO DE REGIME — ÁRVOURE DE DECISÃO:

Fatura até R$81K e é solo?
  → MEI (mais simples)

Fatura até R$4.8M?
  → Calcular Simples Nacional para seu Anexo
  → Comparar com Lucro Presumido (se margem > 32%)
  → Simples Nacional geralmente melhor até ~R$2M em serviços (Anexo III)

Margem bruta > 40% e fatura > R$2M?
  → Lucro Presumido pode ser vantajoso
  → Calcular: 16% IRPJ base presumida × 15% + 9% CSLL = ~3,5% + PIS/COFINS cumulativos

Tem prejuízo ou margem muito baixa (<8%)?
  → Lucro Real (paga IR só sobre lucro real)
  → Pode aproveitar créditos de PIS/COFINS não-cumulativos

COMPARATIVO NUMÉRICO (serviço, R$500K/ano, margem 50%):
Simples Anexo III: ~R$49.050 (9,81% efetivo)
Lucro Presumido: ~R$68.000 (13,6%)
Lucro Real (50% margem): ~R$60.000 (12%)
MELHOR: Simples Nacional neste caso
```

### 4.3 Holding Familiar / Estrutura de Proteção Patrimonial
```
QUANDO CRIAR UMA HOLDING:
[ ] Patrimônio pessoal > R$1 milhão
[ ] Múltiplos sócios/herdeiros
[ ] Quero separar risco empresarial do patrimônio pessoal
[ ] Planejamento sucessório (evitar inventário)
[ ] Receitas de aluguel passivas (holding imobiliária)

ESTRUTURA TÍPICA:
Pessoa Física (sócio)
    ↓
Holding PJ (Ltda ou SA)
    ↓ ↓ ↓
Op.A  Op.B  Op.C (empresas operacionais)

VANTAGEM: Dividendos entre PJs são ISENTOS (regime "participation exemption")
          Imóveis na PJ: ITBI ao transferir, mas ganho de capital menor
          Planejamento sucessório: cotas com cláusulas de impenhorabilidade
```

---

## 5. OBRIGAÇÕES FISCAIS — CHECKLIST POR PORTE

### MEI
```
[ ] DAS mensal (guia unificada: INSS + ICMS ou ISS)
[ ] DASN anual (declaração simplificada) até 31/05
[ ] Notas fiscais (guardar 5 anos)
[ ] Limite de faturamento: R$81.000/ano + R$6.750/mês
[ ] Só 1 funcionário (salário mínimo ou piso da categoria)
PROIBIDO no MEI: sócio, filial, atividade vedada
```

### ME / EPP (Simples Nacional)
```
[ ] DAS mensal (vencimento dia 20)
[ ] DEFIS anual (declaração Simples) até 31/07
[ ] GFIP/eSocial (se tiver funcionários)
[ ] EFD-Contribuições (se tiver isenção Simples)
[ ] SPED Fiscal / EFD-ICMS (depende do estado)
[ ] DCTF mensal (se saiu do Simples ou tem retenções)
Atenção: subexcesso de faturamento → regra de proporcionalidade
         Ultrapassou 20% do limite → exclusão do Simples no ano seguinte
```

### LTDA / SA (Lucro Real ou Presumido)
```
[ ] DCTF mensal
[ ] ECF anual (Escrituração Contábil Fiscal)
[ ] ECD anual (Escrituração Contábil Digital)
[ ] EFD-Contribuições mensal (PIS/COFINS)
[ ] EFD-REINF (retenções/prestadores)
[ ] eSocial (folha de pagamento)
[ ] GFIP mensal (FGTS)
[ ] DIRF anual
[ ] RAIS anual
Custo contábil estimado: R$500-3.000/mês dependendo do porte
```

---

## 6. ABERTURA DE EMPRESA — PASSO A PASSO

```
FLUXO DE ABERTURA (LTDA no Simples Nacional):

1. DEFINIR:
   - Atividade (CNAE) — verificar vedações Simples Nacional
   - Sócios e % de capital
   - Capital social (recomendado: 3-6 meses de custos fixos)
   - Endereço (sede ou coworking/virtual)

2. REGISTRO (7-30 dias úteis):
   a. JUNTA COMERCIAL: registro do contrato social
   b. RECEITA FEDERAL: CNPJ (online, 1-3 dias)
   c. PREFEITURA: alvará de funcionamento + ISS
   d. ESTADO: IE (Inscrição Estadual) se for ICMS
   e. VIGILÂNCIA SANITÁRIA: se alimentos/saúde/farmácia

3. SIMPLES NACIONAL:
   - Solicitar adesão via portal Simples Nacional
   - Prazo: até 30 dias após abertura do CNPJ
   - Verificar vedações (holding, financeira, etc.)

4. PÓS-ABERTURA:
   - Abrir conta PJ (PJ Simples é obrigatório no MEI)
   - Contratar contador
   - Configurar sistema de NF-e/NFS-e
   - Registrar marca (INPI) — pode levar 2-3 anos

CUSTOS MÉDIOS DE ABERTURA:
- Honorários despachante/contador: R$500-1.500
- Taxas estaduais/municipais: R$100-500
- Capital social mínimo sugerido: R$1.000-5.000
- Total: ~R$1.500-3.000
```

---

## 7. CARGA TRIBUTÁRIA REAL — SIMULADOR MENTAL

```
CÁLCULO DA CARGA TOTAL SOBRE O FATURAMENTO (empresa de serviços, Simples III):

Faturamento bruto: R$100.000/mês = R$1.200.000/ano

IMPOSTOS SOBRE FATURAMENTO (Simples Nacional Anexo III, Faixa 4):
Alíquota efetiva: ~14,1%
= R$14.100/mês

FOLHA DE PAGAMENTO (se tiver 3 funcionários, CLT):
Salário bruto: R$5.000 × 3 = R$15.000
+ Encargos patronais (~73% do salário bruto no Lucro Real): mas no Simples, incluso
13º + Férias + FGTS proporcionais: +35% sobre salário = ~R$5.250/mês

PRÓ-LABORE DO SÓCIO:
Bruto: R$5.000
INSS sócio (11%): R$550
IR (tabela): ~R$500
Líquido sócio: ~R$3.950

CUSTO REAL TOTAL DO NEGÓCIO (por R$100K faturado):
- Impostos (Simples): R$14.100 (14,1%)
- Folha + encargos: R$20.250 (20,3%)
- Aluguel: R$3.000 (3%)
- Serviços (contabilidade, etc.): R$2.000 (2%)
- Total custos fixos mínimos: ~R$39.350 (39,4%)
- SOBRA PARA O NEGÓCIO: ~R$60.650 (60,6%)

LIÇÃO: Em serviços, se margem bruta < 40% → negócio inviável no Simples Nacional
```

---

## 8. ARMADILHAS TRIBUTÁRIAS MAIS COMUNS

```
ARMADILHA 1 — Exclusão do Simples por ultrapassagem:
Risco: Faturar > R$4.8M em 12 meses → exclusão retroativa no mesmo ano
Ação: Monitorar faturamento mensalmente; se >80% do limite, planejar saída

ARMADILHA 2 — CNAE vedado no Simples:
Risco: Abrir empresa com CNAE que não permite Simples (ex: seguros, financeiras)
Ação: Verificar ANTES na tabela de CNAEs vedados no site do Simples Nacional

ARMADILHA 3 — Sócio PJ:
Risco: Empresa com sócio PJ não pode optar pelo Simples Nacional
Ação: Avaliar estrutura antes de abrir; holdings podem inviabilizar o Simples

ARMADILHA 4 — Distribuição de lucros sem contabilidade:
Risco: Distribuir valores sem lucro contábil = pro-labore disfarçado → INSS
Ação: Manter contabilidade em dia; distribuir só sobre lucro real apurado

ARMADILHA 5 — Nota fiscal atrasada / sem emitir:
Risco: Autuação fiscal, multa 50-150% do tributo + juros SELIC
Ação: Emitir NF no ato ou antes do recebimento; nunca postergar

ARMADILHA 6 — Reforma tributária (2026-2032):
Risco: Ignorar a transição CBS/IBS → precificação errada
Ação: Contratar contador especializado em reforma; revisar contratos de longo prazo

ARMADILHA 7 — Confusão patrimonial:
Risco: Misturar conta PF com PJ → anulação da responsabilidade limitada
Ação: NUNCA usar conta pessoal para a empresa; toda operação pela conta PJ

ARMADILHA 8 — FGTS e 13º não provisionados:
Risco: Caixa insuficiente em dezembro/aniversário de rescisão
Ação: Provisionar ~35% sobre cada salário pago (13º + férias + FGTS + encargos)
```

---

## 9. FERRAMENTAS RECOMENDADAS

```
CALCULADORAS E SIMULADORES (gratuitos):
- Portal Simples Nacional: http://www8.receita.fazenda.gov.br/SimplesNacional
- Calculadora Simples (CORA): simular alíquota efetiva por faixa
- Simulador IRPJ/CSLL: calculadorabrasil.com.br
- Planilhas SEBRAE: sebraepr.com.br/planilhas (viabilidade econômica gratuita)
- GitHub/calculadora-fiscal: CLI Python Simples + Presumido + Real

ERPs PARA PMEs BRASILEIRAS:
- Omie: ERP + contabilidade integrada (muito usado no Simples)
- Nibo: gestão financeira + integração contador
- ContaAzul: PME, NF-e integrada
- Bling: e-commerce + NF-e
- TOTVS: enterprise
- QuickBooks BR: financeiro

OBRIGAÇÕES DIGITAIS:
- SPED: portal.fazenda.gov.br/spedpor
- eSocial: esocial.gov.br
- NF-e: nfe.fazenda.gov.br
- NFS-e: varia por município

FONTES DE CONSULTA:
- Receita Federal: receita.fazenda.gov.br
- Portal do Empreendedor (MEI): gov.br/empresas-e-negocios/pt-br/empreendedor
- JUCERJA/JUCESP (Juntas Comerciais): por estado
- SEBRAE: sebrae.com.br
```
