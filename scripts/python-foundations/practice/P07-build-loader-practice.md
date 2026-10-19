# PyLearn Guided Practice — Loader Practice

**Voice lock:** Use the approved Kendrick voice with ElevenLabs v3; do not substitute another voice.
**Canonical source:** Pylearn-build260/content/python-foundations/modules/07-build-loader.md, branch ccr-c7f6fdd7-xpzi3g.
**Purpose:** Separate practice companion; do not reveal the required exercise implementation or hidden evaluation answers.
**Track 2 practice visuals:** Use a loader workbench: file card, field inspector, and a highlighted raw value. Keep “Load” active on a small toolkit progress rail. Pause to ask what type a value has before revealing the answer; don't rely on repeated input/output boxes.

## Scene 1 — Trim a field

**Narration:** Let's practise with a small CSV-shaped input. Extra spaces can make values inconsistent, so trimming is a useful loader responsibility.

**Code**

    raw_name = "  Noor  "
    raw_score = " 84 "
    print(raw_name.strip())
    print(raw_score.strip())

**Expected output**

    Noor
    84

Trimming removes surrounding whitespace. It does not convert the score to a number or decide whether it is in range.

## Scene 2 — Keep loading focused

**Code**

    parsed_score = raw_score.strip()
    print(type(parsed_score))

**Expected output**

    <class 'str'>

**Narration:** The value is still a string. That is expected at the loading stage; conversion and validation belong in the next stage.

## Production checklist
- [ ] Use approved Kendrick / ElevenLabs v3 voice.
- [ ] Verify code and output before rendering.
- [ ] Keep the examples separate from the required app exercise.
- [ ] Keep narration and visual directions separate.
- [ ] Watch the full render before approval.
