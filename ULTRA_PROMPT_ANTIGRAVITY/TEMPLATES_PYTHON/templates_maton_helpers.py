"""
maton_helpers.py — Helper CENTRAL do Ultra Prompt v6.1

Todas as funções utilitárias para integração com Maton Gateway.
Outros helpers e módulos devem importar deste arquivo.

Exports:
    - maton_request(app, path, method, data, extra_headers, timeout)
    - check_connection(app)
    - require_connections(*apps)
    - retry_with_backoff(func, max_attempts, base_delay)
    - idempotency_key(session_id, etapa, acao)
    - check_idempotency(key)
    - mark_idempotent(key)
    - pending_sync_add(entry)
    - pending_sync_flush(notion_page_id)

Constantes:
    - GATEWAY_BASE
    - CTRL_BASE
    - MATON_KEY
"""

import os
import json
import hashlib
import time
import random
import urllib.request
import urllib.error
import urllib.parse
import logging
from functools import wraps

# ---------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------

GATEWAY_BASE = "https://gateway.maton.ai"
CTRL_BASE = "https://api.maton.ai"
MATON_KEY = os.environ.get("MATON_API_KEY", "")

SESSION_DIR = os.path.join(os.path.expanduser("~"), ".session")
TRANSACTIONS_FILE = os.path.join(SESSION_DIR, "transactions.json")
PENDING_SYNC_FILE = os.path.join(SESSION_DIR, "pending_sync.json")

MAX_TRANSACTIONS = 200

logger = logging.getLogger("maton_helpers")

# ---------------------------------------------------------------------------
# Utilitários internos
# ---------------------------------------------------------------------------


def _ensure_session_dir():
    """Garante que o diretório .session existe."""
    os.makedirs(SESSION_DIR, exist_ok=True)


def _read_json_file(filepath, default=None):
    """Lê um arquivo JSON de forma segura. Retorna *default* em caso de falha."""
    if default is None:
        default = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError, OSError) as exc:
        logger.debug("Não foi possível ler %s: %s", filepath, exc)
        return default


def _write_json_file(filepath, data):
    """Escreve dados em arquivo JSON de forma segura (backup antes de sobrescrever)."""
    _ensure_session_dir()
    backup = filepath + ".bak"
    if os.path.exists(filepath):
        try:
            os.replace(filepath, backup)
        except OSError as exc:
            logger.warning("Falha ao criar backup de %s: %s", filepath, exc)
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except OSError as exc:
        logger.error("Falha ao escrever %s: %s", filepath, exc)
        # Tenta restaurar backup
        if os.path.exists(backup):
            try:
                os.replace(backup, filepath)
            except OSError:
                pass
        raise


# ---------------------------------------------------------------------------
# 1. maton_request
# ---------------------------------------------------------------------------


