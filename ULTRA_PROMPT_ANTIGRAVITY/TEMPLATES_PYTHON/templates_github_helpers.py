"""
Ultra Prompt v6.1 — Helper centralizado para GitHub via Maton Gateway.

Camada de alto nivel sobre a API do GitHub, com funcoes utilitarias
para leitura, escrita, criacao de repos, PRs e busca de templates/modulos.

Auth: Bearer {MATON_API_KEY}
Base URL: https://gateway.maton.ai/github/
Regra de seguranca: repositorios SEMPRE privados em create_repo.
"""

import urllib.request
import urllib.error
import os
import json
import base64


# === CONFIGURACAO ===

MATON_KEY = os.environ.get('MATON_API_KEY', '')
GITHUB_BASE = 'https://gateway.maton.ai/github'

# Repo padrao para templates/modulos (pode ser sobrescrito por parametro)
DEFAULT_OWNER = os.environ.get('GITHUB_OWNER', '')
DEFAULT_REPO = os.environ.get('GITHUB_REPO', '')


# === REQUEST BASE ===

def _github_request(path, method='GET', data=None):
    """
    Executa requisicao HTTP para a API do GitHub via Maton Gateway.

    Args:
        path: Caminho relativo da API (ex: 'repos/owner/repo/contents/file').
        method: Metodo HTTP (GET, POST, PUT, PATCH, DELETE).
        data: Dicionario com corpo da requisicao (sera convertido em JSON).

    Returns:
        dict ou list: Resposta da API parseada como JSON.

    Raises:
        urllib.error.HTTPError: Se a API retornar erro HTTP.
        ValueError: Se MATON_API_KEY nao estiver configurada.
    """
    if not MATON_KEY:
        raise ValueError(
            'MATON_API_KEY nao configurada. '
            'Defina a variavel de ambiente antes de usar os helpers do GitHub.'
        )
    url = f'{GITHUB_BASE}/{path}'
    encoded = json.dumps(data).encode('utf-8') if data else None
    req = urllib.request.Request(url, data=encoded, method=method)
    req.add_header('Authorization', f'Bearer {MATON_KEY}')
    req.add_header('Accept', 'application/vnd.github+json')
    if data:
        req.add_header('Content-Type', 'application/json')
    return json.load(urllib.request.urlopen(req))


# === FUNCOES PRINCIPAIS ===

def github_read_file(owner, repo, path, ref='main'):
    """
    Le um arquivo do repositorio e retorna o conteudo decodificado.

    Faz GET no endpoint contents/ e decodifica o base64 automaticamente.

    Args:
        owner: Dono do repositorio (usuario ou organizacao).
        repo: Nome do repositorio.
        path: Caminho do arquivo dentro do repo (ex: 'src/main.py').
        ref: Branch, tag ou SHA do commit (padrao: 'main').

    Returns:
        str: Conteudo do arquivo decodificado em UTF-8.

    Raises:
        urllib.error.HTTPError: 404 se o arquivo nao existir.
    """
    url = f'repos/{owner}/{repo}/contents/{path}'
    if ref:
        url += f'?ref={ref}'
    result = _github_request(url)
    content = base64.b64decode(result['content']).decode('utf-8')
    return content


def github_write_file(owner, repo, path, content, message, sha=None):
    """
    Cria ou atualiza um arquivo no repositorio.

    Se sha for fornecido, faz update direto. Se nao, tenta detectar
    automaticamente: busca o SHA atual do arquivo e, se existir, usa-o
    para o update. Se o arquivo nao existir (404), cria novo.

    REGRA DE SEGURANCA: sempre verifica SHA antes de sobrescrever.

    Args:
        owner: Dono do repositorio.
        repo: Nome do repositorio.
        path: Caminho do arquivo.
        content: Conteudo do arquivo (string UTF-8).
        message: Mensagem do commit.
        sha: (Opcional) SHA do arquivo atual. Se None, auto-detecta.

    Returns:
        dict: Dados do commit realizado.

    Raises:
        urllib.error.HTTPError: Se houver erro na API.
    """
    # Auto-detectar SHA se nao fornecido
    if sha is None:
        try:
            url = f'repos/{owner}/{repo}/contents/{path}'
            existing = _github_request(url)
            sha = existing['sha']
        except urllib.error.HTTPError as e:
            if e.code == 404:
                sha = None  # Arquivo novo
            else:
                raise

    data = {
        'message': message,
        'content': base64.b64encode(content.encode('utf-8')).decode('utf-8'),
    }
    if sha:
        data['sha'] = sha

    return _github_request(f'repos/{owner}/{repo}/contents/{path}', 'PUT', data)


def github_create_repo(name, private=True, description=''):
    """
    Cria um novo repositorio no GitHub.

    REGRA DE SEGURANCA INEGOCIAVEL: o parametro private e SEMPRE forcado
    para True, independentemente do valor passado. Repositorios publicos
    nao sao permitidos por este helper.

    Args:
        name: Nome do repositorio.
        private: Ignorado — sempre True (seguranca).
        description: Descricao do repositorio.

    Returns:
        dict: Dados do repo criado (contem 'full_name', 'html_url', etc.).
    """
    # SEGURANCA: private=True FORCADO, parametro ignorado propositalmente
    if not private:
        import warnings
        warnings.warn(
            'github_create_repo: tentativa de criar repo publico bloqueada. '
            'Forcando private=True por regra de seguranca.',
            UserWarning,
            stacklevel=2,
        )

    data = {
        'name': name,
        'description': description,
        'private': True,  # FORCADO — NUNCA publico
        'auto_init': True,
    }
    return _github_request('user/repos', 'POST', data)


