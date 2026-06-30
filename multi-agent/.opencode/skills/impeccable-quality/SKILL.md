---
name: impeccable-quality
description: "Framework Impeccable — padrão de qualidade para entrega de código, design, e processos"
argument-hint: "[trabalho a ser entregue com qualidade impecável]"
user-invocable: true
allowed-tools: Read, Bash, Edit
agent: orquestrador
---

# Framework Impeccable — Qualidade Impecável

Padrão de qualidade que combina boas práticas de Claude Code, Cursor, e OpenCode.

## Princípios Fundamentais

### 1. Simplicidade > Complexidade
- Código simples que resolve o problema é melhor que código esperto que "prevê" o futuro
- Não adicione abstração sem pelo menos 2 casos de uso reais
- Não otimize antes de medir

### 2. Mudança Cirúrgica
- Faça só o que foi pedido — nada mais
- Não "melhore" código adjacente sem ser perguntado
- Não refatore enquanto corrige bug
- Se vir algo melhor, ANOTE e siga em frente

### 3. Entrega Verificável
- Nunca diga "pronto" sem ter provado
- Mostre o output, não só o comando
- Liste o que mudou, mesmo as pequenas coisas
- Documente decisões com evidência

### 4. Contexto é Rei
- Leia o projeto ANTES de implementar
- Entenda o estilo existente e siga
- Verifique o que já foi tentado
- Pergunte se o requisito é ambíguo

## Pipeline de Trabalho (7 Etapas)

### Etapa 1 — Compreender
- Qual é o problema REAL (não o aparente)?
- Quem é o usuário final?
- Qual o critério de sucesso?
- Quais as restrições (tempo, tecnologia, escopo)?

### Etapa 2 — Investigar
- Código similar já existe no projeto?
- Padrão estabelecido para esse tipo de feature?
- Dependências já disponíveis?
- Armadilhas conhecidas?

### Etapa 3 — Planejar
- Decompor em sub-tarefas pequenas
- Identificar dependências entre elas
- Listar riscos de cada sub-tarefa
- Definir critério de "pronto" para cada uma

### Etapa 4 — Implementar
- Menor mudança coerente que resolve
- Seguir convenções do projeto
- Testar à medida que implementa (não no final)
- Manter commits pequenos e atômicos

### Etapa 5 — Verificar
- Build passa
- Testes passam (incluindo novos)
- Lint e type check passam
- Funcionalidade testada manualmente
- Edge cases cobertos

### Etapa 6 — Documentar
- Comentários onde o código não é óbvio
- Atualizar README se mudou interface
- Atualizar CHANGELOG
- Criar ADR se decisão importante

### Etapa 7 — Entregar
- Resumo claro do que mudou
- Lista de evidências (testes, builds)
- Riscos residuais conhecidos
- Próximos passos sugeridos

## Anti-Padrões a Evitar

### ❌ "Já que estou aqui..."
Mexer em código que não foi pedido. Anote e siga.

### ❌ "Vai precisar um dia..."
Adicionar abstração para uso futuro hipotético. YAGNI.

### ❌ "Deveria funcionar"
Assumir sem testar. SEMPRE teste.

### ❌ "Otimização prematura"
Otimizar sem medir antes. Meça, identifique gargalo, otimize.

### ❌ "Refatoração escondida"
Refatorar enquanto implementa feature. Faça separado.

### ❌ "Commit gigante"
Mudar 50 arquivos em 1 commit. Commits atômicos.

### ❌ "Sem testes"
"Não tem teste nesse projeto" não é desculpa — adicione o mínimo.

### ❌ "Vou corrigir depois"
Bugs conhecidos marcados como "TODO" e nunca corrigidos.

## Comportamentos Excelentes

### ✅ Comunicação Proativa
- Avise sobre bloqueios cedo
- Reporte trade-offs claramente
- Explique decisões complexas
- Mostre o que NÃO foi feito e por quê

### ✅ Verificação Contínua
- Teste cada sub-tarefa
- Verifique integração com código existente
- Meça impacto da mudança
- Documente desvios do plano original

### ✅ Pensamento Defensivo
- Considere casos de borda
- Pense em "o que pode dar errado"
- Implemente validações em inputs
- Trate erros explicitamente

### ✅ Foco no Usuário
- Quem usa isso?
- Qual problema resolve para eles?
- Como sei se eles estão satisfeitos?
- Como descubro se algo está confuso?

## Critérios de "Impecável"

Para dizer que um trabalho está impecável, todas estas condições devem ser verdade:

1. **Resolve o problema** declarado completamente
2. **Não introduz bugs** — testes existentes passam
3. **Segue o estilo** do projeto existente
4. **Documenta o necessário** — sem excesso
5. **É verificável** — output visível, não opinião
6. **É seguro** — sem credenciais, sem injection
7. **É performante** — não introduz lentidão
8. **É acessível** — funciona para todos os usuários
9. **É mantível** — outro dev entende em 5 minutos
10. **É reversível** — fácil de reverter se der problema

## Regras de Ouro

✅ Faça o mínimo que resolve — adicione só o que foi pedido.
✅ Verifique antes de afirmar — sem output, sem afirmação.
✅ Comunique bloqueios — não gaste 2h batendo na parede.
✅ Documente o invisível — por que fez X, não o que X faz.

❌ "Beleza, ficou massa" — sem evidência, sem qualidade.
❌ "É o melhor que dá pra fazer" — sempre dá pra fazer melhor.
❌ "Pra mim está bom" — "pra mim" não é métrica.
