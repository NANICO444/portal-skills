# Aurora - workspace OpenCode

Abra **esta pasta** como projeto no OpenCode.

## Primeiro uso

1. Rode `/connect` e escolha `DeepSeek`.
2. Insira a chave somente no campo seguro do OpenCode.
3. Rode `/models` e selecione `DeepSeek V4 Pro`.
4. Crie uma sessão nova para recarregar a configuração.
5. Rode `/start` para confirmar identidade, personas e roteamento.

Não é necessário definir `DEEPSEEK_API_KEY` quando `/connect` já foi usado.

## Automação padrão

- `aurora-routing` e `aurora-workflow` são carregadas desde o início.
- Aurora executa FASE -1 e escolhe personas/subagentes automaticamente.
- Toda entrega não trivial passa por Accessibility, Performance e Reality.
- Deploy permitido somente em STAGING e com confirmação.

## Testes

- `/brief-design landing page para ...`
- `/mood criar três direções para ...`
- `/design construir a tela ...`
- `/audit revisar esta interface`

`source_vps_snapshot/` é referência histórica e não controla a execução.

