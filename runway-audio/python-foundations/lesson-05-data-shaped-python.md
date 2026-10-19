Before using a data-analysis library, we can practice the underlying ideas with plain Python. A list can hold one dictionary per row, and each dictionary can use named fields.

Named fields make the data easier to understand than relying on positions like record zero or record one.

Selection asks for a field. Filtering keeps only rows that meet a condition. These are two common operations in data analysis.

The first operation extracts every score. The second keeps records with scores of at least eighty. Notice that the filter keeps whole rows, not just their scores.

A derived field is calculated from existing data. We can add a pass flag to each record using a consistent threshold.

The new field records a decision based on the score. In real analysis, we should document the threshold so people know what passed means.

Grouping means collecting rows by a shared category. A dictionary can count how often each topic appears.

We now have the core ideas behind later DataFrame work: select fields, filter rows, create derived values, and group records.

Great work! You've finished Think in Tables Before pandas. Next, watch the practice video. I recommend watching it because we'll use a fresh example to reinforce the skill from this lesson.

After the practice video, complete the exercise to unlock the next lesson. If you'd like extra hands-on practice, you can also try it in the PyLearn app.
