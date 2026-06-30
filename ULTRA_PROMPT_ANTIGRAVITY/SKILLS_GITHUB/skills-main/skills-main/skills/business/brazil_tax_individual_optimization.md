# SKILL: Brazil Tax Individual Optimization — Pessoa Física e Sócio
# Versao: 1.0.0 | Para: modules_strategy, modules_personal_v2, modules_data | Fase: 3-5
# Criada em: 2026-05-17 | Sessao: sess_20260517_2226_biz
# Base Legal: PL 1087/2025, EC 132/2023, Lei 9.250/1995, CTN
# Pesquisa: Tavily (2026-05-17) — validar com contador e advogado tributarista

---

## QUANDO USAR
- Ao calcular quanto o sócio deve retirar via pró-labore vs dividendos em 2026+
- Ao planejar previdência privada (PGBL/VGBL) para reduzir IRPF do sócio
- Ao estruturar sucessão patrimonial (ITCMD, holding, doação em vida)
- Ao otimizar declaração de IRPF de pessoa física com renda alta
- Ao calcular se o IRPF Mínimo afeta o planejamento atual

---

## 1. NOVA TABELA IRPF 2026 — PESSOA FÍSICA

```
TABELA PROGRESSIVA IRPF 2026 (PL 1087/2025):

Faixa de renda mensal  | Alíquota | Dedução mensal
-----------------------|----------|---------------
Até R$5.000,00         | ISENTO   | —
R$5.000,01 a R$7.000   | Gradual* | Redução progressiva
R$7.000,01 a R$10.528  | 7,5%     | A regulamentar
R$10.528,01 a R$19.317 | 15,0%    | A regulamentar
R$19.317,01 a R$28.000 | 22,5%    | A regulamentar
Acima de R$28.000      | 27,5%    | A regulamentar

*Faixa R$5-7K: desconto progressivo — quem ganha R$5.001 paga IR reduzido;
 quem ganha R$7.001 começa a pagar pela tabela normal.

DEDUÇÕES PERMITIDAS (IRPF 2026 — mantidas):
  Dependentes: R$2.275,08/dependente/ano
  Instrução: até R$3.561,50/pessoa/ano
  Plano de saúde: dedução integral (sem limite)
  PGBL: até 12% da renda tributável bruta anual
  Pensão alimentícia: 100% (conforme decisão judicial)
  Livro-caixa (autônomo): gastos do negócio

TABELA PROGRESSIVA MENSAL — CÁLCULO PRÁTICO:
  Renda tributável R$10.000/mês:
    Isento (R$0-5K):     R$5.000 × 0% = R$0
    7,5% (R$5K-7K):      R$2.000 × 7,5% = R$150
    15% (R$7K-10K):      R$3.000 × 15% = R$450
    IR mês: R$600 → efetivo: 6%

  Renda tributável R$20.000/mês:
    IR aproximado: ~R$3.100 → efetivo: 15,5%
```

---

## 2. IRPF MÍNIMO — QUEM PAGA E COMO CALCULAR

