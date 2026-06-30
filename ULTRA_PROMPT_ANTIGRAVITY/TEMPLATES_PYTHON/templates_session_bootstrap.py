"""
Ultra Prompt v6.1 — Template: Bootstrap de Sessao
Centraliza TODA a logica de criacao, importacao e gestao de sessoes.
Chamado pelo core.md na Etapa 6 do bootstrap.

Uso: importar funcoes ou executar via exec() no runtime do agente.
"""

# Imports dos helpers (carregados via exec/import no runtime)
# Em runtime, maton_helpers, notion_helpers, drive_helpers ja estao disponiveis

import urllib.request
import urllib.parse
import os
import json
import datetime
import hashlib

# ============================================================
# CONSTANTES
# ============================================================

MATON_KEY = os.environ.get('MATON_API_KEY', '')
DRIVE_BASE = 'https://gateway.maton.ai/google-drive'
NOTION_BASE = 'https://gateway.maton.ai/notion/v1'
MATON_CTRL = 'https://ctrl.maton.ai'
NOTION_VERSION = '2022-06-28'
SESSION_LOCAL_ROOT = '/home/vercel-sandbox/.session'

# Limite estimado de tokens do contexto (usado na heuristica de compaction)
ESTIMATED_CONTEXT_LIMIT = 180000
COMPACTION_THRESHOLD = 0.80  # 80%

# Template das 10 secoes canonicas da pagina Notion
NOTION_SESSION_SECTIONS = [
    'METADADOS',
    'OBJETIVO',
    'CONTEXTO',
    'PLANO',
    'WAL',
    'DECISOES',
    'OUTPUTS',
    'LINKS',
    'APRENDIZADOS',
    'RESUMO',
]


# ============================================================
# HELPERS INTERNOS (urllib direto, sem dependencia externa)
# ============================================================

def _drive_request(path, method='GET', data=None, content_type='application/json'):
    """Requisicao generica para Google Drive via Maton Gateway."""
    url = f'{DRIVE_BASE}/{path}'
    encoded = json.dumps(data).encode('utf-8') if data and isinstance(data, dict) else data
    req = urllib.request.Request(url, data=encoded, method=method)
    req.add_header('Authorization', f'Bearer {MATON_KEY}')
    if content_type:
        req.add_header('Content-Type', content_type)
    return json.load(urllib.request.urlopen(req))


def _notion_request(path, method='GET', data=None):
    """Requisicao generica para Notion via Maton Gateway."""
    url = f'{NOTION_BASE}/{path}'
    encoded = json.dumps(data).encode('utf-8') if data else None
    req = urllib.request.Request(url, data=encoded, method=method)
    req.add_header('Authorization', f'Bearer {MATON_KEY}')
    req.add_header('Notion-Version', NOTION_VERSION)
    if data:
        req.add_header('Content-Type', 'application/json')
    return json.load(urllib.request.urlopen(req))


def _maton_ctrl_request(path, method='GET'):
    """Requisicao para Maton Control API."""
    url = f'{MATON_CTRL}/{path}'
    req = urllib.request.Request(url, method=method)
    req.add_header('Authorization', f'Bearer {MATON_KEY}')
    return json.load(urllib.request.urlopen(req))


def _drive_upload_text(content, filename, folder_id, mime_type='text/markdown'):
    """Upload de conteudo de texto direto para o Drive (multipart)."""
    metadata = {'name': filename}
    if folder_id:
        metadata['parents'] = [folder_id]
    metadata_json = json.dumps(metadata).encode('utf-8')
    file_bytes = content.encode('utf-8')

    boundary = '----UltraPromptV6SessionBoundary'
    body = b''
    body += f'--{boundary}\r\n'.encode()
    body += b'Content-Type: application/json; charset=UTF-8\r\n\r\n'
    body += metadata_json + b'\r\n'
    body += f'--{boundary}\r\n'.encode()
    body += f'Content-Type: {mime_type}\r\n\r\n'.encode()
    body += file_bytes + b'\r\n'
    body += f'--{boundary}--'.encode()

    url = f'{DRIVE_BASE}/upload/drive/v3/files?uploadType=multipart'
    req = urllib.request.Request(url, data=body, method='POST')
    req.add_header('Authorization', f'Bearer {MATON_KEY}')
    req.add_header('Content-Type', f'multipart/related; boundary={boundary}')
    return json.load(urllib.request.urlopen(req))


def _drive_read_text(file_id):
    """Le conteudo de texto de um arquivo no Drive."""
    url = f'{DRIVE_BASE}/drive/v3/files/{file_id}?alt=media'
    req = urllib.request.Request(url)
    req.add_header('Authorization', f'Bearer {MATON_KEY}')
    with urllib.request.urlopen(req) as resp:
        return resp.read().decode('utf-8')


