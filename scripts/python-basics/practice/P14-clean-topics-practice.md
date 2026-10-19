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

## Close

**Narration:** Open PyLearn and find the Clean My Learning Topics project task. This companion uses hobbies instead of the required project data. Pass the required project exercise to unlock the next lesson.

## Production checklist
- [ ] Verify exact approved Kendrick voice ID before generation.
- [ ] Use ElevenLabs v3 with the same approved voice identity.
- [ ] Verify code and outputs in Python.
- [ ] Keep code/output synchronized with narration.
- [ ] Do not reveal required app exercise solutions.
- [ ] End by directing the learner to the required PyLearn task.
