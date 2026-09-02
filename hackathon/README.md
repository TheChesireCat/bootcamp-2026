# Hackathon: choose your own adventure

Two sessions, each with a pick-a-track hackathon after the guided speed-run.

## Session 1: Networks on the Cluster (`cluster/`)
Everything runs on **Explorer**. The speed-run uses `00-hello/` (first single job) and
`track-a-parallel-sim/` (the guided array walkthrough). Then pick a track:

| Folder | Role | Difficulty | Compute |
| --- | --- | --- | --- |
| `cluster/00-hello/` | speed-run: your first `sbatch` | - | CPU |
| `cluster/track-a-parallel-sim/` | guided walkthrough + **Track A** | 🟢 beginner | CPU |
| `cluster/track-b-gnn-gpu/` | **Track B** | 🟡 intermediate | `gpu-short` |
| `cluster/track-c-big-graph/` | **Track C** | 🟡 intermediate | CPU |

## Session 2: Agentic Computing (`agentic/`)
Three projects, all built by driving an agent. Pick one:

| Track | Difficulty | Folder |
| --- | --- | --- |
| 1 · Dashboard website | 🟢 on-ramp | `agentic/track-1-dashboard/` |
| 2 · Extend your Session 1 work | 🟡 intermediate | `agentic/track-2-extend-session1/` |
| 3 · Recreate a paper | 🟡 intermediate | `agentic/track-3-recreate-paper/` |

## Every track folder has
- `README.md`, goal, difficulty, est. time, prerequisites, steps, stretch goals
- starter code that runs on Explorer as-is (correct partition, `module load`, conda env)

All five track folders have working starter code and step-by-step READMEs.
