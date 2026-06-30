# Interoperabilidade Manual Futura - Hefesto

## Estado Atual

Este pacote e independente. Hefesto nao conversa automaticamente com Aurora, nao abre o workspace dela e nao modifica arquivos dela.

## Modelo Para Uma Troca Manual Futura

Se voce decidir fazer os dois agentes colaborarem no futuro, crie uma pasta de intercambio escolhida por voce e mova os artefatos manualmente. Exemplos de arquivos:

```text
PEDIDO.md
CONTRATO_API.md
OPENAPI.yaml
TOKENS_DESIGN.json
VALIDACAO.md
```

Uso sugerido:

1. Hefesto prepara contratos tecnicos, API, estados de erro e resultado de testes.
2. Voce revisa e copia os arquivos para o local onde Aurora podera le-los.
3. Aurora devolve requisitos visuais ou tokens pelo mesmo processo manual.
4. Voce decide o que cada workspace pode receber ou modificar.

## Limites

- Nenhuma pasta compartilhada foi configurada neste pacote.
- Nenhum agente recebe permissao para editar o workspace do outro.
- Integracao automatica somente deve ser criada em trabalho futuro, com sua autorizacao explicita.
