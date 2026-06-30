# NOTES — property-based-testing

**Tipo**: 🆕 criar do zero (Hefesto)
**Fonte da spec**: hefesto_skills_list #44 "A CRIAR (Hypothesis + fast-check)".
**Inventário 771**: não consta → criar do zero correto.

## O que fiz
- Skill de teste por propriedade: Hypothesis (Python) + fast-check (TS), conforme spec Hefesto.
- Catálogo de propriedades comuns (round-trip, invariante, idempotência, comutatividade, oráculo, nunca-quebra) — o "pulo do gato" é ajudar o executor a IDENTIFICAR a propriedade, que é a parte difícil.
- Exemplos reais em Python e TS. Boas práticas (começar pela invariante, restringir geradores ao domínio, fixar contra-exemplo como regressão).
- Amarrei a test-driven-development (nativo, complementa), verification-before-completion (rodar e ler), strict-type-checking (tipos+lógica).

## Checklist model-agnóstico
- [x] Sem sintaxe Claude-específica.
- [x] Exemplos de código genéricos (pytest/jest), não dependem de modelo.
- [x] Um DeepSeek seguiria sem problema.

## Pendências [VALIDAR]
- [VALIDAR: stack do MVP tem TS?] — incluí fast-check (TS) conforme spec. O hefesto_skills_list nota que typescript-advanced-types é "lazy — ativa só se MVP tiver TS". Se o MVP for Python-only, a metade TS desta skill fica latente (não atrapalha). Confirmar.
- Nenhum ponto sensível.
