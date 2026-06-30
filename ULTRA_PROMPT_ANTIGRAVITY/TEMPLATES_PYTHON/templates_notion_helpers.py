"""
Ultra Prompt v6.1 — Helper centralizado para TODAS as operacoes Notion.

Modulo unificado que substitui notion_update.py com funcionalidades avancadas:
- CRUD completo de paginas e blocos
- Sessoes estruturadas com template de 10 secoes
- WAL (Write-Ahead Log) idempotente
- Tabelas de decisoes e outputs
- Retry automatico em falhas transientes
- Paginacao transparente
- Validacao de inputs

Dependencias: apenas stdlib (urllib, json, os, time, uuid).
Auth: Bearer {MATON_API_KEY} do environment.
API: https://gateway.maton.ai/notion/v1/ (Notion-Version: 2022-06-28)
"""

import urllib.request
import urllib.error
import os
import json
import time
import uuid
from datetime import datetime, timezone


# ============================================================
# CONFIGURACAO
# ============================================================

MATON_KEY = os.environ.get('MATON_API_KEY', '')
NOTION_BASE = 'https://gateway.maton.ai/notion/v1'
NOTION_VERSION = '2022-06-28'

_MAX_BLOCKS_PER_REQUEST = 100
_MAX_RETRIES = 3
_RETRY_BACKOFF_BASE = 1.5  # segundos


# ============================================================
# CAMADA DE TRANSPORTE (com retry)
# ============================================================

def _notion_request(path, method='GET', data=None, retries=_MAX_RETRIES):
    """
    Request base para Notion API com retry em falhas transientes.

    Falhas transientes (429, 502, 503, 504) sao retentadas com backoff exponencial.
    Erros 4xx (exceto 429) sao levantados imediatamente.

    Args:
        path: Caminho relativo da API (ex: 'pages', 'blocks/abc/children').
        method: Metodo HTTP.
        data: Payload dict (sera serializado como JSON).
        retries: Numero maximo de tentativas.

    Returns:
        dict: Resposta JSON da API.

    Raises:
        urllib.error.HTTPError: Em erros nao-transientes.
        RuntimeError: Quando todas as tentativas falham.
    """
    if not MATON_KEY:
        raise RuntimeError('MATON_API_KEY nao configurada no environment.')

    url = f'{NOTION_BASE}/{path}'
    encoded = json.dumps(data).encode('utf-8') if data else None

    last_error = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, data=encoded, method=method)
            req.add_header('Authorization', f'Bearer {MATON_KEY}')
            req.add_header('Notion-Version', NOTION_VERSION)
            if data:
                req.add_header('Content-Type', 'application/json')
            resp = urllib.request.urlopen(req)
            body = resp.read().decode('utf-8')
            return json.loads(body) if body.strip() else {}
        except urllib.error.HTTPError as e:
            last_error = e
            if e.code in (429, 502, 503, 504):
                wait = _RETRY_BACKOFF_BASE ** (attempt + 1)
                # Respeitar Retry-After se presente (429)
                retry_after = e.headers.get('Retry-After')
                if retry_after:
                    try:
                        wait = max(wait, float(retry_after))
                    except ValueError:
                        pass
                time.sleep(wait)
                continue
            raise
        except (urllib.error.URLError, OSError) as e:
            last_error = e
            if attempt < retries - 1:
                time.sleep(_RETRY_BACKOFF_BASE ** (attempt + 1))
                continue
            raise

    raise RuntimeError(
        f'Notion API: todas as {retries} tentativas falharam. Ultimo erro: {last_error}'
    )


# ============================================================
# VALIDACAO
# ============================================================

def _validate_id(value, name='id'):
    """Valida que um ID Notion foi fornecido e nao esta vazio."""
    if not value or not isinstance(value, str) or not value.strip():
        raise ValueError(f'{name} e obrigatorio e deve ser uma string nao-vazia.')
    return value.strip()


def _validate_blocks(blocks, name='blocks'):
    """Valida que blocks e uma lista nao-vazia de dicts."""
    if not isinstance(blocks, list):
        raise TypeError(f'{name} deve ser uma lista de blocos.')
    if not blocks:
        raise ValueError(f'{name} nao pode ser uma lista vazia.')
    return blocks


