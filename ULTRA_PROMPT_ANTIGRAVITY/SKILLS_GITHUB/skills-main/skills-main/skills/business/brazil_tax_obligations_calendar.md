# SKILL: Brazil Tax Obligations Calendar
# Versao: 1.0.0 | Para: modules_strategy, modules_data, modules_personal_v2 | Fase: 3-5
# Criada em: 2026-05-17 | Sessao: sess_20260517_2226_biz
# Pesquisa: Tavily (2026-05-17) — validar prazos anuais com contador

---

## QUANDO USAR
- Ao montar o planejamento operacional de qualquer empresa brasileira
- Ao calcular o custo real de conformidade fiscal (contabilidade + multas)
- Ao montar checklist de abertura de empresa
- Ao auditar se uma empresa está em dia com suas obrigações
- Ao negociar cláusulas tributárias em contratos de longo prazo

---

## 1. CALENDÁRIO MENSAL — RECORRÊNCIAS FIXAS

```
DIA  | OBRIGAÇÃO         | QUEM                        | O QUE É
-----|-------------------|-----------------------------|-------------------------------
 07  | FGTS (Digital)    | Todos c/ CLT                | Recolhimento FGTS mensal
     |                   |                             | (FGTS Digital desde mai/2026)
 20  | DAS               | Simples Nacional / MEI      | Tributos unificados do mês ant.
 20  | PGDAS-D           | Simples Nacional            | Declaração mensal da receita
 20  | DARF IRPJ estimat.| Lucro Real (apuração anual) | Estimativa mensal IRPJ/CSLL
 20  | DARF CSLL estimat.| Lucro Real (apuração anual) | Estimativa mensal CSLL
 25  | PIS/COFINS        | Lucro Presumido / Real      | Apuração e recolhimento
 25  | COFINS            | Lucro Presumido / Real      | (em conjunto com PIS)
 25  | ISS               | Todas (se serviço)          | Varia por município (15-25)
Útil | DCTFWeb           | Lucro Pres./Real (c/ folha) | Último dia útil do mês seg.
     |                   |                             | Ex: fato gerador mar → 30/abr
Útil | EFD-Reinf         | Lucro Pres./Real            | Retenções/prestadores serviço

REGRA DE ANTECIPAÇÃO:
  Quando dia 20 cai em sábado, domingo ou feriado NACIONAL:
  → vencimento antecipado para o último dia útil anterior
  Feriados municipais/estaduais NÃO alteram o vencimento

FGTS DIGITAL (a partir de maio/2026):
  Substitui a guia GFIP/SEFIP tradicional
  Sistema: fgts.gov.br
  Empresa consulta, valida e recolhe via Pix ou boleto
  Integrado com eSocial (S-1200/S-1210)
```

---

## 2. CALENDÁRIO TRIMESTRAL

```
TRIMESTRE | VENCIMENTO        | OBRIGAÇÃO               | QUEM
----------|-------------------|-------------------------|---------------------------
Jan-Mar   | Até 30/abril      | DARF IRPJ (trimestral)  | Lucro Real / Presumido
Jan-Mar   | Até 30/abril      | DARF CSLL (trimestral)  | Lucro Real / Presumido
Jan-Mar   | Até 30/abril      | DCTFWeb (se não mensal) | Empresas sem folha
Abr-Jun   | Até 31/julho      | DARF IRPJ               | Lucro Real / Presumido
Abr-Jun   | Até 31/julho      | DARF CSLL               | Lucro Real / Presumido
Jul-Set   | Até 31/outubro    | DARF IRPJ               | Lucro Real / Presumido
Jul-Set   | Até 31/outubro    | DARF CSLL               | Lucro Real / Presumido
Out-Dez   | Até 31/janeiro+1  | DARF IRPJ               | Lucro Real / Presumido
Out-Dez   | Até 31/janeiro+1  | DARF CSLL               | Lucro Real / Presumido

ITR (SA Capital Aberto):
  Trim 1 (jan-mar): Formulário ITR → 45 dias após 31/mar = até 14/mai
  Trim 2 (abr-jun): até 14/ago
  Trim 3 (jul-set): até 14/nov
  (4º trimestre coberto pela DFP anual)
```

---

## 3. CALENDÁRIO ANUAL — POR REGIME

