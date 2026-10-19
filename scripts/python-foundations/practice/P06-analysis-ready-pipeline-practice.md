# PyLearn Guided Practice — Pipeline Practice

**Voice lock:** Use the approved Kendrick voice with ElevenLabs v3; do not substitute another voice.
**Canonical source:** Pylearn-build260/content/python-foundations/modules/06-analysis-ready-pipeline.md, branch ccr-c7f6fdd7-xpzi3g.
**Purpose:** Separate practice companion using fresh examples. Never reveal the required app exercise solution.

## Scene 1 — Inspect first

**Narration:** Here are four raw values. Count the rows before cleaning so you can explain what happened to the input.

**Code**

    raw = ["10", "20", "unknown", "30"]
    print("Rows read:", len(raw))

**Expected output**

    Rows read: 4

The original row count belongs in the report even if some values are later rejected.

## Scene 2 — Keep valid numbers separate

**Code**

    valid = []
    invalid = []
    for item in raw:
        try:
            valid.append(int(item))
        except ValueError:
            invalid.append(item)
    print(valid)
    print(invalid)

**Expected output**

    [10, 20, 30]
    ['unknown']

**Narration:** Now calculate an average only from valid numbers and report how many values were rejected. A reader should not have to guess what your result includes.

## Close — Complete the exercise

**Visual:** End card: “Your turn: Complete the exercise”. Do not show unfinished PyLearn app screens.

**Narration:** Good work. Now complete the exercise to unlock the next lesson. Use the habits from this practice: test small cases, check assumptions, and change one thing at a time. If you'd like extra hands-on practice, you can also try it in the PyLearn app.

## Production checklist
- [ ] Use approved Kendrick / ElevenLabs v3 voice.
- [ ] Verify all code and outputs in Python.
- [ ] Keep examples distinct from the required app exercise.
- [ ] Keep code and output synchronized with narration.
- [ ] Watch the full render before approval.
