# Pesquisa Do Kiro IDE E Decisoes Para Hefesto

## Kiro Local Confirmado

- Aplicativo usado como alvo: Kiro IDE.
- Executavel encontrado: `C:\Users\MASTER-CHIEF\AppData\Local\Programs\Kiro\Kiro.exe`.
- Versao encontrada durante a pesquisa: `0.12.224`.
- Sessao ativa observada: janela `Analise de emais - Kiro`.
- Modelo local observado: `C:\Users\MASTER-CHIEF\Desktop\Pasta trabalho Kiro\nobrestrade-working-review\.kiro\steering`.

Somente a estrutura desse workspace ativo foi usada como referencia. Seu conteudo nao foi copiado para Hefesto.

## Estrutura Do Kiro Aplicada

- `AGENTS.md` na raiz: orientacao principal sempre presente no workspace.
- `.kiro/steering/*.md`: instrucoes permanentes ou carregadas conforme contexto.
- `.kiro/skills/<nome>/SKILL.md`: skills locais chamadas pelo menu `/`.
- `.kiro/agents/*.md`: agentes personalizados que podem ser chamados explicitamente.
- `.kiro/hooks/*.kiro.hook`: automacoes; neste pacote o unico hook fica desativado.

## Adaptacao De Hefesto

- Mantida autonomia para programacao, teste, debug, revisao, APIs, dados e documentacao.
- Mantido o foco em evidencias e validacao antes de concluir.
- Removidas dependencias de automacao entre agentes, servidor remoto e integracoes externas obrigatorias.
- Limitadas operacoes de risco: producao, segredos, dados reais e instalacao global exigem confirmacao.
- Preparada apenas a possibilidade de intercambio manual futuro, sem configurar comunicacao.

## Fontes Oficiais Consultadas

- Steering: https://kiro.dev/docs/steering/
- Skills: https://kiro.dev/docs/skills/
- Agentes personalizados: https://kiro.dev/docs/chat/subagents/
- Hooks: https://kiro.dev/docs/hooks/
