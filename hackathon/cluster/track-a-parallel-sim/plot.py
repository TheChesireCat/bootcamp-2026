"""
Track A, step 2: read every results/p_*.csv, average over trials, and plot.

Run this AFTER the simulation array finishes (see job_plot.sh).
Produces figs/avg_degree_vs_p.png (and prints the summary table).
"""

import glob
import os

import matplotlib

matplotlib.use("Agg")  # no display on a compute node, save to file
import matplotlib.pyplot as plt
import pandas as pd


def load_all(results_dir="results"):
    files = sorted(glob.glob(os.path.join(results_dir, "p_*.csv")))
    if not files:
        raise SystemExit(f"no CSVs in {results_dir}/, did the simulation run?")
    return pd.concat((pd.read_csv(f) for f in files), ignore_index=True)


def main():
    df = load_all()

    # Average (and spread) over trials, per p.
    # CUSTOMIZE: plot avg_clustering, or whatever metric you added in sim.py.
    summary = (
        df.groupby("p")["avg_degree"]
        .agg(mean="mean", std="std")
        .fillna(0.0)
        .reset_index()
    )
    print(summary.to_string(index=False))

    os.makedirs("figs", exist_ok=True)
    fig, ax = plt.subplots(figsize=(4, 3))
    ax.errorbar(summary["p"], summary["mean"], yerr=summary["std"],
                fmt="o", capsize=3, label="mean ± SD")
    ax.set_xlabel("p")
    ax.set_ylabel(r"$\bar{k}$")
    ax.set_title("Average degree vs p", loc="left")
    ax.legend(loc="upper left", frameon=True)
    fig.tight_layout()
    out = os.path.join("figs", "avg_degree_vs_p.png")
    fig.savefig(out, dpi=150, bbox_inches="tight")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
