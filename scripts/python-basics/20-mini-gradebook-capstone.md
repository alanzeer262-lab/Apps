# PyLearn Video 20 — Mini Gradebook Capstone

> **MANDATORY VOICE SETTINGS — DO NOT CHANGE**
> - Voice: Kendrick
> - Model: ElevenLabs v3
> - Voice setup: user confirmed the approved Kendrick / ElevenLabs v3 setup is settled; use the existing approved configuration without substitution.
> - No guessed ID, substitution, or preset. Use the same approved voice identity throughout.
> - Speak narration only; do not read headings or bracketed directions aloud.

**Canonical source:** `Pylearn-build260/content/python-basics/projects/capstone-gradebook.md`, branch `ccr-c7f6fdd7-xpzi3g`.  
**Target runtime:** Approximately 5–7 minutes.  
**Capstone rule:** Explain the workflow and milestone sequence without displaying completed function implementations, full solutions, or completed milestone outputs.

## Scene 1 — Bring the skills together

**Visual:** Title card: “Mini Gradebook Capstone.” Then show the data shape `(name, score)` and a short list of records without revealing any completed solution.

**Narration:**

Welcome to the Mini Gradebook Capstone.

You've spent the Python Basics track learning individual tools: variables, strings, numbers, conditions, lists, loops, dictionaries, and functions. Now the question changes.

Instead of asking, “What does this Python feature do?” we're asking, “How can I combine several Python features to answer a useful question?”

You'll build a small gradebook in five graded milestones. Each milestone has one clear job, and together they form a complete analysis workflow.

## Scene 2 — Inspect the data first

**Visual:** Show the record shape `(name, score)`, then a short loop that unpacks records. Do not show any capstone function solution.

**Code**
```python
records = [
    ("Mia", 81),
    ("Noah", 67)
]

for name, score in records:
    print(name, score)
```

**Expected output**
```text
Mia 81
Noah 67
```

**Narration:**

The gradebook uses a Python list containing records. Each record is a tuple with a name and a score.

The list holds many records. The tuple keeps the name and score together. The name is text, and the score is a number.

Before processing data, inspect it. Make sure you understand what each record contains and how many records are present. This is a simple habit, but it's useful in real programming and data analysis.

## Scene 3 — The five milestones

**Visual:** Reveal the milestones one at a time, with a short label and a simple icon. Do not display implementation code or completed output values.

**On-screen sequence**
1. Average score
2. Top scorer
3. Who passed
4. Letter grades
5. Grade distribution

**Narration:**

Milestone one asks you to calculate the average score. You'll visit the records, collect the scores, calculate the mean, and round it to two decimal places.

Milestone two asks you to find the top scorer. This is a search problem: keep track of the best result you've seen so far. If two people tie, keep the first person who appeared.

Milestone three asks you to find everyone who passed a chosen cutoff. This is filtering. Visit each record, check the score, and keep the name when the score meets the rule. Preserve the original order.

Milestone four asks you to assign a letter grade to each learner and return a dictionary. You'll combine a score, a set of conditions, and a key-value result.

Milestone five asks you to count the letter grades. That creates a frequency table showing how many people received each category.

Each milestone uses ideas you've already practiced. The challenge is combining them carefully.

## Scene 4 — Solve one question at a time

**Visual:** Show the flow “calculate → search → filter → classify → count.” Keep the code editor clean.

**Narration:**

Don't try to write the whole gradebook at once.

The milestones are ordered to help you build one piece at a time. First calculate a summary. Then search for the best result. Then filter records. After that, classify scores into letters and count the categories.

For each milestone, ask three questions.

What information do I have? What calculation or decision do I need? And what should the function return?

When those questions are clear, the implementation becomes easier to plan.

## Scene 5 — Think about boundaries and ties

**Visual:** Show boundary values such as 69, 70, and 90 as examples of testing, without revealing the full milestone result. Show two equal scores for the tie rule.

**Narration:**

Some details deserve special attention.

When a score is exactly at a threshold, it must follow the rule as written. Test values below, at, and above each boundary.

For the top scorer, consider a tie. The capstone says to keep the first person who appeared if two people have the same highest score. Your comparison logic should respect that requirement.

These are not decorative details. They are part of the function's contract, and the tests will check the behavior.

## Scene 6 — Debug one small piece at a time

**Visual:** Show a short inspection loop and a boundary-test checklist. Do not show any complete milestone function.

**Narration:**

If a milestone fails, don't immediately rewrite everything.

Test a smaller piece. If the records look wrong, print each name and score. If the grade logic is wrong, test a few boundary values. If a count is wrong, inspect the grade labels before inspecting the frequency table.

Debugging means asking small questions of your code. It isn't a sign that you failed to learn Python. It's part of learning to program.

## Scene 7 — What completion means

**Visual:** Show a clean checklist of skills: inspect records, calculate, search, filter, classify, count, combine functions. Do not show the final dataset analysis.

**Narration:**

When all five milestones pass, you've done more than memorize Python syntax.

You've represented a dataset, inspected its records, calculated a summary, searched for a best value, filtered records, classified values, and counted categories.

You've combined functions, loops, tuples, conditions, lists, and dictionaries to solve one useful problem.

The next track can introduce tools such as pandas and Jupyter. Those tools make many operations shorter and more powerful, but the reasoning will feel familiar.

The goal of Python Basics is not to memorize Python. It's to become capable of using Python to solve a problem.

## Final call to action — watch the capstone practice video

**Visual:** Use a neutral end card reading “Next: Capstone Practice Video”. Do not show or describe unfinished PyLearn app screens or reveal a completed project/capstone solution.

**Narration:**

Excellent work! You've reached the final lesson of Python Basics and built up the skills needed for this capstone. The next step is to watch the capstone practice video. I recommend watching it to reinforce the approach and prepare you to complete the final exercise.

After the practice video, complete the capstone exercise. You can also try your code in the PyLearn app if you'd like extra hands-on practice.

**Visual:** Hold the “Next: Capstone Practice Video” end card long enough to read.

## Production and QA checklist

- [x] Approved Kendrick / ElevenLabs v3 voice setup confirmed by the user; use the existing configuration without substitution.
- [x] Use the approved Kendrick voice with ElevenLabs v3, as confirmed by the user.
- [ ] Keep production notes out of spoken narration.
- [ ] Do not display full implementations for any milestone.
- [ ] Do not display completed milestone outputs, hidden tests, or a full capstone solution.
- [ ] Preserve the five milestone sequence and tie/boundary requirements.
- [x] Use a neutral end card directing learners to the matching practice video; no app UI footage is required.
