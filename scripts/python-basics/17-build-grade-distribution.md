# PyLearn Video 17 — Build: Grade Distribution

**Voice lock — mandatory:** Kendrick; ElevenLabs v3; exact approved Kendrick voice ID; no substitution/preset; same voice throughout.
**Source:** `Pylearn-build260/content/python-basics/modules/17-build-grade-distribution.md`
**Target:** 5–7 minutes.

### Scene 1 — Scores become categories
**Visual:** Show score rules: 90+ A, 80–89 B, 70–79 C, 60–69 D, below 60 F.
**Narration:** “A score is numeric, but sometimes we want to understand the distribution of grades. We'll translate each score into a category, then count how many times each category appears. The order of the rules matters.”

### Scene 2 — Convert one score
**Visual:** Build a grade_for(score) function with if/elif/else; test 95, 88, 72, 64, 55 one by one.
**Narration:** “Check the highest threshold first, then move downward. A score of ninety-five becomes A, eighty-eight becomes B, seventy-two becomes C, sixty-four becomes D, and fifty-five becomes F. Test the boundaries when you implement these rules.”

### Scene 3 — Count the categories
**Visual:** `scores = [95, 88, 88, 72, 55]`; convert to grades; build counts with dictionary get pattern. Reveal distribution A:1, B:2, C:1, F:1.
**Narration:** “Now we count the categories. Each time a grade appears, increase its count by one. The frequency table says one A, two Bs, one C, and one F. No D appears, so it has no entry in this simple count.”

### Scene 4 — Practice
**Narration:** “Change one score and predict which grade count changes. Then test a score exactly on each boundary: fifty-nine and sixty, sixty-nine and seventy, seventy-nine and eighty, eighty-nine and ninety.”
**Hold:** 4 seconds.
**Narration:** “A frequency table is more useful for analysis than keeping a separate repeated letter for every learner. Next, we'll organize our growing project into reusable functions.”
