# PyLearn Video 17 — Build: Grade Distribution

**Voice lock:** Kendrick · ElevenLabs v3 · exact user-approved Kendrick voice ID only; no preset or substitution.
**Canonical source:** app Module 17, Build 6. **Target:** 3–4 minutes. Teach classification and counting; leave implementation to the app.

## Scene 1 — From scores to categories
**Visual:** Show the exact grade bands: 90+ A; 80–89 B; 70–79 C; 60–69 D; below 60 F.
**Narration:** “A score is a number. A grade turns that number into a category. This project asks you to build one function that converts scores to grades and another that counts the grades.”

## Scene 2 — Why rule order matters
**Visual:** Highlight the highest band first, then move downward. Show one score, 88, and ask which band contains it. Do not reveal code.
**Narration:** “When you write the conditions, check the highest threshold first and then move downward. For example, eighty-eight belongs in the B band. Boundary tests are important because one incorrect comparison can put a score in the wrong category.”

## Scene 3 — Counting a frequency table
**Visual:** Show scores `[95, 88, 88, 72, 55]`. Animate each as a letter, then show the source-defined counts: A: 1, B: 2, C: 1, F: 1. No D entry because no score maps to D.
**Narration:** “After assigning categories, count how often each letter appears. In this sample there is one A, two Bs, one C, and one F. No score maps to D, so D does not appear in this simple frequency dictionary.”

## Scene 4 — Predict at the boundaries
**Visual:** Display pairs: 59/60, 69/70, 79/80, 89/90. Keep resulting grades hidden.
**Narration:** “Pause and predict the grade for each value in these boundary pairs. Which pairs cross into a new category?”
**Hold:** 5 seconds of silence. Reveal the correct grade bands, not the implementation.

## Scene 5 — Build in PyLearn
**Visual:** App/project card: **Build 6 — Grade distribution**. Checklist: score-to-grade function; grade-count function; boundary tests.
**Narration:** “Open Build 6 in PyLearn and implement both functions yourself. Test the sample scores and each boundary. Then reflect: why is a count such as ‘B: 3’ more useful for analysis than storing three separate B values?”

## Final call to action — required for YouTube and in-app versions

**Visual:** Show the PyLearn app's Practice section and the matching project card: **Build 6 — Grade distribution**. Do not show the completed solution.

**Narration:**

Now it's your turn to build it yourself.

Open the PyLearn app and go to the Practice section for this project. If you're watching on YouTube, open PyLearn and find Build 6 — Grade distribution in the app.

Write the code yourself, run it, and use the app's feedback to check your work. Try the required cases before moving on. Mistakes are part of learning, so read the feedback and try again.

Watching the example is only the first step. Now open PyLearn and build it yourself!

**End card:** “Open PyLearn → Practice → Build 6 — Grade distribution”

## Production checklist

- [ ] The video demonstrates the problem and reasoning without giving away the complete app solution.
- [ ] The final card explicitly points to Practice in PyLearn.
- [ ] YouTube viewers are told to open PyLearn and find the matching project.
- [ ] Review the full rendered video at normal speed before marking it complete.
