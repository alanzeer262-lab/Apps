A program that works once is not automatically trustworthy. Testing means checking behavior against results we already know. A test should be small, specific, repeatable, and tied to something important.

An assert stops the program if its condition is false. If execution reaches the print, the assertion succeeded.

A normal example is useful, but boundaries and empty input often expose bugs. We should check each behavior we care about.

These tests check an empty list, a single value, and a wide range. The expected answers are known before we run them.

Testing should include invalid values too. Suppose a score arrives as text and contains a word instead of digits. The program should report that row as invalid, not crash halfway through the report.

This example demonstrates the conversion failure safely. The full toolkit should keep validation rules explicit and test the error case.

When a test fails, compare the expected result with the actual result before changing code. Try normal input, boundary input, empty input, and invalid input. A few focused tests can provide more confidence than one huge example.

Testing is not only about finding mistakes. It makes the behavior of your program clear and repeatable.

Great work! You've finished Validation and Testing. Next, watch the practice video. I recommend watching it because we'll use a fresh example to reinforce the skill from this lesson.

After the practice video, complete the exercise to unlock the next lesson. If you'd like extra hands-on practice, you can also try it in the PyLearn app.
