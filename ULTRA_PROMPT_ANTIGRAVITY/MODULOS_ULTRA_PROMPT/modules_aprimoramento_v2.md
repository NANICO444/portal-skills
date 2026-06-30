# MODULO: APRIMORAMENTO DE MODULOS
# Ultra Prompt v6.2 — Combo Module Enhancement & Iterative Refinement
# Versao: 1.0.0 | Atualizado: 2026-04-20

---

## 0. QUANDO CARREGAR

Carregar quando usuario pede para: criar novo modulo, melhorar modulo existente, criar nova skill, revisar qualidade de prompts, iterar sobre arquitetura de agentes, ou fazer brainstorming estruturado com sub-agentes.

NAO carregar para: uso normal dos modulos (apenas execucao), tarefas simples, correcoes pontuais.

---

## 0.5 INTEGRACAO COM CORE.MD

Este modulo opera como META-EXECUTOR dentro do core.md:
- Core.md controla alocacao de sub-agentes (5-15, padrao Opus 4.7)
- Este modulo DEFINE o processo de melhoria; core.md EXECUTA a orquestracao
- Monitor Agent (SKILL 03 do core) roda em paralelo — este modulo ADICIONA verificacao de truncamento
- Requer minimo 10 sub-agentes simultaneos para review rounds

---

## 0.6 TOKEN BUDGET

- Modulo em contexto: ~6K tokens
- Skill files (sob demanda): ~2K cada, max 2 simultaneos
- Agent prompts (review rounds): ~1K cada × 10-12 agentes = ~12K efemeros
- Debate gates: ~500 tokens × debates ativos
- **Pico estimado:** ~20K tokens (durante round com 12 agentes + debates)
- **Gestao:** Comprimir rounds anteriores para "score + consenso" apenas. Descartar debates resolvidos.

---

## 1. VISAO GERAL DO PROCESSO

```
FASE 1: BRIEFING (capturar requisitos e contexto)
    ↓
FASE 2: BRAINSTORMING (gerar alternativas com agentes)
    ↓ [DEBATE GATE]
FASE 3: ARQUITETURA (escolher e estruturar)
    ↓ [DEBATE GATE]
FASE 4: PROTOTIPAGEM (escrever v1.0)
    ↓
FASE 5: REVIEW ITERATIVO (N rodadas com M agentes)
    ↓ [DEBATE GATE por rodada]
FASE 6: CONSENSO FINAL (aprovacao unanime)
    ↓
FASE 7: DOCUMENTACAO E ENTREGA
```

---

## 2. FASE 1 — BRIEFING

### Objetivo
Extrair do pedido do usuario TUDO que e necessario para criar/melhorar o modulo.

### Protocolo

```
1. IDENTIFICAR tipo de trabalho:
   - [ ] Novo modulo do zero
   - [ ] Melhoria de modulo existente
   - [ ] Nova skill para modulo existente
   - [ ] Refatoracao de arquitetura

2. EXTRAIR requisitos:
   - Objetivo principal (o que o modulo deve fazer)
   - Publico-alvo (quem vai usar)
   - Restricoes (token budget, compatibilidade, plataforma)
   - Exemplos de uso desejado
   - O que NAO deve mudar (invariantes)

3. MAPEAR contexto existente:
   - Ler core.md (entender orquestracao)
   - Ler modulos relacionados (evitar duplicacao)
   - Ler skills existentes (identificar gaps)
   - Verificar ARCHITECTURE.md (invariantes do sistema)

4. DECLARAR:
   "Briefing: [tipo] | Objetivo: [X] | Restricoes: [Y] | Invariantes: [Z]"
```

---

## 3. FASE 2 — BRAINSTORMING COM AGENTES

### Objetivo
Gerar multiplas alternativas de abordagem antes de escolher uma.

### Protocolo