def _drive_list_files(folder_id, query=None):
    """Lista arquivos dentro de uma pasta no Drive."""
    if not query:
        query = f"'{folder_id}' in parents and trashed = false"
    encoded_q = urllib.parse.quote(query)
    url = f'{DRIVE_BASE}/drive/v3/files?q={encoded_q}&fields=files(id,name,mimeType,modifiedTime)'
    req = urllib.request.Request(url)
    req.add_header('Authorization', f'Bearer {MATON_KEY}')
    result = json.load(urllib.request.urlopen(req))
    return result.get('files', [])


def _log(session_path, message, level='INFO'):
    """Adiciona entrada ao log local da sessao."""
    log_path = os.path.join(session_path, 'log.md')
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    entry = f"[{timestamp}] [{level}] {message}\n"
    with open(log_path, 'a', encoding='utf-8') as f:
        f.write(entry)


def _safe_json_write(filepath, data):
    """Escreve JSON de forma segura com indent."""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def _safe_text_write(filepath, content):
    """Escreve texto de forma segura."""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


def _now_iso():
    """Retorna timestamp ISO atual."""
    return datetime.datetime.now().isoformat()


# ============================================================
# NOTION: TEMPLATE ESTRUTURADO DE 10 SECOES
# ============================================================

def _build_notion_session_blocks(session_id, tipo_tarefa, version, objetivo=''):
    """
    Constroi os blocos Notion para a pagina de sessao com as 10 secoes canonicas.
    Cada secao e um heading_2 seguido de conteudo placeholder.

    Args:
        session_id: ID unico da sessao.
        tipo_tarefa: Tipo da tarefa (ex: 'programacao', 'design').
        version: Versao do ultra_prompt.
        objetivo: Descricao do objetivo (opcional).

    Returns:
        list: Lista de blocos Notion prontos para criar a pagina.
    """
    blocks = []

    # --- METADADOS ---
    blocks.append(_heading('METADADOS'))
    blocks.append(_paragraph(f'Session ID: {session_id}'))
    blocks.append(_paragraph(f'Tipo: {tipo_tarefa}'))
    blocks.append(_paragraph(f'Ultra Prompt Version: {version}'))
    blocks.append(_paragraph(f'Criado em: {_now_iso()}'))
    blocks.append(_paragraph(f'Status: ATIVA'))
    blocks.append(_divider())

    # --- OBJETIVO ---
    blocks.append(_heading('OBJETIVO'))
    blocks.append(_paragraph(objetivo or '(sera preenchido durante a sessao)'))
    blocks.append(_divider())

    # --- CONTEXTO ---
    blocks.append(_heading('CONTEXTO'))
    blocks.append(_paragraph('(contexto relevante sera adicionado aqui)'))
    blocks.append(_divider())

    # --- PLANO ---
    blocks.append(_heading('PLANO'))
    blocks.append(_paragraph('(plano de execucao sera registrado aqui)'))
    blocks.append(_divider())

    # --- WAL ---
    blocks.append(_heading('WAL'))
    blocks.append(_paragraph('(etapas serao registradas aqui — este e o log canonico)'))
    blocks.append(_divider())

    # --- DECISOES ---
    blocks.append(_heading('DECISOES'))
    blocks.append(_paragraph('(decisoes importantes serao registradas aqui)'))
    blocks.append(_divider())

    # --- OUTPUTS ---
    blocks.append(_heading('OUTPUTS'))
    blocks.append(_paragraph('(links para arquivos entregues)'))
    blocks.append(_divider())

    # --- LINKS ---
    blocks.append(_heading('LINKS'))
    blocks.append(_paragraph('(links externos relevantes)'))
    blocks.append(_divider())

    # --- APRENDIZADOS ---
    blocks.append(_heading('APRENDIZADOS'))
    blocks.append(_paragraph('(licoes aprendidas durante a sessao)'))
    blocks.append(_divider())

    # --- RESUMO ---
    blocks.append(_heading('RESUMO'))
    blocks.append(_paragraph('(resumo final sera escrito ao encerrar a sessao)'))

    return blocks


def _heading(text, level=2):
    """Cria bloco heading Notion."""
    key = f'heading_{level}'
    return {
        'object': 'block',
        'type': key,
        key: {'rich_text': [{'text': {'content': text}}]}
    }


def _paragraph(text):
    """Cria bloco paragrafo Notion."""
    return {
        'object': 'block',
        'type': 'paragraph',
        'paragraph': {'rich_text': [{'text': {'content': text}}]}
    }


def _divider():
    """Cria bloco divisor Notion."""
    return {'object': 'block', 'type': 'divider', 'divider': {}}


def _callout(text, emoji='📋'):
    """Cria bloco callout Notion."""
    return {
        'object': 'block',
        'type': 'callout',
        'callout': {
            'rich_text': [{'text': {'content': text}}],
            'icon': {'emoji': emoji}
        }
    }


# ============================================================
# 1. setup_session
# ============================================================

