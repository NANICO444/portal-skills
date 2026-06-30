---
name: property-based-testing
description: >
  Escreve testes baseados em propriedades (invariantes) em vez de só exemplos
  fixos: a ferramenta gera centenas de entradas aleatórias e tenta quebrar a
  propriedade, encolhendo o contra-exemplo mínimo quando falha. Ative ao testar
  lógica com muitos casos de entrada (parsers, serialização, cálculos, estruturas
  de dados), ou quando testes por exemplo não cobrem os edge cases. Hypothesis
  (Python) e fast-check (TypeScript).
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [testes, property-based, hypothesis, fast-check, hefesto, qualidade]
    related_skills: [test-driven-development, verification-before-completion, strict-type-checking]
prerequisites:
  python: "hypothesis (pip)"
  node: "fast-check (npm)"
---

# Property-Based Testing

Teste por exemplo verifica casos que VOCÊ pensou. Teste por propriedade verifica
casos que você NÃO pensou: você declara uma *invariante* (algo que deve ser
sempre verdade) e a ferramenta gera centenas de entradas tentando quebrá-la.
Quando acha um contra-exemplo, ela o **encolhe** até o caso mínimo que falha —
o que torna o bug fácil de entender.

## Quando usar

- Lógica com espaço de entrada grande: parsers, serialização/deserialização,
  cálculos, manipulação de strings, estruturas de dados, conversões.
- Quando testes por exemplo passam mas você desconfia de edge cases.
- Para validar invariantes de domínio (ex: "todo pedido tem total ≥ 0").

Não substitui testes por exemplo — **complementa**. Casos específicos
conhecidos (regressões, bugs já vistos) continuam como testes por exemplo.

## Propriedades comuns (padrões pra procurar)

- **Round-trip**: `decode(encode(x)) == x` (serialização, parsing).
- **Invariante**: uma condição sempre verdadeira no resultado (ordenar nunca
  muda o tamanho da lista; soma de positivos é positiva).
- **Idempotência**: `f(f(x)) == f(x)` (normalização, dedup).
- **Comutatividade/associatividade**: `f(a,b) == f(b,a)`.
- **Oráculo**: compara com uma implementação mais simples/lenta que você confia.
- **Nunca quebra**: pra qualquer entrada válida, não lança exceção inesperada.

## Como fazer — Python (Hypothesis)

```python
from hypothesis import given, strategies as st

# Round-trip: serializar e desserializar devolve o original
@given(st.dictionaries(st.text(), st.integers()))
def test_json_roundtrip(d):
    assert json.loads(json.dumps(d)) == d

# Invariante: ordenar preserva o tamanho e é idempotente
@given(st.lists(st.integers()))
def test_sort_invariants(xs):
    s = sorted(xs)
    assert len(s) == len(xs)
    assert sorted(s) == s
```

Rodar: `pytest -q`. Quando falha, Hypothesis imprime o **contra-exemplo mínimo**
(ex: `xs=[0, -1]`) — use-o pra entender e corrigir, e considere fixá-lo como
teste por exemplo (regressão).

## Como fazer — TypeScript (fast-check)

```typescript
import fc from 'fast-check';

test('encode/decode round-trip', () => {
  fc.assert(fc.property(fc.string(), (s) => {
    expect(decode(encode(s))).toBe(s);
  }));
});
```

## Boas práticas

- **Comece pela invariante, não pelo gerador.** Pergunte "o que deve ser SEMPRE
  verdade aqui?" — essa é a propriedade.
- **Restrinja os geradores ao domínio válido** (ex: idades 0–120) pra não testar
  entradas que o sistema nunca receberia — mas não restrinja demais a ponto de
  esconder edge cases.
- **Fixe o contra-exemplo** que a ferramenta achar como teste por exemplo
  (regressão), pra ele nunca mais voltar.
- A verificação de que os testes realmente passam é responsabilidade de
  `[[verification-before-completion]]` — rode e leia a saída.

## Relação com o sistema

- Complementa `[[test-driven-development]]` (Hermes nativo): TDD define o
  comportamento por exemplo; property-based amplia a cobertura por invariante.
- Hefesto em modo RÍGIDO (`[[verification-before-completion]]`): considerar
  property-based pra lógica crítica antes de fechar o card.
- Pareia bem com `[[strict-type-checking]]`: tipos pegam erros de forma; testes
  de propriedade pegam erros de lógica.
