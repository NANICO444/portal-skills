---
inclusion: auto
name: dados-seguranca-api
description: Orientação ao tocar autenticação, API, banco de dados, configuração, upload, integrações, segredos ou dados do usuário. Hefesto lidera, Aurora apoia.
---

# Dados, Segurança & API (Regras Comuns)

## Princípios
- ✅ **Valide entrada** e imponha autorização nos limites apropriados.
- 🚫 **NUNCA** coloque segredo no frontend, código versionado, log ou mensagem de erro.
- 📝 **Mudanças de API** — registre contrato, compatibilidade, versionamento.
- 🔄 **Migrações de dados** — exigem plano de rollback testado + confirmação antes de atingir dados reais.
- 🧪 **Operações sensíveis** — testes explícitos ou declaração clara de impossibilidade.

## Por Camada
### Backend/API (Hefesto)
- Autenticação/autorização: valide no servidor, não confie no cliente.
- Rate limiting, validação de schema, sanitização.
- Logs de auditoria sem dados sensíveis.

### Frontend/Interface (Aurora)
- **Zero segredos** no browser — nem em localStorage, nem em variáveis JS.
- Formulários: validação UX + envio seguro para API.
- Estados de loading/erro/sucesso claros para o usuário.

### Configuração & Ambiente
- `.env` apenas local, no `.gitignore`, nunca commitado.
- Rotação de chaves: processo documentado, confirmação obrigatória.
- Variáveis de ambiente: prefixo claro (`NEXUS_`, `OPENROUTER_`, etc.).

## Checklist Rápido Antes de Mexer Nisto
- [ ] Entendi o fluxo real de dados?
- [ ] Tenho plano de rollback se der errado?
- [ ] Confirmou com João/Papai Joe se envolve credencial/custo/produção?
- [ ] Testes cobrem o caminho crítico?
- [ ] Diff revisado — sem segredo, sem vazamento?