### 3.1 MEI
```
OBRIGAÇÃO | PRAZO          | O QUE É                            | MULTA SE ATRASO
----------|----------------|------------------------------------|------------------
DASN-SIMEI| Até 31/05      | Declaração anual de faturamento    | R$50 fixo
          | (ano-base ant.)| (exercício anterior)               |
NF Guarda | Permanente     | Guardar NFs emitidas por 5 anos    | Perda de prova

CALENDÁRIO MEI 2026 (ano-base 2025):
  DASN-SIMEI 2026: entregar até 31/maio/2026
  DAS mensais: dia 20 de cada mês, o ano todo
```

### 3.2 Simples Nacional (ME/EPP)
```
OBRIGAÇÃO    | PRAZO 2026       | O QUE É                         | MULTA SE ATRASO
-------------|------------------|---------------------------------|------------------
PGDAS-D      | Dia 20/mês       | Declaração mensal receita bruta | 2%/mês s/ imposto
             | (mês seguinte)   |                                 | mín. R$50/mês
DAS          | Dia 20/mês       | Pagamento tributos unificados   | Juros SELIC + 2%
DEFIS        | Até 31/03/2026   | Declaração anual informações    | R$500 ou 0,5% fat.
             | (ano-base 2025)  | socioeconômicas e fiscais       |
GFIP/eSocial | Dia 07/mês       | FGTS (se tiver empregados)      | 100% FGTS + multa
RAIS         | Fev-Mar (ano+1)  | Relação Anual de Empreg./Sal.  | R$425,64/empregado
             | (ano base ant.)  |                                 |
CAGED        | Dia 07 mês seg.  | Admissões e demissões CLT       | R$650-1.300/omissão
             | (evento)         |                                 |
e-Social     | Antes do evento  | Admissão: 1 dia antes de início | R$3.000/empregado
             | (admissão)       | Folha: dia 7 do mês seguinte    |

ATENÇÃO: Se tiver ICMS/ISS separados (Anexo IV ou atividade não Simples):
  → Obrigações estaduais/municipais adicionais (varia por UF/município)
```

### 3.3 Lucro Presumido
```
OBRIGAÇÃO       | PRAZO 2026         | O QUE É                        | MULTA SE ATRASO
----------------|--------------------|---------------------------------|----------------
DCTFWeb         | Último dia útil    | Débitos federais (mensal)       | 2%/mês s/ valor
                | mês seguinte       |                                 | lim. 20% | mín. R$165,74
DARF IRPJ/CSLL  | Trim: 30 dias      | IRPJ + CSLL trimestrais         | Juros SELIC + 0,33%/dia
                | após fim trim.     |                                 |
EFD-Contribuições| Dia 10 do 2º mês  | PIS/COFINS escrituração digital | R$1.500-5.000/mês
                | após período       |                                 |
EFD-Reinf       | Último dia útil    | Retenções (prestadores serv.)   | 2%/mês | mín. R$200
                | mês seguinte       |                                 |
ECD             | Até 30/06/2026     | Escrituração contábil digital   | 0,25% receita
                | (ano-base 2025)    | (obrigat. se > R$78M ou S.A.)   | mín. R$1.500
ECF             | Até 31/07/2026     | Escrituração contábil fiscal    | 0,25% receita
                | (ano-base 2025)    | IRPJ + CSLL                     | mín. R$1.500
DCTF            | Substituída pelo   | —                               | —
                | DCTFWeb em 2025    |                                 |
RAIS            | Fev-Mar/2026       | Relação Anual Empregados        | R$425,64/empregado
CAGED           | Dia 7 mês seguinte | Movimentação CLT                | R$650-1.300
Informe Rendim. | Até 27/02/2026     | Para IRPF dos colaboradores     | R$1.500/omissão
                | (substitui DIRF)   | (via eSocial/EFD-Reinf 2025+)  |
DIMOB           | Fev/ano seguinte   | Apenas empresas imobiliárias    | 5% receita
```

