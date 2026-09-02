# Prompt cheat-sheet (Track 2: Extend Session 1)

Pick the prompt for the track you did. Plan first, verify on the cluster yourself.

## From Track A: make it a 2-D sweep
```
Here's my Track A folder (sim.py, job_sim.sh, plot.py, job_plot.sh). I want to sweep TWO
parameters instead of one and make a heatmap of the result.
Read the code first, then propose a plan: how to index the Slurm array into a 2-D grid, what
each task writes, and how plot.py aggregates into a heatmap. Follow CLAUDE.md.
Dry-run the array with `sbatch --test-only` before telling me it's ready.
```

## From Track B: sweep GNN architectures
```
Here's my Track B GNN code. I want to compare GCN vs GraphSAGE vs GAT (and a couple of hidden
sizes) as a small Slurm array job on gpu-short, and print a table of test accuracy per config.
Plan it first. Keep the CPU fallback working. Pin `--gres=gpu:v100-sxm2:1`.
```

## From Track C: add an igraph comparison
```
Here's my Track C code (networkx). Add an igraph implementation of the same generate+measure,
run both on the size ladder, and plot runtime networkx vs igraph. Plan first; keep results in CSV.
```

## Debug a failed job (any track)
```
This job failed. Here's the batch file and the error from the log:
<paste job.sh + logs/*.err>
Diagnose it and propose the smallest fix. Don't rewrite the whole script.
```

---

### Verify, don't trust
- "It runs" ▸ ask it to show `squeue --me` output or the actual job log.
- "Results look right" ▸ open the figure / diff the numbers yourself.
- After each step: `git diff` before you accept. Undo with `git checkout .` if it drifted.
- The agent sounds sure even when it's wrong. Your job is to catch it.
