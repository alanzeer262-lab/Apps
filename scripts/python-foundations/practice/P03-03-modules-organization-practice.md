# PyLearn Guided Practice — 03 — Organize a Growing Program

**Voice lock — mandatory:** Use the user-approved Kendrick voice with ElevenLabs v3; do not substitute another voice.
**Canonical source:** Pylearn-build260/content/python-foundations/modules/03-modules-organization.md, branch ccr-c7f6fdd7-xpzi3g.
**Target runtime:** Approximately 3–5 minutes.
**Purpose:** Separate guided-practice companion with fresh examples. Never reveal the required app exercise solution.

## Scene 1 — When one file becomes hard to manage

**Visual:** Use a fresh example and the same uncluttered code-first visual style as the lesson.

**Narration:**

A short program can live in one file. As it grows, loading data, validating it, calculating results, and formatting reports can become tangled. A module is simply a Python file that contains reusable code.

**Code**
    
    # analysis.py
        def average_score(scores):
            if not scores:
                return 0.0
            return sum(scores) / len(scores)

**Expected output**
    
This module has one clear responsibility: calculate an average. It also handles an empty list without dividing by zero.

**Narration:**

Predict the result before running the example. Compare the output with your prediction and explain the result in your own words. If it differs, inspect the input and change one thing at a time.

## Scene 2 — Import a reusable function

**Visual:** Use a fresh example and the same uncluttered code-first visual style as the lesson.

**Narration:**

Another Python file can import the function by its module name. The module name comes from the file name, without the .py ending.

**Code**
    
    from analysis import average_score
    
        print(average_score([80, 90]))

**Expected output**
    
    85.0

**Narration:**

Predict the result before running the example. Compare the output with your prediction and explain the result in your own words. If it differs, inspect the input and change one thing at a time.

## Scene 3 — Give each part one job

**Visual:** Use a fresh example and the same uncluttered code-first visual style as the lesson.

**Narration:**

For a data toolkit, one module can load files, another can validate records, another can calculate summaries, and another can write reports. The goal is not to create as many files as possible. The goal is to make each responsibility easy to find.

**Code**
    
    # summary.py
        def passing_count(scores, threshold):
            return sum(score >= threshold for score in scores)
    
        print(passing_count([60, 70, 90], 70))

**Expected output**
    
    2

**Narration:**

Predict the result before running the example. Compare the output with your prediction and explain the result in your own words. If it differs, inspect the input and change one thing at a time.

## Scene 4 — Keep interfaces clear

**Visual:** Use a fresh example and the same uncluttered code-first visual style as the lesson.

**Narration:**

When a function takes a list and returns a result, that boundary can be tested without reading a file. When file loading has its own function, we can test it separately too.

**Code**
    
    scores = [60, 70, 90]
        count = passing_count(scores, 70)
        print(f"Passing: {count}")

**Expected output**
    
    Passing: 2

**Narration:**

Predict the result before running the example. Compare the output with your prediction and explain the result in your own words. If it differs, inspect the input and change one thing at a time.

## Close — Complete the exercise

**Visual:** End card: “Your turn: Complete the exercise”. Do not show or describe unfinished PyLearn app screens.

**Narration:**

Good work. Now complete the exercise to unlock the next lesson. Use the habits from this practice: test small cases, check your assumptions, and make one change at a time. If you'd like extra hands-on practice, you can also try it in the PyLearn app.

## Production checklist

- [ ] Use the approved Kendrick voice with ElevenLabs v3.
- [ ] Verify all example code and outputs in Python.
- [ ] Keep the example distinct from the required app exercise.
- [ ] Do not reveal the exercise solution or hidden tests.
- [ ] Keep code and output synchronized with narration.
- [ ] End by directing the learner to complete the exercise.