def setup_session(session_id, tipo_tarefa, notion_workspace_id, drive_root_id, version="6.1.0"):
    """
    Cria toda a infraestrutura de uma nova sessao.

    Executa na ordem:
    1. Cria pasta no Drive com subpastas outputs/ e recursos/
    2. Cria pagina Notion com template estruturado de 10 secoes
    3. Cria .session/ local com arquivos de estado
    4. Escreve referencia.md no Drive com ultra_prompt_version
    5. Retorna dict com todos os IDs e caminhos

    Args:
        session_id: ID unico da sessao (formato: YYYY-MM-DD-descricao-curta).
        tipo_tarefa: Tipo da tarefa (ex: 'programacao', 'design').
        notion_workspace_id: ID da pagina pai no Notion.
        drive_root_id: ID da pasta raiz no Drive.
        version: Versao do ultra_prompt (default: '6.1.0').

    Returns:
        dict: {session_id, notion_page_id, drive_folder_id, session_local_path, version}

    Raises:
        Exception: Se alguma etapa critica falhar (Drive ou Notion).
    """
    session_path = SESSION_LOCAL_ROOT
    errors = []

    # --- Etapa 1: Criar pasta Drive ---
    drive_folder_id = None
    outputs_folder_id = None
    recursos_folder_id = None

    try:
        # Pasta principal da sessao
        folder_meta = {
            'name': session_id,
            'mimeType': 'application/vnd.google-apps.folder',
            'parents': [drive_root_id]
        }
        result = _drive_request('drive/v3/files', 'POST', folder_meta)
        drive_folder_id = result['id']

        # Subpasta outputs/
        outputs_meta = {
            'name': 'outputs',
            'mimeType': 'application/vnd.google-apps.folder',
            'parents': [drive_folder_id]
        }
        outputs_result = _drive_request('drive/v3/files', 'POST', outputs_meta)
        outputs_folder_id = outputs_result['id']

        # Subpasta recursos/
        recursos_meta = {
            'name': 'recursos',
            'mimeType': 'application/vnd.google-apps.folder',
            'parents': [drive_folder_id]
        }
        recursos_result = _drive_request('drive/v3/files', 'POST', recursos_meta)
        recursos_folder_id = recursos_result['id']

    except Exception as e:
        errors.append(f'Drive: {str(e)}')

    # --- Etapa 2: Criar pagina Notion ---
    notion_page_id = None

    try:
        children_blocks = _build_notion_session_blocks(session_id, tipo_tarefa, version)
        page_data = {
            'parent': {'type': 'page_id', 'page_id': notion_workspace_id},
            'properties': {
                'title': [{'text': {'content': f'Sessao: {session_id}'}}]
            },
            'children': children_blocks
        }
        page_result = _notion_request('pages', 'POST', page_data)
        notion_page_id = page_result['id']

    except Exception as e:
        errors.append(f'Notion: {str(e)}')

    # --- Etapa 3: Criar .session/ local ---
    try:
        os.makedirs(session_path, exist_ok=True)

        # wal.md
        wal_content = f"# WAL — {session_id}\n\n"
        wal_content += f"Sessao criada em {_now_iso()}\n\n"
        wal_content += "| # | Etapa | Status | Inicio | Fim |\n"
        wal_content += "|---|-------|--------|--------|-----|\n"
        wal_content += "| 0 | Bootstrap | CONCLUIDO | " + _now_iso() + " | " + _now_iso() + " |\n"
        _safe_text_write(os.path.join(session_path, 'wal.md'), wal_content)

        # state.json
        state = {
            'session_id': session_id,
            'tipo_tarefa': tipo_tarefa,
            'version': version,
            'created_at': _now_iso(),
            'status': 'ATIVA',
            'notion_page_id': notion_page_id,
            'drive_folder_id': drive_folder_id,
            'drive_outputs_folder_id': outputs_folder_id,
            'drive_recursos_folder_id': recursos_folder_id,
            'current_step': 0,
            'total_steps': 0,
            'connections_available': {},
            'modules_loaded': [tipo_tarefa],
            'imported_from': None,
            'errors': errors if errors else [],
        }
        _safe_json_write(os.path.join(session_path, 'state.json'), state)

        # log.md
        _safe_text_write(os.path.join(session_path, 'log.md'), f"# Log — {session_id}\n\n")
        _log(session_path, f'Sessao criada: {session_id} (tipo: {tipo_tarefa}, version: {version})')
        if drive_folder_id:
            _log(session_path, f'Drive: pasta criada ({drive_folder_id}) com subpastas outputs/ e recursos/')
        if notion_page_id:
            _log(session_path, f'Notion: pagina criada ({notion_page_id}) com 10 secoes')
        for err in errors:
            _log(session_path, f'ERRO durante setup: {err}', level='ERROR')

        # reminders.json
        _safe_json_write(os.path.join(session_path, 'reminders.json'), [])

        # pending_sync.json
        _safe_json_write(os.path.join(session_path, 'pending_sync.json'), {
            'notion': [],
            'drive': [],
            'github': [],
        })

        # transactions.json
        _safe_json_write(os.path.join(session_path, 'transactions.json'), {
            'transactions': [],
            'last_synced': _now_iso(),
        })

    except Exception as e:
        errors.append(f'Local: {str(e)}')

    # --- Etapa 4: Escrever referencia.md no Drive ---
    try:
        if drive_folder_id:
            ref_content = f"# Referencia da Sessao\n\n"
            ref_content += f"- **Session ID**: {session_id}\n"
            ref_content += f"- **Ultra Prompt Version**: {version}\n"
            ref_content += f"- **Tipo**: {tipo_tarefa}\n"
            ref_content += f"- **Notion Page ID**: {notion_page_id or 'ERRO'}\n"
            ref_content += f"- **Drive Folder ID**: {drive_folder_id}\n"
            ref_content += f"- **Outputs Folder ID**: {outputs_folder_id or 'ERRO'}\n"
            ref_content += f"- **Recursos Folder ID**: {recursos_folder_id or 'ERRO'}\n"
            ref_content += f"- **Criado em**: {_now_iso()}\n"
            ref_content += f"- **Status**: ATIVA\n"
            _drive_upload_text(ref_content, 'referencia.md', drive_folder_id)
            _log(session_path, 'referencia.md escrito no Drive')

    except Exception as e:
        errors.append(f'Drive referencia.md: {str(e)}')
        _log(session_path, f'ERRO ao escrever referencia.md: {str(e)}', level='ERROR')

    # --- Etapa 5: Retornar resultado ---
    result = {
        'session_id': session_id,
        'notion_page_id': notion_page_id,
        'drive_folder_id': drive_folder_id,
        'drive_outputs_folder_id': outputs_folder_id,
        'drive_recursos_folder_id': recursos_folder_id,
        'session_local_path': session_path,
        'version': version,
        'errors': errors if errors else [],
    }

    _log(session_path, f'Setup concluido. Erros: {len(errors)}')
    return result


