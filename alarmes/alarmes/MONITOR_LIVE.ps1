# MONITOR LIVE - Mostra progresso do upload a cada 30s
# Abra em uma janela separada para acompanhar ao vivo

$alarmDir = Split-Path $PSCommandPath -Parent
$oldObjects = 0
$staleCount = 0

Write-Host "=========================================="
Write-Host "  MONITOR DE UPLOAD - RCLONE"
Write-Host "  Atualizando a cada 30 segundos"
Write-Host "=========================================="
Write-Host ""

while ($true) {
    Clear-Host
    Write-Host "=========================================="
    Write-Host "  MONITOR DE UPLOAD - $(Get-Date -Format 'HH:mm:ss')"
    Write-Host "=========================================="
    Write-Host ""
    
    # Verifica se rclone esta rodando
    $rclone = Get-Process rclone -ErrorAction SilentlyContinue
    if ($rclone) {
        Write-Host "  RCLONE: RODANDO (PID $($rclone.Id))" -ForegroundColor Green
    } else {
        Write-Host "  RCLONE: PARADO" -ForegroundColor Red
    }
    
    # Pega stats do drive
    $driveInfo = rclone about meuDrive: --json 2>$null | ConvertFrom-Json
    if ($driveInfo) {
        $usedGB = [math]::Round($driveInfo.Used / 1GB, 1)
        $totalGB = [math]::Round($driveInfo.Total / 1GB, 1)
        $freeGB = [math]::Round($driveInfo.Free / 1GB, 1)
        $pctUsed = [math]::Round(($driveInfo.Used / $driveInfo.Total) * 100, 1)
        Write-Host "  DRIVE: $usedGB GB / $totalGB GB ($pctUsed%)" -ForegroundColor Cyan
    }
    
    # Pega stats do upload
    $uploadInfo = rclone size "meuDrive:projeto-master/" 2>$null
    if ($uploadInfo) {
        Write-Host "  UPLOAD: $uploadInfo" -ForegroundColor Yellow
    }
    
    # Log
    $logPath = "$env:USERPROFILE\Desktop\upload_rclone.log"
    if (Test-Path $logPath) {
        $lastLine = Get-Content $logPath -Tail 1
        Write-Host "  ULTIMO LOG: $lastLine" -ForegroundColor Gray
    }
    
    Write-Host ""
    Write-Host "  Pressione Ctrl+C para sair"
    Write-Host "=========================================="
    
    Start-Sleep -Seconds 30
}