# ============================================================
# BLOCK HELPERS
# ============================================================

def paragraph_block(text, bold=False, italic=False, color='default'):
    """
    Cria bloco de paragrafo.

    Args:
        text: Conteudo do paragrafo.
        bold: Se True, texto em negrito.
        italic: Se True, texto em italico.
        color: Cor do texto (default, gray, brown, orange, etc.).

    Returns:
        dict: Bloco paragraph do Notion.
    """
    annotations = {}
    if bold:
        annotations['bold'] = True
    if italic:
        annotations['italic'] = True
    if color != 'default':
        annotations['color'] = color

    rt = {'text': {'content': str(text)}}
    if annotations:
        rt['annotations'] = annotations

    return {
        'object': 'block',
        'type': 'paragraph',
        'paragraph': {'rich_text': [rt]}
    }


def heading_block(text, level=2):
    """
    Cria bloco de heading.

    Args:
        text: Conteudo do heading.
        level: Nivel do heading (1, 2 ou 3).

    Returns:
        dict: Bloco heading do Notion.
    """
    if level not in (1, 2, 3):
        raise ValueError('Nivel de heading deve ser 1, 2 ou 3.')
    key = f'heading_{level}'
    return {
        'object': 'block',
        'type': key,
        key: {'rich_text': [{'text': {'content': str(text)}}]}
    }


def list_block(text, ordered=False):
    """
    Cria bloco de lista (bullet ou numerada).

    Args:
        text: Conteudo do item.
        ordered: Se True, lista numerada. Se False, bullet.

    Returns:
        dict: Bloco de lista do Notion.
    """
    if ordered:
        block_type = 'numbered_list_item'
    else:
        block_type = 'bulleted_list_item'
    return {
        'object': 'block',
        'type': block_type,
        block_type: {'rich_text': [{'text': {'content': str(text)}}]}
    }


def toggle_block(text, children=None):
    """
    Cria bloco toggle (colapsavel).

    Args:
        text: Titulo do toggle.
        children: (Opcional) Lista de blocos filhos dentro do toggle.

    Returns:
        dict: Bloco toggle do Notion.
    """
    block = {
        'object': 'block',
        'type': 'toggle',
        'toggle': {'rich_text': [{'text': {'content': str(text)}}]}
    }
    if children:
        block['toggle']['children'] = children
    return block


def callout_block(text, emoji='💡'):
    """
    Cria bloco callout com icone emoji.

    Args:
        text: Conteudo do callout.
        emoji: Emoji do icone (padrao: lampada).

    Returns:
        dict: Bloco callout do Notion.
    """
    return {
        'object': 'block',
        'type': 'callout',
        'callout': {
            'rich_text': [{'text': {'content': str(text)}}],
            'icon': {'emoji': emoji}
        }
    }


def divider_block():
    """Cria bloco divisor horizontal."""
    return {'object': 'block', 'type': 'divider', 'divider': {}}


def code_block(code, language='python'):
    """
    Cria bloco de codigo.

    Args:
        code: Conteudo do codigo.
        language: Linguagem para syntax highlighting.

    Returns:
        dict: Bloco code do Notion.
    """
    return {
        'object': 'block',
        'type': 'code',
        'code': {
            'rich_text': [{'text': {'content': str(code)}}],
            'language': language
        }
    }


def table_block(rows, has_header=True):
    """
    Cria bloco de tabela.

    Args:
        rows: Lista de listas (cada sub-lista e uma linha da tabela).
        has_header: Se True, primeira linha e tratada como cabecalho.

    Returns:
        dict: Bloco table do Notion.

    Raises:
        ValueError: Se rows estiver vazio.
    """
    if not rows:
        raise ValueError('Tabela deve ter pelo menos uma linha.')

    table_width = len(rows[0])
    table_rows = []
    for row in rows:
        cells = [[{'text': {'content': str(cell)}}] for cell in row]
        # Preencher celulas faltantes para manter largura consistente
        while len(cells) < table_width:
            cells.append([{'text': {'content': ''}}])
        table_rows.append({
            'object': 'block',
            'type': 'table_row',
            'table_row': {'cells': cells}
        })

    return {
        'object': 'block',
        'type': 'table',
        'table': {
            'table_width': table_width,
            'has_column_header': has_header,
            'has_row_header': False,
            'children': table_rows
        }
    }


