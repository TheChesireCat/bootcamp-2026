# Track 2: Extend your Session 1 work 🟡

**For:** anyone who did a cluster track this morning · **Est. time:** ~55 min · **Tool:** Claude Code / Desktop

## Goal
Take the Session 1 cluster track you ran (A parallel-sim, B GNN, or C big-graph) and
**extend it** with the agent. Measure the speed-up, and practice the discipline: a good
`CLAUDE.md`, plan-first, and verifying the agent's claims (especially on the cluster).

## What's in this folder
| File | Use |
| --- | --- |
| `CLAUDE.template.md` | starter memory file preloaded with the Explorer cluster facts, copy to `CLAUDE.md` |
| `PROMPTS.md` | one concrete extension prompt per Session 1 track, plus a debug prompt |

## Pick your extension (based on the track you did)
- **From Track A (parallel-sim):** turn the 1-D sweep into a **2-D sweep** (two parameters),
  index the array into a grid, and aggregate into a heatmap.
- **From Track B (GNN):** **sweep architectures/hyperparameters** (GCN vs GraphSAGE vs GAT,
  or hidden size) as a small array job and compare accuracy.
- **From Track C (big-graph):** add an **`igraph` implementation** and compare speed/memory
  vs networkx, or push the size ladder higher and right-size `--mem`.

## Steps
1. **Copy `CLAUDE.template.md` to `CLAUDE.md`** in your Session 1 track folder and edit the top line.
2. **Pick the prompt** for your track in `PROMPTS.md`. Ask for a plan first.
3. **Scope to one verifiable outcome.** Let it work in small diffs; review `git diff`.
4. **Verify on the cluster yourself:** `sbatch --test-only` first, then read the real job log.
   Don't accept "it works" without seeing `squeue`/output.
5. **Note what it got wrong** and how you caught it.

## Checklist to reinforce
- [ ] Concrete done-criteria written down before starting
- [ ] I dry-ran the batch file (`sbatch --test-only`) before a real submit
- [ ] I verified results by reading the actual job output, not the agent's word
- [ ] No secrets or credentials in prompts

## If you didn't do a cluster track
Pick any Session 1 starter folder from the repo and extend it the same way, or point the
agent at a paper's code repo and reproduce a figure.
