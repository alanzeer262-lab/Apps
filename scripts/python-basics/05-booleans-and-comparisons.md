# PyLearn Video 05 — Booleans and Comparisons

> **MANDATORY VOICE SETTINGS — DO NOT CHANGE**
> - Voice: Kendrick
> - Model: ElevenLabs v3
> - Voice ID: the exact approved custom Kendrick voice ID is not recorded in the reviewed repository files. Insert the verified ID from the original Runway setup before narration generation.
> - Do not guess, substitute another voice, or use a preset. Use the same approved voice identity throughout.
> - Speak narration only. Do not read scene headings or bracketed production notes aloud.

**Canonical source:** `Pylearn-build260/content/python-basics/modules/05-booleans.md`, branch `ccr-c7f6fdd7-xpzi3g`.  
**Target runtime:** Approximately 6–8 minutes.  
**Purpose:** Full teaching video; do not reveal the required app exercise solution.

## Scene 1 — Programs ask questions

**Visual:** Start with a clean editor and a simple title: “Booleans and Comparisons.” Reveal each expression only when discussed.

**Narration:**

Welcome back to PyLearn.

Programs often need to answer questions. Did a learner pass? Is a score high enough? Is a task finished? Should the program continue?

Python represents the answers to yes-or-no questions with a type called a Boolean. A Boolean has one of two values: True or False.

Notice the capital first letter in both words. In Python, write True and False with capital letters.

Let's ask Python two simple questions.

**Code**
```python
print(10 > 5)
print(10 < 5)
```

**Expected output**
```text
True
False
```

**Narration:**

The first question asks whether ten is greater than five. That's true. The second asks whether ten is less than five. That's false.

The symbols greater than and less than are comparison operators. They compare values and produce a Boolean answer.

## Scene 2 — Common comparison operators

**Visual:** Reveal one comparison at a time, highlight the operator, and display a short label beside it.

**Code**
```python
print(10 == 10)
print(10 != 5)
print(10 > 5)
print(10 < 5)
print(10 >= 10)
print(5 <= 10)
```

**Expected output**
```text
True
True
True
False
True
True
```

**Narration:**

Two equals signs ask whether two values are equal. An exclamation mark followed by an equals sign asks whether they are not equal.

The greater-than symbol asks whether the left value is greater than the right. Less-than asks whether it is smaller.

Greater than or equal includes equality. Less than or equal includes equality too.

Let's run the examples and check the results.

[Run code; reveal output line by line in sync with narration.]

Each comparison produces either True or False. We can store those results in variables, combine them, or use them later to make decisions.

## Scene 3 — One equals sign is not two equals signs

**Visual:** Split the editor into two steps. Highlight the single equals sign, then the double equals sign. Do not imply the two operations are interchangeable.

**Code**
```python
score = 70
print(score == 70)
print(score == 65)
```

**Expected output**
```text
True
False
```

**Narration:**

This distinction is important enough to practice.

A single equals sign assigns a value. In the first line, we store seventy in the variable score.

Two equals signs compare values. The first print statement asks whether score equals seventy. The second asks whether it equals sixty-five.

So the answers are True and False.

When you read your own code, say the single equals sign as “assign” or “store.” Say the double equals sign as “is equal to?” Thinking of them as different actions can prevent a common beginner mistake.

## Scene 4 — Boundaries matter

**Visual:** Introduce a fictional pass threshold of 70. Show a number line with 69, 70, and 71. Keep the condition large and simple.

**Narration:**

Suppose a rule says that a score of seventy or higher counts as passing.

The phrase “or higher” matters. A score of seventy should pass, not fail.

Let's write the condition.

**Code**
```python
score = 70
print(score >= 70)
```

**Expected output**
```text
True
```

**Narration:**

The greater-than-or-equal operator includes the boundary value seventy.

Now imagine the score is sixty-nine. That is below the threshold. A score of seventy-one is above it.

Whenever a rule contains a boundary, test three cases: just below the boundary, exactly at the boundary, and just above it. This catches mistakes that can hide in conditions.

