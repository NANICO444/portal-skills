---
name: hefesto-security-review
description: Revisar autenticacao, autorizacao, entrada, segredo, dependencia, upload, integracao e exposicao de dados em codigo ou configuracao.
---

# Revisao De Seguranca

Verifique:

- segredos em codigo, historico, log e frontend;
- validacao e autorizacao em endpoints;
- injecao, XSS, SSRF, path traversal e upload perigoso conforme aplicavel;
- configuracao insegura e dependencias vulneraveis;
- dados pessoais expostos ou persistidos sem necessidade.

Ao encontrar segredo, informe tipo e local, nunca o valor. Mudancas sensiveis exigem testes e confirmacao antes de producao.
