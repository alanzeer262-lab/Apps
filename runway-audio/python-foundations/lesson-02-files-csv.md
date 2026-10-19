Until now, many examples have kept data inside the code. A file lets a program read information saved outside the program. C S V stands for comma-separated values. Think of it as a simple table stored as text.

Pause and identify the header fields and the values in each row before loading the file.

Python includes a csv module. DictReader uses the header names as keys, so each row behaves like a dictionary. The with statement ensures the file is closed when the block finishes.

There is an important detail: values read from C S V arrive as text. The score looks like a number, but the reader gives us the string 88. Convert it deliberately before doing arithmetic.

A normal row can be converted to an integer, but real files can contain blanks or unexpected text. A robust program decides how to handle conversion failures instead of assuming every value is valid.

This example uses a clean value. Later, the pipeline will separate loading from validation so invalid rows can be handled deliberately.

Reading data is only half the story. Python can also write a result to a file. Opening a file with write mode creates it or replaces its previous contents, so use that mode intentionally.

The message confirms the program reached the end. The report itself is stored in the file. In the full toolkit, raw rows, cleaned records, and report writing will remain separate steps.

Great work! You've finished Files and C S V Records. Next, watch the practice video. I recommend watching it because we'll use a fresh example to reinforce the skill from this lesson.

After the practice video, complete the exercise to unlock the next lesson. If you'd like extra hands-on practice, you can also try it in the PyLearn app.
