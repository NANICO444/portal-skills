---
name: hefesto-tdd
description: Implementar comportamento novo ou corrigir bug guiado por teste que falha antes da correcao e passa depois. Use quando o projeto possui testes adequados.
---

# Desenvolvimento Guiado Por Testes

1. Identifique o comportamento esperado e o framework de testes real.
2. Escreva o menor teste que demonstra a necessidade.
3. Execute e confirme que falha pelo motivo esperado.
4. Implemente somente o necessario para passar.
5. Execute o teste alterado e o conjunto relacionado.
6. Refatore apenas mantendo os testes verdes.

Se o projeto nao tiver base de testes utilizavel, explique o limite e use verificacao manual ou automatizada disponivel sem afirmar TDD.
