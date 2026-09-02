# Prompt cheat-sheet (Track 1: Dashboard)

Say what you want, give context, say when it's done. Copy, adapt, go.

## 1. Start the project (plan first)
```
Build a single-page static website (index.html, plain HTML + JS, no build step).
It loads network.json (keys: nodes[{id,degree}], links[{source,target}]) and shows:
  - the network drawn with vis-network (nodes sized by degree)
  - summary stats: node count, edge count, average degree, top 3 hubs
  - a degree-distribution bar chart
Use a CDN for any library. Plan it first, then build in small steps, don't write it all at once.
```

## 2. Run and check
```
How do I view it? (serve with python3 -m http.server if needed.) Walk me through opening it.
```

## 3. Iterate on look and feel
```
Color the highest-degree nodes differently, add a page title and a short caption,
and make the layout two columns: graph on the left, stats + histogram on the right.
```

## 4. When something breaks (paste it)
```
The graph area is blank and the console shows this:
<paste the browser console error>
What's wrong and what's the smallest fix?
```

## 5. Verify before you trust
```
Print the top 3 hubs and their degrees on the page. The hub "alice" should have degree 12,
count it from network.json to confirm the stats are right.
```

## 6. Wrap up
```
Add a one-line comment at the top explaining how to run it, then commit with a clear message.
```

---

### Habits that make the agent better
- One task at a time. Get the graph drawing before you add stats.
- Read the plan before you say yes.
- If it goes sideways, undo (`git checkout .`) and re-prompt instead of piling on fixes.
- You open the page and look at it yourself. "It works" is your call.
