# PyLearn Video — 05 — Think in Tables Before pandas

**Voice lock — mandatory:** Use the user-approved Kendrick voice with ElevenLabs v3. Do not substitute another voice or preset.
**Canonical source:** Pylearn-build260/content/python-foundations/modules/05-data-shaped-python.md, branch ccr-c7f6fdd7-xpzi3g.
**Use:** Full teaching video, not a short outline. Narrate only spoken text; keep scene headings, code labels, and visual directions out of text-to-speech. Do not show the app's required exercise solution.

**Track 2 visual identity:** Keep the same teacher and pacing. Use an analyst's data canvas: structured mini-table, field chips, filter lenses, and a compact grouping view. Highlight selected columns and filtered rows directly in the table; transition from records to a grouped summary. This should feel like inspecting real data, not another sequence of input/output boxes.

## Scene 1 — A table made from dictionaries

**Visual:** Reveal the code gradually. Ask for a prediction before running it. Show the output only after the run.

**Narration:**

Before using a data-analysis library, we can practice the underlying ideas with plain Python. A list can hold one dictionary per row, and each dictionary can use named fields.

**Code**
```python
records = [
    {"name": "Ada", "score": 88, "topic": "Python"},
    {"name": "Lin", "score": 72, "topic": "Python"},
    {"name": "Sam", "score": 95, "topic": "Pandas"},
]
print(records[0]["name"])
print(records[0]["score"])
```

**Expected output**
```text
Ada
88
```

**Narration:**

Named fields make the data easier to understand than relying on positions like record zero or record one.

## Scene 2 — Select and filter

**Visual:** Reveal the code gradually. Ask for a prediction before running it. Show the output only after the run.

**Narration:**

Selection asks for a field. Filtering keeps only rows that meet a condition. These are two common operations in data analysis.

**Code**
```python
scores = [row["score"] for row in records]
strong = [row for row in records if row["score"] >= 80]
print(scores)
print(len(strong))
```

**Expected output**
```text
[88, 72, 95]
2
```

**Narration:**

The first operation extracts every score. The second keeps records with scores of at least eighty. Notice that the filter keeps whole rows, not just their scores.

## Scene 3 — Create a derived field

**Visual:** Reveal the code gradually. Ask for a prediction before running it. Show the output only after the run.

**Narration:**

A derived field is calculated from existing data. We can add a pass flag to each record using a consistent threshold.

**Code**
```python
for row in records:
    row["passed"] = row["score"] >= 70
print(records[1]["passed"])
```

**Expected output**
```text
True
```

**Narration:**

The new field records a decision based on the score. In real analysis, we should document the threshold so people know what passed means.

## Scene 4 — Count categories

**Visual:** Reveal the code gradually. Ask for a prediction before running it. Show the output only after the run.

**Narration:**

Grouping means collecting rows by a shared category. A dictionary can count how often each topic appears.

**Code**
```python
counts = {}
for row in records:
    topic = row["topic"]
    counts[topic] = counts.get(topic, 0) + 1
print(counts)
```

**Expected output**
```text
{'Python': 2, 'Pandas': 1}
```

**Narration:**

We now have the core ideas behind later DataFrame work: select fields, filter rows, create derived values, and group records.

## Your turn — predict, run, explain

**Visual:** Keep the editor uncluttered. Show a fresh, related prompt without using the app's required exercise code.

**Narration:**

Pause the video and try a small variation of the example. Predict the output before you run it. Then run the code, compare the result with your prediction, and explain why it happened. If the result surprises you, inspect the values and change one thing at a time.

This is extra guided practice, not the required PyLearn exercise solution.

## Recap

**Narration:**

Today, you learned the core idea behind records, selection, filtering, derived fields, grouping. Keep the stages clear, test your assumptions, and make the program's behavior visible. In the next lesson, we'll build on this skill.

## Final call to action — watch the practice video

**Visual:** Neutral end card reading “Next: Practice Video”. Do not show unfinished app screens or invent navigation.

**Narration:**

Great work! You've finished Think in Tables Before pandas. Next, watch the practice video. I recommend watching it because we'll use a fresh example to reinforce the skill from this lesson.

After the practice video, complete the exercise to unlock the next lesson. If you'd like extra hands-on practice, you can also try it in the PyLearn app.

**Visual:** Hold the end card long enough to read.

## Production checklist

- [ ] Use the approved Kendrick voice with ElevenLabs v3.
- [ ] Verify every example and expected output in Python before rendering.
- [ ] Reveal code before running it; reveal output only after the run.
- [ ] Keep narration separate from production directions.
- [ ] Do not show the required app exercise solution or hidden tests.
- [ ] Watch the complete rendered video at normal speed before approval.


**Visual transition rule for this lesson:** Keep the same three-row table on screen. Show the exact operation on the relevant column or rows, then reveal the derived list/count only after the operation runs. When adding `passed`, update the visible row fields; when grouping, move each row into its topic group and derive the counts from the records. Do not show a chart or count that isn't computed from this table.