def maton_request(app, path, method="GET", data=None, extra_headers=None, timeout=30):
    """
    Request universal para o Maton API Gateway.

    Parâmetros:
        app (str): Nome do app/conector (ex: 'google-calendar', 'notion').
        path (str): Caminho da API após o app (ex: 'v1/events').
        method (str): Método HTTP — GET, POST, PUT, PATCH, DELETE.
        data (dict | None): Corpo da requisição (será serializado como JSON).
        extra_headers (dict | None): Headers adicionais além do padrão.
        timeout (int): Timeout em segundos (padrão 30).

    Retorna:
        dict: Resposta JSON parseada.

    Raises:
        RuntimeError: Se MATON_API_KEY não estiver configurada.
        urllib.error.HTTPError: Se o servidor retornar erro HTTP.

    Exemplo de uso:
        >>> eventos = maton_request('google-calendar', 'v1/events', method='GET')
        >>> print(eventos)
        {'items': [...]}
    """
    if not MATON_KEY:
        raise RuntimeError(
            "MATON_API_KEY não encontrada no ambiente. "
            "Configure-a antes de usar o gateway."
        )

    url = f"{GATEWAY_BASE}/{app}/{path.lstrip('/')}"

    headers = {
        "Authorization": f"Bearer {MATON_KEY}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    if extra_headers:
        headers.update(extra_headers)

    body = None
    if data is not None:
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")

    req = urllib.request.Request(url, data=body, headers=headers, method=method)

    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read().decode("utf-8")
            if not raw:
                return {}
            return json.loads(raw)
    except urllib.error.HTTPError as exc:
        error_body = ""
        try:
            error_body = exc.read().decode("utf-8", errors="replace")
        except Exception:
            pass
        logger.error(
            "HTTP %s em %s %s — corpo: %s",
            exc.code, method, url, error_body[:500],
        )
        raise
    except urllib.error.URLError as exc:
        logger.error("Erro de conexão em %s %s: %s", method, url, exc.reason)
        raise


# ---------------------------------------------------------------------------
# 2. check_connection
# ---------------------------------------------------------------------------


def check_connection(app):
    """
    Verifica se existe conexão ativa para um app no Maton.

    Parâmetros:
        app (str): Nome do app/conector (ex: 'google-calendar').

    Retorna:
        dict: {'active': bool, 'details': str}

    Exemplo de uso:
        >>> resultado = check_connection('google-calendar')
        >>> if resultado['active']:
        ...     print('Conexão OK')
        ... else:
        ...     print(resultado['details'])
    """
    if not MATON_KEY:
        return {"active": False, "details": "MATON_API_KEY não configurada."}

    url = f"{CTRL_BASE}/v1/connections?app={urllib.parse.quote(app)}"
    headers = {
        "Authorization": f"Bearer {MATON_KEY}",
        "Accept": "application/json",
    }
    req = urllib.request.Request(url, headers=headers, method="GET")

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))

        connections = data if isinstance(data, list) else data.get("connections", [])
        for conn in connections:
            status = conn.get("status", "").upper()
            if status == "ACTIVE":
                return {
                    "active": True,
                    "details": f"Conexão ativa encontrada para '{app}' (id: {conn.get('id', '?')}).",
                }

        return {
            "active": False,
            "details": f"Nenhuma conexão ativa para '{app}'. Crie uma em maton.ai.",
        }

    except urllib.error.HTTPError as exc:
        return {
            "active": False,
            "details": f"Erro HTTP {exc.code} ao verificar conexão de '{app}'.",
        }
    except Exception as exc:
        return {
            "active": False,
            "details": f"Erro ao verificar conexão de '{app}': {exc}",
        }


# ---------------------------------------------------------------------------
# 3. require_connections
# ---------------------------------------------------------------------------


def require_connections(*apps):
    """
    Verifica múltiplas conexões de uma vez. Lança exceção se alguma estiver inativa.

    Parâmetros:
        *apps (str): Nomes dos apps que precisam estar conectados.

    Raises:
        RuntimeError: Mensagem amigável listando conexões faltantes.

    Exemplo de uso:
        >>> require_connections('google-calendar', 'notion', 'gmail')
        # Se 'notion' não estiver ativa:
        # RuntimeError: Conexões faltantes: notion
        #   - notion: Nenhuma conexão ativa para 'notion'. Crie uma em maton.ai.
        # Acesse maton.ai para conectar os apps necessários.
    """
    missing = []
    details_lines = []

    for app in apps:
        result = check_connection(app)
        if not result["active"]:
            missing.append(app)
            details_lines.append(f"  - {app}: {result['details']}")

    if missing:
        msg = (
            f"Conexões faltantes: {', '.join(missing)}\n"
            + "\n".join(details_lines)
            + "\nAcesse maton.ai para conectar os apps necessários."
        )
        raise RuntimeError(msg)


# ---------------------------------------------------------------------------
# 4. retry_with_backoff
# ---------------------------------------------------------------------------


