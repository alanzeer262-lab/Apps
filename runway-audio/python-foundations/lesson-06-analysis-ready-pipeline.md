A reliable data workflow moves through deliberate stages: inspect, validate, clean, transform, summarize, and report. Each stage answers a different question, and the order matters.

We start by counting what arrived. We should not quietly discard rows before we know what the input contains.

A score stored as text needs conversion. A word such as oops cannot be converted to an integer. We'll keep valid values separate from invalid values so the report can explain what happened.

This is one explicit cleaning policy: retain valid numeric scores and record the invalid value. Different datasets may need different rules, but the choice must be clear.

Only after validation can we calculate the average for the valid scores. The report should state how many rows were read and how many were usable.

The average describes the three valid scores, not all four original rows. Reporting the count prevents readers from misunderstanding the number.

Missing values, duplicate records, inconsistent capitalization, and out-of-range scores all require decisions. There is no universal cleaning rule. Choose it, document it, and apply it consistently.

A trustworthy report shows both the result and its limitations. This pipeline is the bridge from beginner Python to dedicated analysis tools.

Great work! You've finished From Raw Records to a Reliable Report. Next, watch the practice video. I recommend watching it because we'll use a fresh example to reinforce the skill from this lesson.

After the practice video, complete the exercise to unlock the next lesson. If you'd like extra hands-on practice, you can also try it in the PyLearn app.
