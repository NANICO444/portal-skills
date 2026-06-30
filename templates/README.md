# Templates

Templates reutilizaveis para documentacao e padronizacao.

| Arquivo | Quando usar |
|---------|-------------|
| [PR.md](PR.md) | Pull Request |
| [ADR.md](ADR.md) | Architecture Decision Record |
| [review.md](review.md) | Code review (output do @supervisor) |
| [bug-report.md](bug-report.md) | Reportar um bug |
| [feature-request.md](feature-request.md) | Pedir nova feature |
| [test-plan.md](test-plan.md) | Plano de teste |
| [security-audit.md](security-audit.md) | Auditoria de seguranca |
| [performance-audit.md](performance-audit.md) | Auditoria de performance |
| [onboarding.md](onboarding.md) | Checklist para novo dev |

## Como usar

1. Copie o template para o local certo
2. Renomeie (se for PR: `PR-123.md`, se for ADR: `ADR-001-titulo.md`)
3. Preencha cada secao
4. Remova comentarios HTML (`<!-- ... -->`)
5. Commite

## Boas praticas

- **Sempre preencher todas as secoes** (ou marcar N/A com motivo)
- **Links** para issues/PRs/ADRs relacionados
- **Datas** em qualquer registro
- **Contexto** para quem nao estava presente
