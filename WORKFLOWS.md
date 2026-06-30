# Workflows Praticos

> **Como usar o sistema em tarefas reais. Do trivial ao critico.**

## Workflow 1: Pergunta de decisao rapida

**Cenario:** "Devo comprar ferramenta X por R$ 200/mes?"

```
1. Usuario: "Devo comprar X?"
2. OpenCode: detecta regra always-use-agents
3. Delega para @financial-advisor (decision-system)
4. Carrega skill: financial-decision
5. Aplica framework 3 perguntas (custo, retorno, ROI)
6. Responde: SIM/NAO/QUAL VALOR com justificativa numerica
```

**Tempo:** 30-60 segundos
**Quando usar:** Decisoes do dia-a-dia, com criterio financeiro

---

## Workflow 2: Implementar feature de codigo

**Cenario:** "Adicionar busca na listagem de produtos"

```
1. Usuario: "Adicionar busca na listagem"
2. OpenCode: detecta regra always-supervise (codigo)
3. Delega para @orquestrador (multi-agent)
4. Orquestrador consulta sub-agentes:
   - @code-reviewer: analisa abordagem
   - @testador: define casos de teste
   - @security-auditor: valida input
5. Implementa
6. Invoca @supervisor (max-thinking) para revisao final
7. Supervisor chama 7 specialists em paralelo:
   - @code-reviewer-x → review
   - @security-auditor → OWASP
   - @performance-auditor → Big O
   - @test-coverage-auditor → gaps
   - @docs-auditor → documentacao
   - @dependency-auditor → deps
   - @standards-enforcer → padroes
8. Supervisor sintetiza: APROVADO / RESSALVAS / REJEITADO
9. Se REJEITADO: lista O QUE APAGAR, ADICIONAR, FAZER, BAIXAR
```

**Tempo:** 5-15 minutos
**Quando usar:** Features de codigo, qualquer mudanca significativa

---

## Workflow 3: Decisao arquitetural critica

**Cenario:** "Devo mudar para microservicos?"

```
1. Usuario: "Devo mudar para microservicos?"
2. OpenCode: detecta tarefa complexa
3. Delega para @arquiteto (multi-agent agent2)
4. Arquiteto carrega skill: complex-architecture-decision
5. Aplica 7 camadas (contexto, opcoes, trade-offs, stress test, etc)
6. Output: recomendacao com pre-commitment metrics
7. Salva em ADR (skill: adr-architecture-decision)
```

**Tempo:** 10-30 minutos
**Quando usar:** Decisoes que custam caro para reverter

---

## Workflow 4: Bug em producao

**Cenario:** "Usuarios reclamando que login falha"

```
1. Usuario: "Login esta falhando"
2. OpenCode: detecta tarefa de bug
3. Delega para @debugger (multi-agent)
4. Carrega skill: systematic-debugging
5. Aplica 5 camadas (superficie → meta)
6. Reproduz, isola causa raiz
7. Corrige
8. Invoca @supervisor para validar fix
9. Se OK: aprova e deploy
```

**Tempo:** 15-60 minutos
**Quando usar:** Bug que precisa ser resolvido rapido e com qualidade

---

## Workflow 5: Pesquisa de tecnologia

**Cenario:** "Qual biblioteca de graficos usar?"

```
1. Usuario: "Qual lib de graficos?"
2. OpenCode: detecta tarefa de pesquisa
3. Delega para @pesquisador (multi-agent agent2)
4. Carrega skill: factual-verify + library-curator
5. Pesquisa, compara, recomenda UMA com exemplo
6. Output: tabela + comando install
```

**Tempo:** 2-5 minutos
**Quando usar:** Decisao tecnologica com trade-offs

---

## Workflow 6: Fechar PR com qualidade

**Cenario:** "Quero fazer merge do PR #123"

```
1. Pre-merge:
   - @testador roda suite completa
   - @code-reviewer faz review final
   - @security-auditor valida
2. Cria PR (skill: github-pr-workflow)
3. Espera CI passar (skill: github-actions-templates)
4. Code review automatico (skill: github-code-review)
5. @supervisor aprova/rejeita
6. Merge (skill: finishing-a-development-branch)
```

**Tempo:** varia
**Quando usar:** Antes de cada merge

---

## Workflow 7: Criar novo agente

**Cenario:** "Preciso de um agente que cuide de licitacoes"

```
1. Verifica se ja existe (skill: find-skills, INDEX.md)
2. Se nao:
   a. Cria opencode.json com novo agent
   b. Cria .md do agent com description, prompt, model
   c. Cria SKILL.md se necessario
   d. Adiciona regra always-* se for parte de um workflow
3. Documenta no README do sistema
4. Testa invocando o agent
```

**Quando usar:** Quando uma especialidade nao esta coberta pelos 35 agents existentes

---

## Como escolher o workflow certo

| Se a tarefa e... | Use o workflow... |
|------------------|-------------------|
| Decisao binaria rapida | 1 (decisao rapida) |
| Implementar feature | 2 (implementar) |
| Decisao grande | 3 (arquitetura) |
| Bug em producao | 4 (debug) |
| Escolher tecnologia | 5 (pesquisa) |
| Fechar PR | 6 (merge) |
| Falta cobertura | 7 (criar agente) |

## Quando chamar diretamente o @supervisor

Use `@supervisor` quando:
- Quer aprovacao ANTES de commitar
- Quer revisao profunda de codigo
- Quer saber o que apagar/adicionar/fazer/baixar
- Quer combinar 7 sub-agentes em paralelo

O supervisor NAO substitui o @orquestrador (multi-agent) — eles sao complementares:
- @orquestrador: implementa
- @supervisor: revisa o implementado
