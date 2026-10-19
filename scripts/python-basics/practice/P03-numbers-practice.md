# PyLearn Guided Practice 03 — Numbers

> **MANDATORY VOICE SETTINGS — DO NOT CHANGE**
> - Voice: Kendrick
> - Model: ElevenLabs v3
> - Voice ID: exact approved Kendrick voice ID is not recorded in the reviewed repository files; insert the verified ID from the original Runway setup before generation.
> - No guessed ID, substitution, or preset; use the same approved voice identity throughout.
> - Speak narration only; do not read scene headings or bracketed production notes aloud.

**Canonical source:** `Pylearn-build260/content/python-basics/modules/03-numbers-operators.md`, branch `ccr-c7f6fdd7-xpzi3g`.
**Target runtime:** Approximately 2–4 minutes.
**Purpose:** Separate guided-practice companion using fresh examples; never reveal the required app exercise solution.

## Scene 1 — Convert minutes

**Visual:** Show the total and ask for a prediction before revealing output.

**Code**
```python
practice_minutes = 245
print(practice_minutes / 60)
```

**Narration:** Normal division converts minutes into decimal hours. Predict the approximate result before running it.

**Expected output:** `4.083333333333333`

## Scene 2 — Full hours and remainder

**Code**
```python
practice_minutes = 245
print(practice_minutes // 60)
print(practice_minutes % 60)
```

**Expected output**
```text
4
5
```

**Narration:** Two slashes count complete hours. Percent gives the leftover minutes. Together, they represent the same duration in a different way.

## Scene 3 — Rounding

**Code**
```python
print(round(245 / 60, 1))
```

**Expected output:** `4.1`

**Narration:** Round displays the value to one decimal place. Now change the total to a different number of minutes and predict all three results before running it.

## Close — Navigate to the real task

**Narration:** Now open PyLearn and find the required coding exercise for Lesson 3. This companion is separate practice and does not unlock the next lesson. Complete and pass the required app exercise.

## Production checklist
- [ ] Verify the exact approved Kendrick voice ID before generating audio.
- [ ] Use ElevenLabs v3 with the same approved voice identity.
- [ ] Verify all code and outputs in Python.
- [ ] Keep code and output synchronized with narration.
- [ ] Do not reveal the required app exercise solution.
- [ ] End by directing the learner to the required PyLearn exercise.
