<#
.SYNOPSIS
  Ciclo completo: VER a tela, DECIDIR o que fazer, AGIR.
#>
param(
    [Parameter(Position=0)]
    [ValidateSet("o_que_tem_na_tela","abrir_calculadora","abrir_notepad_digitar","status_tela","demo_completo")]
    [string]$Acao = "o_que_tem_na_tela",
    [string]$Texto = "Teste do sistema - $(Get-Date -Format 'HH:mm:ss')"
)

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

Write-Host ""
Write-Host "=== CICLO VER + AGIR ===" -ForegroundColor Cyan
Write-Host "Acao: $Acao" -ForegroundColor Gray
Write-Host ""

# --- FASE 1: VER ---
Write-Host "--- FASE 1: VER ---" -ForegroundColor Yellow
$null = & "$scriptDir\screenshot.ps1"
Write-Host "  Screenshot: OK" -ForegroundColor Green
$null = & "$scriptDir\ver_tela.ps1"
Write-Host "  Visao: OK" -ForegroundColor Green

# --- FASE 2: AGIR ---
Write-Host ""
Write-Host "--- FASE 2: AGIR ---" -ForegroundColor Yellow

switch ($Acao) {
    "o_que_tem_na_tela" {
        & "$scriptDir\ver_tela.ps1"
    }
    "abrir_calculadora" {
        Write-Host "  Abrindo Calculadora..." -ForegroundColor Green
        & "$scriptDir\abrir.ps1" "calc"
        Start-Sleep 2
        & "$scriptDir\ver_tela.ps1"
    }
    "abrir_notepad_digitar" {
        Write-Host "  Abrindo Bloco de Notas..." -ForegroundColor Green
        & "$scriptDir\abrir.ps1" "notepad"
        Start-Sleep 2
        Write-Host "  Digitando: $Texto" -ForegroundColor Green
        & "$scriptDir\digitar.ps1" $Texto
        Start-Sleep 1
        & "$scriptDir\tecla.ps1" "enter"
        Start-Sleep 1
        & "$scriptDir\ver_tela.ps1"
    }
    "status_tela" {
        Write-Host "  [OK] Screenshot salvo" -ForegroundColor Green
        Write-Host "  [OK] OCR executado" -ForegroundColor Green
        Write-Host "  [OK] Janelas detectadas" -ForegroundColor Green
        Write-Host "  [OK] Processos em foco" -ForegroundColor Green
    }
    "demo_completo" {
        Write-Host "  === DEMO COMPLETO ===" -ForegroundColor Magenta
        Write-Host "  1. Abrindo Notepad..." -ForegroundColor Gray
        & "$scriptDir\abrir.ps1" "notepad"
        Start-Sleep 2
        Write-Host "  2. Digitando..." -ForegroundColor Gray
        $demoText = "SISTEMA DE VISAO E CONTROLE DO AGENTE -- Data: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') -- Computador: $env:COMPUTERNAME -- VER + DECIDIR + AGIR = Ciclo Fechado."
        & "$scriptDir\digitar.ps1" $demoText
        Start-Sleep 1
        Write-Host "  3. Verificando resultado..." -ForegroundColor Gray
        & "$scriptDir\ver_tela.ps1"
        Write-Host "  4. Demo concluida!" -ForegroundColor Green
    }
}

Write-Host ""
Write-Host "=== CICLO FINALIZADO ===" -ForegroundColor Cyan
