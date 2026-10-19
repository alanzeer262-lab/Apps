# PyLearn Guided Practice — 06 — From Raw Records to a Reliable Report

**Voice lock — mandatory:** Use the user-approved Kendrick voice with ElevenLabs v3; do not substitute another voice.
**Canonical source:** Pylearn-build260/content/python-foundations/modules/06-analysis-ready-pipeline.md, branch ccr-c7f6fdd7-xpzi3g.
**Target runtime:** Approximately 3–5 minutes.
**Purpose:** Separate guided-practice companion with fresh examples. Never reveal the required app exercise solution.

## Scene 1 — Follow the pipeline

**Visual:** Use a fresh example and the same uncluttered code-first visual style as the lesson.

**Narration:**

A reliable data workflow moves through deliberate stages: inspect, validate, clean, transform, summarize, and report. Each stage answers a different question, and the order matters.

**Code**
    
    raw_scores = ["80", "90", "oops", "70"]
        print("Rows read:", len(raw_scores))

**Expected output**
    
    Rows read: 4

**Narration:**

Predict the result before running the example. Compare the output with your prediction and explain the result in your own words. If it differs, inspect the input and change one thing at a time.

## Scene 2 — Validate before calculating

**Visual:** Use a fresh example and the same uncluttered code-first visual style as the lesson.

**Narration:**

A score stored as text needs conversion. A word such as oops cannot be converted to an integer. We'll keep valid values separate from invalid values so the report can explain what happened.

**Code**
    
    raw_scores = ["80", "90", "oops", "70"]
        valid_scores = []
        invalid_values = []
        for raw in raw_scores:
            try:
                valid_scores.append(int(raw))
            except ValueError:
                invalid_values.append(raw)
        print(valid_scores)
        print(invalid_values)

**Expected output**
    
    [80, 90, 70]
        ['oops']

**Narration:**

Predict the result before running the example. Compare the output with your prediction and explain the result in your own words. If it differs, inspect the input and change one thing at a time.

## Scene 3 — Summarize the cleaned data

**Visual:** Use a fresh example and the same uncluttered code-first visual style as the lesson.

**Narration:**

Only after validation can we calculate the average for the valid scores. The report should state how many rows were read and how many were usable.

**Code**
    
    average = sum(valid_scores) / len(valid_scores)
        print("Valid rows:", len(valid_scores))
        print("Average:", average)

**Expected output**
    
    Valid rows: 3
        Average: 80.0

**Narration:**

Predict the result before running the example. Compare the output with your prediction and explain the result in your own words. If it differs, inspect the input and change one thing at a time.

## Scene 4 — Decisions belong in the report

**Visual:** Use a fresh example and the same uncluttered code-first visual style as the lesson.

**Narration:**

Missing values, duplicate records, inconsistent capitalization, and out-of-range scores all require decisions. There is no universal cleaning rule. Choose it, document it, and apply it consistently.

**Code**
    
    print("Rows read: 4")
        print("Valid rows: 3")
        print("Invalid rows: 1")
        print("Warning: one score could not be converted")

**Expected output**
    
    Rows read: 4
        Valid rows: 3
        Invalid rows: 1
        Warning: one score could not be converted

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
