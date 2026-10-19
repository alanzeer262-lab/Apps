# PyLearn Video — Build: Run the Pipeline

**Track 2 visual identity:** Keep the same teacher and pacing. Use an animated pipeline map with three connected stations—Load, Validate, Summarize—and show each station passing a small record bundle to the next. When introducing report requirements, use a checklist panel and report wireframe rather than a stack of input/output boxes. Highlight the active stage on the persistent toolkit rail.

**Voice lock:** Use the user-approved Kendrick voice with ElevenLabs v3. Do not substitute another voice.
**Canonical source:** Pylearn-build260/content/python-foundations/modules/10-build-pipeline.md, branch ccr-c7f6fdd7-xpzi3g.
**Production rule:** Narrate only spoken text. Do not show the required app exercise solution or invent app screens.

## Scene 1 — Start with real input

**Visual:** Show this exact CSV text in a small file panel. Highlight the header, then each row as it enters the pipeline. Keep the invalid text value “oops” visible; do not hide or recolor it as valid.

**Narration:**

Let's connect the stages using a small example that we can run from beginning to end. This is a teaching example, not the required PyLearn exercise solution. We have three records: Ada has eighty-eight, Lin has seventy-two, and Mo has a score written as the word oops.

```csv
name,score
Ada,88
Lin,72
Mo,oops
```

The loader reads all three rows. Validation converts numeric scores and keeps the invalid record separate. The summary calculates only from the valid records.

## Scene 2 — Run one public function

**Visual:** Show the code in readable sections: load, validate, summarize, then run. As each function is highlighted, animate the data moving to the next stage. Keep the code and sample input visible together before running.

**Code**

```python
import csv
import io

def load(text):
    return list(csv.DictReader(io.StringIO(text)))

def validate(rows):
    valid, rejected = [], []
    for row in rows:
        try:
            score = int(row["score"].strip())
        except ValueError:
            rejected.append(row["name"])
            continue
        if 0 <= score <= 100:
            valid.append({"name": row["name"].strip(), "score": score})
        else:
            rejected.append(row["name"])
    return valid, rejected

def summarize(rows):
    if not rows:
        return {"count": 0, "average": None, "top": None}
    scores = [row["score"] for row in rows]
    top = max(rows, key=lambda row: row["score"])
    return {"count": len(rows), "average": sum(scores) / len(scores), "top": top["name"]}

def run(text):
    rows = load(text)
    valid, rejected = validate(rows)
    return {"rows_read": len(rows), "valid_rows": len(valid), "invalid_rows": len(rejected), **summarize(valid)}

raw_text = "name,score\nAda,88\nLin,72\nMo,oops\n"
report = run(raw_text)
print(report)
```

**Expected output — captured from the code above**

```text
{'rows_read': 3, 'valid_rows': 2, 'invalid_rows': 1, 'count': 2, 'average': 80.0, 'top': 'Ada'}
```

**Narration:**

The `run` function connects the stages. It does not hard-code the report. It passes the input through loading, validation, and summarizing, then combines the measured counts with the calculated summary.

## Scene 3 — Trace the result back to the input

**Visual:** Build the report dashboard only from the output above:
- Rows read: **3**
- Valid rows: **2**
- Invalid rows: **1**
- Average of valid scores: **80.0**
- Top performer: **Ada**

Animate Ada's eighty-eight and Lin's seventy-two into the average calculation: eighty-eight plus seventy-two equals one hundred sixty; divided by two equals eighty. Route Mo's “oops” to the rejected lane and show that it does not affect the average. Label this as the result of the small demonstration dataset, not the final capstone report.

**Narration:**

Every number here has a traceable source. Three rows entered the loader. Two scores passed validation. One row was rejected because its score was not numeric. The average is eighty, calculated from eighty-eight and seventy-two, and Ada is the top performer in this example.

The larger capstone uses more fields and additional cleaning decisions, so its report must be generated from the actual capstone data and the rules you implement. Never copy these demonstration numbers into that report.

## Recap and handoff

You've connected the loading, validation, and summary stages into one pipeline concept. Next, watch the practice video, then complete the exercise to unlock the next lesson. Extra practice in the PyLearn app is optional.

## Final production checklist

- [ ] Verify each code sample and stated output in Python.
- [ ] Reveal code before running it and output only after the run.
- [ ] Keep narration separate from visual directions.
- [ ] Watch the complete rendered video at normal speed before approval.


## Production-critical rule — traceable transformation and truthful results
- Show the sequence explicitly: **source/input → each meaningful transformation → final output**. Use the actual data and code from this script; keep transitions readable and in causal order. Do not jump-cut from input to a result without showing or explaining the operation that produced it.
- Whenever a result is shown, it must be the exact output produced by running the displayed code against the displayed sample data. Verify it in Python before rendering. If it has not been run and verified, do not present it as a real result; mark it as a schematic illustration or omit the value.
- For the toolkit-build and capstone scenes, show the real end-to-end result learners can reproduce by building the tool themselves. No fabricated dashboard metrics, invented report rows, decorative “success” values, or output inconsistent with the code/data. Keep the sample dataset, code, and displayed result synchronized.
- For practice videos, use the script's own independent example and verify that example. Do not reveal the required PyLearn exercise solution.


**Visual transition rule for this lesson:** Never jump from the raw CSV directly to dashboard numbers. Show the exact row movement through load, validate, and summarize; preserve the rejected record in a separate lane; then reveal each report field only after the corresponding calculation. The displayed output above was checked against the shown code and input.
