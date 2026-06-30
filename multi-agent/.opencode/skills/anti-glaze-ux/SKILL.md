---
name: anti-glaze-ux
description: "ANTI-GLAZE UX - rejeite UI enganosa, dark patterns, e armadilhas. Proteja o usuario."
user-invocable: true
allowed-tools: Read, Grep
---

# Anti-Glaze UX

## Principio

> **UX enganosa eh pior que UX feia. Recuse-se a implementar.**

## Quando Usar

- Review de qualquer UI
- Decisao de design
- Analise de feature que "engaja" usuario
- Testes A/B que mostram ganho de conversao

## Dark Patterns Comuns

### Confirmshaming
- Botao de cancelar com texto hostil: "Nao, eu prefiro pagar mais"
- Botao de aceitar com texto amigavel: "Sim, economizar agora"
- **Recuse** - texto deve ser neutro

### Roach Motel
- Facil entrar, impossivel sair (assinaturas)
- Cancelar exige ligar para call center
- **Recuse** - saida deve ser tao facil quanto entrada

### Hidden Costs
- Taxa so no final
- Preco "a partir de" mas o minimo eh caro
- **Recuse** - tudo visivel ANTES

### Urgency Falsa
- "Restam apenas 2!" quando tem 100
- Countdown que reseta
- "X pessoas estao vendo agora" fake
- **Recuse** - urgencia real, nao fabricada

### Forced Continuity
- Cobra apos free trial sem avisar
- Datas de cobranca escondidas
- **Recuse** - clareza total

### Misdirection
- Design que distrai do opt-out
- Cores que confundem (botao X eh verde, confirmar eh cinza)
- **Recuse** - hierarquia visual honesta

### Friend Spam
- "Compartilhe com amigos para ganhar" - na verdade eh spam
- **Recuse**

### Bait and Switch
- Propaganda diz uma coisa, entrega outra
- **Recuse**

### Disguised Ads
- Anuncios que parecem conteudo
- **Recuse** - rotule claramente

### Price Comparison Prevention
- Dificultar comparar precos
- Esconder competidores
- **Recuse** - transparencia

### FOMO Artificial
- "Outros 23 usuarios compraram hoje"
- **Recuse** - dados reais, nao inventados

## Checklist Antes de Lançar UI

- [ ] Botoes de cancelar/sair sao claros e faceis
- [ ] Precos estao todos visiveis ANTES do checkout
- [ ] Nenhuma urgencia fabricada
- [ ] Nenhuma contagem fake de usuarios
- [ ] Hierarquia visual nao engana
- [ ] Opt-in eh opt-in (nao pre-marcado)
- [ ] Termos de uso sao claros
- [ ] Saida de assinatura eh 1-clique
- [ ] Sem confirm-shaming

## Quando Recusar

Se alguem pedir:
- "Adiciona um countdown que reinicia"
- "Faz o botao de cancelar pequeno"
- "Esconde a taxa de cancelamento"
- "Mostra que 'X pessoas estao olhando' mesmo que nao esteja"

Responda:
> "Nao faco. Isso eh dark pattern. Posso sugerir alternativas que engajam sem enganar."

## Alternativas Eticas para Engagement

Em vez de urgencia falsa:
- Ofertas reais com prazo real
- Notificacoes opt-in

Em vez de exit-intent com medo:
- Exit-intent com oferta real

Em vez de contagem fake:
- Mostrar demanda real (vagas disponiveis, etc)
- Ou nao mostrar nada

Em vez de friend spam:
- Programa de referral com consentimento explicito
- Compensacao por cada amigo que REALMENTE se cadastrar

## Output

```
UX REVIEW - [feature]

DARK PATTERNS ENCONTRADOS:
1. [ ] [nome do pattern] - [localizacao]
   - Por que: [explicacao]
   - Fix: [solucao etica]
   - Esforco: [baixo / medio / alto]

OK:
- Cancelamento: 1-clique ✅
- Precos: visiveis ✅
- Opt-in: nao pre-marcado ✅
- Sem contagem fake ✅

VEREDITO: APROVAR / REJEITAR
```
