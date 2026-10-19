# PyLearn Guided Practice 09 — Dictionaries, Tuples, and Sets

> **MANDATORY VOICE SETTINGS — DO NOT CHANGE**
> - Voice: Kendrick
> - Model: ElevenLabs v3
> - Voice ID: exact approved Kendrick voice ID is not recorded in the reviewed repository files; insert the verified ID from the original Runway setup before generation.
> - No guessed ID, substitution, or preset; use the same approved voice identity throughout.
> - Speak narration only; do not read scene headings or bracketed production notes aloud.

**Canonical source:** `Pylearn-build260/content/python-basics/modules/09-dict-tuple-set.md`, branch `ccr-c7f6fdd7-xpzi3g`.
**Target runtime:** Approximately 2–4 minutes.
**Purpose:** Separate guided-practice companion using fresh examples; do not reveal the required app exercise solution.

## Scene 1 — A book record

**Code**
```python
book = {"title": "The Little Prince", "pages": 96}
print(book["title"])
print(book["pages"])
```

**Expected output**
```text
The Little Prince
96
```

**Narration:** The dictionary connects labels to values. We use the title key to retrieve the book's title and pages to retrieve its page count.

## Scene 2 — Unpack a tuple

**Code**
```python
record = ("The Hobbit", 310)
title, pages = record
print(f"{title}: {pages} pages")
```

**Expected output:** `The Hobbit: 310 pages`

**Narration:** The tuple keeps two related values together. Unpacking assigns the first item to title and the second to pages.

## Scene 3 — Remove duplicate tags

**Code**
```python
tags = {"fantasy", "classic", "fantasy"}
print(len(tags))
print("classic" in tags)
```

**Expected output**
```text
2
True
```

**Narration:** A set keeps unique values, so fantasy is stored once. Use a set when uniqueness and membership matter more than order.

## Close — Navigate to the real task

**Narration:** Open PyLearn and find the required coding exercise for Lesson 9. This is additional practice, not the graded task that unlocks the next lesson.

## Production checklist
- [ ] Verify the exact approved Kendrick voice ID before generation.
- [ ] Use ElevenLabs v3 with the same approved voice identity.
- [ ] Verify code and expected outputs in Python.
- [ ] Keep output synchronized with narration.
- [ ] Do not reveal the required app exercise solution.
- [ ] End by directing the learner to the required PyLearn exercise.