# ============================================================
# 2. import_session
# ============================================================

def import_session(drive_folder_link_or_id, notion_workspace_id=None, drive_root_id=None, version="6.1.0"):
    """
    Importa uma sessao anterior e cria uma NOVA sessao com referencia a ela.

    REGRA: NUNCA deleta a sessao anterior. Sempre cria nova.

    Fluxo:
    1. Le referencia.md do Drive da sessao anterior
    2. Extrai notion_page_id e metadados
    3. Le pagina Notion da sessao anterior (WAL canonico)
    4. Identifica ultima etapa CONCLUIDA
    5. Cria NOVA sessao com referencia a anterior
    6. Retorna ponto de continuacao

    Args:
        drive_folder_link_or_id: Link ou ID da pasta da sessao anterior no Drive.
        notion_workspace_id: ID do workspace Notion (para criar nova sessao).
        drive_root_id: ID da pasta raiz no Drive (para criar nova sessao).
        version: Versao do ultra_prompt.

    Returns:
        dict: {
            session_result (nova sessao),
            previous_session_id,
            previous_notion_page_id,
            continuation_point (ultima etapa concluida),
            wal_entries (entradas do WAL anterior),
            context_recovered (contexto extraido)
        }
    """
    session_path = SESSION_LOCAL_ROOT
    os.makedirs(session_path, exist_ok=True)
    _safe_text_write(os.path.join(session_path, 'log.md'), f"# Log — Import\n\n")

    # --- Extrair folder_id do link se necessario ---
    folder_id = _extract_drive_id(drive_folder_link_or_id)
    _log(session_path, f'Importando sessao do Drive folder: {folder_id}')

    # --- Etapa 1: Ler referencia.md ---
    ref_data = {}
    try:
        files = _drive_list_files(folder_id)
        ref_file = None
        for f in files:
            if f.get('name') == 'referencia.md':
                ref_file = f
                break

        if not ref_file:
            raise FileNotFoundError('referencia.md nao encontrado na pasta da sessao anterior')

        ref_content = _drive_read_text(ref_file['id'])
        ref_data = _parse_referencia_md(ref_content)
        _log(session_path, f'referencia.md lido: {json.dumps(ref_data, ensure_ascii=False)[:200]}')

    except Exception as e:
        _log(session_path, f'ERRO ao ler referencia.md: {str(e)}', level='ERROR')
        return {'error': f'Falha ao ler referencia.md: {str(e)}', 'success': False}

    # --- Etapa 2: Extrair metadados ---
    previous_session_id = ref_data.get('Session ID', 'desconhecido')
    previous_notion_page_id = ref_data.get('Notion Page ID', '')
    previous_tipo = ref_data.get('Tipo', 'outro')

    # --- Etapa 3: Ler pagina Notion da sessao anterior ---
    wal_entries = []
    context_recovered = ''
    last_completed_step = -1

    try:
        if previous_notion_page_id and previous_notion_page_id != 'ERRO':
            blocks = _read_all_notion_blocks(previous_notion_page_id)
            wal_entries, context_recovered, last_completed_step = _extract_session_data_from_blocks(blocks)
            _log(session_path, f'Notion lido: {len(blocks)} blocos, ultima etapa concluida: {last_completed_step}')
        else:
            _log(session_path, 'Notion page_id invalido, continuando sem dados do Notion', level='WARN')

    except Exception as e:
        _log(session_path, f'ERRO ao ler Notion da sessao anterior: {str(e)}', level='ERROR')

    # --- Etapa 4: Reconstruir .session/ local a partir do Notion (WAL canonico) ---
    try:
        wal_content = f"# WAL — Importado de {previous_session_id}\n\n"
        wal_content += f"Importado em {_now_iso()}\n\n"
        wal_content += "## WAL da sessao anterior\n\n"
        for entry in wal_entries:
            wal_content += f"- {entry}\n"
        wal_content += f"\n## Nova sessao\n\n"
        wal_content += "| # | Etapa | Status | Inicio | Fim |\n"
        wal_content += "|---|-------|--------|--------|-----|\n"
        wal_content += f"| 0 | Import + Bootstrap | CONCLUIDO | {_now_iso()} | {_now_iso()} |\n"
        _safe_text_write(os.path.join(session_path, 'wal.md'), wal_content)

    except Exception as e:
        _log(session_path, f'ERRO ao reconstruir WAL local: {str(e)}', level='ERROR')

    # --- Etapa 5: Criar NOVA sessao com referencia a anterior ---
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    new_session_id = f"{today}-cont-{previous_session_id}"
    # Truncar se muito longo
    if len(new_session_id) > 80:
        new_session_id = new_session_id[:80]

    session_result = None
    if notion_workspace_id and drive_root_id:
        try:
            session_result = setup_session(
                session_id=new_session_id,
                tipo_tarefa=previous_tipo,
                notion_workspace_id=notion_workspace_id,
                drive_root_id=drive_root_id,
                version=version,
            )

            # Atualizar state.json com referencia a sessao anterior
            state_path = os.path.join(SESSION_LOCAL_ROOT, 'state.json')
            if os.path.exists(state_path):
                with open(state_path, 'r', encoding='utf-8') as f:
                    state = json.load(f)
                state['imported_from'] = {
                    'session_id': previous_session_id,
                    'notion_page_id': previous_notion_page_id,
                    'drive_folder_id': folder_id,
                    'last_completed_step': last_completed_step,
                }
                _safe_json_write(state_path, state)

            _log(SESSION_LOCAL_ROOT, f'Nova sessao criada com referencia a {previous_session_id}')

        except Exception as e:
            _log(session_path, f'ERRO ao criar nova sessao: {str(e)}', level='ERROR')
            return {'error': f'Falha ao criar nova sessao: {str(e)}', 'success': False}
    else:
        _log(session_path, 'notion_workspace_id ou drive_root_id nao fornecidos, nova sessao nao criada', level='WARN')

    return {
        'success': True,
        'session_result': session_result,
        'previous_session_id': previous_session_id,
        'previous_notion_page_id': previous_notion_page_id,
        'continuation_point': last_completed_step,
        'wal_entries': wal_entries,
        'context_recovered': context_recovered,
    }


