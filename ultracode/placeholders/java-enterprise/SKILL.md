---
name: java-enterprise
description: >
  Skill completa para desenvolvimento Java corporativo com Spring Boot 3.x, 
  Jakarta EE, padrões de arquitetura enterprise, segurança, performance e 
  boas práticas de código limpo. Abrange REST APIs, microsserviços, 
  bancos relacionais, mensageria, testes e deployment.
alwaysApply: false
globs:
  - "**/*.java"
  - "**/pom.xml"
  - "**/build.gradle*"
  - "**/application.yml"
  - "**/application.properties"
triggerEvents:
  - "file:create:**/*.java"
  - "command:review"
  - "command:java-generate"
---

# Java Enterprise — Skill de Desenvolvimento Corporativo

## Stack e Versões

- **Java 17+ (recomendado Java 21 LTS)**
- **Spring Boot 3.x** (Spring Framework 6+, Jakarta EE 10)
- **Maven 3.9+** ou **Gradle 8.x** com wrapper
- **JUnit 5 + Mockito + AssertJ** para testes
- **Hibernate 6 / JPA 3** para persistência
- **MapStruct** para mapeamento DTO/Entity
- **OpenAPI 3.1** (springdoc-openapi) para documentação
- **Testcontainers** para testes de integração
- **Docker / Podman** para containerização

## Arquitetura em Camadas (Strict 3-Layer)

```
Controller (REST) → Service (Business) → Repository (Data)
         ↓                    ↓                    ↓
       DTO             Domain Model             Entity/SQL
```

### Controller
- Anotar com `@RestController` e `@RequestMapping("/api/v1/...")`
- **NUNCA** colocar lógica de negócio no controller
- Validar input com `@Valid` + Bean Validation (`jakarta.validation`)
- Retornar `ResponseEntity<T>` com status HTTP apropriado
- Usar DTOs de request/response — nunca expor entidades JPA diretamente

```java
@RestController
@RequestMapping("/api/v1/usuarios")
@RequiredArgsConstructor
public class UsuarioController {
    private final UsuarioService service;
    
    @GetMapping("/{id}")
    public ResponseEntity<UsuarioResponse> buscarPorId(@PathVariable Long id) {
        return ResponseEntity.ok(service.buscarPorId(id));
    }
}
```

### Service
- Anotar com `@Service` ou `@Transactional`
- Injetar dependências via construtor (`@RequiredArgsConstructor` do Lombok)
- Lógica de negócio PURA — sem dependência de HTTP, Servlet, Framework Web
- Orquestrar chamadas a repositórios, validações e regras de domínio

### Repository
- Extender `JpaRepository<T, ID>` do Spring Data JPA
- Usar `@Query` apenas quando JPQL/QL der suporte insuficiente
- Preferir derived queries (métodos nomeados) sempre que possível

## REST API Standards

- **Versionamento explícito**: `/api/v1/`, `/api/v2/`
- **Response envelope unificado**:
  ```json
  {
    "success": true,
    "data": { ... },
    "message": null,
    "timestamp": "2026-06-18T10:00:00Z"
  }
  ```
- **Erros**: RFC 9457 (Problem Details) com `ProblemDetail` do Spring MVC
- **Paginação**: Interface `Pageable` + `Page<T>` do Spring Data
- **Validação**: `@Valid` + mensagens em `messages.properties`
- **CORS**: Configurar globalmente via `WebMvcConfigurer`, nunca `@CrossOrigin`

## Tratamento de Exceções

```java
@RestControllerAdvice
public class GlobalExceptionHandler {
    
    @ExceptionHandler(ResourceNotFoundException.class)
    public ProblemDetail handleNotFound(ResourceNotFoundException ex) {
        return ProblemDetail.forStatusAndDetail(HttpStatus.NOT_FOUND, ex.getMessage());
    }
    
    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ProblemDetail handleValidation(MethodArgumentNotValidException ex) {
        var problem = ProblemDetail.forStatus(HttpStatus.UNPROCESSABLE_ENTITY);
        problem.setDetail("Erro de validação");
        problem.setProperty("errors", ex.getBindingResult().getFieldErrors().stream()
            .map(e -> Map.of("field", e.getField(), "message", e.getDefaultMessage()))
            .toList());
        return problem;
    }
}
```

## Segurança (Spring Security 6.x)

- **JWT**: `nimbus-jose-jwt` ou spring-security-oauth2-resource-server
- Refresh token rotation obrigatória
- BCrypt para senhas (cost 12+)
- **CSRF**: Desabilitar apenas para APIs REST stateless
- **Rate limiting**: `Bucket4j` ou Spring Cloud Gateway
- **OWASP**: Sanitizar input, escapar output, contentType: application/json

## Performance

- Evitar N+1: `@EntityGraph`, `JOIN FETCH`, ou `@Query`
- Paginação CURSOR para listas grandes (evitar OFFSET)
- Cache: `@Cacheable` (Redis ou Caffeine) com invalidação explícita
- Pool de conexões: HikariCP (configurado)
- **Async**: `@Async` + `TaskExecutor` configurado, nunca chamar `Future.get()` sem timeout

## Testes

```java
// Unitário — Service isolado
@ExtendWith(MockitoExtension.class)
class UsuarioServiceTest {
    @Mock UsuarioRepository repository;
    @InjectMocks UsuarioService service;
    // ...
}

// Integração — Testcontainers + banco real
@SpringBootTest
@Testcontainers
class UsuarioRepositoryTest {
    @Container
    static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>("postgres:16");
    // ...
}
```

## Logging e Observabilidade

- **Structured logging**: Logback + JSON encoder
- **Correlation ID**: via MDC filter em cada request
- **Métricas**: Micrometer + Prometheus (`/actuator/prometheus`)
- **Health checks**: Liveness + Readiness separados
- **Tracing**: Micrometer Tracing + Zipkin/OpenTelemetry

## Boas Práticas Gerais

- `@Data` do Lombok apenas em DTOs simples; entidades usam `@Getter @Setter` explícito
- Mutable -> imutável: `List.of()`, `@Value`, records
- Injeção de dependência VIA CONSTRUTOR (nunca `@Autowired` em campo)
- Nunca usar `@PostConstruct` para init — usar `ApplicationRunner` ou `CommandLineRunner`
- Config externalizada via `@ConfigurationProperties` (nunca `@Value`)
- SonarQube Quality Gate: cobertura ≥ 80%, Security Hotspot = 0, A rating

## Gatilhos de Uso

- **Ao criar controller/endpoint**: Use `@RestController`, DTOs, validação, paginação
- **Ao modelar banco**: Use Flyway, entities JPA, índices explícitos, chaves compostas
- **Ao implementar regra de negócio**: Service puro, sem framework web acoplado
- **Ao revisar PR**: Verifique N+1, exception handling, cobertura de teste, segurança
- **Ao configurar segurança**: JWT com rotação, BCrypt, CORS configurado, rate limit

## Provedores de Referência

- Spring Initializr: https://start.spring.io
- Spring Boot Reference: https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/
- Spring Security: https://docs.spring.io/spring-security/reference/
- RFC 9457 Problem Details: https://www.rfc-editor.org/rfc/rfc9457
