# Java Enterprise

## Status: ✅ FILLED (SKILL.md disponivel)

Skills de **Java Enterprise** implementadas em `SKILL.md` — Spring Boot 3.x, REST APIs, seguranca, performance, testes e boas praticas.

## Conteudo da Skill (`SKILL.md`)

- **Stack**: Java 17+/21, Spring Boot 3.x, Maven/Gradle, Jakarta EE 10
- **Arquitetura**: 3-layer strict (Controller → Service → Repository)
- **REST API**: Versionamento explicito, response envelope, RFC 9457 Problem Details
- **Seguranca**: Spring Security 6.x, JWT com rotacao, BCrypt (cost 12+), rate limiting
- **Performance**: N+1 prevention, cursor pagination, cache (Redis/Caffeine)
- **Testes**: JUnit 5 + Mockito + Testcontainers
- **Observabilidade**: Structured logging, Micrometer + Prometheus, tracing

## Frameworks cobertos

- **Spring Boot 3.x** (70%+ do mercado Java)
- **Quarkus** (Cloud-native, Red Hat)
- **Jakarta EE 10** (especificacao oficial)
- **Spring Security 6.x**, Spring Data JPA, Spring Cloud

## Como instalar

```bash
# Copiar para skills globais (Windows junction)
# Ou referenciar no projeto:
ln -s "$PWD/SKILL.md" ~/.config/opencode/skills/java-enterprise/SKILL.md
```

## Fontes de referencia externas

| Fonte | URL |
|-------|-----|
| Spring Initializr | https://start.spring.io/ |
| Baeldung | https://www.baeldung.com/ |
| Quarkus Guides | https://quarkus.io/guides/ |
| Jakarta EE Specs | https://jakarta.ee/specifications/ |
| Spring Security | https://docs.spring.io/spring-security/reference/ |
| RFC 9457 | https://www.rfc-editor.org/rfc/rfc9457 |
