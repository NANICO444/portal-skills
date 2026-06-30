# NOTES — strict-type-checking

**Tipo**: 🆕 criar do zero (wrapper — Hefesto)
**Fonte da spec**: hefesto_skills_list #45 "A CRIAR (wrapper que força strict) — mypy strict + pyright + TS strict".
**Base de conceitos**: `wshobson/agents` python-type-safety (busquei verbatim) — usada como referência de conceitos de tipos, NÃO copiada.
**Inventário 771**: não consta → criar wrapper correto.

## O que fiz
- Foco no que a spec pede: FORÇAR strict + disciplina de resolução. Diferenciei da base wshobson (que ENSINA o sistema de tipos) — esta skill CONFIGURA e MANTÉM o strict.
- Configs concretas: mypy strict + pyright strict (pyproject.toml) + TS strict (tsconfig). Recomenda usar mypy E pyright juntos (pegam coisas diferentes).
- O núcleo autoral: **ordem de preferência de resolução** (corrigir tipo > refinar > Any documentado > ignore com código+comentário) + anti-padrão proibido (relaxar a config pra "passar").
- Amarrei a verification-before-completion (evidência), property-based-testing (forma vs lógica), régua RÍGIDA Hefesto.

## Checklist model-agnóstico
- [x] Sem sintaxe Claude-específica.
- [x] Configs/comandos genéricos (mypy/pyright/tsc).
- [x] Um DeepSeek seguiria sem problema.

## Pendências [VALIDAR]
- [VALIDAR: stack TS no MVP] — incluí a parte TS; se MVP for Python-only, fica latente.
- [VALIDAR: flags exatas] — escolhi um conjunto sensato de flags strict-plus (noUncheckedIndexedAccess etc.). Hefesto/Opus podem calibrar quais flags são obrigatórias vs opcionais por projeto.
- Nenhum ponto sensível.