def _extract_drive_id(link_or_id):
    """
    Extrai o ID do Drive a partir de um link ou retorna o ID direto.

    Suporta formatos:
    - https://drive.google.com/drive/folders/FOLDER_ID
    - https://drive.google.com/drive/u/0/folders/FOLDER_ID
    - ID direto (string sem /)

    Args:
        link_or_id: Link do Google Drive ou ID direto.

    Returns:
        str: ID da pasta.
    """
    if '/' not in link_or_id:
        return link_or_id.strip()

    # Extrair de URL
    parts = link_or_id.rstrip('/').split('/')
    # O ID geralmente e o ultimo segmento antes de query params
    raw_id = parts[-1].split('?')[0]
    return raw_id


def _parse_referencia_md(content):
    """
    Faz parse do referencia.md e retorna dict com os campos.

    Args:
        content: Conteudo do referencia.md como string.

    Returns:
        dict: Campos extraidos (Session ID, Notion Page ID, etc.).
    """
    data = {}
    for line in content.split('\n'):
        line = line.strip()
        if line.startswith('- **') and '**:' in line:
            # Formato: - **Campo**: valor
            try:
                key_part = line.split('**')[1]
                value_part = line.split('**: ', 1)[1].strip()
                data[key_part] = value_part
            except (IndexError, ValueError):
                continue
    return data


def _read_all_notion_blocks(page_id):
    """
    Le todos os blocos de uma pagina Notion com paginacao.

    Args:
        page_id: ID da pagina Notion.

    Returns:
        list: Lista de todos os blocos.
    """
    all_blocks = []
    has_more = True
    start_cursor = None

    while has_more:
        url = f'blocks/{page_id}/children?page_size=100'
        if start_cursor:
            url += f'&start_cursor={start_cursor}'
        result = _notion_request(url)
        all_blocks.extend(result.get('results', []))
        has_more = result.get('has_more', False)
        start_cursor = result.get('next_cursor')

    return all_blocks


