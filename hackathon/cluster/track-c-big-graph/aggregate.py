"""
Track C, step 2: combine results/size_*.csv, print the table, plot scaling.
Run after the generate array finishes (see job_aggregate.sh).
"""

import glob
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd


def size_of(path):
    # results/size_100000.csv -> 100000
    return int(os.path.basename(path).split("_")[1].split(".")[0])


def main():
    files = sorted(glob.glob("results/size_*.csv"), key=size_of)
    if not files:
        raise SystemExit("no results/size_*.csv, did the generate array run?")

    df = pd.concat((pd.read_csv(f) for f in files), ignore_index=True).sort_values("n")
    print(df.to_string(index=False))

    os.makedirs("figs", exist_ok=True)

    # How does the hub (max degree) grow with n?
    fig, ax = plt.subplots(figsize=(4, 3))
    ax.loglog(df["n"], df["max_degree"], "o-")
    ax.set_xlabel("n")
    ax.set_ylabel("max degree")
    ax.set_title("Hub size vs n", loc="left")
    fig.tight_layout()
    fig.savefig("figs/max_degree_vs_n.png", dpi=150, bbox_inches="tight")

    # How does the cost of generating grow with n?
    fig2, ax2 = plt.subplots(figsize=(4, 3))
    ax2.loglog(df["n"], df["gen_seconds"], "o-")
    ax2.set_xlabel("n")
    ax2.set_ylabel("generate seconds")
    ax2.set_title("Runtime vs n", loc="left")
    fig2.tight_layout()
    fig2.savefig("figs/runtime_vs_n.png", dpi=150, bbox_inches="tight")

    print("wrote figs/max_degree_vs_n.png and figs/runtime_vs_n.png")


if __name__ == "__main__":
    main()
