---
name: hefesto-verification
description: Executar verificacoes frescas antes de declarar uma mudanca concluida, incluindo testes, build, lint, diff e riscos relevantes.
---

# Verificacao Antes Da Entrega

1. Identifique quais comandos provam o comportamento alterado.
2. Execute os comandos pertinentes e leia o resultado.
3. Revise o diff e confirme que nao ha mudanca fora de escopo nem segredo.
4. Para falhas, reporte o estado real em vez de suavizar o resultado.
5. Somente depois descreva a entrega como validada.

Testes antigos ou nao executados nao contam como evidencia atual.
