---
name: rust-systems
description: >
  Skill completa para desenvolvimento de sistemas em Rust: aplicações de 
  alto desempenho, ferramentas CLI, sistemas embarcados, WebAssembly, 
  servidores HTTP, processamento concorrente seguro (Send/Sync), 
  padrões de segurança de memória, FFI, e integração com C/C++.
alwaysApply: false
globs:
  - "**/*.rs"
  - "**/Cargo.toml"
  - "**/Cargo.lock"
  - "**/*.wasm"
triggerEvents:
  - "file:create:**/*.rs"
  - "command:review"
  - "command:rust-generate"
---

# Rust Systems — Skill de Desenvolvimento Rust

## Stack e Versões

- **Rust Edition 2024** (rustc 1.80+, toolchain via rustup)
- **Cargo workspace** para projetos multi-crate
- **Tokio** (async runtime) para servidores e I/O concorrente
- **Axum** (Tokio-based) para HTTP APIs modernas
- **Tonic** para gRPC (com Prost para protobuf)
- **SQLx** para PostgreSQL assíncrono (compile-time checked queries)
- **Clap** para CLI argument parsing
- **Serde** para serialização JSON/YAML/TOML
- **Tracing** para logging estruturado e spans
- **Criterion** para benchmarks

## Filosofia: Segurança por Construção

```
cargo clippy  →  cargo build  →  cargo test  →  cargo fmt --check
cargo deny check (dependências) → cargo audit (CVEs)
```

- **Sem `unsafe` sem revisão** — todo bloco `unsafe` exige comentário `// SAFETY:`
- **Sem unwrap() em produção** — usar `?`, `.context()`, `.unwrap_or()`
- **Zero-cost abstractions** — iteradores, traits genéricos, enum dispatch
- **Send + Sync** — garantido pelo compilador; `Arc<Mutex<T>>` ou `tokio::sync::*`
- **Ownership** — sem garbage collector, sem ponteiros soltos

## Arquitetura de Aplicação

```
src/
├── main.rs          # Entrypoint
├── lib.rs           # Lógica core
├── routes/          # Handlers HTTP
├── models/          # Structs de domínio
├── services/        # Lógica de negócio
├── db/              # Repositórios/queries
├── middleware/      # Auth, logging, rate limit
├── config/          # Estruturas de configuração
└── errors/          # Tipos de erro unificados
```

### Exemplo: Axum Handler

```rust
use axum::{extract::State, Json, http::StatusCode};
use serde::{Deserialize, Serialize};

#[derive(Deserialize)]
pub struct CriarUsuarioRequest {
    pub nome: String,
    pub email: String,
}

#[derive(Serialize)]
pub struct UsuarioResponse {
    pub id: i64,
    pub nome: String,
    pub email: String,
}

pub async fn criar_usuario(
    State(svc): State<Arc<UsuarioService>>,
    Json(req): Json<CriarUsuarioRequest>,
) -> Result<Json<UsuarioResponse>, AppError> {
    let usuario = svc.criar(req).await?;
    Ok(Json(usuario))
}
```

## Async Rust (Tokio)

- **Runtime**: `#[tokio::main]`, um runtime por processo
- **Tasks**: `tokio::spawn` para I/O concorrente, `JoinSet` para fan-out
- **Sincronização**: `tokio::sync::Mutex` (não `std::sync::Mutex` dentro de await)
- **Streams**: `tokio_stream::StreamExt` + `futures::TryStreamExt`
- **Timeouts**: `tokio::time::timeout` para toda chamada externa
- **Cancelamento**: Usar `CancellationToken` do Tokio para graceful shutdown

```rust
use tokio_util::sync::CancellationToken;

let cancel = CancellationToken::new();
let handle = tokio::spawn(async move {
    tokio::select! {
        _ = processar() => {},
        _ = cancel.cancelled() => {
            tracing::info!("Task cancelled");
        }
    }
});
// ...
cancel.cancel();
```

## Tratamento de Erros

```rust
// Erro unificado com thiserror
#[derive(thiserror::Error, Debug)]
pub enum AppError {
    #[error("recurso não encontrado: {0}")]
    NotFound(String),
    
    #[error("erro de validação: {0}")]
    Validacao(String),
    
    #[error(transparent)]
    Database(#[from] sqlx::Error),
    
    #[error("erro interno")]
    Internal(#[from] anyhow::Error),
}

// Implementar IntoResponse para Axum
impl IntoResponse for AppError {
    fn into_response(self) -> axum::response::Response {
        let (status, message) = match &self {
            AppError::NotFound(_) => (StatusCode::NOT_FOUND, self.to_string()),
            AppError::Validacao(_) => (StatusCode::UNPROCESSABLE_ENTITY, self.to_string()),
            AppError::Database(_) => (StatusCode::INTERNAL_SERVER_ERROR, "db error".into()),
            AppError::Internal(_) => (StatusCode::INTERNAL_SERVER_ERROR, "internal error".into()),
        };
        (status, Json(serde_json::json!({"error": message}))).into_response()
    }
}
```