# ============================================================
# OPERACOES CRUD — PAGINAS
# ============================================================

def notion_create_page(parent_id, title, children_blocks=None):
    """
    Cria uma pagina no Notion.

    Suporta tanto parent do tipo page quanto database.
    Se children_blocks ultrapassar 100 itens, faz append posterior.

    Args:
        parent_id: ID da pagina ou database pai.
        title: Titulo da nova pagina.
        children_blocks: (Opcional) Lista de blocos de conteudo inicial.

    Returns:
        str: ID da pagina criada.

    Raises:
        ValueError: Se parent_id ou title forem invalidos.
    """
    parent_id = _validate_id(parent_id, 'parent_id')
    if not title or not isinstance(title, str):
        raise ValueError('title e obrigatorio e deve ser uma string nao-vazia.')

    # Determinar tipo de parent (page ou database)
    # Notion IDs com hifens tem 36 chars; sem hifens, 32
    data = {
        'parent': {'type': 'page_id', 'page_id': parent_id},
        'properties': {
            'title': [{'text': {'content': title}}]
        }
    }

    # Respeitar limite de 100 blocos na criacao
    initial_blocks = []
    overflow_blocks = []
    if children_blocks:
        _validate_blocks(children_blocks, 'children_blocks')
        initial_blocks = children_blocks[:_MAX_BLOCKS_PER_REQUEST]
        overflow_blocks = children_blocks[_MAX_BLOCKS_PER_REQUEST:]

    if initial_blocks:
        data['children'] = initial_blocks

    result = _notion_request('pages', 'POST', data)
    page_id = result['id']

    # Append blocos excedentes em lotes
    if overflow_blocks:
        notion_append_blocks(page_id, overflow_blocks)

    return page_id


def notion_read_page(page_id, include_children=True):
    """
    Leitura completa de uma pagina Notion com paginacao automatica.

    Args:
        page_id: ID da pagina.
        include_children: Se True, inclui todos os blocos filhos (com paginacao).

    Returns:
        dict: Dicionario com 'metadata' (propriedades da pagina) e
              'children' (lista de blocos, se solicitado).
    """
    page_id = _validate_id(page_id, 'page_id')

    metadata = _notion_request(f'pages/{page_id}')
    result = {'metadata': metadata, 'children': []}

    if include_children:
        all_blocks = []
        has_more = True
        start_cursor = None

        while has_more:
            path = f'blocks/{page_id}/children?page_size=100'
            if start_cursor:
                path += f'&start_cursor={start_cursor}'
            resp = _notion_request(path)
            all_blocks.extend(resp.get('results', []))
            has_more = resp.get('has_more', False)
            start_cursor = resp.get('next_cursor')

        result['children'] = all_blocks

    return result


def notion_update_page(page_id, properties):
    """
    Update atomico de propriedades de uma pagina.

    Atualiza apenas as propriedades fornecidas sem afetar as demais.

    Args:
        page_id: ID da pagina.
        properties: Dict de propriedades Notion a atualizar.
                    Ex: {'title': [{'text': {'content': 'Novo Titulo'}}]}

    Returns:
        dict: Resposta da API com pagina atualizada.

    Raises:
        ValueError: Se page_id ou properties forem invalidos.
        TypeError: Se properties nao for dict.
    """
    page_id = _validate_id(page_id, 'page_id')
    if not isinstance(properties, dict):
        raise TypeError('properties deve ser um dict.')
    if not properties:
        raise ValueError('properties nao pode ser vazio.')

    data = {'properties': properties}
    return _notion_request(f'pages/{page_id}', 'PATCH', data)


# ============================================================
# OPERACOES CRUD — BLOCOS
# ============================================================

