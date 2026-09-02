#!/bin/bash
#============ Slurm options ============
#SBATCH --job-name=biggraph
#SBATCH --partition=short
#SBATCH --time=0-00:30:00
#SBATCH --array=1-5                  # one task per size in generate_analyze.py
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G                     # deliberately modest: the 1M task may OOM.
#SBATCH --output=logs/gen_%a.out     # if a task fails, read this + the .err file,
#SBATCH --error=logs/gen_%a.err      # then bump --mem and resubmit that task.
#SBATCH --mail-user=YOUR_USERNAME@northeastern.edu
#SBATCH --mail-type=END,FAIL
#======================================

mkdir -p logs results figs

module load anaconda3
source activate bootcamp             # the env from the speed-run (networkx, numpy, pandas)

echo "task ${SLURM_ARRAY_TASK_ID} on $(hostname)"
python3 generate_analyze.py "${SLURM_ARRAY_TASK_ID}"
