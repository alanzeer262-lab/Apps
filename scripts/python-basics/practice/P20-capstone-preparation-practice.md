# PyLearn Guided Practice 20 — Capstone Preparation

> **MANDATORY VOICE SETTINGS — DO NOT CHANGE**
> - Voice: Kendrick
> - Model: ElevenLabs v3
> - Voice setup: user confirmed the approved Kendrick / ElevenLabs v3 setup is settled; use the existing approved configuration without substitution.
> - No guessed ID, substitution, or preset; use the same approved voice identity throughout.
> - Speak narration only; do not read headings or bracketed production notes aloud.

**Canonical source:** `Pylearn-build260/content/python-basics/../projects/capstone-gradebook.md`, branch `ccr-c7f6fdd7-xpzi3g`.
**Target runtime:** Approximately 2–4 minutes.
**Purpose:** Separate guided-practice companion using fresh examples; never reveal the required app exercise solution.

## Scene 1 — Inspect two unrelated records

**Visual:** Use a small, unrelated example about plants, not the capstone gradebook data.

```python
plants = [
    ("Basil", 4),
    ("Mint", 2)
]
for name, leaves in plants:
    print(name, leaves)
```

**Expected output**
```text
Basil 4
Mint 2
```

**Narration:** Each tuple keeps a name and a count together. The loop unpacks the pair into two variables and prints the fields.

## Scene 2 — State a rule before coding

**Narration:** Imagine a plant is ready to repot when it has at least three leaves. Before writing a condition, say the rule in plain English: the leaf count must be greater than or equal to three.

```python
leaves = 4
print(leaves >= 3)
```

**Expected output:** `True`

**Narration:** This example practices reading a record and checking a rule. It does not implement any capstone milestone.

## Scene 3 — Prepare for the capstone

**Narration:** In the capstone, inspect the records first, then solve one milestone at a time. Do not try to write the entire program in one pass. Make a prediction, test a small piece, and use feedback to refine your work.

## Close — Complete the exercise

**Visual:** Use a simple end card: “Your turn: Complete the exercise”. Do not show or describe unfinished PyLearn app screens or reveal the capstone solution.

**Narration:** Great job! Now it's your turn. Complete the exercise to unlock the next lesson. If you'd like more hands-on practice, you can also try the practice in the PyLearn app. Keep going!

## Production checklist
- [x] Approved Kendrick / ElevenLabs v3 voice setup confirmed by the user; use the existing configuration without substitution.
- [x] Use the approved Kendrick voice with ElevenLabs v3, as confirmed by the user.
- [ ] Verify code and expected outputs in Python.
- [ ] Keep output synchronized with narration.
- [ ] Do not reveal the required app exercise solution.
- [x] End by telling the learner to complete the exercise to unlock the next lesson; app practice is optional.