def notion_append_blocks(page_id, blocks):
    """
    Append de blocos com tratamento automatico do limite de 100 por request.

    Divide a lista em lotes de ate 100 blocos e envia sequencialmente.

    Args:
        page_id: ID da pagina ou bloco pai.
        blocks: Lista de blocos Notion a adicionar.

    Returns:
        list: Lista de respostas da API (uma por lote).

    Raises:
        ValueError: Se page_id ou blocks forem invalidos.
    """
    page_id = _validate_id(page_id, 'page_id')
    _validate_blocks(blocks, 'blocks')

    responses = []
    for i in range(0, len(blocks), _MAX_BLOCKS_PER_REQUEST):
        batch = blocks[i:i + _MAX_BLOCKS_PER_REQUEST]
        data = {'children': batch}
        resp = _notion_request(f'blocks/{page_id}/children', 'PATCH', data)
        responses.append(resp)

    return responses


# ============================================================
# SESSAO ESTRUTURADA
# ============================================================

def _build_session_template(session_id, tipo_tarefa, version):
    """
    Constroi template estruturado de 10 secoes para uma sessao.

    Secoes: METADADOS, OBJETIVO, CONTEXTO, PLANO, WAL, DECISOES,
    OUTPUTS, LINKS, APRENDIZADOS, RESUMO.

    Args:
        session_id: Identificador unico da sessao.
        tipo_tarefa: Tipo da tarefa (ex: 'pesquisa', 'automacao').
        version: Versao do Ultra Prompt.

    Returns:
        list: Lista de blocos Notion formatados.
    """
    now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')

    blocks = [
        # 1. METADADOS
        heading_block('1. METADADOS', level=1),
        callout_block(
            f'Session: {session_id}\n'
            f'Versao: {version}\n'
            f'Tipo: {tipo_tarefa}\n'
            f'Inicio: {now}\n'
            f'Status: EM_ANDAMENTO',
            '📋'
        ),
        divider_block(),

        # 2. OBJETIVO
        heading_block('2. OBJETIVO', level=1),
        paragraph_block('(Descreva o objetivo principal da tarefa aqui)'),
        divider_block(),

        # 3. CONTEXTO
        heading_block('3. CONTEXTO', level=1),
        paragraph_block('(Informacoes de contexto relevantes para a tarefa)'),
        divider_block(),

        # 4. PLANO
        heading_block('4. PLANO', level=1),
        table_block([
            ['#', 'Etapa', 'Descricao', 'Status'],
        ]),
        divider_block(),

        # 5. WAL (Write-Ahead Log)
        heading_block('5. WAL (Write-Ahead Log)', level=1),
        callout_block('Log de execucao com idempotencia via transaction_id.', '📝'),
        table_block([
            ['TX_ID', 'Timestamp', 'Acao', 'Resultado', 'Duracao'],
        ]),
        divider_block(),

        # 6. DECISOES
        heading_block('6. DECISOES', level=1),
        table_block([
            ['#', 'Decisao', 'Razao', 'Alternativas', 'Impacto'],
        ]),
        divider_block(),

        # 7. OUTPUTS
        heading_block('7. OUTPUTS', level=1),
        table_block([
            ['#', 'Tipo', 'Descricao', 'Caminho/Link', 'Status'],
        ]),
        divider_block(),

        # 8. LINKS
        heading_block('8. LINKS', level=1),
        paragraph_block('(Referencias, URLs e recursos utilizados)'),
        divider_block(),

        # 9. APRENDIZADOS
        heading_block('9. APRENDIZADOS', level=1),
        paragraph_block('(Preenchido ao finalizar a sessao)'),
        divider_block(),

        # 10. RESUMO
        heading_block('10. RESUMO', level=1),
        paragraph_block('(Preenchido ao finalizar a sessao)'),
    ]

    return blocks


