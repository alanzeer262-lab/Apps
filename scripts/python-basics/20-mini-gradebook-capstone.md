# PyLearn Video 20 — Mini Gradebook Capstone

**Voice lock — mandatory:** Kendrick voice; ElevenLabs v3; use the exact approved Kendrick voice ID; no substitution or preset; same voice throughout.
**Canonical source:** `Pylearn-build260/content/python-basics/projects/capstone-gradebook.md` and `content/python-basics/exercises/pb-capstone-m1.yaml` through `pb-capstone-m5.yaml`.
**Target:** 8–10 minutes. This capstone is separate from the 19 Python Basics modules.
**Production rule:** This script teaches the five milestone goals. Do not imply the app requires a different interface, additional fields, or invalid-score handling not specified by the capstone.

## Scene 1 — One small dataset

**Visual:** Show only the sample records. Keep each tuple intact and readable. Do not reveal a completed solution.

```python
records = [
    ("Ada", 88),
    ("Lin", 72),
    ("Sam", 95),
    ("Omar", 64),
    ("Mia", 80)
]
```

**Narration:**

“You've learned Python one tool at a time. Now the goal is to combine those tools to answer useful questions about a small dataset.

Our Mini Gradebook stores a list of records. Each record is a tuple containing a name and a score. The list holds all five records.

Notice how familiar ideas come together: a list holds the records, each tuple groups a name and score, the names are strings, and the scores are numbers.

Before analyzing data, inspect it. Let's loop through the records and print each name and score.”

**Visual:** Reveal the loop only as it is spoken; run it and show the five pairs. Then run `print(len(records))` and show `5`.

## Scene 2 — Milestone 1: Average score

**Visual:** Label the goal `average_score(records)`. Build the steps without revealing future milestones: collect or sum the scores, divide by the record count, round to two decimal places.

**Narration:**

“Our first task is to calculate the mean score. The function is called average_score, and it should return the average rounded to two decimal places.

Think through the steps: visit each record, use its score, add the scores, divide by the number of records, and round the result. For the sample data, the expected result is seventy-nine point eight.

This milestone combines tuple unpacking, arithmetic, sum, len, and round. Test the function before moving on.”

**Expected result:** `79.8`.

## Scene 3 — Milestone 2: Find the top scorer

**Visual:** Keep the same sample data. Highlight scores as they are compared. Do not sort the entire list.

**Narration:**

“Next, find the top scorer. The function top_scorer should return the person's name, not the whole tuple and not the score.

One approach is to keep track of the best record seen so far. When a higher score appears, update the best record. If two people tie, keep the first person who appeared in the list.

For our sample data, Sam is the top scorer.”

**Expected result:** `"Sam"`.

## Scene 4 — Milestone 3: Find everyone who passed

**Visual:** Show the function signature `passed(records, cutoff=70)`. Highlight the threshold condition `score >= cutoff`. Preserve original order in the displayed result.

**Narration:**

“The third task is filtering. The function passed returns the names of everyone whose score is at least the cutoff, in their original order. If we don't supply a cutoff, it defaults to seventy.

That means a score of exactly seventy passes. For the sample data, the returned names are Ada, Lin, Sam, and Mia, in that order.

A different cutoff should change who appears in the result, not the order of the records that remain.”

**Expected result:** `["Ada", "Lin", "Sam", "Mia"]`.

## Scene 5 — Milestone 4: Assign letter grades

**Visual:** Reveal one rule at a time; only show the next rule as the narration reaches it.

- 90 or above → A
- 80 to 89 → B
- 70 to 79 → C
- below 70 → F

**Narration:**

“Now we map each learner's name to a letter grade. A score of ninety or above earns A. Eighty through eighty-nine earns B. Seventy through seventy-nine earns C. Anything below seventy earns F.

Check the highest threshold first, then work downward. The function grade_map returns a dictionary where each name is the key and the letter grade is its value.

For example, Ada's score of eighty-eight maps to B, Sam's ninety-five maps to A, and Omar's sixty-four maps to F.”

**Visual:** Run the function only after the full rule has been explained. Verify the dictionary against the source example.

## Scene 6 — Milestone 5: Count the grades

**Visual:** Transform the score records into letters, then reveal the dictionary counter one narrated step at a time.

**Narration:**

“The final milestone is a frequency count. The function grade_counts counts how many learners received each letter grade.

For the sample data, the result is two Bs, one C, one A, and one F. We can build this dictionary by increasing a grade's count each time that grade appears.

You have seen this pattern before. First classify each score, then count the categories.”

**Expected result:** `{"B": 2, "C": 1, "A": 1, "F": 1}`.

## Scene 7 — Debugging and completion

**Visual:** Show the five milestone names in order, not a new all-in-one solution:
1. `average_score(records)`
2. `top_scorer(records)`
3. `passed(records, cutoff=70)`
4. `grade_map(records)`
5. `grade_counts(records)`

**Narration:**

“Don't try to write the whole gradebook at once. The milestones are ordered to help you build one skill at a time: calculate, search, filter, classify, and count.

If a milestone fails, test a smaller piece. Print the records to inspect their shape. For grade rules, test boundary values such as sixty-nine and seventy, seventy-nine and eighty, and eighty-nine and ninety.

When all five milestones pass, you've combined lists, tuples, loops, functions, conditions, and dictionaries to answer real questions about data.

The next track introduces tools such as pandas and Jupyter. Those tools make data work more powerful, but the reasoning you practiced here remains useful.”

**End screen:** “Python Basics Complete” / “Next: Data Analysis”.

## Release checklist
- [ ] All five milestone names, signatures, return values, and source examples match the canonical capstone.
- [ ] Tie behavior for `top_scorer` is explained accurately.
- [ ] The default cutoff and original-order requirement for `passed` are visible.
- [ ] Grade thresholds are exact and shown before the code is run.
- [ ] The grade-count example matches the canonical output.
- [ ] No unsupported invalid-input requirement or empty-case contract is invented.
- [ ] Code and outputs appear only when narration reaches them.
- [ ] Full rendered video is reviewed end-to-end before user review.
