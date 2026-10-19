# PyLearn Guided Practice 15 — Score Summary

> **MANDATORY VOICE SETTINGS — DO NOT CHANGE**
> - Voice: Kendrick
> - Model: ElevenLabs v3
> - Voice ID: exact approved Kendrick voice ID is not recorded in the reviewed repository files; insert the verified ID from the original Runway setup before generation.
> - No guessed ID, substitution, or preset; same approved voice throughout.
> - Speak narration only; do not read headings or bracketed production notes aloud.

**Canonical source:** `Pylearn-build260/content/python-basics/modules/15-build-score-summary.md`, branch `ccr-c7f6fdd7-xpzi3g`.
**Target runtime:** Approximately 2–4 minutes.
**Purpose:** Separate guided-practice companion using fresh examples; do not reveal the required app exercise solution.

## Scene 1 — Summarize delivery ratings

```python
ratings = [3, 5, 4, 2]
print(len(ratings))
print(sum(ratings) / len(ratings))
print(max(ratings))
print(min(ratings))
```

**Expected output**
```text
4
3.5
5
2
```

**Narration:** This example summarizes fictional delivery ratings. Len counts the values, the average is total divided by count, and max and min find the highest and lowest.

## Scene 2 — Test a threshold

```python
rating = 4
threshold = 4
print(rating >= threshold)
```

**Expected output:** `True`

**Narration:** The boundary is included because the rule uses greater-than-or-equal. Test the value below, exactly at, and above the threshold.

## Scene 3 — Empty data

**Narration:** If the list is empty, dividing by its length would divide by zero. A summary function needs a deliberate empty-case result.

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
