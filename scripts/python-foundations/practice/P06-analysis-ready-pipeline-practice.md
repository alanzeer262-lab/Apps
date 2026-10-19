# PyLearn Guided Practice — Pipeline Practice

**Voice lock:** Use the approved Kendrick voice with ElevenLabs v3; do not substitute another voice.
**Canonical source:** Pylearn-build260/content/python-foundations/modules/06-analysis-ready-pipeline.md, branch ccr-c7f6fdd7-xpzi3g.
**Purpose:** Separate practice companion using fresh examples. Never reveal the required app exercise solution.
**Track 2 practice visuals:** Show the data pipeline as connected stages with a visible rejected-record side lane. Pause on the row count and cleaning decision, then reveal the outcome. Use the toolkit progress rail and a restrained charcoal/teal palette; keep the teacher and voice unchanged.

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


## Production-critical rule — traceable transformation and truthful results
- Show the sequence explicitly: **source/input → each meaningful transformation → final output**. Use the actual data and code from this script; keep transitions readable and in causal order. Do not jump-cut from input to a result without showing or explaining the operation that produced it.
- Whenever a result is shown, it must be the exact output produced by running the displayed code against the displayed sample data. Verify it in Python before rendering. If it has not been run and verified, do not present it as a real result; mark it as a schematic illustration or omit the value.
- For the toolkit-build and capstone scenes, show the real end-to-end result learners can reproduce by building the tool themselves. No fabricated dashboard metrics, invented report rows, decorative “success” values, or output inconsistent with the code/data. Keep the sample dataset, code, and displayed result synchronized.
- For practice videos, use the script's own independent example and verify that example. Do not reveal the required PyLearn exercise solution.


**Visual transition rule for this practice:** Show each record entering the pipeline, then visibly separate accepted and rejected rows according to the displayed cleaning rule. Keep the rejected lane visible when summarizing; every count and average must come from the current sample, not a generic dashboard template.
