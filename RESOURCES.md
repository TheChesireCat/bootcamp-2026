# Resources: compute, git, and learning

A companion handout for **Session 1: Networks on the Cluster**. Keep this after the bootcamp: it collects
where to get more compute, how to level up your git and coding, and the best free ways to keep learning.

Slides point you here for the full lists. Everything below is a live link.

## Explorer and Northeastern compute

- [Explorer documentation (rc-docs)](https://rc-docs.northeastern.edu) ▸ the canonical reference for
  partitions, GPUs, modules, and job arrays.
- [Open OnDemand portal](https://ood.explorer.northeastern.edu) ▸ files, JupyterLab, and job monitoring
  in the browser.
- **Research Computing help:** email `rchelp@northeastern.edu` when a job is stuck or won't release nodes.
- This repo's `CLAUDE.md` has the verified 2026 cluster facts (partitions, GPU types, modules).

## Where to find more GPUs

Develop and debug on Explorer first, then scale out. In rough order of "closest to home":

- **[AICR: the AI Compute Resource](https://rc.northeastern.edu/aicr/)** ▸ the Massachusetts AI Hub
  cluster (Northeastern, BU, Harvard, MIT, UMass, Yale) at MGHPCC. Runs Slurm + Open OnDemand as an
  extension of Explorer, with ~248 NVIDIA B200 and ~152 RTX6000 Pro GPUs.
  - Docs: [docs.aicr.ai](https://docs.aicr.ai/)
  - Access is per-project: your **PI submits a** [Project Proposal](https://docs.google.com/forms/d/e/1FAIpQLSfg1Vj9NRbn2ViPNFsypAGaoQJoKkr-BCssXZhKtDcNTCVYRg/viewform).
    Test on Explorer, then do production runs on AICR.
- **[NAIRR Pilot](https://nairrpilot.org)** ▸ the NSF National AI Research Resource. Free, time-limited
  national GPU and cloud allocations for US researchers, educators, and students.
  See [current allocations and how to apply](https://nairrpilot.org/allocations).
- **Free notebooks with GPUs:**
  - [Google Colab](https://colab.research.google.com) ▸ free tier gives you a GPU session in the browser.
  - [Kaggle Notebooks](https://www.kaggle.com/code) ▸ a weekly quota of free GPU (and TPU) hours.
- **Cloud research credits:** Google Cloud, AWS, Microsoft Azure, NVIDIA, and Lambda all run academic or
  research-credit programs. Ask your advisor, or apply directly on each vendor's education page.
- **On-demand rentals (cheap, pay per hour):** [Lambda](https://lambda.ai),
  [RunPod](https://www.runpod.io), [Vast.ai](https://vast.ai). Read the pricing first, and note that your
  data leaves Northeastern's environment, so do not use these for restricted data.

## Free dev and notebook platforms

- [GitHub Codespaces](https://github.com/features/codespaces) ▸ a full VS Code dev environment in the
  browser (free monthly core-hours; more with the Student Pack below).
- [Google Colab](https://colab.research.google.com) and [Kaggle](https://www.kaggle.com/code) ▸ zero-setup
  Python notebooks.
- [Lightning AI Studios](https://lightning.ai) ▸ free cloud dev environments with GPU sessions.
- [Hugging Face Spaces](https://huggingface.co/spaces) ▸ host and share small ML apps and demos.
- [Binder](https://mybinder.org) ▸ turn any public repo of notebooks into a live, runnable environment.

## Git and GitHub: learn it well

- [Pro Git book](https://git-scm.com/book) ▸ the free, complete reference. Chapters 1-3 cover almost
  everything you need day to day.
- [Learn Git Branching](https://learngitbranching.js.org) ▸ interactive, visual, the fastest way to
  actually understand branches and merges.
- [Atlassian Git tutorials](https://www.atlassian.com/git) ▸ clear explanations of commands and workflows.
- [GitHub Docs](https://docs.github.com) and [GitHub Skills](https://skills.github.com) ▸ hands-on
  courses run by a bot in your own repo.
- [Oh Shit, Git!?!](https://ohshitgit.com) ▸ how to undo common mistakes. Swear-free mirror:
  [dangitgit.com](https://dangitgit.com).

## GitHub Student Developer Pack

If you have a Northeastern `.edu` email, verify as a student and get a large bundle of free tools:
[education.github.com/pack](https://education.github.com/pack).

- GitHub Copilot (free for verified students) and GitHub Pro.
- Cloud credits (for example Microsoft Azure) and 20+ partner offers.
- JetBrains IDEs (PyCharm, IntelliJ, and more), free domain registrations, and other developer tools.
- Benefits last about two years, and you can reapply to renew while still enrolled.

## Learn (and re-learn) computer science

Great universities publish their intro and graduate materials for free. A curated shortlist:

- [The Missing Semester of Your CS Education (MIT)](https://missing.csail.mit.edu) ▸ the practical skills
  courses skip: shell, git, editors, debugging. Start here.
- [MIT OpenCourseWare](https://ocw.mit.edu) ▸ full MIT course materials, from intro programming to grad
  topics.
- [Harvard CS50](https://cs50.harvard.edu) ▸ the classic, friendly intro to computer science.
- [Teach Yourself CS](https://teachyourselfcs.com) ▸ a curated self-study path through the nine core CS
  subjects, with the best book and lecture per topic.
- [Open Source Society University](https://github.com/ossu/computer-science) ▸ a free, complete CS degree
  path built from open courses.
- [UC Berkeley CS61A](https://cs61a.org) and [CMU 15-213 (CS:APP)](https://csapp.cs.cmu.edu) ▸ two of the
  most-recommended courses for foundations and systems.
- For ML specifically: [Stanford CS231n](https://cs231n.github.io) and [fast.ai](https://course.fast.ai).

## Network science

- [Network Science (Barabasi)](https://networksciencebook.com) ▸ the free online textbook.
- [PHYS 7332 Network Science Data book](https://asmithh.github.io/network-science-data-book) ▸ Python for
  network analysis at scale, by Alyssa Smith with Matteo Chinazzi, Qian Zhang, and Brennan Klein
  ([course page](https://brennanklein.com/phys7332-fall25)).
- [Minami Ueda's computation docs](https://minamiueda.com/docs) ▸ the notes behind the 2025 HPC session.
- Snippet manager [pet](https://github.com/knqyf263/pet) ▸ save Slurm and shell commands so you never
  retype them.
