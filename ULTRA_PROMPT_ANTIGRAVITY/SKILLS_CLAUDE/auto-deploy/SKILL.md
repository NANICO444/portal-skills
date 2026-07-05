---
name: auto-deploy
description: "Skill de deploy automatico completo para publicar projetos (sites estaticos, React/Next.js, Python .exe, etc.) no GitHub Pages, Vercel ou Releases. Use quando precisar publicar ou fazer deploy de qualquer projeto na internet."
---

# SKILL: Deploy Automático Completo
# Use esta skill quando precisar publicar qualquer projeto na internet

---

## Quando Usar Esta Skill
- Publicar site estático (HTML/CSS/JS) no GitHub Pages
- Publicar app React/Next.js na Vercel
- Compilar Python para .exe e criar Release no GitHub
- Resolver problemas de hospedagem (banda, domínio, SSL)

## Protocolo de Deploy

### Para Sites Estáticos (GitHub Pages)

#### Passo 1: Preparar Arquivos
```bash
# Verificar tamanho total
du -sh ./pasta-do-site/

# Se > 50MB, otimizar:
# - Comprimir imagens (quality 80%)
# - Converter áudio para MP3 128kbps
# - Minificar CSS/JS
```

#### Passo 2: Criar Repositório
```bash
gh repo create NOME-DO-SITE --public --source=. --remote=origin
```

#### Passo 3: Push e Ativar Pages
```bash
git add .
git commit -m "Deploy inicial"
git push -u origin main
# Ativar Pages via API do GitHub ou Settings
gh api repos/USER/REPO/pages -X POST -f source='{"branch":"main","path":"/"}'
```

#### Passo 4: Verificar
```bash
# Aguardar 2 minutos e testar
curl -s -o /dev/null -w "%{http_code}" https://USER.github.io/REPO/
```

### Para Executáveis Python (PyInstaller + GitHub Releases)

#### Passo 1: Compilar
```bash
pyinstaller --onefile --windowed --name "MeuApp" --icon=icon.ico main.py
```

#### Passo 2: Testar
```bash
# Rodar o .exe gerado
./dist/MeuApp.exe
```

#### Passo 3: Criar Release
```bash
gh release create v1.0 "./dist/MeuApp.exe" \
  --title "MeuApp v1.0" \
  --notes "Primeira versão estável"
```

## Checklist Pré-Deploy
- [ ] Todos os links internos funcionam
- [ ] Imagens carregam corretamente
- [ ] CSS/JS não tem erros no console
- [ ] Responsivo em mobile
- [ ] .gitignore configurado (excluir __pycache__, .venv, node_modules)
- [ ] README.md com instruções claras

## Resolução de Problemas
| Problema | Solução |
|----------|---------|
| Banda esgotada (Netlify) | Migrar para GitHub Pages |
| Arquivo > 100MB | Usar Git LFS ou Google Drive |
| 404 no GitHub Pages | Verificar se o branch está correto |
| CORS bloqueando API | Adicionar headers no servidor |
| .exe bloqueado pelo antivírus | Assinar digitalmente ou usar --onedir |