def github_list_dir(owner, repo, path='', ref='main'):
    """
    Lista o conteudo de um diretorio no repositorio.

    Args:
        owner: Dono do repositorio.
        repo: Nome do repositorio.
        path: Caminho do diretorio ('' para raiz).
        ref: Branch, tag ou SHA (padrao: 'main').

    Returns:
        list[dict]: Lista de itens com 'name', 'path', 'type' ('file' ou 'dir'),
                    'sha', 'size', 'download_url', etc.
    """
    url = f'repos/{owner}/{repo}/contents/{path}'
    if ref:
        url += f'?ref={ref}'
    return _github_request(url)


def github_create_pr(owner, repo, title, body, head, base='main'):
    """
    Cria um Pull Request no repositorio.

    Args:
        owner: Dono do repositorio.
        repo: Nome do repositorio.
        title: Titulo do PR.
        body: Descricao/corpo do PR (suporta Markdown).
        head: Branch de origem (ex: 'feature/nova-funcao').
        base: Branch de destino (padrao: 'main').

    Returns:
        dict: Dados do PR criado (contem 'number', 'html_url', etc.).
    """
    data = {
        'title': title,
        'body': body,
        'head': head,
        'base': base,
    }
    return _github_request(f'repos/{owner}/{repo}/pulls', 'POST', data)


def github_list_prs(owner, repo, state='open'):
    """
    Lista Pull Requests do repositorio.

    Args:
        owner: Dono do repositorio.
        repo: Nome do repositorio.
        state: Filtro de estado — 'open', 'closed' ou 'all' (padrao: 'open').

    Returns:
        list[dict]: Lista de PRs com 'number', 'title', 'state', 'html_url', etc.
    """
    return _github_request(f'repos/{owner}/{repo}/pulls?state={state}')


# === FUNCOES DE BUSCA DE TEMPLATES E MODULOS ===

def fetch_template(name, owner=None, repo=None):
    """
    Busca um arquivo da pasta templates/ do repositorio padrao.

    Util para carregar templates reutilizaveis (prompts, configs, etc.)
    armazenados no repo do projeto.

    Args:
        name: Nome do arquivo (ex: 'base_prompt.txt' ou 'config.json').
        owner: (Opcional) Dono do repo. Usa DEFAULT_OWNER se nao informado.
        repo: (Opcional) Nome do repo. Usa DEFAULT_REPO se nao informado.

    Returns:
        str: Conteudo do template como string.

    Raises:
        ValueError: Se owner/repo nao forem informados e nao houver padrao.
        urllib.error.HTTPError: 404 se o template nao existir.
    """
    owner = owner or DEFAULT_OWNER
    repo = repo or DEFAULT_REPO
    if not owner or not repo:
        raise ValueError(
            'Owner e repo sao obrigatorios. Passe como parametro ou '
            'defina GITHUB_OWNER e GITHUB_REPO como variaveis de ambiente.'
        )
    path = f'templates/{name}'
    return github_read_file(owner, repo, path)


def fetch_module(module_name, owner=None, repo=None):
    """
    Busca um modulo da pasta modules/ do repositorio padrao.

    Util para carregar modulos de logica, dados ou configuracao
    armazenados no repo do projeto.

    Args:
        module_name: Nome do arquivo do modulo (ex: 'design.md', 'data.py').
        owner: (Opcional) Dono do repo. Usa DEFAULT_OWNER se nao informado.
        repo: (Opcional) Nome do repo. Usa DEFAULT_REPO se nao informado.

    Returns:
        str: Conteudo do modulo como string.

    Raises:
        ValueError: Se owner/repo nao forem informados e nao houver padrao.
        urllib.error.HTTPError: 404 se o modulo nao existir.
    """
    owner = owner or DEFAULT_OWNER
    repo = repo or DEFAULT_REPO
    if not owner or not repo:
        raise ValueError(
            'Owner e repo sao obrigatorios. Passe como parametro ou '
            'defina GITHUB_OWNER e GITHUB_REPO como variaveis de ambiente.'
        )
    path = f'modules/{module_name}'
    return github_read_file(owner, repo, path)


# === EXEMPLO DE USO ===

if __name__ == '__main__':
    OWNER = 'usuario'
    REPO = 'ultra-prompt'

    # Criar repo (SEMPRE privado)
    novo_repo = github_create_repo('meu-projeto', description='Projeto de teste')
    print(f"Repo criado: {novo_repo['full_name']} (privado: {novo_repo['private']})")

    # Escrever arquivo (cria automaticamente se nao existir)
    github_write_file(OWNER, REPO, 'docs/exemplo.md', '# Exemplo\nConteudo.', 'Add exemplo.md')

    # Ler arquivo
    conteudo = github_read_file(OWNER, REPO, 'docs/exemplo.md')
    print(f"Conteudo: {conteudo[:60]}...")

    # Listar diretorio
    itens = github_list_dir(OWNER, REPO, 'docs')
    for item in itens:
        print(f"  {item['name']} ({item['type']})")

    # Criar PR
    pr = github_create_pr(OWNER, REPO, 'Adiciona docs', 'PR de exemplo', 'feature/docs')
    print(f"PR criado: {pr['html_url']}")

    # Listar PRs
    prs = github_list_prs(OWNER, REPO)
    for p in prs:
        print(f"  #{p['number']} {p['title']} ({p['state']})")

    # Buscar template e modulo
    # tmpl = fetch_template('base_prompt.txt', OWNER, REPO)
    # mod = fetch_module('design.md', OWNER, REPO)
