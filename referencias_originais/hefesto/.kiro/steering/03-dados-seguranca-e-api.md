---
inclusion: auto
name: hefesto-dados-seguranca-api
description: Orientacao ao tocar autenticacao, API, banco de dados, configuracao, upload, integracoes, segredos ou dados do usuario.
---

# Dados, Seguranca E API

- Valide entrada e imponha autorizacao nos limites apropriados.
- Nao coloque segredo no frontend, codigo versionado, log ou mensagem.
- Mudancas de API devem registrar contrato e compatibilidade.
- Migracoes de dados exigem plano de rollback e confirmacao antes de atingir dados reais.
- Operacoes sensiveis exigem testes explicitos ou declaracao clara de impossibilidade.
