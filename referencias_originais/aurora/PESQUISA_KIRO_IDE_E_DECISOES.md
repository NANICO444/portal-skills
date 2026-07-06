# Pesquisa Kiro IDE E Decisoes Do Pacote

## Estado Confirmado No PC

Pesquisa realizada em 2026-05-25:

- Kiro IDE instalado em `C:\Users\MASTER-CHIEF\AppData\Local\Programs\Kiro\Kiro.exe`.
- Versao exibida pelo comando local: `0.12.224`.
- O Kiro IDE estava aberto com uma janela chamada `Analise de emais - Kiro`.
- Os registros atuais do Kiro confirmaram o workspace ativo `C:\Users\MASTER-CHIEF\Desktop\Pasta trabalho Kiro\nobrestrade-working-review`.
- Esse workspace possui `.kiro\steering\*.md` com regras persistentes para o agente.
- A pasta pessoal `C:\Users\MASTER-CHIEF\.kiro` existe, mas este pacote nao a altera.

## O Que A Documentacao Oficial Confirma

| Recurso | Uso Neste Pacote | Confirmacao |
|---|---|---|
| `AGENTS.md` | Identidade principal do workspace | Kiro coleta automaticamente `AGENTS.md` na raiz do workspace e ele e sempre incluido. |
| `.kiro/steering/` | Regras persistentes | Steering de workspace se aplica somente ao workspace; suporta `always` e `auto`. |
| `.kiro/skills/<nome>/SKILL.md` | Fluxos Aurora ativaveis | Skills de workspace sao carregadas sob demanda e aparecem como comandos `/`. |
| `.kiro/agents/aurora.md` | Subagente opcional | Subagentes customizados podem ser definidos no workspace em markdown. |
| `.kiro/hooks/` | Validacao opcional | Hooks executam prompts ou comandos por evento; por seguranca, o pacote deixa o hook desligado. |

## Fontes Oficiais

- Kiro, Steering: https://kiro.dev/docs/steering/
- Kiro, Agent Skills: https://kiro.dev/docs/skills/
- Kiro, Subagents: https://kiro.dev/docs/chat/subagents/
- Kiro, Hooks: https://kiro.dev/docs/hooks/

Paginas consultadas em 2026-05-25.

## Decisoes De Adaptacao

O Aurora original foi desenhado como um perfil do sistema Hermes. Esse formato nao deve ser copiado diretamente para Kiro porque inclui dependencias que nao existem neste uso.

| Do Aurora Original | Decisao No Kiro IDE |
|---|---|
| Perfil Hermes com configuracao propria | Substituido por `AGENTS.md`, steering e skills do workspace. |
| Trabalho em servidor remoto | Substituido por projeto local no Windows. |
| Dependencia de outros perfis para programacao | Removida; Aurora ganha autonomia full stack. |
| Orquestracao externa e repasse de tarefas | Removidos; Aurora conversa diretamente com o usuario. |
| Publicacao controlada | Mantida como limite: exige confirmacao. |
| Foco visual, acessibilidade e revisao critica | Mantidos e reforcados. |

## Observacao Importante

O Kiro IDE nao apresenta uma categoria nativa chamada `persona` igual a organizacao interna do Aurora original. Por isso, as modulacoes relevantes foram convertidas em skills acionaveis e parte da identidade base foi incorporada ao `AGENTS.md`.
