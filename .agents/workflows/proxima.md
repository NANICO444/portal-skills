# /proxima — Executa a próxima missão do Nexus OS

**Contexto:** Este projeto usa **Hefesto** (engenharia) como principal e **Aurora** (design) para interfaces. Skills em `.kiro/skills/hefesto-*` e `.kiro/skills/aurora-*`. Leia `AGENTS.md` antes para entender a divisão.

Quando eu digitar `/proxima`, siga este loop, sem pular passo:

0. **Se a triagem ainda não foi feita** (seções "Onde estou" / "Pra onde vou" do `ESTADO.md` em branco), rode primeiro o **COMANDO 0** (análise + diálogo de classificação usando skills `hefesto-codebase-onboarding` e ore processo de triagem) e pare. Não comece a programar sem o estado mapeado.
1. Leia `ESTADO.md`, `AGENTS.md` e `REGRAS_GERAIS.md`.
2. Identifique a **missão atual** e a **próxima tarefa concreta**.
3. **Classifique a tarefa:**
   - **Engenharia (backend, lógica, testes, API, banco)** → Hefesto lidera. Ative skill relevante de `.kiro/skills/hefesto-*`.
   - **Design/Interface (landing page, temas, componentes, UX)** → Aurora lidera. Ative skill relevante de `.kiro/skills/aurora-*`.
   - **Mista** → Hefesto planeja a técnica, Aurora cuida do visual.
4. Em no máximo 3 linhas, me diga: (a) o que vai fazer, (b) qual skill vai usar, (c) como eu vou saber que funcionou. **NÃO code ainda.** Espere meu "ok".
5. Depois do meu "ok": implemente a **menor mudança** que cumpre a tarefa. Use venv para Python (`.venv\Scripts\Activate.ps1`). Respeite a TRAVA DE ESCOPO, as regras Karpathy do `AGENTS.md` e as regras de organização da `REGRAS_GERAIS.md`.
6. **Rode e teste** — abra o site no navegador, rode o app Python, execute testes. Se falhar, conserte e repita — não me devolva quebrado.
7. **Verifique** — use steering 05-verificacao-entrega.md como checklist antes de entregar.
8. `git status` + `git diff` + `git add -A && git commit -m "<tipo: mensagem curta>"`.
9. Atualize `ESTADO.md`: marque o item, atualize "Onde estou" e escreva a próxima missão. **Pare e me mostre o resultado em palavras simples.**

Se a tarefa estiver fora da Fase 1, **não faça** — registre em `IDEIAS_FUTURAS.md` e me avise.
Se eu quiser mergulhar numa feature legal (tipo avatar, novos agentes), valide meu entusiasmo e me redirecione pra missão atual com gentileza.
