# Aurora Para Kiro IDE - Pacote De Workspace

Este pacote transforma um projeto aberto no **Kiro IDE** em um workspace orientado pela **Aurora**: design e experiencia visual como prioridade, com autonomia para programar o que for necessario no projeto local.

Ele foi preparado para ser transferido para outro local do PC e instalado por projeto. Ele **nao altera** a configuracao global do Kiro e **nao altera** o perfil original do Hermes.

## O Que Existe Aqui

```text
Aurora_Kiro_IDE/
|-- AGENTS.md
|-- .kiro/
|   |-- agents/aurora.md
|   |-- steering/
|   |-- skills/
|   `-- hooks/
|-- docs/
|-- referencias/
|-- TUTORIAL_PASSO_A_PASSO.md
|-- INTEROPERABILIDADE_MANUAL_FUTURA.md
`-- PROMPT_CODEX_INSTALAR_AURORA.md
```

- `AGENTS.md`: faz Aurora orientar o agente principal no workspace.
- `.kiro/steering`: reforca identidade, seguranca, design, programacao e verificacao.
- `.kiro/skills`: processos acionaveis por tarefa.
- `.kiro/agents/aurora.md`: subagente opcional para uma analise isolada.
- `.kiro/hooks`: um gate manual opcional, desativado por padrao.

## Como Usar Rapido

### Opcao A - Abrir Este Template No Kiro

1. Copie a pasta `Aurora_Kiro_IDE` para o local definitivo desejado.
2. Abra essa pasta no Kiro IDE.
3. Use o chat para criar um projeto novo dentro dela ou adicionar os arquivos do seu projeto.
4. Comece com:

```text
Aurora, leia o workspace atual e me diga qual stack encontrou, quais skills voce ativaria e qual seria o primeiro passo para: <seu objetivo>.
```

### Opcao B - Instalar Em Um Projeto Existente

1. Feche ou pause alteracoes em andamento no projeto de destino.
2. Verifique se o projeto ja possui `AGENTS.md` ou `.kiro`.
3. Se nao possuir, copie `AGENTS.md` e a pasta `.kiro` deste pacote para a raiz do projeto.
4. Se ja possuir, nao sobrescreva: combine as instrucoes manualmente ou use o prompt `PROMPT_CODEX_INSTALAR_AURORA.md`.
5. Abra o projeto de destino no Kiro IDE.

Veja comandos e verificacoes no [TUTORIAL_PASSO_A_PASSO.md](TUTORIAL_PASSO_A_PASSO.md).

## Como Pedir Trabalho

Pedidos gerais usam Aurora automaticamente por causa de `AGENTS.md`.

Exemplos:

```text
Crie uma landing page responsiva para minha empresa. Antes de codar, apresente tres direcoes visuais.
```

```text
Revise esta tela e corrija problemas de hierarquia, responsividade e acessibilidade. Abra a aplicacao local para validar se for possivel.
```

```text
Implemente o fluxo de cadastro completo, incluindo o backend necessario, mas mantenha o design consistente e valide os estados de erro.
```

Skills podem ser chamadas pelo menu `/` do Kiro:

- `/aurora-design-workflow`
- `/aurora-design-brief`
- `/aurora-frontend-build`
- `/aurora-fullstack-feature`
- `/aurora-visual-qa`
- `/aurora-accessibility-audit`
- `/aurora-delivery`

## Limites Intencionais

- Nao ha Kanban, Discord, VPS nem dependencia do Hermes.
- Nao ha instalacao global em `C:\Users\MASTER-CHIEF\.kiro`.
- Nao ha publicacao automatica nem acesso automatico a credenciais.
- Skills externas citadas pelo Aurora original nao foram fingidas como instaladas; foram adaptadas em skills locais proprias e mapeadas em `referencias/`.
- O intercambio futuro com Hefesto e apenas manual e esta descrito em [INTEROPERABILIDADE_MANUAL_FUTURA.md](INTEROPERABILIDADE_MANUAL_FUTURA.md).

## Documentos Principais

- [TUTORIAL_PASSO_A_PASSO.md](TUTORIAL_PASSO_A_PASSO.md)
- [PESQUISA_KIRO_IDE_E_DECISOES.md](PESQUISA_KIRO_IDE_E_DECISOES.md)
- [PROMPT_CODEX_INSTALAR_AURORA.md](PROMPT_CODEX_INSTALAR_AURORA.md)
- [INTEROPERABILIDADE_MANUAL_FUTURA.md](INTEROPERABILIDADE_MANUAL_FUTURA.md)
- [referencias/MAPEAMENTO_SKILLS_ORIGINAIS.md](referencias/MAPEAMENTO_SKILLS_ORIGINAIS.md)
- [referencias/MAPEAMENTO_PERSONAS.md](referencias/MAPEAMENTO_PERSONAS.md)
- [referencias/ORIGEM_E_PRESERVACAO.md](referencias/ORIGEM_E_PRESERVACAO.md)
