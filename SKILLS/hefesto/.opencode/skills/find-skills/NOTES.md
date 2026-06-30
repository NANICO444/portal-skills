# NOTES — find-skills

**Tipo**: 🆕 marcado no índice, mas o catálogo (§5.1) revela: **INSTALÁVEL/adaptar**, não criar do zero.
**Fonte**: `vercel-labs/skills` — `skills/find-skills/SKILL.md` (verbatim, GitHub main, 2026-05-29).
**Catálogo**: `find-skills | Vercel skills | npx skills add vercel-labs/skills@find-skills | instalar`.

## ⚠️ Decisão criar vs instalar/adaptar (regra §5.1)
O catálogo diz que find-skills É a skill do Vercel — instalável. PORÉM ela NÃO pode ser instalada como está, porque a versão Vercel **instala outras skills** (tem "Step 6: Offer to Install" + `npx skills add ... -g -y`), e o baseline Hermes §15.1 #1 + o prompt mestre Lote A #10 dizem explicitamente: **"busca/recomenda, NÃO instala"**.

**Resolução**: adaptei a base do Vercel REMOVENDO todo o comportamento de auto-install. A skill Hermes:
- usa só comandos de leitura (`npx skills find`, `npx skills add --list`);
- avalia qualidade;
- recomenda e PÁRA;
- escala a instalação pro Conductor/Themis (via submit-improvement-to-themis) em vez de rodar `npx skills add`.

Ou seja: **a base é a do Vercel, mas o output final é uma versão Hermes-segura**. Por isso entreguei um SKILL.md adaptado em vez de só apontar "instala do Vercel" — instalar a versão crua violaria a fronteira do sistema.

## O que adaptei
- PT-BR + frontmatter Hermes.
- Mantive: gatilhos de quando usar, o CLI de busca, os 3 critérios de qualidade (instalações/reputação/estrelas).
- **Removido**: Step 6 (auto-install), flags `-g -y`, `npx skills init`, exemplos de instalação direta.
- **Adicionado**: passo 2 "checar primeiro o que já existe no Hermes" (evita recomendar externo redundante), escalonamento via Themis, links `[[anti-glaze]]`/`[[factual-verify]]` (não inflar qualidade), limites explícitos.

## Checklist model-agnóstico
- [x] Sem sintaxe Claude-específica (a fonte Vercel já era multi-agent).
- [x] Procedural.
- [x] Um DeepSeek seguiria sem problema.

## Pendências [VALIDAR]
- ⚠️ [VALIDAR: instalar a BASE Vercel mesmo?] — duas opções pro Opus: (a) instalar o pacote Vercel `find-skills` e aplicar um override Hermes removendo o auto-install; ou (b) usar este SKILL.md adaptado como a skill definitiva (não instalar a do Vercel). Recomendo (b) — mais limpo e garante a fronteira "não instala". Decisão do Opus.
- [VALIDAR: sintaxe exata de install da base] — catálogo diz `npx skills add vercel-labs/skills@find-skills`; o README do Vercel mostra `--skill find-skills`. Confirmar a forma correta SE optarem por (a).
- [VALIDAR: skills.sh acessível na VPS] — a skill depende de `npx skills find` (rede) e skills.sh. Confirmar acesso de rede na VPS Hermes.
- [VALIDAR: submit-improvement-to-themis como canal de escalonamento] — assumi que é o canal certo pra encaminhar pedido de instalação. Confirmar (essa skill é do Lote B, forward-link).
