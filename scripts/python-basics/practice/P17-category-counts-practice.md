# PyLearn Guided Practice 17 — Category Counts

> **MANDATORY VOICE SETTINGS — DO NOT CHANGE**
> - Voice: Kendrick
> - Model: ElevenLabs v3
> - Voice ID: exact approved Kendrick voice ID is not recorded in the reviewed repository files; insert the verified ID from the original Runway setup before generation.
> - No guessed ID, substitution, or preset; use the same approved voice identity throughout.
> - Speak narration only; do not read headings or bracketed production notes aloud.

**Canonical source:** `Pylearn-build260/content/python-basics/17-build-grade-distribution.md`, branch `ccr-c7f6fdd7-xpzi3g`.
**Target runtime:** Approximately 2–4 minutes.
**Purpose:** Separate guided-practice companion using fresh examples; never reveal the required app exercise solution.

## Scene 1 — Classify a different set of values

**Narration:** Let's practice category rules with fictional delivery speeds, not the grade-distribution project.

```python
speed = 42
if speed >= 50:
    category = "Fast"
elif speed >= 30:
    category = "Medium"
else:
    category = "Slow"
print(category)
```

**Expected output:** `Medium`

**Narration:** Python checks conditions from top to bottom and stops at the first true condition.

## Scene 2 — Count labels

```python
labels = ["Fast", "Medium", "Fast", "Slow", "Medium"]
counts = {}
for label in labels:
    counts[label] = counts.get(label, 0) + 1
print(counts)
```

**Expected output:** `{'Fast': 2, 'Medium': 2, 'Slow': 1}`

**Narration:** The dictionary stores one key per category and updates its count each time the label appears. This is a frequency table.

## Close — Complete the exercise

**Visual:** Use a simple end card: “Your turn: Complete the exercise”. Do not show or describe unfinished PyLearn app screens.

**Narration:** Great job! Now it's your turn. Complete the exercise to unlock the next lesson. If you'd like more hands-on practice, you can also try the practice in the PyLearn app. Keep going!

## Production checklist
- [x] Approved Kendrick / ElevenLabs v3 voice setup confirmed by the user; use the existing configuration without substitution.
- [x] Use the approved Kendrick voice with ElevenLabs v3, as confirmed by the user.
- [ ] Verify code and expected outputs in Python.
- [ ] Keep output synchronized with narration.
- [ ] Do not reveal the required app exercise solution.
- [x] End by telling the learner to complete the exercise to unlock the next lesson; app practice is optional.
