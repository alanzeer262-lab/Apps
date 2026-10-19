A score of one hundred and fifty or minus one can quietly distort every number in a report. Validation checks whether a record meets the rules before it is included in calculations. We keep validation separate from loading so each stage has one testable job.

This demonstration uses a range from zero to one hundred. In your toolkit, keep track of rejected rows and the reason each one failed.

C S V values arrive as text. A word like oops or an empty string cannot be converted to an integer. Catch that failure and report it instead of crashing the whole pipeline.

There are two failure reasons here. Keeping them distinct makes the final report more useful.

Test the edge of the allowed range: zero and one hundred should pass, while values just outside the range should fail.

A validation function makes these decisions predictable. The summary should receive validated records, not invent its own rules.

You've learned why validation is a separate gate, how conversion errors happen, and why boundary tests matter. Next, watch the practice video, then complete the exercise to unlock the next lesson. You can also practise in the PyLearn app if you want extra hands-on work.
