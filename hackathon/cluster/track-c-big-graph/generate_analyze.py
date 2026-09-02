"""
Track C, one array task = one graph SIZE.

Slurm runs this several times in parallel (see job_biggraph.sh). Each task
generates one large graph, measures a few cheap structural properties, times
itself, and writes results/size_<n>.csv

The interesting part is scaling: how do the properties and the runtime/memory
change as n grows? Watch the biggest task, it may run out of memory.
"""

import os
import sys
import time

import networkx as nx
import numpy as np
import pandas as pd

# Node counts, one per array task. The last one is the stress test.
# CUSTOMIZE: add/remove sizes and match --array in job_biggraph.sh.
SIZES = [10_000, 30_000, 100_000, 300_000, 1_000_000]
M = 3  # Barabasi-Albert: edges added per new node


def measure(G):
    """Cheap properties only, so this stays fast even for big graphs.
    (Clustering and path length are expensive at scale, skip them here.)
    """
    degrees = np.fromiter((d for _, d in G.degree()), dtype=int)
    components = list(nx.connected_components(G))
    largest = max((len(c) for c in components), default=0)
    return {
        "n": G.number_of_nodes(),
        "m": G.number_of_edges(),
        "mean_degree": float(degrees.mean()),
        "max_degree": int(degrees.max()),
        "num_components": len(components),
        "largest_cc_frac": largest / G.number_of_nodes(),
    }


def run(task_id):
    n = SIZES[task_id - 1]
    print(f"[task {task_id}] generating BA graph with n={n}, m={M}")

    t0 = time.time()
    G = nx.barabasi_albert_graph(n, M)  # CUSTOMIZE: try fast_gnp_random_graph for components
    gen_seconds = time.time() - t0

    t1 = time.time()
    row = measure(G)
    row["gen_seconds"] = round(gen_seconds, 2)
    row["measure_seconds"] = round(time.time() - t1, 2)

    os.makedirs("results", exist_ok=True)
    out = os.path.join("results", f"size_{n}.csv")
    pd.DataFrame([row]).to_csv(out, index=False)
    print(f"[task {task_id}] {row} -> {out}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: python3 generate_analyze.py <SLURM_ARRAY_TASK_ID>")
    run(int(sys.argv[1]))
