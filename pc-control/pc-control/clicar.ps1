# pc-control: clicar na posicao atual (botao esquerdo)
# Uso: .\clicar.ps1
# Opcoes: .\clicar.ps1 -Direito, .\clicar.ps1 -Duplo

param([switch]$Direito, [switch]$Duplo)

Add-Type -AssemblyName System.Windows.Forms

if ($Direito) {
    [System.Windows.Forms.SendKeys]::SendWait("{RIGHTCLICK}")
    Write-Host "Clique direito"
} elseif ($Duplo) {
    [System.Windows.Forms.SendKeys]::SendWait("{DOUBLECLICK}")
    Write-Host "Duplo clique"
} else {
    [System.Windows.Forms.SendKeys]::SendWait("{CLICK}")
    Write-Host "Clique esquerdo"
}