def _extract_session_data_from_blocks(blocks):
    """
    Extrai dados estruturados dos blocos Notion de uma sessao.

    Identifica secoes pelo heading e extrai:
    - WAL entries
    - Contexto
    - Ultima etapa concluida

    Args:
        blocks: Lista de blocos Notion.

    Returns:
        tuple: (wal_entries, context_text, last_completed_step)
    """
    wal_entries = []
    context_parts = []
    last_completed_step = -1

    current_section = None

    for block in blocks:
        block_type = block.get('type', '')

        # Detectar secao pelo heading
        if block_type in ('heading_1', 'heading_2', 'heading_3'):
            rich_text = block.get(block_type, {}).get('rich_text', [])
            heading_text = ''.join(rt.get('plain_text', '') for rt in rich_text).strip().upper()

            for section in NOTION_SESSION_SECTIONS:
                if section in heading_text:
                    current_section = section
                    break
            else:
                current_section = heading_text
            continue

        # Extrair texto do bloco
        content = block.get(block_type, {})
        rich_text = content.get('rich_text', [])
        text = ''.join(rt.get('plain_text', '') for rt in rich_text).strip()

        if not text:
            continue

        # Classificar por secao
        if current_section == 'WAL':
            wal_entries.append(text)
            # Detectar ultima etapa concluida
            text_upper = text.upper()
            if 'CONCLUIDO' in text_upper or 'CONCLUIDA' in text_upper:
                # Tentar extrair numero da etapa
                for part in text.split():
                    if part.isdigit():
                        step_num = int(part)
                        if step_num > last_completed_step:
                            last_completed_step = step_num
                        break

        elif current_section == 'CONTEXTO':
            context_parts.append(text)

        elif current_section == 'OBJETIVO':
            context_parts.insert(0, f'[OBJETIVO] {text}')

    context_recovered = '\n'.join(context_parts)
    return wal_entries, context_recovered, last_completed_step


# ============================================================
# 3. check_all_connections
# ============================================================

def check_all_connections():
    """
    Verifica TODAS as conexoes Maton ativas do usuario.

    Checa os 4 servicos obrigatorios (notion, google-drive, github, google-mail)
    e salva o resultado em .session/state.json -> connections_available.

    Returns:
        dict: Mapa de app -> status (ex: {'notion': 'ACTIVE', 'google-drive': 'MISSING'}).
    """
    apps = ['notion', 'google-drive', 'github', 'google-mail']
    connections = {}

    for app in apps:
        try:
            result = _maton_ctrl_request(f'connections?app={app}&status=ACTIVE')
            conns = result.get('connections', [])
            if conns:
                connections[app] = 'ACTIVE'
            else:
                connections[app] = 'MISSING'
        except Exception as e:
            connections[app] = f'ERROR: {str(e)}'

    # Salvar em state.json se existir
    state_path = os.path.join(SESSION_LOCAL_ROOT, 'state.json')
    try:
        if os.path.exists(state_path):
            with open(state_path, 'r', encoding='utf-8') as f:
                state = json.load(f)
            state['connections_available'] = connections
            state['connections_checked_at'] = _now_iso()
            _safe_json_write(state_path, state)
            _log(SESSION_LOCAL_ROOT, f'Conexoes verificadas: {json.dumps(connections)}')
    except Exception:
        pass  # state.json pode nao existir ainda no bootstrap inicial

    return connections


# ============================================================
# 4. detect_compaction_risk
# ============================================================

