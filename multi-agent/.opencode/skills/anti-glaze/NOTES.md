# NOTES — anti-glaze

**Tipo**: 🆕 criar do zero
**Fonte da spec**: common_baseline §2.2 (Anti-Glaze) + §5 (vícios de linguagem).
**Catálogo**: `anti-glaze | Custom-to-create` — confirmado que NÃO há repo pronto (origem analisada era um post sem repo). Criar do zero está correto.

## O que fiz
- Construí a skill 100% a partir do common_baseline (§2.2 + §5), sem inventar capacidade fora da spec (regra #4).
- Estruturei: regra central, vícios proibidos (lista literal do §5), vícios fortes (lista literal do §5), exemplo antes/depois, modulação por cérebro (tabela do §2.2), relações com outras skills.
- Exemplo antes/depois é autoral mas usa o mesmo caso (cache) já presente no critical-thinking pra coerência sistêmica.
- Links: `[[critique-with-evidence]]` (Lote B), `[[factual-verify]]`, `[[critical-thinking]]`.

## Checklist model-agnóstico
- [x] Sem sintaxe Claude-específica. (Irônico e relevante: a própria skill-creator da Anthropic tende a injetar exatamente os vícios que esta skill proíbe — revisei pra que a SKILL.md não cometa os vícios que ela condena.)
- [x] Procedural + exemplos.
- [x] Um DeepSeek seguiria sem problema.

## Pendências [VALIDAR]
- [VALIDAR: fronteira anti-glaze vs critique-with-evidence] — defini anti-glaze como o comportamento contínuo de base e critique-with-evidence (Apollo, Lote B) como a versão estruturada sob demanda (/critique). Confirmar que essa divisão de responsabilidade é a desejada, pra não duplicar conteúdo entre as duas.
- Nenhum ponto sensível (sem sudo/AWS/secrets/OAuth).
