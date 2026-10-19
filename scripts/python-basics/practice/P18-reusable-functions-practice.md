# PyLearn Guided Practice 18 — Reusable Functions

> **MANDATORY VOICE SETTINGS — DO NOT CHANGE**
> - Voice: Kendrick
> - Model: ElevenLabs v3
> - Voice ID: exact approved Kendrick voice ID is not recorded in the reviewed repository files; insert the verified ID from the original Runway setup before generation.
> - No guessed ID, substitution, or preset; use the same approved voice identity throughout.
> - Speak narration only; do not read headings or bracketed production notes aloud.

**Canonical source:** `Pylearn-build260/content/python-basics/18-build-toolkit.md`, branch `ccr-c7f6fdd7-xpzi3g`.
**Target runtime:** Approximately 2–4 minutes.
**Purpose:** Separate guided-practice companion using fresh examples; never reveal the required app exercise solution.

## Scene 1 — A helper with one job

```python
def total_pages(pages):
    return sum(pages)

print(total_pages([10, 20, 30]))
```

**Expected output:** `60`

**Narration:** The function has one job: total the page counts and return the result.

## Scene 2 — Reuse the helper

```python
first_total = total_pages([12, 8])
second_total = total_pages([25, 15])
print(first_total)
print(second_total)
```

**Expected output**
```text
20
40
```

**Narration:** The same function works with different inputs. That is the benefit of giving reusable behavior a clear name.

## Scene 3 — Empty input

**Narration:** Consider what your function should return when the list is empty. The correct rule depends on the task; don't assume every function has the same empty-case behavior.

## Close

**Narration:** Open PyLearn and find the Reusable Analysis Toolkit project task. This companion uses page counts, not the required project functions. Pass the required exercise to unlock the next lesson.

## Production checklist
- [ ] Verify the exact approved Kendrick voice ID before generation.
- [ ] Use ElevenLabs v3 with the same approved voice identity.
- [ ] Verify code and expected outputs in Python.
- [ ] Keep output synchronized with narration.
- [ ] Do not reveal the required app exercise solution.
- [ ] End by directing the learner to the required PyLearn task.
