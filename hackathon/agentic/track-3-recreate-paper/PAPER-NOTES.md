# Paper notes: hierarchical networks

**Paper:** E. Ravasz and A.-L. Barabási, *Hierarchical Organization in Complex Networks*,
Phys. Rev. E 67, 026112 (2003). arXiv: `cond-mat/0206130`
<https://arxiv.org/abs/cond-mat/0206130>

**Big idea:** real networks are both **scale-free** (a few big hubs) and **highly clustered**,
and these coexist because the network is built from modules nested inside larger modules. The
fingerprint of that hierarchy is a specific scaling law for clustering.

**Reference figures in this folder (from the paper):**
- `paper-fig1-construction.png` (Fig 1): the iterative construction N=5 (a) ▸ N=25 (b) ▸ N=125 (c). Build this.
- `paper-fig2-results.png` (Fig 2): the results to reproduce, (a) P(k), (b) C(k), (c) C(N).

## The deterministic hierarchical model (what to build)
An iterated construction that produces the effect cleanly:
- **Level 0:** a small fully connected cluster of 5 nodes; call one of them the central node.
- **Each step:** make **4 copies** of the current module, then connect the **peripheral nodes**
  of the 4 copies to the **central node** of the original module. The central node keeps
  accumulating links, so it becomes a hub.
- After `k` steps you have `5^k` nodes.

(There are minor wiring variants in the literature; read the paper for the exact rule. The two
target results below hold for the hierarchical construction regardless of small variations.)

## Target results to reproduce (these are the plots in `paper-fig2-results.png`)
1. **(a) Scale-free P(k):** a power law on a log-log plot.
   Expected exponent for this construction: **γ = 1 + ln5 / ln4 ≈ 2.16**.
2. **(b) Hierarchy signature C(k) ~ k⁻¹ (the money figure):** the clustering coefficient of a
   node as a function of its degree, slope ≈ -1 on a log-log plot.
   A plain Barabási-Albert graph does NOT show this (it's flat); that's the whole point.
3. **(c) Size-independent clustering C(N):** the average clustering stays roughly constant
   (~0.74) as the network grows, unlike a scale-free model where it decays with N.

## How to check you got it
- Plot P(k) log-log, fit the tail, exponent near ~2.1 to 2.2.
- Plot C(k) vs k log-log, slope near -1.
- Compare against a BA graph of the same size: BA is scale-free but C(k) is roughly flat.
- Grow the model (N = 5, 25, 125, 625, ...) and check average clustering barely moves.
