# PyLearn Guided Practice — 09 — Build: Summary Report

**Voice lock — mandatory:** Use the user-approved Kendrick voice with ElevenLabs v3; do not substitute another voice.
**Canonical source:** Pylearn-build260/content/python-foundations/modules/09-build-summary.md, branch ccr-c7f6fdd7-xpzi3g.
**Target runtime:** Approximately 3–5 minutes.
**Purpose:** Separate guided-practice companion with fresh examples. Never reveal the required app exercise solution.

## Scene 1 — Turn rows into answers

**Visual:** Use a fresh example and the same uncluttered code-first visual style as the lesson.

**Narration:**

A pile of records is not yet a useful answer. A summary should tell us how many valid scores we have, what their average is, and who has the highest score. The function should receive validated records, not raw CSV text.

**Code**
    
    scores = [88, 72, 95]
        print("Count:", len(scores))
        print("Average:", sum(scores) / len(scores))
        print("Top score:", max(scores))

**Expected output**
    
    Count: 3
        Average: 85.0
        Top score: 95

**Narration:**

Predict the result before running the example. Compare the output with your prediction and explain the result in your own words. If it differs, inspect the input and change one thing at a time.

## Scene 2 — Protect the empty case

**Visual:** Use a fresh example and the same uncluttered code-first visual style as the lesson.

**Narration:**

If there are no valid scores, there is no average and no top scorer. Calling max on an empty list raises an error, and dividing by zero does too. The summary should handle the empty case explicitly.

**Code**
    
    scores = []
        if not scores:
            print("No valid scores")
        else:
            print(sum(scores) / len(scores))
            print(max(scores))

**Expected output**
    
    No valid scores

**Narration:**

Predict the result before running the example. Compare the output with your prediction and explain the result in your own words. If it differs, inspect the input and change one thing at a time.

## Scene 3 — Make the output interpretable

**Visual:** Use a fresh example and the same uncluttered code-first visual style as the lesson.

**Narration:**

A summary can report a count, average, and top score. For a real toolkit, it should also preserve the row counts and validation warnings from earlier stages.

**Code**
    
    scores = [88, 72, 95]
        summary = {
            "count": len(scores),
            "average": sum(scores) / len(scores),
            "top_score": max(scores),
        }
        print(summary)

**Expected output**
    
    {'count': 3, 'average': 85.0, 'top_score': 95}

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
