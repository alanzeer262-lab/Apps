# PyLearn Guided Practice — 01 — Debugging: Ask Smaller Questions

**Voice lock — mandatory:** Use the user-approved Kendrick voice with ElevenLabs v3; do not substitute another voice.
**Canonical source:** Pylearn-build260/content/python-foundations/modules/01-debugging.md, branch ccr-c7f6fdd7-xpzi3g.
**Target runtime:** Approximately 3–5 minutes.
**Purpose:** Separate guided-practice companion with fresh examples. Never reveal the required app exercise solution.

## Scene 1 — Three kinds of failure

**Visual:** Use a fresh example and the same uncluttered code-first visual style as the lesson.

**Narration:**

A program can fail in more than one way. Sometimes Python cannot understand the code. That is a syntax error. Sometimes the code starts and then crashes; that is a runtime error. And sometimes the program runs perfectly but gives the wrong answer. That last case is easy to miss, especially when working with data.

**Code**
    
    print(10 + 20)
        print(10 + 20)  # a wrong assumption can still produce valid code

**Expected output**
    
    30
        30

**Narration:**

Predict the result before running the example. Compare the output with your prediction and explain the result in your own words. If it differs, inspect the input and change one thing at a time.

## Scene 2 — Investigate, don't guess

**Visual:** Use a fresh example and the same uncluttered code-first visual style as the lesson.

**Narration:**

Imagine we want the average of three scores. The program runs, but the result is wrong. Before editing anything, ask what the code assumes.

**Code**
    
    scores = [80, 90, 100]
        average = sum(scores) / 4
        print(average)

**Expected output**
    
    67.5

**Narration:**

Predict the result before running the example. Compare the output with your prediction and explain the result in your own words. If it differs, inspect the input and change one thing at a time.

## Scene 3 — Make the problem smaller

**Visual:** Use a fresh example and the same uncluttered code-first visual style as the lesson.

**Narration:**

A useful debugging routine is: reproduce the problem, read the useful error line, inspect the value and its type, reduce the example, change one assumption, and run a small test again.

**Code**
    
    scores = [80, 90, 100]
        print(scores)
        print(len(scores))
        print(type(scores))

**Expected output**
    
    [80, 90, 100]
        3
        <class 'list'>

**Narration:**

Predict the result before running the example. Compare the output with your prediction and explain the result in your own words. If it differs, inspect the input and change one thing at a time.

## Scene 4 — Empty input

**Visual:** Use a fresh example and the same uncluttered code-first visual style as the lesson.

**Narration:**

A function should also be tested with an empty list. There may be no records to inspect, and code that assumes the first item exists can fail.

**Code**
    
    records = []
        print(len(records))
        if records:
            print(records[0])
        else:
            print("No records yet")

**Expected output**
    
    0
        No records yet

**Narration:**

Predict the result before running the example. Compare the output with your prediction and explain the result in your own words. If it differs, inspect the input and change one thing at a time.

## Close — Complete the exercise

**Visual:** End card: “Your turn: Complete the exercise”. Do not show or describe unfinished PyLearn app screens.

**Narration:**

Good work. Now complete the exercise to unlock the next lesson. Use the habits from this practice: test small cases, check your assumptions, and make one change at a time. If you'd like extra hands-on practice, you can also try it in the PyLearn app.

## Production checklist

- [ ] Use the approved Kendrick voice with ElevenLabs v3.
- [ ] Verify all example code and outputs in Python.
- [ ] Keep the example distinct from the required app exercise.
- [ ] Do not reveal the exercise solution or hidden tests.
- [ ] Keep code and output synchronized with narration.
- [ ] End by directing the learner to complete the exercise.
