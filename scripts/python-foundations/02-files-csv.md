# PyLearn Video — 02 — Files and CSV Records

**Voice lock — mandatory:** Use the user-approved Kendrick voice with ElevenLabs v3. Do not substitute another voice or preset.
**Canonical source:** Pylearn-build260/content/python-foundations/modules/02-files-csv.md, branch ccr-c7f6fdd7-xpzi3g.
**Use:** Full teaching video, not a short outline. Narrate only spoken text; keep scene headings, code labels, and visual directions out of text-to-speech. Do not show the app's required exercise solution.

**Track 2 visual identity:** Keep the same teacher and pacing. Use a refined data-workbench look: charcoal canvas, subtle grid, teal field labels, and warm amber for a selected row. Visualize a CSV as a sheet of records that flows into structured rows; highlight headers, one row, and the file boundary. Use a file-to-record transformation and row highlighting instead of another generic input/output box.

## Scene 1 — Data that survives the program

**Visual:** Show `learners.csv` as a real sheet of text. Highlight the header row first, then trace Ada and Lin into the table. Ask the learner to identify the three fields before moving to the reader code in the next scene.

**Narration:**

Until now, many examples have kept data inside the code. A file lets a program read information saved outside the program. CSV stands for comma-separated values. Think of it as a simple table stored as text.

**Input file — `learners.csv`**
```csv
name,topic,score
Ada,Python,88
Lin,Python,72
```

**Visual result**
A header row and two data records. The header names each column; each following line contains one learner’s values. This is the source file for Scene 2.

**Narration:**

Pause and identify the header fields and the values in each row before loading the file.

## Scene 2 — Read rows with the standard library

**Visual:** Reveal the code gradually. Ask for a prediction before running it. Show the output only after the run.

**Narration:**

Python includes a csv module. DictReader uses the header names as keys, so each row behaves like a dictionary. The with statement ensures the file is closed when the block finishes.

**Code**
```python
import csv

with open("learners.csv", newline="") as file:
    reader = csv.DictReader(file)
    records = list(reader)

print(records[0]["name"])
print(records[0]["score"])
```

**Expected output**
```text
Ada
88
```

**Narration:**

There is an important detail: values read from CSV arrive as text. The score looks like a number, but the reader gives us the string 88. Convert it deliberately before doing arithmetic.

## Scene 3 — Convert carefully

**Visual:** Reveal the code gradually. Ask for a prediction before running it. Show the output only after the run.

**Narration:**

A normal row can be converted to an integer, but real files can contain blanks or unexpected text. A robust program decides how to handle conversion failures instead of assuming every value is valid.

**Code**
```python
raw_score = "88"
score = int(raw_score)
print(score + 2)
print(type(score))
```

**Expected output**
```text
90
<class 'int'>
```

**Narration:**

This example uses a clean value. Later, the pipeline will separate loading from validation so invalid rows can be handled deliberately.

## Scene 4 — Write a report

**Visual:** Reveal the code gradually. Ask for a prediction before running it. Show the output only after the run.

**Narration:**

Reading data is only half the story. Python can also write a result to a file. Opening a file with write mode creates it or replaces its previous contents, so use that mode intentionally.

**Code**
```python
with open("report.txt", "w") as file:
    file.write("Average score: 80.0\n")

print("Report saved")
```

**Expected output**
```text
Report saved
```

**File written — `report.txt`**
```text
Average score: 80.0
```

**Narration:**

The message confirms the program reached the end. The report itself is stored in the file. In the full toolkit, raw rows, cleaned records, and report writing will remain separate steps.

## Your turn — predict, run, explain

**Visual:** Keep the editor uncluttered. Show a fresh, related prompt without using the app's required exercise code.

**Narration:**

Pause the video and try a small variation of the example. Predict the output before you run it. Then run the code, compare the result with your prediction, and explain why it happened. If the result surprises you, inspect the values and change one thing at a time.

This is extra guided practice, not the required PyLearn exercise solution.

## Recap

**Narration:**

Today, you learned the core idea behind CSV files. Keep the stages clear, test your assumptions, and make the program's behavior visible. In the next lesson, we'll build on this skill.

## Final call to action — watch the practice video

**Visual:** Neutral end card reading “Next: Practice Video”. Do not show unfinished app screens or invent navigation.

**Narration:**

Great work! You've finished Files and CSV Records. Next, watch the practice video. I recommend watching it because we'll use a fresh example to reinforce the skill from this lesson.

After the practice video, complete the exercise to unlock the next lesson. If you'd like extra hands-on practice, you can also try it in the PyLearn app.

**Visual:** Hold the end card long enough to read.

## Production checklist

- [ ] Use the approved Kendrick voice with ElevenLabs v3.
- [ ] Verify every example and expected output in Python before rendering.
- [ ] Reveal code before running it; reveal output only after the run.
- [ ] Keep narration separate from production directions.
- [ ] Do not show the required app exercise solution or hidden tests.
- [ ] Watch the complete rendered video at normal speed before approval.


**Visual transition rule for this lesson:** Show the exact `learners.csv` file before the loader runs. Trace header names into dictionary keys and the first row into `records[0]`; show that the score is text before converting it in Scene 3. In Scene 4, show the write operation creating `report.txt`, then show the actual file contents separately from the console message. Never present a file's contents as console output.
