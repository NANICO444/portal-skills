# stop-agents.ps1 - Para os servidores multi-agent
Write-Host "Parando servidores multi-agent..." -ForegroundColor Cyan

$ports = @(3001, 3002)
$stopped = $false

Get-CimInstance Win32_Process -Filter "Name='opencode-cli.exe'" | ForEach-Object {
    $cmd = $_.CommandLine
    foreach ($port in $ports) {
        if ($cmd -match "--port $port") {
            Write-Host "  Parando PID $($_.ProcessId) (porta $port)..." -ForegroundColor Yellow
            Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue
            Write-Host "  PID $($_.ProcessId) parado." -ForegroundColor Green
            $stopped = $true
        }
    }
}

if (-not $stopped) {
    Write-Host "  Nenhum servidor multi-agent rodando nas portas 3001/3002." -ForegroundColor Gray
}

Start-Sleep -Seconds 1
$remaining = $false
foreach ($port in $ports) {
    $test = Test-NetConnection -ComputerName 127.0.0.1 -Port $port -WarningAction SilentlyContinue -InformationLevel Quiet
    if ($test) {
        Write-Host "  Porta ${port}: AINDA RODANDO (problema)" -ForegroundColor Red
        $remaining = $true
    } else {
        Write-Host "  Porta ${port}: PARADA ok" -ForegroundColor Green
    }
}

if (-not $remaining) { Write-Host "`nTodos servidores parados." -ForegroundColor Green }
