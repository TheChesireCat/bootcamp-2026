#!/bin/bash
# One-time setup: build the conda env for the GNN track on Explorer.
# Run this on the login node (or inside an interactive session). Takes a few minutes.
set -e

module load anaconda3 cuda/12.1.1

conda create -y -n gnn python=3.11
source activate gnn

# PyTorch built for CUDA 12.1 (matches the cuda/12.1.1 module we load at run time).
# This wheel is large; the download takes a minute or two.
pip install torch --index-url https://download.pytorch.org/whl/cu121

# PyTorch Geometric. The pure-Python install is enough for a basic GCN.
pip install torch_geometric

echo
echo "sanity check:"
python3 -c "import torch; print('torch', torch.__version__, 'cuda available:', torch.cuda.is_available())"
echo "env 'gnn' ready. Submit with: sbatch job_gnn.sh"
