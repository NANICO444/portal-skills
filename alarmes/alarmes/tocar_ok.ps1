# Toca alarme OK: alarme_curto.wav x 8 vezes
Add-Type -AssemblyName System.Windows.Forms
$path = Join-Path $PSScriptRoot "alarme_curto.wav"

if (-not (Test-Path $path)) {
    Write-Host "ERRO: $path nao encontrado"
    exit 1
}

$player = New-Object System.Media.SoundPlayer $path
1..8 | ForEach-Object {
    $player.PlaySync()
    Start-Sleep -Milliseconds 150
}
Write-Host "OK! Alarme curto x8 tocado"
