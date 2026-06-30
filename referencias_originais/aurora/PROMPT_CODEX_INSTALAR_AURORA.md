# Prompt Para Codex Instalar Aurora Em Outro Workspace Kiro IDE

Copie o texto abaixo em uma nova conversa do Codex quando quiser instalar este pacote em um projeto real.

```text
TAREFA: instalar o pacote Aurora para Kiro IDE em um workspace local, com validacao e sem sobrescrever configuracoes existentes silenciosamente.

PACOTE FONTE:
<PREENCHER_CAMINHO_DO_PACOTE_AURORA>

PROJETO DESTINO:
<PREENCHER_CAMINHO_DO_PROJETO>

REGRAS OBRIGATORIAS:
1. Trabalhe somente no projeto destino e leia o pacote fonte; nao modifique o pacote fonte.
2. NUNCA altere o perfil Hermes original em:
   C:\Users\MASTER-CHIEF\Documents\hermes-vps-stack\profiles\aurora
3. O alvo e o Kiro IDE, nao o Kiro CLI.
4. Antes de editar, verifique no PC:
   - versao instalada do Kiro IDE;
   - documentacao oficial atual sobre AGENTS.md, steering, skills, subagents e hooks;
   - se o destino ja possui AGENTS.md ou .kiro.
5. Se o destino ja possuir AGENTS.md ou arquivos .kiro com nomes conflitantes, pare antes de sobrescrever e apresente um plano de mescla arquivo a arquivo para aprovacao.
6. Se nao houver conflito, copie para a raiz do projeto destino:
   - AGENTS.md
   - .kiro\steering\
   - .kiro\skills\
   - .kiro\agents\
   - .kiro\hooks\ (mantenha hooks desativados por padrao)
7. Nao instalar nada globalmente em C:\Users\MASTER-CHIEF\.kiro.
8. Nao habilitar deploy, credenciais, integracoes externas, hooks automaticos ou comandos destrutivos.
9. Ao finalizar, valide:
   - existencia de AGENTS.md e das pastas .kiro instaladas;
   - frontmatter valido de todas as skills e nomes iguais as pastas;
   - JSON valido dos hooks;
   - que hooks permanecem desativados;
   - que nao foram alterados arquivos fora do destino.
10. Entregue um relatorio conciso em portugues contendo:
   - caminho do pacote fonte;
   - caminho do destino;
   - arquivos criados ou mesclados;
   - conflitos encontrados;
   - validacoes executadas e resultados;
   - o que ainda precisa ser confirmado pelo usuario.

OBJETIVO DO PERFIL:
Aurora deve ser a orientacao principal do workspace por AGENTS.md e steering. Ela trabalha em PC Windows comum, diretamente no projeto local, sem Kanban, sem VPS, sem Discord e sem depender de outros agentes. Ela tem autonomia para implementar frontend e backend necessario ao produto, mantendo prioridade em design, experiencia visual, acessibilidade, responsividade e verificacao real. Deve pedir autorizacao antes de publicar, acessar credenciais, gastar, excluir em massa ou fazer operacoes irreversiveis.
```
