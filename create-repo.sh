#!/usr/bin/env bash
set -euo pipefail

REPO="voice-cloning"
OWNER="standardgalactic"
DESCRIPTION="An experiment in reproducing my own speaking voice with Hume AI, demonstrated through a short narration of my research frameworks."

FILES=(
  "README.md"
  "my-research-frameworks-script.txt"
  "my-research-frameworks.mp3"
)

# Verify prerequisites.
command -v git >/dev/null || {
  echo "Error: git is not installed."
  exit 1
}

command -v gh >/dev/null || {
  echo "Error: GitHub CLI is not installed."
  exit 1
}

gh auth status >/dev/null || {
  echo "Error: Authenticate using gh auth login."
  exit 1
}

# Verify project files.
for file in "${FILES[@]}"; do
  if [[ ! -f "$file" ]]; then
    echo "Missing file: $file"
    exit 1
  fi
done

# Initialize the repository if necessary.
if [[ ! -d .git ]]; then
  git init -b main
fi

git branch -M main

# Stage only the project files.
git add -- "${FILES[@]}"

if ! git diff --cached --quiet; then
  git commit -m "Add narration"
fi

# Create the GitHub repository if it doesn't exist.
if ! gh repo view "$OWNER/$REPO" >/dev/null 2>&1; then
  gh repo create "$OWNER/$REPO" \
    --public \
    --description "$DESCRIPTION"
fi

# Configure the remote.
REMOTE="git@github.com:$OWNER/$REPO.git"

if git remote get-url origin >/dev/null 2>&1; then
  git remote set-url origin "$REMOTE"
else
  git remote add origin "$REMOTE"
fi

# Publish.
git push -u origin main

echo
echo "Repository published:"
echo "https://github.com/$OWNER/$REPO"
