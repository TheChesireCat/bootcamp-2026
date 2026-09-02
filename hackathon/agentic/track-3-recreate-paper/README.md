# Track 3: Recreate a paper 🟡

**For:** anyone who likes a research challenge · **Est. time:** ~55 min · **Tool:** Claude Code / Desktop

## Goal
Use the agent to **rebuild the hierarchical network and make its main-result plots** from
Ravasz & Barabási, *Hierarchical Organization in Complex Networks* (PRE 2003, arXiv
`cond-mat/0206130`). You direct; the agent builds the model and the figures; you verify them
against the paper's plots (`paper-fig2-results.png`).

## The target: reproduce these three plots
Build the **deterministic hierarchical scale-free network** (`paper-fig1-construction.png`),
then reproduce the panels of Figure 2:
1. **(a)** a **scale-free** P(k) (log-log), exponent γ ≈ 2.16
2. **(b)** the hierarchy fingerprint **C(k) ~ k⁻¹** (clustering vs degree, slope ≈ -1)
3. **(c)** **size-independent** average clustering C(N) (~0.74, roughly flat as N grows)

See `PAPER-NOTES.md` for the construction and the numbers to check against. (Getting (a) and
(b) is a great result; (c) is the stretch.)

## What's in this folder
| File | Use |
| --- | --- |
| `paper-fig1-construction.png` | Fig 1: the network to build (N=5 ▸ 25 ▸ 125) |
| `paper-fig2-results.png` | Fig 2: the plots you're reproducing |
| `PAPER-NOTES.md` | the paper, the model construction, and the target numbers |
| `PROMPTS.md` | prompts to plan the model, build it, plot, and verify |
| `CLAUDE.template.md` | starter project memory file, copy to `CLAUDE.md` |

## Steps
1. **Read `PAPER-NOTES.md`** so you know what "correct" looks like.
2. **Copy `CLAUDE.template.md` to `CLAUDE.md`** in a fresh folder.
3. **Ask the agent to plan** the hierarchical construction before it writes code (prompt #1).
   Read the plan and sanity-check the wiring against the notes.
4. **Build in small steps:** first the graph builder, then P(k), then C(k). Run after each.
5. **Verify against the paper:** exponent near ~2.1 to 2.2, and C(k) slope near -1. Compare to a
   BA graph of the same size (BA should be flat in C(k)).
6. **Commit** when the two plots match the paper's behavior.

## Checklist to reinforce
- [ ] I read the target results before starting
- [ ] I checked the C(k) slope is near -1, not just "a line"
- [ ] I compared against a BA baseline
- [ ] I verified the numbers myself, didn't take the agent's word

## If you finish early
- Fit the power-law exponent properly and compare to γ = 1 + ln5/ln4.
- Try the stochastic hierarchical variant from the paper.
