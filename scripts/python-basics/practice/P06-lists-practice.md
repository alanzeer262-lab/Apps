# PyLearn Guided Practice 06 — Lists

> **MANDATORY VOICE SETTINGS — DO NOT CHANGE**
> - Voice: Kendrick
> - Model: ElevenLabs v3
> - Voice ID: exact approved Kendrick voice ID is not recorded in the reviewed repository files; insert the verified ID from the original Runway setup before generation.
> - No guessed ID, substitution, or preset; use the same approved voice identity throughout.
> - Speak narration only; do not read scene headings or bracketed production notes aloud.

**Canonical source:** `Pylearn-build260/content/python-basics/modules/06-lists.md`, branch `ccr-c7f6fdd7-xpzi3g`.
**Target runtime:** Approximately 2–4 minutes.
**Purpose:** Separate guided-practice companion using fresh examples; do not reveal the required app exercise solution.

## Scene 1 — Book page counts

**Code**
```python
pages = [120, 85, 210, 95]
print(len(pages))
print(sum(pages))
print(min(pages))
print(max(pages))
```

**Expected output**
```text
4
510
85
210
```

**Narration:** This list contains four books' page counts. Len counts the books, sum adds the pages, min finds the smallest count, and max finds the largest.

## Scene 2 — Select and update

**Code**
```python
pages = [120, 85, 210, 95]
print(pages[-1])
print(pages[1:3])
pages.append(160)
print(pages)
```

**Expected output**
```text
95
[85, 210]
[120, 85, 210, 95, 160]
```

**Narration:** Negative one selects the last item. The slice starts at index one and stops before index three. Append adds a new item at the end.

## Scene 3 — Think about empty lists

**Narration:** What would happen if the list were empty? Len would be zero, and an average calculation would divide by zero. A real program needs an explicit rule for this case.

**Visual:** Ask the learner to change one page count and predict which results will change.

## Close — Navigate to the real task

**Narration:** Open PyLearn and find the required coding exercise for Lesson 6. This is extra practice; only passing the required app exercise unlocks the next lesson.

## Production checklist
- [ ] Verify the exact approved Kendrick voice ID before generation.
- [ ] Use ElevenLabs v3 with the same approved voice identity.
- [ ] Verify code and expected outputs in Python.
- [ ] Keep output synchronized with narration.
- [ ] Do not reveal the required app exercise solution.
- [ ] End by directing the learner to the required PyLearn exercise.
