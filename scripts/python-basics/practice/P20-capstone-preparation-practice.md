# PyLearn Guided Practice 20 — Capstone Preparation

> **MANDATORY VOICE SETTINGS — DO NOT CHANGE**
> - Voice: Kendrick
> - Model: ElevenLabs v3
> - Voice ID: exact approved Kendrick voice ID is not recorded in the reviewed repository files; insert the verified ID from the original Runway setup before generation.
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

## Close

**Narration:** Open PyLearn and enter Mini Gradebook Capstone. Start with Milestone 1, submit your work, read the feedback, and fix what you need to fix before moving on. Work through the milestones one at a time. The solution is yours to build.

## Production checklist
- [ ] Verify the exact approved Kendrick voice ID before generation.
- [ ] Use ElevenLabs v3 with the same approved voice identity.
- [ ] Verify code and expected outputs in Python.
- [ ] Keep output synchronized with narration.
- [ ] Do not reveal the required app exercise solution.
- [ ] End by directing the learner to the required PyLearn task.
