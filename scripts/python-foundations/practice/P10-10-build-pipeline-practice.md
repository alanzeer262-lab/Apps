# PyLearn Guided Practice — 10 — Build: Run the Pipeline

**Voice lock — mandatory:** Use the user-approved Kendrick voice with ElevenLabs v3; do not substitute another voice.
**Canonical source:** Pylearn-build260/content/python-foundations/modules/10-build-pipeline.md, branch ccr-c7f6fdd7-xpzi3g.
**Target runtime:** Approximately 3–5 minutes.
**Purpose:** Separate guided-practice companion with fresh examples. Never reveal the required app exercise solution.

## Scene 1 — Connect the parts

**Visual:** Use a fresh example and the same uncluttered code-first visual style as the lesson.

**Narration:**

A user of your toolkit should not need to remember every internal step. One public function can take raw CSV text and coordinate loading, validation, and aggregation. Internally, each stage still has one job.

**Code**
    
    raw_text = "name,score\nAda,88\nLin,72\n"
        print("Pipeline input received")
        print("Characters:", len(raw_text))

**Expected output**
    
    Pipeline input received
        Characters: 31

**Narration:**

Predict the result before running the example. Compare the output with your prediction and explain the result in your own words. If it differs, inspect the input and change one thing at a time.

## Scene 2 — Preserve the stages

**Visual:** Use a fresh example and the same uncluttered code-first visual style as the lesson.

**Narration:**

The pipeline should load first, validate second, and summarize last. This keeps the code understandable and makes each part testable on its own.

**Code**
    
    stages = ["load", "validate", "summarize"]
        for stage in stages:
            print("Running:", stage)

**Expected output**
    
    Running: load
        Running: validate
        Running: summarize

**Narration:**

Predict the result before running the example. Compare the output with your prediction and explain the result in your own words. If it differs, inspect the input and change one thing at a time.

## Scene 3 — One call, useful result

**Visual:** Use a fresh example and the same uncluttered code-first visual style as the lesson.

**Narration:**

A single entry point can hide the plumbing while still returning a structured summary. The caller can then display the result, save it, or test it.

**Code**
    
    result = {
            "rows_read": 2,
            "valid_rows": 2,
            "invalid_rows": 0,
            "average": 80.0,
        }
        print("Average:", result["average"])
        print("Invalid rows:", result["invalid_rows"])

**Expected output**
    
    Average: 80.0
        Invalid rows: 0

**Narration:**

Predict the result before running the example. Compare the output with your prediction and explain the result in your own words. If it differs, inspect the input and change one thing at a time.

## Scene 4 — Ready for the final build

**Visual:** Use a fresh example and the same uncluttered code-first visual style as the lesson.

**Narration:**

You now have the building blocks: load, validate, summarize, and connect. In the capstone, you will run the toolkit on a deliberately imperfect CSV and explain the cleaning decisions. Do not aim only for code that runs; aim for a report a person can trust.

**Code**
    
    required_sections = [
            "rows read", "valid rows", "invalid rows",
            "cleaning decisions", "average", "top performer",
            "grade distribution", "warning or limitation",
        ]
        print("Report sections:", len(required_sections))

**Expected output**
    
    Report sections: 8

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
