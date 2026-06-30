# 🚨 ALARME DE MERDA - Eco + voz grave
# Toca o audio processado 2 vezes
$player = New-Object System.Media.SoundPlayer "$env:USERPROFILE\Desktop\merda_eco.wav"
1..2 | ForEach-Object { $player.PlaySync(); Start-Sleep -Millis 300 }
$player.Dispose()
