# PyLearn Video 08 — Loops: for and while

**Voice lock — mandatory:** Kendrick; ElevenLabs v3; exact approved Kendrick voice ID; no substitution/preset; same voice throughout.
**Source:** `Pylearn-build260/content/python-basics/modules/08-loops.md`
**Target:** 7–8 minutes.

### Scene 1 — Repeat without copying
**Visual:** `names = ["Ada", "Lin", "Sam", "Omar"]`; show repetitive print lines briefly, then replace them with a for loop.
**Narration:** “If you have four learners, you could print every name manually. But what if you had four thousand? A loop lets you say: do this once for every item. The loop variable name refers to the current item.”
**Code:** `for name in names:` then indented `print(name)`; run and reveal all four names.

### Scene 2 — Accumulate a total
**Visual:** Start with `scores = [70, 95, 88, 60]`, `total = 0`, then loop with `total += score`; print total.
**Narration:** “An accumulator starts with a value and updates it as the loop visits each item. Here, total starts at zero. Each score is added to it. At the end, total is three hundred and thirteen. This pattern appears often in data work.”

### Scene 3 — Filter records
**Visual:** Build `passed = []`; loop through scores; if score >= 70, append it. Run and show `[70, 95, 88]`.
**Narration:** “A loop can also filter. Visit each score, test the rule, and keep only values that pass. The pattern is visit, test, keep. Later, you'll use the same reasoning with data-analysis tools.”

### Scene 4 — Loop over records
**Visual:** Show tuples for Ada, Lin, and Sam; then `for name, score in records:` and f-string output.
**Narration:** “A record can contain more than one field. Tuple unpacking gives each part a meaningful name. This is clearer than repeatedly reading numeric positions.”

### Scene 5 — while, break, continue
**Visual:** Show count 3 and a while loop that decrements; outputs 3, 2, 1. Then briefly demonstrate break on score 95 and continue to skip scores below 70.
**Narration:** “A while loop repeats as long as its condition stays true. Make sure something changes so the condition eventually becomes false, or the loop may run forever. Break stops a loop. Continue skips the rest of the current iteration. Use them when they make the logic clearer.”

### Scene 6 — Practice and recap
**Visual:** Show four learner records and tasks: print each learner, calculate total, count passes, print scores below 70.
**Narration:** “Your turn. Process these records with a loop. Add one more learner and predict how the totals and counts change.”
**Hold:** 4 seconds.
**Narration:** “Loops repeat work over items or while a condition is true. You can accumulate totals, filter collections, and unpack records. Next, we'll choose the right data structure for different kinds of information.”

## App practice handoff

**Visual:** End card showing the corresponding PyLearn lesson/exercise; do not show a completed solution.

**Narration:** "Open Lesson 8 in PyLearn and process the learner records yourself. Build the requested totals, counts, and filtered names, then add one record and check what changes."
