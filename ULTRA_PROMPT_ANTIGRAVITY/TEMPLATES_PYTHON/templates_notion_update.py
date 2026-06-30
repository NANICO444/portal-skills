"""
Ultra Prompt v6.0 — Template: Operacoes Notion via Maton Gateway
Uso: importar funcoes ou copiar/adaptar conforme necessidade da sessao.
"""

import urllib.request
import os
import json


MATON_KEY = os.environ.get('MATON_API_KEY', '')
NOTION_BASE = 'https://gateway.maton.ai/notion/v1'
NOTION_VERSION = '2022-06-28'


def _notion_request(path, method='GET', data=None):
    """Request base para Notion API."""
    url = f'{NOTION_BASE}/{path}'
    encoded = json.dumps(data).encode('utf-8') if data else None
    req = urllib.request.Request(url, data=encoded, method=method)
    req.add_header('Authorization', f'Bearer {MATON_KEY}')
    req.add_header('Notion-Version', NOTION_VERSION)
    if data:
        req.add_header('Content-Type', 'application/json')
    return json.load(urllib.request.urlopen(req))


# === PAGINAS ===

def create_page(parent_page_id, title, children=None):
    """
    Cria uma pagina no Notion.

    Args:
        parent_page_id: ID da pagina pai.
        title: Titulo da pagina.
        children: (Opcional) Lista de blocos filhos.

    Returns:
        dict: Dados da pagina criada (contém 'id').
    """
    data = {
        'parent': {'type': 'page_id', 'page_id': parent_page_id},
        'properties': {
            'title': [{'text': {'content': title}}]
        }
    }
    if children:
        data['children'] = children
    return _notion_request('pages', 'POST', data)


def get_page(page_id):
    """Le metadata de uma pagina."""
    return _notion_request(f'pages/{page_id}')


def update_page_title(page_id, new_title):
    """Atualiza o titulo de uma pagina."""
    data = {
        'properties': {
            'title': [{'text': {'content': new_title}}]
        }
    }
    return _notion_request(f'pages/{page_id}', 'PATCH', data)


# === BLOCOS (CONTEUDO) ===

def get_blocks(block_id, page_size=100):
    """Le blocos filhos de uma pagina/bloco."""
    return _notion_request(f'blocks/{block_id}/children?page_size={page_size}')


def append_blocks(page_id, blocks):
    """
    Adiciona blocos de conteudo a uma pagina.

    Args:
        page_id: ID da pagina.
        blocks: Lista de blocos Notion.

    Returns:
        dict: Resposta da API.
    """
    data = {'children': blocks}
    return _notion_request(f'blocks/{page_id}/children', 'PATCH', data)


def delete_block(block_id):
    """Deleta um bloco."""
    return _notion_request(f'blocks/{block_id}', 'DELETE')


# === BLOCOS HELPERS ===

def heading_block(text, level=2):
    """Cria bloco de heading (level 1, 2 ou 3)."""
    key = f'heading_{level}'
    return {
        'object': 'block',
        'type': key,
        key: {'rich_text': [{'text': {'content': text}}]}
    }


def paragraph_block(text):
    """Cria bloco de paragrafo."""
    return {
        'object': 'block',
        'type': 'paragraph',
        'paragraph': {'rich_text': [{'text': {'content': text}}]}
    }


def bulleted_list_block(text):
    """Cria bloco de lista com bullet."""
    return {
        'object': 'block',
        'type': 'bulleted_list_item',
        'bulleted_list_item': {'rich_text': [{'text': {'content': text}}]}
    }


def numbered_list_block(text):
    """Cria bloco de lista numerada."""
    return {
        'object': 'block',
        'type': 'numbered_list_item',
        'numbered_list_item': {'rich_text': [{'text': {'content': text}}]}
    }


def toggle_block(text, children=None):
    """Cria bloco toggle (colapsavel)."""
    block = {
        'object': 'block',
        'type': 'toggle',
        'toggle': {'rich_text': [{'text': {'content': text}}]}
    }
    if children:
        block['toggle']['children'] = children
    return block


def callout_block(text, emoji='💡'):
    """Cria bloco callout com emoji."""
    return {
        'object': 'block',
        'type': 'callout',
        'callout': {
            'rich_text': [{'text': {'content': text}}],
            'icon': {'emoji': emoji}
        }
    }


def divider_block():
    """Cria bloco divisor."""
    return {'object': 'block', 'type': 'divider', 'divider': {}}


def code_block(code, language='python'):
    """Cria bloco de codigo."""
    return {
        'object': 'block',
        'type': 'code',
        'code': {
            'rich_text': [{'text': {'content': code}}],
            'language': language
        }
    }


def table_block(rows, has_header=True):
    """
    Cria bloco de tabela.

    Args:
        rows: Lista de listas (cada sub-lista e uma linha).
        has_header: Se True, primeira linha e header.

    Returns:
        dict: Bloco table do Notion.
    """
    table_width = len(rows[0]) if rows else 0
    table_rows = []
    for row in rows:
        cells = [[{'text': {'content': str(cell)}}] for cell in row]
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


# === BUSCA ===

def search_pages(query='', page_size=10):
    """Busca paginas no Notion."""
    data = {'query': query, 'page_size': page_size}
    return _notion_request('search', 'POST', data)


# === LEITURA COMPLETA ===

def read_page_content(page_id):
    """
    Le todo o conteudo de uma pagina (todos os blocos).
    Pagina automaticamente se houver mais de 100 blocos.

    Returns:
        list: Lista de todos os blocos da pagina.
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


def extract_text_from_blocks(blocks):
    """Extrai texto puro de uma lista de blocos Notion."""
    texts = []
    for block in blocks:
        block_type = block.get('type', '')
        content = block.get(block_type, {})
        rich_text = content.get('rich_text', [])
        for rt in rich_text:
            texts.append(rt.get('plain_text', ''))
    return '\n'.join(texts)


# --- Exemplo de uso ---
if __name__ == '__main__':
    # Criar pagina com conteudo
    WORKSPACE_ID = 'SEU_WORKSPACE_ID'

    page = create_page(
        parent_page_id=WORKSPACE_ID,
        title='Sessao: 2026-04-17-teste',
        children=[
            heading_block('Resumo'),
            paragraph_block('Esta sessao foi criada como teste.'),
            divider_block(),
            heading_block('WAL'),
            table_block([
                ['#', 'Etapa', 'Status'],
                ['1', 'Setup', 'CONCLUIDO'],
                ['2', 'Execucao', 'PENDENTE']
            ]),
            divider_block(),
            callout_block('Lembrete: atualizar ao final da sessao', '📝')
        ]
    )
    print(f"Pagina criada: {page['id']}")

    # Ler conteudo
    blocks = read_page_content(page['id'])
    text = extract_text_from_blocks(blocks)
    print(f"Conteudo:\n{text}")

    # Adicionar blocos
    append_blocks(page['id'], [
        heading_block('Notas adicionais'),
        bulleted_list_block('Nota 1'),
        bulleted_list_block('Nota 2')
    ])
    print("Blocos adicionados.")
