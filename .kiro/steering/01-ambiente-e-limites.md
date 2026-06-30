---
inclusion: always
---

# Ambiente Local & Limites (Regras de Ouro)

## Ambiente
- **PC Windows local** — Kiro IDE / OpenCode. Sem servidor remoto, nuvem, pipeline ou ferramenta externa não instalada.
- **Workspace = esta pasta apenas** (`mkdir meu-agente/`). **Nada fora daqui** sem autorização explícita.
- **Python:** **venv obrigatório** (`.venv/` na raiz). Nunca instale pacotes globalmente.
- **Node/JS:** Use `npx` ou scripts locais (`package.json`). Nunca `npm install -g`.
- **Segredos:** **NUNCA** no código, logs, commits, arquivos versionados. `.env` só local, no `.gitignore`.

## Limites Rígidos — Confirmação OBRIGATÓRIA Antes De:
- 📦 Publicar, deploy, alterar infraestrutura, mexer em produção
- 🔐 Usar, criar, copiar, rotacionar segredos e credenciais
- 🗄️ Migrar ou apagar dados reais
- 🌐 Instalar dependência global, contratar serviço, gerar custo
- 💥 Apagar arquivos em massa, reescrever histórico Git, force push
- 🚫 Modificar algo **fora deste workspace**

## Preservação
- Alterações preexistentes fora do escopo atual: **preservem**.
- Arquivos em `referencias_originais/` (Hefesto/Aurora originais): **somente leitura — nunca modifiquem**.
- Regras, skills, agents, steering desta pasta: **não modifiquem sem autorização**.