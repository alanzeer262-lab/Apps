# PyLearn Guided Practice 11 — Comprehensions and Safe Conversion

> **MANDATORY VOICE SETTINGS — DO NOT CHANGE**
> - Voice: Kendrick
> - Model: ElevenLabs v3
> - Voice ID: exact approved Kendrick voice ID is not recorded in the reviewed repository files; insert the verified ID from the original Runway setup before generation.
> - No guessed ID, substitution, or preset; same approved voice throughout.
> - Speak narration only; do not read headings or bracketed production notes aloud.

**Canonical source:** `Pylearn-build260/content/python-basics/modules/11-comprehensions-imports.md`, branch `ccr-c7f6fdd7-xpzi3g`.
**Target runtime:** Approximately 2–4 minutes.
**Purpose:** Separate guided-practice companion using fresh examples; do not reveal the required app exercise solution.

## Scene 1 — Transform values

```python
numbers = [2, 4, 6]
doubled = [number * 2 for number in numbers]
print(doubled)
```

**Expected output:** `[4, 8, 12]`

**Narration:** The comprehension creates a new list by multiplying each number by two. Use it when the transformation is simple and easy to read.

## Scene 2 — Reuse a standard-library tool

```python
from statistics import mean
print(mean([10, 20, 30]))
```

**Expected output:** `20`

**Narration:** The import makes mean available from Python's statistics module. Reusing a standard-library tool can be clearer than writing the calculation yourself.

## Scene 3 — Handle invalid text

```python
def safe_int(value):
    try:
        return int(value)
    except ValueError:
        return None

print(safe_int("42"))
print(safe_int("oops"))
```

**Expected output**
```text
42
None
```

**Narration:** The first value converts successfully. The second raises ValueError, which the function handles by returning None. None represents the absence of a valid numeric value; it should not be confused with zero.

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
