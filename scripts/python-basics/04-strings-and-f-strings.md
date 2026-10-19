# PyLearn Video 04 — Strings and f-strings

**Voice lock — mandatory:** Kendrick voice; ElevenLabs v3; exact approved Kendrick voice ID; no substitution or preset; same voice throughout.
**Source:** `Pylearn-build260/content/python-basics/modules/04-strings.md`
**Target:** 6–8 minutes.

## Learning outcome
Read, slice, clean, split, search, replace, and format strings.

### Scene 1 — Messy text is still data
**Visual:** Type `raw = " python, pandas, machine learning "`.
**Narration:** “Real programs often receive text with extra spaces or inconsistent capitalization. Imagine a list of learning topics arrives with spaces around it. Before analyzing that text, we need to understand strings and how to transform them.”

### Scene 2 — Characters and positions
**Visual:** Type `topic = "Python"`, then reveal `print(topic[0])` and `print(topic[1])`; output P then y.
**Narration:** “A string is a sequence of characters. Python counts positions starting at zero, not one. So position zero is P, and position one is y. This is called zero-based indexing.”
**Visual:** Show `print(topic[0:2])`, `print(topic[:2])`, and `print(topic[2:])` in separate beats; outputs Py, Py, thon.
**Narration:** “A slice takes part of a string. The start is included, but the stop position is not. Think: start here, stop before there.”

### Scene 3 — Clean with methods
**Visual:** `name = "  ada  "`; reveal `strip()`, `upper()`, `lower()`, `title()` one by one with outputs.
**Narration:** “String methods transform text. Strip removes surrounding whitespace. Upper makes letters uppercase; lower makes them lowercase; title formats the text like a name. We can save a cleaned result with `clean_name = name.strip().title()`. The result is Ada. A useful pattern is messy input, transform it, keep the useful result.”

### Scene 4 — Split and search
**Visual:** `raw = "python, pandas, machine learning"`, `topics = raw.split(",")`; show the three list items with spaces visible.
**Narration:** “Split separates one string into pieces using the separator you provide. Here, the comma separates the topics. Notice the pieces may still have spaces, so splitting alone is not the full cleanup.”
**Visual:** `topic = "machine learning"`; show `"learning" in topic` → True and `"python" in topic` → False.
**Narration:** “The word in checks whether one piece of text appears inside another. For case-insensitive checks, normalize the text first—for example, search inside topic.lower().”

### Scene 5 — Replace and format
**Visual:** `message = "I like Java"`, `message = message.replace("Java", "Python")`, `print(message)`.
**Narration:** “Replace substitutes the exact text you specify. Be precise about what you want to replace.”
**Visual:** `name = "Ada"`, `score = 92`, `print(f"{name} scored {score}.")`, then `print(f"Next target: {score + 3}")`.
**Narration:** “An f-string lets you put variable values or expressions inside curly braces. The f before the quote tells Python to fill those braces in. It makes output easier to read.”

### Scene 6 — Topic cleaner challenge
**Visual:** Show `raw_topics = " python, pandas, machine learning "`; show pipeline labels: strip → split → clean each topic → count → check membership. Do not show a full solution prematurely.
**Narration:** “Your turn. Clean this topic text, split it, clean each topic, print the results, count the topics, and check whether Python is present. Pause and plan the steps before coding.”
**Hold:** 4 seconds.
**Narration:** “Test a different input too. Watch for extra spaces and capitalization.”

### Recap
**Narration:** “Strings are sequences of characters. You can index and slice them, clean them with methods, split them into pieces, search with in, replace text, and create readable output with f-strings. Next, we'll teach Python to answer true-or-false questions.”

## App practice handoff

**Visual:** End card showing the corresponding PyLearn lesson/exercise; do not show a completed solution.

**Narration:** "Open Lesson 4 in PyLearn and complete the topic-cleaning exercise yourself. Clean and split the supplied text, check membership, and test a changed input. Use the app feedback to verify the result."
