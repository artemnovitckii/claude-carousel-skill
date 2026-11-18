#!/usr/bin/env bash
# Links the /carousel skill into ~/.claude/skills/ so it shows up in Claude Code. Re-run after a git pull.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEST="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"
mkdir -p "$DEST"
for d in "$ROOT"/skills/*/; do
  name=$(basename "$d")
  if [ -e "$DEST/$name" ] && [ ! -L "$DEST/$name" ]; then
    echo "skip $name: $DEST/$name already exists and is not a link"
    continue
  fi
  ln -sfn "${d%/}" "$DEST/$name"
  echo "linked /$name"
done
command -v python3 >/dev/null || echo "note: /carousel needs python3 to render the slides"
echo "done. Open Claude Code and type /carousel <your topic>"
