---
name: aurora-error-recovery
description: Projetar estados de falha, recuperacao, vazio, offline ou dados invalidos em produtos digitais. Use quando a experiencia precisa continuar funcionando diante de erro.
---

# Recuperacao De Erros

Para cada operacao importante, verifique:

- O que o usuario ve enquanto aguarda?
- O que ocorre quando falha?
- A mensagem informa o que aconteceu sem culpar o usuario?
- Ha nova tentativa, retorno seguro ou preservacao de entrada?
- O erro tecnico fica protegido e o log nao revela segredo?

Implemente estados coerentes com os componentes existentes e teste pelo menos um caminho de falha relevante quando possivel.
