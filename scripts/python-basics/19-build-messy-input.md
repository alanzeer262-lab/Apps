# PyLearn Video 19 — Build: Handle Imperfect Scores

**Voice lock — mandatory:** Kendrick; ElevenLabs v3; exact approved Kendrick voice ID; no substitution/preset; same voice throughout.
**Source:** `Pylearn-build260/content/python-basics/modules/19-build-messy-input.md`
**Target:** 6–8 minutes.

### Scene 1 — Real input is imperfect
**Visual:** Show records Ada "88", Lin "72", Sam "oops", Mia empty string.
**Narration:** “Real data isn't always clean. Some scores arrive as text, one is not a number, and one is empty. We need to separate usable records from invalid ones without letting one bad value crash the whole program.”

### Scene 2 — Define the output
**Visual:** Show two empty collections labelled valid_records and invalid_records.
**Narration:** “Our function clean_score_records returns two groups. Valid records keep the learner's name and convert the score to a number. Invalid records keep the name and a reason, such as invalid score or empty score. Keeping the reason makes the cleanup explainable.”

### Scene 3 — Convert safely
**Visual:** Build loop; distinguish empty string from conversion failure; use try/except ValueError; append valid numeric tuples or invalid records with reason.
**Narration:** “For each record, first check whether the score is empty. Otherwise, attempt integer conversion. If conversion succeeds, keep the numeric record. If it raises ValueError, record the failure instead of crashing. Don't silently turn bad input into zero.”
**Visual:** Run; show valid Ada 88 and Lin 72; invalid Sam with invalid score and Mia with empty score.

### Scene 4 — Analyze only valid data
**Visual:** Show valid scores going to analysis; invalid records displayed separately. Show note that invalid values are excluded from average.
**Narration:** “The valid records can now be analyzed. Invalid records stay visible so someone can correct them. Replacing an invalid score with zero would change the average and could create a misleading conclusion. Excluding invalid values is a deliberate data-quality decision, not a rule built into Python.”

### Scene 5 — Practice and recap
**Narration:** “Add one more record: a valid numeric string, an invalid word, or an empty score. Predict which output group it belongs in, then run the function.”
**Hold:** 4 seconds.
**Narration:** “The pipeline is raw records, validation, valid and invalid groups, then analysis. You now have the foundations to combine Python features into the Mini Gradebook capstone.”
