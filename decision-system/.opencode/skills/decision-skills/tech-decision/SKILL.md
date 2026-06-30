---
name: tech-decision
description: "DECISAO TECNICA RAPIDA — Para @tech-lead. Escolha stack/ferramenta em segundos."
model: openrouter/deepseek-v4-flash
user-invocable: true
allowed-tools: Read, Bash, Grep
---

# Tech Decision — Fast

## Regra de Ouro
Toda decisao tecnica responde a 3 perguntas:
- Funciona?
- Equipe domina?
- Custo/beneficio faz sentido?

## Quando Usar
"Qual framework/lib/banco usar?"
"Como fazer X?"
"Devo usar Y ou Z?"

## Framework (5 Perguntas, 30 segundos)

### Q1 — Resolve o problema?
- SIM se: atende requisitos funcionais E nao-funcionais
- NAO se: falta feature essencial OU performance ruim

### Q2 — Equipe domina ou aprende rapido?
- SIM se: ja usou OU tem na equipe OU docs boas
- NAO se: requer especializacao rara OU curva de aprendizado > 1 semana

### Q3 — Custo/beneficio?
- Licenca: gratis, freemium, pago
- Manutencao: ativo/descontinuado
- Tamanho do bundle: leve/pesado
- Lock-in vendor: baixo/medio/alto

### Q4 — Reversivel?
- SIM (substituivel em 1-2 sprints)
- NAO (dependencia profunda)

### Q5 — Documentacao/Comunidade?
- Forte: docs boas + comunidade ativa
- Fraco: pouca info OU abandonware

## Matriz de Decisao

| Q1 | Q2 | Q3 | Q4 | Decisao |
|----|----|----|----|---------|
| ✅ | ✅ | ✅ | - | VAI |
| ✅ | ✅ | ❌ | SIM | Aceitar custo |
| ✅ | ❌ | ✅ | - | Treinamento primeiro |
| ❌ | - | - | - | FORA |

## Output Esperado

```
PROBLEMA: [1 frase]

OPCOES:
- A: [lib/framework]
  Q1:✅ Q2:✅ Q3:✅ Q4:SIM Q5:✅
  Nota: 9/10
  
- B: [alternativa]
  Q1:✅ Q2:❌ Q3:✅ Q4:SIM Q5:✅
  Nota: 7/10 (requer 3 dias de ramp-up)

DECISAO: A

JUSTIFICATIVA: [1 frase tecnica]
```

## Quando Pedir Mais Analise
- Decisao arquitetural de longo prazo
- Multiplos sistemas interconectados
- Trade-off de performance critico
- Nesses casos: delegue para ultra-powerful/complex-architecture-decision