def notion_create_session_page(workspace_id, session_id, tipo_tarefa, version='6.1.0'):
    """
    Cria pagina de sessao com template estruturado de 10 secoes.

    Secoes criadas: METADADOS, OBJETIVO, CONTEXTO, PLANO, WAL,
    DECISOES, OUTPUTS, LINKS, APRENDIZADOS, RESUMO.

    Args:
        workspace_id: ID da pagina pai (workspace) no Notion.
        session_id: Identificador unico da sessao (ex: '2026-04-17-pesquisa-001').
        tipo_tarefa: Tipo da tarefa (ex: 'pesquisa', 'automacao', 'integracao').
        version: Versao do Ultra Prompt (padrao: '6.1.0').

    Returns:
        str: ID da pagina de sessao criada.
    """
    workspace_id = _validate_id(workspace_id, 'workspace_id')
    if not session_id:
        raise ValueError('session_id e obrigatorio.')

    title = f'Sessao: {session_id} [{tipo_tarefa}]'
    template_blocks = _build_session_template(session_id, tipo_tarefa, version)

    return notion_create_page(workspace_id, title, template_blocks)


# ============================================================
# OPERACOES DE SESSAO
# ============================================================

# Cache local de transaction_ids processados para garantir idempotencia
_processed_transactions = set()


def notion_append_wal_entry(page_id, entry_dict):
    """
    Append ao WAL (Write-Ahead Log) da sessao, idempotente via transaction_id.

    Se a entry_dict nao tiver 'transaction_id', um UUID4 e gerado automaticamente.
    Entradas com transaction_id ja processado sao ignoradas (idempotencia).

    Args:
        page_id: ID da pagina de sessao.
        entry_dict: Dicionario com campos da entrada WAL.
            Campos esperados:
            - transaction_id (str, opcional): ID unico da transacao.
            - acao (str): Descricao da acao executada.
            - resultado (str): Resultado da acao ('OK', 'ERRO', etc.).
            - duracao (str, opcional): Tempo de execucao.

    Returns:
        dict | None: Resposta da API ou None se transacao duplicada.

    Raises:
        ValueError: Se campos obrigatorios estiverem ausentes.
    """
    page_id = _validate_id(page_id, 'page_id')
    if not isinstance(entry_dict, dict):
        raise TypeError('entry_dict deve ser um dict.')

    tx_id = entry_dict.get('transaction_id', str(uuid.uuid4()))
    if tx_id in _processed_transactions:
        return None  # Idempotencia: ja processado

    acao = entry_dict.get('acao', '')
    if not acao:
        raise ValueError("Campo 'acao' e obrigatorio no entry_dict.")

    resultado = entry_dict.get('resultado', '-')
    duracao = entry_dict.get('duracao', '-')
    timestamp = datetime.now(timezone.utc).strftime('%H:%M:%S')

    row_block = {
        'object': 'block',
        'type': 'table_row',
        'table_row': {
            'cells': [
                [{'text': {'content': tx_id[:8]}}],
                [{'text': {'content': timestamp}}],
                [{'text': {'content': str(acao)}}],
                [{'text': {'content': str(resultado)}}],
                [{'text': {'content': str(duracao)}}],
            ]
        }
    }

    # Encontrar o bloco da tabela WAL e fazer append
    # Estrategia: buscar blocos, localizar tabela WAL pelo heading anterior
    children = _get_all_children(page_id)
    wal_table_id = _find_table_after_heading(children, '5. WAL')

    if wal_table_id:
        resp = _notion_request(
            f'blocks/{wal_table_id}/children', 'PATCH',
            {'children': [row_block]}
        )
    else:
        # Fallback: append como lista ao final (nao ideal, mas seguro)
        resp = notion_append_blocks(page_id, [
            callout_block(f'WAL [{tx_id[:8]}] {timestamp}: {acao} -> {resultado}', '📝')
        ])

    _processed_transactions.add(tx_id)
    return resp


