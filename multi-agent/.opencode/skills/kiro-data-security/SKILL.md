---
name: kiro-data-security
description: "Regras transversais de dados, segurança e API — checklist obrigatório antes de expor endpoints"
argument-hint: "[endpoint/dado a proteger]"
user-invocable: true
allowed-tools: Read, Grep, Bash, Edit
agent: security-auditor
---

# Dados, Segurança e API — Regras Transversais

Checklist obrigatório para qualquer trabalho com dados, credenciais ou endpoints.

## Dados

### Classificação
- [ ] **Público** — pode ser exposto livremente (docs, marketing)
- [ ] **Interno** — só dentro da organização (analytics agregado)
- [ ] **Confidencial** — clientes/usuários (email, telefone, endereço)
- [ ] **Sensível** — PII crítico, financeiro, saúde (CPF, cartão, senha)

### Armazenamento
- [ ] Senhas: bcrypt/argon2 NUNCA plain text
- [ ] PII: encriptado em repouso (AES-256)
- [ ] Logs: NÃO registrar PII ou credenciais
- [ ] Backup: encriptado e testado
- [ ] Retenção: política de limpeza (LGPD/GDPR)

### Transporte
- [ ] TLS 1.3+ em todas as comunicações
- [ ] HSTS habilitado
- [ ] Certificados válidos e auto-renovados
- [ ] Sem fallback para HTTP

## Segurança

### Credenciais
- [ ] NUNCA em código (git history é público)
- [ ] NUNCA em logs
- [ ] NUNCA em URLs (sempre em headers)
- [ ] NUNCA commitadas (pre-commit hook)
- [ ] Rotação periódica (90 dias para chaves)

### Onde guardar
- [ ] `.env` (com `.gitignore`)
- [ ] Vault (HashiCorp, AWS Secrets Manager, Azure Key Vault)
- [ ] CI/CD secrets (GitHub Actions secrets)
- [ ] Sistema operacional keyring (nunca texto plano)

### Pre-commit hooks
- [ ] `gitleaks` ou `trufflehog` instalado
- [ ] Detecta: AWS keys, API tokens, private keys
- [ ] Bloqueia commit se encontrar

## API

### Design
- [ ] Versionamento (URL: `/v1/`, header: `Accept: application/vnd.api+json;v=1`)
- [ ] Status codes semânticos (200, 201, 400, 401, 403, 404, 409, 422, 429, 500)
- [ ] Mensagens de erro descritivas (não vazar stack trace)
- [ ] Documentação: OpenAPI/Swagger atualizada

### Autenticação
- [ ] JWT com expiração curta (15 min access, 7d refresh)
- [ ] Refresh tokens rotacionados
- [ ] Rate limiting por usuário E por IP
- [ ] 2FA para ações sensíveis

### Validação
- [ ] Schema validation em TODA entrada (Zod, Joi, Pydantic)
- [ ] Sanitização contra XSS (escape de HTML)
- [ ] Parameterized queries contra SQLi (NUNCA concatenar)
- [ ] Whitelist de valores permitidos (não blacklist)

### Rate Limiting
- [ ] Por IP: 100 req/min (login: 5/min)
- [ ] Por usuário: 1000 req/hora
- [ ] Por endpoint sensível: limite explícito
- [ ] Headers: `X-RateLimit-Remaining`, `Retry-After`

### CORS
- [ ] Whitelist explícita de origins
- [ ] NÃO usar `*` se houver credenciais
- [ ] Métodos permitidos explícitos
- [ ] Headers permitidos explícitos

## Auditoria

### Logs de segurança
- [ ] Login (sucesso e falha)
- [ ] Mudança de senha
- [ ] Acesso a dados sensíveis
- [ ] Erros 401/403 (tentativas de acesso)
- [ ] Mudança de permissões

### Monitoramento
- [ ] Alertas para padrões anômalos
- [ ] Detecção de brute force
- [ ] Detecção de scraping
- [ ] Detecção de credential stuffing

## Compliance

### LGPD/GDPR
- [ ] Consentimento explícito para coleta
- [ ] Direito ao esquecimento (delete account)
- [ ] Exportação de dados do usuário
- [ ] Política de privacidade publicada
- [ ] DPO designado

## Regras de Ouro

✅ Segredos NUNCA em código, logs, URLs, commits, ou comentários.
✅ Validação em TODA entrada externa (cliente, API, banco, env).
✅ Princípio do menor privilégio (cada componente só vê o que precisa).
✅ Defensiva em profundidade (múltiplas camadas, não confie em uma só).

❌ Confiar em validação só do cliente.
❌ Logar request/response body inteiro (vaza PII).
❌ `*` em CORS com credenciais.
❌ Rollback de segurança sem plano (vulnerabilidade em produção é emergência).
