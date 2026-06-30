---
name: code-review-checklist
description: >
  Checklist sistemático de revisão de código focado nos pontos cegos que um LLM
  costuma deixar passar (edge cases, segurança, concorrência, tratamento de
  erro, efeitos colaterais). Ative ao revisar um diff/PR — próprio ou de outro
  — antes de aprovar/fechar. Não é nitpick de formatação (isso é linter); é
  caçar bug, risco e dívida que o olho destreinado e o modelo médio ignoram.
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [code-review, qualidade, checklist, anti-blind-spot, hefesto, seguranca]
    related_skills: [verification-before-completion, strict-type-checking, anti-glaze, critique-with-evidence]
    adapted_from: "wshobson/agents — plugins/developer-essentials/skills/code-review-excellence (base de princípios)"
---

# Code Review Checklist (anti-blind-spot)

Revisão de código existe pra pegar bug, risco e dívida — não pra brigar por
formatação (isso é trabalho do linter). Esta skill é um checklist sistemático
focado nos **pontos cegos** que um LLM (e um revisor cansado) costuma deixar
passar: o código "parece certo", compila, e ainda assim quebra num edge case,
vaza um segredo ou cria uma race condition.

Os princípios de *como dar feedback* vêm da base `code-review-excellence` do
wshobson (feedback específico, educativo, não pessoal). O foco Hermes é o
**checklist anti-blind-spot** aplicado ao diff.

## Quando usar

- Ao revisar um PR/diff — próprio (antes de pedir review) ou de outro cérebro.
- Antes de aprovar um merge (baseline §10: PR precisa de diff revisado).
- Faz parte da régua RÍGIDA do Hefesto antes de `kanban_complete`.

## Princípio do feedback (da base wshobson)

- **Específico e acionável**, não "isso está errado".
- **Educa**, não julga; foca no código, não na pessoa.
- **Prioriza**: marque `[crítico]`, `[importante]`, `[nit]`. Nit não bloqueia.
- **Reconhece o que está bom** — mas sem bajular (`[[anti-glaze]]`: elogio só com mérito).

## O checklist anti-blind-spot

Rode o diff contra cada item. Os marcados ⚠️ são os que mais escapam.

### Correção e edge cases ⚠️
```
□ Casos de borda: vazio, nulo/None, zero, negativo, lista de 1, lista enorme
□ Off-by-one em índices/loops/ranges
□ A condição de erro é tratada OU propagada conscientemente (não engolida)?
□ O retorno cobre todos os caminhos (inclusive o "não encontrado")?
□ Mudou comportamento existente sem querer? (verificar o que ANTES funcionava)
```

### Segurança ⚠️
```
□ Input externo é validado/sanitizado antes de usar?
□ SQL/comando montado com concatenação? (injeção) → usar parametrização
□ Segredo/token/credencial hardcoded ou logado? (baseline §15.2 — NUNCA)
□ Dados de terceiros expostos sem mascarar? (CPF, email, cartão)
□ Permissão/autorização checada onde precisa?
```

### Concorrência e estado ⚠️
```
□ Estado compartilhado mutável acessado por mais de um fluxo? (race condition)
□ Recurso aberto é fechado em todos os caminhos (inclusive erro)? (arquivo, conexão)
□ Operação assumida atômica realmente é?
```

### Robustez
```
□ Dependência externa pode falhar/demorar? Tem timeout/retry?
□ Erro tem mensagem útil pra diagnosticar (sem vazar segredo)?
□ Recursos liberados (memória, handles)?
```

### Manutenção e escopo (Karpathy)
```
□ A mudança é cirúrgica? (só o necessário — [[karpathy-discipline]])
□ Apagou código morto PREEXISTENTE sem pedir? (baseline §15.3 #15 — não fazer)
□ Há teste cobrindo a mudança? (o caminho feliz E ao menos um edge case)
□ Nome de variável/função diz o que faz?
□ TODO/FIXME sem card atrelado? (baseline §10 — não permitir)
```

## Como fazer

1. Leia o diff inteiro primeiro (contexto), depois passe o checklist.
2. Para cada achado: anote `[severidade] arquivo:linha — problema + sugestão concreta`.
   Cite evidência (`[[anti-glaze]]`/`[[factual-verify]]` — não invente o problema).
3. Separe **bloqueadores** (crítico/importante) de **nits** (não bloqueiam).
4. Veredito: aprovar / aprovar com ajustes / pedir mudanças — com a razão.

```markdown
## Review: [PR/diff]
**Bloqueadores:**
- [crítico] auth.py:42 — token logado em texto plano → remover o log (vaza segredo)
- [importante] parser.py:88 — não trata lista vazia → IndexError; adicionar guard

**Nits:**
- [nit] utils.py:12 — `uc` → `user_count` pra clareza (não bloqueia)

**O que está bom:** tratamento de retry no client está sólido.
**Veredito:** pedir mudanças (resolver os 2 bloqueadores).
```

## Relação com o sistema

- Pareia com `[[strict-type-checking]]` e `[[verification-before-completion]]`:
  tipos + testes + review = a régua RÍGIDA do Hefesto antes de fechar card.
- Usa `[[anti-glaze]]`/`[[critique-with-evidence]]`: feedback honesto, com
  evidência, sem bajular nem demolir.
- [VALIDAR: alinhar com os anti-patterns do hefesto/playbook §8] — a spec cita
  "base nos 20 anti-patterns do hefesto/playbook §8"; este checklist cobre as
  categorias principais, mas conferir contra a lista literal do playbook quando
  disponível, pra não faltar nenhum.
