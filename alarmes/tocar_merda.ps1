# Toca alarme MERDA: merda_eco.wav x 2 vezes
Add-Type -AssemblyName System.Windows.Forms
$path = Join-Path $PSScriptRoot "merda_eco.wav"

if (-not (Test-Path $path)) {
    Write-Host "ERRO: $path nao encontrado"
    exit 1
}

$player = New-Object System.Media.SoundPlayer $path
1..2 | ForEach-Object {
    $player.PlaySync()
    Start-Sleep -Milliseconds 300
}
Write-Host "MERDA! Alarme eco x2 tocado"
