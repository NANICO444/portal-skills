# pc-control: tecla especial (Enter, Tab, Esc, F1-F12, setas, etc)
# Uso: .\tecla.ps1 "{ENTER}"
# Ex:  .\tecla.ps1 "{TAB}"
# Ex:  .\tecla.ps1 "{ESC}"
# Ex:  .\tecla.ps1 "^c" (Ctrl+C)
# Ex:  .\tecla.ps1 "%{F4}" (Alt+F4)

param([string]$Tecla)

Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.SendKeys]::SendWait($Tecla)
Write-Host "Tecla enviada: $Tecla"
