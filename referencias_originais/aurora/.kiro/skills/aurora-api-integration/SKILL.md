---
name: aurora-api-integration
description: Integrar interface com APIs locais ou externas, formularios, uploads e dados de produto de forma clara e segura. Use quando uma tela consome ou envia dados.
---

# Integracao De API

- Identifique contrato existente, tipos, autenticacao e comportamento de erro.
- Centralize chamadas no padrao ja adotado pelo projeto.
- Valide dados antes de enviar e trate resposta falha sem deixar a tela travada.
- Mostre feedback util: carregando, sucesso, erro recuperavel e nova tentativa.
- Nao inclua segredos no cliente, logs ou documentacao.
- Para API externa ou credencial nao configurada, solicite confirmacao e instrucao do usuario.

Verifique com teste ou chamada controlada quando possivel; nao presuma funcionamento da integracao.
