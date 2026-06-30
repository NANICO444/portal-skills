"""
Ultra Prompt v6.1 — Helper centralizado para Google Drive via Maton Gateway.

Todas as operacoes usam urllib (sem requests).
Auth via Bearer {MATON_API_KEY}.
Base URL: https://gateway.maton.ai/google-drive/

Funcoes disponiveis:
    drive_upload          — Upload multipart de arquivo local.
    drive_upload_content  — Upload de string direto (sem arquivo local).
    drive_create_folder   — Cria pasta no Drive.
    drive_download        — Download de arquivo para disco local.
    drive_find            — Busca arquivos com paginacao completa.
    drive_list            — Lista TODOS os arquivos de uma pasta com paginacao.
    drive_create_session_folder — Cria estrutura de sessao (pasta + outputs/ + recursos/).
    drive_write_referencia      — Escreve referencia.md estruturado.
"""

import urllib.request
import urllib.parse
import os
import json
import logging
import mimetypes
from datetime import datetime

logger = logging.getLogger(__name__)

MATON_KEY = os.environ.get('MATON_API_KEY', '')
DRIVE_BASE = 'https://gateway.maton.ai/google-drive'
BOUNDARY = '----UltraPromptV61Boundary'


# ---------------------------------------------------------------------------
# Helpers internos
# ---------------------------------------------------------------------------

def _auth_header():
    """Retorna dicionario com header de autorizacao."""
    return {'Authorization': f'Bearer {MATON_KEY}'}


def _build_multipart_body(metadata: dict, content: bytes, mime_type: str) -> bytes:
    """Monta corpo multipart/related para upload na API do Drive."""
    metadata_json = json.dumps(metadata).encode('utf-8')
    body = b''
    body += f'--{BOUNDARY}\r\n'.encode()
    body += b'Content-Type: application/json; charset=UTF-8\r\n\r\n'
    body += metadata_json + b'\r\n'
    body += f'--{BOUNDARY}\r\n'.encode()
    body += f'Content-Type: {mime_type}\r\n\r\n'.encode()
    body += content + b'\r\n'
    body += f'--{BOUNDARY}--'.encode()
    return body


def _upload_multipart(metadata: dict, content: bytes, mime_type: str) -> dict:
    """Executa upload multipart e retorna resposta JSON."""
    body = _build_multipart_body(metadata, content, mime_type)
    url = f'{DRIVE_BASE}/upload/drive/v3/files?uploadType=multipart'
    req = urllib.request.Request(url, data=body, method='POST')
    req.add_header('Authorization', f'Bearer {MATON_KEY}')
    req.add_header('Content-Type', f'multipart/related; boundary={BOUNDARY}')
    result = json.load(urllib.request.urlopen(req))
    logger.info("Upload concluido: %s (id=%s)", metadata.get('name', '?'), result.get('id'))
    return result


# ---------------------------------------------------------------------------
# 1. drive_upload
# ---------------------------------------------------------------------------

def drive_upload(path_local: str, parent_id: str, mime_type: str = None) -> str:
    """
    Faz upload multipart de um arquivo local para o Google Drive.

    Args:
        path_local: Caminho absoluto do arquivo local.
        parent_id: ID da pasta pai no Drive.
        mime_type: (Opcional) MIME type. Se None, detecta automaticamente.

    Returns:
        str: file_id do arquivo criado no Drive.

    Raises:
        FileNotFoundError: Se path_local nao existir.
    """
    if not os.path.isfile(path_local):
        raise FileNotFoundError(f"Arquivo nao encontrado: {path_local}")

    filename = os.path.basename(path_local)
    if mime_type is None:
        mime_type = mimetypes.guess_type(path_local)[0] or 'application/octet-stream'

    metadata = {'name': filename, 'parents': [parent_id]}

    with open(path_local, 'rb') as f:
        file_content = f.read()

    logger.info("Iniciando upload: %s (%d bytes) -> pasta %s", filename, len(file_content), parent_id)
    result = _upload_multipart(metadata, file_content, mime_type)
    return result['id']


# ---------------------------------------------------------------------------
# 2. drive_upload_content
# ---------------------------------------------------------------------------

def drive_upload_content(
    content: str,
    filename: str,
    parent_id: str,
    mime_type: str = 'text/plain',
) -> str:
    """
    Faz upload de conteudo de texto direto (sem arquivo local).

    Args:
        content: String com o conteudo a enviar.
        filename: Nome do arquivo no Drive.
        parent_id: ID da pasta pai no Drive.
        mime_type: (Opcional) MIME type. Padrao: text/plain.

    Returns:
        str: file_id do arquivo criado no Drive.
    """
    metadata = {'name': filename, 'parents': [parent_id]}
    file_bytes = content.encode('utf-8')

    logger.info("Upload de conteudo: %s (%d bytes) -> pasta %s", filename, len(file_bytes), parent_id)
    result = _upload_multipart(metadata, file_bytes, mime_type)
    return result['id']


