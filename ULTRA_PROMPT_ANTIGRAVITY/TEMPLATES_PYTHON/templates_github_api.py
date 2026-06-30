"""
Ultra Prompt v6.0 — Template: Operacoes GitHub via Maton Gateway
Uso: importar funcoes ou copiar/adaptar conforme necessidade da sessao.
"""

import urllib.request
import os
import json
import base64


MATON_KEY = os.environ.get('MATON_API_KEY', '')
GITHUB_BASE = 'https://gateway.maton.ai/github'


def _github_request(path, method='GET', data=None):
    """Request base para GitHub API."""
    url = f'{GITHUB_BASE}/{path}'
    encoded = json.dumps(data).encode('utf-8') if data else None
    req = urllib.request.Request(url, data=encoded, method=method)
    req.add_header('Authorization', f'Bearer {MATON_KEY}')
    req.add_header('Accept', 'application/vnd.github+json')
    if data:
        req.add_header('Content-Type', 'application/json')
    return json.load(urllib.request.urlopen(req))


# === REPOSITORIOS ===

def create_repo(name, description='', private=True):
    """
    Cria um repositorio. SEMPRE privado por padrao (regra de seguranca).

    Args:
        name: Nome do repositorio.
        description: Descricao.
        private: SEMPRE True (seguranca inegociavel).

    Returns:
        dict: Dados do repo criado (contém 'full_name', 'html_url').
    """
    data = {
        'name': name,
        'description': description,
        'private': True,  # FORCADO — nunca publico
        'auto_init': True
    }
    return _github_request('user/repos', 'POST', data)


def get_repo(owner, repo):
    """Retorna info do repositorio."""
    return _github_request(f'repos/{owner}/{repo}')


def list_repos(per_page=30):
    """Lista repositorios do usuario autenticado."""
    return _github_request(f'user/repos?per_page={per_page}&sort=updated')


# === ARQUIVOS ===

def read_file(owner, repo, path, ref=None):
    """
    Le um arquivo do repositorio.

    Args:
        owner: Dono do repo.
        repo: Nome do repo.
        path: Caminho do arquivo.
        ref: (Opcional) Branch ou commit SHA.

    Returns:
        tuple: (conteudo_decodificado, sha_do_arquivo)
    """
    url = f'repos/{owner}/{repo}/contents/{path}'
    if ref:
        url += f'?ref={ref}'
    result = _github_request(url)
    content = base64.b64decode(result['content']).decode('utf-8')
    return content, result['sha']


def create_file(owner, repo, path, content, message, branch=None):
    """
    Cria um arquivo novo no repositorio.

    Args:
        owner: Dono do repo.
        repo: Nome do repo.
        path: Caminho do arquivo.
        content: Conteudo do arquivo (string).
        message: Mensagem do commit.
        branch: (Opcional) Branch alvo.

    Returns:
        dict: Dados do commit.
    """
    data = {
        'message': message,
        'content': base64.b64encode(content.encode('utf-8')).decode('utf-8')
    }
    if branch:
        data['branch'] = branch
    return _github_request(f'repos/{owner}/{repo}/contents/{path}', 'PUT', data)


def update_file(owner, repo, path, content, message, sha, branch=None):
    """
    Atualiza um arquivo existente (requer SHA do arquivo atual).

    Args:
        owner: Dono do repo.
        repo: Nome do repo.
        path: Caminho do arquivo.
        content: Novo conteudo (string).
        message: Mensagem do commit.
        sha: SHA do arquivo atual (obtido via read_file).
        branch: (Opcional) Branch alvo.

    Returns:
        dict: Dados do commit.
    """
    data = {
        'message': message,
        'content': base64.b64encode(content.encode('utf-8')).decode('utf-8'),
        'sha': sha
    }
    if branch:
        data['branch'] = branch
    return _github_request(f'repos/{owner}/{repo}/contents/{path}', 'PUT', data)


def create_or_update_file(owner, repo, path, content, message, branch=None):
    """
    Cria ou atualiza um arquivo automaticamente.
    Tenta ler o arquivo primeiro; se existir, faz update com SHA correto.
    """
    try:
        _, sha = read_file(owner, repo, path, ref=branch)
        return update_file(owner, repo, path, content, message, sha, branch)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return create_file(owner, repo, path, content, message, branch)
        raise


def list_directory(owner, repo, path='', ref=None):
    """Lista arquivos em um diretorio do repositorio."""
    url = f'repos/{owner}/{repo}/contents/{path}'
    if ref:
        url += f'?ref={ref}'
    return _github_request(url)


# === COMMITS ===

def list_commits(owner, repo, per_page=10, path=None):
    """Lista commits recentes."""
    url = f'repos/{owner}/{repo}/commits?per_page={per_page}'
    if path:
        url += f'&path={path}'
    return _github_request(url)


# === BRANCHES ===

def list_branches(owner, repo):
    """Lista branches do repositorio."""
    return _github_request(f'repos/{owner}/{repo}/branches')


def create_branch(owner, repo, branch_name, from_branch='main'):
    """Cria uma branch nova a partir de outra."""
    # Pegar SHA da branch base
    ref = _github_request(f'repos/{owner}/{repo}/git/ref/heads/{from_branch}')
    sha = ref['object']['sha']

    # Criar nova branch
    data = {
        'ref': f'refs/heads/{branch_name}',
        'sha': sha
    }
    return _github_request(f'repos/{owner}/{repo}/git/refs', 'POST', data)


# === ISSUES ===

def create_issue(owner, repo, title, body='', labels=None):
    """Cria uma issue."""
    data = {'title': title, 'body': body}
    if labels:
        data['labels'] = labels
    return _github_request(f'repos/{owner}/{repo}/issues', 'POST', data)


def list_issues(owner, repo, state='open', per_page=10):
    """Lista issues."""
    return _github_request(f'repos/{owner}/{repo}/issues?state={state}&per_page={per_page}')


# === UTIL ===

def upload_multiple_files(owner, repo, files, base_message='Upload', branch=None):
    """
    Faz upload de multiplos arquivos de uma vez.

    Args:
        owner: Dono do repo.
        repo: Nome do repo.
        files: Dict {path: content} (ex: {'modules/design.md': '# Design...'})
        base_message: Prefixo da mensagem de commit.
        branch: (Opcional) Branch alvo.

    Returns:
        list: Lista de resultados de cada upload.
    """
    results = []
    for path, content in files.items():
        message = f'{base_message}: {path}'
        result = create_or_update_file(owner, repo, path, content, message, branch)
        results.append({'path': path, 'result': result})
    return results


# --- Exemplo de uso ---
if __name__ == '__main__':
    OWNER = 'usuario'
    REPO = 'ultra-prompt'

    # Criar repo (sempre privado)
    repo = create_repo('ultra-prompt', 'Ultra Prompt v6.0 modules')
    print(f"Repo criado: {repo['full_name']}")

    # Upload de arquivo
    create_or_update_file(OWNER, REPO, 'modules/test.md', '# Test', 'Add test module')

    # Ler arquivo
    content, sha = read_file(OWNER, REPO, 'modules/test.md')
    print(f"Conteudo: {content[:50]}... (SHA: {sha[:8]})")

    # Listar diretorio
    files = list_directory(OWNER, REPO, 'modules')
    for f in files:
        print(f"  {f['name']} ({f['type']})")

    # Upload em batch
    files = {
        'modules/design.md': '# Design Module\n...',
        'modules/data.md': '# Data Module\n...',
    }
    upload_multiple_files(OWNER, REPO, files, 'Setup: add modules')
