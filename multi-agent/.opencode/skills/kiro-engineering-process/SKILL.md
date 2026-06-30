---
name: kiro-engineering-process
description: "Processo de Engenharia Hefesto — 6 passos: inspecionar, delimitar, planejar, implementar, testar/revisar, entregar"
argument-hint: "[descrição da tarefa de engenharia]"
user-invocable: true
allowed-tools: Read, Glob, Grep, Bash, Edit, Write, Task
agent: orquestrador
---

# Processo de Engenharia (Hefesto)

Metodologia dos 6 passos para tarefas de engenharia de software.

## Fluxo Obrigatório

### Passo 1 — Inspecione
- Stack: linguagem, framework, runtime, banco, sistema operacional
- Comandos: build, test, lint, typecheck
- Estrutura: diretórios, módulos, pontos de entrada
- Testes: existentes, padrão, cobertura
- Estado Git: branch, modificações não commitadas

### Passo 2 — Delimite
- Comportamento esperado da mudança (o que DEVE acontecer)
- Arquivos permitidos (lista explícita)
- Riscos identificados (dados, segurança, compatibilidade)
- Critério de sucesso verificável (teste, build, comando)

### Passo 3 — Planeje
Para mudanças multi-módulo ou complexas:
- Use `skill:writing-plans` para estruturar o plano
- Identifique dependências entre sub-tarefas
- Estime riscos e pontos de verificação

### Passo 4 — Implemente
- Menor mudança coerente que atende o objetivo
- Siga estilo existente do projeto (formatação, padrões)
- NÃO refatore código vizinho não relacionado
- NÃO adicione abstração especulativa ("vai precisar um dia")
- Preserve a arquitetura existente

### Passo 5 — Teste & Revise
- Rode testes existentes (não alegue sucesso sem executar)
- Rode linter, typecheck, build
- Revise diff completo (mudanças acidentais?)
- Segurança: se tocar auth, dados, API, config — revise explicitamente
- Verifique compatibilidade reversa

### Passo 6 — Entregue
- Liste todos os arquivos alterados
- Liste evidências de verificação (testes passaram, build OK)
- Liste riscos residuais conhecidos
- Documente decisões técnicas relevantes

## Regras de Ouro

✅ Testes proporcionais ao risco: sem testes no projeto? Adicione o mínimo viável.
✅ Mudanças de API/contrato: registre compatibilidade e documentação.
✅ Migrações de dados: EXIGEM plano de rollback + confirmação antes de executar.
✅ Critique com evidência: mostre o erro, linha, stack trace — não opine.

❌ Refatoração adjacente ("já que estou aqui...").
❌ Dependências novas sem necessidade justificada.
❌ Arquitetura antecipada para cenários improváveis.
