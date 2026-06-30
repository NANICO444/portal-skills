# NOTES — karpathy-discipline

**Tipo**: 🆕 criar (adaptando conceito de base externa)
**Fonte**: `multica-ai/andrej-karpathy-skills` — `skills/karpathy-guidelines/SKILL.md` (verbatim, GitHub main, 2026-05-29). Licença: MIT.
**Spec Hermes**: common_baseline §2.1 (os 4 princípios já estão literais lá).

## O que adaptei (não copiei cego)
- A fonte `karpathy-guidelines` tem exatamente os 4 princípios que o baseline §2.1 já adota (Think Before / Simplicity First / Surgical Changes / Goal-Driven). Então a adaptação foi: traduzir pra PT-BR + casar com o nome e a modulação Hermes ("karpathy-discipline", não "karpathy-guidelines").
- Mantive o conteúdo forte da fonte (as 4 seções, a pergunta-teste do sênior, a regra de órfãos, transformar tarefa em objetivo verificável).
- **Integrei com o sistema**: liguei o princípio 3 (cirúrgico) à fronteira §15.3 #15 do baseline (NUNCA apagar código morto preexistente — marcar em DECISIONS.md e perguntar). Liguei princípio 1 a `[[human-in-the-loop]]` e princípio 4 a `[[verification-before-completion]]`.
- **Adicionei** a tabela de modulação por cérebro do baseline §2.1 (Hefesto/vps RÍGIDO, Apollo/Midas NORMAL→RÍGIDO, Aurora criativo→RÍGIDO).
- **Removido**: o link direto pro tweet do Karpathy como dependência. Mantive a atribuição ("derivados das observações de Andrej Karpathy") sem URL, já que o protocolo anti-alucinação manda não citar URL não verificada — e eu não verifiquei o link do tweet nesta sessão. Crédito à fonte fica no NOTES (aqui) e no campo `adapted_from`.

## Checklist model-agnóstico
- [x] Sem sintaxe Claude-específica.
- [x] Procedural + tabela.
- [x] Um DeepSeek seguiria sem problema.

## Pendências [VALIDAR]
- [VALIDAR: sobreposição com critical-thinking] — karpathy princípio 1 (pensar antes) e critical-thinking se tocam. Mantive karpathy focado em EXECUÇÃO/código e critical-thinking em DECISÃO/estratégia. Confirmar que essa divisão é a desejada (ambas são "sempre ativas" no baseline, então conviver é esperado).
- [VALIDAR: atribuição] — incluí "Andrej Karpathy" como origem do conceito sem URL (anti-alucinação). Se quiserem o link do tweet, está no NOTES da fonte original (multica-ai cita `x.com/karpathy/status/...`) — Opus pode validar e reinserir.