```
SPAWNAR 5-8 agentes com perspectivas DIFERENTES:

Agente 1: Arquiteto de Prompts — foco em compliance LLM e clareza
Agente 2: Especialista de Dominio — foco em utilidade pratica
Agente 3: Advogado do Diabo — foco em falhas e edge cases
Agente 4: Minimalista — foco em simplicidade e token efficiency
Agente 5: Maximalista — foco em cobertura completa
Agente 6: Usuario Final — foco em experiencia de uso
Agente 7: Integrador — foco em compatibilidade com sistema existente
Agente 8: Inovador — foco em abordagens nao-convencionais

CADA AGENTE deve propor:
1. Abordagem (1-2 paragrafos)
2. Estrutura sugerida (topicos)
3. Riscos da abordagem
4. Estimativa de tokens
```

### Consolidacao

```
Apos receber propostas:
1. Agrupar por similaridade
2. Identificar pontos de consenso (presentes em 5+ propostas)
3. Identificar divergencias criticas
4. Executar DEBATE GATE para resolver divergencias
5. Sintetizar: abordagem hibrida com os melhores elementos
```

---

## 4. FASE 3 — ARQUITETURA

### Objetivo
Definir estrutura final antes de escrever conteudo.

### Protocolo

```
1. DEFINIR componentes:
   - Modulo principal (arquivo .md)
   - Skills necessarias (lista com justificativa)
   - Dependencias externas (outros modulos, core.md sections)

2. DEFINIR estrutura do modulo:
   - Secoes obrigatorias: QUANDO CARREGAR, INTEGRACAO, TOKEN BUDGET, WORKFLOW
   - Secoes especificas do dominio
   - Debate gates (onde inserir checkpoints)
   - Fallbacks (o que fazer se skill indisponivel)

3. DEFINIR skills:
   - Nome + objetivo (1 frase)
   - Quando carregar (fase do workflow)
   - O que extrair (dados especificos)
   - Token budget (~1.5K cada)
   - Prioridade (CRITICA / ALTA / MEDIA)

4. VALIDAR contra invariantes do sistema:
   - [ ] 1 modulo = 1 arquivo = 1 responsabilidade
   - [ ] Modulo e executor, NAO orquestrador
   - [ ] Skills sao on-demand, NAO always-loaded
   - [ ] Token budget < 20K no pico
   - [ ] Sem cross-references entre modulos
   - [ ] Fallback gracioso se skill ausente
```

### Debate Gate: Arquitetura

```
═══ DEBATE GATE: ARQUITETURA ═══
DECIDINDO: Estrutura final do modulo
A FAVOR: [2 argumentos]
CONTRA: [2 riscos]
RISCO 1: [desc] → Mitigacao: [acao]
RISCO 2: [desc] → Mitigacao: [acao]
ALTERNATIVA: [opcao descartada + motivo]
DECISAO: [escolha] | CONFIANCA: [ALTA/MEDIA/BAIXA]
═══ GATE APROVADO ═══
```

---

## 5. FASE 4 — PROTOTIPAGEM

### Objetivo
Escrever v1.0 do modulo e skills com base na arquitetura aprovada.

### Protocolo

```
1. ESCREVER modulo principal:
   - Seguir estrutura definida na Fase 3
   - Usar linguagem imperativa e clara
   - Incluir exemplos concretos (nao abstratos)
   - Definir formatos de output esperados
   - Marcar com [TODO] areas que precisam de dados

2. ESCREVER skills (em paralelo se independentes):
   - Cada skill em arquivo separado
   - Frontmatter: nome, versao, objetivo
   - Conteudo acionavel (tabelas, checklists, decision trees)
   - Max 1.5K-2K tokens cada

3. COMMITAR estado:
   - git init (se necessario)
   - git add -A && git commit -m "feat: initial v1.0 prototype"

4. DECLARAR: "Prototipo v1.0 pronto. [N] tokens modulo, [M] skills criadas."
```

---

## 6. FASE 5 — REVIEW ITERATIVO

### Objetivo
Melhorar qualidade atraves de multiplas rodadas de review com agentes especializados.

### Configuracao