```
GATILHO: Renda TOTAL (todas as fontes) acima de R$600.000/ano = R$50.000/mês

FONTES QUE ENTRAM NA RENDA TOTAL:
  [ ] Salário/pró-labore (já tributado pela tabela progressiva)
  [ ] Dividendos distribuídos pela empresa
  [ ] Aluguéis recebidos (PF)
  [ ] Ganhos de capital (venda de imóvel, ações)
  [ ] Rendimentos de aplicações financeiras (CDB, fundos)
  [ ] JCP (Juros sobre Capital Próprio) recebidos
  [ ] Rendimentos do exterior
  [ ] Outros rendimentos isentos (exceto LCI/LCA/Poupança — ainda isentos)

FONTES QUE NÃO ENTRAM:
  [ ] LCI/LCA/LIG/LH (mantidos isentos)
  [ ] Poupança (mantida isenta)
  [ ] Indenizações (FGTS, acidente de trabalho, etc.)
  [ ] Herança/doação (sujeita a ITCMD, não IRPF)

CÁLCULO DO IRPF MÍNIMO:

  PASSO 1: Some toda a renda (inclusive isentos sujeitos ao mínimo)
  PASSO 2: Se total > R$600.000/ano → calcule 10% do total
  PASSO 3: Subtraia o IRPF já pago (pró-labore, aluguéis, etc.)
  PASSO 4: Se a diferença for positiva → é o IRPF Mínimo a complementar

EXEMPLOS PRÁTICOS:

EXEMPLO 1 — Sócio com renda alta (renda ~R$1,2M/ano):
  Pró-labore:       R$120.000/ano → IRPF pago: ~R$30.000
  Dividendos:       R$800.000/ano → IRPF pago: R$0 (até R$600K/ano isento)
                                               R$50.000 (IRRF 10% s/ R$200K excedente → R$20.000)
  Aluguel PF:       R$60.000/ano → IRPF pago: ~R$8.000
  Aplicações (CDB): R$40.000/ano → IR pago: ~R$6.000 (tabela regressiva)
  Poupança:         R$20.000/ano → ISENTO (não entra)
  ─────────────────────────────────────────────────
  Renda total sujeita: R$120K + R$800K + R$60K + R$40K = R$1.020.000
  IRPF Mínimo (10%): R$102.000
  IRPF já pago:      R$30.000 + R$20.000 + R$8.000 + R$6.000 = R$64.000
  COMPLEMENTO DEVIDO: R$102.000 - R$64.000 = R$38.000/ano

EXEMPLO 2 — Sócio com renda menor (renda ~R$700K/ano):
  Pró-labore:       R$60.000/ano → IRPF: ~R$8.000
  Dividendos:       R$600.000/ano → IRPF: R$0 (abaixo do limite R$50K/mês)
  Aluguéis:         R$40.000/ano → IRPF: ~R$5.000
  TOTAL:            R$700.000/ano
  IRPF Mínimo (10%): R$70.000
  IRPF já pago:      R$13.000
  COMPLEMENTO:       R$57.000/ano → SIGNIFICATIVO

EXEMPLO 3 — Sócio estruturado (renda ~R$580K/ano):
  Pró-labore:       R$60.000/ano → IRPF: R$8.000
  Dividendos:       R$480.000/ano → R$0 (R$40K/mês — abaixo de R$50K)
  Aluguel:          R$40.000/ano → IRPF: R$5.000
  TOTAL:            R$580.000/ano → ABAIXO DO GATILHO R$600K
  IRPF Mínimo:      NÃO APLICÁVEL
  → ESTRATÉGIA: manter renda total < R$600K/ano
```

---

## 3. PRÓ-LABORE ÓTIMO 2026 — CALCULADORA ESTRATÉGICA

