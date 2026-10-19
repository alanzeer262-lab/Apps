# PyLearn Video 15 — Build: Score Summary

**Voice lock:** Kendrick · ElevenLabs v3 · exact user-approved Kendrick voice ID only; no preset or substitution.
**Canonical source:** app Module 15, Build 4. **Target:** 3–4 minutes. Demonstrate concepts without giving the complete solution.

## Scene 1 — The mission
**Visual:** Show `scores = [70, 95, 88, 60]`. Display five output labels: count, average, highest, lowest, passed.
**Narration:** “A list of scores holds the data, but a summary helps us understand it. Your task is to build summarize_scores with a threshold that defaults to seventy. It must return a dictionary containing the count, average, highest score, lowest score, and number of scores that pass.”

## Scene 2 — Match each question to an operation
**Visual:** Reveal a simple concept map: count → length; extremes → highest/lowest; passed → compare each score with threshold. Leave average calculation as a question.
**Narration:** “Each field answers a different question. Count tells us how many scores we have. Highest and lowest describe the extremes. Passed counts scores at or above the threshold. The average summarizes the values together. A dictionary gives each result a clear label.”

## Scene 3 — Test the boundary
**Visual:** Three cards: 69, 70, 71; threshold 70. Initially hide the pass/fail marks.
**Narration:** “The rule says seventy or higher passes. Predict which of these three scores should count before revealing the result.”
**Hold:** 5 seconds of silence. Reveal: 69 does not pass; 70 and 71 pass.

## Scene 4 — Empty input matters
**Visual:** Show an empty list and the note: “Return a deliberate empty result; do not crash.” Do not prescribe an exact dictionary unless the app brief does.
**Narration:** “The project also requires a deliberate empty result for an empty list. An empty list has no average, highest, or lowest value. Follow the behavior specified in the app task rather than guessing.”

## Scene 5 — Build in PyLearn
**Visual:** App/project card: **Build 4 — Score summary**. Test checklist: normal list, empty list, 69/70/71, changed threshold.
**Narration:** “Open Build 4 in PyLearn and implement summarize_scores yourself. Test the normal list, the empty list, and the threshold boundary. Then change the threshold and predict how the passed count changes.”

## Final call to action — required for YouTube and in-app versions

**Visual:** Show the PyLearn app's Practice section and the matching project card: **Build 4 — Score summary**. Do not show the completed solution.

**Narration:**

Now it's your turn to build it yourself.

Open the PyLearn app and go to the Practice section for this project. If you're watching on YouTube, open PyLearn and find Build 4 — Score summary in the app.

Write the code yourself, run it, and use the app's feedback to check your work. Try the required cases before moving on. Mistakes are part of learning, so read the feedback and try again.

Watching the example is only the first step. Now open PyLearn and build it yourself!

**End card:** “Open PyLearn → Practice → Build 4 — Score summary”

## Production checklist

- [ ] The video demonstrates the problem and reasoning without giving away the complete app solution.
- [ ] The final card explicitly points to Practice in PyLearn.
- [ ] YouTube viewers are told to open PyLearn and find the matching project.
- [ ] Review the full rendered video at normal speed before marking it complete.
