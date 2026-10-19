# PyLearn Video — Learning Analytics Toolkit — Final Build

**Track 2 visual identity:** Keep the same teacher and pacing, but make the capstone feel like a final project workspace. Use a wide canvas with the six-stage pipeline, a milestone board, a data-quality lane, and a blank report wireframe. Reveal milestones one at a time and use progress markers to signal the learner is assembling a complete tool. Do not show a finished solution, finished report values, or unfinished app UI. End with a distinctive “Final Capstone Practice” card, not a next-lesson unlock prompt.

**Voice lock:** Use the approved Kendrick voice with ElevenLabs v3.
**Canonical source:** Pylearn-build260/content/python-foundations/projects/final-toolkit.md, branch ccr-c7f6fdd7-xpzi3g.

## Scene 1 — Bring the toolkit together

**Visual:** Show raw CSV → load → inspect → validate → clean → analyze → report. Do not show a completed solution.

**Narration:**

Welcome to the final build of Python Foundations. You've practised debugging, reading CSV records, organizing code into modules, validating input, testing behavior, and summarizing table-shaped data. Now you'll bring those skills together in one Learning Analytics Toolkit.

The input is a CSV containing learner name, topic, score, attempt count, and completion status. Realistic data is rarely perfect, so the dataset includes a blank score, a score stored as text, a duplicate row, inconsistent topic capitalization, and an out-of-range score.

Your goal is not to pretend the data is clean. Your goal is to build a pipeline that handles it deliberately and explains what happened.

## Scene 2 — Five milestones

**Visual:** Reveal each milestone card separately, with no implementation code.

**Narration:**

Work through five milestones. First, load the CSV and inspect what arrived. Keep the original row count. Second, validate records and track invalid rows and rejection reasons. Third, clean and transform the data using documented decisions. Fourth, analyze valid records: calculate the average, identify the top performer, and produce a grade distribution. Fifth, create the final report.

Your report must include rows read, valid rows, invalid rows, cleaning decisions, average score, top performer, grade distribution, and one warning or limitation.

## Scene 3 — Build for trust

**Narration:**

A report can look polished and still be wrong. Test normal records, empty data, invalid scores, and boundary values. Keep loading separate from validation and validation separate from aggregation, so you can find problems without guessing.

When the report works, make one deliberate modification: add a count by topic, change the pass threshold and update the report, or add a grade category. Rerun your tests. The goal is to prove you can change a working program without breaking its core behavior.

## Scene 4 — See a real reference run

**Reference source for production QA:** `scripts/python-foundations/reference_runs/capstone_reference_demo.py`. The output below comes from running that Python file against the exact demonstration CSV shown here. This is a separate teaching dataset, not the required PyLearn exercise data or its hidden solution.

**Visual — input first:** Show the seven CSV records with the fields `name, topic, score, attempt_count, completion_status`. Highlight the imperfect rows as they enter validation:
- Sam: blank score
- Lin: exact duplicate row
- Noor: score 150, outside the 0–100 rule
- Ivy: score text “oops”, not numeric

**Visual — transformation:** Keep accepted and rejected records in separate lanes. The three accepted scores are Ada 88, Lin 72, and Mira 95. Show topic capitalization being normalized; show the rejected rows and their reasons. Do not skip straight from the CSV to the dashboard.

**Visual — actual report produced by the reference run:**

```text
Rows read: 7
Valid rows: 3
Invalid rows: 4
Cleaning decisions:
- Removed exact duplicate rows
- Rejected blank and non-numeric scores
- Rejected scores outside 0-100
- Normalized topic capitalization
Average score: 85.0
Top performer: Mira
Grade distribution:
A (90-100): 1
B (80-89): 1
C (70-79): 1
D (60-69): 0
F (below 60): 0
Warning: Average and grade distribution use only valid, deduplicated rows.
```

**Narration:**

This is a real reference run, not a decorative mock-up. Seven rows entered the pipeline. Three remained valid after the documented rules, and four were excluded: one blank score, one duplicate, one out-of-range score, and one non-numeric score. The average is eighty-five, calculated from eighty-eight, seventy-two, and ninety-five. Mira is the top performer with ninety-five. The grade distribution also comes from those same three scores.

Your own result will depend on your input data and the cleaning rules you choose. If you use this exact demonstration CSV and these same rules, your report should match these values. If your result differs, investigate it rather than changing the displayed numbers to make them match.

## Final call to action — watch capstone practice

**Visual:** End card: “Next: Capstone Practice Video”. Do not show a completed report or unfinished app screens.

**Narration:**

You've reached the final lesson of Python Foundations. Next, watch the capstone practice video. I recommend watching it to help you plan the milestones and check your approach.

After the practice video, complete the final capstone exercise. Take it one stage at a time, test your work, and be ready to explain one cleaning decision. You can also try your code in the PyLearn app for extra hands-on practice.

## Production checklist

- [ ] Use the approved Kendrick voice with ElevenLabs v3.
- [ ] Keep the five milestones distinct.
- [ ] Do not reveal completed implementation, final answers, or evaluation answers.
- [ ] Check code and outputs before rendering.
- [ ] Use the capstone practice handoff, not a claim that another lesson unlocks.

## Production checklist
- [ ] Verify all code and outputs in Python.
- [ ] Keep narration separate from visual directions.
- [ ] Do not reveal the required app exercise solution.
- [ ] Watch the full render before approval.


## Production-critical rule — traceable transformation and truthful results
- Show the sequence explicitly: **source/input → each meaningful transformation → final output**. Use the actual data and code from this script; keep transitions readable and in causal order. Do not jump-cut from input to a result without showing or explaining the operation that produced it.
- Whenever a result is shown, it must be the exact output produced by running the displayed code against the displayed sample data. Verify it in Python before rendering. If it has not been run and verified, do not present it as a real result; mark it as a schematic illustration or omit the value.
- For the toolkit-build and capstone scenes, show the real end-to-end result learners can reproduce by building the tool themselves. No fabricated dashboard metrics, invented report rows, decorative “success” values, or output inconsistent with the code/data. Keep the sample dataset, code, and displayed result synchronized.
- For practice videos, use the script's own independent example and verify that example. Do not reveal the required PyLearn exercise solution.


**Visual transition rule for this lesson:** The capstone must show the complete causal path: the exact raw rows → each cleaning/validation decision → the accepted records → calculations → report. Reveal the report only after the pipeline completes. Use the output from the committed reference Python file, and rerun it if the sample data or cleaning policy changes. Never fabricate or manually tune report values.
