# PyLearn Video 18 — Project 7: Reusable Analysis Toolkit

> **MANDATORY VOICE SETTINGS — DO NOT CHANGE**
> - Voice: Kendrick
> - Model: ElevenLabs v3
> - Voice ID: exact approved Kendrick voice ID is not recorded in the reviewed repository files; insert the verified ID from the original Runway setup before generating audio.
> - Do not guess or substitute a voice or preset. Use the same approved voice throughout.
> - Speak narration only; do not read headings or bracketed directions aloud.

**Canonical source:** `Pylearn-build260/content/python-basics/modules/18-build-toolkit.md`, branch `ccr-c7f6fdd7-xpzi3g`.  
**Target runtime:** Approximately 5–7 minutes. Do not show the complete required implementation.

## Scene 1 — When a program grows

**Visual:** Show a crowded block of repeated analysis steps, then separate two named functions. Avoid displaying a full toolkit implementation.

**Narration:**

Welcome back. Your Learning Analytics Toolkit now has several kinds of logic: calculating averages, comparing scores, and working with records.

As a program grows, a large block of code can become hard to understand and change. Functions let us give a name to a behavior so we can reuse it and test it separately.

In this project, you'll focus on two functions: one to calculate an average score, and another to identify the top scorer in a set of records.

## Scene 2 — Give one calculation a clear name

**Visual:** Use a separate example list. Reveal a small function and then its call.

**Code**
```python
def total_points(points):
    return sum(points)

result = total_points([12, 18, 20])
print(result)
```

**Expected output**
```text
50
```

**Narration:**

This function has one clear job: add the values in a list and return the total.

The name tells us what it does. The parameter tells us what input it needs. The return statement sends the result back to the caller.

A function doesn't need to print a message to be useful. Returning a value lets another part of the program decide how to use it.

## Scene 3 — Separate the calculation from the caller

**Visual:** Show a function call assigned to a variable. Highlight that the caller receives the returned result.

**Code**
```python
total = total_points([5, 10, 15])
print(total / 3)
```

**Expected output**
```text
10.0
```

**Narration:**

Here, we reuse the function's returned total in a separate calculation. We don't need to copy the addition logic into every place that needs it.

That's one reason functions are valuable. If the logic changes, we have one place to update. And because the function has a clear input and output, we can test it with small examples.

## Scene 4 — Think about top scorer as a separate job

**Visual:** Show a small independent list of name-score records, then a simple question: “Which record has the highest score?” Do not show a full top_scorer implementation.

**Code**
```python
records = [
    ("Mia", 81),
    ("Noah", 67),
    ("Iris", 93)
]
```

**Narration:**

The second function in your project identifies the top scorer. Its job is different from calculating an average.

The input is a collection of records. Each record keeps a name together with a score. The function needs to compare the scores and determine which record has the highest one.

Plan what the function should return before writing the loop. Should it return a name, a record, or another clearly defined result? Follow the exact contract specified by the app and its tests.

This video does not provide the finished function. Your job is to turn the question into a clear algorithm and implement it.

## Scene 5 — Empty inputs need a rule

**Visual:** Show an empty list next to a function call, then a question mark next to the expected result. Do not invent the required empty-case output.

**Narration:**

Both functions need a deliberate empty-case rule. What should an average function do when there are no scores? What does it mean to find a top scorer when there are no records?

There isn't one universal answer for every program. The important thing is to choose a rule that matches the project requirements, then implement it consistently.

Do not allow an accidental division by zero, and don't invent a top scorer when no records were supplied.

## Scene 6 — Test each function independently

**Visual:** Show a test checklist: typical input, one-item input, empty input. Keep result fields blank so the learner completes them.

**Narration:**

Test each function separately before combining it with the rest of the toolkit.

For the average function, use several values, then one value, then an empty list. For the top-scorer function, try multiple records, a single record, and an empty collection.

These cases help you verify the contract: the function receives the expected input, performs one clear job, and returns a useful result.

If a test fails, you know which function to inspect. That is much easier than debugging a large program all at once.

## Scene 7 — Reflection

**Visual:** Display the question “Would naming this behavior make the program easier to understand and reuse?”

**Narration:**

Before you finish, ask yourself which function from your project would be useful in a completely different program.

The point is not to turn every line into a function. The point is to give reusable behavior a clear name when doing so makes the program easier to understand, test, or change.

## Final call to action — watch the practice video

**Visual:** Use a neutral end card reading “Next: Practice Video”. Do not show or describe unfinished PyLearn app screens or reveal a completed project/capstone solution.

**Narration:**

Great work! You've finished this lesson. The next step is to watch the practice video. I recommend watching it because it will help you apply what you've learned with a fresh example.

After the practice video, complete the exercise to unlock the next lesson. If you'd like extra hands-on practice, you can also try it in the PyLearn app.

**Visual:** Hold the “Next: Practice Video” end card long enough to read.

## Production and QA checklist

- [ ] Verify the exact approved Kendrick voice ID before generating audio.
- [ ] Use ElevenLabs v3 and the same approved voice throughout.
- [ ] Keep production notes out of spoken narration.
- [ ] Verify every demonstration code sample and output in Python.
- [ ] Do not show the complete `average_score` or `top_scorer` required implementations.
- [ ] Do not invent empty-case behavior; follow the app contract.
- [ ] Preserve the project navigation ending and progression rule.
