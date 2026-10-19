# PyLearn Video — 08 — Build: Validate Intake

**Voice lock — mandatory:** Use the user-approved Kendrick voice with ElevenLabs v3. Do not substitute another voice or preset.
**Canonical source:** Pylearn-build260/content/python-foundations/modules/08-build-validate.md, branch ccr-c7f6fdd7-xpzi3g.
**Use:** Full teaching video, not a short outline. Narrate only spoken text; keep scene headings, code labels, and visual directions out of text-to-speech. Do not show the app's required exercise solution.

## Scene 1 — Why validation is a gate

**Visual:** Reveal the code gradually. Ask for a prediction before running it. Show the output only after the run.

**Narration:**

A score of 150 or minus one can quietly distort every number in a report. Validation checks whether a record meets the rules before it is included in calculations. Keep it separate from loading so both parts can be tested independently.

**Code**
    
    scores = [88, 150, -1, 72]
        valid = [score for score in scores if 0 <= score <= 100]
        print(valid)

**Expected output**
    
    [88, 72]

**Narration:**

This demonstration uses a range from zero to one hundred. The toolkit should apply the rule consistently and keep a reason for every rejected record.

## Scene 2 — Text can fail conversion

**Visual:** Reveal the code gradually. Ask for a prediction before running it. Show the output only after the run.

**Narration:**

CSV data often arrives as text. Conversion can fail if a field contains a word or is blank. Catch that failure and record it as invalid instead of crashing the entire pipeline.

**Code**
    
    raw_values = ["88", "oops", "", "72"]
        valid = []
        rejected = []
        for raw in raw_values:
            try:
                score = int(raw)
                if 0 <= score <= 100:
                    valid.append(score)
                else:
                    rejected.append((raw, "out of range"))
            except ValueError:
                rejected.append((raw, "invalid number"))
        print(valid)
        print(rejected)

**Expected output**
    
    [88, 72]
        [('oops', 'invalid number'), ('', 'invalid number')]

**Narration:**

There are two different failure reasons here. Separating them makes the report more useful and helps us understand the quality of the source data.

## Scene 3 — Test the boundary

**Visual:** Reveal the code gradually. Ask for a prediction before running it. Show the output only after the run.

**Narration:**

A boundary is a value at the edge of the allowed range. Test zero and one hundred, then test values just outside the range. A validation function should make these decisions predictable.

**Code**
    
    print(0 <= 0 <= 100)
        print(0 <= 100 <= 100)
        print(0 <= -1 <= 100)
        print(0 <= 101 <= 100)

**Expected output**
    
    True
        True
        False
        False

**Narration:**

These checks make the rule visible. Do not let the summary function silently invent a validation policy; give it records that have already passed the gate.

## Your turn — predict, run, explain

**Visual:** Keep the editor uncluttered. Show a fresh, related prompt without using the app's required exercise code.

**Narration:**

Pause the video and try a small variation of the example. Predict the output before you run it. Then run the code, compare the result with your prediction, and explain why it happened. If the result surprises you, inspect the values and change one thing at a time.

This is extra guided practice, not the required PyLearn exercise solution.

## Recap

**Narration:**

Today, you learned the core idea behind validation as separate gate. Keep the stages clear, test your assumptions, and make the program's behavior visible. In the next lesson, we'll build on this skill.

## Final call to action — watch the practice video

**Visual:** Neutral end card reading “Next: Practice Video”. Do not show unfinished app screens or invent navigation.

**Narration:**

Great work! You've finished Build: Validate Intake. Next, watch the practice video. I recommend watching it because we'll use a fresh example to reinforce the skill from this lesson.

After the practice video, complete the exercise to unlock the next lesson. If you'd like extra hands-on practice, you can also try it in the PyLearn app.

**Visual:** Hold the end card long enough to read.

## Production checklist

- [ ] Use the approved Kendrick voice with ElevenLabs v3.
- [ ] Verify every example and expected output in Python before rendering.
- [ ] Reveal code before running it; reveal output only after the run.
- [ ] Keep narration separate from production directions.
- [ ] Do not show the required app exercise solution or hidden tests.
- [ ] Watch the complete rendered video at normal speed before approval.
