# PyLearn Video 05 — Booleans and Comparisons

**Voice lock — mandatory:** Kendrick voice; ElevenLabs v3; exact approved Kendrick voice ID; no substitution or preset; same voice throughout.
**Source:** `Pylearn-build260/content/python-basics/modules/05-booleans.md`
**Target:** 6–7 minutes.

### Scene 1 — Programs ask questions
**Visual:** Show `print(10 > 5)` then `print(10 < 5)`; reveal True and False only after run.
**Narration:** “Programs often need to answer questions: did the learner pass, is the score high enough, or should we continue? Python represents yes-or-no answers with Boolean values: True and False. A comparison produces one of those two values.”

### Scene 2 — The comparison operators
**Visual:** Show separate rows: `10 == 10`, `10 != 5`, `10 > 5`, `10 < 5`, `10 >= 10`, `5 <= 10`.
**Narration:** “Double equals asks whether two values are equal. Exclamation equals means not equal. Greater than and less than compare size. Greater than or equal and less than or equal include the boundary.”
**Visual:** `score = 70` then `score == 70`.
**Narration:** “Be careful: one equals sign assigns a value. Two equals signs compare values. Assignment changes what a variable refers to; comparison asks a question.”

### Scene 3 — Test the boundary
**Visual:** Show `score >= 70` with score values 69, 70, and 71; update one value at a time and show result.
**Narration:** “Suppose passing means at least seventy. Then the condition is score greater than or equal to seventy. Test sixty-nine, seventy, and seventy-one. The exact boundary matters. Whenever a rule changes at a threshold, test just below, exactly at, and just above it.”

### Scene 4 — Combine conditions
**Visual:** Reveal `score >= 70 and attendance >= 80`, then separate examples with `or` and `not`.
**Narration:** “Use and when every condition must be true. Use or when at least one condition can be true. Use not to reverse a Boolean. Read a condition as an English sentence. If the sentence is confusing, simplify the condition or give a piece of it a clear variable name.”

### Scene 5 — Learner practice
**Visual:** `score = 82`, `attendance = 90`, `is_beginner = True`. Prompt for booleans: score at least 70, attendance at least 80, both requirements met, beginner, not beginner.
**Narration:** “Your turn. Create these three variables and calculate the five Boolean results. Before running, predict each answer. Then change the score to sixty-nine and check what changes.”
**Hold:** 4 seconds; reveal only after the prediction pause.

### Recap
**Narration:** “Booleans are True or False. Comparisons produce them, and and, or, and not combine them. Remember the difference between assignment and comparison, and test threshold boundaries deliberately. Next, we'll store collections of values in lists.”

## App practice handoff

**Visual:** End card showing the corresponding PyLearn lesson/exercise; do not show a completed solution.

**Narration:** "Open Lesson 5 in PyLearn and complete the Boolean practice in the app. Predict the results first, then change the score to 69 and check the boundary behavior."
