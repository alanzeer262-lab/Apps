# PyLearn Video 19 — Project 8: Handle Imperfect Scores

> **MANDATORY VOICE SETTINGS — DO NOT CHANGE**
> - Voice: Kendrick
> - Model: ElevenLabs v3
> - Voice ID: exact approved Kendrick voice ID is not recorded in the reviewed repository files; insert the verified ID from the original Runway setup before generating audio.
> - No guessed ID, substitution, or preset. Use the same approved voice throughout.
> - Speak narration only; do not read headings or bracketed directions aloud.

**Canonical source:** `Pylearn-build260/content/python-basics/modules/19-build-messy-input.md`, branch `ccr-c7f6fdd7-xpzi3g`.  
**Target runtime:** Approximately 5–7 minutes. Do not show the complete required function or solution.

## Scene 1 — Real input is not always clean

**Visual:** Show a few fictional name-score pairs with numeric text, valid numbers, invalid text, and an empty string. Do not show the complete required dataset as a solved example.

**Narration:**

Welcome back. This project focuses on data quality.

Real data can contain scores as text, invalid words, or empty values. If we try to convert every value without checking, one bad value can stop the program.

Our goal is to separate valid records from invalid records. The invalid records should keep the learner's name and a reason, so we can inspect the problem instead of silently losing information.

## Scene 2 — Convert numeric text

**Visual:** Demonstrate a valid string conversion separately.

**Code**
```python
raw_score = "88"
score = int(raw_score)
print(score)
print(type(score))
```

**Expected output**
```text
88
<class 'int'>
```

**Narration:**

The text eighty-eight can be converted to an integer because its contents form a valid whole number. After conversion, the value has type int.

But not every string contains a valid number. We need to handle those cases deliberately.

## Scene 3 — Detect invalid input

**Visual:** Run an invalid conversion in a separate example. Show the ValueError, then transition to a try/except example.

**Code**
```python
raw_score = "oops"
score = int(raw_score)
```

**Narration:**

This conversion raises ValueError. Python cannot turn the word oops into an integer, and it doesn't guess what number we intended.

If invalid input is expected, use try and except to handle the conversion error.

**Code**
```python
raw_score = "oops"

try:
    score = int(raw_score)
except ValueError:
    score = None

print(score is None)
```

**Expected output**
```text
True
```

**Narration:**

Python tries the conversion inside the try block. If a ValueError occurs, the except block runs. In this demonstration, it assigns None to represent the missing numeric result.

The project needs more than a conversion. It needs to keep track of which records are valid and which records need attention.

## Scene 4 — Empty text is a different problem

**Visual:** Show an empty string as two adjacent quotation marks. Distinguish “empty score” from “invalid score” in a two-row table.

**Narration:**

An empty string is not the same as a word such as oops, even though both fail integer conversion.

The project asks you to keep a reason for each invalid record. A blank value can be labeled empty score. Text that cannot be converted can be labeled invalid score.

Those reasons help someone understand what went wrong and what should happen next.

## Scene 5 — Separate valid and invalid records

**Visual:** Show a pipeline with raw records entering and two output groups: valid records and invalid records. Do not display the full completed output for the required dataset.

**Narration:**

Your function clean_score_records receives the raw records. For each record, it should inspect the score, attempt conversion safely, and decide where the record belongs.

Valid records should contain numeric scores. Invalid records should keep the learner's name and a reason, such as invalid score or empty score.

Do not replace invalid scores with zero. That would change the meaning of the data and could make the analysis misleading. An invalid score is not the same as a score of zero.

## Scene 6 — Analyze only valid values

**Visual:** Show a valid-record group flowing into a summary calculation, while invalid records flow into a separate report. Avoid giving a complete code solution.

**Narration:**

After cleaning, analysis should use the valid records. Invalid scores should be excluded from the average, while the invalid-record list remains available for review.

This is a data-quality decision, not a Python rule. We choose to keep valid and invalid records separate because it preserves information about what was accepted and what needs attention.

The full pipeline is raw records, validation, valid and invalid groups, then analysis. Build each stage and test it separately.

## Scene 7 — Test the pipeline

**Visual:** Show a checklist: valid numeric score, invalid text, empty score, mixed records. Do not show completed required outputs.

**Narration:**

Test a record with a valid numeric string. Test a record with text that cannot be converted. Test a record with an empty score. Then test a collection that mixes all these cases.

Check that valid records have numeric scores, invalid records preserve their names and reasons, and the program continues instead of crashing.

If a test fails, inspect the validation step before changing the analysis. Keeping the stages separate makes debugging easier.

## Scene 8 — Reflection

**Visual:** Show “invalid score is not zero” as a concise reminder.

**Narration:**

Before you finish, ask why replacing an invalid score with zero could create a misleading analysis.

Zero is a real numeric value. An invalid score means the data could not be interpreted as a valid number. Treating both the same would hide a data-quality problem and lower the average for the wrong reason.

## Project closing — required for in-app and YouTube versions

**Visual:** Show the real PyLearn navigation path to the “Handle Imperfect Scores” task. Do not show the full `clean_score_records` function or the completed required output.

**Narration:**

Now open PyLearn and find the Handle Imperfect Scores task.

Build it yourself and run the tests. This video has shown the ideas, not the finished solution. Practice Drills, if shown, are optional; complete and pass the required project exercise to unlock the next lesson.

Pause the video and start building.

## Production and QA checklist

- [ ] Verify the exact approved Kendrick voice ID before generating audio.
- [ ] Use ElevenLabs v3 and the same approved voice throughout.
- [ ] Keep production notes out of spoken narration.
- [ ] Verify all demonstration code and outputs in Python.
- [ ] Do not reveal the complete `clean_score_records` implementation or full required dataset output.
- [ ] Never imply that invalid scores should silently become zero.
- [ ] Preserve the project navigation ending and progression rule.