# ---------------------------------------------------------------------------
# 3. drive_create_folder
# ---------------------------------------------------------------------------

def drive_create_folder(name: str, parent_id: str) -> str:
    """
    Cria uma pasta no Google Drive.

    Args:
        name: Nome da pasta.
        parent_id: ID da pasta pai.

    Returns:
        str: folder_id da pasta criada.
    """
    metadata = {
        'name': name,
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': [parent_id],
    }
    data = json.dumps(metadata).encode('utf-8')
    req = urllib.request.Request(f'{DRIVE_BASE}/drive/v3/files', data=data, method='POST')
    req.add_header('Authorization', f'Bearer {MATON_KEY}')
    req.add_header('Content-Type', 'application/json')

    result = json.load(urllib.request.urlopen(req))
    logger.info("Pasta criada: %s (id=%s)", name, result.get('id'))
    return result['id']


# ---------------------------------------------------------------------------
# 4. drive_download
# ---------------------------------------------------------------------------

def drive_download(file_id: str, dest_path: str) -> str:
    """
    Faz download de um arquivo do Drive para o disco local.

    Args:
        file_id: ID do arquivo no Drive.
        dest_path: Caminho absoluto de destino no disco local.

    Returns:
        str: Caminho do arquivo salvo.

    Raises:
        FileExistsError: Se dest_path ja existir (nunca sobrescreve sem confirmar).
    """
    if os.path.exists(dest_path):
        raise FileExistsError(
            f"Destino ja existe: {dest_path}. Remova manualmente ou use outro caminho."
        )

    dest_dir = os.path.dirname(dest_path)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    url = f'{DRIVE_BASE}/drive/v3/files/{file_id}?alt=media'
    req = urllib.request.Request(url)
    req.add_header('Authorization', f'Bearer {MATON_KEY}')

    with urllib.request.urlopen(req) as resp:
        content = resp.read()

    with open(dest_path, 'wb') as f:
        f.write(content)

    logger.info("Download concluido: %s (%d bytes)", dest_path, len(content))
    return dest_path


# ---------------------------------------------------------------------------
# 5. drive_find
# ---------------------------------------------------------------------------

def drive_find(
    name: str = None,
    parent_id: str = None,
    mime_type: str = None,
) -> list:
    """
    Busca arquivos no Drive com paginacao completa.

    Args:
        name: (Opcional) Nome exato do arquivo.
        parent_id: (Opcional) Restringir busca a esta pasta.
        mime_type: (Opcional) Filtrar por MIME type.

    Returns:
        list: Lista de dicts com id, name, mimeType, modifiedTime.
    """
    conditions = ["trashed = false"]
    if name:
        conditions.append(f"name = '{name}'")
    if parent_id:
        conditions.append(f"'{parent_id}' in parents")
    if mime_type:
        conditions.append(f"mimeType = '{mime_type}'")

    query = ' and '.join(conditions)
    fields = 'nextPageToken,files(id,name,mimeType,modifiedTime)'
    all_files = []
    page_token = None

    while True:
        params = {
            'q': query,
            'fields': fields,
            'pageSize': '1000',
        }
        if page_token:
            params['pageToken'] = page_token

        url = f'{DRIVE_BASE}/drive/v3/files?{urllib.parse.urlencode(params)}'
        req = urllib.request.Request(url)
        req.add_header('Authorization', f'Bearer {MATON_KEY}')

        result = json.load(urllib.request.urlopen(req))
        all_files.extend(result.get('files', []))

        page_token = result.get('nextPageToken')
        if not page_token:
            break

    logger.info("drive_find: %d resultados (query=%s)", len(all_files), query)
    return all_files


# ---------------------------------------------------------------------------
# 6. drive_list
# ---------------------------------------------------------------------------

