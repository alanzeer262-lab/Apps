# PyLearn Guided Practice — Modules Practice

**Voice lock:** Use the approved Kendrick voice with ElevenLabs v3; do not substitute another voice.
**Canonical source:** Pylearn-build260/content/python-foundations/modules/03-modules-organization.md, branch ccr-c7f6fdd7-xpzi3g.
**Purpose:** Separate practice companion using fresh examples. Never reveal the required app exercise solution.

## Scene 1 — Give the function one job

**Narration:** A function that reads a file and calculates an average in one block has two responsibilities. Imagine separating file loading from average calculation.

**Code**

    def average_values(values):
        if not values:
            return 0.0
        return sum(values) / len(values)

    print(average_values([4, 8, 12]))

**Expected output**

    8.0

This calculation can be tested without reading a file. That clear boundary makes the code easier to maintain.

## Scene 2 — Reuse rather than copy

**Narration:** When a function lives in a module, another file can import it rather than copying its implementation. Keep the interface small and predictable.

**Code**

    values = [5, 10]
    result = sum(values) / len(values)
    print(result)

**Expected output**

    7.5

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
