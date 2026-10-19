# PyLearn Guided Practice 10 — Functions

> **MANDATORY VOICE SETTINGS — DO NOT CHANGE**
> - Voice: Kendrick
> - Model: ElevenLabs v3
> - Voice ID: exact approved Kendrick voice ID is not recorded in the reviewed repository files; insert the verified ID from the original Runway setup before generation.
> - No guessed ID, substitution, or preset; use the same approved voice identity throughout.
> - Speak narration only; do not read scene headings or bracketed production notes aloud.

**Canonical source:** `Pylearn-build260/content/python-basics/modules/10-functions.md`, branch `ccr-c7f6fdd7-xpzi3g`.
**Target runtime:** Approximately 2–4 minutes.
**Purpose:** Separate guided-practice companion using fresh examples; do not reveal the required app exercise solution.

## Scene 1 — Define a reusable conversion

**Code**
```python
def minutes_to_hours(minutes):
    return minutes / 60

hours = minutes_to_hours(90)
print(hours)
```

**Expected output:** `1.5`

**Narration:** The function takes minutes as input and returns hours. The parameter is minutes, and ninety is the argument in the call.

## Scene 2 — Reuse the result

**Code**
```python
hours = minutes_to_hours(90)
print(f"Hours: {hours}")
print(hours * 2)
```

**Expected output**
```text
Hours: 1.5
3.0
```

**Narration:** Because the function returns a value, we can store it and use it again. Return gives the answer back to the code; it does not display it by itself.

## Scene 3 — Compare print and return

**Code**
```python
def show_double(number):
    print(number * 2)

def double(number):
    return number * 2

saved = show_double(4)
print(saved)
```

**Expected output**
```text
8
None
```

**Narration:** The first function prints eight, but it does not return a value, so saved receives None. The second function returns a number that can be reused.

## Close — Complete the exercise

**Visual:** Use a simple end card: “Your turn: Complete the exercise”. Do not show or describe unfinished PyLearn app screens.

**Narration:** Great job! Now it's your turn. Complete the exercise to unlock the next lesson. If you'd like more hands-on practice, you can also try the practice in the PyLearn app. Keep going!

## Production checklist
- [x] Approved Kendrick / ElevenLabs v3 voice setup confirmed by the user; use the existing configuration without substitution.
- [x] Use the approved Kendrick voice with ElevenLabs v3, as confirmed by the user.
- [ ] Verify code and expected outputs in Python.
- [ ] Keep output synchronized with narration.
- [ ] Do not reveal the required app exercise solution.
- [x] End by telling the learner to complete the exercise to unlock the next lesson; app practice is optional.