```
PARAMETROS (configuravel pelo usuario):
- MIN_ROUNDS: 5 (padrao) | pode ser 3-20
- MAX_ROUNDS: ate aprovacao unanime ou limite do usuario
- NUM_AGENTS: 10 (padrao) | minimo 5, maximo 15
- SKILL_SCOUT: 1 agente dedicado (agente N+1)
- MONITOR: 1 agente dedicado (verificacao de truncamento)
- APPROVAL_THRESHOLD: score >= 8.0/10 E zero bloqueios
- SKILL_VOTE_THRESHOLD: ceil(NUM_AGENTS * 0.7) votos para aprovar nova skill
- TIMEOUT_PER_AGENT: 10 minutos max (estender para 15 se terminal ativo)
- HARD_TIMEOUT: 20 minutos absoluto (kill e marcar FAILED)

MODO ADAPTATIVO (padrao ligado):
- Se 2 rodadas consecutivas com delta > 1.5: reduzir MIN_ROUNDS em 1 (min 3)
- Se 2 rodadas consecutivas com delta < 0.3: aumentar MIN_ROUNDS em 1 (max 10)
- Se score >= 9.0 antes de MIN_ROUNDS: override, ir para sign-off
- Usuario pode desligar: "modo fixo"

SCALING TIERS (auto-detectado pelo score inicial):
- TIER 1 (score inicial >= 7.0): 3-5 rounds, 8 agents, sem skill scout
- TIER 2 (score inicial 5.0-6.9): 5-8 rounds, 10 agents, skill scout
- TIER 3 (score inicial < 5.0): 10-15 rounds, 12+ agents, skill scout + auditor dedicado
```

### Selecao de Roles (dinamica por modulo)

```
ROLES OBRIGATORIOS (sempre presentes):
- Prompt Engineer (clareza LLM)
- Integration Architect (compatibilidade core.md)
- Devil's Advocate (questionador, busca falhas)

ROLES CONDICIONAIS (por tipo de modulo):
- Tecnico: +Security, QA, Performance, Error Recovery, Dominio #1, Dominio #2
- Conteudo: +Content Strategist, UX Writer, SEO, Accessibility, Brand
- Processo: +Process Designer, DevOps, Error Recovery, QA, UX/Ergonomia

SELECAO: Fase 1 (Briefing) define REQUIRED_ROLES baseado no tipo.
Resultado: painel de 5-12 agentes (NAO fixo em 10).
Usuario pode override: "Incluir [role]" ou "Pular [role]"
```

### Panels Pre-Configurados (referencia)

```
Os slots sao CONFIGURADOS por tipo de modulo:

PARA MODULOS DE CODIGO/TECNICO:
1. Prompt Engineer (clareza LLM)
2. Especialista de Dominio #1 (area principal)
3. Especialista de Dominio #2 (area secundaria)
4. QA/Testing (cobertura, edge cases)
5. Security Expert (vulnerabilidades)
6. Performance (eficiencia, tokens)
7. Error Recovery (falhas, fallbacks)
8. Integration Architect (compatibilidade core.md)
9. UX/Usabilidade (experiencia de quem usa o prompt)
10. Devil's Advocate (questionador, busca falhas)

PARA MODULOS DE CONTEUDO/CREATIVE:
1. Prompt Engineer (clareza LLM)
2. Content Strategist (qualidade de conteudo)
3. Copywriter (tom, persuasao)
4. UX Writer (microcopy, acessibilidade)
5. SEO Specialist (discoverability)
6. Brand Consistency (alinhamento visual/verbal)
7. Accessibility Expert (WCAG, inclusao)
8. Performance (token efficiency)
9. Integration Architect (compatibilidade)
10. Devil's Advocate (questionador)

PARA MODULOS DE PROCESSO/WORKFLOW:
1. Prompt Engineer (clareza LLM)
2. Process Designer (fluxo, eficiencia)
3. Error Recovery (falhas, deadlocks)
4. QA Specialist (completude)
5. DevOps (automacao, deploy)
6. Security (permissoes, dados)
7. UX/Ergonomia (facilidade de uso)
8. Performance (velocidade, tokens)
9. Integration Architect (compatibilidade)
10. Devil's Advocate (questionador)
```

### Protocolo por Rodada

