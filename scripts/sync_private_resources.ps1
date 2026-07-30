param(
    [switch]$ValidateOnly
)

$projectRoot = Split-Path -Parent $PSScriptRoot
$destinationRoot = Join-Path $projectRoot 'knowledge\private-resources'
$sources = @(
    @{ Id = 'stamping-2026-06-03'; Path = 'D:\6.3 冲压 已处理' },
    @{ Id = 'apex-batch-1'; Path = 'D:\3.12 APEX 第一批（已处理）' },
    @{ Id = 'apex-batch-2'; Path = 'D:\5.5 APEX 第二批（已处理）' },
    @{ Id = 'tiger-products'; Path = 'D:\5.6 3D TIGER 产品图（已处理）' },
    @{ Id = 'tiger-guangxi'; Path = 'D:\5.8 3D TIGER-广西-已处理' },
    @{ Id = 'tiger-metal-3d-printing'; Path = 'D:\6.3 3D TIGER-金属3D打印-已处理' },
    @{ Id = 'factory-images'; Path = 'D:\工厂图' },
    @{ Id = 'enterprise-knowledge'; Path = 'C:\企业知识（保密）' }
)

$missing = @()
foreach ($source in $sources) {
    if (-not (Test-Path -LiteralPath $source.Path -PathType Container)) {
        $missing += $source.Path
        continue
    }
    if ($ValidateOnly) {
        continue
    }
    $destination = Join-Path $destinationRoot $source.Id
    New-Item -ItemType Directory -Path $destination -Force | Out-Null
    Get-ChildItem -LiteralPath $source.Path -Force | ForEach-Object {
        Copy-Item -LiteralPath $_.FullName -Destination $destination -Recurse -Force
    }
}

if ($missing.Count -gt 0) {
    Write-Output 'MISSING_SOURCES'
    $missing | ForEach-Object { Write-Output "- $_" }
    exit 2
}

if ($ValidateOnly) {
    Write-Output 'PASS: all private resource sources are available'
} else {
    Write-Output "PASS: private resources synchronized to $destinationRoot"
}