```
VARIÁVEIS A BALANCEAR:
  + Pró-labore maior: gera mais benefício INSS, dedução ECF (Lucro Real)
  - Pró-labore maior: paga mais IRPF + INSS sócio (11%)
  + Dividendo maior: sem INSS, sem IRPF (até R$50K/mês)
  - Dividendo maior: conta para IRPF Mínimo se renda total > R$600K/ano

REGRAS BASE 2026:
  Pró-labore MÍNIMO obrigatório: 1 salário mínimo (R$1.518/mês em 2026)
  Pró-labore até R$5.000/mês: isento de IRPF (tabela nova)
  Dividendos até R$50.000/mês: sem IRRF
  Renda total até R$600.000/ano: sem IRPF Mínimo

ESTRATÉGIA PONTO A — SÓCIO COM RENDA TOTAL < R$600K/ANO:
  Pró-labore ótimo: R$5.000/mês (máximo isento de IRPF)
    → INSS sócio: R$550/mês (11% até teto)
    → IRPF sócio: R$0/mês
  Dividendos: até R$600K/ano - R$60K pró-labore = R$540K/ano = R$45K/mês
    → IRRF: R$0 (abaixo de R$50K/mês)
  CARGA TOTAL PF: apenas INSS = R$550/mês = R$6.600/ano

ESTRATÉGIA PONTO B — SÓCIO COM RENDA TOTAL > R$600K/ANO:
  Calcular o "ponto de indiferença" entre pró-labore e dividendo:

  Via pró-labore acima de R$7K:
    IR progressivo (7,5% a 27,5%) + INSS 11%
    Custo para receber R$10.000 líquido via pró-labore ≈ R$14.000 bruto

  Via dividendo acima de R$50K/mês:
    IRRF 10% na fonte + potencial IRPF Mínimo no ajuste anual
    Custo para receber R$10.000 via dividendo ≈ R$11.100 bruto

  CONCLUSÃO: Mesmo com IRPF Mínimo, dividendo ainda é mais eficiente
  que pró-labore para altas rendas — diferença menor que antes, mas existe.

TABELA COMPARATIVA — RENDA LÍQUIDA DO SÓCIO:

Retirada bruta | Via pró-labore | Via dividendo | Mais eficiente
---------------|----------------|---------------|---------------
R$5.000/mês    | -R$550 INSS    | R$0           | Dividendo (sem INSS)
               | -R$0 IR        |               |
               | Líq: R$4.450   | Líq: R$5.000  |
R$20.000/mês   | -R$550 INSS    | R$0           | Dividendo
               | -R$2.500 IR    |               |
               | Líq: R$16.950  | Líq: R$20.000 |
R$60.000/mês   | -R$550 INSS    | -R$1.000 IRRF | Dividendo
               | -R$13.000 IR   | (10% s/ R$10K)|
               | Líq: R$46.450  | Líq: R$59.000 |
R$100.000/mês  | -R$550 INSS    | -R$5.000 IRRF | Dividendo
               | -R$26.000 IR   |               |
               | Líq: R$73.450  | Líq: R$95.000 |
```

---

## 4. PGBL — PREVIDÊNCIA PRIVADA COMO DEDUÇÃO FISCAL

```
PGBL (Plano Gerador de Benefício Livre):

QUEM DEVE USAR:
  → Declaração COMPLETA do IRPF (não simplificada)
  → Contribuinte ao INSS (pró-labore ou CLT)
  → Renda tributável > R$60.000/ano (benefício maior)

COMO FUNCIONA:
  Contribuições ao PGBL até 12% da renda tributável bruta anual
  → São DEDUZIDAS da base de cálculo do IRPF no ano de entrada
  → O IR é diferido para o momento do resgate (não isento — apenas adiado)
  → No resgate: IR na tabela progressiva ou regressiva (a escolher)

VANTAGEM REAL DO PGBL:
  Não é isenção — é DIFERIMENTO. A vantagem é:
  1. Usar dinheiro do IR para investir agora (ganho financeiro)
  2. Resgatar futuramente com alíquota menor (se renda cair na aposentadoria)
  3. Usar tabela regressiva do IRPF (15% após 8 anos de acumulação)

CÁLCULO DO BENEFÍCIO FISCAL DO PGBL:
  Renda tributável anual: R$300.000
  PGBL máximo: 12% = R$36.000/ano
  IR economizado agora (alíquota marginal 27,5%): R$9.900/ano
  → R$9.900 pode ser reinvestido agora

  No resgate (depois de 8+ anos), tabela regressiva:
  → Alíquota de 15% sobre o total resgatado (incluindo rendimentos)
  → SE renda na aposentadoria for menor que R$300K/ano:
    Alíquota efetiva no resgate < 27,5% → ganho real

PGBL OU VGBL — QUAL ESCOLHER:

Condição                                    | Escolha
--------------------------------------------|----------
Declaração completa + contribui ao INSS     | PGBL (até 12%)
Declaração simplificada                     | VGBL
Já usou 12% em PGBL e quer mais             | VGBL (excedente)
Profissional liberal sem INSS               | VGBL (sem benefício PGBL)
Quero herdar para herdeiros (sucessão)      | VGBL (inventário gratuito*)

*VGBL: inventário gratuito — não entra no espólio para ITCMD (vantagem sucessória)

TABELA REGRESSIVA IR PGBL/VGBL:
  Prazo de acumulação | Alíquota IR no resgate
  --------------------|------------------------
  Até 2 anos          | 35%
  2 a 4 anos          | 30%
  4 a 6 anos          | 25%
  6 a 8 anos          | 20%
  8 a 10 anos         | 15%
  Acima de 10 anos    | 10%

ESTRATÉGIA ÓTIMA PGBL:
  1. Contribuir regularmente por 10+ anos
  2. Usar tabela regressiva (15%/10% alíquota)
  3. Resgatar na aposentadoria quando renda for menor
  4. Combinar com VGBL para sucessão dos excedentes
```

