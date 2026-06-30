# pc-control: mover mouse para X,Y
# Uso: .\mover_mouse.ps1 X Y
# Ex:  .\mover_mouse.ps1 500 300

param([int]$X, [int]$Y)

Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.Cursor]::Position = New-Object System.Drawing.Point($X, $Y)
Write-Host "Mouse movido para ($X, $Y)"