```
PARA CADA RODADA [R]:

1. DISPATCH: Enviar estado atual para todos os N agentes em PARALELO
   - Mecanismo: usar spawn_agent(role, prompt) do core.md Section 6
   - Cada agente recebe: modulo + skills + instrucoes de review (via template em agent-review-patterns.md)
   - Timeout: 10 min por agente (estender para 15 se terminal ativo com output)
   - Hard timeout: 20 min absoluto → kill + marcar FAILED
   - Se timeout: registrar "TIMEOUT" e seguir com os que responderam

2. COLLECT: Aguardar respostas (min ceil(NUM_AGENTS × 0.8) para rodada valida)
   - Com 10 agentes: min 8 | Com 12: min 10 | Com 8: min 7
   - Se mesmo agente timeout 2+ rodadas → substituir por agente reserva
   - Cada agente DEVE retornar neste formato exato:

   FORMATO OBRIGATORIO:
   Score: [N]/10
   Issues:
     1. [secao/linha]: [problema] → Fix: [acao concreta]
     2. [secao/linha]: [problema] → Fix: [acao concreta]
     3. [secao/linha]: [problema] → Fix: [acao concreta]
   Status: APROVADO / PRECISA FIX

   VALIDACAO: Se resposta nao cita secao/linha especifica → peso 0.5x na media

3. SKILL SCOUT (agente N+1): Em paralelo, propoe novas skills
   - Retorna: nome, proposito, gap que preenche, argumentos for/against

4. CONSOLIDATE: Identificar consenso
   - Issue aparece em 3+ agentes → CONSENSO (aplicar)
   - Issue aparece em 1-2 agentes → CONSIDERAR (debater)
   - Skill proposta → VOTAR (ceil(NUM_AGENTS × 0.7) para aprovar)
   - VALIDACAO PRE-APPLY: verificar que fix NAO contradiz:
     a) Invariantes do sistema (ARCHITECTURE.md, core.md)
     b) Requisitos explicitos do briefing (Fase 1)
     c) Se contradiz → BLOQUEAR fix, debater alternativa
   - ANTI-FALSE-POSITIVE: Se score medio >= 9.5 na rodada 1-2:
     verificar evidencia. Exigir que cada agente cite issue real.
     Se nenhum cita issue → marcar round como SUSPEITA, repetir com prompt mais rigoroso
   - ANTI-OSCILLATION: Se score oscila (delta alternando +/- por 2+ rounds):
     congelar fixes, pedir input usuario sobre direcao

5. APPLY: Executar correcoes de consenso (SEM COMMIT)
   - Editar arquivos com as correcoes
   - Criar skills aprovadas
   - NAO commitar ainda

6. VERIFY: Monitor agent verifica:
   - [ ] Todas as correcoes foram aplicadas?
   - [ ] Nenhuma regressao introduzida?
   - [ ] Token budget ainda dentro do limite?
   - [ ] Contexto nao esta proximo de truncar?

7. COMMIT (somente se verificacao passa):
   - git add -A && git commit -m "fix: round [R] consensus corrections"
   - git tag "recovery_R[R]_score[X.X]"
   - Se verificacao FALHA: desfazer correcoes problematicas e re-tentar

8. SMOKE TEST:
   - Verificar que modulo e parseavel (todas secoes carregam)
   - Verificar token count < budget definido
   - Se falha: score -1.0, rollback, re-tentar fixes individualmente

9. GATE: Decidir proximo passo
   - Score medio >= APPROVAL_THRESHOLD E zero bloqueios → APROVAR
   - Score medio < APPROVAL_THRESHOLD → PROXIMA RODADA
   - Rodada = MAX_ROUNDS → FORCAR ENTREGA com nota de issues pendentes
```

### Formato de Report por Rodada

```markdown
═══ RODADA [R] DE [MAX] ═══
SCORE MEDIO: [X.X]/10
AGENTES RESPONDERAM: [N]/[TOTAL]

CONSENSO (aplicar):
| # | Issue | Agentes | Fix |
|---|-------|---------|-----|

CONSIDERAR (debater):
| # | Issue | Agentes | Decisao |
|---|-------|---------|---------|

SKILLS VOTADAS:
| Skill | Votos | Resultado |
|-------|-------|-----------|

BLOQUEIOS: [lista ou NENHUM]
DECISAO: [PROXIMA RODADA / APROVADO / ENTREGA FORCADA]
═══════════════════════════════
```

