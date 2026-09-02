# CLAUDE.md (starter for cluster work, edit me)

Copy this to `CLAUDE.md` in your project. It teaches the agent the Explorer facts so
it writes Slurm scripts that actually run. Delete what doesn't apply, add your own.

## Project
- (one line: what this repo does)
- Stack: Python 3.11, conda env `bootcamp` (networkx, numpy, pandas, matplotlib).

## Cluster: Explorer (verified 2026)
- Login host `login.explorer.northeastern.edu`. Never compute on the login node; submit jobs.
- CPU work: `--partition=short` (default, up to 2 days). The old `express` partition is retired.
- GPU work: `--partition=gpu-short` (2h) with `--gres=gpu:v100-sxm2:1`. Pin the V100.
- Modules: `module load anaconda3` (then `source activate <env>`); `cuda/12.1.1` for GPU.
- Job arrays for parameter sweeps: `#SBATCH --array=1-N%K`.
- Do NOT use `netsi_*` partitions (may not have access). Do NOT hardcode `--account`.
- Commands: `sbatch job.sh`, `squeue --me`, `scancel <id>`, `sbatch --test-only ...` (dry run).

## Conventions
- Show me a plan before editing more than one file.
- Small diffs. After writing a Slurm script, dry-run it with `sbatch --test-only` before real submit.
- Verify claims: if you say a job ran, show me the `squeue`/output, don't assume.
- Use `YOUR_USERNAME` placeholders, never real emails or credentials.