### 3.4 Lucro Real
```
OBRIGAÇÃO       | PRAZO 2026         | O QUE É                        | MULTA SE ATRASO
----------------|--------------------|---------------------------------|----------------
DCTFWeb         | Último dia útil    | Débitos federais (mensal)       | 2%/mês | mín. R$165,74
                | mês seguinte       |                                 |
DARF IRPJ/CSLL  | Dia 20/mês         | Estimativa mensal (apuração     | Juros SELIC+multa
(estimativa)    | (anual)            | anual) OU último dia do trim.   |
EFD-Contribuições| Dia 10 do 2º mês  | PIS/COFINS não-cumulativo       | R$1.500-5.000/mês
EFD-Reinf       | Último dia útil    | Retenções prestadores           | 2%/mês | mín. R$200
ECD             | Até 30/06/2026     | Escrituração contábil digital   | 0,25% receita
                |                    | (OBRIGATÓRIO Lucro Real)        | mín. R$1.500
ECF             | Até 31/07/2026     | Escrituração contábil fiscal    | 0,25% receita
                |                    | LALUR incluído                  | mín. R$1.500
SPED Fiscal     | Varia por estado   | EFD-ICMS/IPI (Lucro Real)       | R$1.500-10.000/mês
(EFD-ICMS/IPI)  | (geralmente dia 15)|                                 |
RAIS            | Fev-Mar/2026       | Relação Anual Empregados        | R$425,64/empregado
DIRBI           | Mensal, dia 20     | Incentivos/benefícios fiscais   | 0,5-3% s/ receita
Informe Rendim. | Até 27/02/2026     | Para IRPF colaboradores         | R$1.500/omissão
Ativo Exterior  | Jun/ano seguinte   | Declaração BACEN (se aplicável) | R$1.500-250.000
```

### 3.5 SA Capital Aberto (obrigações CVM adicionais)
```
OBRIGAÇÃO       | PRAZO 2026         | O QUE É                        | MULTA / PENALIDADE
----------------|--------------------|---------------------------------|---------------------
ITR             | 45 dias após trim. | Info Trimestral (IFRS + notas) | CVM: advertência/multa
DFP             | Até 31/03/2026     | Demo Financeiras Padronizadas  | Suspensão negociação
                | (ano-base 2025)    | (balanço auditado IFRS)        | na B3
Form. Referência| Até 31/05/2026     | Governança, risco, histórico   | CVM: multa até R$5M
Fatos Relevantes| Imediatamente      | Eventos materiais para mercado  | CVM: multa até R$5M
Reunião CA      | Min. 4x/ano        | Ata publicada                  | Responsab. pessoal
AGO             | Até 30/04          | Assembleia Geral Ordinária     | CVM: responsab. diretores
AGE             | Conforme necessário| Assembleia Geral Extraordinária|
Auditoria ext.  | Anual              | Big Four ou equivalente        | Cancelamento registro

OBRIGAÇÕES TRIBUTÁRIAS: as mesmas do Lucro Real + regime CVM acima
```

---

## 4. CUSTO REAL DA CONFORMIDADE (TCO fiscal)

```
CUSTO ANUAL ESTIMADO POR PORTE/REGIME:

MEI:
  Contador (opcional, recomendado): R$0-300/mês
  Taxas/certidões: R$100-300/ano
  Sistema NFS-e: R$0-50/mês
  TOTAL/ANO: R$0-4.000

Simples Nacional (sem empregados):
  Contador/escritório: R$300-600/mês
  Sistema de NF: R$50-150/mês
  Total obrigações externas: R$4.200-9.000/ano

Simples Nacional (com 3-5 empregados):
  Contador/escritório: R$500-900/mês
  Sistema eSocial/folha: R$100-300/mês
  Total: R$7.200-14.400/ano

Lucro Presumido (sem empregados):
  Contador/escritório: R$800-1.500/mês
  Sistema EFD-Contrib.: R$200-500/mês
  Total: R$12.000-24.000/ano

Lucro Presumido (com 10-20 empregados):
  Contador/escritório: R$1.500-3.000/mês
  Sistema integrado: R$300-800/mês
  Total: R$21.600-45.600/ano

Lucro Real (PME, 20-50 func.):
  Departamento contábil ou BPO: R$3.000-8.000/mês
  Sistemas (ERP+SPED): R$500-2.000/mês
  Auditoria interna: R$5.000-20.000/ano
  Total: R$45.000-120.000/ano

SA Capital Aberto:
  Auditoria externa (Big Four): R$500.000-5.000.000/ano
  RI + Compliance + Jurídico: R$500.000-2.000.000/ano
  Total mínimo: R$2.000.000/ano
```

---

## 5. TABELA DE MULTAS — REFERÊNCIA RÁPIDA

