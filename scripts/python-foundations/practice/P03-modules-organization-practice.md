# PyLearn Guided Practice — Modules Practice

**Voice lock:** Use the approved Kendrick voice with ElevenLabs v3; do not substitute another voice.
**Canonical source:** Pylearn-build260/content/python-foundations/modules/03-modules-organization.md, branch ccr-c7f6fdd7-xpzi3g.
**Purpose:** Separate practice companion using fresh examples. Never reveal the required app exercise solution.
**Track 2 practice visuals:** Use draggable-looking file cards and a simple module connection map. During each pause, highlight the responsibility the learner should assign to a function or module. Reveal import connections one at a time. Preserve the teacher and voice; the visual language alone signals the new level.

## Scene 1 — Give the function one job

**Narration:** A function that reads a file and calculates an average in one block has two responsibilities. Imagine separating file loading from average calculation.

**Module file — `calculations.py`**

```python
def average_values(values):
    if not values:
        return 0.0
    return sum(values) / len(values)
```

**Visual result:** The module defines a reusable calculation and prints nothing by itself. Show the function staying inside its own file tab.

This calculation can be tested without reading a file. That clear boundary makes the code easier to maintain.

## Scene 2 — Reuse rather than copy

**Narration:** When a function lives in a module, another file can import it rather than copying its implementation. Keep the interface small and predictable.

**Runner file — `main.py`**

```python
from calculations import average_values

values = [5, 10]
print(average_values(values))
```

**Expected output**

```text
7.5
```

Use this example to decide which code belongs in a reusable calculation module and which belongs in the report layer.

## Close — Complete the exercise

**Visual:** End card: “Your turn: Complete the exercise”. Do not show unfinished PyLearn app screens.

**Narration:** Good work. Now complete the exercise to unlock the next lesson. Use the habits from this practice: test small cases, check assumptions, and change one thing at a time. If you'd like extra hands-on practice, you can also try it in the PyLearn app.

## Production checklist
- [ ] Use approved Kendrick / ElevenLabs v3 voice.
- [ ] Verify all code and outputs in Python.
- [ ] Keep examples distinct from the required app exercise.
- [ ] Keep code and output synchronized with narration.
- [ ] Watch the full render before approval.


**Visual transition rule for this practice:** Show the function being defined in `calculations.py`, then draw the import connection to `main.py`, then show the call with `[5, 10]` and reveal `7.5` only after execution. Keep module contents separate from console output.
