#!/bin/bash
#============ Slurm options ============
#SBATCH --job-name=er-sim
#SBATCH --partition=short           # default CPU partition (express is retired)
#SBATCH --time=0-00:10:00
#SBATCH --array=1-11                # 11 tasks: one per p-value in sim.py
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=2G
#SBATCH --output=logs/sim_%a.out    # %a = array task id
#SBATCH --error=logs/sim_%a.err
#SBATCH --mail-user=YOUR_USERNAME@northeastern.edu
#SBATCH --mail-type=END,FAIL
#======================================

mkdir -p logs results figs

module load anaconda3
source activate bootcamp            # the env you built in the speed-run

echo "task ${SLURM_ARRAY_TASK_ID} starting on $(hostname)"
python3 sim.py "${SLURM_ARRAY_TASK_ID}"
echo "task ${SLURM_ARRAY_TASK_ID} done"
