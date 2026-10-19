# PyLearn Guided Practice — 07 — Build: Load a Scores CSV

**Voice lock — mandatory:** Use the user-approved Kendrick voice with ElevenLabs v3; do not substitute another voice.
**Canonical source:** Pylearn-build260/content/python-foundations/modules/07-build-loader.md, branch ccr-c7f6fdd7-xpzi3g.
**Target runtime:** Approximately 3–5 minutes.
**Purpose:** Separate guided-practice companion with fresh examples. Never reveal the required app exercise solution.

## Scene 1 — The loader's responsibility

**Visual:** Use a fresh example and the same uncluttered code-first visual style as the lesson.

**Narration:**

Now we move from individual skills to a small toolkit. The loader's job is narrow: take raw CSV text and turn it into a consistent list of records. It should not calculate averages or decide which scores are valid.

**Code**
    
    csv_text = "name,score\nAda,88\nLin,72\n"
        print(csv_text.splitlines())

**Expected output**
    
    ['name,score', 'Ada,88', 'Lin,72']

**Narration:**

Predict the result before running the example. Compare the output with your prediction and explain the result in your own words. If it differs, inspect the input and change one thing at a time.

## Scene 2 — Separate parsing from analysis

**Visual:** Use a fresh example and the same uncluttered code-first visual style as the lesson.

**Narration:**

For this demonstration, we'll use Python's CSV reader with an in-memory text stream. That lets us show the parsing idea without needing a real file on screen.

**Code**
    
    import csv
        from io import StringIO
    
        text = "name,score\nAda,88\nLin,72\n"
        reader = csv.DictReader(StringIO(text))
        rows = list(reader)
        print(rows[0]["name"], rows[0]["score"])

**Expected output**
    
    Ada 88

**Narration:**

Predict the result before running the example. Compare the output with your prediction and explain the result in your own words. If it differs, inspect the input and change one thing at a time.

## Scene 3 — Handle ordinary mess

**Visual:** Use a fresh example and the same uncluttered code-first visual style as the lesson.

**Narration:**

Real inputs may have extra spaces or a final blank line. A good loader trims fields and skips rows that contain no meaningful data. That makes its output more consistent without hiding invalid scores.

**Code**
    
    raw_name = "  Ada  "
        raw_score = " 88 "
        print(raw_name.strip())
        print(raw_score.strip())

**Expected output**
    
    Ada
        88

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
