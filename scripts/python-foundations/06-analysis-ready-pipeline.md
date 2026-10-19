# PyLearn Video — 06 — From Raw Records to a Reliable Report

**Voice lock — mandatory:** Use the user-approved Kendrick voice with ElevenLabs v3. Do not substitute another voice or preset.
**Canonical source:** Pylearn-build260/content/python-foundations/modules/06-analysis-ready-pipeline.md, branch ccr-c7f6fdd7-xpzi3g.
**Use:** Full teaching video, not a short outline. Narrate only spoken text; keep scene headings, code labels, and visual directions out of text-to-speech. Do not show the app's required exercise solution.

**Track 2 visual identity:** Keep the same teacher and pacing. Show a living data pipeline across the screen: raw records enter, cleaned records continue, rejected records branch into a review lane, and a report emerges. Use thin connectors, stage labels, and small status indicators in a charcoal-and-teal palette. Make flow and transformation the main visual, not input/output boxes.

## Scene 1 — Follow the pipeline

**Visual:** Reveal the code gradually. Ask for a prediction before running it. Show the output only after the run.

**Narration:**

A reliable data workflow moves through deliberate stages: inspect, validate, clean, transform, summarize, and report. Each stage answers a different question, and the order matters.

**Code**
```python
raw_scores = ["80", "90", "oops", "70"]
print("Rows read:", len(raw_scores))
```

**Expected output**
```text
Rows read: 4
```

**Narration:**

We start by counting what arrived. We should not quietly discard rows before we know what the input contains.

## Scene 2 — Validate before calculating

**Visual:** Reveal the code gradually. Ask for a prediction before running it. Show the output only after the run.

**Narration:**

A score stored as text needs conversion. A word such as oops cannot be converted to an integer. We'll keep valid values separate from invalid values so the report can explain what happened.

**Code**
```python
raw_scores = ["80", "90", "oops", "70"]
valid_scores = []
invalid_values = []
for raw in raw_scores:
    try:
        valid_scores.append(int(raw))
    except ValueError:
        invalid_values.append(raw)
print(valid_scores)
print(invalid_values)
```

**Expected output**
```text
[80, 90, 70]
['oops']
```

**Narration:**

This is one explicit cleaning policy: retain valid numeric scores and record the invalid value. Different datasets may need different rules, but the choice must be clear.

## Scene 3 — Summarize the cleaned data

**Visual:** Reveal the code gradually. Ask for a prediction before running it. Show the output only after the run.

**Narration:**

Only after validation can we calculate the average for the valid scores. The report should state how many rows were read and how many were usable.

**Code**
```python
valid_scores = [80, 90, 70]
average = sum(valid_scores) / len(valid_scores)
print("Valid rows:", len(valid_scores))
print("Average:", average)
```

**Expected output**
```text
Valid rows: 3
Average: 80.0
```

**Narration:**

The average describes the three valid scores, not all four original rows. Reporting the count prevents readers from misunderstanding the number.

## Scene 4 — Decisions belong in the report

**Visual:** Reveal the code gradually. Ask for a prediction before running it. Show the output only after the run.

**Narration:**

Missing values, duplicate records, inconsistent capitalization, and out-of-range scores all require decisions. There is no universal cleaning rule. Choose it, document it, and apply it consistently.

**Code**
```python
raw_scores = ["80", "90", "oops", "70"]
valid_scores = []
invalid_values = []
for raw in raw_scores:
    try:
        valid_scores.append(int(raw))
    except ValueError:
        invalid_values.append(raw)

print("Rows read:", len(raw_scores))
print("Valid rows:", len(valid_scores))
print("Invalid rows:", len(invalid_values))
if invalid_values:
    print("Warning: one or more scores could not be converted")
```

**Expected output**
```text
Rows read: 4
Valid rows: 3
Invalid rows: 1
Warning: one or more scores could not be converted
```

**Narration:**

A trustworthy report shows both the result and its limitations. This pipeline is the bridge from beginner Python to dedicated analysis tools.

## Your turn — predict, run, explain

**Visual:** Keep the editor uncluttered. Show a fresh, related prompt without using the app's required exercise code.

**Narration:**

Pause the video and try a small variation of the example. Predict the output before you run it. Then run the code, compare the result with your prediction, and explain why it happened. If the result surprises you, inspect the values and change one thing at a time.

This is extra guided practice, not the required PyLearn exercise solution.

## Recap

**Narration:**

Today, you learned the core idea behind pipeline and explicit cleaning decisions. Keep the stages clear, test your assumptions, and make the program's behavior visible. In the next lesson, we'll build on this skill.

## Final call to action — watch the practice video

**Visual:** Neutral end card reading “Next: Practice Video”. Do not show unfinished app screens or invent navigation.

**Narration:**

Great work! You've finished From Raw Records to a Reliable Report. Next, watch the practice video. I recommend watching it because we'll use a fresh example to reinforce the skill from this lesson.

After the practice video, complete the exercise to unlock the next lesson. If you'd like extra hands-on practice, you can also try it in the PyLearn app.

**Visual:** Hold the end card long enough to read.

## Production checklist

- [ ] Use the approved Kendrick voice with ElevenLabs v3.
- [ ] Verify every example and expected output in Python before rendering.
- [ ] Reveal code before running it; reveal output only after the run.
- [ ] Keep narration separate from production directions.
- [ ] Do not show the required app exercise solution or hidden tests.
- [ ] Watch the complete rendered video at normal speed before approval.


## Production-critical rule — traceable transformation and truthful results
- Show the sequence explicitly: **source/input → each meaningful transformation → final output**. Use the actual data and code from this script; keep transitions readable and in causal order. Do not jump-cut from input to a result without showing or explaining the operation that produced it.
- Whenever a result is shown, it must be the exact output produced by running the displayed code against the displayed sample data. Verify it in Python before rendering. If it has not been run and verified, do not present it as a real result; mark it as a schematic illustration or omit the value.
- For the toolkit-build and capstone scenes, show the real end-to-end result learners can reproduce by building the tool themselves. No fabricated dashboard metrics, invented report rows, decorative “success” values, or output inconsistent with the code/data. Keep the sample dataset, code, and displayed result synchronized.
- For practice videos, use the script's own independent example and verify that example. Do not reveal the required PyLearn exercise solution.


**Visual transition rule for this lesson:** In every scene, begin with the raw list, highlight the exact operation (count, convert, separate invalid values, calculate), then animate the resulting list or number into the report. Keep the same four input values visible across the sequence so learners can trace each change. The report numbers must be generated from the variables in the displayed code, never typed as decorative values.