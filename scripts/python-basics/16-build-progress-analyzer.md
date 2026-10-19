# PyLearn Video 16 — Build: Multi-Record Progress Analyzer

**Voice lock:** Kendrick · ElevenLabs v3 · exact user-approved Kendrick voice ID only; no preset or substitution.
**Canonical source:** app Module 16, Build 5. **Target:** 3–4 minutes. Do not reveal the completed analyzer.

## Scene 1 — Several learners, one report
**Visual:** Show the four source records, one at a time: `("Ada", 88)`, `("Lin", 72)`, `("Sam", 95)`, `("Omar", 64)`. Then show the requested function name `analyze_records(records, threshold=70)`.
**Narration:** “A score summary works on one list of numbers. Now we have several learner records, each containing a name and a score. Your task is to analyze all the records together and return one summary.”

## Scene 2 — Read each record
**Visual:** Highlight the name and score positions in one tuple. Show the pattern `for name, score in records:` only; do not reveal the function body.
**Narration:** “Each tuple groups two related values. Tuple unpacking lets the loop work with the name and score directly. As you visit each record, you can update totals, compare scores, and decide which group the learner belongs to.”

## Scene 3 — Know the contract
**Visual:** Display only the required output keys: count, average, top_scorer, passed, needs_support. Add note: “Keep learner lists in original input order.”
**Narration:** “Your result must contain five things: count, average, top scorer, the learners who passed, and the learners who need support. Keep the learner lists in the same order as the input. The project also requires a deliberate empty-records case.”

## Scene 4 — Predict
**Visual:** Highlight Omar's score of 64 with threshold 70. Keep the full result hidden.
**Narration:** “With a threshold of seventy, where should Omar appear: in passed or needs support? And if you add one more record, which summary values might change?”
**Hold:** 5 seconds of silence. Reveal only Omar's classification, not the complete report.

## Scene 5 — Build in PyLearn
**Visual:** App/project card: **Build 5 — Multi-record progress analyzer**. Checklist: loop through tuples; calculate summary; preserve order; test empty records.
**Narration:** “Open Build 5 in PyLearn and build analyze_records yourself. Test the supplied records, then add a learner and check the changes. Finally, explain why a tuple containing a name and score is easier to process than two unrelated lists.”

## Final call to action — required for YouTube and in-app versions

**Visual:** Show the PyLearn app's Practice section and the matching project card: **Build 5 — Progress analyzer**. Do not show the completed solution.

**Narration:**

Now it's your turn to build it yourself.

Open the PyLearn app and go to the Practice section for this project. If you're watching on YouTube, open PyLearn and find Build 5 — Progress analyzer in the app.

Write the code yourself, run it, and use the app's feedback to check your work. Try the required cases before moving on. Mistakes are part of learning, so read the feedback and try again.

Watching the example is only the first step. Now open PyLearn and build it yourself!

**End card:** “Open PyLearn → Practice → Build 5 — Progress analyzer”

## Production checklist

- [ ] The video demonstrates the problem and reasoning without giving away the complete app solution.
- [ ] The final card explicitly points to Practice in PyLearn.
- [ ] YouTube viewers are told to open PyLearn and find the matching project.
- [ ] Review the full rendered video at normal speed before marking it complete.
