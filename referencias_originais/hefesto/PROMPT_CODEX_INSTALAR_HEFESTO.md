# Prompt Para O Codex Pesquisar E Instalar Hefesto Em Outro Projeto

Use o texto abaixo ao pedir que o Codex instale este pacote em outro workspace:

```text
Trabalhe somente com o Kiro IDE instalado neste PC. Primeiro, confirme em documentacao oficial atual como o Kiro IDE carrega AGENTS.md, .kiro/steering, .kiro/skills, .kiro/agents e .kiro/hooks. Depois, inspecione o Kiro local e uma sessao ativa apenas para confirmar a estrutura real usada.

Quero instalar Hefesto como orientacao principal LOCAL do workspace de destino. A fonte do pacote e:
G:\Hefesto_Kiro_IDE

O projeto de destino e:
<COLE_AQUI_O_CAMINHO_DO_PROJETO>

Regras obrigatorias:
- nao modifique nem mova o original em C:\Users\MASTER-CHIEF\Documents\hermes-vps-stack\profiles\hefesto;
- nao instale nada na configuracao global do Kiro;
- nao sobrescreva AGENTS.md ou .kiro existentes sem primeiro listar conflitos e pedir confirmacao;
- mantenha o uso em PC Windows local, sem servidor remoto, quadro de tarefas ou integracoes externas obrigatorias;
- mantenha o hook desativado;
- nao crie comunicacao automatica com outro agente;
- adapte caminhos somente se a instalacao no destino exigir.

Ao finalizar, confirme os arquivos copiados, conte as skills validas, valide que o hook permanece desativado e informe como iniciar Hefesto no Kiro.
```
