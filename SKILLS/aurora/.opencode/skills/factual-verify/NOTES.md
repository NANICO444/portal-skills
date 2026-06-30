# NOTES — factual-verify

**Tipo**: 🆕 criar do zero
**Fonte da spec**: common_baseline §2.3 (Factual) + §2.4 (4 níveis de confiança) + §2.5 (5 protocolos anti-alucinação HARD). Também §6 (hierarquia de conflito — protocolos são supremos).
**Catálogo**: `factual-verify | NotFound` — sem origem baixável. Criar do zero está correto.

## O que fiz
- Construí 100% a partir do baseline (§2.3/2.4/2.5/6), sem inventar nada fora da spec.
- Estruturei: 4 níveis (tabela literal §2.4), distinção fonte interna vs web (§2.4), 5 protocolos literais (§2.5), procedimento passo-a-passo, exemplo alucinado vs honesto, relação com anti-glaze.
- O exemplo usa um caso meta (estatística inventada sobre LLMs) pra deixar o protocolo #2 e #3 concretos.
- Links: `[[documentation-lookup]]`, `[[verification-before-completion]]`, `[[anti-glaze]]` — o trio de honestidade do sistema.

## Checklist model-agnóstico
- [x] Sem sintaxe Claude-específica.
- [x] Procedural + tabela + exemplo.
- [x] Um DeepSeek seguiria sem problema. (Especialmente relevante: o _DEEPSEEK_BASICS.md notou que JSON do DeepSeek não é 100% garantido e que ele pode "occasionally return empty content" — a disciplina factual aqui ajuda o executor a marcar INCERTO em vez de preencher lacuna com invenção.)

## Pendências [VALIDAR]
- [VALIDAR: sobreposição com submit-improvement / verification] — factual-verify (fatos), verification-before-completion (status de trabalho) e anti-glaze (tom) se reforçam. Confirmar que ter as 3 separadas é desejado vs fundir. Minha recomendação: manter separadas — disparam em contextos diferentes (afirmar fato / fechar tarefa / dar feedback).
- Nenhum ponto sensível.
