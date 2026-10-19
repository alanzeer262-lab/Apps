# PyLearn Guided Practice 19 — Imperfect Input

> **MANDATORY VOICE SETTINGS — DO NOT CHANGE**
> - Voice: Kendrick
> - Model: ElevenLabs v3
> - Voice ID: exact approved Kendrick voice ID is not recorded in the reviewed repository files; insert the verified ID from the original Runway setup before generation.
> - No guessed ID, substitution, or preset; use the same approved voice identity throughout.
> - Speak narration only; do not read headings or bracketed production notes aloud.

**Canonical source:** `Pylearn-build260/content/python-basics/19-build-messy-input.md`, branch `ccr-c7f6fdd7-xpzi3g`.
**Target runtime:** Approximately 2–4 minutes.
**Purpose:** Separate guided-practice companion using fresh examples; never reveal the required app exercise solution.

## Scene 1 — Clean a quantity

```python
raw_quantity = " 12 "
quantity = int(raw_quantity.strip())
print(quantity + 3)
```

**Expected output:** `15`

**Narration:** Strip removes surrounding spaces. Then int converts the cleaned text into a whole number.

## Scene 2 — Handle invalid text

```python
raw_quantity = "many"
try:
    quantity = int(raw_quantity)
except ValueError:
    quantity = None
print(quantity is None)
```

**Expected output:** `True`

**Narration:** The word many cannot be converted to an integer. The except block handles the expected conversion error and uses None to indicate there is no valid quantity.

## Scene 3 — Do not silently replace bad data

**Narration:** An invalid quantity is not automatically zero. Zero is a real quantity; invalid means the input could not be interpreted. Keep that distinction in your data-quality decisions.

## Close

**Narration:** Open PyLearn and find the Handle Imperfect Scores project task. This practice uses quantities, not the required records. Complete and pass the project exercise to unlock the next lesson.

## Production checklist
- [ ] Verify the exact approved Kendrick voice ID before generation.
- [ ] Use ElevenLabs v3 with the same approved voice identity.
- [ ] Verify code and expected outputs in Python.
- [ ] Keep output synchronized with narration.
- [ ] Do not reveal the required app exercise solution.
- [ ] End by directing the learner to the required PyLearn task.