## Concorrência Segura

| Padrão | Uso | Exemplo |
|--------|-----|---------|
| `Arc<T>` | Compartilhar imutável entre threads | `Arc<AppState>` |
| `Arc<Mutex<T>>` | Mutação compartilhada (std) | Cache local síncrono |
| `Arc<RwLock<T>>` | Leitores múltiplos, 1 escritor | Config compartilhada |
| `tokio::sync::Mutex` | Mutação entre `.await` pontos | Pool de conexões |
| `tokio::sync::RwLock` | Leituras frequentes + escrita rara | State global |
| `tokio::sync::oneshot` | 1 produtor → 1 consumidor | Resposta de task |
| `tokio::sync::mpsc` | Múltiplos produtores, 1 consumidor | Pipeline de eventos |

## Performance

- **Perf**: `cargo flamegraph` para identificar gargalos
- **Alocação**: Pre-alocar com `Vec::with_capacity`, reutilizar buffers
- **Iteradores**: Preferir `Iterator` methods sobre loops manuais (otimiza melhor)
- **String**: `String` vs `&str` — `Cow<'_, str>` quando incerto
- **Serialização**: `serde_json::to_writer` (streaming) para payloads grandes
- **Benchmarks**: `criterion` para funções críticas

## CLI (Clap)

```rust
#[derive(Parser)]
#[command(name = "meu-servico", version, about)]
struct Cli {
    #[arg(short, long, default_value = "config.toml")]
    config: PathBuf,
    
    #[command(subcommand)]
    command: Option<Comando>,
}

#[derive(Subcommand)]
enum Comando {
    Servidor { #[arg(short, long, default_value = "3000")] porta: u16 },
    Migrar,
}
```

## Testes

```rust
#[cfg(test)]
mod tests {
    use super::*;
    
    #[tokio::test]
    async fn test_criar_usuario() {
        let pool = cria_pool_teste().await;
        let svc = UsuarioService::new(pool);
        
        let req = CriarUsuarioRequest {
            nome: "João".into(),
            email: "joao@email.com".into(),
        };
        
        let resp = svc.criar(req).await.unwrap();
        assert_eq!(resp.nome, "João");
    }
    
    #[tokio::test]
    async fn test_email_duplicado() {
        // ...
    }
}
```

## Observabilidade (Tracing)

```rust
use tracing::{info, error, instrument, span, Level};

#[instrument(skip(service))]
pub async fn criar_usuario_handler(
    State(service): State<Arc<UsuarioService>>,
    Json(req): Json<CriarUsuarioRequest>,
) -> Result<Json<UsuarioResponse>, AppError> {
    info!("criando usuário: {}", req.email);
    let usuario = service.criar(req).await?;
    Ok(Json(usuario))
}

// Initialization
tracing_subscriber::fmt()
    .with_env_filter("meu_servico=debug,tokio=warn")
    .json()
    .init();
```

## Boas Práticas

- **NUNCA** usar `unsafe` sem `// SAFETY:` explicando POR QUE é seguro
- **NUNCA** usar `.unwrap()` em código de produção — usar `?` ou `.context()`
- **NUNCA** ignorar warnings do compilador — `#[warn(unused)]` é erro
- **NUNCA** usar `std::mem::transmute` ou `pointer::offset` sem revisão
- **Sempre** rodar `cargo clippy`, `cargo fmt`, `cargo test` antes de commit
- **Sempre** documentar `pub` items com `///` doc comments
- **Usar** `dead_code` lint em crates binárias (permitir em libs intencionalmente)

## Gatilhos de Uso

- **Criar servidor HTTP**: Axum + Tokio + Tracing + graceful shutdown
- **Criar CLI**: Clap + anyhow + tracing (file/console)
- **Criar lib**: Documentação completa, `#[must_use]`, sem pânicos
- **Concorrência**: Tokio tasks + canais + CancellationToken
- **FFI**: `#[repr(C)]`, `extern "C"`, `cbindgen` header generation
- **Revisar PR**: Unsafe justification, erro handling, Send/Sync, clone costs, unwraps

## Provedores de Referência

- Rust Book: https://doc.rust-lang.org/book/
- Rust Async Book: https://rust-lang.github.io/async-book/
- Axum Guide: https://docs.rs/axum/latest/axum/
- Tokio Tutorial: https://tokio.rs/tokio/tutorial
- SQLx: https://github.com/launchbadge/sqlx
- Clap: https://docs.rs/clap/latest/clap/
