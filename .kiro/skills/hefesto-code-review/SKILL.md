---
name: hefesto-code-review
description: Revisar codigo ou diff procurando bugs, regressao, risco de seguranca e testes ausentes. Use antes de integrar alteracoes ou quando o usuario pedir review.
---

# Revisao De Codigo

Priorize achados por gravidade:

- falha funcional, perda de dados ou quebra de contrato;
- vulnerabilidade, vazamento de segredo ou permissao indevida;
- regressao, concorrencia, estado inconsistente ou erro sem tratamento;
- falta de teste para comportamento arriscado.

Cite arquivo e local preciso. Resumo vem depois dos problemas. Nao aprove uma mudanca apenas por parecer limpa.
