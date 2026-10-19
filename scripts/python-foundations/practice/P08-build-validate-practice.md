# PyLearn Guided Practice — Validation Practice

**Voice lock:** Use the approved Kendrick voice with ElevenLabs v3; do not substitute another voice.
**Canonical source:** Pylearn-build260/content/python-foundations/modules/08-build-validate.md, branch ccr-c7f6fdd7-xpzi3g.
**Purpose:** Separate practice companion; do not reveal the required exercise implementation or hidden evaluation answers.
**Track 2 practice visuals:** Use a validation gate and number-line boundaries. Pause while each value approaches the gate, then reveal whether it passes and why. Show rejection reasons in a side queue. Use the same teacher and restrained visual palette.

## Scene 1 — Apply a range rule

**Narration:** For this example, scores must be between zero and one hundred inclusive. Values outside that range should not be included in the summary.

**Code**

    values = [0, 64, 100, -3, 104]
    valid = [value for value in values if 0 <= value <= 100]
    print(valid)

**Expected output**

    [0, 64, 100]

The rule includes both boundaries. Test the edge values instead of relying only on typical scores.

## Scene 2 — Record the reason

**Code**

    rejected = [("oops", "invalid number"), (104, "out of range")]
    for value, reason in rejected:
        print(value, "-", reason)

**Expected output**

    oops - invalid number
    104 - out of range

**Narration:** Different problems deserve clear reasons. Keep the rule consistent and test it with valid and invalid examples.

## Production checklist
- [ ] Use approved Kendrick / ElevenLabs v3 voice.
- [ ] Verify code and output before rendering.
- [ ] Keep the examples separate from the required app exercise.
- [ ] Keep narration and visual directions separate.
- [ ] Watch the full render before approval.


## Production-critical rule — traceable transformation and truthful results
- Show the sequence explicitly: **source/input → each meaningful transformation → final output**. Use the actual data and code from this script; keep transitions readable and in causal order. Do not jump-cut from input to a result without showing or explaining the operation that produced it.
- Whenever a result is shown, it must be the exact output produced by running the displayed code against the displayed sample data. Verify it in Python before rendering. If it has not been run and verified, do not present it as a real result; mark it as a schematic illustration or omit the value.
- For the toolkit-build and capstone scenes, show the real end-to-end result learners can reproduce by building the tool themselves. No fabricated dashboard metrics, invented report rows, decorative “success” values, or output inconsistent with the code/data. Keep the sample dataset, code, and displayed result synchronized.
- For practice videos, use the script's own independent example and verify that example. Do not reveal the required PyLearn exercise solution.


**Visual transition rule for this practice:** Show each raw value approaching the gate, run conversion before checking the 0–100 range, and route rejected values with their actual reasons. Reveal the valid list and rejection list only after the loop finishes.