def notion_append_decision(page_id, decision_row):
    """
    Append a tabela de decisoes da sessao.

    Args:
        page_id: ID da pagina de sessao.
        decision_row: Dict com campos da decisao.
            Campos esperados:
            - numero (str|int): Numero sequencial.
            - decisao (str): Descricao da decisao.
            - razao (str): Justificativa.
            - alternativas (str, opcional): Alternativas consideradas.
            - impacto (str, opcional): Nivel de impacto.

    Returns:
        dict: Resposta da API.

    Raises:
        ValueError: Se campos obrigatorios estiverem ausentes.
    """
    page_id = _validate_id(page_id, 'page_id')
    if not isinstance(decision_row, dict):
        raise TypeError('decision_row deve ser um dict.')

    numero = str(decision_row.get('numero', '?'))
    decisao = decision_row.get('decisao', '')
    if not decisao:
        raise ValueError("Campo 'decisao' e obrigatorio.")

    razao = decision_row.get('razao', '-')
    alternativas = decision_row.get('alternativas', '-')
    impacto = decision_row.get('impacto', '-')

    row_block = {
        'object': 'block',
        'type': 'table_row',
        'table_row': {
            'cells': [
                [{'text': {'content': numero}}],
                [{'text': {'content': str(decisao)}}],
                [{'text': {'content': str(razao)}}],
                [{'text': {'content': str(alternativas)}}],
                [{'text': {'content': str(impacto)}}],
            ]
        }
    }

    children = _get_all_children(page_id)
    table_id = _find_table_after_heading(children, '6. DECISOES')

    if table_id:
        return _notion_request(
            f'blocks/{table_id}/children', 'PATCH',
            {'children': [row_block]}
        )

    # Fallback: append como callout
    return notion_append_blocks(page_id, [
        callout_block(f'DECISAO #{numero}: {decisao} (Razao: {razao})', '⚖️')
    ])[0]


def notion_append_output(page_id, output_row):
    """
    Append a tabela de outputs da sessao.

    Args:
        page_id: ID da pagina de sessao.
        output_row: Dict com campos do output.
            Campos esperados:
            - numero (str|int): Numero sequencial.
            - tipo (str): Tipo do output (arquivo, link, mensagem, etc.).
            - descricao (str): Descricao do output.
            - caminho (str, opcional): Caminho ou link do output.
            - status (str, opcional): Status (ENTREGUE, PENDENTE, etc.).

    Returns:
        dict: Resposta da API.

    Raises:
        ValueError: Se campos obrigatorios estiverem ausentes.
    """
    page_id = _validate_id(page_id, 'page_id')
    if not isinstance(output_row, dict):
        raise TypeError('output_row deve ser um dict.')

    numero = str(output_row.get('numero', '?'))
    tipo = output_row.get('tipo', '')
    if not tipo:
        raise ValueError("Campo 'tipo' e obrigatorio.")

    descricao = output_row.get('descricao', '-')
    caminho = output_row.get('caminho', '-')
    status = output_row.get('status', 'PENDENTE')

    row_block = {
        'object': 'block',
        'type': 'table_row',
        'table_row': {
            'cells': [
                [{'text': {'content': numero}}],
                [{'text': {'content': str(tipo)}}],
                [{'text': {'content': str(descricao)}}],
                [{'text': {'content': str(caminho)}}],
                [{'text': {'content': str(status)}}],
            ]
        }
    }

    children = _get_all_children(page_id)
    table_id = _find_table_after_heading(children, '7. OUTPUTS')

    if table_id:
        return _notion_request(
            f'blocks/{table_id}/children', 'PATCH',
            {'children': [row_block]}
        )

    # Fallback
    return notion_append_blocks(page_id, [
        callout_block(f'OUTPUT #{numero}: [{tipo}] {descricao} -> {caminho} ({status})', '📦')
    ])[0]