def retry_with_backoff(func=None, max_attempts=3, base_delay=1):
    """
    Wrapper de retry com exponential backoff + jitter.

    Pode ser usado como decorator (com ou sem parâmetros) ou como wrapper direto.

    Parâmetros:
        func (callable | None): Função a ser decorada. None quando usado com parâmetros.
        max_attempts (int): Número máximo de tentativas (padrão 3).
        base_delay (int | float): Delay base em segundos (padrão 1).

    Retorna:
        callable: Função decorada com retry automático.

    Exemplo de uso como decorator:
        >>> @retry_with_backoff
        ... def buscar_eventos():
        ...     return maton_request('google-calendar', 'v1/events')

        >>> @retry_with_backoff(max_attempts=5, base_delay=2)
        ... def buscar_emails():
        ...     return maton_request('gmail', 'v1/messages')

    Exemplo de uso como wrapper:
        >>> resultado = retry_with_backoff(lambda: maton_request('notion', 'v1/pages'))
    """

    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            last_exc = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return fn(*args, **kwargs)
                except Exception as exc:
                    last_exc = exc
                    if attempt == max_attempts:
                        logger.error(
                            "Falha após %d tentativas em %s: %s",
                            max_attempts, fn.__name__, exc,
                        )
                        raise
                    delay = base_delay * (2 ** (attempt - 1)) + random.uniform(0, 1)
                    logger.warning(
                        "Tentativa %d/%d de %s falhou (%s). Retry em %.1fs...",
                        attempt, max_attempts, fn.__name__, exc, delay,
                    )
                    time.sleep(delay)
            raise last_exc  # pragma: no cover
        return wrapper

    # Permite uso como @retry_with_backoff (sem parênteses)
    if func is not None and callable(func):
        return decorator(func)

    return decorator


# ---------------------------------------------------------------------------
# 5. idempotency_key
# ---------------------------------------------------------------------------


def idempotency_key(session_id, etapa, acao):
    """
    Gera hash determinístico SHA256 para deduplicação de operações.

    Parâmetros:
        session_id (str): ID da sessão atual.
        etapa (str): Nome/número da etapa do fluxo.
        acao (str): Descrição da ação específica.

    Retorna:
        str: Hash SHA256 hexadecimal de 64 caracteres.

    Exemplo de uso:
        >>> key = idempotency_key('sess_123', 'etapa_2', 'criar_pagina_notion')
        >>> print(key)
        'a3f2b8c1...'  # hash determinístico
    """
    payload = f"{session_id}:{etapa}:{acao}"
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# 6. check_idempotency / mark_idempotent
# ---------------------------------------------------------------------------


def check_idempotency(key):
    """
    Verifica se uma chave de idempotência já foi registrada.

    Lê o arquivo .session/transactions.json para determinar se a operação
    já foi executada anteriormente.

    Parâmetros:
        key (str): Chave de idempotência (gerada por idempotency_key).

    Retorna:
        bool: True se a chave já existe (operação já executada), False caso contrário.

    Exemplo de uso:
        >>> key = idempotency_key('sess_1', 'etapa_1', 'enviar_email')
        >>> if check_idempotency(key):
        ...     print('Operação já executada, pulando...')
        ... else:
        ...     enviar_email()
        ...     mark_idempotent(key)
    """
    transactions = _read_json_file(TRANSACTIONS_FILE, default=[])
    return any(t.get("key") == key for t in transactions)


def mark_idempotent(key):
    """
    Registra uma chave de idempotência como executada.

    Salva em .session/transactions.json, mantendo no máximo as últimas
    200 entradas (MAX_TRANSACTIONS) para evitar crescimento infinito.

    Parâmetros:
        key (str): Chave de idempotência a registrar.

    Exemplo de uso:
        >>> key = idempotency_key('sess_1', 'etapa_1', 'criar_pagina')
        >>> mark_idempotent(key)
        >>> check_idempotency(key)
        True
    """
    transactions = _read_json_file(TRANSACTIONS_FILE, default=[])

    # Evita duplicatas
    if any(t.get("key") == key for t in transactions):
        return

    transactions.append({
        "key": key,
        "timestamp": time.time(),
        "iso": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
    })

    # Manter apenas as últimas MAX_TRANSACTIONS entradas
    if len(transactions) > MAX_TRANSACTIONS:
        transactions = transactions[-MAX_TRANSACTIONS:]

    _write_json_file(TRANSACTIONS_FILE, transactions)


