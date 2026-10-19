# PyLearn Guided Practice — Learning Analytics Toolkit Capstone

**Voice lock:** Use the approved Kendrick voice with ElevenLabs v3; do not substitute another voice.
**Canonical source:** Pylearn-build260/content/python-foundations/projects/final-toolkit.md, branch ccr-c7f6fdd7-xpzi3g.
**Purpose:** Separate practice companion; do not reveal the required exercise implementation or hidden evaluation answers.
**Track 2 capstone-practice visuals:** Treat this as the final project room, distinct from regular practice videos. Use a milestone board, pipeline canvas, data-quality side lane, and blank report wireframe. Reveal a checklist one item at a time; do not fill in the final report or show the app's required solution. Close on a celebratory “Python Foundations Complete” end card. Do not say another lesson will unlock.

## Scene 1 — Inspect the data first

**Visual:** Show the column names: name, topic, score, attempt_count, completion_status. Then show a checklist of known imperfections without showing a cleaned final table.

**Narration:**

Welcome to the final capstone practice. The goal is to build a reliable pipeline, not just make one calculation work. Start by inspecting the CSV. It contains names, topics, scores, attempt counts, and completion status. The source data includes a blank score, a score stored as text, a duplicate row, inconsistent topic capitalization, and an out-of-range score.

Before cleaning anything, ask what arrived. How many rows are there? Which fields are present? Which values need closer inspection? Keep a record of your observations so the report can explain what changed.

## Scene 2 — Plan the pipeline

**Visual:** Reveal the stages one by one: load, inspect, validate, clean, analyze, report.

**Narration:**

Keep the stages separate. Loading turns the CSV into records. Inspection helps you understand the input. Validation checks the rules. Cleaning applies documented decisions. Analysis calculates the requested summaries. Reporting explains both results and limitations.

## Scene 3 — Check the report requirements

**Visual:** Show a blank checklist, not filled-in results.

**Narration:**

Your report needs eight things: rows read, valid rows, invalid rows, cleaning decisions, average score, top performer, grade distribution, and one warning or limitation. Do not invent a cleaning rule after seeing the result just because it produces a convenient number. Choose a rule, document it, and apply it consistently.

## Scene 4 — Test and modify

**Narration:**

Test normal input, empty input, invalid values, and boundary values. Compare expected and actual results. If something fails, reproduce the smallest case and change one assumption at a time.

After the report works, choose one modification: add a count by topic, change the pass threshold and update the report, or add a grade category. Rerun your tests to make sure the change has not broken existing behavior.

## Close — Finish the final capstone

**Visual:** End card: “Complete the Final Capstone”. Do not show a completed solution or unfinished app UI.

**Narration:**

You're ready to complete the final capstone. Work through the milestones, test each stage, and make sure your report explains its own limitations. When you finish, be ready to explain one cleaning decision and why you made it.

If you'd like extra hands-on practice, you can also try your code in the PyLearn app. Congratulations on completing Python Foundations!

## Production checklist
- [ ] Use approved Kendrick / ElevenLabs v3 voice.
- [ ] Verify code and output before rendering.
- [ ] Keep the examples separate from the required app exercise.
- [ ] Keep narration and visual directions separate.
- [ ] Watch the full render before approval.
