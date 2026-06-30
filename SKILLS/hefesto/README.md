# Hefesto - workspace OpenCode

Abra **esta pasta** como projeto no OpenCode.

## Primeiro uso

1. Rode `/connect` e escolha `DeepSeek`.
2. Insira a chave somente no campo seguro do OpenCode.
3. Rode `/models` e selecione `DeepSeek V4 Pro`.
4. Crie uma sessão nova para recarregar a configuração.
5. Rode `/start` para confirmar identidade e roteamento.

Não é necessário definir `DEEPSEEK_API_KEY` quando `/connect` já foi usado.

## Automação padrão

- `hefesto-routing` e `hefesto-workflow` são carregadas desde o início.
- Hefesto escolhe automaticamente architect, coder, debugger, explore, reviewer e security.
- Mudança não trivial termina com reviewer e verificação.

## Testes

- `/plan adicionar endpoint de healthcheck`
- `/debug investigar este erro: ...`
- `/workflow implementar uma feature pequena`
- `/verify`

`source_vps_snapshot/` é referência histórica e não controla a execução.

