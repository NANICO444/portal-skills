# Aurora para Kiro IDE - Desenho Aprovado

## Objetivo

Criar um pacote portatil para transformar um workspace local do Kiro IDE em um ambiente orientado pela Aurora, sem alterar o perfil Hermes original e sem instalar regras globais no Kiro.

## Decisoes Confirmadas

- Uso em PC Windows comum, com projeto local aberto no Kiro IDE.
- Instalacao por workspace: copiar `AGENTS.md` e `.kiro/` para o projeto desejado.
- Aurora e a orientacao principal do workspace, nao apenas um subagente.
- Nao existe Kanban, Discord, VPS, Apollo, Hefesto, Jarvis ou outro perfil.
- Aurora pode programar frontend e backend necessario para entregar o produto.
- O foco continua sendo design, experiencia visual, acessibilidade e qualidade de interface.
- Acoes sensiveis pedem confirmacao: publicacao em producao, uso de credenciais, gastos, exclusao ampla e operacoes irreversiveis.

## Arquitetura Do Pacote

- `AGENTS.md`: regra principal, sempre aplicada pelo Kiro no workspace.
- `.kiro/steering/`: regras persistentes e orientacao condicional.
- `.kiro/skills/`: processos detalhados carregados sob demanda.
- `.kiro/agents/aurora.md`: subagente opcional `/aurora` para uma tarefa isolada.
- `.kiro/hooks/`: validacoes manuais opcionais, desativadas por padrao.
- `referencias/`: mapeamento de origem e decisoes de adaptacao.

## Fonte Local Usada Como Modelo

O Kiro IDE ativo em 2026-05-25 abriu o workspace:

`C:\Users\MASTER-CHIEF\Desktop\Pasta trabalho Kiro\nobrestrade-working-review`

Esse workspace usa `.kiro/steering/*.md` para instrucoes permanentes. O pacote Aurora adota a mesma forma de organizacao, com conteudo proprio e independente.

## Criterios De Aceite

- O pacote existe apenas em `G:\Aurora_Kiro_IDE`.
- O perfil original Hermes permanece inalterado.
- Existe orientacao principal via `AGENTS.md` e steering `always`.
- Skills cobrem fluxo de design, implementacao local, revisao e entrega.
- O tutorial explica instalar em outro projeto sem alterar configuracao global.
- O prompt de continuidade instrui outro Codex a pesquisar, instalar com cuidado e verificar o resultado.
