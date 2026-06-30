---
name: pc-control
description: "CONTROLE FISICO DO PC — move mouse, clica, digita, abre programas, captura tela. O agente controla seu PC em tempo real via PowerShell. Nao instala nada."
user-invocable: true
allowed-tools: Read, Bash
---

# 🖥️ PC Control — O Agente Mexe no Seu PC

> **O OpenCode controla fisicamente seu computador.**
> Move mouse, clica, digita, abre programas, captura tela.
> Tudo via PowerShell nativo — sem instalar nada.

## ⚠️ SEGURANCA

- O agente SO executa os comandos que vc pedir
- Nada é instalado
- Tudo é via PowerShell nativo do Windows
- Vc VE o que está acontecendo na tela
- Para parar: feche a janela ou Ctrl+C

---

## 📂 LOCAL DOS SCRIPTS

`C:\Users\User\Desktop\pc-control\`

## 📋 COMANDOS DISPONIVEIS

| Comando | Descricao | Exemplo |
|---------|-----------|---------|
| `abrir.ps1 "programa"` | Abre programa/arquivo/URL | `abrir.ps1 "notepad.exe"` |
| `mover_mouse.ps1 X Y` | Move cursor para posicao | `mover_mouse.ps1 500 300` |
| `clicar.ps1` | Clica esquerdo | `clicar.ps1` |
| `clicar.ps1 -Direito` | Clica direito | `clicar.ps1 -Direito` |
| `clicar.ps1 -Duplo` | Duplo clique | `clicar.ps1 -Duplo` |
| `digitar.ps1 "texto"` | Digita texto | `digitar.ps1 "Ola mundo"` |
| `tecla.ps1 "{ENTER}"` | Tecla especial | `tecla.ps1 "{TAB}"` |
| `screenshot.ps1` | Captura tela | `screenshot.ps1` |
| `arrastar.ps1 X1 Y1 X2 Y2` | Arrasta mouse | `arrastar.ps1 100 100 500 300` |
| `executar.ps1 -Passos @(...)` | Sequencia de acoes | (ver abaixo) |

## 🎯 EXEMPLOS

### Abrir bloco de notas e escrever
```
.\abrir.ps1 "notepad.exe"
Start-Sleep 2
.\digitar.ps1 "Ola, eu sou o OpenCode controlando seu PC!"
```

### Abrir calculadora
```
.\abrir.ps1 "calc.exe"
```

### Abrir site
```
.\abrir.ps1 "https://google.com"
```

### Clicar em coordenada especifica
```
.\mover_mouse.ps1 800 500
.\clicar.ps1
```

### Tirar screenshot
```
.\screenshot.ps1
```

### Sequencia completa (JSON)
```powershell
.\executar.ps1 -Passos @(
    @{Acao="abrir"; Alvo="notepad.exe"},
    @{Acao="esperar"; Segundos=2},
    @{Acao="digitar"; Texto="Ola, eu sou o OpenCode!"},
    @{Acao="screenshot"}
)
```

---

## 🧠 COMO O AGENTE USA

Quando vc pedir algo como "abre o bloco de notas e escreve 'teste'", o agente:

1. Identifica o programa (notepad.exe)
2. Executa: `C:\Users\User\Desktop\pc-control\abrir.ps1 "notepad.exe"`
3. Espera 2 segundos
4. Executa: `C:\Users\User\Desktop\pc-control\digitar.ps1 "teste"`

Tudo em tempo real, vc ve acontecendo na tela.

---

## 🔧 TECLAS ESPECIAIS (SendKeys)

| Tecla | Codigo |
|-------|--------|
| Enter | `{ENTER}` |
| Tab | `{TAB}` |
| Esc | `{ESC}` |
| Backspace | `{BACKSPACE}` ou `{BS}` |
| Delete | `{DELETE}` ou `{DEL}` |
| Setas | `{UP}`, `{DOWN}`, `{LEFT}`, `{RIGHT}` |
| Home | `{HOME}` |
| End | `{END}` |
| F1-F12 | `{F1}` ... `{F12}` |
| Ctrl+C | `^c` |
| Alt+F4 | `%{F4}` |
| Ctrl+Shift+Esc | `^+{ESC}` |
| Win+R | `^{ESC}`r ou `#r` |
