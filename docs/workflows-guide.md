# Guia de Workflows

> **7 workflows praticos para tarefas reais.**

## Workflow 1: Decisao Rapida

**Quando:** Pergunta de sim/nao, com prazo curto.

**Tempo:** 30-60 segundos

**Passos:**
1. OpenCode detecta always-delegate
2. Carrega decision-system
3. Identifica o decisor (financial, risk, etc)
4. Aplica framework 3 perguntas
5. Responde com SIM/NAO/VALOR

**Exemplo:**
```
Usuario: "Devo contratar servico X por R$ 500/mes?"

OpenCode → @financial-advisor → financial-decision

CUSTO_TOTAL_12M: R$ 6000
RETORNO_12M: R$ 30000 (em vendas adicionais)
ROI: 400%
PAYBACK: 2.4 meses

DECISAO: SIM
```

---

## Workflow 2: Implementar Feature

**Quando:** Pedido de implementacao.

**Tempo:** 5-15 minutos (mais se complexo)

**Passos:**
1. OpenCode carrega @orquestrador (multi-agent)
2. Orquestrador planeja (investigate-before-edit)
3. Sub-agentes contribuem:
   - @code-reviewer — analise
   - @testador — testes (TDD)
   - @security-auditor — validacao input
4. Implementacao
5. @supervisor revisa (max-thinking)
6. Output final: APROVADO + detalhes

---

## Workflow 3: Decisao Arquitetural

**Quando:** Decisao grande, dificil de reverter.

**Tempo:** 10-30 minutos

**Passos:**
1. OpenCode carrega @arquiteto (multi-agent agent2)
2. Carrega skill complex-architecture-decision (Opus 4.8 se disponivel)
3. Aplica 7 camadas:
   - Contexto
   - Opcoes (min 3)
   - Trade-off matrix
   - Stress test
   - Second-order effects
   - Decisao
   - Documentacao (ADR)
4. Output: recomendacao + pre-commitment metrics
5. Salva ADR

---

## Workflow 4: Bug em Producao

**Quando:** Algo quebrou, precisa resolver rapido.

**Tempo:** 15-60 minutos

**Passos:**
1. OpenCode carrega @debugger (multi-agent)
2. Carrega systematic-debugging
3. 5 camadas:
   - Reproduz
   - Isola causa raiz
   - Formula hipotese
   - Aplica correcao
   - Cria teste de regressao
4. Verifica que nao quebrou outras coisas
5. @supervisor valida

---

## Workflow 5: Pesquisa de Tecnologia

**Quando:** "Qual lib/framework usar?"

**Tempo:** 2-5 minutos

**Passos:**
1. OpenCode carrega @pesquisador (multi-agent agent2)
2. Carrega library-curator
3. Pesquisa, compara 3-5 opcoes
4. Avalia 7 criterios:
   - Funcionalidade
   - Manutencao
   - Comunidade
   - Documentacao
   - Performance
   - Licenca
   - Lock-in
5. Recomenda UMA com codigo exemplo
6. Comando de install

---

## Workflow 6: Fechar PR com Qualidade

**Quando:** PR aberto, vai mergear.

**Tempo:** Varia (pode ser automatico)

**Passos:**
1. CI roda (tests, lint, type-check, build)
2. Pre-merge checks:
   - @testador roda suite completa
   - @code-reviewer revisa
   - @security-auditor valida
3. Cria PR (github-pr-workflow)
4. Aguarda code review (github-code-review)
5. @supervisor aprova/rejeita
6. Merge (finishing-a-development-branch)
7. Post-merge: monitor

---

## Workflow 7: Criar Novo Agente

**Quando:** Falta cobertura em alguma area.

**Passos:**
1. Verifica se ja existe (INDEX.md, find-skills)
2. Se nao:
   - Cria opencode.json ou .md do agent
   - Define description, prompt, model
   - Cria SKILL.md se for complex
   - Adiciona regra se for parte de workflow
3. Documenta no README
4. Testa invocando o agent

---

## Como Escolher o Workflow

```
Pergunta do usuario
       │
       ▼
   Classifique
       │
   ┌───┴────────────────────┐
   │                        │
   ▼                        ▼
Codigo/                  Conhecimento/
Tecnico                  Pesquisa
   │                        │
   ▼                        ▼
Complexo?              Decisao?
   │                   ┌────┴────┐
   │                   ▼         ▼
   Nao              Simples   Critica
   │                (30s)     (Opus 4.8)
   ▼                   │         │
   Workflow 2           ▼         ▼
   ou 4            Workflow 1  Workflow 3
```

## Quando Misturar Workflows

- **Decisao + implementacao:** Workflow 1 (decide) + Workflow 2 (implementa)
- **Bug + deploy:** Workflow 4 (fix) + Workflow 6 (PR + merge)
- **Pesquisa + implementacao:** Workflow 5 (escolhe) + Workflow 2 (implementa)

## Metricas de Sucesso

| Workflow | Metrica |
|----------|---------|
| Decisao rapida | Tempo de resposta < 60s |
| Feature | Tests passing + score supervisor > 85 |
| Decisao arquitetural | ADR criado + 3 opcoes consideradas |
| Bug | Tempo de resolucao + teste de regressao |
| Pesquisa | Comando de install + exemplo funcional |
| PR merge | CI passing + review approval |
| Novo agent | Aparece no OpenCode global + funciona |

## Anti-Padroes

- Pular workflow por "ser simples"
- Misturar workflows sem planejar
- Nao medir tempo de resposta
- Nao documentar decisao
- "Fazer rapido" sem seguir framework
