# PyLearn Guided Practice — Pipeline Practice

**Voice lock:** Use the approved Kendrick voice with ElevenLabs v3; do not substitute another voice.
**Canonical source:** Pylearn-build260/content/python-foundations/modules/10-build-pipeline.md, branch ccr-c7f6fdd7-xpzi3g.
**Purpose:** Separate practice companion; do not reveal the required exercise implementation or hidden evaluation answers.
**Track 2 practice visuals:** Animate records through Load → Validate → Summarize. Pause at each handoff and ask what should happen next. Finish with a report wireframe showing categories of information, not the solution to the required app exercise.

## Scene 1 — Check the order

**Narration:** A pipeline should load, validate, and then summarize. Reversing those steps can let bad records influence the final numbers.

**Code**

    stages = ["load", "validate", "summarize"]
    print(" -> ".join(stages))

**Expected output**

    load -> validate -> summarize

This reminds us of the intended sequence. Each step should receive predictable input and return a documented result.

## Scene 2 — Make the report useful

**Code**

    report = {
        "rows_read": 4,
        "valid_rows": 3,
        "invalid_rows": 1,
        "warning": "one score was not numeric",
    }
    print(report["rows_read"] - report["valid_rows"])

**Expected output**

    1

**Narration:** These values illustrate the shape of a report; they are not the solution to the required app exercise. Use your own input and tests to check the completed toolkit.

## Production checklist
- [ ] Use approved Kendrick / ElevenLabs v3 voice.
- [ ] Verify code and output before rendering.
- [ ] Keep the examples separate from the required app exercise.
- [ ] Keep narration and visual directions separate.
- [ ] Watch the full render before approval.


## Production-critical rule — traceable transformation and truthful results
- Show the sequence explicitly: **source/input → each meaningful transformation → final output**. Use the actual data and code from this script; keep transitions readable and in causal order. Do not jump-cut from input to a result without showing or explaining the operation that produced it.
- Any result shown must be the exact output produced by running the displayed code against the displayed sample data. Verify it in Python before rendering. If it has not been run and verified, do not present it as a real result; mark it as schematic or omit the value.
- For toolkit-build and capstone scenes, show the real end-to-end result learners can reproduce by building the tool themselves. No fabricated dashboard metrics, invented report rows, decorative success values, or output inconsistent with the code/data. Keep sample dataset, code, and displayed result synchronized.
- For practice videos, use the script's own independent example and verify it. Do not reveal the required PyLearn exercise solution.
