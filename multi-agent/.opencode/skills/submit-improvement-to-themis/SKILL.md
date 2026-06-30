---
name: submit-improvement-to-themis
description: >
  Envia uma sugestão de melhoria do sistema (skill nova, correção de regra,
  drift de config, padrão recorrente, ferramenta útil) pra fila do Themis
  (Conductor) consolidar. Ative quando o cérebro identifica algo que melhoraria
  a si mesmo ou o sistema, mas que NÃO pode aplicar sozinho (instalar skill,
  mudar config, alterar outro cérebro). Empacota a sugestão com evidência e
  manda pro destinatário central — não tenta executar a mudança.
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [meta, melhoria, themis, conductor, sugestao, sistema, universal]
    related_skills: [self-improvement-tracker, find-skills, critique-with-evidence]
---

# Submit Improvement to Themis

Skill universal (todos os cérebros têm). Permite que qualquer cérebro mande
uma sugestão de melhoria pro **Themis** (o Conductor beta) consolidar e
priorizar. O Themis é o único destinatário — todos enviam, só ele recebe (via
a contraparte `improvement-consolidator`, que mantém a fila e detecta
duplicatas).

A razão de existir: nenhum cérebro instala skill, muda config ou altera outro
cérebro sozinho (baseline §15.1 #1). Quando você percebe uma melhoria que está
fora do seu poder de aplicar, você não a executa — você a **propõe** ao canal
certo, com evidência, e segue seu trabalho.

## Quando usar

- Você identificou uma skill que ajudaria (via `[[find-skills]]`) mas não pode instalar.
- Notou uma regra do baseline/playbook desatualizada, contraditória ou com furo.
- Detectou um padrão recorrente que merece virar skill/workflow próprio.
- Encontrou uma ferramenta externa útil que valeria integrar.
- O `[[self-improvement-tracker]]` acumulou fricções que merecem proposta formal.

Não use pra: tarefa normal de trabalho (isso é Kanban), nem pra bug de código
de um projeto (isso é card pro executor). Esta skill é só pra melhorias do
**próprio sistema/cérebros**.

## O que NÃO fazer

- **Não aplique a mudança você mesmo.** Instalar skill, editar config de
  cérebro, mexer em outro workspace — tudo isso é do Themis com aprovação
  humana dupla. Você só propõe.
- **Não envie sugestão sem evidência.** Proposta vaga ("acho que podia
  melhorar") é ruído pro consolidador. Traga o caso concreto.

## Como fazer

O transporte e o schema do pacote são um **contrato fixo** — o lado receptor
(`improvement-consolidator`, custom do Themis) lê exatamente este formato.

1. **Transporte**: criar um card no board `improvements` do Themis (Kanban é
   rastreável; o Themis consome via listagem de cards):

   ```
   kanban_create(
       title="<resumo curto da sugestão>",
       assignee="themis",
       board="improvements",
       body="<o pacote YAML abaixo>"
   )
   ```

2. **Schema do `body`** — produza EXATAMENTE estes campos (nessa ordem):

   ```yaml
   origem_cerebro: <apollo|midas|hefesto|aurora|atlas|themis|...>
   categoria: <seguranca|performance|ux|fluxo|skill|custo|outro>
   problema: "<o que está ruim/faltando hoje — 1-2 frases>"
   sugestao: "<o que melhorar — concreto>"
   evidencia: "<por que — com marcador [VERIFICADO|INFERIDO|INCERTO]>"
   prioridade_sugerida: <baixa|media|alta>
   ```

   O `title` do card = o resumo curto da sugestão.

3. **Registre e siga.** Anote que enviou (pra não duplicar) e volte ao seu
   trabalho. Não fique esperando — o Themis consolida em digest (trigger
   `/themis improvements`) e responde no tempo dele.

## Exemplo

```
kanban_create(
    title="Integrar skill de transcrição de áudio",
    assignee="themis",
    board="improvements",
    body="""
origem_cerebro: apollo
categoria: skill
problema: "Usuário pediu transcrição de áudio 4x esta semana e não temos skill; fiz manual."
sugestao: "Avaliar/instalar 'whisper-transcribe' do ecossistema (achado via find-skills)."
evidencia: "8.2k instalações, fonte vercel-labs, 1.1k estrelas; pedidos nos cards #a12,#a19,#a27,#a31. [VERIFICADO: skills.sh, 2026-05-29]"
prioridade_sugerida: media
"""
)
```

## Integração Hermes

- Destinatário: **Themis** (`hermes-conductor` beta). Receiver:
  `improvement-consolidator` (custom do Themis — fila em
  `/srv/workspace/themis/improvements/queue/`).
- Conecta com `[[self-improvement-tracker]]` (que acumula as fricções que
  viram proposta) e `[[find-skills]]` (que descobre a skill que você propõe).
- **Limite Midas** (baseline §15.4): se for o Midas e a melhoria tocar
  infraestrutura/sistema, ele escala pro Miguel ANTES, não manda direto pro Themis.
