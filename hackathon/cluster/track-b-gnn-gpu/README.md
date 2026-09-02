# Track B: GNN on GPU 🟡

**Difficulty:** intermediate · **Est. time:** ~55 min
**Compute:** general **`gpu-short`** partition (CPU fallback works too)

## Goal
Train a graph neural network for node classification on an Explorer GPU, and see
what requesting/using a GPU actually looks like in Slurm.

## Cluster facts (verified 2026-08-31: general access, no netsi_* assumed)
- GPU partitions: **`gpu-short`** (2h) or **`gpu`** (8h). Interactive: `gpu-interactive` (2h).
  All three are the SAME nodes, pick by time limit / interactivity.
- Modules present: `anaconda3/2024.06`, `cuda/12.1.1`…`13.2.0`, `cuDNN/9.10.2`.
- Interactive smoke test:
  `srun -p gpu-interactive --gres=gpu:v100-sxm2:1 --cpus-per-task=2 --mem=10G -t 00:30:00 --pty bash`
  then `nvidia-smi`.

## Which GPU should I request?  ⭐ read this
You choose the card with `--gres=gpu:TYPE:1`. **Different cards need different software, and an
old card can silently break new code.** Request strings on `gpu-short`/`gpu`:

| Request string | Card | VRAM | When to use |
|---|---|---|---|
| **`--gres=gpu:v100-sxm2:1`** ⭐ | V100 SXM2 | 32 GB | **Default for this track**, most available, always works, plenty for a GNN |
| `--gres=gpu:a100:1` | A100 | 40–80 GB | If you need bf16 / TF32 / FlashAttention or big memory |
| `--gres=gpu:t4:1` | T4 | 16 GB | Tiny models / inference; weak for training |
| `--gres=gpu:h200:1` | H200 | 141 GB | Only if you know you need it, newest, needs recent CUDA + matching PyTorch |
| `--gres=gpu:1` | *any* | ⚠️ | ⚠️ Avoid, the scheduler may hand you a T4 or a busy card; not reproducible |

**The gotcha:** if your PyTorch/CUDA don't match the card you'll see
`CUDA error: no kernel image is available for execution on the device`, the build is too new for
an old card, or too old for the H200. **V100 avoids this**; the H200 is the most likely to trip it.
So: pin `v100-sxm2`, and load a matching CUDA module (`module load cuda/12.1.1`).

## Prerequisites
- Explorer access (GPU partitions are generally available; confirm you can `sbatch -p gpu-short`).
- conda env with PyTorch + PyTorch Geometric, build with the CUDA module above.

## Steps (to be fleshed out)
## What's in this folder
| File | What it does |
| --- | --- |
| `setup_env.sh` | one-time: builds the `gnn` conda env (PyTorch for CUDA 12.1 + PyTorch Geometric) |
| `train_gnn.py` | 2-layer GCN node classification; `--dataset`, `--device`, `--epochs` flags; prints the GPU it landed on |
| `job_gnn.sh` | Slurm job on `gpu-short` pinned to `--gres=gpu:v100-sxm2:1` |

## Steps
1. **Build the env once** (on the login node):
   ```bash
   bash setup_env.sh          # creates the 'gnn' env, a few minutes
   ```
2. **Read `train_gnn.py`.** It's a standard 2-layer GCN. Note the `--device` flag and
   the block that prints the GPU name + compute capability.
3. **Try it on CPU first** (tiny, no queue wait):
   ```bash
   module load anaconda3 && source activate gnn
   python3 train_gnn.py --dataset KarateClub --device cpu
   ```
4. **Edit `job_gnn.sh`** email, then submit the GPU run:
   ```bash
   sbatch job_gnn.sh
   watch -n 1 squeue --me
   ```
5. **Read `logs/gnn_<jobid>.out`:** the `nvidia-smi` header, the GPU name/capability line,
   and the test accuracy (Cora should reach ~0.8).
6. **Compare** GPU vs CPU wall-clock (`--device cpu` vs `--device auto`).

## Stretch goals
- Swap GCN for GraphSAGE / GAT; sweep `--hidden` as a small array job.
- Try a bigger dataset (`--dataset Pubmed`).
- Try an H200 (`--gres=gpu:h200:1 -p gpu`) and confirm the env still works (this is where a
  mismatched build would show the "no kernel image" error).

## Note on netsi_gpu
There is a dedicated `netsi_gpu` partition (V100s, 30-day limit) tied to the NetSI sponsor.
**Do not rely on it**, students may not have access. Everything here targets `gpu-short` / `gpu`.
