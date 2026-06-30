# pc-control: helper para executar sequencia de acoes
# Uso: .\executar.ps1 -Passos @(
#     @{Acao="abrir"; Alvo="notepad.exe"},
#     @{Acao="esperar"; Segundos=2},
#     @{Acao="digitar"; Texto="Ola mundo!"}
# )

param(
    [array]$Passos,
    [string]$Arquivo
)

if ($Arquivo) {
    $Passos = Get-Content $Arquivo -Raw | ConvertFrom-Json
}

$dir = Split-Path $PSCommandPath -Parent

foreach ($passo in $Passos) {
    $acao = $passo.Acao
    Write-Host ">> $($passo.Acao)" -ForegroundColor Cyan
    
    switch ($acao) {
        "abrir" {
            & "$dir\abrir.ps1" $passo.Alvo
        }
        "mover" {
            & "$dir\mover_mouse.ps1" $passo.X $passo.Y
        }
        "clicar" {
            $args = @()
            if ($passo.Direito) { $args += "-Direito" }
            if ($passo.Duplo) { $args += "-Duplo" }
            & "$dir\clicar.ps1" @args
        }
        "digitar" {
            & "$dir\digitar.ps1" $passo.Texto
        }
        "tecla" {
            & "$dir\tecla.ps1" $passo.Tecla
        }
        "screenshot" {
            & "$dir\screenshot.ps1"
        }
        "arrastar" {
            & "$dir\arrastar.ps1" $passo.X1 $passo.Y1 $passo.X2 $passo.Y2
        }
        "esperar" {
            Start-Sleep -Seconds $passo.Segundos
        }
        "executar" {
            Invoke-Expression $passo.Comando
        }
    }
    
    if ($passo.Aguardar -and $passo.Aguardar -gt 0) {
        Start-Sleep -Milliseconds $passo.Aguardar
    } else {
        Start-Sleep -Milliseconds 300
    }
}

Write-Host "Sequencia concluida!" -ForegroundColor Green
