# PyLearn Video 19 — Build: Handle Imperfect Scores

**Voice lock:** Kendrick · ElevenLabs v3 · exact user-approved Kendrick voice ID only; no preset or substitution.
**Canonical source:** app Module 19, Build 8. **Target:** 3–4 minutes. Explain the data-quality problem, but leave the implementation to the learner.

## Scene 1 — Real input is imperfect
**Visual:** Show the exact records: `("Ada", "88")`, `("Lin", "72")`, `("Sam", "oops")`, `("Mia", "")`. Highlight numeric text, invalid text, and empty text separately.
**Narration:** “Real data is not always ready to analyze. Some scores arrive as strings, one is not a valid number, and one is empty. Your task is to clean these records without letting bad input crash the program.”

## Scene 2 — Define the result
**Visual:** Show two empty containers: valid_records and invalid_records. Add note: valid records become numeric tuples; invalid records keep the name and a reason.
**Narration:** “Build clean_score_records with two outputs: valid records and invalid records. Convert usable scores to numbers. For invalid records, keep the learner's name and a reason, such as invalid score or empty score.”

## Scene 3 — Safe conversion
**Visual:** Show the decision sequence only: check empty input → attempt numeric conversion → keep valid record or record the failure. Do not reveal full code.
**Narration:** “Check for an empty score, then attempt conversion safely. If conversion fails, record the problem rather than crashing. Don't silently change invalid input to zero. That would make the data look valid when it isn't.”

## Scene 4 — What should happen to invalid scores?
**Visual:** Show the pipeline: raw records → validate → valid + invalid → analyze valid records. Highlight that invalid scores are excluded from the average.
**Narration:** “The project specifies that invalid scores are excluded from the average rather than changed to zero. Keep invalid records visible so they can be corrected. This is a data-quality decision, not a built-in Python rule.”

## Scene 5 — Predict, then practice
**Visual:** Ask where each new record belongs: `("Noor", "91")`, `("Rami", "oops")`, `("Maya", "")`. Keep answers hidden during the pause.
**Narration:** “Pause and classify each example: valid or invalid, and why?”
**Hold:** 5 seconds of silence. Reveal classification only after the hold.

**Visual:** App/project card: **Build 8 — Handle imperfect scores**.
**Narration:** “Now open Build 8 in PyLearn and implement clean_score_records yourself. Use the app's feedback to test valid input, invalid text, and an empty score. You're ready to combine these skills in the Mini Gradebook capstone.”

**End card:** “Open PyLearn → Build 8: Handle imperfect scores”