**Visual:** Change only the score to 69, run, then change it to 71 and run again. Narration should identify the values before each run.

**Expected outputs:** For 69, `False`. For 71, `True`.

**Narration:**

The condition is false for sixty-nine and true for seventy-one. This simple testing habit will become useful when you build grade rules, analyze data, and write programs that make decisions.

## Scene 5 — Combine conditions with and

**Visual:** Show the two questions separately, then combine them. Use check marks only after the expression is evaluated.

**Code**
```python
score = 82
attendance = 90
print(score >= 70)
print(attendance >= 80)
print(score >= 70 and attendance >= 80)
```

**Expected output**
```text
True
True
True
```

**Narration:**

Sometimes a decision depends on more than one question.

Here, the score must be at least seventy, and attendance must be at least eighty. The word and means both conditions must be true.

The score condition is true. The attendance condition is true. Because both are true, the combined condition is true.

Read the full expression like a sentence: the score is at least seventy, and attendance is at least eighty.

If either condition were false, the combined result would be false. Use and when every requirement must be satisfied.

## Scene 6 — Combine conditions with or and not

**Visual:** Reveal each expression in turn. Use a simple two-row truth illustration only if it remains legible.

**Code**
```python
is_beginner = True
needs_help = False
print(is_beginner or needs_help)
print(not is_beginner)
```

**Expected output**
```text
True
False
```

**Narration:**

The word or works differently from and. With or, at least one condition must be true for the combined result to be true.

In this example, is_beginner is true, so the first expression is true even though needs_help is false.

The word not reverses a Boolean value. Since is_beginner is true, not is_beginner is false.

These words help us express rules in plain terms. And means every required condition must be true. Or means at least one can be true. Not reverses the answer.

## Scene 7 — Read a condition as a sentence

**Visual:** Display the condition and an English interpretation beside it. Keep both on screen during the narration.

**Code**
```python
score = 82
attempts = 2
print(score >= 70 and attempts < 3)
```

**Expected output**
```text
True
```

**Narration:**

Let's read this condition out loud in plain English.

The score is at least seventy, and the number of attempts is less than three.

The score is eighty-two, so the first part is true. There have been two attempts, so the second part is also true. Because both conditions are true, the full expression is true.

If the English sentence sounds wrong, the Python condition may be wrong too. Break a complicated rule into smaller questions, check each one, and then combine them.

## Scene 8 — Recap and test your understanding

**Visual:** Show the terms True/False, comparison operators, assignment versus comparison, and/or/not, boundary tests. Do not display the app exercise's provided values and full answers.

**Narration:**

Let's recap.

Booleans are True and False. Comparison operators ask questions about values and return Boolean results.

A single equals sign assigns a value. Two equals signs compare values. Greater-than-or-equal and less-than-or-equal include the boundary.

And combines conditions when all of them must be true. Or allows at least one condition to be true. Not reverses a Boolean.

When you write a rule, read it as an English sentence. If it includes a boundary, test a value below it, at it, and above it.

## Final call to action — watch the practice video

**Visual:** Use a neutral end card reading “Next: Practice Video”. Do not show or describe unfinished PyLearn app screens.

**Narration:**

Great work! You've finished this lesson. The next step is to watch the practice video. I recommend watching it because it will help you apply what you've learned with a fresh example.

After the practice video, complete the exercise to unlock the next lesson. If you'd like extra hands-on practice, you can also try it in the PyLearn app.

**Visual:** Hold the “Next: Practice Video” end card long enough to read.

## Production and QA checklist

- [x] Approved Kendrick / ElevenLabs v3 voice setup confirmed by the user; use the existing configuration without substitution.
- [x] Use the approved Kendrick voice with ElevenLabs v3, as confirmed by the user.
- [ ] Keep headings and production directions out of the spoken text.
- [ ] Verify each code sample and output in Python.
- [ ] Keep the comparison symbols and capitalization of True/False clear on screen.
- [ ] Do not reveal the required Lesson 5 exercise solution.
- [x] Use the agreed lesson-to-practice handoff; no app UI footage is required.
