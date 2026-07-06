# Tutorial Passo A Passo - Aurora No Kiro IDE

## 1. Entenda O Tipo De Instalacao

Este pacote usa **escopo de workspace**. Em outras palavras: Aurora so influencia o projeto onde `AGENTS.md` e `.kiro` forem colocados.

Isso e mais seguro que instalar globalmente porque nao muda outros projetos do Kiro.

## 2. Escolha O Destino Final

O pacote foi criado em:

```text
G:\Aurora_Kiro_IDE
```

Voce pode transferir a pasta inteira para outro local do PC. Exemplo:

```powershell
Copy-Item -LiteralPath 'G:\Aurora_Kiro_IDE' -Destination 'D:\Projetos\Aurora_Kiro_IDE' -Recurse
```

O pacote continua funcional depois de transferido porque seus arquivos operacionais usam caminhos relativos ao workspace.

## 3. Instalar Para Criar Projetos Dentro Do Workspace Aurora

1. No Kiro IDE, escolha **Open Folder**.
2. Abra a pasta copiada `Aurora_Kiro_IDE`.
3. Confirme na area **Agent Steering & Skills** que aparecem regras e skills `aurora-*`.
4. No chat do Kiro, envie:

```text
Leia AGENTS.md e as orientacoes Aurora deste workspace. Informe em poucas linhas qual e seu papel, quais limites exigem minha confirmacao e quais skills estao disponiveis para comecar um novo projeto visual.
```

5. Crie ou importe seu codigo dentro desse workspace e trabalhe normalmente.

## 4. Instalar Em Um Projeto Ja Existente

Suponha que seu projeto esteja em `D:\Projetos\MeuSite`.

### 4.1 Verificacao Antes Da Copia

No PowerShell:

```powershell
Test-Path -LiteralPath 'D:\Projetos\MeuSite\AGENTS.md'
Test-Path -LiteralPath 'D:\Projetos\MeuSite\.kiro'
```

- Se ambos retornarem `False`, pode copiar o pacote.
- Se algum retornar `True`, **nao sobrescreva**. Use o prompt para Codex incluido neste pacote para mesclar com cuidado.

### 4.2 Copia Quando Nao Ha Configuracao Existente

```powershell
Copy-Item -LiteralPath 'G:\Aurora_Kiro_IDE\AGENTS.md' -Destination 'D:\Projetos\MeuSite\AGENTS.md'
Copy-Item -LiteralPath 'G:\Aurora_Kiro_IDE\.kiro' -Destination 'D:\Projetos\MeuSite\.kiro' -Recurse
```

### 4.3 Confirmacao Da Copia

```powershell
Test-Path -LiteralPath 'D:\Projetos\MeuSite\AGENTS.md'
Test-Path -LiteralPath 'D:\Projetos\MeuSite\.kiro\steering\00-aurora-identidade.md'
Get-ChildItem -LiteralPath 'D:\Projetos\MeuSite\.kiro\skills' -Directory | Measure-Object
```

## 5. Abrir E Validar No Kiro IDE

1. Abra o projeto de destino no Kiro IDE.
2. Abra **Agent Steering & Skills**.
3. Confirme que as skills com prefixo `aurora-` aparecem.
4. Envie este teste simples:

```text
Qual e sua identidade principal neste workspace e quais acoes voce nao deve executar sem minha confirmacao?
```

A resposta esperada deve mencionar Aurora, foco visual com autonomia de programacao local e confirmacao para publicacao, credenciais, exclusoes amplas ou operacoes irreversiveis.

## 6. Fluxos De Uso

### Projeto Visual Novo

```text
/aurora-design-workflow Crie uma landing page para <produto>. Comece pelo brief e por direcoes visuais antes da implementacao.
```

### Implementacao Completa

```text
/aurora-fullstack-feature Implemente <funcionalidade> com interface, API e persistencia necessarias. Leia a stack real antes de alterar arquivos.
```

### Auditoria De Interface

```text
/aurora-visual-qa Revise a tela atual, identifique problemas por prioridade e corrija os bloqueadores apos explicar o escopo.
```

### Verificacao Final

```text
/aurora-delivery Verifique o trabalho atual e entregue um relatorio com arquivos alterados, testes executados, verificacao visual, limitacoes e riscos.
```

## 7. Subagente Opcional

O arquivo `.kiro\agents\aurora.md` permite chamar:

```text
/aurora Analise esta pagina e proponha correcoes de design e acessibilidade.
```

Use o subagente para tarefas isoladas. A orientacao principal do workspace ja vem de `AGENTS.md` e steering.

## 8. Hook Manual Opcional

Existe um hook em:

```text
.kiro\hooks\aurora-quality-gate-manual.kiro.hook
```

Ele esta desativado por padrao. Para usar, habilite manualmente no painel de hooks do Kiro e dispare apenas quando quiser uma revisao final.

## 9. Remover Aurora De Um Projeto

Se o projeto nao tinha configuracao Kiro propria antes da instalacao:

1. Feche o projeto no Kiro IDE.
2. Remova apenas o `AGENTS.md` copiado e a pasta `.kiro` copiada.

Se os arquivos foram mesclados com configuracao preexistente, nao apague a pasta inteira: remova apenas os arquivos Aurora identificados no relatorio da instalacao.

## 10. O Que Nao Fazer

- Nao copie o perfil Hermes original para dentro do Kiro esperando que funcione sem adaptacao.
- Nao instale globalmente sem querer afetar todos os projetos.
- Nao habilite hooks automaticos sem entender quando executam.
- Nao forneca chaves ou senhas em prompts.
