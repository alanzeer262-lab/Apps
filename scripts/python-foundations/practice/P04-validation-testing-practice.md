# PyLearn Guided Practice — Testing Practice

**Voice lock:** Use the approved Kendrick voice with ElevenLabs v3; do not substitute another voice.
**Canonical source:** Pylearn-build260/content/python-foundations/modules/04-validation-testing.md, branch ccr-c7f6fdd7-xpzi3g.
**Purpose:** Separate practice companion using fresh examples. Never reveal the required app exercise solution.
**Track 2 practice visuals:** Use a test bench with a compact test matrix, boundary number line, and passed/rejected markers. Pause before each assertion result so the learner can predict it. Use teal for passing checks, coral for failures, and amber for edge cases; avoid a repetitive input/output-box layout.

## Scene 1 — Write a known test

**Narration:** A good test starts with a result you can calculate yourself. The average of six and ten is eight.

**Code**

    def average(values):
        if not values:
            return 0.0
        return sum(values) / len(values)

    assert average([6, 10]) == 8
    print("Test passed")

**Expected output**

    Test passed

If the result changes unexpectedly, the assertion fails where the behavior is checked.

## Scene 2 — Add edge cases

**Code**

    assert average([]) == 0.0
    assert average([9]) == 9
    print("Edge cases passed")

**Expected output**

    Edge cases passed

**Narration:** Don't stop after one normal example. Test empty input, a single value, boundary values, and invalid input where appropriate.

## Close — Complete the exercise

**Visual:** Keep the `average` function from Scene 1 in the same editor session. Add the two assertions below it and reveal “Edge cases passed” only after both checks succeed.

**Narration:** Good work. Now complete the exercise to unlock the next lesson. Use the habits from this practice: test small cases, check assumptions, and change one thing at a time. If you'd like extra hands-on practice, you can also try it in the PyLearn app.

## Production checklist
- [ ] Use approved Kendrick / ElevenLabs v3 voice.
- [ ] Verify all code and outputs in Python.
- [ ] Keep examples distinct from the required app exercise.
- [ ] Keep code and output synchronized with narration.
- [ ] Watch the full render before approval.


**Visual transition rule for this practice:** Show the expected value before each assertion runs, then reveal the pass marker only after the assertion succeeds. Keep the same `average` function active between scenes; never display a pass result before execution.
