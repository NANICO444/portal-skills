# Hooks Opcionais

O pacote inclui apenas um hook manual e ele vem com `"enabled": false`.

Isso evita que o Kiro execute revisoes ou comandos inesperados assim que o pacote for copiado para um projeto.

Para habilitar:

1. Abra o projeto no Kiro IDE.
2. Abra a area **Agent Hooks**.
3. Localize `aurora-quality-gate-manual`.
4. Ative somente se quiser disparar revisoes manualmente antes de entregar.

O hook nao publica, nao instala dependencias e nao deve substituir as verificacoes do projeto.
