# PyLearn Guided Practice 14 — Clean Topics

> **MANDATORY VOICE SETTINGS — DO NOT CHANGE**
> - Voice: Kendrick
> - Model: ElevenLabs v3
> - Voice ID: exact approved Kendrick voice ID is not recorded in the reviewed repository files; insert the verified ID from the original Runway setup before generation.
> - No guessed ID, substitution, or preset; same approved voice throughout.
> - Speak narration only; do not read headings or bracketed production notes aloud.

**Canonical source:** `Pylearn-build260/content/python-basics/modules/14-build-topic-cleaner.md`, branch `ccr-c7f6fdd7-xpzi3g`.
**Target runtime:** Approximately 2–4 minutes.
**Purpose:** Separate guided-practice companion using fresh examples; do not reveal the required app exercise solution.

## Scene 1 — Clean a hobby list

```python
raw = "  hiking, cooking, hiking  "
clean = raw.strip()
parts = clean.split(",")
print(parts)
```

**Expected output**
```text
['hiking', ' cooking', ' hiking']
```

**Narration:** Strip removes outer whitespace from the whole string. Split breaks it at commas, but spaces around individual pieces may remain.

## Scene 2 — Normalize one item

```python
hobby = "  COOKING  "
print(hobby.strip().lower())
```

**Expected output:** `cooking`

**Narration:** Clean each piece by removing outer spaces and converting it to lowercase. A consistent rule helps avoid treating Cooking and cooking as different categories.

## Scene 3 — Check membership

```python
hobbies = ["hiking", "cooking", "reading"]
print("COOKING".lower() in hobbies)
```

**Expected output:** `True`

**Narration:** Normalize the search text to match the way the stored items are normalized.

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
