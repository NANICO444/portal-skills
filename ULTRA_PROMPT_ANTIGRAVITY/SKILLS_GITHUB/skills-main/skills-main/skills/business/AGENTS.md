# Business & Tax Brasil — Skill Library
# Agent Instructions | Ler SEMPRE primeiro | ~600 tokens
# GitHub: https://github.com/Joehott/skills/tree/main/skills/business
# Raw base: https://raw.githubusercontent.com/Joehott/skills/main/skills/business/

---

## REGRA #1 — NAO CARREGUE TUDO

Este repositorio tem ~56.000 tokens. Carregar tudo e desperdicio.
Leia ESTE arquivo (600 tokens), identifique a tarefa, carregue APENAS os arquivos listados abaixo.
Maximo recomendado por sessao: 2-3 arquivos = ~15.000 tokens.

---

## ROTEADOR — Situacao → Arquivo(s)

| Situacao | Arquivos a carregar |
|----------|---------------------|
| Abrir empresa / escolher regime | `brazil_tax_regulatory.md` |
| Referencia completa de aliquotas | `brazil_tax_complete.md` |
| Consultar CNAE especifico | **EXECUTAR** `brazil_cnae_database.py` (ver abaixo) |
| Validar ideia / Lean Canvas / PMF | `business_idea_validation.md` |
| Calcular VPL, TIR, payback | `business_viability_calculation.md` |
| Montar plano de negocios | `business_plan_creation.md` |
| Analisar empresa (SWOT, Porter) | `business_analysis.md` |
| Calendario fiscal / prazos 2026 | `brazil_tax_obligations_calendar.md` |
| RET / Lei do Bem / ZFM / Transacao | `brazil_tax_special_regimes.md` |
| CBS / IBS / Reforma 2026-2033 | `brazil_tax_reform_2026_2032.md` |
| Pro-labore / dividendos / PGBL / ITCMD | `brazil_tax_individual_optimization.md` |
| Plano de negocios completo | `business_plan_creation.md` + `business_viability_calculation.md` + `brazil_tax_regulatory.md` |
| Mentoria tributaria completa | `brazil_tax_regulatory.md` + `brazil_tax_complete.md` |

---

## CNAE — USE O SCRIPT, NAO LEIA O FONTE

O arquivo brazil_cnae_database.py tem 7.445 tokens. NAO leia o codigo.
Execute diretamente:

```bash
python3 brazil_cnae_database.py 6201500
python3 brazil_cnae_database.py --search "engenharia"
python3 brazil_cnae_database.py --simular --cnae 7112000 --faturamento 800000 --folha 250000
python3 brazil_cnae_database.py --list-vedados
```

Output: ~50 tokens com regime, anexo, aliquota efetiva e comparativo. 150x mais eficiente.

---

## COMO BUSCAR UM ARQUIVO

### Se os arquivos estao locais (clone do repo):
```
Read: skills/business/<arquivo>.md
```

### Se for agente remoto (sem clone):
```
WebFetch: https://raw.githubusercontent.com/Joehott/skills/main/skills/business/<arquivo>.md
```

### Exemplos:
```
https://raw.githubusercontent.com/Joehott/skills/main/skills/business/brazil_tax_regulatory.md
https://raw.githubusercontent.com/Joehott/skills/main/skills/business/business_viability_calculation.md
```

---

## MAPA RAPIDO DE ARQUIVOS

```
brazil_tax_regulatory.md         3.9K tok | Regimes, tipos empresa, armadilhas
brazil_tax_complete.md           8.2K tok | 6 regimes detalhados (referencia)
brazil_tax_obligations_calendar  4.7K tok | Calendario 2026, multas, sistemas
brazil_tax_special_regimes.md    5.4K tok | RET, REIDI, Lei do Bem, ZFM, PADIS
brazil_tax_reform_2026_2032.md   5.5K tok | CBS/IBS/IS, IRPF Minimo 2026-2033
brazil_tax_individual_optim.md   5.5K tok | Pro-labore, PGBL, ITCMD, holding
business_analysis.md             2.3K tok | SWOT, Porter, BCG, VRIO
business_idea_validation.md      3.1K tok | Lean Canvas, PMF, TAM/SOM
business_plan_creation.md        3.2K tok | Plano 8 secoes + Pitch Deck
business_viability_calculation   3.4K tok | VPL, TIR, Payback, Valuation
brazil_cnae_database.py          EXECUTAR | Nao ler o fonte
```

---

## CONTEXTO DE VALIDACAO

Dados com base em legislacao brasileira ate 2026-05-17.
Reforma Tributaria: EC 132/2023 + LC 214/2025 + PL 1087/2025.
Sempre recomendar validacao com contador para decisoes finais.
