#!/bin/bash
#============ Slurm options ============
#SBATCH --job-name=er-plot
#SBATCH --partition=short
#SBATCH --time=0-00:05:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=2G
#SBATCH --output=logs/plot.out
#SBATCH --error=logs/plot.err
#SBATCH --mail-user=YOUR_USERNAME@northeastern.edu
#SBATCH --mail-type=END,FAIL
#======================================

mkdir -p logs figs

module load anaconda3
source activate bootcamp

python3 plot.py
