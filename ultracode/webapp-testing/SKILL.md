---
name: webapp-testing
description: "Anthropic webapp-testing - workflow Playwright para apps locais com scripts Python e helpers"
user-invocable: true
allowed-tools: Read, Bash, Write
---

# Webapp Testing (Anthropic)

## O que e

Workflow oficial Anthropic para **testes E2E com Playwright** em aplicacoes web locais. Inclui scripts Python e helpers de servidor.

## Quando usar

- Criar testes E2E para webapp
- Validar fluxo completo (UI + backend)
- Testar contra servidor local
- Regression testing visual

## Instalacao

```bash
# Via CLI de skills
npx skills add https://github.com/anthropics/skills --skill webapp-testing
```

## Git

- Repo: https://github.com/anthropics/skills
- Skill: https://github.com/anthropics/skills/tree/main/skills/webapp-testing

## Processo de uso (5 fases)

### 1. Setup
- Instalar Playwright
- Instalar browsers
- Configurar helpers

### 2. Subir servidor local
- Script Python para start/stop
- Aguardar ready
- Cleanup

### 3. Escrever testes
- Page Object Model
- Locators estaveis
- Assertions

### 4. Rodar
- Local: real browser
- CI: headless
- Screenshots/videos

### 5. Reportar
- HTML report
- Trace viewer
- CI artifacts

## Exemplo Python

```python
import pytest
from playwright.sync_api import sync_playwright

def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://localhost:3000/login")
        page.fill('input[name="email"]', "user@example.com")
        page.fill('input[name="password"]', "senha123")
        page.click('button[type="submit"]')
        page.wait_for_url("**/dashboard")
        assert page.title() == "Dashboard"
        browser.close()
```

## Prompt de exemplo

```
Crie testes E2E para a pagina de checkout:
- Adicionar produto ao carrinho
- Preencher endereco
- Escolher pagamento
- Confirmar pedido
- Verificar tela de sucesso

Use a skill webapp-testing com Playwright + Python.
```

## Boas praticas

- Usar `data-testid` para locators estaveis
- Esperar elementos visiveis, nao por tempo
- Limpar state entre tests
- Screenshots em falhas
- CI: rodar em paralelo

## Complementa

- `test-driven-development` (ja temos)
- `python-testing` (ja temos)
- `property-based-testing` (ja temos)
- `webapp-testing` adiciona E2E
