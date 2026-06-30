---
name: go-microservices
description: >
  Skill completa para desenvolvimento de microsserviços em Go (Golang), 
  com padrões de concorrência, APIs REST/gRPC, persistência, observabilidade, 
  testes, deployment em containers e arquitetura cloud-native.
alwaysApply: false
globs:
  - "**/*.go"
  - "**/go.mod"
  - "**/go.sum"
  - "**/Dockerfile"
  - "**/*.proto"
triggerEvents:
  - "file:create:**/*.go"
  - "command:review"
  - "command:go-generate"
---

# Go Microservices — Skill de Desenvolvimento Go

## Stack e Versões

- **Go 1.24+** (1.25+ recommended), toolchain, workspace mode
- **Chi Router** (go-chi/chi/v5) ou **Gin** para REST APIs
- **gRPC** + **Protocol Buffers** (buf.build) para comunicação interna
- **sqlx** ou **pgx** para PostgreSQL
- **Redis/go-redis** para cache
- **Docker multi-stage builds** com `distroless` ou `scratch`
- **Testify** + **gomock**/**mockgen** para testes
- **OpenTelemetry Go SDK** para tracing/métricas
- **Kubernetes** para orquestração

## Arquitetura Clean / Hexagonal

```
┌─────────────┐    ┌──────────────┐    ┌────────────┐
│   Handler   │ →  │   Service    │ →  │ Repository │
│  (HTTP/gRPC)│    │  (Business)  │    │   (Data)   │
└─────────────┘    └──────────────┘    └────────────┘
       ↓                   ↓                  ↓
   DTO/Request        Domain Model        SQL/gRPC
```

### Handler Layer
- Apenas parsing de request + validação + chamada ao Service
- NUNCA colocar lógica de negócio aqui
- Tratar contexto (`context.Context`) com timeout

```go
// Handler limpo
func (h *UsuarioHandler) Criar(w http.ResponseWriter, r *http.Request) {
    var req CriarUsuarioRequest
    if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
        http.Error(w, "invalid request", http.StatusBadRequest)
        return
    }
    
    resp, err := h.service.Criar(r.Context(), req)
    if err != nil {
        h.writeError(w, err)
        return
    }
    
    h.writeJSON(w, http.StatusCreated, resp)
}
```

### Service Layer
- Regras de negócio PURAS — sem dependência de HTTP
- Injeção de dependência via interface (não struct concreto)
- Transações gerenciadas explicitamente

```go
type UsuarioService struct {
    repo  UsuarioRepository
    cache Cache
}

func (s *UsuarioService) Criar(ctx context.Context, req CriarUsuarioRequest) (*UsuarioResponse, error) {
    if err := req.Validate(); err != nil {
        return nil, fmt.Errorf("validação: %w", err)
    }
    
    usuario := &Usuario{
        Nome:  req.Nome,
        Email: req.Email,
    }
    
    if err := s.repo.Salvar(ctx, usuario); err != nil {
        return nil, fmt.Errorf("salvar usuário: %w", err)
    }
    
    return ToResponse(usuario), nil
}
```

## REST API Standards

- **Versionamento por header**: `Accept: application/vnd.api+json;version=1`
- **Response uniforme**:
  ```json
  {"data": {...}, "meta": {...}, "errors": null}
  ```
- **Erros**: Estrutura padronizada com código, mensagem, detalhes
- **Pagination**: `?cursor=...&limit=20` (cursor-based) ou `?page=1&size=20`
- **Validação**: `go-playground/validator` ou validação manual em `Validate()` do request

## gRPC (comunicação entre serviços)

```protobuf
service UsuarioService {
    rpc Criar (CriarUsuarioRequest) returns (UsuarioResponse);
    rpc BuscarPorId (BuscarUsuarioRequest) returns (UsuarioResponse);
}
```

- Usar **buf.build** para gerenciamento de protos
- **gRPC interceptors** para logging, tracing, auth
- **Connect-go** para compatibilidade REST+gRPC

## Concorrência Go

- **Goroutines**: Lançar com `go func()`, sempre com waitgroup ou errgroup
- **Context**: `context.Context` no primeiro parâmetro de toda função de I/O
- **Channels**: Preferir canais tipados com buffer pequeno
- **Sync**: `sync.Mutex` para estado compartilhado, `sync.Map` para caches
- **ErrGroup**: `golang.org/x/sync/errgroup` para fan-out/fan-in
- **Rate limit**: `golang.org/x/time/rate` para throttling

```go
g, ctx := errgroup.WithContext(ctx)
for _, item := range items {
    item := item // puxar pra dentro do escopo
    g.Go(func() error {
        return processar(ctx, item)
    })
}
if err := g.Wait(); err != nil {
    return fmt.Errorf("processamento em lote: %w", err)
}
```

## Performance

- **Pool de objetos**: `sync.Pool` para alocações frequentes
- **Zero alocações**: Pre-alocar slices, evitar `fmt.Sprintf` em hot paths
- **JSON**: `encoding/json` para geral, `jsoniter` para alta performance
- **I/O**: `io.Copy` com buffer, `bytes.Buffer` para concatenação
- **Profiling**: `pprof` habilitado em `/debug/pprof/`
- **Benchmarks**: `go test -bench=. -benchmem` obrigatório em hot paths

## Testes

```go
// Unit test com testify
func TestCriarUsuario(t *testing.T) {
    // Arrange
    mockRepo := new(MockUsuarioRepository)
    svc := NewUsuarioService(mockRepo)
    
    mockRepo.On("Salvar", mock.Anything, mock.AnythingOfType("*Usuario")).
        Return(nil)
    
    // Act
    resp, err := svc.Criar(context.Background(), CriarUsuarioRequest{
        Nome: "João", Email: "joao@email.com",
    })
    
    // Assert
    assert.NoError(t, err)
    assert.NotNil(t, resp)
    assert.Equal(t, "João", resp.Nome)
    mockRepo.AssertExpectations(t)
}

// Integration test com testcontainers-go
func TestPostgresRepositorio(t *testing.T) {
    postgres, err := testcontainers.StartContainer(
        context.Background(),
        testcontainers.WithImage("postgres:16"),
    )
    // ...
}
```

## Observabilidade

```go
// OpenTelemetry setup
tp, _ := sdktrace.NewProvider(
    sdktrace.WithBatcher(otlpexp.NewExporter(ctx, opts)),
    sdktrace.WithResource(resource.NewWithAttributes(
        semconv.SchemaURL,
        semconv.ServiceNameKey.String("usuario-service"),
    )),
)
otel.SetTracerProvider(tp)

// Middleware de tracing automático (ex: chi)
r.Use(otelhttp.NewMiddleware(""))
```

## Deployment

- **Multi-stage Dockerfile**:
  ```dockerfile
  FROM golang:1.24 AS build
  RUN CGO_ENABLED=0 go build -o /app .
  
  FROM gcr.io/distroless/base-debian12
  COPY --from=build /app /app
  CMD ["/app"]
  ```
- **Health probes**: `/healthz` (liveness) e `/readyz` (readiness)
- **Graceful shutdown**: `signal.NotifyContext` + `http.Server.Shutdown`
- **Config**: `viper` + env vars, 12-factor app

## Boas Práticas Go

- **NUNCA** usar `panic` para erros esperados — retorne `error`
- **Erros**: `fmt.Errorf("contexto: %w", err)` com wrapping
- **Naming**: `CamelCase` exportado, `camelCase` privado
- **Pacotes**: Um por diretório, nomes curtos (`http`, `svc`, `repo`)
- **Init**: Evitar `init()`, preferir `New() *Service` explícito
- **Interface**: Definir no consumidor, não no produtor
- **Linter**: `golangci-lint` com `gosec`, `revive`, `errcheck`

## Gatilhos de Uso

- **Criar handler**: Use chi/Gin, decode/validate, delegue ao service
- **Modelar dados**: sqlx struct tags, migrations (golang-migrate), índices
- **Comunicação entre serviços**: gRPC + protobuf + interceptors
- **Concorrência**: errgroup + context + canais bufferizados
- **Revisar PR**: Goroutine leaks, race conditions, erro handling, context propagation

## Provedores de Referência

- Go Official: https://go.dev/doc/
- Chi Router: https://github.com/go-chi/chi
- sqlx: https://github.com/jmoiron/sqlx
- OpenTelemetry Go: https://opentelemetry.io/docs/languages/go/
- Testcontainers Go: https://golang.testcontainers.org/
