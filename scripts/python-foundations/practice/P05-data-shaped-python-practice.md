# PyLearn Guided Practice — Table-Shaped Data Practice

**Voice lock:** Use the approved Kendrick voice with ElevenLabs v3; do not substitute another voice.
**Canonical source:** Pylearn-build260/content/python-foundations/modules/05-data-shaped-python.md, branch ccr-c7f6fdd7-xpzi3g.
**Purpose:** Separate practice companion using fresh examples. Never reveal the required app exercise solution.
**Track 2 practice visuals:** Use an analyst's canvas: mini-table, column highlights, filter chips, and grouped result bars. Let the viewer see rows being selected or filtered directly. Pause before the result to invite a prediction. Keep the same teacher and voice.

## Scene 1 — Select a field

**Narration:** Use fresh records about books. A list of dictionaries lets us use meaningful field names instead of remembering column positions.

**Code**

    books = [
        {"title": "North", "pages": 120, "genre": "Fiction"},
        {"title": "Signals", "pages": 240, "genre": "Science"},
        {"title": "River", "pages": 180, "genre": "Fiction"},
    ]
    print([book["pages"] for book in books])

**Expected output**

    [120, 240, 180]

The list comprehension selects one field from each record.

## Scene 2 — Filter and count

**Code**

    long_books = [book for book in books if book["pages"] >= 180]
    counts = {}
    for book in books:
        counts[book["genre"]] = counts.get(book["genre"], 0) + 1
    print(len(long_books))
    print(counts)

**Expected output**

    2
    {'Fiction': 2, 'Science': 1}

**Narration:** These are the same core operations you'll use later with DataFrames: select, filter, derive, and group.

## Close — Complete the exercise

**Visual:** End card: “Your turn: Complete the exercise”. Do not show unfinished PyLearn app screens.

**Narration:** Good work. Now complete the exercise to unlock the next lesson. Use the habits from this practice: test small cases, check assumptions, and change one thing at a time. If you'd like extra hands-on practice, you can also try it in the PyLearn app.

## Production checklist
- [ ] Use approved Kendrick / ElevenLabs v3 voice.
- [ ] Verify all code and outputs in Python.
- [ ] Keep examples distinct from the required app exercise.
- [ ] Keep code and output synchronized with narration.
- [ ] Watch the full render before approval.


**Visual transition rule for this practice:** Keep the three-book table on screen. Highlight the `pages` column before revealing `[120, 240, 180]`, then highlight the two qualifying rows before revealing count `2`. Derive genre counts from the same rows; do not substitute unrelated chart values.
