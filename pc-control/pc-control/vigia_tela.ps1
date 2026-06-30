# pc-control: VIGIA DA TELA - monitoramento continuo
# Fica tirando screenshot + OCR a cada N segundos
# Uso: .\vigia_tela.ps1
# Para sair: Ctrl+C

param(
    [int]$Intervalo = 5,  # segundos entre cada "olhada"
    [int]$Rodadas = 0      # 0 = infinito
)

Write-Host "=========================================="
Write-Host "  VIGIA DA TELA ATIVADO"
Write-Host "  Olhando a tela a cada $Intervalo segundos"
if ($Rodadas -gt 0) { Write-Host "  Total de $Rodadas observacoes" }
Write-Host "  Ctrl+C para parar"
Write-Host "=========================================="
Write-Host ""

$count = 0
while ($true) {
    $count++
    Write-Host "[$(Get-Date -Format 'HH:mm:ss')] Observacao #$count" -ForegroundColor Cyan
    
    # Chama o script de visao
    & "$PSScriptRoot\ver_tela.ps1"
    
    Write-Host ""
    Write-Host "---"
    Write-Host ""
    
    if ($Rodadas -gt 0 -and $count -ge $Rodadas) {
        Write-Host "Observacoes concluidas ($Rodadas rodadas)." -ForegroundColor Green
        break
    }
    
    Start-Sleep -Seconds $Intervalo
}
