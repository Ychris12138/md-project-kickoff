#!/usr/bin/env bash

set -euo pipefail

REPO="Ychris12138/md-project-kickoff"

if ! command -v node >/dev/null 2>&1; then
  echo "md-project-kickoff: Node.js 18 or newer is required." >&2
  echo "Install it from https://nodejs.org or your system package manager." >&2
  exit 1
fi

NODE_MAJOR="$(node -p "process.versions.node.split('.').shift()")"
if [ "$NODE_MAJOR" -lt 18 ]; then
  echo "md-project-kickoff: Node.js 18 or newer is required." >&2
  exit 1
fi

HERE="$(cd "$(dirname "${BASH_SOURCE[0]:-}")" 2>/dev/null && pwd)" || HERE=""
if [ -n "$HERE" ] && [ -f "$HERE/bin/install.js" ]; then
  exec node "$HERE/bin/install.js" "$@"
fi

if ! command -v npx >/dev/null 2>&1; then
  echo "md-project-kickoff: npx is required; reinstall Node.js." >&2
  exit 1
fi

exec npx -y "github:$REPO" --install "$@"
