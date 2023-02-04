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
The size of output pictures, only effective when target type is ico 
.Parameter RawType
The raw type of pictures, such as png jpg ico 
.Parameter TargetType
The target type of pictures, such as png jpg ico 
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

$PYTHON_ENV = ".\whirlpool"
$PIP_REQUIREMENTS = "requirements.txt"
$IS_EXIST = (Test-Path $PYTHON_ENV)
if ($IS_EXIST) {}
else {
    python -m venv $PYTHON_ENV
    .\whirlpool\Scripts\Activate.ps1
    pip install -r $PIP_REQUIREMENTS
    deactivate
}
.\whirlpool\Scripts\Activate.ps1
python whirlpool_terminal.py $Path $IsHidden $Size $RawType $TargetType
deactivate
