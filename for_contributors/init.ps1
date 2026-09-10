$scriptdir = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectdir = split-path -Parent $scriptdir
if(-not (Get-Command python -ErrorAction SilentlyContinue)) {
  Write-Host "python not installed"
  exit 1
}
python -m venv "$projectdir\.venv" & "$projectdir\.venv\scripts\python.exe" -m pip install -r "$scriptdir\requirements.txt"
