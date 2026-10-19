# PyLearn Video 06 — Lists

**Voice lock — mandatory:** Kendrick voice; ElevenLabs v3; exact approved Kendrick voice ID; no substitution or preset; same voice throughout.
**Source:** `Pylearn-build260/content/python-basics/modules/06-lists.md`
**Target:** 6–8 minutes.

### Scene 1 — Store many values
**Visual:** Type `scores = [70, 95, 88, 60]`; highlight square brackets and each item.
**Narration:** “A variable often stores one value, but a gradebook needs many scores. A list stores multiple values in order. Here, the scores are separated by commas and surrounded by square brackets.”

### Scene 2 — Indexing and slicing
**Visual:** Run `print(scores[0])`, `print(scores[2])`, `print(scores[-1])`; outputs 70, 88, 60.
**Narration:** “Like strings, lists use zero-based positions. Index zero gives the first item, index two gives the third, and negative one gives the last item.”
**Visual:** `print(scores[1:3])` → `[95, 88]`.
**Narration:** “Slicing gives a smaller list. The start position is included; the end position is excluded.”

### Scene 3 — Change a list
**Visual:** `scores.append(75)`, show list; then `scores[0] = 72`, show list.
**Narration:** “Lists can change. Append adds one item at the end. Assignment to an index replaces an existing item. Because the contents can change after the list is created, we call lists mutable.”

### Scene 4 — Ask questions about a collection
**Visual:** Show `len(scores)`, `sum(scores)`, `min(scores)`, `max(scores)`, and `sorted(scores)` in separate beats; run.
**Narration:** “Python has built-in tools for common questions. Len counts items, sum adds them, min finds the smallest, max finds the largest, and sorted returns a sorted list. Choose the simplest operation that answers your question.”
**Visual:** `average = sum(scores) / len(scores)`.
**Narration:** “An average is the total divided by the number of scores. But what if the list is empty? Its length is zero, so this division would fail. Empty collections are an important edge case to think about.”

### Scene 5 — Membership and sorting
**Visual:** `print(95 in scores)`, `print(100 in scores)`; then compare original list with `ordered = sorted(scores)`.
**Narration:** “The in operator checks whether a value appears. Sorted creates a new ordered result, leaving the original list unchanged. If you only need the highest score, max is simpler than sorting everything.”

### Scene 6 — Your turn
**Visual:** `scores = [70, 95, 88, 60, 80]`; show task list: count, total, average, highest, lowest, top two. Keep solution hidden.
**Narration:** “Calculate the number of scores, total, average, highest, lowest, and top two scores. Predict which results change if you replace one score. Then consider an empty list and decide how a real program should handle it.”
**Hold:** 4 seconds.

### Recap
**Narration:** “Lists keep values in order. You can access and slice items, append or replace values, and use len, sum, min, max, sorted, and membership checks. Always consider edge cases like an empty list. Next, we'll use conditions to make decisions.”

## App practice handoff

**Visual:** End card showing the corresponding PyLearn lesson/exercise; do not show a completed solution.

**Narration:** "Open Lesson 6 in PyLearn and complete the list exercise in the app. Calculate the requested summary values, change one score, and test the empty-list case thoughtfully."
