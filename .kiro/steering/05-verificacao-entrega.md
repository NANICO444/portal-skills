---
inclusion: always
---

# Verificação & Entrega (Sempre — Antes de Concluir QUALQUER Tarefa)

## Checklist Obrigatório

### 1. Liste Arquivos Alterados
- Mostre `git diff --name-only` ou equivalente.
- Destaque se criou/removeu/renomeou arquivos.

### 2. Execute Verificações Relevantes
| Tipo | Comando Exemplo | Quando |
|------|----------------|--------|
| Testes Python | `python -m pytest` / `python -m unittest` | Qualquer mudança Python |
| Lint Python | `ruff check .` / `flake8` | Qualquer mudança Python |
| Typecheck | `mypy` / `pyright` | Se projeto usa tipagem |
| Testes JS | `npm test` / `vitest run` | Mudança landing page |
| Lint JS | `npm run lint` / `eslint .` | Mudança landing page |
| Build | `npm run build` / `pyinstaller` | Antes de entregar executável |
| Abertura visual | Abrir `landing-page/index.html` no navegador | Qualquer mudança visual |

**Se não houver comando configurado no projeto: digam claramente o que NÃO puderam validar.**

### 3. Leia o Diff Final
- Procure alterações fora de escopo.
- Procure segredos, credenciais, tokens, chaves.
- Confira se segue estilo existente.

### 4. Declare Limitações
- O que **não** conseguiu validar e **por quê**.
- Riscos residuais conhecidos.
- Decisões que ainda dependem do usuário.

### 5. NUNCA (sem autorização expressa)
- ❌ Publique, faça merge, deploy, push para produção
- ❌ Execute operação irreversível (force push, rebase destrutivo, `rm -rf`, `DROP TABLE`)
- ❌ Alterar algo fora deste workspace

## Entrega Mínima
> "Alterei X arquivos. Rodei Y testes (passaram/falharam). Build OK. Não validei Z porque [motivo]. Riscos: [lista]. Próximo passo sugerido: [ação]."

## Para Interface (Aurora) — Adicional
- Abra/renderize a tela **localmente** (navegador, app Tkinter).
- Confirme: responsivo (mobile/desktop), teclado navega, foco visível, contraste OK, estados de erro/loading.
- Se não puder abrir: **diga claramente** — "não consegui abrir a interface localmente, validação visual pendente".