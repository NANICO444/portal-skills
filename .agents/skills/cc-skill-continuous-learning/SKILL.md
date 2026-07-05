---
name: cc-skill-continuous-learning
description: "Captura licoes aprendidas durante o trabalho (bugs recorrentes, padroes que funcionaram, preferencias do usuario, armadilhas do codebase) e consolida em memoria persistente para reuso em sessoes futuras. Use ao final de tarefas complexas, quando um bug foi resolvido, ou quando o usuario corrige um comportamento do agente."
author: affaan-m
version: "1.0"
---

# Continuous Learning

> **Quando usar:** ao final de uma tarefa nao-trivial, depois de resolver um bug dificil, ou quando o usuario corrigir explicitamente um comportamento que errou.

## O que esta skill faz

Transforma experiencias pontuais em conhecimento reusavel, evitando que os mesmos erros se repitam em sessoes futuras e acelerando tarefas similares.

## Quando usar

- Resolvi um bug que custou mais de alguns minutos
- Descobri uma convencao ou armadilha do codebase
- O usuario corrigiu meu comportamento ("nao faca X, faca Y")
- Completei um padrao de tarefa que provavelmente vai se repetir
- Aprendi uma preferencia do usuario (estilo, formato, ferramenta)

## Protocolo de captura

1. **Identifique** — O que foi aprendido? Categorize:
   - **Bug/padrao do codebase** — "Em X, sempre faca Y senao quebra Z"
   - **Preferencia do usuario** — "Usuario prefere commits atomicos em PT-BR"
   - **Armadiha** — "Biblioteca X tem bug com versao Y, usar workaround Z"
   - **Atalho/otimizacao** — "Para task X, pular etapa Y e ir direto pra Z"

2. **Valide** — Antes de gravar:
   - E geral o suficiente para reuso? (caso unico nao precisa gravar)
   - Nao contradiz licao anterior? (se contradiz, atualize aquela)
   - E acionavel? (vai mudar como faco algo no futuro?)

3. **Persista** — Escreva no local de memoria do agente:
   - Formato: `QUANDO [situacao], ENTAO [acao], PORQUE [razao]`
   - Exemplo: `QUANDO editar package.json do oh-my-openagent, ENTAO rodar bun install depois, PORQUE o prepare script recria dist/`

4. **Indexe** — Garanta que a licao sera encontrada:
   - Adicione tags ou categorias
   - Conecte com licoes relacionadas
   - Marque data/secao onde aprendeu (para revisao futura)

## Anti-padroes

- NAO gravar obviedades ("git commit salva mudancas")
- NAO gravar sem validar (pode ser coincidencia, nao padrao)
- NAO acumular sem revisar — licoes antigas podem estar desatualizadas
- NAO ignorar correcoes do usuario — sao o sinal mais forte de aprendizado