def drive_list(parent_id: str, page_size: int = 100) -> list:
    """
    Lista TODOS os arquivos dentro de uma pasta, com paginacao completa.

    Args:
        parent_id: ID da pasta no Drive.
        page_size: Quantidade de itens por pagina (max 1000).

    Returns:
        list: Lista de dicts com id, name, mimeType, modifiedTime.
    """
    query = f"'{parent_id}' in parents and trashed = false"
    fields = 'nextPageToken,files(id,name,mimeType,modifiedTime,size)'
    all_files = []
    page_token = None

    while True:
        params = {
            'q': query,
            'fields': fields,
            'pageSize': str(min(page_size, 1000)),
        }
        if page_token:
            params['pageToken'] = page_token

        url = f'{DRIVE_BASE}/drive/v3/files?{urllib.parse.urlencode(params)}'
        req = urllib.request.Request(url)
        req.add_header('Authorization', f'Bearer {MATON_KEY}')

        result = json.load(urllib.request.urlopen(req))
        all_files.extend(result.get('files', []))

        page_token = result.get('nextPageToken')
        if not page_token:
            break

    logger.info("drive_list: %d arquivos em %s", len(all_files), parent_id)
    return all_files


# ---------------------------------------------------------------------------
# 7. drive_create_session_folder
# ---------------------------------------------------------------------------

def drive_create_session_folder(root_id: str, session_id: str) -> dict:
    """
    Cria estrutura de pasta para uma sessao: pasta principal + outputs/ + recursos/.

    Args:
        root_id: ID da pasta raiz no Drive.
        session_id: Identificador da sessao (usado como nome da pasta).

    Returns:
        dict: {'folder_id': str, 'outputs_id': str, 'recursos_id': str}
    """
    folder_id = drive_create_folder(session_id, root_id)
    outputs_id = drive_create_folder('outputs', folder_id)
    recursos_id = drive_create_folder('recursos', folder_id)

    logger.info(
        "Sessao criada: %s (folder=%s, outputs=%s, recursos=%s)",
        session_id, folder_id, outputs_id, recursos_id,
    )
    return {
        'folder_id': folder_id,
        'outputs_id': outputs_id,
        'recursos_id': recursos_id,
    }


# ---------------------------------------------------------------------------
# 8. drive_write_referencia
# ---------------------------------------------------------------------------

def drive_write_referencia(folder_id: str, data_dict: dict) -> str:
    """
    Escreve um arquivo referencia.md estruturado dentro da pasta indicada.

    O arquivo inclui automaticamente o campo ultra_prompt_version e timestamp.

    Args:
        folder_id: ID da pasta onde salvar o arquivo.
        data_dict: Dicionario com campos a incluir na referencia.
                   Chaves comuns: titulo, descricao, objetivo, notas, links.

    Returns:
        str: file_id do arquivo referencia.md criado.
    """
    lines = [
        '# Referencia',
        '',
        f'- **ultra_prompt_version**: v6.1',
        f'- **gerado_em**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}',
    ]

    for key, value in data_dict.items():
        if isinstance(value, list):
            lines.append(f'- **{key}**:')
            for item in value:
                lines.append(f'  - {item}')
        elif isinstance(value, dict):
            lines.append(f'- **{key}**:')
            for k, v in value.items():
                lines.append(f'  - {k}: {v}')
        else:
            lines.append(f'- **{key}**: {value}')

    lines.append('')
    content = '\n'.join(lines)

    file_id = drive_upload_content(content, 'referencia.md', folder_id, 'text/markdown')
    logger.info("referencia.md escrito em pasta %s (id=%s)", folder_id, file_id)
    return file_id


# ---------------------------------------------------------------------------
# Exemplo de uso
# ---------------------------------------------------------------------------

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

    ROOT_ID = 'SEU_DRIVE_ROOT_FOLDER_ID'

    # Criar sessao
    sessao = drive_create_session_folder(ROOT_ID, '2026-04-17-teste')
    print(f"Sessao: {sessao}")

    # Upload de arquivo
    fid = drive_upload('/tmp/exemplo.pdf', sessao['outputs_id'])
    print(f"Upload: {fid}")

    # Upload de conteudo
    fid = drive_upload_content('Conteudo de teste', 'nota.txt', sessao['outputs_id'])
    print(f"Texto: {fid}")

    # Referencia
    ref_id = drive_write_referencia(sessao['folder_id'], {
        'titulo': 'Sessao de teste',
        'objetivo': 'Validar helpers do Drive',
        'links': ['https://example.com'],
    })
    print(f"Referencia: {ref_id}")

    # Listar
    arquivos = drive_list(sessao['folder_id'])
    for a in arquivos:
        print(f"  {a['name']} ({a['id']})")

    # Buscar
    encontrados = drive_find(name='nota.txt', parent_id=sessao['outputs_id'])
    print(f"Encontrados: {encontrados}")

    # Download
    if encontrados:
        drive_download(encontrados[0]['id'], '/tmp/nota_download.txt')
        print("Download OK")
