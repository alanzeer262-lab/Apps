# PyLearn Guided Practice 12 — My Learning Report

> **MANDATORY VOICE SETTINGS — DO NOT CHANGE**
> - Voice: Kendrick
> - Model: ElevenLabs v3
> - Voice ID: exact approved Kendrick voice ID is not recorded in the reviewed repository files; insert the verified ID from the original Runway setup before generation.
> - No guessed ID, substitution, or preset; same approved voice throughout.
> - Speak narration only; do not read headings or bracketed production notes aloud.

**Canonical source:** `Pylearn-build260/content/python-basics/modules/12-build-personal-report.md`, branch `ccr-c7f6fdd7-xpzi3g`.
**Target runtime:** Approximately 2–4 minutes.
**Purpose:** Separate guided-practice companion using fresh examples; do not reveal the required app exercise solution.

## Scene 1 — Describe a reading habit

**Visual:** Use a separate example from the required learner-report task.

**Code**
```python
reader = "Mia"
book_goal = "Read more science"
books_this_month = 3
```

**Narration:** These values describe a fictional reading habit. The name and goal are text; the number of books is a measurement.

## Scene 2 — Return a short report

```python
def reading_report(reader, goal, books):
    return f"Reader: {reader}\nGoal: {goal}\nBooks this month: {books}"

report = reading_report("Mia", "Read more science", 3)
print(report)
```

**Expected output**
```text
Reader: Mia
Goal: Read more science
Books this month: 3
```

**Narration:** The function returns a string with multiple lines. Print displays the returned report. Notice that the function returns the report instead of printing inside the function.

## Scene 3 — Change one input

**Narration:** Try changing the number of books and predicting which part of the report changes. Then try a different goal. You should not need to rewrite the function.

## Close

**Narration:** Open PyLearn and find the My Learning Report project task. This companion demonstrates the idea with a different example; it does not solve the project. Pass the required project exercise to unlock the next lesson.

## Production checklist
- [ ] Verify exact approved Kendrick voice ID before generation.
- [ ] Use ElevenLabs v3 with the same approved voice identity.
- [ ] Verify code and outputs in Python.
- [ ] Keep code/output synchronized with narration.
- [ ] Do not reveal required app exercise solutions.
- [ ] End by directing the learner to the required PyLearn task.
