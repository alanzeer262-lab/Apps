A short program can live in one file. As it grows, loading data, validating it, calculating results, and formatting reports can become tangled. A module is simply a Python file that contains reusable code.

Pause and identify the function's input, its return value, and why defining it does not print anything by itself.

Another Python file can import the function by its module name. The module name comes from the file name, without the .py ending.

The second file does not need to copy the average calculation. It uses the same function. That makes fixes and tests easier to manage.

For a data toolkit, one module can load files, another can validate records, another can calculate summaries, and another can write reports. The goal is not to create as many files as possible. The goal is to make each responsibility easy to find.

This function answers one question: how many scores meet the threshold? A small, focused function is easier to test than a single giant program.

When a function takes a list and returns a result, that boundary can be tested without reading a file. When file loading has its own function, we can test it separately too.

Separating responsibilities helps us locate a bug. If the scores are wrong, inspect loading or validation. If the count is wrong for a known list, inspect the calculation.

Great work! You've finished Organize a Growing Program. Next, watch the practice video. I recommend watching it because we'll use a fresh example to reinforce the skill from this lesson.

After the practice video, complete the exercise to unlock the next lesson. If you'd like extra hands-on practice, you can also try it in the PyLearn app.
