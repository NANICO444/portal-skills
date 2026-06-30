---
name: adr-architecture-decision
description: "Architecture Decision Records — documentar decisões arquiteturais com contexto, alternatives e consequências"
argument-hint: "[decisão arquitetural a documentar]"
user-invocable: true
allowed-tools: Read, Write, Task
agent: orquestrador
---

# ADR — Architecture Decision Records

Formato padronizado para documentar decisões arquiteturais importantes.

## Quando Criar um ADR

- Escolha entre tecnologias (banco, framework, biblioteca, runtime)
- Mudança de arquitetura (monolito → microsserviços, nova camada)
- Decisão de design que afeta múltiplos módulos
- Introdução de nova dependência externa
- Mudança de protocolo, formato de dados, schema
- Decisão que você sabe que vão questionar depois

## Template ADR

```markdown
# ADR-NNN: Título da Decisão

## Status
[Proposto | Aceito | Depreciado | Substituído por ADR-NNN]

## Contexto
Descreva o problema, limitações, restrições, e forças atuando.
Inclua: o que motivou a decisão, histórico relevante, requisitos não-funcionais.

## Decisão
Descreva a decisão tomada. Seja específico:
- O que vai ser feito
- Como vai ser feito
- O que NÃO vai ser feito (tão importante quanto)

## Alternativas Consideradas
Para cada alternativa:
- Descrição resumida
- Prós (2-3)
- Contras (2-3)
- Por que foi rejeitada

## Consequências
- Positivas: o que ganhamos com esta decisão
- Negativas: o que sacrificamos ou o risco que assumimos
- Mitigações: como vamos lidar com os aspectos negativos

## Referências
- Documentos relacionados
- ADRs relacionados
- Links para RFCs, issues, discussões
```

## Modos de Review

### Full Review
Para decisões de alto impacto (mudança de stack, arquitetura, protocolo):
- Mínimo 2 revisores
- Período de comentários: 24h
- Decisão por consenso

### Lean Review
Para decisões de médio impacto (biblioteca nova, endpoint, schema):
- 1 revisor
- Período de comentários: 4h
- Decisão por maioria simples

### Solo Review
Para decisões de baixo impacto (ferramenta interna, script, config):
- Sem revisor obrigatório
- Documentação continua necessária

## Onde Armazenar

- Projeto raiz: `docs/adr/NNN-titulo.md`
- Ou `.omo/notepads/decisoes/`
- Manter `docs/adr/README.md` com índice de todos os ADRs

## Regras de Ouro

✅ Datas em todas as entradas.
✅ Alternativas rejeitadas registradas (tão importante quanto a escolhida).
✅ Linguagem clara e direta (evite jargão desnecessário).
✅ ADRs são IMUTÁVEIS depois de aceitos. Errou? Crie ADR de substituição.

❌ ADR para decisão trivial ("vou usar async/await" não precisa de ADR).
❌ Decisão sem alternativa considerada.
❌ ADR que descreve implementação em vez de decisão.
