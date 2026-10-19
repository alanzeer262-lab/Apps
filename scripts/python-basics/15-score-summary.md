# PyLearn Video 15 — Project 4: Score Summary

> **MANDATORY VOICE SETTINGS — DO NOT CHANGE**
> - Voice: Kendrick
> - Model: ElevenLabs v3
> - Voice ID: exact approved Kendrick voice ID is not recorded in the reviewed repository files; insert the verified ID from the original Runway setup before generating audio.
> - Do not guess or substitute a voice or preset. Use the same approved voice throughout.
> - Speak narration only; do not read headings or bracketed production notes aloud.

**Canonical source:** `Pylearn-build260/content/python-basics/modules/15-build-score-summary.md`, branch `ccr-c7f6fdd7-xpzi3g`.  
**Target runtime:** Approximately 5–7 minutes. Do not show the complete required function or solution.

## Scene 1 — Turn a list into a summary

**Visual:** Show a short list of fictional scores, then the questions a summary should answer: count, average, highest, lowest, passed.

**Narration:**

Welcome back. In this project, you're going to turn a collection of scores into a useful summary.

A list holds the raw values. A summary helps someone understand them. Instead of reading every score individually, we may want to know how many scores there are, the average, the highest and lowest values, and how many meet a passing threshold.

Before coding, write down what each field means. That helps you decide which built-in function or calculation belongs to each part.

## Scene 2 — Explore the built-in tools

**Visual:** Use a separate example from the project’s required input. Reveal one function at a time.

**Code**
```python
scores = [62, 78, 91, 84]
print(len(scores))
print(sum(scores) / len(scores))
print(max(scores))
print(min(scores))
```

**Expected output**
```text
4
78.75
91
62
```

**Narration:**

Len counts the items. Sum adds the values, so dividing sum by len gives the average. Max finds the highest value, and min finds the lowest.

Notice that each line answers one question. Using these tools keeps the code focused and easier to check.

But what if the list is empty? Len would return zero, and dividing by zero would fail. Your project must return a deliberate empty result instead of crashing. Decide what an empty summary should mean before writing the function.

## Scene 3 — Use a threshold as a rule

**Visual:** Demonstrate a simple comparison with an independent example. Highlight the boundary operator.

**Code**
```python
score = 70
threshold = 70
print(score >= threshold)
```

**Expected output**
```text
True
```

**Narration:**

The passing rule uses a threshold. If a score of seventy or higher passes, the comparison must include seventy itself. That's why greater-than-or-equal is different from greater-than.

Test values just below, exactly at, and just above the threshold. For this rule, test sixty-nine, seventy, and seventy-one. The exact boundary is often where a small logic mistake appears.

## Scene 4 — Return a structured result

**Visual:** Show a dictionary with field names only, without filling the complete required result. Use labels such as count, average, highest, lowest, and passed.

**Narration:**

The project asks you to return a dictionary. A dictionary is useful because each result has a clear key. The caller can ask for the average by name rather than remembering a position in a list.

Your function should calculate the requested fields, package them in a dictionary, and return that dictionary. Keep the function focused on summarizing the scores; don't mix in unrelated tasks.

I'm not showing the complete function or its finished output, because you'll build and test that part yourself in PyLearn.

## Scene 5 — Test ordinary and edge cases

**Visual:** Show a test checklist, not completed outputs: a typical list, values around the threshold, and an empty list.

**Narration:**

Test a typical list first. Then test the threshold boundary. If seventy is passing, exactly seventy must count.

Finally, test an empty list. It is a valid input even though it has no scores. Your code should return the empty result you decided on, rather than attempting to calculate an average by dividing by zero.

When a test fails, check one field at a time. Is the count correct? Is the average based on all values? Does the threshold include the boundary? Does the empty case follow your chosen rule?

## Scene 6 — Reflection

**Visual:** Display “Why a dictionary?” and highlight named fields.

**Narration:**

Before you finish, ask why a dictionary is a useful shape for an analysis result.

A dictionary makes each result self-describing. Count, average, highest, lowest, and passed are named fields. That makes the result easier to read and reuse in another part of a program.

## Project closing — required for in-app and YouTube versions

**Visual:** Show the real PyLearn navigation path to the “Score Summary” project task. Do not show the complete `summarize_scores` function or its full result.

**Narration:**

Now open PyLearn and find the Score Summary task.

Build it yourself and run the tests. This video has shown the ideas, not the finished solution. Practice Drills, if shown, are optional; complete and pass the required project exercise to unlock the next lesson.

Pause the video and start building.

## Production and QA checklist

- [ ] Verify the exact approved Kendrick voice ID before generating audio.
- [ ] Use ElevenLabs v3 and the same approved voice throughout.
- [ ] Keep production notes out of spoken narration.
- [ ] Verify all demonstration code and outputs in Python.
- [ ] Do not reveal the complete `summarize_scores` implementation or required solution.
- [ ] Preserve the project navigation ending and progression rule.
