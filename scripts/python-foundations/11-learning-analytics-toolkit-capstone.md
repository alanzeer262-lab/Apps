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
