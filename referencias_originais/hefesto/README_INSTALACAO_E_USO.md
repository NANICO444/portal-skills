# Hefesto Para Kiro IDE - Pacote De Workspace

Este pacote transforma um projeto aberto no **Kiro IDE** em um workspace orientado pelo **Hefesto**: engenharia de software, diagnostico, testes e entrega tecnica como prioridade, com autonomia para programar no projeto local.

Ele foi preparado para ser movido para outro local do PC e instalado por projeto. Ele **nao altera** configuracao global do Kiro e **nao altera** o perfil original do Hermes.

## O Que Existe Aqui

```text
Hefesto_Kiro_IDE/
|-- AGENTS.md
|-- .kiro/
|   |-- agents/hefesto.md
|   |-- steering/
|   |-- skills/
|   `-- hooks/
|-- docs/
|-- referencias/
|-- TUTORIAL_PASSO_A_PASSO.md
|-- INTEROPERABILIDADE_MANUAL_FUTURA.md
`-- PROMPT_CODEX_INSTALAR_HEFESTO.md
```

- `AGENTS.md`: faz Hefesto orientar o agente principal no workspace.
- `.kiro/steering`: regras permanentes e regras acionadas pelo contexto.
- `.kiro/skills`: processos tecnicos que podem ser chamados no chat.
- `.kiro/agents/hefesto.md`: subagente opcional para tarefa isolada.
- `.kiro/hooks`: gate manual opcional, desativado por padrao.

## Como Usar Rapido

### Opcao A - Abrir Este Template No Kiro

1. Copie a pasta `Hefesto_Kiro_IDE` para o local definitivo.
2. Abra essa pasta no Kiro IDE.
3. Crie ou coloque o projeto dentro dela.
4. Comece com:

```text
Hefesto, leia o workspace atual, identifique stack, testes e riscos, e proponha o primeiro passo para: <seu objetivo>.
```

### Opcao B - Instalar Em Um Projeto Existente

1. Verifique se o projeto ja possui `AGENTS.md` ou `.kiro`.
2. Se nao possuir, copie `AGENTS.md` e a pasta `.kiro` deste pacote para a raiz do projeto.
3. Se ja possuir, nao sobrescreva; combine as regras manualmente ou use `PROMPT_CODEX_INSTALAR_HEFESTO.md`.
4. Abra o projeto no Kiro IDE e confirme que Hefesto foi carregado.

Veja os passos detalhados em [TUTORIAL_PASSO_A_PASSO.md](TUTORIAL_PASSO_A_PASSO.md).

## Pedidos E Skills

Exemplos:

```text
Implemente esta funcionalidade completa, incluindo testes e tratamento de erros. Antes, identifique os arquivos afetados.
```

```text
Investigue este erro local, encontre a causa real e corrija somente depois de demonstrar o problema.
```

Skills uteis no menu `/` do Kiro:

- `/hefesto-codebase-onboarding`
- `/hefesto-feature-implementation`
- `/hefesto-systematic-debugging`
- `/hefesto-api-design`
- `/hefesto-tdd`
- `/hefesto-verification`

## Limites Intencionais

- Nao ha quadro de tarefas, servidor remoto, Discord nem dependencia do Hermes.
- Nao ha instalacao global em `C:\Users\MASTER-CHIEF\.kiro`.
- Nao ha deploy, migracao real, publicacao ou uso de credenciais sem confirmacao.
- O intercambio futuro com Aurora e apenas manual e esta descrito em [INTEROPERABILIDADE_MANUAL_FUTURA.md](INTEROPERABILIDADE_MANUAL_FUTURA.md).

## Documentos Principais

- [TUTORIAL_PASSO_A_PASSO.md](TUTORIAL_PASSO_A_PASSO.md)
- [PESQUISA_KIRO_IDE_E_DECISOES.md](PESQUISA_KIRO_IDE_E_DECISOES.md)
- [PROMPT_CODEX_INSTALAR_HEFESTO.md](PROMPT_CODEX_INSTALAR_HEFESTO.md)
- [referencias/MAPEAMENTO_SKILLS_ORIGINAIS.md](referencias/MAPEAMENTO_SKILLS_ORIGINAIS.md)
- [referencias/ORIGEM_E_PRESERVACAO.md](referencias/ORIGEM_E_PRESERVACAO.md)