---

## 5. ITCMD — IMPOSTO SOBRE HERANÇA E DOAÇÃO 2026+

```
BASE LEGAL: EC 132/2023 — obrigou alíquotas progressivas em todos os estados

MUDANÇA CRÍTICA:
  ANTES (até 2025): estados podiam ter alíquota fixa (maioria usava 4%)
  A PARTIR DE 2027: OBRIGATÓRIO progressividade (estados devem adaptar até 2027)
  TETO CONSTITUCIONAL: máximo 8% (pode ser ampliado por Resolução do Senado)

CENÁRIO ATUAL (2026 — estados em transição):
  Maioria dos estados ainda com alíquotas antigas:
  São Paulo:    4% (proposta progressiva até 8% em discussão na ALESP)
  Rio de Janeiro: 4% a 8% progressivo (já implementado)
  Minas Gerais: 5% fixo (revisão em 2026)
  Rio Grande do Sul: 3% a 6% progressivo (já progressivo)
  Outros: variam — consultar SEFAZ estadual

PROJEÇÃO PÓS-2027 (alíquota progressiva de até 8%):
  Patrimônio transmitido | Alíquota estimada
  -----------------------|------------------
  Até R$100.000          | 2-4%
  R$100K a R$500K        | 4-6%
  R$500K a R$1M          | 6-7%
  Acima de R$1M          | 8% (teto atual)
  Obs: estados com RC aprovada pela Resolução Senado podem superar 8%

CÁLCULO IMPACTO ITCMD (patrimônio R$5.000.000):
  COM alíquota 8%: R$400.000 de ITCMD
  COM planejamento sucessório (doação progressiva em vida): muito menor

ESTRATÉGIAS PARA REDUZIR ITCMD:

ESTRATÉGIA 1 — DOAÇÃO EM VIDA (antecipação da herança):
  Doação feita ANTES de 2027 (quando muitos estados ainda têm alíquota menor):
  → Doação em 2026 a 4% vs herança em 2028 a 8% → economia de 4% do patrimônio
  Para R$1M de patrimônio: economia de R$40.000 fazendo a doação em 2026
  ATENÇÃO: ITCMD também incide sobre doações — não é isento, apenas pode ser menor

ESTRATÉGIA 2 — HOLDING FAMILIAR:
  Patrimônio (imóveis, participações) dentro de holding LTDA/SA:
  → Transferência de cotas da holding para herdeiros = ITCMD sobre cotas
  → Cotas geralmente avaliadas com desconto em relação ao ativo subjacente
  → Pode ter cláusulas: impenhorabilidade, incomunicabilidade, reversão
  → Planejamento sucessório eficiente sem necessidade de inventário judicial

  IMPOSTO NA TRANSFERÊNCIA DAS COTAS:
  → ITCMD sobre o valor das cotas (não sobre o imóvel direto)
  → Em estados que aceitam: avaliação por múltipla de patrimônio líquido
    pode ser menor que valor de mercado do ativo

ESTRATÉGIA 3 — VGBL PARA SUCESSÃO:
  VGBL não entra no inventário (não é herança civil)
  → Beneficiários recebem DIRETAMENTE sem ITCMD (dependendo do estado)
  → Alguns estados já estão tentando tributar VGBL com ITCMD — verificar
  → Enquanto não regulamentado: VGBL = sucessão sem ITCMD

ESTRATÉGIA 4 — SEGURO DE VIDA (LOVIR):
  Indenização de seguro de vida: ISENTA de IRPF e ISENTA de ITCMD
  → Ferramente poderosa para passar patrimônio sem impostos
  → Limites: prêmio deve ser compatível com a renda (não é planejamento abusivo)

ESTRATÉGIA 5 — IMÓVEL INTEGRALIZADO EM HOLDING:
  Transferir imóvel para holding: paga ITBI (2-3% do valor)
  Depois transferir cotas da holding para herdeiros: ITCMD sobre cotas
  Vantagem: ITBI (2-3%) < ITCMD em herança futura com alíquotas maiores
  + Proteção patrimonial + Gestão facilitada

CALENDÁRIO DE URGÊNCIA ITCMD:
  2026: Últimas janelas com alíquotas menores em muitos estados
  2027: Estados OBRIGADOS a implementar progressividade
  → Quem tem patrimônio significativo (>R$500K) deve agir EM 2026
```

