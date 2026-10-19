# PyLearn Guided Practice 16 — Progress Analyzer

> **MANDATORY VOICE SETTINGS — DO NOT CHANGE**
> - Voice: Kendrick
> - Model: ElevenLabs v3
> - Voice ID: exact approved Kendrick voice ID is not recorded in the reviewed repository files; insert the verified ID from the original Runway setup before generation.
> - No guessed ID, substitution, or preset; same approved voice throughout.
> - Speak narration only; do not read headings or bracketed production notes aloud.

**Canonical source:** `Pylearn-build260/content/python-basics/modules/16-build-progress-analyzer.md`, branch `ccr-c7f6fdd7-xpzi3g`.
**Target runtime:** Approximately 2–4 minutes.
**Purpose:** Separate guided-practice companion using fresh examples; do not reveal the required app exercise solution.

## Scene 1 — Count daily habit records

```python
days = [1, 2, 1, 3]
total = 0
for day_count in days:
    total += day_count
print(total)
```

**Expected output:** `7`

**Narration:** The accumulator starts at zero and adds each daily count. The total is seven.

## Scene 2 — Find the largest day

```python
days = [1, 2, 1, 3]
print(max(days))
```

**Expected output:** `3`

**Narration:** Max finds the largest value in the list. This can help describe the highest daily count, but it doesn't tell us which date it came from unless we keep that information in our records.

## Scene 3 — Keep input order

**Narration:** When processing records, preserve the order if the project asks for it. Try changing the list and predict how the total and maximum will change.

## Close — Complete the exercise

**Visual:** Use a simple end card: “Your turn: Complete the exercise”. Do not show or describe unfinished PyLearn app screens.

**Narration:** Great job! Now it's your turn. Complete the exercise to unlock the next lesson. If you'd like more hands-on practice, you can also try the practice in the PyLearn app. Keep going!

## Production checklist
- [x] Approved Kendrick / ElevenLabs v3 voice setup confirmed by the user; use the existing configuration without substitution.
- [x] Use the approved Kendrick voice with ElevenLabs v3, as confirmed by the user.
- [ ] Verify code and outputs in Python.
- [ ] Keep code/output synchronized with narration.
- [ ] Do not reveal required app exercise solutions.
- [x] End by telling the learner to complete the exercise to unlock the next lesson; app practice is optional.
