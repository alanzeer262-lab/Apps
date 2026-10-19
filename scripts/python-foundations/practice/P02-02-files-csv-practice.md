# PyLearn Guided Practice — 02 — Files and CSV Records

**Voice lock — mandatory:** Use the user-approved Kendrick voice with ElevenLabs v3; do not substitute another voice.
**Canonical source:** Pylearn-build260/content/python-foundations/modules/02-files-csv.md, branch ccr-c7f6fdd7-xpzi3g.
**Target runtime:** Approximately 3–5 minutes.
**Purpose:** Separate guided-practice companion with fresh examples. Never reveal the required app exercise solution.

## Scene 1 — Data that survives the program

**Visual:** Use a fresh example and the same uncluttered code-first visual style as the lesson.

**Narration:**

Until now, many examples have kept data inside the code. A file lets a program read information saved outside the program. CSV stands for comma-separated values. Think of it as a simple table stored as text.

**Code**
    
    name,topic,score
        Ada,Python,88
        Lin,Python,72

**Expected output**
    
This CSV has a header row and two records. The header names each column, and each following line contains one learner's values.

**Narration:**

Predict the result before running the example. Compare the output with your prediction and explain the result in your own words. If it differs, inspect the input and change one thing at a time.

## Scene 2 — Read rows with the standard library

**Visual:** Use a fresh example and the same uncluttered code-first visual style as the lesson.

**Narration:**

Python includes a csv module. DictReader uses the header names as keys, so each row behaves like a dictionary. The with statement ensures the file is closed when the block finishes.

**Code**
    
    import csv
    
        with open("learners.csv", newline="") as file:
            reader = csv.DictReader(file)
            records = list(reader)
    
        print(records[0]["name"])
        print(records[0]["score"])

**Expected output**
    
    Ada
        88

**Narration:**

Predict the result before running the example. Compare the output with your prediction and explain the result in your own words. If it differs, inspect the input and change one thing at a time.

## Scene 3 — Convert carefully

**Visual:** Use a fresh example and the same uncluttered code-first visual style as the lesson.

**Narration:**

A normal row can be converted to an integer, but real files can contain blanks or unexpected text. A robust program decides how to handle conversion failures instead of assuming every value is valid.

**Code**
    
    raw_score = "88"
        score = int(raw_score)
        print(score + 2)
        print(type(score))

**Expected output**
    
    90
        <class 'int'>

**Narration:**

Predict the result before running the example. Compare the output with your prediction and explain the result in your own words. If it differs, inspect the input and change one thing at a time.

## Scene 4 — Write a report

**Visual:** Use a fresh example and the same uncluttered code-first visual style as the lesson.

**Narration:**

Reading data is only half the story. Python can also write a result to a file. Opening a file with write mode creates it or replaces its previous contents, so use that mode intentionally.

**Code**
    
    with open("report.txt", "w") as file:
            file.write("Average score: 80.0\n")
    
        print("Report saved")

**Expected output**
    
    Report saved

**Narration:**

Predict the result before running the example. Compare the output with your prediction and explain the result in your own words. If it differs, inspect the input and change one thing at a time.

## Close — Complete the exercise

**Visual:** End card: “Your turn: Complete the exercise”. Do not show or describe unfinished PyLearn app screens.

**Narration:**

Good work. Now complete the exercise to unlock the next lesson. Use the habits from this practice: test small cases, check your assumptions, and make one change at a time. If you'd like extra hands-on practice, you can also try it in the PyLearn app.

## Production checklist

- [ ] Use the approved Kendrick voice with ElevenLabs v3.
- [ ] Verify all example code and outputs in Python.
- [ ] Keep the example distinct from the required app exercise.
- [ ] Do not reveal the exercise solution or hidden tests.
- [ ] Keep code and output synchronized with narration.
- [ ] End by directing the learner to complete the exercise.
