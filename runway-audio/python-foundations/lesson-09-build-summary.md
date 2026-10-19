A pile of records is not yet an answer. A useful summary tells us how many valid scores we have, what their average is, and who has the highest score. The summary function should receive validated records, not raw C S V text.

Each statistic answers a different question. The count describes the size of the group, the average describes its central value, and the top score identifies its highest value.

What happens when there are no valid scores? There is no average and no top scorer. Dividing by zero or calling max on an empty list raises an error, so the function must handle the empty case explicitly.

A clear empty result is better than a crash. It tells the person reading the report why no statistic was produced.

Returning a dictionary gives the rest of the program a structured result to format or save. The summary function calculates; the report layer decides how to present it.

You've learned to summarize validated data and protect the empty case. Next, watch the practice video, then complete the exercise to unlock the next lesson. You can also practise in the PyLearn app for extra hands-on work.
