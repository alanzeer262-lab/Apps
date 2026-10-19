# PyLearn Video 17 — Project 6: Grade Distribution

> **MANDATORY VOICE SETTINGS — DO NOT CHANGE**
> - Voice: Kendrick
> - Model: ElevenLabs v3
> - Voice ID: exact approved Kendrick voice ID is not recorded in the reviewed repository files; insert the verified ID from the original Runway setup before generating audio.
> - No guessed ID, substitution, or preset. Use the same approved voice throughout.
> - Speak narration only; do not read headings or bracketed directions aloud.

**Canonical source:** `Pylearn-build260/content/python-basics/modules/17-build-grade-distribution.md`, branch `ccr-c7f6fdd7-xpzi3g`.  
**Target runtime:** Approximately 5–7 minutes. Do not show the complete required implementation.

## Scene 1 — Turn scores into categories

**Visual:** Show a few fictional scores and category labels. Do not reveal the project's full required grade distribution example.

**Narration:**

Welcome back. In this project, you'll turn numerical scores into letter grades and then count how often each grade appears.

A score is a measurement. A letter grade is a category. Once we have categories, we can summarize them in a frequency table.

Before writing code, make the rules clear. For this project, scores of ninety or higher map to A, eighty through eighty-nine map to B, seventy through seventy-nine map to C, sixty through sixty-nine map to D, and anything below sixty maps to F.

## Scene 2 — Convert one score to a category

**Visual:** Use a separate score example. Reveal the branches gradually and highlight the first true condition.

**Code**
```python
score = 86

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(grade)
```

**Expected output**
```text
B
```

**Narration:**

This example converts one score into a letter grade. Python checks the conditions from top to bottom and stops at the first one that is true.

Eighty-six is below ninety, so the first condition is false. It is at least eighty, so the next condition is true, and the grade becomes B.

The order matters. A score of ninety-five should be caught by the first condition, not by a broader condition that comes earlier.

## Scene 3 — Test the boundaries

**Visual:** Display paired boundary values: 89 and 90; 79 and 80; 69 and 70; 59 and 60. Do not produce a complete answer table for the app exercise.

**Narration:**

Category rules have boundaries. Test the values just below and exactly at each boundary.

For the A category, compare eighty-nine with ninety. For B, compare seventy-nine with eighty. Do the same at sixty and seventy.

This catches mistakes such as using greater-than when you meant greater-than-or-equal. Write the rules in ordinary language first, then translate them into comparisons.

## Scene 4 — Count the categories

**Visual:** Show a small unrelated list of grades, then an empty dictionary. Reveal the counting loop step by step.

**Code**
```python
grades = ["A", "B", "A", "C", "B"]
counts = {}

for grade in grades:
    counts[grade] = counts.get(grade, 0) + 1

print(counts)
```

**Expected output**
```text
{'A': 2, 'B': 2, 'C': 1}
```

**Narration:**

Once values are converted into categories, we can count each category with a dictionary.

We begin with an empty dictionary. For each grade, get looks up the current count. If the grade hasn't appeared yet, the default is zero. We add one and store the new count.

When A appears again, its count increases. The same happens for B. The final dictionary tells us how many times each category appeared.

This is a frequency table: it summarizes repeated labels into counts.

## Scene 5 — Why a frequency table is useful

**Visual:** Contrast a list of repeated grade labels with a compact dictionary of counts.

**Narration:**

Imagine analyzing a large collection of scores. Keeping every letter grade in a long list makes it hard to see the overall pattern. A frequency table gives us a compact summary.

Instead of storing three separate A labels, the dictionary can store one key A with a count of three. That makes it easier to compare categories, report results, or build a chart later.

The goal is not simply to write a dictionary. It's to choose a data structure that answers the question we want to ask.

## Scene 6 — Plan and test your project

**Visual:** Show a checklist: convert score to grade, count grades, test boundary values, compare frequency table. Do not show the full required solution.

**Narration:**

Your project needs one function to convert scores to grades and another to count the grades. Keep each function focused on one job.

Test scores at the boundaries and test repeated categories. Check that every score receives exactly one grade and that the total of the category counts matches the number of input scores.

If the counts are wrong, inspect the grade conversion first, then inspect the counting loop. Separating those steps makes the problem easier to locate.

## Scene 7 — Reflection

**Visual:** Show “A: 3” next to three repeated A labels.

**Narration:**

Before you finish, ask why A colon three is more useful for analysis than storing three separate A values.

A count summarizes repetition. It makes the distribution easier to read and gives you a useful structure for later reporting.

## Final call to action — watch the practice video

**Visual:** Use a neutral end card reading “Next: Practice Video”. Do not show or describe unfinished PyLearn app screens or reveal a completed project solution.

**Narration:**

Great work! You've finished this lesson. The next step is to watch the practice video. I recommend watching it because it will help you apply what you've learned with a fresh example.

After the practice video, complete the exercise to unlock the next lesson. If you'd like extra hands-on practice, you can also try it in the PyLearn app.

**Visual:** Hold the “Next: Practice Video” end card long enough to read.

## Production and QA checklist

- [ ] Verify the exact approved Kendrick voice ID before generating audio.
- [ ] Use ElevenLabs v3 and the same approved voice throughout.
- [ ] Keep production notes out of spoken narration.
- [ ] Verify all demonstration code and outputs in Python.
- [ ] Do not reveal the full required grade-distribution solution.
- [ ] Preserve boundary-testing guidance and project navigation ending.
