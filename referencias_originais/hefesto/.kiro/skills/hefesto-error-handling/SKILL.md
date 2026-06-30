---
name: hefesto-error-handling
description: Estruturar tratamento de falhas, validacao, retries, logs e mensagens sem ocultar problemas nem vazar informacao.
---

# Tratamento De Erros

- Trate falha onde houver contexto suficiente para agir.
- Preserve causa para diagnostico, mas sanitize respostas e logs.
- Evite capturar erro sem acao ou silenciosamente.
- Use retries apenas quando a operacao for segura e a falha temporaria.
- Escreva testes para caminhos de erro importantes.
