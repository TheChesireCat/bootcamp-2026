# Track 1: Dashboard website 🟢

**For:** anyone (great on-ramp if you're newer to coding) · **Est. time:** ~55 min · **Tool:** Claude Code / Desktop

## Goal
Build a small **static website** that visualizes a network: the graph itself, a few
metrics, and its degree distribution. You drive the agent; it writes the HTML/JS.
The point is the workflow (describe, plan, run, fix), not hand-writing web code.

## Deliverable
An `index.html` you can open in a browser that:
- draws the network (nodes sized by degree) with a JS graph lib (vis-network or D3)
- shows summary stats (node count, edge count, average degree, the top hubs)
- plots the degree distribution

## What's in this folder
| File | Use |
| --- | --- |
| `network.json` | ready-to-load graph (18 nodes, 35 links, each node has a `degree`) |
| `edges.csv` | the same graph as a raw edge list, if you'd rather parse CSV |
| `PROMPTS.md` | copy-paste prompt cheat-sheet for each step |
| `CLAUDE.template.md` | starter project memory file, copy to `CLAUDE.md` |

## Steps
1. **Make a folder**, copy `network.json` (and `CLAUDE.template.md` renamed to `CLAUDE.md`) into it.
2. **Open the agent** there and ask for a **plan** first (prompt #1 in `PROMPTS.md`). Read it.
3. **Build in small steps:** first get the graph drawing, then add stats, then the histogram.
   Open `index.html` in your browser after each step to check it.
4. **Iterate on look and feel** (prompt #3): color hubs, add a title, make it responsive.
5. **Verify** one number by hand (the hub `alice` has degree 12) so you trust the stats.
6. **Commit** when it works.

## Checklist to reinforce
- [ ] I read the plan before approving
- [ ] I opened the page in a browser and checked it myself
- [ ] I verified a stat by hand (hub degree)
- [ ] I kept changes small and committed often

## If you finish early
- Add a search box or a click-to-highlight-neighbors interaction.
- Swap in a bigger network (export one from your Session 1 Track A run) and see what breaks.

> Serve it with `python3 -m http.server` if your browser blocks loading `network.json` from `file://`.
