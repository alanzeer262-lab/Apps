# PyLearn Video 07 — Conditionals: if, elif, and else

> **MANDATORY VOICE SETTINGS — DO NOT CHANGE**
> - Voice: Kendrick
> - Model: ElevenLabs v3
> - Voice ID: exact approved Kendrick voice ID not recorded in the reviewed repository files; insert the verified ID from the original Runway setup before generating narration.
> - No guessed ID, voice substitution, or preset. Same approved voice for every part.
> - Speak narration only. Do not read headings or bracketed production notes aloud.

**Canonical source:** `Pylearn-build260/content/python-basics/modules/07-conditionals.md`, branch `ccr-c7f6fdd7-xpzi3g`.  
**Target runtime:** Approximately 7–8 minutes. Do not reveal the required app exercise solution.

## Scene 1 — Programs make decisions

**Visual:** Keep the established editor. Display a fictional score of 82, then reveal the condition line by line.

**Narration:**

Welcome back to PyLearn.

A program doesn't only calculate values. It can also make decisions based on those values.

Imagine a learner has a score of eighty-two. Should the program display a message that says the learner passed? We can express that rule with a conditional.

**Code**
```python
score = 82

if score >= 70:
    print("Passed")
```

**Expected output**
```text
Passed
```

**Narration:**

Read the code as a sentence: if the score is at least seventy, print Passed.

Python checks the condition. Since eighty-two is greater than or equal to seventy, the condition is true, so the indented print line runs.

The word if introduces the condition. The colon marks the start of the block, and the indented line is the action to perform when the condition is true.

## Scene 2 — Indentation changes meaning

**Visual:** Highlight the four spaces before the print line. Do not show a syntax error unless you run a separate, intentional demonstration.

**Narration:**

Notice the indentation before print. Python uses indentation to show which lines belong to a block. Four spaces is the common convention.

Indentation is not decoration. It tells Python which instructions belong to the condition. If the line is not indented correctly, the code may fail or behave differently from what you intended.

When you write an if statement, remember three parts: the condition, a colon, and the indented block that should run when the condition is true.

## Scene 3 — Add an alternative with else

**Visual:** Add an else block beneath the first branch. Keep the two branches visually distinct.

**Code**
```python
score = 62

if score >= 70:
    print("Passed")
else:
    print("Needs more practice")
```

**Expected output**
```text
Needs more practice
```

**Narration:**

What if the score is below seventy? We can add else to describe the alternative.

If the condition is true, Python runs the first branch. Otherwise, it runs the else branch. In this example, sixty-two is below seventy, so the program prints Needs more practice.

For this simple if-and-else structure, one of the two branches runs. The condition determines which one.

## Scene 4 — Handle more than two cases with elif

**Visual:** Build a separate example with named categories. Reveal the branches from top to bottom. Keep the order visible.

**Code**
```python
score = 84

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(grade)
```

**Expected output**
```text
B
```

**Narration:**

Sometimes there are more than two possibilities. The word elif means “else if.” It lets us test another condition when the earlier condition was false.

Python checks these conditions from top to bottom. For a score of eighty-four, the first condition is false because the score is below ninety. The next condition is true because the score is at least eighty. Python assigns the grade B and stops checking the remaining branches.

The order matters. Python uses the first condition that is true. If a broad condition appears before a more specific one, it may catch values that should have reached a later branch.

## Scene 5 — Write the rules before the code

**Visual:** Show a simple text list of rules first, then the matching code. Use a different score from the app exercise's required starting values.

**Narration:**

Before writing a decision, describe the rules in ordinary language.

For this example, a score of ninety or higher receives A. A score from eighty through eighty-nine receives B. A score from seventy through seventy-nine receives C. Anything below seventy receives F.

Writing the rules first helps us check whether the code matches the intention. It also makes the boundaries clear.

**Visual:** Highlight the comparisons `>= 90`, `>= 80`, and `>= 70` in order. Do not fill the screen with extra explanatory paragraphs.

**Narration:**

Notice that the conditions use “at least.” That means the boundary value is included. The first branch catches ninety and above. If the score is below ninety, Python moves to the next branch, and so on.

## Scene 6 — Test boundaries deliberately

**Visual:** Show the values 89, 90, 79, 80, 69, and 70 as a test list. Demonstrate only the idea of testing boundaries; do not display a complete answer table for the required exercise.

**Narration:**

A program can look correct for an ordinary value and still fail at the boundary where one rule changes into another.

For a rule that changes at eighty, test seventy-nine and eighty. For a rule that changes at ninety, test eighty-nine and ninety.

These pairs help us discover whether the boundary is included in the right category.

Don't test only values from the middle of a range. Test just below the boundary, exactly at the boundary, and just above it. This habit is useful in grading rules, eligibility checks, prices, and many other programs.

## Scene 7 — Combine conditions

**Visual:** Reveal the two requirements separately, then combine them with and.

**Code**
```python
score = 82
attempts = 2

if score >= 70 and attempts <= 3:
    print("Passed")
else:
    print("Check requirements")
```

**Expected output**
```text
Passed
```

**Narration:**

A condition can combine Boolean expressions. Here, the score must be at least seventy, and the number of attempts must be three or fewer.

The word and means both requirements must be true. If either one is false, the combined condition is false and Python follows the alternative branch.

Keep conditions readable. If a condition is difficult to explain in one sentence, break it into smaller questions and inspect each one.

## Scene 8 — Recap

**Visual:** Reveal: if, elif, else, indentation, order, boundaries. Keep the editor clean.

**Narration:**

Let's recap.

If runs a block when its condition is true. Else gives us an alternative, and elif lets us check additional cases.

Indentation tells Python which lines belong to each block. With multiple branches, Python checks from top to bottom and takes the first branch whose condition is true.

Write rules in plain English before translating them into code. Pay special attention to boundary values, and test the values just below, at, and above each boundary.

## Final call to action — required for in-app and YouTube versions

**Visual:** Show the real PyLearn navigation path to Lesson 7 and highlight its required coding exercise. Do not show a completed score-classifier solution or unverified app UI. Hold the navigation screen long enough to read.

**Narration:**

Now it's your turn to write code yourself.

Open PyLearn and go to Lesson 7, then complete its required coding exercise. If you're watching this on YouTube, open PyLearn and find this lesson there.

Run your code, read the feedback, and fix mistakes as needed. Practice Drills are optional. Passing the required exercise is what unlocks the next lesson.

Pause this video and start coding.

## Production and QA checklist

- [ ] Verify the exact approved Kendrick voice ID before generating audio.
- [ ] Use ElevenLabs v3 and the same approved voice identity throughout.
- [ ] Keep production notes out of spoken text.
- [ ] Verify every code sample and output in Python.
- [ ] Ensure indentation is visible and code remains legible on a phone.
- [ ] Do not reveal the required Lesson 7 exercise solution.
- [ ] Preserve the required PyLearn navigation ending and progression rule.
