# PyLearn Guided Practice — Debugging Practice

**Voice lock:** Use the approved Kendrick voice with ElevenLabs v3; do not substitute another voice.
**Canonical source:** Pylearn-build260/content/python-foundations/modules/01-debugging.md, branch ccr-c7f6fdd7-xpzi3g.
**Purpose:** Separate practice companion using fresh examples. Never reveal the required app exercise solution.
**Track 2 practice visuals:** Use the same graphite/teal developer workspace as its lesson, but make this companion more interactive: pause cards that ask the learner to predict, magnify the suspicious line, and reveal the test result after a short beat. Amber marks the current hypothesis; teal marks the verified fix. Keep the teacher and voice unchanged.

## Scene 1 — Find the wrong assumption

**Narration:** Let's practise debugging with a fresh example. The code runs, but the average looks suspicious. Inspect the number of values and the denominator before changing anything.

**Code**

    temperatures = [18, 20, 22]
    average = sum(temperatures) / 4
    print(average)
    print(len(temperatures))

**Expected output**

    15.0
    3

The list has three values, but the code divides by four. Correct the assumption, then run the smallest test again.

## Scene 2 — Recognize a runtime error

**Code**

    value = int("twenty")

**Expected output:** ValueError during conversion.

**Narration:** This is a runtime conversion error. Reproduce it with the smallest possible input, then decide how invalid input should be handled. Do not randomly edit unrelated lines.

## Close — Complete the exercise

**Visual:** End card: “Your turn: Complete the exercise”. Do not show unfinished PyLearn app screens.

**Narration:** Good work. Now complete the exercise to unlock the next lesson. Use the habits from this practice: test small cases, check assumptions, and change one thing at a time. If you'd like extra hands-on practice, you can also try it in the PyLearn app.

## Production checklist
- [ ] Use approved Kendrick / ElevenLabs v3 voice.
- [ ] Verify all code and outputs in Python.
- [ ] Keep examples distinct from the required app exercise.
- [ ] Keep code and output synchronized with narration.
- [ ] Watch the full render before approval.
