# Hefesto Para Kiro IDE - Desenho Aplicado

## Objetivo

Criar um pacote portatil de workspace para o Kiro IDE em que Hefesto seja o agente principal de engenharia, adaptado para PC Windows local e independente de qualquer sistema de agentes externo.

## Requisitos Recebidos

- Uma pasta independente para Hefesto, separada da pasta Aurora.
- Futuras trocas entre os dois perfis serao configuradas manualmente pelo usuario.
- Nenhum arquivo do perfil original pode ser modificado.
- O pacote deve poder ser transferido para outro local do computador.
- A estrutura deve seguir uma sessao ativa do Kiro IDE como modelo.

## Arquitetura

- `AGENTS.md`: identidade principal sempre presente no workspace.
- `.kiro/steering/`: regras permanentes e regras ativadas por contexto.
- `.kiro/skills/`: processos de engenharia acionaveis.
- `.kiro/agents/hefesto.md`: subagente opcional para tarefa isolada.
- `.kiro/hooks/`: gate manual desativado por padrao.
- `referencias/`: origem, mapeamento e futuro intercambio manual.

## Adaptacao

Mantido do perfil original:

- implementacao rigorosa;
- testes, diagnostico, revisao, APIs, banco de dados e documentacao;
- verificacao objetiva antes de concluir;
- cautela com seguranca, mudancas de contrato e operacoes de producao.

Removido:

- dependencias de perfis externos;
- servidor remoto, bridge, comunicacao automatica e caminhos Linux;
- ferramentas ou integracoes externas como requisito.

## Criterios De Aceite

- O pacote existe somente em `G:\Hefesto_Kiro_IDE` e seu ZIP portatil.
- O original permanece com o mesmo conjunto de arquivos e hash agregado.
- Hefesto atua como orientacao principal no Kiro IDE por workspace.
- Skills cobrem engenharia, testes, debug, seguranca, dados, API e entrega.
