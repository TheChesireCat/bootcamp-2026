#!/bin/bash
# Sync the student-facing subset from dev to the `main` branch and push it.
# Assumes the slide PDFs already exist in dist/ (the `make release` target builds
# them first via the `pdf` prerequisite). Run from anywhere; paths are resolved
# relative to the repo root.
#
# main = README.md (student) + SETUP.md + RESOURCES.md + hackathon/ + slides/*.pdf
# It never touches the dev working tree (uses a throwaway git worktree on main),
# and it leaves main's curated README.md and .gitignore alone.
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$root"

pdf1="$root/dist/01-networks-on-the-cluster.pdf"
pdf2="$root/dist/02-agentic-computing.pdf"
for p in "$pdf1" "$pdf2"; do
  [ -f "$p" ] || { echo "error: $p not found. Run 'make pdf' first (or 'make release')."; exit 1; }
done

# Fresh worktree checked out on main (reset to origin/main).
git fetch -q origin main
wt="$(mktemp -d)"
trap 'git worktree remove --force "$wt" 2>/dev/null || true; rm -rf "$wt"' EXIT
git worktree add -q -B main "$wt" origin/main

# Sync the student subset into the worktree.
rsync -a --delete \
  --exclude='__pycache__' --exclude='logs/' --exclude='results/' --exclude='figs/' \
  "$root/hackathon" "$wt/"
cp "$root/SETUP.md" "$root/RESOURCES.md" "$wt/"
mkdir -p "$wt/slides"
cp "$pdf1" "$wt/slides/Networks-on-the-Cluster.pdf"
cp "$pdf2" "$wt/slides/Agentic-Computing.pdf"

# Commit + push only if something changed.
cd "$wt"
git add -A
if git diff --cached --quiet; then
  echo "main is already up to date, nothing to release."
else
  git commit -q -m "Release: sync hackathon materials and slides ($(date +%Y-%m-%d))"
  git push -q origin main
  echo "released to main: https://github.com/TheChesireCat/bootcamp-2026/tree/main"
fi
