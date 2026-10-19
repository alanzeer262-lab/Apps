# PyLearn Guided Practice 05 — Booleans

> **MANDATORY VOICE SETTINGS — DO NOT CHANGE**
> - Voice: Kendrick
> - Model: ElevenLabs v3
> - Voice ID: exact approved Kendrick voice ID is not recorded in the reviewed repository files; insert the verified ID from the original Runway setup before generation.
> - No guessed ID, substitution, or preset; use the same approved voice identity throughout.
> - Speak narration only; do not read scene headings or bracketed production notes aloud.

**Canonical source:** `Pylearn-build260/content/python-basics/modules/05-booleans.md`, branch `ccr-c7f6fdd7-xpzi3g`.
**Target runtime:** Approximately 2–4 minutes.
**Purpose:** Separate guided-practice companion using fresh examples; never reveal the required app exercise solution.

## Scene 1 — Check a temperature range

**Visual:** Introduce a fictional temperature and a simple rule.

**Code**
```python
temperature = 22
print(temperature >= 18)
print(temperature <= 26)
```

**Expected output**
```text
True
True
```

**Narration:** The first comparison asks whether the temperature is at least eighteen. The second asks whether it is at most twenty-six. Both are true for twenty-two.

## Scene 2 — Combine the conditions

**Code**
```python
temperature = 22
comfortable = temperature >= 18 and temperature <= 26
print(comfortable)
```

**Expected output:** `True`

**Narration:** And requires both comparisons to be true. Now change the temperature to seventeen and predict the result before running it.

## Scene 3 — Test the boundary

**Visual:** Change only the temperature value and run each case separately. Keep the same comparison visible.

**Code — start with 17**
```python
temperature = 17
print(temperature >= 18 and temperature <= 26)
```

**Expected output:** `False`

Now change the value to `18`, then `26`, then `27`, running after each change.

**Expected results, in order:** `True`, `True`, `False`

**Narration:** Boundary values help us check whether the rule is correct. Eighteen and twenty-six are included because we used greater-than-or-equal and less-than-or-equal. Seventeen and twenty-seven are outside the range.

## Close — Navigate to the real task

**Narration:** Now open PyLearn and find the required coding exercise for Lesson 5. This companion is extra practice, not a substitute for the required exercise that unlocks the next lesson.

## Production checklist
- [ ] Verify the exact approved Kendrick voice ID before generating audio.
- [ ] Use ElevenLabs v3 with the same approved voice identity.
- [ ] Verify all code and outputs in Python.
- [ ] Keep code and output synchronized with narration.
- [ ] Do not reveal the required app exercise solution.
- [ ] End by directing the learner to the required PyLearn exercise.