```
OBRIGAÇÃO      | MULTA POR ATRASO                    | MULTA POR OMISSÃO TOTAL
---------------|-------------------------------------|----------------------------
DAS (Simples)  | Juros SELIC + 2% mês                | Exclusão do Simples
PGDAS-D        | 2% ao mês s/ tributo, mín. R$50     | Mesma
DEFIS          | R$500 ou 0,5% fat., mín. R$200      | Mesma
DCTFWeb        | 2%/mês s/ tributo, lim. 20%         | R$165,74 mínimo
               | mínimo: R$165,74                    |
EFD-Contribui. | R$1.500/mês (c/ mov.)               | R$500/mês (sem mov.)
               | R$5.000/mês (Lucro Real)            |
ECD            | 0,25% receita bruta, mín. R$1.500   | Mesma
ECF            | 0,25% receita bruta, mín. R$1.500   | Mesma
FGTS           | 100% do FGTS + SELIC + multa 50%    | Processo crime
eSocial admiss.| R$3.000 por empregado não registr.  | Autuação trabalhista
RAIS           | R$425,64 por empregado omitido      | Mesma
CAGED          | R$650-1.300 por movim. não declarado| Mesma
Form. Referência| CVM: advertência → multa até R$5M  | Suspensão na B3
(SA)            |                                     |
BACEN (CBE)    | R$1.500 a R$250.000                 | Crime cambial
Transfer Pric. | 75% da diferença (dolo: 150%)       | Mesma

JUROS PADRÃO SOBRE TRIBUTOS ATRASADOS:
  Taxa SELIC acumulada + 1% no mês do pagamento
  (não há capitalização — SELIC é simples)

DENÚNCIA ESPONTÂNEA: se pagar o tributo + juros ANTES de qualquer
intimação da RF → multa de mora é CANCELADA (art. 138 CTN)
```

---

## 6. CALENDÁRIO CONSOLIDADO 2026 — DATAS CRÍTICAS

```
JANEIRO 2026:
  Dia 07: FGTS dezembro/2025
  Dia 20: DAS/PGDAS-D dezembro/2025 (Simples)
  Dia 20: IRPJ/CSLL estimativa (Lucro Real anual) dezembro
  Dia 31: DARF IRPJ/CSLL Lucro Real/Presumido — 4º trim 2025

FEVEREIRO 2026:
  Dia 07: FGTS janeiro/2026
  Dia 20: DAS/PGDAS-D janeiro/2026
  Dia 27: Informe de Rendimentos (substitui DIRF) — ano-base 2025
  Dia 28: EFD-Contribuições dezembro/2025

MARÇO 2026:
  Dia 07: FGTS fevereiro
  Dia 20: DAS/PGDAS-D fevereiro
  Último útil: DCTFWeb fevereiro

ABRIL 2026:
  Dia 07: FGTS março
  Dia 14: ITR (SA) 1T26
  Dia 20: DAS/PGDAS-D março | IRPJ estimativa março
  Dia 30: IRPJ/CSLL 1T26 (Lucro Real/Presumido trimestral)

MAIO 2026:
  Dia 07: FGTS abril
  Dia 20: DAS/PGDAS-D abril
  Dia 31: DASN-SIMEI 2026 (MEI — ano-base 2025)

JUNHO 2026:
  Dia 07: FGTS maio
  Dia 20: DAS/PGDAS-D maio
  Dia 30: ECD 2025 (Lucro Presumido/Real — prazo final)

JULHO 2026:
  Dia 14: ITR (SA) 2T26
  Dia 20: DAS/PGDAS-D junho
  Dia 31: IRPJ/CSLL 2T26 | ECF 2025 (Lucro Real/Presumido — prazo final)

AGOSTO 2026:
  Dia 20: DAS/PGDAS-D julho
  Último útil: DCTFWeb julho

SETEMBRO 2026:
  Dia 20: DAS/PGDAS-D agosto

OUTUBRO 2026:
  Dia 14: ITR (SA) 3T26
  Dia 20: DAS/PGDAS-D setembro
  Dia 31: IRPJ/CSLL 3T26

NOVEMBRO 2026:
  Dia 20: DAS/PGDAS-D outubro

DEZEMBRO 2026:
  Dia 20: DAS/PGDAS-D novembro
  Dia 31: Ajuste anual estimativa (Lucro Real — apuração anual)

RAIS 2025 (ano-base 2025):
  Prazo: Fevereiro-Março/2026 (aguardar portaria MTE)

DIRBI (mensal — incentivos fiscais):
  Dia 20 de cada mês
```

---

## 7. OBRIGAÇÕES POR EVENTO (não-periódicas)

