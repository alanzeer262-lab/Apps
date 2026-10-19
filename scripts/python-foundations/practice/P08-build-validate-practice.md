# PyLearn Guided Practice — Validation Practice

**Voice lock:** Use the approved Kendrick voice with ElevenLabs v3; do not substitute another voice.
**Canonical source:** Pylearn-build260/content/python-foundations/modules/08-build-validate.md, branch ccr-c7f6fdd7-xpzi3g.
**Purpose:** Separate practice companion; do not reveal the required exercise implementation or hidden evaluation answers.

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