---

## 6. IRPF — OTIMIZAÇÃO DA DECLARAÇÃO ANUAL

```
DEDUÇÕES POUCO UTILIZADAS (mas válidas):

1. PLANO DE SAÚDE (dedução integral):
   Pague pelo CNPJ da empresa (deduz como despesa operacional)
   E declare o valor no IRPF (dedução integral — sem limite)
   → Aumenta restituição PF + reduz base IRPJ PJ (duplo benefício)

2. DEPENDENTES:
   Filho até 25 anos em faculdade: R$2.275,08/ano + R$3.561,50 instrução
   Cônjuge sem renda: R$2.275,08/ano (se faz sentido economicamente)
   Pais/avós dependentes: R$2.275,08/ano cada

3. EDUCAÇÃO (R$3.561,50/pessoa):
   Sua faculdade, pós, MBA + filhos dependentes
   → Escola particular dos filhos: entra como instrução
   → Curso de idiomas: NÃO é dedutível (não considerado instrução)
   → Cursos técnicos/profissionalizantes: dedutíveis

4. PENSÃO ALIMENTÍCIA:
   Paga por ordem judicial: 100% dedutível (sem limite)
   Paga por acordo extrajudicial: NÃO dedutível

5. LIVRO-CAIXA (profissional autônomo/prestador):
   Despesas necessárias à geração da renda podem ser deduzidas
   → Aluguel do escritório, material, telefone vinculado à atividade
   → Requer organização de documentos + NF de todas as despesas

6. PREVIDÊNCIA PGBL:
   Até 12% da renda tributável bruta anual (não líquida)
   → Calcular exatamente o limite antes de contribuir

7. PERDAS NA BOLSA:
   Prejuízo em ações pode ser compensado com ganhos futuros
   → Manter controle de todas as operações (CEI ou planilha)
   → ETF e fundos: compensação dentro da mesma categoria

GANHO DE CAPITAL — IMÓVEL RESIDENCIAL:
  Venda de único imóvel até R$440.000: ISENTO de ganho de capital
  Venda de qualquer imóvel para compra de outro dentro de 180 dias: ISENTO
  Demais: IR de 15% a 22,5% sobre o ganho (lucro = venda - custo)
  → DARF deve ser pago até o último dia útil do mês seguinte à venda

DECLARAÇÃO SIMPLIFICADA vs COMPLETA:
  Simplificada: dedução padrão de 20% (limite R$16.754,34/ano)
  Completa: todas as deduções reais
  → Usar completa se: plano de saúde + PGBL + dependentes + instrução > R$16.754
  → Para renda >R$84.000/ano com família: quase sempre completa é melhor
```

---

## 7. PLANEJAMENTO INTEGRADO — SÓCIO 2026+

