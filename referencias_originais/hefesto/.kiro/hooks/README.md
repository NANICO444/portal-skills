# Hooks Opcionais

O pacote inclui um hook manual de verificacao e ele vem com `"enabled": false`.

Ele nao roda automaticamente apos a copia do pacote. Para usa-lo:

1. Abra o projeto no Kiro IDE.
2. Abra o painel **Agent Hooks**.
3. Habilite `hefesto-quality-gate-manual` somente se quiser dispara-lo manualmente.

O hook nao substitui os testes do projeto e nao deve autorizar deploy, merge ou operacoes destrutivas.
