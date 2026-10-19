# PyLearn Guided Practice 13 — Study Time Calculator

> **MANDATORY VOICE SETTINGS — DO NOT CHANGE**
> - Voice: Kendrick
> - Model: ElevenLabs v3
> - Voice ID: exact approved Kendrick voice ID is not recorded in the reviewed repository files; insert the verified ID from the original Runway setup before generation.
> - No guessed ID, substitution, or preset; same approved voice throughout.
> - Speak narration only; do not read headings or bracketed production notes aloud.

**Canonical source:** `Pylearn-build260/content/python-basics/modules/13-build-study-calculator.md`, branch `ccr-c7f6fdd7-xpzi3g`.
**Target runtime:** Approximately 2–4 minutes.
**Purpose:** Separate guided-practice companion using fresh examples; do not reveal the required app exercise solution.

## Scene 1 — Convert a different duration

```python
minutes = 95
print(minutes / 60)
print(minutes // 60)
print(minutes % 60)
```

**Expected output**
```text
1.5833333333333333
1
35
```

**Narration:** Normal division gives decimal hours. Floor division gives one complete hour, and modulo gives thirty-five minutes left over.

## Scene 2 — Average session length

```python
total_minutes = 80
sessions = 4
print(total_minutes / sessions)
```

**Expected output:** `20.0`

**Narration:** Average session length is total minutes divided by the number of sessions. Before using this formula in a function, decide what should happen if the session count is zero.

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