```
PERFIL 1 — SÓCIO EMPREENDEDOR, renda ~R$300K/ano, empresário PME:

SITUAÇÃO ÓTIMA:
  Pró-labore: R$5.000/mês = R$60.000/ano (isento IRPF, paga apenas INSS R$550/mês)
  Dividendos: R$20.000/mês = R$240.000/ano (sem IRRF — abaixo de R$50K/mês)
  TOTAL PF: R$300.000/ano → ABAIXO DO GATILHO R$600K → sem IRPF Mínimo
  Carga PF: apenas INSS = R$6.600/ano = 2,2% da renda total

  PGBL: R$5.000/mês × 12% = R$7.200/ano em PGBL
    → Reduz base IRPF (já isento, mas prepara aposentadoria com alíquota 10%)
  Plano de saúde: deduzido via empresa + declarado no IRPF

PERFIL 2 — SÓCIO DE SUCESSO, renda ~R$1M/ano, empresa consolidada:

SITUAÇÃO OTIMIZADA:
  Pró-labore: R$5.000/mês = R$60.000/ano (isento)
  Dividendos diretos: R$40.000/mês × 12 = R$480.000/ano (abaixo de R$50K/mês, sem IRRF)
  Dividendos via holding: R$380.000/ano para holding (holding para holding: isento)
  IRPF Mínimo cálculo:
    Renda PF: R$60K + R$480K = R$540.000 → abaixo de R$600K? → sem IRPF Mínimo!
    (Os R$380K ficam na holding — não entra na renda PF ainda)
  → Estratégia: acumular na holding, distribuir gradualmente nos anos seguintes

  Quando precisar dos R$380K:
  Opção A: distribuir em anos seguintes controlando < R$600K/ano
  Opção B: usar na holding para investimentos (imóveis, CDB corporativo)
  Opção C: planejamento sucessório (doação de cotas da holding para herdeiros)

PERFIL 3 — PROFISSIONAL LIBERAL, renda ~R$600K/ano:

  Receita via PJ (LTDA no Lucro Presumido):
    Faturamento: R$600.000/ano
    Pró-labore: R$5.000/mês = R$60.000/ano (isento)
    Dividendos: R$400.000/ano (R$33.333/mês — sem IRRF)
    IRPF Mínimo: R$60K + R$400K = R$460K → abaixo de R$600K → sem mínimo

  Economias anuais vs CLT equivalente:
    INSS: -R$7.786 (teto)
    IR: -R$100.000+ (dividendo isento)
    TOTAL ECONOMIA: ~R$107.786/ano (mas perde FGTS, aviso-prévio, etc.)

CHECKLIST DE REVISÃO ANUAL (todo início de ano):
[ ] Calcular renda total prevista (todas as fontes)
[ ] Se > R$600K: calcular IRPF Mínimo e planejar ajuste na fonte
[ ] Verificar limite de pró-labore isento (R$5.000/mês em 2026)
[ ] Verificar dividendos mensais (manter < R$50K/mês para evitar IRRF)
[ ] Calcular PGBL: 12% da renda tributável bruta
[ ] Revisar dependentes na declaração
[ ] Verificar ITCMD do estado: há janela de doação vantajosa este ano?
[ ] Revisar apólice de seguro de vida para sucessão
```

---

## 8. SUCESSÃO PATRIMONIAL — MATRIZ DE DECISÃO

```
PATRIMÔNIO  | HERDEIROS | INSTRUMENTO IDEAL        | CUSTO APROX.
------------|-----------|--------------------------|----------------
< R$100K    | Direto    | Testamento + inventário  | 5-10% do PL
R$100K-500K | 1-3 filhos| Doação em vida + cláusulas| 3-5% do PL
R$500K-2M   | Família   | Holding + VGBL            | 2-4% do PL
> R$2M      | Complexo  | Holding SA + trust PL     | 1-3% do PL
                         | jurídico estruturado      |

PROCESSO DE DOAÇÃO EM VIDA (fluxo):
  1. Avaliar patrimônio (laudos de imóvel, cotas)
  2. Escolher estrutura: doação direta vs doação de cotas da holding
  3. Pagar ITCMD (calculado sobre valor da doação)
  4. Lavrar escritura com cláusulas de proteção:
     - Impenhorabilidade (credores do donatário não alcançam)
     - Incomunicabilidade (cônjuge do donatário não tem direito)
     - Reversão (se donatário morrer antes do doador, bem volta)
     - Usufruto vitalício (doador mantém usufruto até morrer)
  5. Registrar em cartório de imóveis (se imóvel) ou JUNTA (se cotas)

HOLDING FAMILIAR — QUANDO VALE A PENA:
  Critério                             | Vale a pena?
  -------------------------------------|-------------
  Patrimônio > R$1M                    | Quase sempre
  Múltiplos herdeiros (>2)             | Sim — simplifica divisão
  Imóveis geradores de renda           | Sim — IRPJ empresa < IRPF PF
  Sócio em múltiplas empresas          | Sim — centraliza estrutura
  Quero proteger de dívidas pessoais   | Sim — holding separa risco
  Patrimônio < R$500K, 1 herdeiro      | Provavelmente não (custo alto)

CUSTOS DE MONTAR HOLDING:
  Honorários advogado/contador: R$3.000-15.000
  ITBI (transferência de imóvel para PJ): 2-3% do valor do imóvel
  Registro/taxas junta: R$500-2.000
  Manutenção anual (contabilidade, obrigações): R$3.000-8.000/ano
  BREAK-EVEN: patrimônio de ~R$500K-1M para compensar os custos
```

