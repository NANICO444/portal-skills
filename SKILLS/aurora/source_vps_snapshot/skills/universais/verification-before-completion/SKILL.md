---
name: verification-before-completion
description: >
  Exige evidência fresca antes de afirmar que algo está pronto, corrigido,
  passando ou funcionando. Ative SEMPRE antes de qualquer declaração de
  conclusão, de fechar um card no Kanban, de fazer commit/PR, ou de expressar
  satisfação com o trabalho ("pronto", "feito", "funciona", "deve passar").
  Sem rodar o comando de verificação nesta mesma resposta, não se pode
  afirmar que passou. Use em entregas, fixes, builds, testes e handoffs.
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [qualidade, verificacao, entrega, anti-alucinacao, testes, build]
    related_skills: [factual-verify, critical-thinking]
    adapted_from: "obra/superpowers — skills/verification-before-completion"
---

# Verificação Antes de Concluir

Afirmar que um trabalho está completo sem verificar não é eficiência — é
desonestidade. O princípio central é simples: **evidência antes de afirmação,
sempre**. Violar a letra desta regra é violar o espírito dela.

Esta skill existe porque o executor (qualquer LLM) tende a dizer "pronto"
por inércia ou otimismo, sem checar. O custo disso no sistema é alto: card
fechado errado, retrabalho, perda de confiança de quem delegou.

## Quando usar

Ative **antes** de:

- Qualquer variação de "está pronto / concluído / corrigido / passando / funciona".
- Qualquer expressão de satisfação com o estado do trabalho.
- Fechar card (`kanban_complete`), fazer commit, abrir PR, ou passar pra próxima tarefa.
- Confiar no relatório de "sucesso" de um subagente ou ferramenta.

Não use como desculpa pra rodar verificação infinita em tarefa trivial e
reversível (ex: renomear variável local) — aí a verificação é o próprio
diff. Use o bom senso: quanto mais irreversível ou visível a afirmação,
mais obrigatória a evidência.

## A Lei de Ferro

```
NENHUMA AFIRMAÇÃO DE CONCLUSÃO SEM EVIDÊNCIA DE VERIFICAÇÃO FRESCA
```

Se você não rodou o comando de verificação **nesta mesma mensagem**, você
não pode afirmar que passa. Evidência de uma rodada anterior não conta —
o estado pode ter mudado.

## Como fazer — função de portão (gate)

Antes de afirmar qualquer status, rode estes passos em ordem:

1. **IDENTIFICAR**: qual comando/checagem prova esta afirmação?
2. **RODAR**: execute o comando COMPLETO (fresco, inteiro — não parcial).
3. **LER**: leia a saída inteira, confira o código de saída (exit code), conte falhas.
4. **VERIFICAR**: a saída confirma a afirmação?
   - Se NÃO: declare o status real, com a evidência.
   - Se SIM: faça a afirmação JUNTO com a evidência.
5. **SÓ ENTÃO**: faça a afirmação.

Pular qualquer passo = mentir, não verificar.

## Tabela de evidência mínima

| Afirmação | Exige | NÃO basta |
|---|---|---|
| Testes passam | Saída do comando de teste: 0 falhas | Rodada anterior, "deveria passar" |
| Lint limpo | Saída do linter: 0 erros | Checagem parcial, extrapolação |
| Build funciona | Comando de build: exit 0 | Linter passou, "logs parecem ok" |
| Bug corrigido | Teste do sintoma original: passa | Código mudou, "presumo que corrigiu" |
| Teste de regressão funciona | Ciclo vermelho-verde verificado | Passou uma vez |
| Subagente concluiu | Diff no versionamento mostra a mudança | Subagente "reportou sucesso" |
| Requisitos atendidos | Checklist item a item | "Os testes passam" |

## Sinais de alerta — PARE

- Usar "deveria", "provavelmente", "parece que".
- Expressar satisfação antes de verificar ("ótimo!", "perfeito!", "pronto!").
- Prestes a commitar/abrir PR sem verificação.
- Confiar em relatório de sucesso de subagente sem checar o diff.
- Pensar "só dessa vez não precisa".
- Estar cansado e querer terminar logo.

## Prevenção de racionalização

| Desculpa | Realidade |
|---|---|
| "Deve funcionar agora" | RODE a verificação |
| "Tenho confiança" | Confiança ≠ evidência |
| "Só dessa vez" | Sem exceções |
| "O linter passou" | Linter ≠ compilador |
| "O subagente disse que deu certo" | Verifique de forma independente |
| "Estou cansado" | Cansaço ≠ desculpa |
| "Palavras diferentes, então a regra não vale" | Espírito acima da letra |

## Padrões de verificação

**Testes:**
```
✅ [rodar comando de teste] [ver: 34/34 passam] → "Todos os testes passam"
❌ "Deve passar agora" / "Parece correto"
```

**Teste de regressão (ciclo vermelho-verde):**
```
✅ Escrever → Rodar (passa) → Reverter o fix → Rodar (DEVE FALHAR) → Restaurar → Rodar (passa)
❌ "Escrevi um teste de regressão" (sem o ciclo vermelho-verde)
```

**Build:**
```
✅ [rodar build] [ver: exit 0] → "Build passa"
❌ "O linter passou" (linter não checa compilação)
```

**Requisitos:**
```
✅ Reler o plano/card → montar checklist → verificar cada item → reportar lacunas ou conclusão
❌ "Testes passam, fase completa"
```

## Integração com o sistema Hermes

- Ao fechar card, a evidência vai no campo `metadata.verification` do
  `kanban_complete` — ex: `["pytest tests/x.py -q (3.2s, 14 ok)"]`. A regra
  desta skill é o que produz esse campo. Card sem evidência real de
  verificação não deve ser fechado.
- Conecta com `[[factual-verify]]` (não afirmar fato sem fonte) e com os 5
  protocolos anti-alucinação do baseline: ambos são a mesma disciplina —
  evidência antes de afirmação.
- **Modulação de rigor por cérebro** (do common_baseline): Hefesto e
  hermes-vps em **RÍGIDO** (build + test + lint + diff obrigatórios);
  Aurora em RÍGIDO com build + acessibilidade + checagem visual;
  Apollo/Midas/pipelines em Normal. O rigor maior significa mais checagens
  obrigatórias antes de afirmar, não uma regra diferente.

## Por que isso importa

Quando o executor afirma "pronto" sem evidência e está errado, o card volta,
o tempo de quem delegou é desperdiçado, e a confiança no cérebro cai (e isso
entra na pontuação do sistema de pontos). Rodar o comando, ler a saída, e só
então afirmar é mais barato que o retrabalho. Sem atalho.

## Resumindo

Rode o comando. Leia a saída. **Só então** afirme o resultado.
