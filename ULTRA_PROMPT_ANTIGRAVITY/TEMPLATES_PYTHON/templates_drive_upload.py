"""
Ultra Prompt v6.0 — Template: Upload para Google Drive via Maton Gateway
Uso: importar funcoes ou copiar/adaptar conforme necessidade da sessao.
"""

import urllib.request
import urllib.parse
import os
import json
import mimetypes


MATON_KEY = os.environ.get('MATON_API_KEY', '')
DRIVE_BASE = 'https://gateway.maton.ai/google-drive'


def create_folder(name, parent_id=None):
    """
    Cria uma pasta no Google Drive.

    Args:
        name: Nome da pasta.
        parent_id: (Opcional) ID da pasta pai.

    Returns:
        dict: Dados da pasta criada (contém 'id').
    """
    metadata = {
        'name': name,
        'mimeType': 'application/vnd.google-apps.folder'
    }
    if parent_id:
        metadata['parents'] = [parent_id]

    data = json.dumps(metadata).encode('utf-8')
    req = urllib.request.Request(f'{DRIVE_BASE}/drive/v3/files', data=data, method='POST')
    req.add_header('Authorization', f'Bearer {MATON_KEY}')
    req.add_header('Content-Type', 'application/json')

    return json.load(urllib.request.urlopen(req))


def upload_file(filepath, folder_id=None, filename=None):
    """
    Faz upload de um arquivo para o Google Drive usando multipart upload.

    Args:
        filepath: Caminho local do arquivo.
        folder_id: (Opcional) ID da pasta de destino.
        filename: (Opcional) Nome do arquivo no Drive (default: nome original).

    Returns:
        dict: Dados do arquivo criado (contém 'id').
    """
    if not filename:
        filename = os.path.basename(filepath)

    mime_type = mimetypes.guess_type(filepath)[0] or 'application/octet-stream'

    # Metadata
    metadata = {'name': filename}
    if folder_id:
        metadata['parents'] = [folder_id]
    metadata_json = json.dumps(metadata).encode('utf-8')

    # File content
    with open(filepath, 'rb') as f:
        file_content = f.read()

    # Multipart body
    boundary = '----UltraPromptV6Boundary'
    body = b''
    body += f'--{boundary}\r\n'.encode()
    body += b'Content-Type: application/json; charset=UTF-8\r\n\r\n'
    body += metadata_json + b'\r\n'
    body += f'--{boundary}\r\n'.encode()
    body += f'Content-Type: {mime_type}\r\n\r\n'.encode()
    body += file_content + b'\r\n'
    body += f'--{boundary}--'.encode()

    url = f'{DRIVE_BASE}/upload/drive/v3/files?uploadType=multipart'
    req = urllib.request.Request(url, data=body, method='POST')
    req.add_header('Authorization', f'Bearer {MATON_KEY}')
    req.add_header('Content-Type', f'multipart/related; boundary={boundary}')

    return json.load(urllib.request.urlopen(req))


def upload_text_file(content, filename, folder_id=None, mime_type='text/plain'):
    """
    Faz upload de conteudo de texto direto (sem arquivo local).

    Args:
        content: String com o conteudo.
        filename: Nome do arquivo no Drive.
        folder_id: (Opcional) ID da pasta de destino.
        mime_type: (Opcional) MIME type do arquivo.

    Returns:
        dict: Dados do arquivo criado.
    """
    metadata = {'name': filename}
    if folder_id:
        metadata['parents'] = [folder_id]
    metadata_json = json.dumps(metadata).encode('utf-8')

    file_bytes = content.encode('utf-8')

    boundary = '----UltraPromptV6Boundary'
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


def list_files(folder_id=None, query=None):
    """
    Lista arquivos no Drive.

    Args:
        folder_id: (Opcional) Listar arquivos dentro desta pasta.
        query: (Opcional) Query customizada (Drive API q parameter).

    Returns:
        list: Lista de arquivos (cada um com 'id', 'name', 'mimeType').
    """
    if folder_id and not query:
        query = f"'{folder_id}' in parents and trashed = false"
    elif not query:
        query = "trashed = false"

    url = f'{DRIVE_BASE}/drive/v3/files?q={urllib.parse.quote(query)}&fields=files(id,name,mimeType,modifiedTime)'
    req = urllib.request.Request(url)
    req.add_header('Authorization', f'Bearer {MATON_KEY}')

    result = json.load(urllib.request.urlopen(req))
    return result.get('files', [])


def get_file_info(file_id):
    """Retorna metadata de um arquivo."""
    url = f'{DRIVE_BASE}/drive/v3/files/{file_id}?fields=id,name,mimeType,size,modifiedTime,parents'
    req = urllib.request.Request(url)
    req.add_header('Authorization', f'Bearer {MATON_KEY}')
    return json.load(urllib.request.urlopen(req))


# --- Exemplo de uso ---
if __name__ == '__main__':
    import urllib.parse

    # Criar pasta
    folder = create_folder('2026-04-17-exemplo', parent_id='DRIVE_ROOT_FOLDER_ID')
    print(f"Pasta criada: {folder['id']}")

    # Upload de arquivo
    result = upload_file('/path/to/report.pdf', folder_id=folder['id'])
    print(f"Arquivo enviado: {result['id']}")

    # Upload de texto
    result = upload_text_file('# Referencia\nConteudo aqui', 'referencia.md', folder_id=folder['id'])
    print(f"Texto enviado: {result['id']}")

    # Listar arquivos
    files = list_files(folder_id=folder['id'])
    for f in files:
        print(f"  {f['name']} ({f['id']})")
