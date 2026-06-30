# pc-control: capturar screenshot da tela inteira
# Uso: .\screenshot.ps1
# Saida: C:\Users\User\Desktop\screenshot_AAAAMMDD_HHmmss.png

Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

$path = "$env:USERPROFILE\Desktop\screenshot_$(Get-Date -Format 'yyyyMMdd_HHmmss').png"
$bounds = [System.Windows.Forms.Screen]::PrimaryScreen.Bounds
$bitmap = New-Object System.Drawing.Bitmap $bounds.Width, $bounds.Height
$graphics = [System.Drawing.Graphics]::FromImage($bitmap)
$graphics.CopyFromScreen($bounds.Location, [System.Drawing.Point]::Empty, $bounds.Size)
$bitmap.Save($path)
$graphics.Dispose()
$bitmap.Dispose()

Write-Host "Screenshot salva: $path"