def notion_finalize_session(page_id, aprendizados, resumo):
    """
    Finaliza uma sessao, preenchendo secoes APRENDIZADOS e RESUMO.

    Tambem atualiza o status nos METADADOS para FINALIZADO.

    Args:
        page_id: ID da pagina de sessao.
        aprendizados: Lista de strings com aprendizados da sessao.
        resumo: String com resumo final da sessao.

    Returns:
        dict: Dicionario com chaves 'aprendizados_resp' e 'resumo_resp'.

    Raises:
        ValueError: Se aprendizados ou resumo forem invalidos.
    """
    page_id = _validate_id(page_id, 'page_id')
    if not isinstance(aprendizados, list) or not aprendizados:
        raise ValueError('aprendizados deve ser uma lista nao-vazia de strings.')
    if not resumo or not isinstance(resumo, str):
        raise ValueError('resumo deve ser uma string nao-vazia.')

    children = _get_all_children(page_id)

    # --- Aprendizados ---
    aprendizados_blocks = []
    for item in aprendizados:
        aprendizados_blocks.append(list_block(str(item), ordered=False))

    aprendizados_placeholder_id = _find_paragraph_after_heading(
        children, '9. APRENDIZADOS'
    )
    if aprendizados_placeholder_id:
        # Deletar placeholder e adicionar conteudo real
        try:
            _notion_request(f'blocks/{aprendizados_placeholder_id}', 'DELETE')
        except Exception:
            pass  # Nao falhar se placeholder ja foi removido

    # Encontrar o heading de APRENDIZADOS para append abaixo
    aprendizados_heading_id = _find_heading_block_id(children, '9. APRENDIZADOS')
    if aprendizados_heading_id:
        aprend_resp = _notion_request(
            f'blocks/{aprendizados_heading_id}/children', 'PATCH',
            {'children': aprendizados_blocks}
        )
    else:
        aprend_resp = notion_append_blocks(page_id, [
            heading_block('9. APRENDIZADOS', level=1),
            *aprendizados_blocks
        ])

    # --- Resumo ---
    resumo_blocks = [paragraph_block(resumo)]

    resumo_placeholder_id = _find_paragraph_after_heading(
        children, '10. RESUMO'
    )
    if resumo_placeholder_id:
        try:
            _notion_request(f'blocks/{resumo_placeholder_id}', 'DELETE')
        except Exception:
            pass

    resumo_heading_id = _find_heading_block_id(children, '10. RESUMO')
    if resumo_heading_id:
        resumo_resp = _notion_request(
            f'blocks/{resumo_heading_id}/children', 'PATCH',
            {'children': resumo_blocks}
        )
    else:
        resumo_resp = notion_append_blocks(page_id, [
            heading_block('10. RESUMO', level=1),
            *resumo_blocks
        ])

    # --- Atualizar status nos metadados (append callout de finalizacao) ---
    now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
    notion_append_blocks(page_id, [
        divider_block(),
        callout_block(f'SESSAO FINALIZADA em {now}', '✅'),
    ])

    return {
        'aprendizados_resp': aprend_resp,
        'resumo_resp': resumo_resp,
    }


# ============================================================
# FUNCOES AUXILIARES INTERNAS
# ============================================================

def _get_all_children(page_id):
    """
    Le todos os blocos filhos de uma pagina com paginacao automatica.

    Args:
        page_id: ID da pagina.

    Returns:
        list: Lista completa de blocos filhos.
    """
    all_blocks = []
    has_more = True
    start_cursor = None

    while has_more:
        path = f'blocks/{page_id}/children?page_size=100'
        if start_cursor:
            path += f'&start_cursor={start_cursor}'
        resp = _notion_request(path)
        all_blocks.extend(resp.get('results', []))
        has_more = resp.get('has_more', False)
        start_cursor = resp.get('next_cursor')

    return all_blocks


def _extract_block_text(block):
    """Extrai texto plano de um bloco Notion."""
    block_type = block.get('type', '')
    content = block.get(block_type, {})
    rich_text = content.get('rich_text', [])
    return ''.join(rt.get('plain_text', '') for rt in rich_text)


def _find_table_after_heading(blocks, heading_prefix):
    """
    Encontra o ID da primeira tabela que aparece apos um heading especifico.

    Args:
        blocks: Lista de blocos da pagina.
        heading_prefix: Prefixo do texto do heading a buscar.

    Returns:
        str | None: ID da tabela encontrada ou None.
    """
    found_heading = False
    for block in blocks:
        block_type = block.get('type', '')
        text = _extract_block_text(block)

        if block_type.startswith('heading') and text.startswith(heading_prefix):
            found_heading = True
            continue

        if found_heading and block_type == 'table':
            return block.get('id')

        # Se encontrou outro heading, parar a busca
        if found_heading and block_type.startswith('heading'):
            break

    return None


