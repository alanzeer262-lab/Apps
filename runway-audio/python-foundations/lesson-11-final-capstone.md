Welcome to the final build of Python Foundations. You've practised debugging, reading C S V records, organizing code into modules, validating input, testing behavior, and summarizing table-shaped data. Now you'll bring those skills together in one Learning Analytics Toolkit.

The input is a C S V containing learner name, topic, score, attempt count, and completion status. Realistic data is rarely perfect, so the dataset includes a blank score, a score stored as text, a duplicate row, inconsistent topic capitalization, and an out-of-range score.

Your goal is not to pretend the data is clean. Your goal is to build a pipeline that handles it deliberately and explains what happened.

Work through five milestones. First, load the C S V and inspect what arrived. Keep the original row count. Second, validate records and track invalid rows and rejection reasons. Third, clean and transform the data using documented decisions. Fourth, analyze valid records: calculate the average, identify the top performer, and produce a grade distribution. Fifth, create the final report.

Your report must include rows read, valid rows, invalid rows, cleaning decisions, average score, top performer, grade distribution, and one warning or limitation.

A report can look polished and still be wrong. Test normal records, empty data, invalid scores, and boundary values. Keep loading separate from validation and validation separate from aggregation, so you can find problems without guessing.

When the report works, make one deliberate modification: add a count by topic, change the pass threshold and update the report, or add a grade category. Rerun your tests. The goal is to prove you can change a working program without breaking its core behavior.

This is a real reference run, not a decorative mock-up. Seven rows entered the pipeline. Three remained valid after the documented rules, and four were excluded: one blank score, one duplicate, one out-of-range score, and one non-numeric score. The average is eighty-five, calculated from eighty-eight, seventy-two, and ninety-five. Mira is the top performer with ninety-five. The grade distribution also comes from those same three scores.

Your own result will depend on your input data and the cleaning rules you choose. If you use this exact demonstration C S V and these same rules, your report should match these values. If your result differs, investigate it rather than changing the displayed numbers to make them match.

You've reached the final lesson of Python Foundations. Next, watch the capstone practice video. I recommend watching it to help you plan the milestones and check your approach.

After the practice video, complete the final capstone exercise. Take it one stage at a time, test your work, and be ready to explain one cleaning decision. You can also try your code in the PyLearn app for extra hands-on practice.
