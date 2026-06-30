---
name: token-budget-advisor
description: >
  Recomenda (não impõe) um orçamento de tokens e qual modelo usar antes de
  uma tarefa cara: estima o tamanho do contexto, sugere MODELO_B/Flash pra
  tarefas simples e MODELO_A/Pro pra tarefas difíceis, e alerta quando o
  contexto está crescendo demais. Ative antes de tarefas grandes (processar
  muitos arquivos, pesquisa longa, geração extensa), ao escolher entre os
  modelos, ou quando o custo/contexto vira preocupação.
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [meta, tokens, orcamento, custo, roteamento-modelo, contexto]
    related_skills: [context-snapshot, find-skills]
prerequisites:
  python: ">=3.8"
---

# Token Budget Advisor

Recomenda um orçamento de tokens e o modelo adequado **antes** de uma tarefa
cara. É um conselheiro, não um portão: sugere e alerta, mas a decisão final é
de quem está executando ou de quem delegou. O objetivo é evitar dois
desperdícios — usar o modelo caro (MODELO_A/Pro) numa tarefa que o barato
(MODELO_B/Flash) resolveria, e deixar o contexto inchar até forçar
compactação no meio de algo importante.

## Quando usar

- Antes de uma tarefa grande: processar muitos arquivos, pesquisa longa,
  geração de artefato extenso, varredura de repositório.
- Ao decidir entre MODELO_A (Pro) e MODELO_B (Flash) pra uma subtarefa.
- Quando o contexto da sessão está crescendo e a compactação se aproxima.

Para tarefas pequenas e óbvias, não rode o advisor — é overhead desnecessário
(Karpathy: o mínimo que resolve).

## Modelos do sistema (referência)

Do `_DEEPSEEK_BASICS.md` (auditoria desta sessão):

| Papel | Modelo | Janela | Posição |
|---|---|---|---|
| **MODELO_A** | DeepSeek V4 Pro | 1M tokens | Raciocínio profundo, tarefas difíceis, código complexo |
| **MODELO_B** | DeepSeek V4 Flash | 1M tokens | Tarefas simples, repetitivas, alto volume, sensíveis a custo/latência |

> O custo do Pro é várias vezes o do Flash, e há promoção temporária — por isso
> esta skill **não embute preço**. Decida por papel (difícil → A, simples → B),
> não por número de preço hardcoded. [VALIDAR: preços DeepSeek mudam]

## Como recomendar

1. **Classifique a complexidade da tarefa:**
   - **Simples**: passo único, transformação mecânica, extração, formatação,
     resumo curto, classificação. → recomende **MODELO_B (Flash)**.
   - **Difícil**: raciocínio multi-passo, decisão arquitetural, código não
     trivial, síntese de muitas fontes, depuração. → recomende **MODELO_A (Pro)**.

2. **Estime o orçamento de entrada.** Some o tamanho estimado do contexto que
   a tarefa vai puxar (arquivos, histórico, docs). Regra de bolso: ~4
   caracteres por token. Use o helper `implementation.py` pra estimar.

3. **Compare com a janela.** A janela é 1M tokens — generosa, mas custo escala
   com tokens. Se a entrada estimada passar de ~50% da janela OU a tarefa for
   gerar saída muito longa, sugira dividir/paginar a tarefa.

4. **Alerte sobre compactação.** Se a sessão já está grande e a tarefa vai
   adicionar muito, recomende rodar `[[context-snapshot]]` ANTES (baseline
   §15.3 #14: nunca compactar sem snapshot).

5. **Apresente a recomendação como conselho**, no formato abaixo. Nunca
   bloqueie a tarefa — quem decide é o executor/orquestrador.

```
ORÇAMENTO SUGERIDO
- Complexidade: [simples|difícil]
- Modelo recomendado: [MODELO_B/Flash | MODELO_A/Pro] — [motivo em 1 linha]
- Entrada estimada: ~N tokens (~X% da janela de 1M)
- Saída esperada: [curta|média|longa]
- Alerta: [dividir tarefa? rodar context-snapshot antes? nenhum]
```

## Helper

`implementation.py` faz a estimativa de tokens e a recomendação de modelo a
partir de uma descrição/tamanho. Uso:

```bash
python implementation.py --chars 48000 --complexity simples
python implementation.py --file caminho/arquivo.txt --complexity dificil
```

Ele imprime o bloco "ORÇAMENTO SUGERIDO". É uma estimativa grosseira
(heurística de ~4 chars/token), não um contador exato — serve pra ordem de
grandeza e roteamento, não pra cobrança.

## Limites

- **Recomenda, não impõe.** Nunca recuse executar por causa do orçamento.
- **Não embute preço** (volátil — ver acima).
- A estimativa de tokens é aproximada; trate como sinal, não como medição.