---

## 7. FASE 6 — CONSENSO FINAL

### Criterios de Aprovacao

```
APROVADO quando TODOS verdadeiros:
- [ ] Score medio >= 8.0/10
- [ ] Zero issues bloqueantes
- [ ] Minimo MIN_ROUNDS completadas
- [ ] Ultima rodada: todos agentes STATUS = APROVADO

SE nao atingir em MAX_ROUNDS:
- Entregar com nota: "Versao [X] — issues pendentes: [lista]"
- Marcar issues como TODO para proxima sessao
```

### Validacao Final (Round de Sign-Off)

```
Rodada especial (apos aprovacao):
- Cada agente: CONFIRMA APROVACAO (YES/NO)
- Se unanime → APROVADO PARA PRODUCAO
- Se split → resolver issues pendentes + 1 rodada extra
- Recomendar versao final
```

---

## 8. FASE 7 — DOCUMENTACAO E ENTREGA

### Output Obrigatorio

```
1. MODULO FINAL: arquivo .md commitado e testado
2. SKILLS FINAIS: arquivos .md na pasta /skills/[dominio]/
3. CHANGELOG: resumo de mudancas por rodada
4. METRICAS:
   - Rodadas executadas: [N]
   - Score inicial → final: [X] → [Y]
   - Skills criadas: [N]
   - Skills propostas e rejeitadas: [N]
   - Issues resolvidas: [N]
5. UPLOAD: Enviar para Google Drive do usuario
```

### Changelog por Rodada

```markdown
## CHANGELOG — [Nome do Modulo]

### Rodada 1 (Score: X.X)
- Reescrita de [secao] por [motivo]
- Adicionada skill [nome]

### Rodada 2 (Score: X.X)
- Corrigido [issue] conforme consenso de [N] agentes
- Aprovada skill [nome] (votos: X/10)

[... continua ate rodada final ...]

### Rodada Final (Score: X.X) — APROVADO
- Aprovacao unanime (10/10)
- Versao final: v[X.Y.Z]
```

---

## 9. AGENTE MONITOR (Anti-Truncamento)

### Responsabilidades

```
O Monitor Agent roda em PARALELO durante todo o processo:

1. VERIFICAR CONTEXTO:
   - Se contexto > 80% do limite → ALERTAR
   - Se contexto > 90% → COMPRIMIR debates anteriores
   - Se contexto > 95% → COMMITAR TUDO + resumir estado + continuar em nova thread

2. VERIFICAR TIMEOUTS:
   - Cada terminal: max 10 min
   - Se agente nao responde em 10 min → registrar TIMEOUT
   - Se 3+ agentes timeout na mesma rodada → verificar se sistema travou
   - Se terminal ativo (processando) → estender ate 15 min
   - Se terminal inativo (sem output) → cancelar aos 10 min

3. VERIFICAR INTEGRIDADE:
   - Apos cada rodada: verificar que arquivos nao foram corrompidos
   - Verificar que token count do modulo nao excedeu budget
   - Verificar que nenhuma skill duplicada foi criada

4. RECOVERY (via Git, NAO /tmp):
   - Se truncamento detectado → commitar estado imediatamente
   - git tag "recovery_R[N]_score[X.X]" + commit message com estado:
     "CHECKPOINT: Round [N] | Score: [X.X] | Pending: [issues]"
   - Se nova sessao: git log --tags → encontrar ultimo recovery tag → retomar
   - Usar skill token-compression-strategies.md para formato de estado comprimido

5. COMPRESSAO (carregar token-compression-strategies.md):
   - Apos cada round: comprimir round R-2 para formato resumido (1 linha)
   - Apos debate gate: comprimir para "DECISAO + motivo" (80 tokens)
   - Se YELLOW (80%): comprimir tudo exceto ultimos 2 rounds
   - Se RED (95%): commitar + resumo 500 tokens + nova thread
```

