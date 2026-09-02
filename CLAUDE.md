# CLAUDE.md: working conventions for this repo

This repo holds slides and hackathon materials for two NetSI Bootcamp 2026 sessions.
Read `README.md` first for the schedule and audience.

## Git (STRICT)
- **Never add Claude / AI attribution to git.** No `Co-Authored-By: Claude`, no "Generated with
  Claude", no AI mention in commit messages, PR bodies, or author/committer fields. Write plain,
  human commit messages describing the change only.
- Branches: `dev` = full working repo; `main` = student-facing subset (hackathon + SETUP +
  RESOURCES + README + slide PDFs). Do real work on `dev`; sync the student files to `main`.

## Writing style (STRICT)
- **NEVER use em dashes (`—`) anywhere in this project.** Not in slides, READMEs, code
  comments, commit messages, or docs. This is a hard rule to avoid AI-tell writing.
  Use a colon, a comma, parentheses, or two sentences instead.
- Also avoid en dashes (`–`) except inside genuine numeric ranges (e.g. `40-80 GB` is fine
  with a hyphen; prefer the hyphen).
- **For "leads to / see" arrows use the triangle `▸` (U+25B8), never `→`.** Applies to slides
  and docs (e.g. `simulate ▸ plot`, `▸ hackathon/cluster/...`).
- Keep prose plain and direct. No filler, no "it's worth noting", no over-hedging.

## Slides (Marp)
- Decks live in `slides/*.md`, one file per session. Build with `make html` / `make pdf`.
- Every deck starts with front-matter that sets `theme: netsi` and `paginate: true`.
- Slides are separated by `---` on its own line.
- Use theme utilities from `themes/netsi.css`:
  - Title slide: `<!-- _class: title -->`
  - Section divider: `<!-- _class: divider -->`
  - Hands-on marker: `<span class="pill">Hands-on Session</span>` in the heading area.
  - Emphasis: `*coral text*` renders coral+bold (not italic), this is intentional.
  - Big stats: `<span class="stat">1,024</span>`.
- Reference images as `../assets/...` (relative to `slides/`). Keep images in `assets/`.
- Match the 2025 deck's voice: short bold blue titles, one idea per slide, big code blocks,
  minimal prose. See `references/minami2025_Introduction to High-Performance Computing.pdf`.

## Cluster facts: VERIFIED on Explorer 2026-08-31 (students copy-paste these)
Source: live `sinfo`/`scontrol`/`sbatch --test-only` on explorer-02 + rc-docs.northeastern.edu.

- Login host: **`login.explorer.northeastern.edu`** (canonical; verified working). Some materials
  say `explorer.northeastern.edu`, prefer the `login.` form to match the docs + SSH-key setup.
- OOD: `https://ood.explorer.northeastern.edu`
- Docs: `https://rc-docs.northeastern.edu`, connecting: `/connectingtocluster/`,
  GPU: `/gpus/`, job arrays: `/runningjobs/`.

### SSH config (we teach students to set this up so `ssh explorer` "just works")
Add to `~/.ssh/config`:
```
Host explorer
    HostName login.explorer.northeastern.edu
    User <your-nu-username>        # e.g. lastname.f  (verified example: ramakrishnan.ank)
    IdentityFile ~/.ssh/id_rsa
```
Then `ssh explorer`, and in VS Code Remote-SSH the host shows up as `explorer`.
Passwordless key setup (from rc-docs): `ssh-keygen -t rsa` (no passphrase) ▸
`ssh-copy-id -i ~/.ssh/id_rsa.pub <username>@login.explorer.northeastern.edu`
(rc-docs notes passwordless SSH is REQUIRED for GUI/OOD apps to launch cleanly).
- **`express` is RETIRED**, the 2025 deck/code use `--partition=express`; that now errors
  ("Partition express not found"). Use `short` instead.
- **Default partition = `short`** (2-day limit). If no `--partition`, you land here.

### Partitions to use in STUDENT materials (general access: do NOT assume netsi_*)
- **CPU work ▸ `short`** (2-day, `-p short` or just omit it).
- **GPU work ▸ `gpu-short`** (2h) or **`gpu`** (8h). `gpu-interactive` (2h) is the same nodes.
  These three partitions share the SAME physical hardware, pick by time limit / interactivity.
  - Interactive GPU: `srun -p gpu-interactive --gres=gpu:v100-sxm2:1 --cpus-per-task=2 --mem=10G -t 02:00:00 --pty /bin/bash`

