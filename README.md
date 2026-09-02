# NetSI PhD Bootcamp 2026: Cluster & Agentic Computing

Materials for two Thursday sessions at the Network Science Institute PhD Bootcamp
(**Sep 2–4, 2026**, 101 Belvidere St, Room 134).

| Time (Thu Sep 3) | Session | This repo covers |
| --- | --- | --- |
| 10am–12pm | **Networks on the Cluster** | `slides/01-networks-on-the-cluster.md` + `hackathon/cluster/` |
| 2pm–4pm | **Agentic Computing** | `slides/02-agentic-computing.md` + `hackathon/agentic/` |

Instructors: Ankit Ramakrishnan, Minami Ueda.

Both sessions run **choose-your-own-adventure hackathon** style: a ~45-min guided
speed-run, then ~60 min where students pick a track, then lightning share-outs.

## Audience assumptions
- Comfortable with Python / notebooks.
- **New to** clusters, SSH, the terminal, Slurm, and coding agents.
- Agentic session is a three-project hackathon: dashboard website, extend Session 1 work, recreate a paper.

## Cluster note
We use **Explorer only**, login host `login.explorer.northeastern.edu`, OOD at
`ood.explorer.northeastern.edu`. Discovery has been retired, ignore any Discovery
references in the 2025 materials under `references/`. Sponsor storage: `/projects/netsi`
(sponsor: Daria Alekseeva). Students should request access **before** the session via
the ServiceNow form in the agenda PDF, then set up SSH, see **`SETUP.md`**.

**Verified on Explorer (2026-08-31):** the old `express` partition is gone, use `short`
(the default). GPU work goes to `gpu-short` (2h) / `gpu` (8h) with `--gres=gpu:1`. Do **not**
assume students have the `netsi_*` partitions; all materials target the general partitions.
See `CLAUDE.md` for the full verified partition/module/SSH reference.

## Building the slides

Slides are [Marp](https://marp.app/) Markdown in `slides/`, styled by
`themes/netsi.css` (NetSI blue/coral/green, matching the 2025 deck).

```bash
make setup   # one-time: installs marp-cli locally
make html    # ▸ dist/*.html  (self-contained, shareable)
make pdf     # ▸ dist/*.pdf
make watch   # live preview with hot reload
```

No global installs, everything runs through `npx`.

## Layout

```
slides/      Marp decks (one per session)
themes/      netsi.css Marp theme
assets/      logos, diagrams (SVG), screenshots referenced by slides
hackathon/   choose-your-own-adventure tracks + starter code
  cluster/   Session 1: parallel-sim, GNN-on-GPU, big-graph tracks
  agentic/   Session 2: dashboard, extend-session1, recreate-paper tracks
references/  Minami's 2025 deck, hpc-introduction code, 2026 agenda (read-only)
RESOURCES.md Session 1 handout: more GPUs (AICR, NAIRR), git, free platforms, CS learning
```

## Status
Both decks are complete and build; all hackathon tracks have starter code and step-by-step
READMEs. Remaining: set the real repo URL on the "Get the example code" slide, optional VS Code
screenshots, and a final layout polish pass.
