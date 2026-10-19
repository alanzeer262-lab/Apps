A program can fail in more than one way. Sometimes Python cannot understand the code. That is a syntax error. Sometimes the code starts and then crashes; that is a runtime error. And sometimes the program runs perfectly but gives the wrong answer. That last case is easy to miss, especially when working with data.

The program runs, but a correct-looking run does not prove the answer is correct. We need to check the logic and the data too.

Imagine we want the average of three scores. The program runs, but the result is wrong. Before editing anything, ask what the code assumes.

There are three scores, but the code divides by four. Python did exactly what we asked; our assumption was wrong. We can inspect the values and the number of items.

A useful debugging routine is: reproduce the problem, read the useful error line, inspect the value and its type, reduce the example, change one assumption, and run a small test again.

These checks reveal what the program actually has. They are more useful than changing random lines until the error disappears.

A function should also be tested with an empty list. There may be no records to inspect, and code that assumes the first item exists can fail.

The condition prevents us from accessing a first item when there is none. Small edge cases often reveal assumptions that normal examples hide.

Great work! You've finished Debugging: Ask Smaller Questions. Next, watch the practice video. I recommend watching it because we'll use a fresh example to reinforce the skill from this lesson.

After the practice video, complete the exercise to unlock the next lesson. If you'd like extra hands-on practice, you can also try it in the PyLearn app.
