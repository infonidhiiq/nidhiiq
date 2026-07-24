[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$url = "https://www.python.org/ftp/python/3.11.9/python-3.11.9-embed-amd64.zip"
$output = "python_embed.zip"
Write-Host "Downloading Python 3.11 embedded ZIP..."
Invoke-WebRequest -Uri $url -OutFile $output
Write-Host "Extracting Python..."
Expand-Archive -Path $output -DestinationPath "C:\Users\getsu\python_embed" -Force
Remove-Item $output -ErrorAction SilentlyContinue

# Download get-pip.py
$pipUrl = "https://bootstrap.pypa.net/get-pip.py"
Invoke-WebRequest -Uri $pipUrl -OutFile "C:\Users\getsu\python_embed\get-pip.py"

# Uncomment import site in python311._pth
$pthFile = "C:\Users\getsu\python_embed\python311._pth"
if (Test-Path $pthFile) {
    (Get-Content $pthFile) -replace '#import site', 'import site' | Set-Content $pthFile
}

Write-Host "Installing pip into C:\Users\getsu\python_embed..."
& "C:\Users\getsu\python_embed\python.exe" "C:\Users\getsu\python_embed\get-pip.py" --no-warn-script-location

Write-Host "Installing requirements..."
& "C:\Users\getsu\python_embed\python.exe" -m pip install fastapi uvicorn pydantic sqlalchemy jinja2 aiofiles httpx

Write-Host "Python environment ready!"
