---
name: aurora-design-tokens
description: Criar ou revisar tokens de cor, tipografia, espacamento, raio, sombra e estados interativos para interfaces consistentes. Use ao iniciar ou estabilizar um design system.
---

# Tokens De Design

## Processo

1. Localize estilos e variaveis existentes.
2. Preserve tokens existentes se ja formarem um sistema coerente.
3. Se precisar criar, defina poucos tokens sem duplicacao:
   - superficies e texto;
   - acao primaria, secundaria e estados;
   - sucesso, alerta e erro;
   - escala tipografica;
   - espacamento, raios e sombras.
4. Valide contraste para texto e controles importantes.
5. Centralize tokens na tecnologia usada pelo projeto, como CSS variables ou tema do framework.

## Proibicoes

- Nao espalhe valores de cor repetidos em dezenas de componentes.
- Nao introduza dark mode, tema novo ou biblioteca de estilos sem necessidade ou pedido.
