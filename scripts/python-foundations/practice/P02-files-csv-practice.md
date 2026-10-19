# PyLearn Guided Practice — Files and CSV Practice

**Voice lock:** Use the approved Kendrick voice with ElevenLabs v3; do not substitute another voice.
**Canonical source:** Pylearn-build260/content/python-foundations/modules/02-files-csv.md, branch ccr-c7f6fdd7-xpzi3g.
**Purpose:** Separate practice companion using fresh examples. Never reveal the required app exercise solution.

## Scene 1 — Inspect a CSV row

**Narration:** Here is a fresh CSV example. Before calculating anything, identify the headers and remember that values are read as text.

**Code**

    import csv
    from io import StringIO
    text = "item,quantity\nPens,12\nBooks,4\n"
    rows = list(csv.DictReader(StringIO(text)))
    print(rows[0])

**Expected output**

    {'item': 'Pens', 'quantity': '12'}

The quantity is text, so convert it before arithmetic.

## Scene 2 — Convert and total

**Code**

    quantities = [int(row["quantity"]) for row in rows]
    print(sum(quantities))

**Expected output**

    16

**Narration:** Now imagine one quantity is blank. Decide how your program should report that invalid value instead of assuming every row is clean.

## Close — Complete the exercise

**Visual:** End card: “Your turn: Complete the exercise”. Do not show unfinished PyLearn app screens.

**Narration:** Good work. Now complete the exercise to unlock the next lesson. Use the habits from this practice: test small cases, check assumptions, and change one thing at a time. If you'd like extra hands-on practice, you can also try it in the PyLearn app.

## Production checklist
- [ ] Use approved Kendrick / ElevenLabs v3 voice.
- [ ] Verify all code and outputs in Python.
- [ ] Keep examples distinct from the required app exercise.
- [ ] Keep code and output synchronized with narration.
- [ ] Watch the full render before approval.
