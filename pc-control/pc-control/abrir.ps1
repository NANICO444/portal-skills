# pc-control: abrir programa ou arquivo
# Uso: .\abrir.ps1 "notepad.exe"
# Ex:  .\abrir.ps1 "calc.exe"
# Ex:  .\abrir.ps1 "C:\Windows\System32\notepad.exe"
# Ex:  .\abrir.ps1 "https://google.com"

param([string]$Alvo)

Start-Process $Alvo
Write-Host "Aberto: $Alvo"