```
EVENTO                    | OBRIGAÇÃO                | PRAZO
--------------------------|--------------------------|----------------------------------
Abertura da empresa       | Inscrição eSocial        | Antes da 1ª contratação
                          | Adesão Simples Nacional  | Até 30 dias após CNPJ
                          | Alvará/IE/IM             | Varia por UF/município
Contratação CLT           | eSocial S-2200           | ATÉ 1 dia antes do início
                          | Cadastro CTPS digital    | No ato da contratação
                          | GFIP/eSocial S-1200      | Folha do mês da contratação
Demissão CLT              | eSocial S-2299           | Até 10 dias após aviso-prévio
                          | Rescisão/homologação     | Conforme modalidade
                          | TRCT (saldo + verbas)    | 10 dias corridos após aviso
Entrada capital estrang.  | RDE-IED (BACEN)          | Até 30 dias após integralização
Distribuição lucros       | DARF IRRF (se 2026+)     | Até 20 do mês seguinte
para não-residente        | Câmbio BACEN             | No ato da remessa
Aquisição de imóvel PJ    | ITBI                     | Antes do registro cartório
Venda de participação     | DARF ganho capital       | Último dia do mês seguinte
                          | e-CAC declaração         | Junto com ECF
Incorporação/fusão        | Protocolo Junta Comerc.  | Ato + aprovação societária
                          | ECF especial             | Prazo normal
Encerramento empresa      | Baixa CNPJ               | Após liquidação de débitos
                          | ECF final                | 6 meses após encerramento
                          | eSocial desligamentos    | Antes da baixa
```

---

## 8. FERRAMENTAS E SISTEMAS OBRIGATÓRIOS

```
SISTEMA          | O QUE É                      | ONDE ACESSAR
-----------------|------------------------------|-----------------------------------
eSocial          | Folha e eventos trabalhistas | esocial.gov.br
SPED             | Escriturações digitais        | sped.rfb.gov.br
e-CAC            | Portal tributário RFB         | cav.receita.fazenda.gov.br
PGDAS-D          | Declaração Simples Nacional  | receita.fazenda.gov.br/SN
DCTFWeb          | Débitos tributários federais | sped.rfb.gov.br/dctfweb
EFD-Contribuições| PIS/COFINS digital           | sped.rfb.gov.br
NF-e             | Nota fiscal eletrônica prod. | nfe.fazenda.gov.br
NFS-e            | Nota fiscal eletrônica serv. | portal do município
CTE              | Conhecimento transp. eletrôn.| cte.fazenda.gov.br
FGTS Digital     | FGTS integrado eSocial       | fgts.gov.br (mai/2026)
SISBACEN/RDE     | Capital estrangeiro BACEN    | bcb.gov.br
CVM Online       | Obrigações SA capital aberto | cvmonline.cvm.gov.br

OBRIGAÇÕES ESTADUAIS (variam por UF):
  SEFAZ-e / SPED Fiscal:  EFD-ICMS/IPI (Lucro Real, alguns Presumidos)
  GIA / DAPI / DAICMS:    Apuração ICMS mensal
  DIFAL:                  E-commerce e compras interestaduais
  Nota Fiscal Gaúcha / Paulista: programas estaduais de NF ao consumidor

OBRIGAÇÕES MUNICIPAIS (variam por cidade):
  NFS-e: sistema de cada prefeitura (ex: São Paulo = NF Paulistana)
  ISS: guia municipal (geralmente dia 15-25 do mês seguinte)
  IPTU (imóvel comercial): anual
  Alvará de funcionamento: anual (renovação)
```

---

## 9. CHECKLIST ANUAL — CONFORMIDADE FISCAL COMPLETA

```
MENSAL (toda empresa):
[ ] DAS pago até dia 20? (Simples/MEI)
[ ] PGDAS-D declarado até dia 20? (Simples)
[ ] FGTS pago até dia 07 / 20? (se CLT)
[ ] DCTFWeb entregue até último dia útil?
[ ] NF emitida para toda receita?
[ ] ISS pago (se serviço)?
[ ] eSocial folha (S-1200) transmitido?

TRIMESTRAL:
[ ] DARF IRPJ/CSLL pago no prazo? (Presumido/Real trimestral)
[ ] ITR entregue? (SA Capital Aberto)

ANUAL:
[ ] DEFIS entregue até 31/março? (Simples)
[ ] DASN-SIMEI entregue até 31/maio? (MEI)
[ ] ECD entregue até 30/junho?
[ ] ECF entregue até 31/julho?
[ ] RAIS entregue (fev-mar)?
[ ] Informe de Rendimentos emitido até 27/fev?
[ ] DIRBI em dia (mensal — dia 20)?
[ ] CBE/DCBE entregue até 5/abril? (capital estrangeiro)

SITUAÇÃO FISCAL:
[ ] Certidão Negativa RFB em dia? (CND ou CPEN)
[ ] Certidão FGTS em dia?
[ ] Certidão Municipal/Estadual em dia?
[ ] Nenhum débito em cobrança administrativa?
```
