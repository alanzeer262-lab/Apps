# PyLearn Guided Practice — 04 — Validation and Testing

**Voice lock — mandatory:** Use the user-approved Kendrick voice with ElevenLabs v3; do not substitute another voice.
**Canonical source:** Pylearn-build260/content/python-foundations/modules/04-validation-testing.md, branch ccr-c7f6fdd7-xpzi3g.
**Target runtime:** Approximately 3–5 minutes.
**Purpose:** Separate guided-practice companion with fresh examples. Never reveal the required app exercise solution.

## Scene 1 — One successful run is not proof

**Visual:** Use a fresh example and the same uncluttered code-first visual style as the lesson.

**Narration:**

A program that works once is not automatically trustworthy. Testing means checking behavior against results we already know. A test should be small, specific, repeatable, and tied to something important.

**Code**
    
    def average_score(scores):
            if not scores:
                return 0.0
            return sum(scores) / len(scores)
    
        assert average_score([10, 20]) == 15
        print("Average test passed")

**Expected output**
    
    Average test passed

**Narration:**

Predict the result before running the example. Compare the output with your prediction and explain the result in your own words. If it differs, inspect the input and change one thing at a time.

## Scene 2 — Test more than the happy path

**Visual:** Use a fresh example and the same uncluttered code-first visual style as the lesson.

**Narration:**

A normal example is useful, but boundaries and empty input often expose bugs. We should check each behavior we care about.

**Code**
    
    assert average_score([]) == 0.0
        assert average_score([7]) == 7
        assert average_score([0, 100]) == 50
        print("Boundary tests passed")

**Expected output**
    
    Boundary tests passed

**Narration:**

Predict the result before running the example. Compare the output with your prediction and explain the result in your own words. If it differs, inspect the input and change one thing at a time.

## Scene 3 — Invalid input needs a rule

**Visual:** Use a fresh example and the same uncluttered code-first visual style as the lesson.

**Narration:**

Testing should include invalid values too. Suppose a score arrives as text and contains a word instead of digits. The program should report that row as invalid, not crash halfway through the report.

**Code**
    
    raw_score = "oops"
        try:
            score = int(raw_score)
        except ValueError:
            print("Invalid score")

**Expected output**
    
    Invalid score

**Narration:**

Predict the result before running the example. Compare the output with your prediction and explain the result in your own words. If it differs, inspect the input and change one thing at a time.

## Scene 4 — Read both sides of a failure

**Visual:** Use a fresh example and the same uncluttered code-first visual style as the lesson.

**Narration:**

When a test fails, compare the expected result with the actual result before changing code. Try normal input, boundary input, empty input, and invalid input. A few focused tests can provide more confidence than one huge example.

**Code**
    
    expected = 15
        actual = average_score([10, 20])
        print("Expected:", expected)
        print("Actual:", actual)
        assert actual == expected

**Expected output**
    
    Expected: 15
        Actual: 15

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