### Formato de Alerta

```
⚠️ MONITOR: [tipo] — [descricao]
Acao: [o que fazer]
Estado: [salvo/nao salvo]
```

---

## 10. SKILL SCOUT — PROTOCOLO

### Responsabilidades

```
O Skill Scout e o agente N+1 que roda em PARALELO aos reviewers:

1. LER todos os skills existentes do modulo
2. IDENTIFICAR gaps (o que esta faltando que causaria falha)
3. PROPOR novas skills (max 5 por rodada)
4. Para cada proposta:
   - Nome (filename.md)
   - Proposito (1 frase)
   - Gap que preenche
   - Token cost estimado (~1.5K)
   - Prioridade (CRITICA / ALTA / MEDIA / BAIXA)
   - Argumento FOR e AGAINST

5. VOTACAO:
   - Apresentar propostas aos 10 reviewers
   - Cada reviewer vota SIM/NAO
   - Threshold: 7/10 para aprovar
   - Excecao: se 1 agente tem argumento MUITO forte contra → veto (debate extra)

6. SKILLS REJEITADAS:
   - Podem ser re-propostas em rodada futura com argumento mais forte
   - Se rejeitada 2x → nao re-propor (decisao final)
```

---

## 11. DEBATE PROTOCOL

### Formato (visivel no chat)

```
═══ DEBATE GATE: [Fase/Rodada] ═══
DECIDINDO: [pergunta central]
A FAVOR: [2 argumentos]
CONTRA: [2 argumentos/riscos]
RISCO 1: [desc] → Mitigacao: [acao]
RISCO 2: [desc] → Mitigacao: [acao]
ALTERNATIVA: [opcao descartada + motivo]
DECISAO: [escolha] | CONFIANCA: [ALTA/MEDIA/BAIXA]
═══ GATE APROVADO ═══
```

### Quando Debater

```
OBRIGATORIO:
- Antes de escolher arquitetura (Fase 3)
- Quando ha divergencia entre agentes (2+ posicoes)
- Quando issue e classificada como BLOQUEANTE
- Quando skill e aprovada por margem minima (7/10 exato)

OPCIONAL:
- Entre rodadas para decisoes de direcao
- Quando score estagna (mesma nota 2 rodadas seguidas)
```

---

## 12. ERROR RECOVERY

```
SE rodada falha (menos de 8 agentes respondem):
├── Verificar timeouts → estender para 15 min e re-tentar
├── Se mesmo assim < 8 → rodar rodada com os que responderam (marcar como "parcial")
└── Se 0 respostas → problema de sistema, salvar estado, avisar usuario

SE score NAO melhora por 3 rodadas seguidas:
├── Mudar estrategia: trocar 2-3 agentes por perspectivas diferentes
├── Ou: pedir input do usuario sobre direcao
└── Se continuar estagnado → entregar com nota "plateau atingido em [score]"

SE contexto trunca:
├── Monitor agent ja commita + git tag "recovery_R[N]" automaticamente
├── Na nova sessao:
│   1. git log --tags --grep="recovery" → encontrar ultimo tag
│   2. Ler commit message do tag para contexto (score, pendencias)
│   3. Carregar modulo + skills do estado commitado
│   4. Retomar rodada N+1
├── NAO re-executar rodadas ja finalizadas
└── DECLARAR ao usuario: "Retomando de rodada [N+1]. Score anterior: [X.X]"

SE conflito entre agentes (split 5/5):
├── Executar debate gate dedicado
├── Se debate nao resolver → pedir input do usuario
└── Se usuario nao disponivel → escolher opcao mais conservadora
```

---

## 13. EXEMPLO DE USO — CASO REAL

### Input do usuario:
> "Crie um modulo de criacao de sites full-stack com debate obrigatorio e 5 rodadas de review"

### Execucao resumida:

