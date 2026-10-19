# PyLearn Guided Practice 02 — Variables and Types

> **MANDATORY VOICE SETTINGS — DO NOT CHANGE**
> - Voice: Kendrick
> - Model: ElevenLabs v3
> - Voice ID: exact approved Kendrick voice ID is not recorded in the reviewed repository files; insert the verified ID from the original Runway setup before generation.
> - No guessed ID, substitution, or preset; use the same approved voice identity throughout.
> - Speak narration only; do not read scene headings or bracketed production notes aloud.

**Canonical source:** `Pylearn-build260/content/python-basics/modules/02-variables-types.md`, branch `ccr-c7f6fdd7-xpzi3g`.
**Target runtime:** Approximately 2–4 minutes.
**Purpose:** Separate guided-practice companion using fresh examples; never reveal the required app exercise solution.

## Scene 1 — Give values names

**Visual:** Reveal each assignment one line at a time.

**Code**
```python
course = "Python"
minutes = 25
rating = 4.5
is_ready = True
```

**Narration:** These variables store four different kinds of values. Course is text, minutes is a whole number, rating is a decimal number, and is_ready is a Boolean.

## Scene 2 — Inspect the types

**Code**
```python
print(type(course))
print(type(minutes))
print(type(rating))
print(type(is_ready))
```

**Expected output**
```text
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

**Narration:** Type tells us what kind of value Python is working with. Use it when a value behaves unexpectedly instead of guessing.

## Scene 3 — Convert numeric text

**Code**
```python
minutes_text = "25"
minutes_value = int(minutes_text)
print(minutes_value + 5)
```

**Expected output:** `30`

**Narration:** The string contains digits that can be converted to an integer. Once converted, Python can perform arithmetic with it. Predict the output, run the code, then try changing the text to a valid different number.

## Scene 4 — Notice invalid input

**Visual:** In a separate run, change the text to `"twenty-five"` and demonstrate the conversion error. Keep this failing example separate from the valid conversion code, and explain the error before moving on.

**Code — expected ValueError**
```python
minutes_text = "twenty-five"
minutes_value = int(minutes_text)
```

**Expected result:** Python raises a `ValueError` because the text is not a valid integer representation.

**Narration:** Words such as twenty-five are not written as integer digits, so int cannot convert them directly. A real program needs a deliberate rule for invalid input.

## Close — Navigate to the real task

**Narration:** Now open PyLearn and find the required coding exercise for Lesson 2. This companion is extra practice, not the graded exercise. Complete the required exercise and pass it to unlock the next lesson.

## Production checklist
- [ ] Verify the exact approved Kendrick voice ID before generating audio.
- [ ] Use ElevenLabs v3 with the same approved voice identity.
- [ ] Verify all code and outputs in Python.
- [ ] Keep code and output synchronized with narration.
- [ ] Do not reveal the required app exercise solution.
- [ ] End by directing the learner to the required PyLearn exercise.
