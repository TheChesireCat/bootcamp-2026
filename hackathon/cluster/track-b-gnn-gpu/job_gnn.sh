#!/bin/bash
#============ Slurm options ============
#SBATCH --job-name=gnn
#SBATCH --partition=gpu-short          # 2h GPU partition (general access)
#SBATCH --gres=gpu:v100-sxm2:1         # pin V100: abundant + always supported
#SBATCH --time=0-00:30:00
#SBATCH --cpus-per-task=2
#SBATCH --mem=16G
#SBATCH --output=logs/gnn_%j.out
#SBATCH --error=logs/gnn_%j.err
#SBATCH --mail-user=YOUR_USERNAME@northeastern.edu
#SBATCH --mail-type=END,FAIL
#======================================

mkdir -p logs data

module load anaconda3 cuda/12.1.1
source activate gnn                    # built by setup_env.sh

# Which GPU did we actually get? (name, memory, utilization)
nvidia-smi

python3 train_gnn.py --dataset Cora --device auto --epochs 200
