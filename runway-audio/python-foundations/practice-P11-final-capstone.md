Welcome to the final capstone practice. The goal is to build a reliable pipeline, not just make one calculation work. Start by inspecting the C S V. It contains names, topics, scores, attempt counts, and completion status. The source data includes a blank score, a score stored as text, a duplicate row, inconsistent topic capitalization, and an out-of-range score.

Before cleaning anything, ask what arrived. How many rows are there? Which fields are present? Which values need closer inspection? Keep a record of your observations so the report can explain what changed.

Keep the stages separate. Loading turns the C S V into records. Inspection helps you understand the input. Validation checks the rules. Cleaning applies documented decisions. Analysis calculates the requested summaries. Reporting explains both results and limitations.

Your report needs eight things: rows read, valid rows, invalid rows, cleaning decisions, average score, top performer, grade distribution, and one warning or limitation. Do not invent a cleaning rule after seeing the result just because it produces a convenient number. Choose a rule, document it, and apply it consistently.

Test normal input, empty input, invalid values, and boundary values. Compare expected and actual results. If something fails, reproduce the smallest case and change one assumption at a time.

After the report works, choose one modification: add a count by topic, change the pass threshold and update the report, or add a grade category. Rerun your tests to make sure the change has not broken existing behavior.

You're ready to complete the final capstone. Work through the milestones, test each stage, and make sure your report explains its own limitations. When you finish, be ready to explain one cleaning decision and why you made it.

If you'd like extra hands-on practice, you can also try your code in the PyLearn app. Congratulations on completing Python Foundations!
