# Prompt cheat-sheet (Track 3: Recreate a paper)

Plan first, build in small steps, verify against `PAPER-NOTES.md`.

## 1. Plan the model
```
I want to reproduce a result from Ravasz & Barabasi, "Hierarchical Organization in Complex
Networks" (arXiv cond-mat/0206130). Read PAPER-NOTES.md in this folder.
Propose a plan to build the deterministic hierarchical network in Python with networkx:
the construction rule, how many levels, and how you'll represent the "central node". Don't
write code yet, just the plan, and flag anything ambiguous in the wiring.
```

## 2. Build the generator
```
Implement the builder as build_hierarchical(levels) returning a networkx Graph.
Start with levels=3 (125 nodes) so it's quick. Print node and edge counts. Small steps.
```

## 3. Reproduce the two figures
```
Now plot, saving PNGs:
  1) the degree distribution P(k) on log-log axes
  2) the clustering coefficient C(k) vs degree k on log-log axes
Run it and show me the numbers. What exponent do you get for P(k)?
```

## 4. Verify against the paper
```
The paper expects P(k) scale-free with exponent ~2.16 and C(k) ~ k^-1 (slope about -1).
Fit both slopes and tell me if they match. Then build a Barabasi-Albert graph of the same size
and plot its C(k) too, it should be roughly flat. Show both on one figure.
```

## 5. When something's off (paste it)
```
My C(k) doesn't look like a -1 slope. Here's the builder and the plot code:
<paste>
Is the construction wrong, or the measurement? Find the smallest fix.
```

---

### Verify, don't trust
- A "line" on a log-log plot is not enough, check the **slope** is near -1.
- Compare against the **BA baseline**; if BA also looks like your model, something's wrong.
- `git diff` before you accept each step. Undo with `git checkout .` if it drifted.
- The agent will sound confident about the physics. Check it against the paper yourself.
