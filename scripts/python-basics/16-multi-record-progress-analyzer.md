# PyLearn Video 16 — Project 5: Multi-Record Progress Analyzer

> **MANDATORY VOICE SETTINGS — DO NOT CHANGE**
> - Voice: Kendrick
> - Model: ElevenLabs v3
> - Voice ID: exact approved Kendrick voice ID is not recorded in the reviewed repository files; insert the verified ID from the original Runway setup before generating audio.
> - No guessed ID, voice substitution, or preset. Use the same approved voice throughout.
> - Speak narration only; do not read headings or bracketed directions aloud.

**Canonical source:** `Pylearn-build260/content/python-basics/modules/16-build-progress-analyzer.md`, branch `ccr-c7f6fdd7-xpzi3g`.  
**Target runtime:** Approximately 5–7 minutes. Do not reveal the complete required function or solution.

## Scene 1 — Process several records

**Visual:** Show a short list of fictional learner records as name-score pairs. Highlight one record at a time.

**Narration:**

Welcome back. In the last project, we summarized one list of scores. Now we're going to think about several learner records.

Each record contains a name and a score. We want the program to process all the records and return a summary: the number of records, average score, top scorer, learners who passed, and learners who need support.

The key idea is to process the records consistently, one at a time, and apply clear rules.

## Scene 2 — Understand the record structure

**Visual:** Reveal an independent, small list of records. Unpack the fields in a for loop.

**Code**
```python
records = [
    ("Mia", 81),
    ("Noah", 67),
    ("Iris", 93)
]

for name, score in records:
    print(f"{name}: {score}")
```

**Expected output**
```text
Mia: 81
Noah: 67
Iris: 93
```

**Narration:**

The outer list keeps the records in order. Each tuple groups a name with a score. The loop unpacks each tuple into name and score, so we can work with meaningful variable names.

This is easier to read than maintaining separate lists of names and scores and hoping the positions continue to match.

## Scene 3 — Apply a rule to each record

**Visual:** Demonstrate a simple passing rule using the independent example. Do not build the complete required analyzer.

**Code**
```python
threshold = 70

for name, score in records:
    if score >= threshold:
        print(f"{name} passed")
```

**Expected output**
```text
Mia passed
Iris passed
```

**Narration:**

Here, we visit every record and compare its score with the threshold. If the score is at least seventy, we display a message for that learner.

The loop handles each record in the same way. The condition decides which records meet the rule.

In the project, you'll use this kind of reasoning to separate learners who passed from those who need support. Make the rule clear before writing the code, and check the boundary value.

## Scene 4 — Build a summary from the records

**Visual:** Show a checklist of required summary fields: count, average, top scorer, passed, needs support. Avoid showing a complete function or a full output.

**Narration:**

The project asks you to return several pieces of information.

Count tells you how many records were provided. Average summarizes the scores. Top scorer identifies the learner associated with the highest score. Passed and needs support are lists of learners separated by the threshold rule.

Plan each field separately. Ask what information it needs, how you can calculate it, and what structure will make the result useful.

For example, a loop can update a running total. A condition can decide which list receives a learner. Comparing scores can help identify the top scorer.

The full analyzer is your work to build in PyLearn. This video demonstrates the building blocks, not the finished solution.

## Scene 5 — Preserve input order and handle empty records

**Visual:** Show a list order marker and an empty-list symbol. Do not fill in the complete required output.

**Narration:**

The project also asks you to preserve input order in the learner lists. That means you should append learners as you encounter them, rather than sorting the lists unless the requirement asks for sorting.

You also need to handle empty records. If the list is empty, there is no average to calculate and no top scorer to identify. Decide on a deliberate empty result rather than letting the program crash.

Empty input is an edge case, not an excuse to invent a score or a learner.

## Scene 6 — Test your reasoning

**Visual:** Show a test checklist: multiple records, a score at the threshold, an empty record list. Keep output hidden.

**Narration:**

Test your function with several records. Check the count, average, top scorer, and both learner lists.

Then test the threshold boundary. If the rule says seventy or higher passes, exactly seventy should be included in the passing group.

Finally, test an empty list. Your function should return the empty result you planned.

If something is wrong, isolate one part at a time. Check the loop, the comparison, the running total, and the structure of the returned summary.

## Scene 7 — Reflection

**Visual:** Display two structures: a list of paired records and two unrelated lists. Highlight how a tuple keeps each name with its score.

**Narration:**

Before you finish, consider why a record such as a name-score pair is easier to process than unrelated name and score lists.

A paired record keeps related values together. It reduces the risk of matching the wrong score to the wrong learner and makes loop code clearer.

## Project closing — required for in-app and YouTube versions

**Visual:** Show the real PyLearn navigation path to the “Multi-Record Progress Analyzer” task. Do not show the completed `analyze_records` function or its full required output.

**Narration:**

Now open PyLearn and find the Multi-Record Progress Analyzer task.

Build it yourself and run the tests. This video has shown the ideas, not the finished solution. Practice Drills, if shown, are optional; complete and pass the required project exercise to unlock the next lesson.

Pause the video and start building.

## Production and QA checklist

- [ ] Verify the exact approved Kendrick voice ID before generating audio.
- [ ] Use ElevenLabs v3 and the same approved voice throughout.
- [ ] Keep production notes out of spoken narration.
- [ ] Verify all demonstration code and outputs in Python.
- [ ] Do not reveal the complete `analyze_records` function or required project solution.
- [ ] Preserve input-order guidance and empty-input edge case.
- [ ] Preserve the project navigation ending and progression rule.
