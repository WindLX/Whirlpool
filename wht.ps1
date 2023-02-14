<#
.Synopsis
This PowerShell script will build the running environment automatically and run Python script to start conversion work.
.Description
This PowerShell script will build the running environment automatically and run Python script to start conversion work. The output file will be saved at .\whirlpool_result folder
.Parameter Path
The path of folder which storages your target pictures.
.Parameter IsHidden
Change the presentation form of work progress.
.Parameter Size
The size of output pictures, only effective when target type is ico. 
.Parameter RawType
The raw type of pictures, such as png jpg ico.
.Parameter TargetType
The target type of pictures, such as png jpg ico.
.Example
.\wht.ps1 -Path .\Download -IsHidden true -Size 128
#>

[CmdletBinding()]
Param(
    [string] $Path = ".\",
    [bool] $IsHidden = $false,
    [Int32] $Size = 256,
    [Parameter(Mandatory = $true)]
    [string] $RawType,
    [Parameter(Mandatory = $true)]
    [string] $TargetType
)

$CONFIG = Get-Content "settings.json" | ConvertFrom-Json
$WHIRLPOOL_PATH = $CONFIG.WhirlpoolPath
$WHIRLPOOL_ENV = Join-Path $WHIRLPOOL_PATH "whirlpool"
$ENV_ACTIVATE = Join-Path $WHIRLPOOL_ENV "Scripts\Activate.ps1"
$WHIRLPOOL_START = Join-Path $WHIRLPOOL_PATH "whirlpool_terminal.py"
$PIP_REQUIREMENTS = Join-Path $WHIRLPOOL_PATH "requirements.txt"
$IS_EXIST = (Test-Path $WHIRLPOOL_ENV)
$IS_EXIST_PILLOW = Join-Path $WHIRLPOOL_ENV "Lib\site-packages\Pillow*" | Test-Path
if ($IS_EXIST) {}
else {
    Write-Host "[INFO]" -NoNewline -ForegroundColor:Blue
    Write-Host " MAKE PYTHON ENVIRONMENT" -ForegroundColor:Green
    python -m venv $WHIRLPOOL_ENV
}
if ($IS_EXIST_PILLOW) {}
else {
    Invoke-Expression $ENV_ACTIVATE
    Write-Host "[INFO]" -NoNewline -ForegroundColor:Blue
    Write-Host " INSTALL PYTHON PACKAGES" -ForegroundColor:Green
    pip install -r $PIP_REQUIREMENTS
    deactivate
}
Invoke-Expression $ENV_ACTIVATE
python $WHIRLPOOL_START $Path $IsHidden $Size $RawType $TargetType
deactivate
