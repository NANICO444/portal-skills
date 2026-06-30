---
name: rollback-strategy
description: "ESTRATEGIA DE ROLLBACK - sempre tenha um plano de reverter. Para deploys, migracoes, mudancas grandes."
user-invocable: true
allowed-tools: Read, Bash
---

# Estrategia de Rollback

## Principio

> **Toda mudanca importante precisa de um "undo". Sem plano de rollback, nao faca.**

## Quando Usar

- Deploy de producao
- Migracao de banco
- Mudanca de schema
- Feature flag que liga/desliga
- Configuracao de infraestrutura
- Atualizacao de dependencia critica

## Tipos de Rollback

### Rollback de Codigo
- Git revert (cria novo commit que desfaz)
- Git reset (apaga commits, perigoso em main)
- Re-deploy de versao anterior
- Tempo: segundos a minutos

### Rollback de Banco
- Migration down script
- Restore de backup
- Forward-fix (corrige sem voltar)
- Tempo: minutos a horas

### Rollback de Infraestrutura
- Terraform destroy
- Revert de config
- Re-deploy de versao anterior
- Tempo: minutos

### Rollback de Dependencia
- Pin para versao anterior
- npm install pacote@versao_anterior
- Tempo: segundos

## Framework

### Antes da Mudanca (Obrigatorio)

1. **Identifique o que pode dar errado**
2. **Crie o script de rollback ANTES de aplicar**
3. **Teste o rollback em ambiente de staging**
4. **Documente tempo esperado de rollback**
5. **Defina criterios de "rollback automatico"**
6. **Tenha equipe disponivel para rollback**

### Durante a Mudanca

1. **Monitore metricas criticas**
2. **Esteja pronto para rollback em < 5 min**
3. **Comunique o status em canal visivel**
4. **Documente o que esta acontecendo**

### Apos a Mudanca

1. **Mantenha rollback disponivel por 24-48h**
2. **Monitore por anomalias**
3. **Documente o que foi aprendido**

## Criterios para Rollback Automatico

- Error rate > 5%
- Latencia p95 > 2x baseline
- Memoria > 90% por 5 min
- Disco > 90%
- Health check falha por 3+ tentativas

## Anti-Padroes

❌ "Nao precisa de rollback" → Sempre precisa
❌ "Vou pensar nisso depois" → Pense ANTES
❌ "Backup antigo serve" → Restaure periodicamente
❌ "Forward fix eh mais rapido" → As vezes sim, as vezes nao
❌ "Vou reverter no git" → E se nao tem permissao?

## Output Template

```
PLANO DE ROLLBACK

MUDANCA: [o que sera feito]
TIPO: [codigo / banco / infra / dependencia]
RISCO: [baixo / medio / alto / critico]

PRE-CONDICOES:
- [ ] Backup de banco feito em [data]
- [ ] Snapshot de config capturado
- [ ] Versao anterior ainda deployavel
- [ ] Equipe disponivel para rollback

SCRIPT DE ROLLBACK:

```bash
# Adicionar aqui os comandos exatos para reverter
```

TESTADO EM STAGING: [sim / nao]
TEMPO ESTIMADO: [X minutos]
REVERSAO DE DADOS: [sim / nao]
DADOS PERDIDOS: [sim / nao - quais]

CRITERIOS DE ROLLBACK AUTOMATICO:
- [criterio 1]
- [criterio 2]

OWNER DA DECISAO: [pessoa/equipe]
```
