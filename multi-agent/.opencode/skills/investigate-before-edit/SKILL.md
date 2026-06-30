---
name: investigate-before-edit
description: "INVESTIGAR ANTES DE EDITAR - sempre investigue o codigo/problema antes de modificar. Faca o minimo necessario."
user-invocable: true
allowed-tools: Read, Grep, Glob, Bash
---

# Investigar Antes de Editar

## Principio Fundamental

> **Nao edite o que voce nao entende. Invista tempo ANTES de tocar no codigo.**

## Quando Usar

- Bug que voce nao sabe a causa
- Codigo legado sem documentacao
- Mudanca em sistema que voce nao conhece
- Antes de qualquer refatoracao

## Framework (5 Etapas)

### Etapa 1 - Entender o Contexto (15-30 min)
- O que esse codigo FAZ (nao como, mas o que)
- Quem usa (outros modulos, usuarios, etc)
- Quando foi escrito / por quem
- Documentacao existente? (leia)
- Tests existentes? (leia)

### Etapa 2 - Mapear as Dependencias
- Quem chama essa funcao/classe?
- O que essa funcao/classe chama?
- Variaveis de estado compartilhado?
- Recursos externos (banco, API, arquivo)?

### Etapa 3 - Reproduzir (se for bug)
- Como reproduzir o problema?
- O que tem que estar no estado X para dar bug?
- Stack trace completo
- Logs no momento do erro

### Etapa 4 - Formar Hipotese
- Minha melhor explicacao do que esta acontecendo
- Evidencia que SUPORTA essa explicacao
- Evidencia que CONTRA essa explicacao
- Se nao tem hipotese: investigue mais, nao edite

### Etapa 5 - Edicao MINIMA
- Menor mudanca que resolve
- NAO "melhore" codigo vizinho
- NAO adicione features especulativas
- NAO refatore por refatorar

## Anti-Padroes

❌ "Vou alterar e ver se resolve" → Edita, nao investiga
❌ "Esse codigo esta feio, vou refatorar" → Foco, nao escopo
❌ "Vou adicionar feature que vai precisar" → YAGNI
❌ "Nao tenho tempo de investigar" → Investigue, depois edite

## Tempo de Investigacao

| Complexidade | Tempo sugerido |
|--------------|----------------|
| Simples (1 arquivo, logica clara) | 5-15 min |
| Medio (multiplos arquivos, logica) | 30-60 min |
| Complexo (sistema legado) | 2-4 horas |
| Muito complexo (subsistema) | 1+ dia |

## Output

```
INVESTIGACAO COMPLETA:

CONTEXTO: [o que esse codigo faz]
DEPENDENCIAS: [quem chama, quem eh chamado]
ESTADO COMPARTILHADO: [variaveis globais, banco, etc]

REPRODUCAO: [como reproduzir]
- Pre-requisito: [estado X]
- Acao: [passo 1, 2, 3]
- Resultado: [o que acontece]

HIPOTESE PRINCIPAL: [minha explicacao]
- Evidencia a favor: ...
- Evidencia contra: ...
- Confianca: [0-100%]

MUDANCA PROPOSTA: [menor mudanca]
ARQUIVO: [arquivo:linha]
RISCO: [baixo / medio / alto]
REVERSAVEL: [sim / parcial / nao]
```
