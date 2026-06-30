---
name: hefesto-parallel-investigation
description: Dividir uma investigacao em hipoteses independentes, arquivos ou subsistemas quando uma falha tiver varias causas plausiveis.
---

# Investigacao Paralela

- Liste hipoteses distintas e evidencia que confirmaria cada uma.
- Separe leituras ou testes que nao alteram estado.
- Evite duas alteracoes concorrentes no mesmo arquivo ou banco.
- Reuna conclusoes antes de implementar uma correcao.
- Se usar subagentes, limite-os a leitura ou tarefas sem conflito ate a causa ser confirmada.
