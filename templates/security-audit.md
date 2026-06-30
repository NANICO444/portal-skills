# Security Audit Checklist

## Autenticacao

- [ ] Senhas armazenadas com bcrypt/argon2 (NUNCA plain text)
- [ ] JWT com expiracao curta (15min access, 7d refresh)
- [ ] Refresh tokens rotacionados
- [ ] 2FA disponivel para acoes sensiveis
- [ ] Logout invalida tokens server-side

## Autorizacao

- [ ] Cada endpoint verifica permissao do usuario
- [ ] Principio do menor privilegio
- [ ] Nenhum endpoint exposto por engano
- [ ] Admin routes separadas e protegidas
- [ ] RBAC ou ABAC implementado

## Input Validation

- [ ] TODA entrada externa validada (request body, query, headers, cookies)
- [ ] Schema validation (Zod, Joi, Pydantic)
- [ ] Whitelist > Blacklist
- [ ] Tamanho maximo de input limitado
- [ ] Content-Type validado

## SQL Injection

- [ ] SEMPRE parameterized queries (nunca concatenar)
- [ ] ORM usado (Prisma, TypeORM, SQLAlchemy)
- [ ] Stored procedures usadas com cuidado
- [ ] Permissoes de DB user limitadas

## XSS

- [ ] HTML escapado em templates
- [ ] React/Vue/Angular default escape (nao usar dangerouslySetInnerHTML)
- [ ] CSP headers configurados
- [ ] Trusted Types onde possivel

## CSRF

- [ ] Tokens CSRF em forms
- [ ] SameSite cookies
- [ ] Origin/Referer validation
- [ ] Double-submit cookie pattern

## Cryptography

- [ ] TLS 1.3+ em todas as comunicacoes
- [ ] HSTS habilitado
- [ ] Certificados validos
- [ ] Dados em repouso encriptados (AES-256)
- [ ] Chaves rotacionadas periodicamente (90 dias)
- [ ] bcrypt cost >= 12

## Secrets

- [ ] Nenhuma credencial em codigo
- [ ] Nenhuma credencial em git history
- [ ] Nenhuma credencial em logs
- [ ] Vault usado (HashiCorp, AWS Secrets, etc)
- [ ] Pre-commit hooks (gitleaks, trufflehog)
- [ ] CI/CD secrets separados

## API Security

- [ ] Rate limiting (100 req/min padrao)
- [ ] Rate limit por usuario E IP
- [ ] Login: max 5 tentativas/min
- [ ] CORS whitelist (nao usar `*` com credenciais)
- [ ] Headers: X-Content-Type-Options, X-Frame-Options

## Logging

- [ ] Login (sucesso e falha)
- [ ] Mudanca de senha
- [ ] Acesso a dados sensiveis
- [ ] Erros 401/403
- [ ] Mudanca de permissoes
- [ ] SEM PII em logs

## Dependencias

- [ ] `npm audit` / `pip-audit` / `safety check`
- [ ] Renovate ou Dependabot
- [ ] Pin de versao (evitar wildcards)
- [ ] SBOM (Software Bill of Materials) gerado

## Compliance

- [ ] LGPD / GDPR se aplicavel
- [ ] Consentimento para coleta de dados
- [ ] Direito ao esquecimento implementado
- [ ] Exportacao de dados do usuario
- [ ] DPO designado (se aplicavel)

## Resposta a Incidentes

- [ ] Plano de resposta documentado
- [ ] Contato de seguranca conhecido
- [ ] Backup testado
- [ ] Restore testado
- [ ] Comunicacao para usuarios preparada

## Output

```
SECURITY AUDIT - [data]

CRITICOS ENCONTRADOS: X
ALTOS: Y
MEDIOS: Z
BAIXOS: W

ACAO IMEDIATA:
1. [critico 1]
2. [critico 2]

PROXIMOS 30 DIAS:
1. [alto 1]
2. [alto 2]
```
