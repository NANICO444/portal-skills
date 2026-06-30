# Rust Systems

## Status: ✅ FILLED (SKILL.md disponivel)

Skills de **Rust** implementadas em `SKILL.md` — Axum/Tokio, Async Rust, concorrencia segura, PostgreSQL, CLI com Clap, testes, FFI e safety.

## Conteudo da Skill (`SKILL.md`)

- **Stack**: Rust Edition 2024, Tokio, Axum, Tonic (gRPC), SQLx, Clap, Serde, Tracing
- **Filosofia**: Seguranca por construcao — sem unsafe sem revisao, sem unwrap em producao
- **Arquitetura**: Axum handlers → Services → DB repositories
- **Async**: Tokio runtime, tasks, CancellationToken, graceful shutdown
- **Erros**: thiserror + anyhow, IntoResponse para Axum, zero panics
- **Concorrencia**: Arc, Mutex, RwLock, canais (oneshot/mpsc), Send+Sync garantido
- **Performance**: flamegraph, pre-alocacao, criterion benchmarks, zero-cost abstractions
- **Testes**: tokio::test, testcontainers, cargo clippy obrigatorio
- **CLI**: Clap + anyhow + tracing
- **Seguranca**: Todo bloco unsafe exige // SAFETY:, deny checked, audit CVEs

## Frameworks cobertos

- **Axum** (HTTP, Tokio-based)
- **Tonic** (gRPC)
- **Tokio** (async runtime)
- **SQLx** (PostgreSQL async, compile-time checked)
- **Clap** (CLI)
- **Tracing** (observabilidade)
- **Criterion** (benchmarks)

## Como instalar

```bash
# Copiar para skills globais
cp SKILL.md ~/.config/opencode/skills/rust-systems/SKILL.md
```

## Fontes de referencia externas

| Fonte | URL |
|-------|-----|
| The Rust Book | https://doc.rust-lang.org/book/ |
| Rust Async Book | https://rust-lang.github.io/async-book/ |
| Axum Guide | https://docs.rs/axum/latest/axum/ |
| Tokio Tutorial | https://tokio.rs/tokio/tutorial |
| SQLx | https://github.com/launchbadge/sqlx |
