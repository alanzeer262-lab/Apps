# PyLearn Guided Practice — Pipeline Practice

**Voice lock:** Use the approved Kendrick voice with ElevenLabs v3; do not substitute another voice.
**Canonical source:** Pylearn-build260/content/python-foundations/modules/10-build-pipeline.md, branch ccr-c7f6fdd7-xpzi3g.
**Purpose:** Separate practice companion; do not reveal the required exercise implementation or hidden evaluation answers.

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