### GPU types (verified 2026-08-31): request as `--gres=gpu:TYPE:N`
| TYPE | Card | Compute | VRAM | Count | Notes |
|------|------|---------|------|-------|-------|
| `v100-sxm2` | V100 SXM2 | 7.0 | 32 GB | ~43 | most abundant; solid; NO bf16/TF32/FlashAttn |
| `v100-pcie` | V100 PCIe | 7.0 | 16–32 GB | 8 | same caveats |
| `t4` | T4 | 7.5 | 16 GB | 4 | weak FP32, inference-grade |
| `a100` | A100 | 8.0 | 40–80 GB | 11 | bf16+TF32+FlashAttn, big mem |
| `h200` | H200 | 9.0 | 141 GB | 32 | needs recent CUDA 12.x + sm_90 PyTorch build |
- No `p100`/`k80` in general `gpu*` partitions (p100 is only in `courses-gpu`).
- **Recommendation for student materials:** pin **`--gres=gpu:v100-sxm2:1`** (abundant + universally
  supported + plenty for a GNN). Use `a100` if you need bf16/TF32/FlashAttention or big memory.
  Avoid bare `--gres=gpu:1` in the workshop (non-deterministic, may hand you a T4 or a busy card).
- **The "old GPU" gotcha to teach:** if PyTorch/CUDA don't match the card's compute capability you
  get `CUDA error: no kernel image is available for execution on the device` (build too new for an
  old card, or too old for H200/sm_90). Fix: match the `cuda/` module + a PyTorch built for it, or
  pin a different `--gres` type. V100 avoids this for beginners; H200 is the most likely to trip it.
- **`courses` / `courses-gpu`** exist (1-day) for class accounts, mention only if relevant.

### netsi_* partitions: DO NOT assume bootcamp students have access
`netsi_standard` (CPU), `netsi_gpu` (4×V100-SXM2/node), `netsi_largemem`, all 30-day limit,
tied to the NetSI sponsor account (`da.alekseeva`). Reference them ONLY as an optional
"if your sponsor gave you access" aside; never as the default in copy-paste blocks.

### Modules (verified present)
`anaconda3/2024.06`, `miniconda3/24.11.1`, `miniconda3/25.9.1`,
`cuda/12.1.1`, `cuda/12.3.0`, `cuda/12.8.0`, `cuda/13.2.0`, `cuDNN/9.10.2`.
- Env pattern: `module load anaconda3` ▸ `source activate <env>` (docs also show `conda activate`).
- GPU/DL env: `module load anaconda3/2024.06` + `module load cuda/12.1.1` (match your PyTorch build).

### Slurm cheat (verified)
- `sbatch job.sh` · `squeue --me` · `scancel <id>` · `sbatch --test-only ...` (dry-run, no queue)
- Interactive: `srun -p short --pty bash -i`
- Job arrays: `#SBATCH --array=1-N%K` (N tasks, ≤K concurrent), the core "embarrassingly
  parallel" pattern the cluster hackathon builds on.
- Don't hardcode `--account`; a student's default account differs (mine is a course account).
  General partitions work without an explicit account.

- **Explorer only.** Do NOT reintroduce Discovery (`login.discovery.neu.edu`), it's retired.

## Agent / Claude facts (for the agentic session)
- Access: `https://claude.northeastern.edu` ▸ SSO with NU credentials.
- Tools taught: Claude Code (CLI) + Claude Desktop. Mention Codex / opencode as alternatives.
- Best-practice themes to reinforce: a project `CLAUDE.md`, plan-before-edit, small verifiable
  diffs, managing context, and MCP in one breath.

## Hackathon materials
- Each track is a self-contained folder under `hackathon/<session>/` with its own `README.md`
  stating: goal, difficulty, est. time, prerequisites, and step-by-step + stretch goals.
- Starter code should run on Explorer as-is (correct partitions, `module load`, conda env).

## Don't
- Don't edit anything under `references/`, it's the source archive.
- Don't hard-code personal usernames/emails in committed starter code; use `YOUR_USERNAME` /
  `<username>` placeholders like the 2025 batch files do.
