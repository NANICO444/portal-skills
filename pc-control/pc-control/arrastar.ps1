# pc-control: arrastar mouse de (X1,Y1) ate (X2,Y2)
# Uso: .\arrastar.ps1 X1 Y1 X2 Y2
# Ex:  .\arrastar.ps1 100 100 500 300

param([int]$X1, [int]$Y1, [int]$X2, [int]$Y2)

Add-Type -AssemblyName System.Windows.Forms
Add-Type @"
using System;
using System.Runtime.InteropServices;
public class MouseDrag {
    [DllImport("user32.dll")]
    public static extern void mouse_event(uint dwFlags, uint dx, uint dy, uint dwData, int dwExtraInfo);
    public const uint MOUSEEVENTF_LEFTDOWN = 0x02;
    public const uint MOUSEEVENTF_LEFTUP = 0x04;
    public const uint MOUSEEVENTF_MOVE = 0x01;
}
"@

# Move pro inicio
[System.Windows.Forms.Cursor]::Position = New-Object System.Drawing.Point($X1, $Y1)
Start-Sleep -Milliseconds 100

# Aperta botao
[MouseDrag]::mouse_event([MouseDrag]::MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
Start-Sleep -Milliseconds 100

# Move pro fim (em passos)
$passos = 20
for ($i = 1; $i -le $passos; $i++) {
    $x = $X1 + (($X2 - $X1) * $i / $passos)
    $y = $Y1 + (($Y2 - $Y1) * $i / $passos)
    [System.Windows.Forms.Cursor]::Position = New-Object System.Drawing.Point([int]$x, [int]$y)
    Start-Sleep -Milliseconds 10
}

Start-Sleep -Milliseconds 100
# Solta botao
[MouseDrag]::mouse_event([MouseDrag]::MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

Write-Host "Arrastado de ($X1,$Y1) ate ($X2,$Y2)"
