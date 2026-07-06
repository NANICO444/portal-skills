$alarmDir = Split-Path $PSCommandPath -Parent
$rcloneLog = "$env:USERPROFILE\Desktop\alarmes\upload_log.txt"
$maxRetries = 3
$retryCount = 0
$source = "C:\Users\User\Desktop\COISAS JOAO"
$dest = "meuDrive:COISAS_JOAO/bkp_20260627"

Write-Host "VIGIA CORUJA INICIADO - $(Get-Date)" | Out-File $rcloneLog -Append

while ($true) {
    $rclone = Get-Process rclone -ErrorAction SilentlyContinue
    if (-not $rclone) {
        $retryCount++
        Write-Host "[$(Get-Date)] rclone nao encontrado. Tentativa $retryCount/$maxRetries" | Out-File $rcloneLog -Append
        if ($retryCount -le $maxRetries) {
            Start-Process -WindowStyle Hidden -FilePath "rclone" -ArgumentList "sync", "`"$source`"", $dest, "--progress", "--stats-one-line", "--log-file", "$rcloneLog", "--log-level", "INFO", "--ignore-existing", "--transfers", "4", "--checkers", "8"
            Write-Host "[$(Get-Date)] rclone reiniciado (tentativa $retryCount)" | Out-File $rcloneLog -Append
            Start-Sleep -Seconds 30
        } else {
            Write-Host "[$(Get-Date)] ESGOTOU TENTATIVAS - TOCANDO ALARME" | Out-File $rcloneLog -Append
            Add-Type -AssemblyName System.Windows.Forms
            $player = New-Object System.Media.SoundPlayer (Join-Path $alarmDir "merda_eco.wav")
            1..2 | ForEach-Object { $player.PlaySync(); Start-Sleep -Milliseconds 300 }
            $retryCount = 0
        }
    } else {
        $retryCount = 0
    }
    Start-Sleep -Seconds 15
}
