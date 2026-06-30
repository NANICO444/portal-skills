---
name: think-max-protocol
description: "Protocolo de Pensamento Máximo — análise ultra-profunda de problemas complexos com 5 camadas de investigação"
argument-hint: "[problema complexo para analisar]"
user-invocable: true
allowed-tools: Read, Glob, Grep, Bash, Task, WebFetch
agent: orquestrador
---

# Think Max Protocol

Protocolo de pensamento máximo para problemas de altíssima complexidade.

## Quando Ativar

- Bug intermitente sem causa aparente
- Problema de performance em produção
- Decisão arquitetural com trade-offs complexos
- Sistema legado sem documentação
- Problema que já consumiu horas sem solução

## O Protocolo (5 Camadas)

### Camada 1 — Superfície
O que PARECE ser o problema?
- Sintomas observáveis
- Mensagens de erro
- Comportamento atual vs. esperado
- Momento em que ocorre (após quanto tempo, após qual ação)

### Camada 2 — Causa Imediata
O que CAUSA o sintoma diretamente?
- Stack trace completo
- Estado das variáveis no momento do erro
- Condições que reproduzem o problema
- Logs no momento da falha

### Camada 3 — Causa Raiz
O que PERMITE que a causa imediata exista?
- Suposições incorretas no código
- Edge cases não tratados
- Condições de corrida / concorrência
- Dependências com comportamento inesperado
- Configuração incorreta

### Camada 4 — Sistema
Que PROPRIEDADES DO SISTEMA tornam essa causa possível?
- Acoplamento entre módulos
- Falta de invariantes ou contratos
- Modelo de dados inconsistente
- Arquitetura que não prevê este cenário
- Ausência de barreiras de segurança

### Camada 5 — Metodologia
O que no PROCESSO permitiu que isso chegasse em produção?
- Testes insuficientes para este cenário
- Code review que não capturou
- Falta de validação de requisitos
- Documentação ausente ou desatualizada

## Modos de Operação

### Modo Forense (bug já ocorreu)
1. Colete todas as evidências (logs, stack traces, estado)
2. Reproduza isoladamente (mínimo necessário para reproduzir)
3. Altere UMA variável por vez
4. Documente cada tentativa (hipótese → experimento → resultado)

### Modo Preventivo (antes de implementar)
1. Liste todos os modos de falha conhecidos
2. Para cada modo: probabilidade × impacto
3. Implemente barreiras para os 3 mais críticos
4. Teste cada barreira

### Modo Performance (sistema lento)
1. Meça antes de otimizar (métrica objetiva)
2. Identifique o gargalo (amostragem, não suposição)
3. Altere UMA coisa por vez
4. Meça depois de cada alteração

## Regras de Ouro

✅ Evidência > intuição: se não mediu, não sabe.
✅ Uma variável por vez: alterar múltiplas coisas invalida o diagnóstico.
✅ Reproduza antes de corrigir: se não reproduziu, não vai saber se a correção funciona.
✅ Documente cada tentativa: hipótese, experimento, resultado.

❌ "Vou tentar X para ver se resolve" sem hipótese.
❌ Ignorar o óbvio (verifique permissões, URL, porta, fuso horário).
❌ Aplicar correção sem entender causa raiz.
