# PyLearn Video — Build: Validate Intake

**Track 2 visual identity:** Keep the same teacher and pacing. Use a validation gate motif: incoming records pass through visible rule checks, accepted rows continue in teal, rejected rows move to a side queue with concise reasons. Add a number-line boundary visual for range checks. Keep the stage rail visible with “Validate” highlighted.

**Voice lock:** Use the user-approved Kendrick voice with ElevenLabs v3. Do not substitute another voice.
**Canonical source:** Pylearn-build260/content/python-foundations/modules/08-build-validate.md, branch ccr-c7f6fdd7-xpzi3g.
**Production rule:** Narrate only spoken text. Do not show the required app exercise solution or invent app screens.

## Scene 1 — Validation is a gate

**Visual:** Show a short list of scores, then highlight values outside the allowed range.

**Narration:**

A score of one hundred and fifty or minus one can quietly distort every number in a report. Validation checks whether a record meets the rules before it is included in calculations. We keep validation separate from loading so each stage has one testable job.

**Code**

    scores = [88, 150, -1, 72]
    valid = [score for score in scores if 0 <= score <= 100]
    print(valid)

**Expected output**

    [88, 72]

**Narration:**

This demonstration uses a range from zero to one hundred. In your toolkit, keep track of rejected rows and the reason each one failed.

## Scene 2 — Conversion can fail

**Visual:** Run the conversion example separately, then show the guarded version.

**Narration:**

CSV values arrive as text. A word like oops or an empty string cannot be converted to an integer. Catch that failure and report it instead of crashing the whole pipeline.

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

There are two failure reasons here. Keeping them distinct makes the final report more useful.

## Scene 3 — Test boundaries

**Narration:**

Test the edge of the allowed range: zero and one hundred should pass, while values just outside the range should fail.

**Code**

    for value in [0, 100, -1, 101]:
        print(value, 0 <= value <= 100)

**Expected output**

    0 True
    100 True
    -1 False
    101 False

A validation function makes these decisions predictable. The summary should receive validated records, not invent its own rules.

## Recap and handoff

You've learned why validation is a separate gate, how conversion errors happen, and why boundary tests matter. Next, watch the practice video, then complete the exercise to unlock the next lesson. You can also practise in the PyLearn app if you want extra hands-on work.

## Final production checklist

- [ ] Verify each code sample and stated output in Python.
- [ ] Reveal code before running it and output only after the run.
- [ ] Keep narration separate from visual directions.
- [ ] Watch the complete rendered video at normal speed before approval.
