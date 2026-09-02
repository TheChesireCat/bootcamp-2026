"""
Track A, one array task = one parameter value.

Slurm runs this script 11 times in parallel (see job_sim.sh, --array=1-11).
Each run picks ONE probability p from the list below using its array task id,
simulates several ER graphs at that p, measures a couple of properties, and
writes one CSV: results/p_<value>.csv

>>> This is your starting point. Look for "CUSTOMIZE" to make it your own. <<<
"""

import os
import sys

import networkx as nx
import numpy as np
import pandas as pd

# The parameter we sweep. Task id 1 -> p=0.0, task id 2 -> p=0.1, ... id 11 -> p=1.0
P_VALUES = [i / 10.0 for i in range(11)]  # [0.0, 0.1, ..., 1.0]

# Fixed simulation settings. Kept small so each array task finishes in seconds;
# bump these once your pipeline works (that's the whole point of the cluster).
N_NODES = 300        # nodes per graph
N_TRIALS = 10        # repeat each p this many times (for error bars)


def measure(G):
    """Return a dict of properties for one graph.

    CUSTOMIZE: add/replace metrics here, clustering, largest component,
    average path length, assortativity, ... (keep them cheap-ish so the
    hands-on stays fast).
    """
    degrees = [d for _, d in G.degree()]
    return {
        "avg_degree": float(np.mean(degrees)),
        "avg_clustering": nx.average_clustering(G),
    }


def run(task_id):
    # Pick this task's parameter value.
    p = P_VALUES[task_id - 1]  # array ids are 1-based
    print(f"[task {task_id}] p={p:.1f}: running {N_TRIALS} trials of n={N_NODES}")

    rows = []
    for trial in range(N_TRIALS):
        # CUSTOMIZE: swap the generator (barabasi_albert_graph, watts_strogatz_graph, ...)
        G = nx.erdos_renyi_graph(n=N_NODES, p=p)
        row = {"p": p, "trial": trial, **measure(G)}
        rows.append(row)

    os.makedirs("results", exist_ok=True)
    out = os.path.join("results", f"p_{p:.1f}.csv")
    pd.DataFrame(rows).to_csv(out, index=False)
    print(f"[task {task_id}] wrote {len(rows)} rows -> {out}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: python3 sim.py <SLURM_ARRAY_TASK_ID>")
    run(int(sys.argv[1]))
