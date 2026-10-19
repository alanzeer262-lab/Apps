# PyLearn Video — 04 — Validation and Testing

**Voice lock — mandatory:** Use the user-approved Kendrick voice with ElevenLabs v3. Do not substitute another voice or preset.
**Canonical source:** Pylearn-build260/content/python-foundations/modules/04-validation-testing.md, branch ccr-c7f6fdd7-xpzi3g.
**Use:** Full teaching video, not a short outline. Narrate only spoken text; keep scene headings, code labels, and visual directions out of text-to-speech. Do not show the app's required exercise solution.

**Track 2 visual identity:** Keep the same teacher and pacing. Use a quality-control dashboard aesthetic: dark slate, teal for passed checks, muted coral for rejected cases, and amber for edge cases. Show test cases moving through a gate, a compact pass/fail matrix, and boundary markers on a number line. Do not rely on input/output cards as the main visual metaphor.

## Scene 1 — One successful run is not proof

**Visual:** Reveal the code gradually. Ask for a prediction before running it. Show the output only after the run.

**Narration:**

A program that works once is not automatically trustworthy. Testing means checking behavior against results we already know. A test should be small, specific, repeatable, and tied to something important.

**Code**
```python
def average_score(scores):
    if not scores:
        return 0.0
    return sum(scores) / len(scores)

assert average_score([10, 20]) == 15
print("Average test passed")
```

**Expected output**
```text
Average test passed
```

**Narration:**

An assert stops the program if its condition is false. If execution reaches the print, the assertion succeeded.

## Scene 2 — Test more than the happy path

**Visual:** Keep the `average_score` function from Scene 1 in the same editor session. Add these assertions beneath it, run them together, and reveal the pass message only after all assertions succeed.

**Narration:**

A normal example is useful, but boundaries and empty input often expose bugs. We should check each behavior we care about.

**Code**
```python
assert average_score([]) == 0.0
assert average_score([7]) == 7
assert average_score([0, 100]) == 50
print("Boundary tests passed")
```

**Expected output**
```text
Boundary tests passed
```

**Narration:**

These tests check an empty list, a single value, and a wide range. The expected answers are known before we run them.

## Scene 3 — Invalid input needs a rule

**Visual:** Reveal the code gradually. Ask for a prediction before running it. Show the output only after the run.

**Narration:**

Testing should include invalid values too. Suppose a score arrives as text and contains a word instead of digits. The program should report that row as invalid, not crash halfway through the report.

**Code**
```python
raw_score = "oops"
try:
    score = int(raw_score)
except ValueError:
    print("Invalid score")
```

**Expected output**
```text
Invalid score
```

**Narration:**

This example demonstrates the conversion failure safely. The full toolkit should keep validation rules explicit and test the error case.

## Scene 4 — Read both sides of a failure

**Visual:** Reveal the code gradually. Ask for a prediction before running it. Show the output only after the run.

**Narration:**

When a test fails, compare the expected result with the actual result before changing code. Try normal input, boundary input, empty input, and invalid input. A few focused tests can provide more confidence than one huge example.

**Code**
```python
expected = 15
actual = average_score([10, 20])
print("Expected:", expected)
print("Actual:", actual)
assert actual == expected
```

**Expected output**
```text
Expected: 15
Actual: 15
```

**Narration:**

Testing is not only about finding mistakes. It makes the behavior of your program clear and repeatable.

## Your turn — predict, run, explain

**Visual:** Keep the editor uncluttered. Show a fresh, related prompt without using the app's required exercise code.

**Narration:**

Pause the video and try a small variation of the example. Predict the output before you run it. Then run the code, compare the result with your prediction, and explain why it happened. If the result surprises you, inspect the values and change one thing at a time.

This is extra guided practice, not the required PyLearn exercise solution.

## Recap

**Narration:**

Today, you learned the core idea behind assertions and edge cases. Keep the stages clear, test your assumptions, and make the program's behavior visible. In the next lesson, we'll build on this skill.

## Final call to action — watch the practice video

**Visual:** Neutral end card reading “Next: Practice Video”. Do not show unfinished app screens or invent navigation.

**Narration:**

Great work! You've finished Validation and Testing. Next, watch the practice video. I recommend watching it because we'll use a fresh example to reinforce the skill from this lesson.

After the practice video, complete the exercise to unlock the next lesson. If you'd like extra hands-on practice, you can also try it in the PyLearn app.

**Visual:** Hold the end card long enough to read.

## Production checklist

- [ ] Use the approved Kendrick voice with ElevenLabs v3.
- [ ] Verify every example and expected output in Python before rendering.
- [ ] Reveal code before running it; reveal output only after the run.
- [ ] Keep narration separate from production directions.
- [ ] Do not show the required app exercise solution or hidden tests.
- [ ] Watch the complete rendered video at normal speed before approval.


**Visual transition rule for this lesson:** Show each assertion as a specific gate with its expected value visible before execution. On success, reveal the pass message only after the assertion completes; on failure, pause at the failed condition and compare expected versus actual. For invalid conversion, trace the text value into the exception path and show the handled message, not a fabricated successful conversion.
