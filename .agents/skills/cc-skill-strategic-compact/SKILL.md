---
name: cc-skill-strategic-compact
description: "Compacta o contexto de conversa estrategicamente antes que o limite de tokens seja atingido, preservando decisoes, estado do projeto, arquivos abertos e tarefas em andamento. Use quando a sessao esta longa (acima de ~70% da janela), antes de handoffs, ou quando o LLM comeca a esquecer instrucoes iniciais."
author: affaan-m
version: "1.0"
---

# Strategic Context Compaction

> **Quando usar:** sessao se aproximando do limite de tokens, antes de handoffs para outra sessao/agente, ou quando instrucoes antigas estao sendo esquecidas.

## O que esta skill faz

Preserva o estado essencial de uma sessao longa em um resumo denso e estruturado, permitindo que o trabalho continue sem perda de contexto critico.

## Quando usar

- A janela de contexto esta acima de ~70% da capacidade
- Antes de delegar para outra sessao ou agente (handoff)
- O LLM comeca a ignorar instrucoes dadas no inicio da conversa
- Sessao acumulou muitos arquivos/edits e precisa de reset estrategico

## Protocolo de compactacao

1. **Inventario** — Liste o que esta em andamento:
   - Tarefa atual e proximos passos
   - Arquivos modificados (caminho + resumo da mudanca)
   - Decisoes tomadas (com racional)
   - Pendencias e bloqueios

2. **Priorize** — Classifique em:
   - **Critico** (deve sobreviver ao reset): decisoes arquiteturais, estado de tarefas, caminhos de arquivos
   - **Util** (manter se couber): contexto tecnico, referencias
   - **Descartavel** (pode ir embora): exploracoes mortas, tentativas falhas, conversa de saudacao

3. **Escreva o resumo** — Formato denso:

   ```
   ## Estado atual
   [1-2 paragrafos do que existe agora]

   ## Tarefa em andamento
   [o que esta sendo feito, em qual arquivo, passo atual]

   ## Proximos passos
   [lista numerada]

   ## Decisoes importantes
   [bullets com decisoes e o porquê]

   ## Arquivos relevantes
   [caminho - o que contem]
   ```

4. **Validacao** — Antes de descartar o contexto antigo, confirme:
   - O resumo permite retomar sem perguntas?
   - Caminhos de arquivo estao completos?
   - Ha dependencias externas (MCPs, variaveis, permissoes) listadas?

## Anti-padroes

- NAO compactar cedo demais (perde contexto util)
- NAO manter tudo (vira so um dump, nao resumo)
- NAO omitir o "porque" das decisoes — so o "o que" nao ajuda na retomada
- NAO esquecer de listar pendencias e bloqueios explicitamente
