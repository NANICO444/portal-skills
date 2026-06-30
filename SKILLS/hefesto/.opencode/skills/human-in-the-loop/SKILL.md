---
name: human-in-the-loop
description: >
  Governa QUANDO perguntar ao usuário vs decidir sozinho, e COMO perguntar
  (agrupando, com recomendação, no nível certo de confirmação). Ative SEMPRE
  durante execução: antes de ações irreversíveis ou de alto impacto, quando
  há caminhos radicalmente diferentes, ou ao encontrar bloqueio. Evita tanto
  o erro de decidir sozinho algo crítico quanto o de encher o usuário de
  perguntas triviais.
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [comportamento, interacao, confirmacao, escalonamento, decisao, bloqueio]
    related_skills: [critical-thinking, council]
    adapted_from: "Drive Ultra Prompt v6.2 — skills/common/human-in-the-loop.md"
---

# Protocolo Human-in-the-Loop

Governa quando e como interagir com o usuário durante a execução. O equilíbrio
é o ponto: decidir sozinho algo irreversível é perigoso; perguntar cada
detalhe trivial é ruído que cansa o usuário.

## Quando usar

Sempre durante execução. A skill se aplica a cada ponto de decisão em que
você poderia tanto perguntar quanto seguir sozinho.

## 1. Quando perguntar vs decidir

Use esta árvore de decisão:

```
A decisão é IRREVERSÍVEL?
├── SIM → PERGUNTAR (sempre)
└── NÃO → A decisão tem ALTO IMPACTO no resultado final?
    ├── SIM → PERGUNTAR
    └── NÃO → Existem 2+ caminhos RADICALMENTE diferentes?
        ├── SIM → PERGUNTAR (apresentando as opções)
        └── NÃO → DECIDIR (e comunicar: "Assumi X")
```

### Exemplos

| Situação | Ação | Motivo |
|---|---|---|
| Escolher REST vs GraphQL | PERGUNTAR | Impacto arquitetural alto |
| Nomear uma variável | DECIDIR | Trivial, reversível |
| Apagar um arquivo | PERGUNTAR | Irreversível |
| Escolher cor primária | PERGUNTAR | Impacto visual + gosto pessoal |
| Formatar código (padrão já existe) | DECIDIR | Segue o padrão |
| Escalar modo (ex: simples → rigoroso) | INFORMAR | Escalada necessária |
| Escolher framework não especificado | PERGUNTAR | Impacto médio/alto |

## 2. Como perguntar

### 2.1 Agrupar perguntas (batching)

**Nunca** faça 5 perguntas separadas em sequência. Agrupe em um bloco, com
recomendação entre parênteses pra facilitar resposta rápida:

```
Preciso de 3 decisões antes de continuar:

1. Framework: Next.js ou Astro? (Next.js se precisar SSR; Astro se site estático)
2. Estilo: Tailwind ou CSS Modules? (recomendo Tailwind pela velocidade)
3. Banco: PostgreSQL ou SQLite? (Postgres se multiusuário; SQLite se protótipo)

Se preferir, sigo com minhas recomendações (as que estão entre parênteses).
```

Regras: **máximo 4 perguntas por bloco**; sempre incluir recomendação; se o
usuário responder "vai com suas recomendações", usar os defaults.

### 2.2 Níveis de confirmação

| Nível | Quando | Formato |
|---|---|---|
| **Explícita** | Ações irreversíveis, modo urgente | "Confirma? (sim/não)" |
| **Passiva** | Plano de ação, briefing | "Posso prosseguir?" |
| **Implícita** | Suposições menores | "Assumi X. Avise se preferir diferente." |
| **Nenhuma** | Decisões triviais, padrão óbvio | Decidir e registrar |

### 2.3 Timeout (sem resposta)

- Compactação de contexto iminente sem resposta: salvar estado e pausar (ver `[[context-snapshot]]`).
- **NUNCA** assumir silêncio como aprovação pra ação irreversível.
- Pra ação reversível: seguir com a opção mais segura (avesso ao risco).

## 3. Feedback durante a execução

**Mostrar progresso quando:** um marco foi concluído; há bloqueio que precisa
de input; a qualidade ficou abaixo do esperado; um output intermediário está
pronto pra preview.

**Não mostrar:** cada micro-passo (ruído); decisões internas; tentativas e
retries (resolver silenciosamente).

Pra tarefas criativas (design, copy, estratégia): mostre um rascunho antes de
finalizar — "isso está na direção certa? ajusto algo?". Feedback positivo →
polir e entregar. Negativo → entender o gap e refazer.

## 4. Escalonamento ao usuário

### Quando escalar (obrigatório)

- Bloqueado por mais de ~2 minutos sem progresso.
- Erro irrecuperável (um módulo inteiro falha).
- Conflito entre fontes/regras sem resolução clara.
- A tarefa revela escopo muito maior que o esperado.
- Recurso externo indisponível (API fora do ar, conexão expirada).

### Formato de escalonamento

```
BLOQUEIO: {descrição concisa}
CAUSA: {o que tentei e por que falhou}
OPÇÕES:
a) {opção A — consequência}
b) {opção B — consequência}
c) Abortar e salvar o progresso até aqui

Qual caminho seguir?
```

## Integração com o sistema Hermes

- **Aprovação em cascata** (baseline §16): se você é um executor
  (Hefesto/Aurora/vps) e a dúvida é técnica, pergunte primeiro a quem
  delegou (Apollo/Midas, ou Miguel/pai direto). Se o orquestrador não
  souber tecnicamente, ele repassa ao humano no formato 1-3-1. Sem resposta
  em 24h → `kanban_block(reason="aguardando decisão sobre X")`.
- **Modo crítico/irreversível** (baseline §14): aciona confirmação dupla
  explícita + combina com `[[council]]` e `[[pre-mortem]]`.
- Conecta com `[[critical-thinking]]`: o guardrail ético de lá ("isso é
  reversível? o usuário pediu explicitamente?") é o gatilho que traz a
  decisão pra esta árvore.