def detect_compaction_risk(context_text='', extra_tokens=0):
    """
    Heuristica simples para detectar risco de compaction do contexto.

    Estima o numero de tokens no contexto atual e verifica se esta
    acima do threshold de 80% do limite estimado.

    NOTA: Este e um stub que sera expandido na Fase 5 com metricas
    mais sofisticadas (contagem real de tokens, historico de crescimento, etc.).

    Args:
        context_text: Texto do contexto atual para estimar tokens.
        extra_tokens: Tokens adicionais a considerar (modulos carregados, etc.).

    Returns:
        dict: {
            'at_risk': bool,
            'snapshot_needed': bool,
            'estimated_tokens': int,
            'limit': int,
            'usage_percent': float,
            'recommendation': str
        }
    """
    # Heuristica: ~4 caracteres por token (aproximacao para PT-BR)
    estimated_tokens = len(context_text) // 4 + extra_tokens

    # Considerar tambem o tamanho dos arquivos locais da sessao
    local_tokens = 0
    try:
        for fname in ['wal.md', 'log.md']:
            fpath = os.path.join(SESSION_LOCAL_ROOT, fname)
            if os.path.exists(fpath):
                with open(fpath, 'r', encoding='utf-8') as f:
                    local_tokens += len(f.read()) // 4
        for fname in ['state.json', 'reminders.json', 'pending_sync.json', 'transactions.json']:
            fpath = os.path.join(SESSION_LOCAL_ROOT, fname)
            if os.path.exists(fpath):
                with open(fpath, 'r', encoding='utf-8') as f:
                    local_tokens += len(f.read()) // 4
    except Exception:
        pass

    total_estimated = estimated_tokens + local_tokens
    usage_percent = total_estimated / ESTIMATED_CONTEXT_LIMIT if ESTIMATED_CONTEXT_LIMIT > 0 else 0
    at_risk = usage_percent >= COMPACTION_THRESHOLD

    recommendation = ''
    if usage_percent >= 0.95:
        recommendation = 'CRITICO: Snapshot imediato necessario. Risco de perda de contexto.'
    elif usage_percent >= COMPACTION_THRESHOLD:
        recommendation = 'ALERTA: Contexto proximo do limite. Preparar snapshot preventivo.'
    elif usage_percent >= 0.60:
        recommendation = 'ATENCAO: Contexto em 60%+. Monitorar crescimento.'
    else:
        recommendation = 'OK: Contexto dentro dos limites seguros.'

    result = {
        'at_risk': at_risk,
        'snapshot_needed': at_risk,
        'estimated_tokens': total_estimated,
        'limit': ESTIMATED_CONTEXT_LIMIT,
        'usage_percent': round(usage_percent * 100, 1),
        'recommendation': recommendation,
    }

    # Log se sessao existir
    try:
        if os.path.exists(os.path.join(SESSION_LOCAL_ROOT, 'log.md')):
            _log(SESSION_LOCAL_ROOT, f'Compaction check: {result["usage_percent"]}% ({total_estimated}/{ESTIMATED_CONTEXT_LIMIT} tokens) — {recommendation}')
    except Exception:
        pass

    return result


# ============================================================
# 5. snapshot_before_compaction
# ============================================================

