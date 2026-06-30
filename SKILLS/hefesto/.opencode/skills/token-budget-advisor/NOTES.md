# NOTES — token-budget-advisor

**Tipo**: 🆕 criar do zero (com implementation.py)
**Fonte da spec**: common_baseline §3 #13 (token-budget-advisor — "Built-in concept + ECC fallback") + `_DEEPSEEK_BASICS.md` (modelos, janela, custo Pro vs Flash).
**Catálogo**: `token-budget-advisor | NotFound` — sem origem baixável. Criar do zero está correto.

## O que fiz
- Skill conselheira (recomenda, não impõe — explícito nos limites). Karpathy: mínimo que resolve.
- `implementation.py`: helper Python sem dependências externas, model-agnóstico (não chama API nenhuma). Estima tokens (~4 chars/token), classifica complexidade → modelo (simples=Flash, difícil=Pro), calcula % da janela de 1M, e emite alertas (dividir tarefa, max_tokens, context-snapshot).
- **VERIFICADO nesta sessão**: rodei `implementation.py` com 2 casos (simples/48k e difícil/2.4M chars). Saída correta: roteamento certo, % certo (1.2% e 60%), alertas disparando nos thresholds certos. (Os caracteres estranhos no terminal são só o codepage do console Windows; o arquivo .py é UTF-8 válido.)
- Roteamento por PAPEL, não por preço (preço DeepSeek tem promo temporária e muda — não hardcodei, conforme orientação do Opus no checkpoint 0).

## Checklist model-agnóstico
- [x] Sem sintaxe Claude-específica.
- [x] Helper não depende de nenhum provider; pura heurística.
- [x] Um DeepSeek seguiria sem problema.

## Pendências [VALIDAR]
- [VALIDAR: preços DeepSeek] — deliberadamente NÃO embutidos. Se o sistema quiser estimativa de custo real, precisa de uma tabela de preço externa atualizável (não hardcoded na skill).
- [VALIDAR: heurística 4 chars/token] — é grosseira e pior pra PT-BR/código que pra inglês. Se precisar de precisão, trocar por um tokenizer real (ex: tiktoken) — mas isso adiciona dependência. Mantive simples de propósito.
- [VALIDAR: thresholds dos alertas] — escolhi 50% (dividir), 30% (snapshot). São chutes razoáveis; Opus pode calibrar.
- [VALIDAR: "ECC fallback"] — o baseline §3 menciona "Built-in concept + ECC fallback" mas não achei skill ECC equivalente no catálogo (há `context-budget` no ECC — pode ser a referência). Confirmar se devo me alinhar à ECC `context-budget` ou se a versão custom basta.