def _find_paragraph_after_heading(blocks, heading_prefix):
    """
    Encontra o ID do primeiro paragrafo apos um heading especifico.

    Usado para localizar placeholders a serem substituidos.

    Args:
        blocks: Lista de blocos da pagina.
        heading_prefix: Prefixo do texto do heading a buscar.

    Returns:
        str | None: ID do paragrafo encontrado ou None.
    """
    found_heading = False
    for block in blocks:
        block_type = block.get('type', '')
        text = _extract_block_text(block)

        if block_type.startswith('heading') and text.startswith(heading_prefix):
            found_heading = True
            continue

        if found_heading and block_type == 'paragraph':
            return block.get('id')

        if found_heading and block_type.startswith('heading'):
            break

    return None


def _find_heading_block_id(blocks, heading_prefix):
    """
    Encontra o ID de um bloco heading pelo prefixo do texto.

    Args:
        blocks: Lista de blocos da pagina.
        heading_prefix: Prefixo do texto do heading.

    Returns:
        str | None: ID do heading ou None.
    """
    for block in blocks:
        block_type = block.get('type', '')
        if block_type.startswith('heading'):
            text = _extract_block_text(block)
            if text.startswith(heading_prefix):
                return block.get('id')
    return None


def extract_text_from_blocks(blocks):
    """
    Extrai texto puro de uma lista de blocos Notion.

    Args:
        blocks: Lista de blocos Notion.

    Returns:
        str: Texto concatenado com quebras de linha.
    """
    return '\n'.join(_extract_block_text(b) for b in blocks if _extract_block_text(b))


# ============================================================
# BUSCA
# ============================================================

def notion_search(query='', page_size=10):
    """
    Busca paginas no Notion.

    Args:
        query: Texto de busca.
        page_size: Numero maximo de resultados.

    Returns:
        dict: Resposta da API com resultados da busca.
    """
    data = {'query': query, 'page_size': page_size}
    return _notion_request('search', 'POST', data)


# ============================================================
# EXEMPLO DE USO
# ============================================================

if __name__ == '__main__':
    WORKSPACE_ID = 'SEU_WORKSPACE_ID'

    # Criar sessao estruturada
    session_page_id = notion_create_session_page(
        workspace_id=WORKSPACE_ID,
        session_id='2026-04-17-pesquisa-001',
        tipo_tarefa='pesquisa'
    )
    print(f'Sessao criada: {session_page_id}')

    # Adicionar entrada WAL
    notion_append_wal_entry(session_page_id, {
        'acao': 'Inicio da pesquisa de mercado',
        'resultado': 'OK',
        'duracao': '0.5s'
    })
    print('WAL entry adicionada.')

    # Registrar decisao
    notion_append_decision(session_page_id, {
        'numero': 1,
        'decisao': 'Usar API publica para coleta',
        'razao': 'Gratuita e bem documentada',
        'alternativas': 'Web scraping',
        'impacto': 'MEDIO'
    })
    print('Decisao registrada.')

    # Registrar output
    notion_append_output(session_page_id, {
        'numero': 1,
        'tipo': 'arquivo',
        'descricao': 'Relatorio de mercado em PDF',
        'caminho': '/outputs/relatorio_mercado.pdf',
        'status': 'ENTREGUE'
    })
    print('Output registrado.')

    # Finalizar sessao
    notion_finalize_session(
        session_page_id,
        aprendizados=[
            'API X tem rate limit de 100 req/min',
            'Formato CSV mais eficiente que JSON para este caso',
            'Retry com backoff essencial para estabilidade'
        ],
        resumo='Pesquisa de mercado concluida com sucesso. '
               '3 fontes analisadas, relatorio gerado em PDF.'
    )
    print('Sessao finalizada.')

    # Leitura completa
    page_data = notion_read_page(session_page_id)
    text = extract_text_from_blocks(page_data['children'])
    print(f'Conteudo:\n{text}')
