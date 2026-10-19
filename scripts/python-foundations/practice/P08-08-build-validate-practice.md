# PyLearn Guided Practice — 08 — Build: Validate Intake

**Voice lock — mandatory:** Use the user-approved Kendrick voice with ElevenLabs v3; do not substitute another voice.
**Canonical source:** Pylearn-build260/content/python-foundations/modules/08-build-validate.md, branch ccr-c7f6fdd7-xpzi3g.
**Target runtime:** Approximately 3–5 minutes.
**Purpose:** Separate guided-practice companion with fresh examples. Never reveal the required app exercise solution.

## Scene 1 — Why validation is a gate

**Visual:** Use a fresh example and the same uncluttered code-first visual style as the lesson.

**Narration:**

A score of 150 or minus one can quietly distort every number in a report. Validation checks whether a record meets the rules before it is included in calculations. Keep it separate from loading so both parts can be tested independently.

**Code**
    
    scores = [88, 150, -1, 72]
        valid = [score for score in scores if 0 <= score <= 100]
        print(valid)

**Expected output**
    
    [88, 72]

**Narration:**

Predict the result before running the example. Compare the output with your prediction and explain the result in your own words. If it differs, inspect the input and change one thing at a time.

## Scene 2 — Text can fail conversion

**Visual:** Use a fresh example and the same uncluttered code-first visual style as the lesson.

**Narration:**

CSV data often arrives as text. Conversion can fail if a field contains a word or is blank. Catch that failure and record it as invalid instead of crashing the entire pipeline.

**Code**
    
    raw_values = ["88", "oops", "", "72"]
        valid = []
        rejected = []
        for raw in raw_values:
            try:
                score = int(raw)
                if 0 <= score <= 100:
                    valid.append(score)
                else:
                    rejected.append((raw, "out of range"))
            except ValueError:
                rejected.append((raw, "invalid number"))
        print(valid)
        print(rejected)

**Expected output**
    
    [88, 72]
        [('oops', 'invalid number'), ('', 'invalid number')]

**Narration:**

Predict the result before running the example. Compare the output with your prediction and explain the result in your own words. If it differs, inspect the input and change one thing at a time.

## Scene 3 — Test the boundary

**Visual:** Use a fresh example and the same uncluttered code-first visual style as the lesson.

**Narration:**

A boundary is a value at the edge of the allowed range. Test zero and one hundred, then test values just outside the range. A validation function should make these decisions predictable.

**Code**
    
    print(0 <= 0 <= 100)
        print(0 <= 100 <= 100)
        print(0 <= -1 <= 100)
        print(0 <= 101 <= 100)

**Expected output**
    
    True
        True
        False
        False

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
