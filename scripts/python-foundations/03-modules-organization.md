# PyLearn Video — 03 — Organize a Growing Program

**Voice lock — mandatory:** Use the user-approved Kendrick voice with ElevenLabs v3. Do not substitute another voice or preset.
**Canonical source:** Pylearn-build260/content/python-foundations/modules/03-modules-organization.md, branch ccr-c7f6fdd7-xpzi3g.
**Use:** Full teaching video, not a short outline. Narrate only spoken text; keep scene headings, code labels, and visual directions out of text-to-speech. Do not show the app's required exercise solution.

**Track 2 visual identity:** Keep the same teacher and pacing. Use a clean software-architecture canvas with connected file tabs and module cards. Animate one crowded file separating into focused modules, then show simple import connections. Use a small dependency map and color-coded responsibility labels instead of repeated input/output boxes; keep the layout calm and readable.

## Scene 1 — When one file becomes hard to manage

**Visual:** Reveal the code gradually. Ask for a prediction before running it. Show the output only after the run.

**Narration:**

A short program can live in one file. As it grows, loading data, validating it, calculating results, and formatting reports can become tangled. A module is simply a Python file that contains reusable code.

**Module file — `analysis.py`**
```python
def average_score(scores):
    if not scores:
        return 0.0
    return sum(scores) / len(scores)
```

**Visual result**
The module defines one reusable function. Defining the function does not print anything; the next scene imports and calls it.

**Narration:**

Pause and compare the output with your prediction. Change one thing at a time, run the example again, and explain what changed.

## Scene 2 — Import a reusable function

**Visual:** Reveal the code gradually. Ask for a prediction before running it. Show the output only after the run.

**Narration:**

Another Python file can import the function by its module name. The module name comes from the file name, without the .py ending.

**Runner file — `main.py`**
```python
from analysis import average_score

print(average_score([80, 90]))
```

**Expected output**
```text
85.0
```

**Narration:**

The second file does not need to copy the average calculation. It uses the same function. That makes fixes and tests easier to manage.

## Scene 3 — Give each part one job

**Visual:** Reveal the code gradually. Ask for a prediction before running it. Show the output only after the run.

**Narration:**

For a data toolkit, one module can load files, another can validate records, another can calculate summaries, and another can write reports. The goal is not to create as many files as possible. The goal is to make each responsibility easy to find.

**Module file — `summary.py`**
```python
def passing_count(scores, threshold):
    return sum(score >= threshold for score in scores)
```

**Visual result**
The function counts scores meeting the threshold. Keep the module focused on defining the function; call it from the runner in Scene 4.

**Narration:**

This function answers one question: how many scores meet the threshold? A small, focused function is easier to test than a single giant program.

## Scene 4 — Keep interfaces clear

**Visual:** Reveal the code gradually. Ask for a prediction before running it. Show the output only after the run.

**Narration:**

When a function takes a list and returns a result, that boundary can be tested without reading a file. When file loading has its own function, we can test it separately too.

**Runner file — `main.py`**
```python
from summary import passing_count

scores = [60, 70, 90]
count = passing_count(scores, 70)
print(f"Passing: {count}")
```

**Expected output**
```text
Passing: 2
```

**Narration:**

Separating responsibilities helps us locate a bug. If the scores are wrong, inspect loading or validation. If the count is wrong for a known list, inspect the calculation.

## Your turn — predict, run, explain

**Visual:** Keep the editor uncluttered. Show a fresh, related prompt without using the app's required exercise code.

**Narration:**

Pause the video and try a small variation of the example. Predict the output before you run it. Then run the code, compare the result with your prediction, and explain why it happened. If the result surprises you, inspect the values and change one thing at a time.

This is extra guided practice, not the required PyLearn exercise solution.

## Recap

**Narration:**

Today, you learned the core idea behind modules and single responsibility. Keep the stages clear, test your assumptions, and make the program's behavior visible. In the next lesson, we'll build on this skill.

## Final call to action — watch the practice video

**Visual:** Neutral end card reading “Next: Practice Video”. Do not show unfinished app screens or invent navigation.

**Narration:**

Great work! You've finished Organize a Growing Program. Next, watch the practice video. I recommend watching it because we'll use a fresh example to reinforce the skill from this lesson.

After the practice video, complete the exercise to unlock the next lesson. If you'd like extra hands-on practice, you can also try it in the PyLearn app.

**Visual:** Hold the end card long enough to read.

## Production checklist

- [ ] Use the approved Kendrick voice with ElevenLabs v3.
- [ ] Verify every example and expected output in Python before rendering.
- [ ] Reveal code before running it; reveal output only after the run.
- [ ] Keep narration separate from production directions.
- [ ] Do not show the required app exercise solution or hidden tests.
- [ ] Watch the complete rendered video at normal speed before approval.


**Visual transition rule for this lesson:** Show separate file tabs for `analysis.py` or `summary.py` and `main.py`. First show the function definition living in its module; then draw the import connection; finally show the runner calling the function and reveal the exact returned/printed value. Do not show the function's return value as console output until a call actually prints it.
