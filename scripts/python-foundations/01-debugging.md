# PyLearn Video — 01 — Debugging: Ask Smaller Questions

**Voice lock — mandatory:** Use the user-approved Kendrick voice with ElevenLabs v3. Do not substitute another voice or preset.
**Canonical source:** Pylearn-build260/content/python-foundations/modules/01-debugging.md, branch ccr-c7f6fdd7-xpzi3g.
**Use:** Full teaching video, not a short outline. Narrate only spoken text; keep scene headings, code labels, and visual directions out of text-to-speech. Do not show the app's required exercise solution.

**Track 2 visual identity:** Keep the same teacher and pacing, but frame the lesson as a developer's investigation. Use a deep graphite workspace, restrained teal highlights, and amber only for the line under investigation. Replace repeated input/output cards with a bug trail: symptom → isolate → test → verified fix. Use a magnified code line, a small stack trace, and a clean before/after diff. Avoid flashy glitch effects or changing the teacher's visual identity.

## Scene 1 — Three kinds of failure

**Visual:** Reveal the code gradually. Ask for a prediction before running it. Show the output only after the run.

**Narration:**

A program can fail in more than one way. Sometimes Python cannot understand the code. That is a syntax error. Sometimes the code starts and then crashes; that is a runtime error. And sometimes the program runs perfectly but gives the wrong answer. That last case is easy to miss, especially when working with data.

**Code**
    
    print(10 + 20)
        print(10 + 20)  # a wrong assumption can still produce valid code

**Expected output**
    
    30
        30

**Narration:**

The program runs, but a correct-looking run does not prove the answer is correct. We need to check the logic and the data too.

## Scene 2 — Investigate, don't guess

**Visual:** Reveal the code gradually. Ask for a prediction before running it. Show the output only after the run.

**Narration:**

Imagine we want the average of three scores. The program runs, but the result is wrong. Before editing anything, ask what the code assumes.

**Code**
    
    scores = [80, 90, 100]
        average = sum(scores) / 4
        print(average)

**Expected output**
    
    67.5

**Narration:**

There are three scores, but the code divides by four. Python did exactly what we asked; our assumption was wrong. We can inspect the values and the number of items.

## Scene 3 — Make the problem smaller

**Visual:** Reveal the code gradually. Ask for a prediction before running it. Show the output only after the run.

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

These checks reveal what the program actually has. They are more useful than changing random lines until the error disappears.

## Scene 4 — Empty input

**Visual:** Reveal the code gradually. Ask for a prediction before running it. Show the output only after the run.

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

The condition prevents us from accessing a first item when there is none. Small edge cases often reveal assumptions that normal examples hide.

## Your turn — predict, run, explain

**Visual:** Keep the editor uncluttered. Show a fresh, related prompt without using the app's required exercise code.

**Narration:**

Pause the video and try a small variation of the example. Predict the output before you run it. Then run the code, compare the result with your prediction, and explain why it happened. If the result surprises you, inspect the values and change one thing at a time.

This is extra guided practice, not the required PyLearn exercise solution.

## Recap

**Narration:**

Today, you learned the core idea behind debugging. Keep the stages clear, test your assumptions, and make the program's behavior visible. In the next lesson, we'll build on this skill.

## Final call to action — watch the practice video

**Visual:** Neutral end card reading “Next: Practice Video”. Do not show unfinished app screens or invent navigation.

**Narration:**

Great work! You've finished Debugging: Ask Smaller Questions. Next, watch the practice video. I recommend watching it because we'll use a fresh example to reinforce the skill from this lesson.

After the practice video, complete the exercise to unlock the next lesson. If you'd like extra hands-on practice, you can also try it in the PyLearn app.

**Visual:** Hold the end card long enough to read.

## Production checklist

- [ ] Use the approved Kendrick voice with ElevenLabs v3.
- [ ] Verify every example and expected output in Python before rendering.
- [ ] Reveal code before running it; reveal output only after the run.
- [ ] Keep narration separate from production directions.
- [ ] Do not show the required app exercise solution or hidden tests.
- [ ] Watch the complete rendered video at normal speed before approval.
