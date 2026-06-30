---
name: hefesto-api-design
description: Definir ou alterar API REST, GraphQL ou contratos internos com compatibilidade, validacao, erros e documentacao. Use quando interfaces entre sistemas mudarem.
---

# Design De API

- Descreva consumidor, operacao, entrada, saida, erros e autorizacao.
- Preserve compatibilidade quando possivel; identifique quebra explicitamente.
- Valide entrada e nao exponha detalhes sensiveis em resposta.
- Mantenha contrato perto do codigo ou na documentacao usada pelo projeto.
- Adicione testes para casos principais e falhas relevantes.

Se outro projeto consumir a API futuramente, gere um contrato copiavel para intercambio manual.
