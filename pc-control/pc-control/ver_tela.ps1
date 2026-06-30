# pc-control: VER TELA - diagnostico completo do que esta acontecendo
# O agente "ve" a tela atraves de: processos, janelas, cursor, clipboard + screenshot
# Uso: .\ver_tela.ps1

Add-Type -AssemblyName System.Drawing
Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName UIAutomationClient

$output = "$env:USERPROFILE\Desktop\screenshot_$(Get-Date -Format 'yyyyMMdd_HHmmss').png"
$outputSmall = "$env:USERPROFILE\Desktop\screenshot_thumb_$(Get-Date -Format 'yyyyMMdd_HHmmss').jpg"

# 1. CAPTURAR TELA
$bounds = [System.Windows.Forms.Screen]::PrimaryScreen.Bounds
$bitmap = New-Object System.Drawing.Bitmap $bounds.Width, $bounds.Height
$graphics = [System.Drawing.Graphics]::FromImage($bitmap)
$graphics.CopyFromScreen($bounds.Location, [System.Drawing.Point]::Empty, $bounds.Size)
$graphics.Dispose()
$bitmap.Save($output, [System.Drawing.Imaging.ImageFormat]::Png)

Write-Host "=============================="
Write-Host "  VISAO DO AGENTE"
Write-Host "=============================="
Write-Host ""

# 2. JANELAS ABERTAS
Write-Host "=== JANELAS ABERTAS ==="
$windows = @()
$rootElement = [System.Windows.Automation.AutomationElement]::RootElement
$cond = New-Object System.Windows.Automation.PropertyCondition([System.Windows.Automation.AutomationElement]::IsEnabledProperty, $true)
$allElements = $rootElement.FindAll([System.Windows.Automation.TreeScope]::Subtree, $cond)
$seen = @{}
foreach ($elem in $allElements) {
    try {
        $name = $elem.Current.Name
        $ctrlType = $elem.Current.LocalizedControlType
        if ($name -and $name.Trim() -ne "" -and !$seen.ContainsKey($name)) {
            $seen[$name] = $true
            $isKeyboard = $elem.Current.IsKeyboardFocusable
            if ($isKeyboard) {
                Write-Host "  [ATIVO] $name ($ctrlType)" -ForegroundColor Green
            } else {
                Write-Host "  $name ($ctrlType)"
            }
            $windows += @{Nome=$name; Tipo=$ctrlType; Ativo=$isKeyboard}
        }
    } catch {}
}
Write-Host "Total: $($windows.Count) elementos de UI" -ForegroundColor Gray
Write-Host ""

# 3. PROCESSOS EM PRIMEIRO PLANO
Write-Host "=== PROCESSOS EM FOCO ==="
$fgProcess = Get-Process | Where-Object { $_.MainWindowTitle -ne "" } | Sort-Object StartTime -Descending | Select-Object -First 10
foreach ($p in $fgProcess) {
    Write-Host "  $($p.ProcessName) - '$($p.MainWindowTitle)' (PID $($p.Id))"
}
if ($fgProcess.Count -eq 0) { Write-Host "  (nenhum processo com janela)" }
Write-Host ""

# 4. CURSOR
Write-Host "=== CURSOR ==="
$cursor = [System.Windows.Forms.Cursor]::Position
$primary = [System.Windows.Forms.Screen]::PrimaryScreen
Write-Host "  Posicao: ($($cursor.X), $($cursor.Y))"
Write-Host "  Resolucao: $($primary.Bounds.Width)x$($primary.Bounds.Height)"
Write-Host "  Trabalho: $($primary.WorkingArea.Width)x$($primary.WorkingArea.Height)"
Write-Host ""

# 5. CLIPBOARD
Write-Host "=== CLIPBOARD ==="
try {
    if ([System.Windows.Forms.Clipboard]::ContainsText()) {
        $clipText = [System.Windows.Forms.Clipboard]::GetText()
        $clipPreview = if ($clipText.Length -gt 200) { $clipText.Substring(0, 200) + "..." } else { $clipText }
        Write-Host "  Texto: $clipPreview"
    } elseif ([System.Windows.Forms.Clipboard]::ContainsImage()) {
        Write-Host "  Imagem: sim"
    } elseif ([System.Windows.Forms.Clipboard]::ContainsFileDropList()) {
        $files = [System.Windows.Forms.Clipboard]::GetFileDropList()
        Write-Host "  Arquivos: $($files.Count) item(ns)"
        foreach ($f in $files) { Write-Host "    - $f" }
    } else {
        Write-Host "  Vazio"
    }
} catch { Write-Host "  (inacessivel)" }
Write-Host ""

# 6. DATA/HORA
Write-Host "=== SISTEMA ==="
Write-Host "  Data: $(Get-Date -Format 'dd/MM/yyyy HH:mm:ss')"
Write-Host "  Computador: $env:COMPUTERNAME"
$os = Get-CimInstance Win32_OperatingSystem
Write-Host "  OS: $($os.Caption)"
$uptime = (Get-Date) - $os.LastBootUpTime
Write-Host "  Uptime: $([math]::Floor($uptime.TotalDays))d $($uptime.Hours)h $($uptime.Minutes)m"
Write-Host ""

# 7. OCR via OCR engine
Write-Host "=== TEXTO NA TELA (OCR) ==="
$ocrExe = "C:\Users\User\Desktop\pc-control\ocr-engine\ocr-app.exe"
if (Test-Path $ocrExe) {
    $ocrTemp = "$env:TEMP\_ocr_vision.png"
    $bitmap.Save($ocrTemp, [System.Drawing.Imaging.ImageFormat]::Png)
    
    try {
        $output = & $ocrExe $ocrTemp 2>&1
        $stderr = $output | Where-Object { $_ -match '^OK:|^NOK:|^ERR:' }
        $text = $output | Where-Object { $_ -notmatch '^OK:|^NOK:|^ERR:' }
        
        if ($text -and $text.Trim() -ne "") {
            Write-Host "$($text -join "`n")"
            $words = ($text -join " " -split '\s+' | Where-Object { $_ -ne "" }).Count
            Write-Host "--- $words palavras reconhecidas ---" -ForegroundColor Gray
        } else {
            $errMsg = $stderr -join ", "
            if ($errMsg -match "no_text") { Write-Host "(nenhum texto na tela)" }
            else { Write-Host "(OCR: $errMsg)" }
        }
    } catch {
        Write-Host "(OCR: $($_.Exception.Message))"
    }
    Remove-Item $ocrTemp -Force -ErrorAction SilentlyContinue
} else {
    Write-Host "(OCR engine ausente. Compile com: dotnet publish C:\Users\User\Desktop\pc-control\ocr-app)"
}

$bitmap.Dispose()

Write-Host ""
Write-Host "=============================="
Write-Host "Screenshot: $output" -ForegroundColor Cyan
Write-Host "=============================="
