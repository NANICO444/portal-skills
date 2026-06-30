# Go Microservices

## Status: ✅ FILLED (SKILL.md disponivel)

Skills de **Go** para microsservicos implementadas em `SKILL.md` — Chi/Gin, gRPC, concorrencia, PostgreSQL, containers, observabilidade e testes.

## Conteudo da Skill (`SKILL.md`)

- **Stack**: Go 1.24+, Chi/Gin, gRPC (buf.build), sqlx/pgx, Redis
- **Arquitetura**: Clean/Hexagonal (Handler → Service → Repository)
- **REST API**: Versionamento header, response uniforme, paginacao cursor
- **gRPC**: Protobuf, interceptors, Connect-go, buf.build
- **Concorrencia**: goroutines, errgroup, context.Context, channels, rate limiting
- **Performance**: sync.Pool, zero alloc, pprof, benchmarks obrigatorios
- **Testes**: Testify + gomock + testcontainers-go
- **Seguranca**: Nenhum panic para erros esperados, erros com wrapping
- **Observabilidade**: OpenTelemetry tracing + metrics, health probes

## Frameworks cobertos

- **Chi Router** / **Gin** (REST)
- **gRPC** + Protocol Buffers (RPC interno)
- **sqlx** / **pgx** (PostgreSQL)
- **Testcontainers Go** (testes integracao)
- **OpenTelemetry Go SDK** (observabilidade)
- **Docker multi-stage** + distroless (deployment)

## Como instalar

```bash
# Copiar para skills globais
cp SKILL.md ~/.config/opencode/skills/go-microservices/SKILL.md
```

## Fontes de referencia externas

| Fonte | URL |
|-------|-----|
| Go Official | https://go.dev/doc/ |
| Chi Router | https://github.com/go-chi/chi |
| sqlx | https://github.com/jmoiron/sqlx |
| OpenTelemetry Go | https://opentelemetry.io/docs/languages/go/ |
| Testcontainers Go | https://golang.testcontainers.org/ |