def snapshot_before_compaction(notion_page_id):
    """
    Salva snapshot completo no Notion antes de compaction.

    Persiste no Notion: estado completo, WAL, decisoes, modulos em uso,
    tom de comunicacao, proximos passos e lembretes.

    Este snapshot permite que uma sessao futura reconstrua todo o contexto
    a partir do Notion, sem depender da memoria local ou do contexto do agente.

    Args:
        notion_page_id: ID da pagina Notion da sessao atual.

    Returns:
        dict: {
            'success': bool,
            'blocks_written': int,
            'snapshot_timestamp': str,
            'error': str (se houver)
        }
    """
    timestamp = _now_iso()
    blocks_written = 0

    try:
        # --- Coletar dados locais ---
        state = {}
        state_path = os.path.join(SESSION_LOCAL_ROOT, 'state.json')
        if os.path.exists(state_path):
            with open(state_path, 'r', encoding='utf-8') as f:
                state = json.load(f)

        wal_content = ''
        wal_path = os.path.join(SESSION_LOCAL_ROOT, 'wal.md')
        if os.path.exists(wal_path):
            with open(wal_path, 'r', encoding='utf-8') as f:
                wal_content = f.read()

        reminders = []
        reminders_path = os.path.join(SESSION_LOCAL_ROOT, 'reminders.json')
        if os.path.exists(reminders_path):
            with open(reminders_path, 'r', encoding='utf-8') as f:
                reminders = json.load(f)

        transactions = {}
        transactions_path = os.path.join(SESSION_LOCAL_ROOT, 'transactions.json')
        if os.path.exists(transactions_path):
            with open(transactions_path, 'r', encoding='utf-8') as f:
                transactions = json.load(f)

        # --- Construir blocos do snapshot ---
        snapshot_blocks = []

        # Marcador de snapshot
        snapshot_blocks.append(_divider())
        snapshot_blocks.append(_callout(
            f'SNAPSHOT PRE-COMPACTION — {timestamp}',
            '📸'
        ))
        snapshot_blocks.append(_divider())

        # Estado completo
        snapshot_blocks.append(_heading('SNAPSHOT: Estado', level=3))
        state_summary = json.dumps(state, indent=2, ensure_ascii=False)
        # Notion tem limite de 2000 chars por bloco de texto
        for chunk in _chunk_text(state_summary, 1900):
            snapshot_blocks.append({
                'object': 'block',
                'type': 'code',
                'code': {
                    'rich_text': [{'text': {'content': chunk}}],
                    'language': 'json'
                }
            })

        # WAL
        snapshot_blocks.append(_heading('SNAPSHOT: WAL', level=3))
        for chunk in _chunk_text(wal_content, 1900):
            snapshot_blocks.append(_paragraph(chunk))

        # Decisoes (extrair do state se existirem)
        decisions = state.get('decisions', [])
        if decisions:
            snapshot_blocks.append(_heading('SNAPSHOT: Decisoes', level=3))
            for d in decisions:
                snapshot_blocks.append(_paragraph(f'- {d}'))

        # Modulos em uso
        modules = state.get('modules_loaded', [])
        if modules:
            snapshot_blocks.append(_heading('SNAPSHOT: Modulos', level=3))
            snapshot_blocks.append(_paragraph(f'Modulos carregados: {", ".join(modules)}'))

        # Tom de comunicacao
        tom = state.get('communication_tone', '')
        if tom:
            snapshot_blocks.append(_heading('SNAPSHOT: Tom', level=3))
            snapshot_blocks.append(_paragraph(f'Tom: {tom}'))

        # Proximos passos
        next_steps = state.get('next_steps', [])
        if next_steps:
            snapshot_blocks.append(_heading('SNAPSHOT: Proximos Passos', level=3))
            for step in next_steps:
                snapshot_blocks.append(_paragraph(f'- {step}'))

        # Lembretes
        if reminders:
            snapshot_blocks.append(_heading('SNAPSHOT: Lembretes', level=3))
            for r in reminders:
                if isinstance(r, dict):
                    snapshot_blocks.append(_paragraph(f'- {r.get("text", str(r))}'))
                else:
                    snapshot_blocks.append(_paragraph(f'- {r}'))

        # Transacoes pendentes
        pending = transactions.get('transactions', [])
        if pending:
            snapshot_blocks.append(_heading('SNAPSHOT: Transacoes Pendentes', level=3))
            for t in pending:
                snapshot_blocks.append(_paragraph(f'- {json.dumps(t, ensure_ascii=False)[:500]}'))

        # Marcador de fim
        snapshot_blocks.append(_divider())
        snapshot_blocks.append(_callout(
            f'FIM DO SNAPSHOT — Total: {len(snapshot_blocks)} blocos',
            '✅'
        ))

        # --- Enviar para Notion ---
        # Notion aceita max 100 blocos por request
        for i in range(0, len(snapshot_blocks), 100):
            batch = snapshot_blocks[i:i+100]
            _notion_request(f'blocks/{notion_page_id}/children', 'PATCH', {'children': batch})
            blocks_written += len(batch)

        # --- Log ---
        _log(SESSION_LOCAL_ROOT, f'Snapshot pre-compaction salvo no Notion: {blocks_written} blocos')

        # Atualizar state.json
        if os.path.exists(state_path):
            with open(state_path, 'r', encoding='utf-8') as f:
                state = json.load(f)
            if 'snapshots' not in state:
                state['snapshots'] = []
            state['snapshots'].append({
                'timestamp': timestamp,
                'blocks_written': blocks_written,
                'reason': 'pre_compaction',
            })
            _safe_json_write(state_path, state)

        return {
            'success': True,
            'blocks_written': blocks_written,
            'snapshot_timestamp': timestamp,
            'error': None,
        }

    except Exception as e:
        error_msg = f'ERRO no snapshot: {str(e)}'
        try:
            _log(SESSION_LOCAL_ROOT, error_msg, level='ERROR')
        except Exception:
            pass
        return {
            'success': False,
            'blocks_written': blocks_written,
            'snapshot_timestamp': timestamp,
            'error': error_msg,
        }


def _chunk_text(text, max_len=1900):
    """
    Divide texto em chunks respeitando limite de caracteres do Notion.

    Args:
        text: Texto a dividir.
        max_len: Tamanho maximo de cada chunk.

    Returns:
        list: Lista de strings.
    """
    if len(text) <= max_len:
        return [text] if text else ['(vazio)']

    chunks = []
    while text:
        if len(text) <= max_len:
            chunks.append(text)
            break
        # Tentar quebrar em newline
        cut_pos = text.rfind('\n', 0, max_len)
        if cut_pos <= 0:
            cut_pos = max_len
        chunks.append(text[:cut_pos])
        text = text[cut_pos:].lstrip('\n')

    return chunks if chunks else ['(vazio)']


# ============================================================
# EXEMPLO DE USO
# ============================================================

if __name__ == '__main__':
    print("=== Session Bootstrap v6.1 ===\n")

    # Verificar conexoes
    print("1. Verificando conexoes...")
    conns = check_all_connections()
    for app, status in conns.items():
        print(f"   {app}: {status}")

    # Detectar risco de compaction
    print("\n2. Verificando risco de compaction...")
    risk = detect_compaction_risk("Texto de exemplo para teste de heuristica.")
    print(f"   Tokens estimados: {risk['estimated_tokens']}")
    print(f"   Uso: {risk['usage_percent']}%")
    print(f"   Recomendacao: {risk['recommendation']}")

    # Setup de sessao (requer conexoes ativas)
    print("\n3. Para criar sessao, use:")
    print("   result = setup_session('2026-04-17-teste', 'programacao', 'NOTION_ID', 'DRIVE_ID')")

    # Import de sessao
    print("\n4. Para importar sessao, use:")
    print("   result = import_session('DRIVE_FOLDER_ID_OU_LINK', 'NOTION_ID', 'DRIVE_ID')")
