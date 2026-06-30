---
name: aurora-security-boundaries
description: Revisar limites de seguranca em funcionalidades locais, formularios, APIs, autenticacao, uploads, configuracao e publicacao. Use quando houver dados sensiveis ou operacoes de risco.
---

# Limites De Seguranca

- Nunca exponha segredos em frontend, commit, log ou mensagem.
- Valide entrada no backend quando houver backend.
- Trate HTML dinamico, uploads, URLs, redirecionamentos e dados de usuario com cautela.
- Nao altere autenticacao, permissoes ou producao sem confirmar escopo e testes exigidos.
- Se encontrar segredo, informe tipo e local, nunca o valor.
- Para dependencia nova, considere manutencao e risco antes de adicionar.

Relate riscos encontrados separadamente da implementacao visual.
