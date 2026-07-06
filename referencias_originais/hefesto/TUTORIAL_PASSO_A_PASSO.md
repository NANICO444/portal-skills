# Tutorial - Instalar E Usar Hefesto No Kiro IDE

## 1. Escolha O Projeto

O pacote pode ser usado como pasta de projeto nova ou instalado dentro de um projeto ja existente.

Antes de copiar para um projeto existente, verifique:

```powershell
Test-Path -LiteralPath 'C:\CAMINHO\DO\PROJETO\AGENTS.md'
Test-Path -LiteralPath 'C:\CAMINHO\DO\PROJETO\.kiro'
```

Se qualquer resultado for `True`, nao sobrescreva automaticamente. Abra os arquivos existentes e combine as instrucoes com cuidado.

## 2. Copie Para Um Projeto Sem Configuracao Kiro

Substitua o caminho de destino pelo projeto real:

```powershell
Copy-Item -LiteralPath 'G:\Hefesto_Kiro_IDE\AGENTS.md' -Destination 'C:\CAMINHO\DO\PROJETO\AGENTS.md'
Copy-Item -LiteralPath 'G:\Hefesto_Kiro_IDE\.kiro' -Destination 'C:\CAMINHO\DO\PROJETO\.kiro' -Recurse
```

Para usar o pacote inteiro como base, mova ou copie a pasta `G:\Hefesto_Kiro_IDE` para o local desejado e abra essa pasta diretamente.

## 3. Abra No Kiro IDE

1. Inicie o Kiro IDE.
2. Abra a pasta raiz que contem `AGENTS.md` e `.kiro`.
3. Inicie um novo chat nesse workspace.
4. Envie:

```text
Qual e sua orientacao principal neste workspace? Cite as regras locais e as skills Hefesto que estao disponiveis.
```

O esperado e que a resposta reconheca Hefesto como orientacao principal local.

## 4. Trabalhe Com Hefesto

Pedido geral:

```text
Hefesto, analise este projeto e implemente <funcionalidade>. Antes de editar, descreva arquivos afetados, riscos e validacoes.
```

Skill direta:

```text
/hefesto-systematic-debugging Investigue o erro apresentado ao iniciar a aplicacao.
```

Para concluir uma mudanca:

```text
/hefesto-verification Verifique o que foi alterado e relate testes executados e riscos restantes.
```

## 5. O Que Nao Acontece Automaticamente

- O pacote nao altera o Kiro global.
- O pacote nao altera o Hermes original.
- O hook de qualidade esta desativado por padrao.
- O pacote nao se comunica automaticamente com Aurora.
- Deploy, dados reais e operacoes destrutivas dependem de sua confirmacao.

## 6. Mover O Pacote

Voce pode copiar a pasta inteira ou descompactar o ZIP em outro local do PC. Ao abrir a nova pasta no Kiro, os caminhos internos continuam relativos ao workspace.
