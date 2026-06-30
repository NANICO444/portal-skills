# pc-control: digitar texto
# Uso: .\digitar.ps1 "texto aqui"
# Ex:  .\digitar.ps1 "Ola mundo!"

param([string]$Texto)

Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.SendKeys]::SendWait($Texto)
Write-Host "Digitado: $Texto"
