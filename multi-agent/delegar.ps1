# delegar.ps1 — Delega uma tarefa para um sub-agente específico
param(
    [Parameter(Mandatory=$true)]
    [string]$Agente,
    
    [Parameter(Mandatory=$true)]
    [string]$Tarefa
)

$MA = Split-Path $MyInvocation.MyCommand.Path -Parent
$Auth = "opencode:b5fb90e2-06f0-4554-9657-73028cdb7ca7"
$AuthB64 = [Convert]::ToBase64String([Text.Encoding]::ASCII.GetBytes($Auth))

# Agent port mapping
$agents = @{
    "code-reviewer" = 3001
    "testador" = 3001
    "debugger" = 3001
    "refatorador" = 3001
    "security-auditor" = 3001
    "otimizador" = 3001
    "pesquisador" = 3002
    "documentador" = 3002
    "arquiteto" = 3002
    "devops" = 3002
}

if (-not $agents.ContainsKey($Agente)) {
    Write-Host "ERRO: Agente '$Agente' nao reconhecido." -ForegroundColor Red
    Write-Host "Agentes disponiveis:" -ForegroundColor Yellow
    foreach ($k in $agents.Keys | Sort-Object) { Write-Host "  $k (porta $($agents[$k]))" }
    exit 1
}

$port = $agents[$Agente]
$agentName = if ($port -eq 3001) { "Agent 1 (north-mini-code)" } else { "Agent 2 (gpt-oss-120b)" }

Write-Host "Delegando para $Agente ($agentName, porta $port)..." -ForegroundColor Cyan
Write-Host "Tarefa: $Tarefa" -ForegroundColor Yellow
Write-Host ""

# Use opencode run --attach
$opencode = "C:\Users\User\AppData\Local\OpenCode\opencode-cli.exe"
$cmd = "& `"$opencode`" run --attach http://127.0.0.1:$port --agent $Agente --format json `"$Tarefa`" 2>&1"

Write-Host "Executando: opencode run --attach http://127.0.0.1:$port --agent $Agente" -ForegroundColor Gray
Write-Host ""

$result = Invoke-Expression $cmd
Write-Host $result

Write-Host ""
Write-Host "--- FIM DA DELEGAÇÃO ---" -ForegroundColor Cyan