---

## 9. SIMULADOR RÁPIDO — QUANTO PAGAR EM 2026

```
FÓRMULA DE CARGA FISCAL ANUAL DO SÓCIO:

Dados necessários:
  A = Pró-labore bruto anual
  B = Dividendos mensais (< R$50K/mês)
  C = Dividendos mensais (> R$50K/mês)
  D = Outras rendas (aluguel, CDB, etc.)

Cálculo:
  INSS sócio = min(A × 11%, R$9.507/ano) [teto aprox. 2026]
  IRPF pró-labore = tabela progressiva sobre (A - INSS - PGBL - deduções)
  IRRF dividendos excedente = C × 10%
  IRPF outras rendas = tabela/fonte sobre D

  TOTAL RENDA = A + B + C × 12 + D
  SE TOTAL > R$600.000:
    IRPF MÍNIMO = TOTAL × 10% - (IRPF já pago)

  CARGA TOTAL = INSS + IRPF + IRRF + IRPF MÍNIMO

EXEMPLO RÁPIDO — Sócio retira R$30K/mês total:
  Pró-labore: R$5K/mês → INSS R$550, IRPF R$0
  Dividendos: R$25K/mês → sem IRRF (< R$50K)
  Renda anual: R$360K → sem IRPF Mínimo (< R$600K)
  CARGA ANUAL: R$6.600 (apenas INSS) = 1,8% da renda
  ALTAMENTE EFICIENTE

EXEMPLO — Sócio retira R$100K/mês:
  Pró-labore: R$5K/mês → INSS R$550, IRPF R$0
  Dividendos: R$95K/mês → IRRF 10% s/ R$45K = R$4.500/mês = R$54K/ano
  Renda anual: R$1.200.000 → IRPF Mínimo devido:
    10% × R$1.200K = R$120K
    Já pago: R$6.600 INSS (não desconta) + R$54K IRRF = R$54K
    COMPLEMENTO: R$66.000
  CARGA TOTAL: R$6.600 + R$54.000 + R$66.000 = R$126.600 = 10,5%
  Ainda MUITO mais eficiente que CLT equivalente (~28-32% de carga)
```

---

## FONTES E VALIDAÇÃO

```
Legislação:
  PL 1087/2025 (isenção R$5K, IRPF Mínimo, IRRF dividendos)
  EC 132/2023 (ITCMD progressivo)
  Lei 9.532/1997 + Lei 11.053/2004 (PGBL/VGBL)
  CTN art. 38 (base ITBI)

Portais:
  Receita Federal IRPF: receita.fazenda.gov.br/irpf
  Simulador PGBL: previc.gov.br
  SEFAZ SP (ITCMD): fazenda.sp.gov.br

AVISO CRÍTICO:
  Esta skill é guia estratégico. O IRPF Mínimo (PL 1087/2025) ainda
  aguarda regulamentação final do Senado e possíveis ajustes.
  SEMPRE validar cálculos com contador tributarista antes de decidir
  a estrutura de remuneração do sócio.
```
