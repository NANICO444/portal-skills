# Interoperabilidade Manual Futura - Aurora

## Estado Atual

Este pacote e independente. Aurora nao conversa automaticamente com Hefesto, nao abre o workspace dele e nao modifica arquivos dele.

## Modelo Para Uma Troca Manual Futura

Se voce decidir fazer os dois agentes colaborarem no futuro, crie uma pasta de intercambio escolhida por voce e mova os artefatos manualmente. Exemplos de arquivos:

```text
PEDIDO.md
TOKENS_DESIGN.json
CONTRATO_API.md
OPENAPI.yaml
VALIDACAO.md
```

Uso sugerido:

1. Aurora prepara direcao visual, tokens, componentes e estados de interface.
2. Voce revisa e copia os arquivos para o local onde Hefesto podera le-los.
3. Hefesto devolve contratos tecnicos, testes ou limites de implementacao pelo mesmo processo manual.
4. Voce decide o que cada workspace pode receber ou modificar.

## Limites

- Nenhuma pasta compartilhada foi configurada neste pacote.
- Nenhum agente recebe permissao para editar o workspace do outro.
- Integracao automatica somente deve ser criada em trabalho futuro, com sua autorizacao explicita.
