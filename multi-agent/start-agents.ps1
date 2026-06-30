# start-agents.ps1 - Inicia os dois servidores multi-agent
$MA = Split-Path $MyInvocation.MyCommand.Path -Parent
$opencode = "C:\Users\User\AppData\Local\OpenCode\opencode-cli.exe"

$pwd = "b5fb90e2-06f0-4554-9657-73028cdb7ca7"
[Environment]::SetEnvironmentVariable("OPENCODE_SERVER_PASSWORD", $pwd, "User")
$env:OPENCODE_SERVER_PASSWORD = $pwd
Write-Host "OPENCODE_SERVER_PASSWORD set" -ForegroundColor Green

$servers = @(
    @{Name="Agent 1 (north-mini-code)"; Port=3001; ConfigDir=Join-Path $MA "agent1-north"}
    @{Name="Agent 2 (gpt-oss-120b)"; Port=3002; ConfigDir=Join-Path $MA "agent2-gptoss"}
)

foreach ($s in $servers) {
    Write-Host "`nIniciando $($s.Name) na porta $($s.Port)..." -ForegroundColor Cyan

    $log = Join-Path $s.ConfigDir "server.log"
    $err = Join-Path $s.ConfigDir "server.err"

    try {
        Start-Process -NoNewWindow -FilePath $opencode -ArgumentList @('serve','--hostname','127.0.0.1','--port',$($s.Port.ToString())) -WorkingDirectory $s.ConfigDir -RedirectStandardOutput $log -RedirectStandardError $err
        Write-Host "  Iniciado (log: $log)" -ForegroundColor Green
    } catch {
        Write-Host "  ERRO: $_" -ForegroundColor Red
    }
}

Write-Host "`nAguardando servidores iniciarem..." -ForegroundColor Yellow
Start-Sleep -Seconds 5

$online = $true
foreach ($s in $servers) {
    $test = Test-NetConnection -ComputerName 127.0.0.1 -Port $s.Port -WarningAction SilentlyContinue -InformationLevel Quiet
    if ($test) {
        Write-Host "$($s.Name): ONLINE ok" -ForegroundColor Green
    } else {
        Write-Host "$($s.Name): OFFLINE (verifique logs)" -ForegroundColor Red
        $online = $false
    }
}

if ($online) {
    Write-Host "`nSistema pronto!" -ForegroundColor Cyan
} else {
    Write-Host "`nVerifique os logs em cada agent*/server.err" -ForegroundColor Yellow
}