# ---------------------------------------------------------------------------
# 7. pending_sync_add / pending_sync_flush
# ---------------------------------------------------------------------------


def pending_sync_add(entry):
    """
    Adiciona uma entrada à fila de sincronização pendente.

    Usado quando o Notion (ou outro destino) falha e a operação precisa
    ser retentada depois. As entradas ficam em .session/pending_sync.json.

    Parâmetros:
        entry (dict): Dados da operação pendente. Deve conter ao menos
                      'action' e 'payload'. Um timestamp é adicionado
                      automaticamente.

    Exemplo de uso:
        >>> pending_sync_add({
        ...     'action': 'create_page',
        ...     'payload': {'title': 'Reunião semanal', 'content': '...'},
        ...     'target': 'notion',
        ... })
    """
    if not isinstance(entry, dict):
        raise ValueError("entry deve ser um dict.")

    entry.setdefault("timestamp", time.time())
    entry.setdefault("iso", time.strftime("%Y-%m-%dT%H:%M:%S%z"))

    pending = _read_json_file(PENDING_SYNC_FILE, default=[])
    pending.append(entry)
    _write_json_file(PENDING_SYNC_FILE, pending)
    logger.info("Entrada adicionada à fila de sync pendente (%d total).", len(pending))


def pending_sync_flush(notion_page_id):
    """
    Processa e remove entradas pendentes destinadas a uma página Notion específica.

    Tenta reenviar cada entrada pendente via maton_request. Entradas que
    falharem novamente permanecem na fila. Entradas processadas com
    sucesso são removidas.

    Parâmetros:
        notion_page_id (str): ID da página Notion de destino.

    Retorna:
        dict: {
            'processed': int,   — quantidade processada com sucesso
            'failed': int,      — quantidade que falhou novamente
            'remaining': int,   — total restante na fila
        }

    Exemplo de uso:
        >>> result = pending_sync_flush('abc-123-def')
        >>> print(result)
        {'processed': 3, 'failed': 1, 'remaining': 1}
    """
    pending = _read_json_file(PENDING_SYNC_FILE, default=[])

    if not pending:
        return {"processed": 0, "failed": 0, "remaining": 0}

    # Separar entradas relacionadas a esta page_id e as demais
    target_entries = []
    other_entries = []
    for entry in pending:
        page = (
            entry.get("notion_page_id")
            or entry.get("payload", {}).get("page_id")
            or entry.get("payload", {}).get("parent", {}).get("page_id")
        )
        if page == notion_page_id:
            target_entries.append(entry)
        else:
            other_entries.append(entry)

    processed = 0
    still_failed = []

    for entry in target_entries:
        action = entry.get("action", "")
        payload = entry.get("payload", {})

        try:
            if action == "create_page":
                maton_request("notion", "v1/pages", method="POST", data=payload)
            elif action == "update_page":
                page_id = payload.pop("page_id", notion_page_id)
                maton_request(
                    "notion", f"v1/pages/{page_id}", method="PATCH", data=payload
                )
            elif action == "append_blocks":
                maton_request(
                    "notion",
                    f"v1/blocks/{notion_page_id}/children",
                    method="PATCH",
                    data=payload,
                )
            else:
                # Ação genérica — tenta POST
                maton_request("notion", "v1/pages", method="POST", data=payload)

            processed += 1

        except Exception as exc:
            logger.warning("Flush falhou para entrada '%s': %s", action, exc)
            entry["last_error"] = str(exc)
            entry["last_retry"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
            still_failed.append(entry)

    remaining = other_entries + still_failed
    _write_json_file(PENDING_SYNC_FILE, remaining)

    return {
        "processed": processed,
        "failed": len(still_failed),
        "remaining": len(remaining),
    }
