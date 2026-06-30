# SKILL: Orquestração Avançada de Sub-Agentes
# Use esta skill quando precisar dividir uma tarefa grande em sub-tarefas paralelas

---

## Quando Usar Esta Skill
- Tarefa envolve mais de 3 arquivos diferentes
- Tarefa tem etapas independentes que podem rodar em paralelo
- Tarefa é grande demais para resolver numa única rodada
- Tarefa requer expertise de múltiplos domínios (ex: Python + Web + Deploy)

## Protocolo de Orquestração

### Passo 1: Análise e Decomposição
Antes de qualquer código, analise a tarefa e divida em sub-tarefas atômicas:
```
Tarefa: "Criar landing page com chat IA integrado"
├── Sub-tarefa A: Criar HTML/CSS do layout (cyberpunk-web-designer)
├── Sub-tarefa B: Implementar lógica JS do chat (gameplay-programmer)
├── Sub-tarefa C: Configurar API OpenRouter (openrouter-api-specialist)
└── Sub-tarefa D: Fazer deploy (deployment-specialist)
```

### Passo 2: Invocação Paralela
Use `invoke_subagent` para disparar sub-agentes em paralelo:
```
invoke_subagent([
    {TypeName: "self", Role: "HTML/CSS Designer", Prompt: "Crie o layout..."},
    {TypeName: "self", Role: "JS Developer", Prompt: "Implemente o chat..."},
    {TypeName: "research", Role: "API Researcher", Prompt: "Pesquise os modelos..."},
])
```

### Passo 3: Consolidação
Após receber resultados de todos os sub-agentes:
1. Revise cada resultado individualmente
2. Resolva conflitos entre arquivos
3. Integre tudo num resultado coeso
4. Teste o resultado final
5. Apresente ao Chefe

## Regras de Orquestração
1. **Máximo 4 sub-agentes** rodando ao mesmo tempo
2. **Cada sub-agente** deve ter um prompt CLARO e ESPECÍFICO
3. **Nunca** deixe dois sub-agentes editando o mesmo arquivo
4. **Sempre** faça uma revisão final após consolidar
5. **Reporte** o status ao Chefe após cada fase

## Padrão de Prompt para Sub-Agentes
```
Você é o [ROLE]. Sua tarefa específica é:
[DESCRIÇÃO CLARA DA SUB-TAREFA]

Arquivos que você pode editar:
[LISTA DE ARQUIVOS]

Arquivos que você NÃO pode editar (outro agente cuida):
[LISTA DE ARQUIVOS BLOQUEADOS]

Critério de sucesso:
[COMO SABER QUE TERMINOU]
```
