---
name: council
description: >
  Convoca um conselho de 4 vozes para decisões ambíguas, trade-offs e
  chamadas de seguir/não-seguir (go/no-go). Ative quando existem múltiplos
  caminhos válidos sem vencedor óbvio, quando o usuário pede segunda opinião,
  dissenso ou "vê isso por vários ângulos", ou antes de decisão crítica. Não
  é pra revisão de código, planejamento de implementação ou design de
  arquitetura — é pra DECIDIR sob ambiguidade. Trigger: /council.
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [raciocinio, decisao, conselho, trade-offs, dissenso, go-no-go]
    related_skills: [critical-thinking, pre-mortem, human-in-the-loop]
    adapted_from: "affaan-m/everything-claude-code — skills/council"
---

# Conselho (Council)

Convoca quatro vozes para uma decisão ambígua. O valor não é a unanimidade —
é tornar o **desacordo legível** antes de escolher. A primeira ideia ancorada
na conversa costuma ser fraca; o conselho quebra essa âncora.

## Quando usar

- A decisão tem vários caminhos críveis e nenhum vencedor óbvio.
- É preciso explicitar os trade-offs.
- O usuário pede segunda opinião, dissenso ou múltiplas perspectivas.
- Há risco real de ancoragem (você já "se apegou" a uma resposta).
- Uma chamada go/no-go se beneficiaria de desafio adversarial.

**Ativação por cérebro** (baseline §3): Apollo e Midas ativam por padrão em
decisões; os demais cérebros, sob demanda. O usuário nunca é obrigado — o
cérebro sugere o `/council` quando ajuda.

## Quando NÃO usar

| Em vez de council | Use |
|---|---|
| Verificar se o output está correto | `[[verification-before-completion]]` |
| Quebrar feature em passos de implementação | skill de planejamento (`plan`/`writing-plans`) |
| Revisar código (bugs, segurança) | `code-review-checklist` / `security-review` |
| Pergunta factual direta | responda direto |
| Tarefa de execução óbvia | só execute |

## As 4 vozes

| Voz | Lente |
|---|---|
| **Pragmático** | velocidade de entrega, impacto no usuário, realidade operacional |
| **Cético** | desafia a premissa, simplifica, quebra suposições |
| **Idealista** | a melhor solução possível, correção e implicações de longo prazo |
| **Técnico** | viabilidade técnica, edge cases, modos de falha, risco de downside |

## Como fazer

### 1. Extrair a pergunta real

Reduza a decisão a um enunciado explícito: o que estamos decidindo? Quais
restrições importam? O que conta como sucesso? Se estiver vago, faça **uma**
pergunta de esclarecimento antes de convocar.

### 2. Reunir só o contexto necessário

Se a decisão é específica do código/projeto: junte os trechos/métricas
relevantes, compactos. Se é estratégica/geral: pule trechos de repo a não ser
que mudem a resposta.

### 3. Formar a sua posição inicial PRIMEIRO

Antes de ouvir as outras vozes, escreva sua posição inicial, as 3 razões mais
fortes a favor, e o maior risco do seu caminho preferido. Isso evita que a
síntese final só espelhe as vozes externas.

### 4. Abrir as outras vozes de forma independente (anti-ancoragem)

Cada voz deve receber **apenas a pergunta + o contexto relevante** — nunca a
conversa inteira. Esse isolamento é o mecanismo anti-ancoragem.

- Se o cérebro tem capacidade de subagente disponível, abra cada voz como um
  processo independente com contexto limitado.
- Se não tiver, raciocine cada papel de forma deliberadamente isolada,
  respondendo cada um a partir só da pergunta + contexto (sem deixar uma voz
  contaminar a outra).

Formato pedido a cada voz:

```
Você é a voz [PAPEL] de um conselho de decisão de 4 vozes.

Pergunta:
[a pergunta da decisão]

Contexto:
[só os trechos/restrições relevantes]

Responda com:
1. Posição — 1-2 frases
2. Raciocínio — 3 bullets concisos
3. Risco — o maior risco da sua recomendação
4. Surpresa — uma coisa que as outras vozes podem estar ignorando

Seja direto. Sem hedging. Até 300 palavras.
```

### 5. Sintetizar com guardrails de viés

Você é participante E sintetizador, então:

- Não descarte uma voz externa sem explicar por quê.
- Se uma voz externa mudou sua recomendação, diga isso explicitamente.
- Sempre inclua o dissenso mais forte, mesmo que você o rejeite.
- Se duas vozes convergem contra sua posição inicial, trate como sinal real.
- Mantenha as posições cruas visíveis antes do veredito.

### 6. Apresentar veredito compacto

```markdown
## Conselho: [título curto da decisão]

**Pragmático:** [posição 1-2 frases] — [1 linha do porquê]
**Cético:** [posição] — [1 linha]
**Idealista:** [posição] — [1 linha]
**Técnico:** [posição] — [1 linha]

### Veredito
- **Consenso:** [onde concordam]
- **Dissenso mais forte:** [a discordância mais importante]
- **Checagem de premissa:** [o Cético desafiou a própria pergunta?]
- **Recomendação:** [o caminho sintetizado]
```

## Anti-padrões

- Usar council pra revisão de código ou tarefa de execução.
- Alimentar as vozes com a transcrição inteira da conversa (mata o anti-ancoragem).
- Esconder o desacordo no veredito final.
- Convocar o conselho pra decisão trivial e reversível.

## Integração Hermes

- Trigger nativo `/council` (baseline §13). Combina em sequência com
  `[[pre-mortem]]` (antecipar falhas do caminho escolhido) e
  `[[critical-thinking]]` (gerar as alternativas que o conselho avalia).
- Em modo crítico/irreversível (baseline §14), o council ativa
  automaticamente junto com a confirmação dupla de `[[human-in-the-loop]]`.
- Persistência: só registre o resultado se ele mudar algo real (uma decisão
  de longo prazo, uma política). Decisão trivial não vira registro.
