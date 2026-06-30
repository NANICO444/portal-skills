---
name: csharp-dotnet
description: >
  Skill completa para desenvolvimento .NET com C#, ASP.NET Core, Entity 
  Framework, padrões cloud-native, performance, segurança, testes e 
  práticas modernas de engenharia de software na plataforma .NET 10.
alwaysApply: false
globs:
  - "**/*.cs"
  - "**/*.csproj"
  - "**/*.sln"
  - "**/appsettings.json"
  - "**/Program.cs"
triggerEvents:
  - "file:create:**/*.cs"
  - "command:review"
  - "command:dotnet-generate"
---

# C# .NET — Skill de Desenvolvimento Moderno

## Stack e Versões

- **.NET 10 LTS** (C# 13, runtime otimizado, Native AOT)
- **ASP.NET Core 10** (Minimal APIs, Endpoint Filters, Middleware nativo)
- **Entity Framework Core 10** (ORM, migrações, interceptors)
- **FluentValidation** para validação de input
- **MediatR** para CQRS / pipeline de comandos
- **Serilog** + **OpenTelemetry** para observabilidade
- **xUnit + FluentAssertions + Testcontainers** para testes
- **.NET Aspire 13+** para orquestração distribuída
- **Microsoft Agent Framework** para integração com AI

## Filosofia de Arquitetura

### 3-Layer Strict (com variação Clean/MediatR)

```
API Layer (Controllers/Minimal API) → Application Layer (MediatR) → Infrastructure (EF Core)
          ↓                                     ↓
      DTO/Contracts                        Commands/Queries
```

### Minimal APIs (preferenciais para microsserviços)

```csharp
// .NET 10 — Minimal API com endpoint filters
var builder = WebApplication.CreateBuilder(args);
builder.Services.AddScoped<IUsuarioService, UsuarioService>();

var app = builder.Build();

app.MapGet("/api/v1/usuarios/{id}", async (int id, IUsuarioService service) =>
{
    var result = await service.BuscarPorIdAsync(id);
    return result is not null ? Results.Ok(result) : Results.NotFound();
})
.WithName("GetUsuario")
.WithOpenApi();

app.Run();
```

### Controllers (preferenciais para APIs complexas)

```csharp
[ApiController]
[Route("api/v1/[controller]")]
public class UsuariosController : ControllerBase
{
    private readonly IMediator _mediator;
    
    public UsuariosController(IMediator mediator) => _mediator = mediator;

    [HttpGet("{id:guid}")]
    public async Task<ActionResult<UsuarioResponse>> Get(Guid id)
    {
        return Ok(await _mediator.Send(new GetUsuarioQuery(id)));
    }
}
```

## REST API Standards (.NET 10)

- **Versionamento**: `ApiVersion` + URL path `/api/v{version:apiVersion}/`
- **Response envelope**: `IResult` com `Results.Ok/Created/NoContent/Problem`
- **Erros RFC 9457**: `ProblemDetails` built-in do ASP.NET Core
- **Validação**: `FluentValidation` + `ValidationFilter` (Endpoint Filter global)
- **Health checks**: Liveness `/healthz` + Readiness `/ready` separados

```csharp
builder.Services.AddHealthChecks()
    .AddDbContextCheck<AppDbContext>()
    .AddRedis("redis");
```

## EF Core 10 — Boas Práticas

- **NUNCA** usar `.Result`, `.Wait()` ou `Task.Run` em async
- Migrações com `dotnet ef migrations add` + aplicação automática em dev
- **AsNoTracking()** para queries somente leitura
- **Batch operations**: `ExecuteUpdateAsync` / `ExecuteDeleteAsync`
- **N+1 prevention**: `Include().ThenInclude()` ou `Select()` explícito
- **Interceptors**: `SaveChangesInterceptor` para auditoria automática

```csharp
public class Usuario
{
    public Guid Id { get; set; }
    public string Nome { get; set; } = string.Empty;
    public string Email { get; set; } = string.Empty;
    public DateTime CriadoEm { get; set; }
    
    // Value Object (owned entity)
    public Endereco? Endereco { get; set; }
}
```

## Segurança

- **Auth**: JWT com Azure AD / IdentityServer / Duende
- **Policies**: `[Authorize(Policy = "requer_admin")]` + claims-based
- **Senhas**: `PasswordHasher<TUser>` do ASP.NET Core Identity
- **CORS**: `builder.Services.AddCors()` configurado por origem
- **Rate limiting**: `builder.Services.AddRateLimiter()` (built-in .NET 7+)
- **Anti-forgery**: CSRF habilitado para endpoints stateful

## Performance

- **Async ALL THE WAY**: Nunca bloquear threads de I/O
- **Caching**: `IMemoryCache` (local) / `IDistributedCache` (Redis)
- **Response caching**: `[ResponseCache]` ou Output Caching middleware
- **Native AOT**: `dotnet publish -p:PublishProfile=DefaultContainer` para containers
- **Pooling**: `HttpClientFactory` + `IHttpClientFactory` (nunca `new HttpClient()`)
- **Minimize alocações**: `struct`, `Span<T>`, `ArrayPool<T>` em hot paths

## Testes

```csharp
// Unit test com xUnit
public class UsuarioServiceTests
{
    [Fact]
    public async Task BuscarPorId_QuandoExiste_RetornaUsuario()
    {
        // Arrange
        var repo = new Mock<IUsuarioRepository>();
        repo.Setup(r => r.GetByIdAsync(It.IsAny<Guid>()))
            .ReturnsAsync(new Usuario { Id = Guid.NewGuid(), Nome = "Teste" });
        var service = new UsuarioService(repo.Object);
        
        // Act
        var result = await service.BuscarPorIdAsync(Guid.NewGuid());
        
        // Assert
        Assert.NotNull(result);
        Assert.Equal("Teste", result.Nome);
    }
}

// Integration test com Testcontainers
[CollectionDefinition("Postgres")]
public class PostgresCollection : ICollectionFixture<PostgresFixture> { }
```

## Observabilidade (Aspire + OpenTelemetry)

```csharp
// Program.cs — OpenTelemetry setup
builder.Services.AddOpenTelemetry()
    .WithTracing(t => t
        .AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation()
        .AddEntityFrameworkCoreInstrumentation())
    .WithMetrics(m => m
        .AddAspNetCoreInstrumentation()
        .AddRuntimeInstrumentation())
    .ExportToZipkin();

builder.Host.UseSerilog((ctx, cfg) => cfg
    .ReadFrom.Configuration(ctx.Configuration)
    .Enrich.WithCorrelationId());
```

## .NET Aspire (Orquestração Distribuída)

- `Aspire.StackExchange.Redis` para cache distribuído
- `Aspire.Npgsql.EntityFrameworkCore.PostgreSQL` para banco
- `Aspire.Azure.ServiceBus` para mensageria
- Service discovery automático via `WithReference()`
- Dashboard de métricas, logs e traces embutida

## Boas Práticas C# 13

- **Primary constructors** para classes com DI
- **`ListPattern`** e **`SlicePattern`** para matching de coleções
- **`field` keyword** em auto-properties
- **`params ReadOnlySpan<T>`** para performance
- **Records** para DTOs: `public record UsuarioResponse(Guid Id, string Nome);`
- **NUNCA**: `async void` (exceto event handlers), `.Result`, exceptions para fluxo de controle

## Gatilhos de Uso

- **Criar endpoint**: Minimal API ou Controller + FluentValidation + ProblemDetails
- **Modelar dados**: EF Core Fluent API, migrações, owned types, índices
- **Criar microsserviço**: .NET Aspire + container nativo AOT + health checks
- **Revisar PR**: Async correctness, N+1, disposição de recursos, segurança
- **Configurar segurança**: JWT + policies + rate limiting + CORS

## Provedores de Referência

- Microsoft Learn ASP.NET Core: https://learn.microsoft.com/aspnet/core
- .NET Aspire Docs: https://learn.microsoft.com/dotnet/aspire
- OpenTelemetry .NET: https://opentelemetry.io/docs/languages/net/