```
FASE 1 (Briefing):
- Tipo: Novo modulo
- Dominio: Site creation (frontend + backend + deploy)
- Restricoes: debate obrigatorio, min 5 rodadas, full-stack

FASE 2 (Brainstorming):
- 8 agentes propuseram abordagens
- Consenso: workflow faseado + skills on-demand + design contract
- Divergencia: quantas skills? (resolvido: comecar com 5, skill scout adiciona)

FASE 3 (Arquitetura):
- Hibrido: "Lean Domain Guide + Fallbacks"
- 7 fases de workflow
- 6 debate gates
- Skill files on-demand

FASE 4 (Prototipagem):
- Modulo v1.0: ~5K tokens
- 5 skills iniciais: frontend, palette, testing, deploy, recovery

FASE 5 (Review Iterativo):
- Rodada 1: 6.5/10 → reescrita major (v1.0 → v1.1)
- Rodada 2: 7.5/10 → 8 correcoes de consenso + 2 skills aprovadas
- Rodada 3: 8.3/10 → 1 bloqueio (seguranca) + 1 skill aprovada
- Rodada 4: 9.1/10 → bloqueio resolvido, APROVADO
- Rodada 5: Unanime → sign-off final

FASE 6 (Consenso): 10/10 aprovaram
FASE 7 (Entrega): Upload Google Drive, 42 arquivos

METRICAS FINAIS:
- Rodadas: 5
- Score: 6.5 → 9.1 (+2.6)
- Skills: 5 iniciais + 6 adicionadas = 11 total
- Skills rejeitadas: 3
- Issues resolvidas: 23
```

---

## 14. CONFLITO DE REGRAS

Prioridade (maior para menor):
1. Seguranca (nunca expor credenciais)
2. Pedido explicito do usuario (num rounds, num agentes)
3. Invariantes do sistema (core.md, ARCHITECTURE.md)
4. Consenso dos agentes (maioria)
5. Conhecimento interno do modelo

---

## 15. SAFEGUARDS (Robustez)

### Self-Review Protocol

```
SE este modulo precisa ser melhorado:
- NAO usar este modulo para revisar a si mesmo (paradoxo recursivo)
- Usar agente EXTERNO como auditor primario
- Validar mudancas contra versao anterior (diff)
- Manter backup da versao funcional antes de editar
- Regra: mudancas neste modulo requerem 80%+ consenso (mais rigoroso que padrao)
```

### Caps e Limites

```
LIMITES ABSOLUTOS (nao configuraveis):
- Max skills totais por modulo: 15 (evitar token explosion)
- Max skills propostas por round pelo Scout: 3 (nao 5)
- Max rounds consecutivos sem melhoria: 3 → parar
- Max token peak: 25K (alem disso → comprimir antes de continuar)
- Max agentes simultaneos: 15 (hard cap do core.md)
- Se score >= 9.5 em round < 3: exigir evidencia, nao aprovar automaticamente
```

### Git Fallback

```
SE Git indisponivel no ambiente:
1. Usar /tmp/checkpoints/round_[N].json como backup de estado
2. Formato: { "round": N, "score": X.X, "pending": [...], "timestamp": "ISO" }
3. Avisar usuario: "Recovery limitado sem Git. Recomendo ambiente com Git."
4. Se ambiente efemero: salvar estado via api-gateway para storage externo
5. NAO bloquear processo — apenas degradar recovery capabilities
```

### Context RED Recovery (Early Round)

```
SE contexto atinge 95% ANTES de MIN_ROUNDS:
1. Commitar/salvar estado IMEDIATAMENTE
2. Comprimir TUDO para estado minimo (~500 tokens):
   "ESTADO: Round [N], Score [X.X], Fixes pendentes: [lista], Skills: [lista]"
3. DECLARAR ao usuario como retomar
4. Na nova thread: carregar estado + modulo fresco (sem historico)
5. Configuracao preservada: NUM_AGENTS, ROLES, scores anteriores
6. NAO repetir rounds anteriores — confiar nos scores salvos
```

---

*Modulo Aprimoramento v1.0.0 — Ultra Prompt v6.2*
*7 Fases | Debate Gates | Review Iterativo | Monitor + Skill Scout*
