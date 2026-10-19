Let's connect the stages using a small example that we can run from beginning to end. This is a teaching example, not the required PyLearn exercise solution. We have three records: Ada has eighty-eight, Lin has seventy-two, and Mo has a score written as the word oops.

The loader reads all three rows. Validation converts numeric scores and keeps the invalid record separate. The summary calculates only from the valid records.

The run function connects the stages. It does not hard-code the report. It passes the input through loading, validation, and summarizing, then combines the measured counts with the calculated summary.

Every number here has a traceable source. Three rows entered the loader. Two scores passed validation. One row was rejected because its score was not numeric. The average is eighty, calculated from eighty-eight and seventy-two, and Ada is the top performer in this example.

The larger capstone uses more fields and additional cleaning decisions, so its report must be generated from the actual capstone data and the rules you implement. Never copy these demonstration numbers into that report.

You've connected the loading, validation, and summary stages into one pipeline concept. Next, watch the practice video, then complete the exercise to unlock the next lesson. Extra practice in the PyLearn app is optional.
