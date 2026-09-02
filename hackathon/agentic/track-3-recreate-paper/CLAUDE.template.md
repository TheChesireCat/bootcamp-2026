# CLAUDE.md (starter, edit me)

Copy this to `CLAUDE.md` in your project folder. The agent reads it every session.

## Project
- Reproduce a result from a network science paper (see PAPER-NOTES.md).
- Stack: Python 3.11, networkx, numpy, matplotlib.

## How to run
- `python3 hierarchical.py` (builds the model and saves the P(k) and C(k) plots).

## Conventions
- Show me a plan before writing the generator; the wiring rule is easy to get subtly wrong.
- Small steps: builder first, then each plot. Run after every change and show me the numbers.
- Don't claim a result matches the paper until you've fit the slope and compared to a BA baseline.
- Keep it to a couple of small files; no heavy dependencies.
