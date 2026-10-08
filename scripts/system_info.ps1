Write-Host "=== Windows System Information ===" -ForegroundColor Cyan

$computer = Get-CimInstance Win32_ComputerSystem
$os = Get-CimInstance Win32_OperatingSystem

Write-Host "Hostname : $($computer.Name)"
Write-Host "OS       : $($os.Caption)"
Write-Host "Version  : $($os.Version)"
Write-Host "RAM      : $([math]::Round($computer.TotalPhysicalMemory / 1GB, 2)) GB"

Write-Host "`nNetwork:"
Get-NetIPAddress -AddressFamily IPv4 |
    Where-Object {$_.IPAddress -notlike "127.*"} |
    Select-Object InterfaceAlias, IPAddress |
    Format-Table -AutoSize
