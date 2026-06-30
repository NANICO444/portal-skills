---
name: marketing-decision
description: "DECISAO DE MARKETING RAPIDA — Para @marketing-strategist. Foco em ROI."
model: openrouter/deepseek-v4-flash
user-invocable: true
allowed-tools: Read, Bash, Grep
---

# Marketing Decision — Fast

## Regra de Ouro
Toda acao de marketing tem CAC, LTV e ROI. Se nao sabe o ROI, NAO faca.

## Quando Usar
"Vale a pena investir em canal X?"
"Devo lancar campanha Y?"
"Publico alvo certo: Z ou W?"

## Framework (4 Perguntas, 30 segundos)

### Q1 — Quem?
- ICP (Ideal Customer Profile) definido?
- Tamanho do mercado: TAM/SAM/SOM
- Comportamento: onde esta, como compra, quando

### Q2 — Mensagem?
- Dor principal do publico
- Proposta de valor unica
- CTA claro

### Q3 — Canal?
- Custo por aquisicao (CAC) estimado
- Volume potencial
- Tempo ate resultado

### Q4 — ROI projetado?
- LTV > 3x CAC (saudavel)
- Payback < 12 meses
- Margem de contribuicao > 30%

## Output Esperado

```
ICP: [descricao do cliente ideal]
TAM: X / SAM: Y / SOM: Z

DOR PRINCIPAL: [frase]
PROPOSTA DE VALOR: [frase]
CTA: [acao]

CANAIS TESTADOS:
- Canal A: CAC=R$X, LTV=R$Y, ROI=Z%
- Canal B: CAC=R$X, LTV=R$Y, ROI=Z%

DECISAO: [Canal X / Nenhum / Testar A e B]

ORCAMENTO SUGERIDO: R$ [valor]/mes
METRICAS A MONITORAR: [lista]
```

## Quando Pedir Mais Analise
- Lançamento de marca/produto novo
- Mudanca de posicionamento
- Investimento > R$ 50k/mes
- Nesses casos: delegue para ultra-powerful/cross-domain-optimization
