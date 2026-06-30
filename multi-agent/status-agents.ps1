# status-agents.ps1 — Verifica estado dos servidores multi-agent
$MA = Split-Path $MyInvocation.MyCommand.Path -Parent

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   MULTI-AGENT SYSTEM — STATUS" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

# Check ports
$ports = @(
    @{Name="Agent 1 (north-mini-code)"; Port=3001; Dir="agent1-north"},
    @{Name="Agent 2 (gpt-oss-120b)"; Port=3002; Dir="agent2-gptoss"}
)

foreach ($p in $ports) {
    $test = Test-NetConnection -ComputerName 127.0.0.1 -Port $p.Port -WarningAction SilentlyContinue -InformationLevel Quiet
    $status = if ($test) { "ONLINE ✅" } else { "OFFLINE ❌" }
    Write-Host "`n$($p.Name): $status" -ForegroundColor $(if($test){"Green"}else{"Red"})
    Write-Host "  URL: http://127.0.0.1:$($p.Port)"
    
    # Check config exists
    $configPath = Join-Path $MA $p.Dir "opencode.json"
    if (Test-Path $configPath) {
        Write-Host "  Config: OK ($(($configPath | Get-Item).Length) bytes)"
    } else {
        Write-Host "  Config: MISSING" -ForegroundColor Red
    }
    
    # Check log files
    $logDir = Join-Path $MA $p.Dir
    $log = Join-Path $logDir "server.log"
    $err = Join-Path $logDir "server.err"
    if ((Test-Path $log) -and ((Get-Item $log).Length -gt 0)) {
        Write-Host "  Log: $(Get-Content $log -Tail 3 -ErrorAction SilentlyContinue | Out-String | Select -First 1)"
    }
}

# Check skills count
$skillsDir = Join-Path $MA ".opencode\skills"
if (Test-Path $skillsDir) {
    $count = (Get-ChildItem $skillsDir -Directory).Count
    Write-Host "`nSkills instaladas: $count" -ForegroundColor Yellow
}

# Check .omo/rules
$ruleFile = Join-Path $MA ".omo\rules\always-use-agents.md"
if (Test-Path $ruleFile) {
    Write-Host "Regra always-use-agents: OK" -ForegroundColor Yellow
}

# Quick test via curl if online
$auth = "opencode:b5fb90e2-06f0-4554-9657-73028cdb7ca7"
foreach ($p in $ports) {
    $test = Test-NetConnection -ComputerName 127.0.0.1 -Port $p.Port -WarningAction SilentlyContinue -InformationLevel Quiet
    if ($test) {
        try {
            $health = Invoke-WebRequest -Uri "http://127.0.0.1:$($p.Port)/health" -TimeoutSec 5 -ErrorAction Stop
            Write-Host "  Health: $($health.StatusCode) $($health.StatusDescription)"
        } catch {
            Write-Host "  Health: $($_.Exception.Message.Substring(0, [Math]::Min(80, $_.Exception.Message.Length)))"
        }
    }
}

Write-Host "`n========================================" -ForegroundColor Cyan
