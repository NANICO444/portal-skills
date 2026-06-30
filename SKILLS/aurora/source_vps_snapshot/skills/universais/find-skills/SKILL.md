---
name: find-skills
description: >
  Descobre e recomenda skills do ecossistema aberto quando o usuário pergunta
  "como eu faço X", "tem uma skill pra X?", "dá pra fazer X?", ou quer estender
  as capacidades do cérebro. Busca no ecossistema, avalia qualidade (instalações,
  reputação da fonte, estrelas) e RECOMENDA — mas NUNCA instala sozinha. A
  instalação é decisão do Conductor/Themis com aprovação humana dupla.
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [meta, descoberta, skills, recomendacao, ecossistema]
    related_skills: [token-budget-advisor, submit-improvement-to-themis]
    adapted_from: "vercel-labs/skills — skills/find-skills (auto-install REMOVIDO)"
prerequisites:
  node: ">=18 (para o CLI npx skills)"
---

# Find Skills (busca e recomenda — NÃO instala)

Ajuda a descobrir skills do ecossistema aberto de agentes. **Diferença crítica
em relação à versão original do Vercel**: no sistema Hermes esta skill **busca e
recomenda, mas NUNCA instala**. Instalar skill é ação estrutural reservada ao
Conductor/Themis, com aprovação humana dupla (baseline §15.1 #1). Qualquer
cérebro que use esta skill pára na recomendação e escala a instalação.

## Quando usar

Ative quando o usuário:

- Pergunta "como eu faço X?" onde X pode ser uma tarefa com skill existente.
- Diz "tem uma skill pra X?" ou "procura uma skill de X".
- Pergunta "você consegue fazer X?" sendo X uma capacidade especializada.
- Quer estender as capacidades do cérebro (design, testes, deploy, etc).

## O CLI de skills

`npx skills` é o gerenciador de pacotes do ecossistema aberto de skills.
Comandos de **leitura/busca** (os únicos que esta skill usa):

- `npx skills find [termo]` — busca skills por palavra-chave.
- `npx skills add <pacote> --list` — lista as skills de um repo SEM instalar.

Catálogo público: https://skills.sh/ [VALIDAR: confirmar URL/acesso na VPS]

> ⚠️ **NÃO use** `npx skills add` (sem `--list`) nem as flags `-g`/`-y`. Esses
> instalam. Esta skill não instala.

## Como fazer

### 1. Entender a necessidade

Identifique: o domínio (React, testes, deploy…), a tarefa específica (escrever
testes, revisar PR…), e se é comum o bastante pra provavelmente existir uma skill.

### 2. Checar primeiro o que já existe no Hermes

Antes de buscar fora, confira se o cérebro já tem (ou o hub Hermes oferece) uma
skill que resolve. Muitas necessidades já estão cobertas pelas skills nativas
(`hermes skills`) ou pelas universais. Não recomende instalar algo externo se
já existe equivalente interno.

### 3. Buscar no ecossistema (só leitura)

```bash
npx skills find [termo]
```
Exemplos: "react performance" → `npx skills find react performance`;
"revisão de PR" → `npx skills find pr review`.

Para inspecionar um repo sem instalar: `npx skills add <owner/repo> --list`.

### 4. Avaliar qualidade ANTES de recomendar

Nunca recomende com base só no resultado de busca. Verifique:

- **Nº de instalações** — prefira 1k+; cautela abaixo de 100.
- **Reputação da fonte** — oficiais (`vercel-labs`, `anthropics`, `microsoft`)
  são mais confiáveis que autores desconhecidos.
- **Estrelas no GitHub** — repo com <100 estrelas merece ceticismo.

Aplica aqui o `[[anti-glaze]]` + `[[factual-verify]]`: não infle a qualidade de
uma skill; cite o número real de instalações/estrelas (verificado), não chute.

### 5. Apresentar a recomendação (e PARAR aqui)

```
Achei uma skill que pode ajudar: "<nome>" — <o que faz>.
Fonte: <owner/repo> · <N> instalações · <M> estrelas.
Verificação de qualidade: [ok / cautela porque ...]

⚠️ Não posso instalar sozinho. Pra instalar, isso precisa ir pro Conductor/Themis
com sua aprovação. Quer que eu encaminhe a sugestão de instalação?
```

### 6. Escalar a instalação (em vez de instalar)

Se o usuário quiser prosseguir, **não rode `npx skills add`**. Em vez disso,
encaminhe via `[[submit-improvement-to-themis]]` (ou avise que depende de
aprovação do Miguel), descrevendo: a skill, a fonte, a verificação de qualidade
e por que ela ajuda. O Conductor/Themis decide e instala com revisão dupla.

## Quando nenhuma skill serve

1. Diga honestamente que não achou skill relevante.
2. Ofereça resolver a tarefa direto com as capacidades atuais do cérebro.
3. Se for recorrente, sugira que vire uma skill própria (proposta via
   `[[submit-improvement-to-themis]]`).

## Limites

- **NÃO instala** (baseline §15.1 #1). Só busca, avalia e recomenda.
- Não usa `npx skills add` sem `--list`, nem `-g`/`-y`.
- Recomendação sempre com qualidade verificada (instalações/estrelas reais).
