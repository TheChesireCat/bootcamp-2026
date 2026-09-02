# Track C: Big-graph generate & analyze 🟡

**Difficulty:** intermediate · **Est. time:** ~50 min · **Compute:** CPU (`short`, watch `--mem`)

## Goal
Use a Slurm array to generate large networks at several sizes, measure structural
properties, and study how things **scale** with `n`, including runtime and memory.

## What's in this folder
| File | What it does |
| --- | --- |
| `generate_analyze.py` | one array task = one size; generates a BA graph, measures properties, writes `results/size_<n>.csv` |
| `job_biggraph.sh` | Slurm array (`--array=1-5`) over the sizes, deliberately modest `--mem` |
| `aggregate.py` | combines CSVs, prints the table, plots max-degree-vs-n and runtime-vs-n |
| `job_aggregate.sh` | Slurm job that runs `aggregate.py` |

## Prerequisites
- Connected to Explorer, and the `bootcamp` conda env from the speed-run (networkx, numpy, pandas, matplotlib).

## Steps
1. **Read `generate_analyze.py`.** Note the `SIZES` ladder and the cheap-only `measure()`.
2. **Edit `job_biggraph.sh`** email (or delete the `--mail-*` lines).
3. **Run the array:**
   ```bash
   sbatch job_biggraph.sh
   watch -n 1 squeue --me
   ls results/                 # size_10000.csv ... (however many finished)
   ```
4. **Expect the biggest task to struggle.** The 1M-node task may hit the memory limit
   and show up as `FAILED` / `OUT_OF_MEMORY`. Read `logs/gen_5.err`, then:
   ```bash
   sbatch --array=5 --mem=16G job_biggraph.sh   # rerun just the big one with more memory
   ```
5. **Aggregate + plot:**
   ```bash
   sbatch job_aggregate.sh
   ls figs/                    # max_degree_vs_n.png, runtime_vs_n.png
   ```

## What to look for
- **Hub growth:** in a scale-free (BA) graph the max degree grows with `n` (a power law).
- **Runtime scaling:** generation time vs `n` on a log-log plot, roughly linear in edges.
- **Memory:** the reason the big task fails, and how much `--mem` it actually needs.

## Make it yours
- Swap the generator: `nx.fast_gnp_random_graph(n, c/n)` (sparse ER) to study the
  **giant component** as mean degree crosses 1 (then `num_components` / `largest_cc_frac` get interesting).
- Add a metric to `measure()` that stays cheap at scale (degree assortativity, density).
- Push the ladder higher and find where each size needs which `--mem` / `--time`.
- Compare `networkx` vs `igraph` generation speed for the same sizes.
