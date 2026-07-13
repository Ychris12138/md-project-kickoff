# md-project-kickoff installer shim for Windows PowerShell.

function Install-MdProjectKickoff {
    param([string[]]$InstallerArgs = @())

    $ErrorActionPreference = "Stop"
    $repo = "Ychris12138/md-project-kickoff"
    $node = Get-Command node -ErrorAction SilentlyContinue
    if (-not $node) {
        Write-Error "md-project-kickoff: Node.js 18 or newer is required. Install from https://nodejs.org or with winget."
        exit 1
    }

    $nodeMajor = [int](& node -p "process.versions.node.split('.').shift()")
    if ($nodeMajor -lt 18) {
        Write-Error "md-project-kickoff: Node.js 18 or newer is required."
        exit 1
    }

    if ($PSCommandPath) {
        $here = Split-Path -Parent $PSCommandPath
        $localInstaller = Join-Path $here "bin\install.js"
        if (Test-Path $localInstaller) {
            & node $localInstaller @InstallerArgs
            exit $LASTEXITCODE
        }
    }

    $npx = Get-Command npx -ErrorAction SilentlyContinue
    if (-not $npx) {
        Write-Error "md-project-kickoff: npx is required; reinstall Node.js."
        exit 1
    }

    & npx -y "github:$repo" --install @InstallerArgs
    exit $LASTEXITCODE
}

Install-MdProjectKickoff -InstallerArgs $args
