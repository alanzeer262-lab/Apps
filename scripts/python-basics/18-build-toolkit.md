# PyLearn Video 18 — Build: Reusable Analysis Toolkit

**Voice lock — mandatory:** Kendrick; ElevenLabs v3; exact approved Kendrick voice ID; no substitution/preset; same voice throughout.
**Source:** `Pylearn-build260/content/python-basics/modules/18-build-toolkit.md`
**Target:** 5–7 minutes.

### Scene 1 — When a project grows
**Visual:** Show a large block of repeated analysis code, then mark the two distinct jobs: average_score and top_scorer.
**Narration:** “As a project grows, one large block of code becomes harder to understand and change. We don't need to turn every line into a function. Instead, look for a clear job that deserves a name and can be reused.”

### Scene 2 — Average function
**Visual:** Build `average_score(scores)` returning the average; explicitly handle an empty list using a chosen return rule consistent with the project.
**Narration:** “The average_score function receives scores and returns their average. The caller doesn't need to know every step inside the function; it only needs to know what input it expects and what result it returns. We also define what happens for an empty list.”

### Scene 3 — Top scorer function
**Visual:** Build `top_scorer(records)` over name/score tuples; show output for Ada, Lin, Sam. Handle empty records deliberately.
**Narration:** “The top_scorer function answers a different question. It scans records and returns the learner with the highest score, following our chosen empty-case rule. Each function has one clear responsibility.”

### Scene 4 — Test and reflect
**Visual:** Call both functions with normal data, one record, and empty data; show results.
**Narration:** “Test each function independently. Try several records, then one record, then no records. A reusable function is easier to test because its job is narrow.”
**Narration:** “Ask yourself: which function from your project would be useful in a completely different program? That's a good sign that you have found a reusable piece of logic.”
**Hold:** 4 seconds.

### Recap
**Narration:** “A useful function has a clear input, a clear job, a useful return value, and a deliberate edge-case rule. Don't create functions just for the sake of it—create them when the name makes the program easier to understand. Next, we'll handle imperfect scores safely.”
