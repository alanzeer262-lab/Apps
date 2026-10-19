# PyLearn Guided Practice — 05 — Think in Tables Before pandas

**Voice lock — mandatory:** Use the user-approved Kendrick voice with ElevenLabs v3; do not substitute another voice.
**Canonical source:** Pylearn-build260/content/python-foundations/modules/05-data-shaped-python.md, branch ccr-c7f6fdd7-xpzi3g.
**Target runtime:** Approximately 3–5 minutes.
**Purpose:** Separate guided-practice companion with fresh examples. Never reveal the required app exercise solution.

## Scene 1 — A table made from dictionaries

**Visual:** Use a fresh example and the same uncluttered code-first visual style as the lesson.

**Narration:**

Before using a data-analysis library, we can practice the underlying ideas with plain Python. A list can hold one dictionary per row, and each dictionary can use named fields.

**Code**
    
    records = [
            {"name": "Ada", "score": 88, "topic": "Python"},
            {"name": "Lin", "score": 72, "topic": "Python"},
            {"name": "Sam", "score": 95, "topic": "Pandas"},
        ]
        print(records[0]["name"])
        print(records[0]["score"])

**Expected output**
    
    Ada
        88

**Narration:**

Predict the result before running the example. Compare the output with your prediction and explain the result in your own words. If it differs, inspect the input and change one thing at a time.

## Scene 2 — Select and filter

**Visual:** Use a fresh example and the same uncluttered code-first visual style as the lesson.

**Narration:**

Selection asks for a field. Filtering keeps only rows that meet a condition. These are two common operations in data analysis.

**Code**
    
    scores = [row["score"] for row in records]
        strong = [row for row in records if row["score"] >= 80]
        print(scores)
        print(len(strong))

**Expected output**
    
    [88, 72, 95]
        2

**Narration:**

Predict the result before running the example. Compare the output with your prediction and explain the result in your own words. If it differs, inspect the input and change one thing at a time.

## Scene 3 — Create a derived field

**Visual:** Use a fresh example and the same uncluttered code-first visual style as the lesson.

**Narration:**

A derived field is calculated from existing data. We can add a pass flag to each record using a consistent threshold.

**Code**
    
    for row in records:
            row["passed"] = row["score"] >= 70
        print(records[1]["passed"])

**Expected output**
    
    True

**Narration:**

Predict the result before running the example. Compare the output with your prediction and explain the result in your own words. If it differs, inspect the input and change one thing at a time.

## Scene 4 — Count categories

**Visual:** Use a fresh example and the same uncluttered code-first visual style as the lesson.

**Narration:**

Grouping means collecting rows by a shared category. A dictionary can count how often each topic appears.

**Code**
    
    counts = {}
        for row in records:
            topic = row["topic"]
            counts[topic] = counts.get(topic, 0) + 1
        print(counts)

**Expected output**
    
    {'Python': 2, 'Pandas': 1}

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
