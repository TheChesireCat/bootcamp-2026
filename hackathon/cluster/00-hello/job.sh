#!/bin/bash
#============ Slurm options ============
#SBATCH --job-name=hello-cluster
#SBATCH --partition=short           # default CPU partition (express is retired)
#SBATCH --time=0-00:05:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mail-user=YOUR_USERNAME@northeastern.edu
#SBATCH --mail-type=END
#======================================

module load anaconda3
source activate base                # hello_cluster.py has no dependencies

python3 hello_cluster.py
