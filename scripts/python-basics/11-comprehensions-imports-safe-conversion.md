# PyLearn Video 11 — Comprehensions, Imports, and Safe Conversion

**Voice lock — mandatory:** Kendrick; ElevenLabs v3; exact approved Kendrick voice ID; no substitution/preset; same voice throughout.
**Source:** `Pylearn-build260/content/python-basics/modules/11-comprehensions-imports.md`
**Target:** 7–8 minutes.

### Scene 1 — Imperfect input
**Visual:** `raw_scores = ["88", "72", "oops", "95"]`; highlight the invalid item.
**Narration:** “Real programs receive imperfect input. Three entries look numeric, but one says oops. If we convert every item without a plan, the program can stop with an error. This lesson adds three tools: a compact way to build lists, imports for reusable Python tools, and safe handling for expected conversion errors.”

### Scene 2 — List comprehensions
**Visual:** Show normal loop building doubled scores, run; then show equivalent `doubled = [score * 2 for score in scores]`.
**Narration:** “A list comprehension creates a list by describing the transformation. This version doubles every score. It does the same job as the loop, but in one expression. Use it when the result remains easy to read, not merely to make the code shorter.”
**Visual:** `passing = [score for score in scores if score >= 70]`; reveal output.

### Scene 3 — Imports
**Visual:** `import math`, `print(math.sqrt(25))` → 5.0; then `from statistics import mean`, `print(mean([70, 80, 90]))` → 80.
**Narration:** “Python's standard library provides tools you don't need to write yourself. Import math, then use math dot sqrt. Or import mean from statistics and use it on a list. The module name helps show where a tool came from.”

### Scene 4 — Missing is not zero
**Visual:** Show `result = None`, then contrast None, 0, empty string, and False as distinct values.
**Narration:** “Sometimes there is no value. Python represents that with None. None is not the same as zero, an empty string, or False. If a score is missing, silently changing it to zero can misrepresent the data. Decide what missing means in the problem you're solving.”

### Scene 5 — Safe conversion
**Visual:** Run `int("88")`; then show `int("oops")` with the actual ValueError. Replace with try/except returning None.
**Narration:** “Converting the text eighty-eight to an integer works. Converting oops raises ValueError. If invalid input is expected, try and except let us handle that case deliberately. Here, we use None to represent an invalid conversion. In another program, you might report the record or ask for corrected input.”
**Visual:** Pipeline: raw input → convert → separate valid/invalid → analyze valid → report rejected.

### Scene 6 — Practice and bridge
**Visual:** Prompt safe_int(value), tests for "88", "oops", and empty text; don't show answer before the prediction pause.
**Narration:** “Build a safe conversion function. Test a valid number, an invalid word, and an empty string. Then separate valid scores from invalid ones. Ask yourself: should missing data be ignored, reported, or treated another way? Choose the rule deliberately.”
**Hold:** 4 seconds.

### Recap
**Narration:** “Comprehensions transform collections, imports reuse existing tools, None represents absence of a value, and try/except handles expected conversion errors. You've completed the core Python Basics modules. Next, we'll apply these skills in small projects and then the Mini Gradebook capstone.”
