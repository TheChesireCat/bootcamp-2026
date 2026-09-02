# Track A: Parallel simulations 🟢

**Difficulty:** beginner · **Est. time:** ~50 min · **Compute:** CPU (`short`, the default partition)

## Goal
Use a **Slurm job array** to run many independent simulations at once, then
aggregate them into one figure. Start from a working ER-graph example and make it
*your own* experiment.

## What's in this folder
| File | What it does |
| --- | --- |
| `sim.py` | one array task = one `p`; simulates ER graphs, writes `results/p_<value>.csv` |
| `job_sim.sh` | Slurm array (`--array=1-11`) that runs `sim.py` in parallel |
| `plot.py` | reads all CSVs, averages over trials, writes `figs/avg_degree_vs_p.png` |
| `job_plot.sh` | Slurm job that runs `plot.py` after the array finishes |

## Prerequisites
- Connected to Explorer (`ssh explorer`), and the `bootcamp` conda env from the speed-run
  (`module load anaconda3` ▸ `conda create -n bootcamp python=3.11 networkx numpy pandas matplotlib`).

## Steps
1. **Read `sim.py`.** Find the `P_VALUES` sweep and the `measure()` function.
2. **Edit `job_sim.sh`**, put your email in `--mail-user` (or delete those two lines).
3. **Run the array:**
   ```bash
   sbatch job_sim.sh
   watch -n 1 squeue --me      # Ctrl-C when all tasks show CD/complete
   ls results/                 # p_0.0.csv ... p_1.0.csv
   ```
4. **Plot:**
   ```bash
   sbatch job_plot.sh
   ls figs/                    # avg_degree_vs_p.png
   ```
5. **Sanity check:** the mean degree should track the theory line **k̄ = p (n − 1)**.

## Ideas: what could you study?
Each idea fits the same pattern: **sweep one parameter across the array, measure one
property, average over trials, plot.** Pick whatever you find interesting.

1. **Giant component emerges (percolation).** Generator: ER. Sweep mean degree
   `c = p(n-1)` from 0 to ~4. Measure the size of the largest connected component
   (fraction of nodes). Look for the sharp jump right at `c = 1`, the classic phase transition.

2. **Small-world crossover.** Generator: Watts-Strogatz (`nx.watts_strogatz_graph(n, k, beta)`).
   Sweep the rewiring probability `beta` from 0 to 1 (log-spaced). Measure clustering `C`
   and average shortest path `L`. Look for the window where `L` collapses but `C` is still high.

3. **Scale-free structure.** Generator: Barabási-Albert (`nx.barabasi_albert_graph(n, m)`).
   Sweep `m` (edges per new node). Measure the max degree, the degree-distribution slope,
   or degree assortativity. Compare the heavy tail against an ER graph with the same mean degree.

4. **Robustness to failure vs attack.** Fix one graph type. Sweep the fraction of nodes removed
   (0 to 0.9). Measure the largest-component size after removing nodes **randomly** vs
   **highest-degree-first**. Scale-free networks shrug off random loss but shatter under targeted attack.

5. **Epidemic threshold.** Run a simple SIR spread on the graph. Sweep the infection probability.
   Measure the final outbreak size (fraction ever infected). Look for the threshold below which
   outbreaks fizzle and above which they take off.

6. **Does the world get smaller?** Fix the graph model. Sweep `n` (100, 300, 1000, 3000, ...).
   Measure the average shortest path length. See whether it grows like `log n`.

> Ideas 1-3 and 6 use metrics that are cheap and already close to the starter code.
> Ideas 4-5 need a little extra code (node removal / a spreading loop), good if you want a challenge.

## Make it yours (implementation hints)
- Change the sweep: edit `P_VALUES` in `sim.py` (rename it to whatever you're sweeping), and set
  `--array=1-<count>` in `job_sim.sh` to match the number of values.
- Change the generator: swap `nx.erdos_renyi_graph` for `nx.barabasi_albert_graph`,
  `nx.watts_strogatz_graph`, `nx.configuration_model`, ...
- Change the metric: add to the `measure()` function (largest-component size with
  `len(max(nx.connected_components(G), key=len))`, path length, assortativity, ...).
- Plot the right column: point `plot.py` at whatever metric you measured.
- Bump `N_NODES` / `N_TRIALS` and compare array wall-clock vs. running everything serially.

## Stretch
- Make it a **2-D sweep** (two parameters), extend the array and index into a grid.
- Limit concurrency with `--array=1-11%4` and watch how the queue changes.

> ℹ️ If you instead adapt Minami's original repo (`github.com/mu373/hpc-introduction`),
> note its batch files use `--partition=express`, which is **retired**, change it to `short`.
