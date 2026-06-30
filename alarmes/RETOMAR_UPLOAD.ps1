# RETOMAR UPLOAD - Forca retomada do sync rclone
# Uso: powershell -File "C:\Users\User\Desktop\alarmes\RETOMAR_UPLOAD.ps1"

$alarmDir = Split-Path $PSCommandPath -Parent
$source = "C:\Users\User\Desktop\COISAS JOAO\skills pastas melhorias agentes"
$dest = "meuDrive:projeto-master/"
$logFile = "$env:USERPROFILE\Desktop\upload_rclone.log"

Write-Host "=== RETOMAR UPLOAD ==="
Write-Host ""

# Mata rclone existente se estiver rodando
$existing = Get-Process rclone -ErrorAction SilentlyContinue
if ($existing) {
    Write-Host "rclone ja rodando (PID $($existing.Id)). Finalizando..."
    Stop-Process -Id $existing.Id -Force
    Start-Sleep -Seconds 2
    Write-Host "Finalizado."
}

Write-Host "Iniciando sync..."
Write-Host "Origem: $source"
Write-Host "Destino: $dest"
Write-Host "Log: $logFile"
Write-Host ""

# Inicia sync em background
Start-Process -WindowStyle Hidden -FilePath "rclone" -ArgumentList "sync", "`"$source`"", $dest, "--progress", "--log-file", $logFile

Start-Sleep -Seconds 3
$newProc = Get-Process rclone -ErrorAction SilentlyContinue
if ($newProc) {
    Write-Host "UPLOAD INICIADO (PID $($newProc.Id))" -ForegroundColor Green
    # Toca OK
    Add-Type -AssemblyName System.Windows.Forms
    $player = New-Object System.Media.SoundPlayer (Join-Path $alarmDir "alarme_curto.wav")
    1..8 | ForEach-Object { $player.PlaySync(); Start-Sleep -Milliseconds 150 }
} else {
    Write-Host "FALHA AO INICIAR UPLOAD" -ForegroundColor Red
}
