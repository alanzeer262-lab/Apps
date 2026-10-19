# PyLearn Guided Practice 07 — Conditionals

> **MANDATORY VOICE SETTINGS — DO NOT CHANGE**
> - Voice: Kendrick
> - Model: ElevenLabs v3
> - Voice ID: exact approved Kendrick voice ID is not recorded in the reviewed repository files; insert the verified ID from the original Runway setup before generation.
> - No guessed ID, substitution, or preset; use the same approved voice identity throughout.
> - Speak narration only; do not read scene headings or bracketed production notes aloud.

**Canonical source:** `Pylearn-build260/content/python-basics/modules/07-conditionals.md`, branch `ccr-c7f6fdd7-xpzi3g`.
**Target runtime:** Approximately 2–4 minutes.
**Purpose:** Separate guided-practice companion using fresh examples; do not reveal the required app exercise solution.

## Scene 1 — Check a battery level

**Code**
```python
battery = 18
if battery <= 20:
    print("Low battery")
else:
    print("Battery okay")
```

**Expected output:** `Low battery`

**Narration:** The condition asks whether the battery level is twenty or lower. Since eighteen meets that rule, the first branch runs.

## Scene 2 — Add another category

**Code**
```python
battery = 55
if battery <= 20:
    status = "Low"
elif battery <= 60:
    status = "Medium"
else:
    status = "High"
print(status)
```

**Expected output:** `Medium`

**Narration:** Python checks branches from top to bottom and stops at the first true condition. Fifty-five is not twenty or lower, but it is sixty or lower, so status becomes Medium.

## Scene 3 — Test the boundaries

**Visual:** Change only the battery value in Scene 2 and run each case separately. Show the value and result after each run.

**Expected results**
- `battery = 20` → `Low`
- `battery = 21` → `Medium`
- `battery = 60` → `Medium`
- `battery = 61` → `High`

**Narration:** Test values just below, at, and above the thresholds. Twenty is still Low because the condition uses less-than-or-equal. Twenty-one enters Medium. Sixty is still Medium, while sixty-one becomes High. Boundary tests help you catch conditions that are too broad or too narrow.

## Close — Navigate to the real task

**Narration:** Open PyLearn and find the required coding exercise for Lesson 7. This companion is additional practice and does not unlock the next lesson. Pass the required exercise in PyLearn.

## Production checklist
- [ ] Verify the exact approved Kendrick voice ID before generation.
- [ ] Use ElevenLabs v3 with the same approved voice identity.
- [ ] Verify code and expected outputs in Python.
- [ ] Keep output synchronized with narration.
- [ ] Do not reveal the required app exercise solution.
- [ ] End by directing the learner to the required PyLearn exercise.
