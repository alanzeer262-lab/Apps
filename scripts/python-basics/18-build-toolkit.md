# PyLearn Video 18 — Build: Reusable Analysis Toolkit

**Voice lock:** Kendrick · ElevenLabs v3 · exact user-approved Kendrick voice ID only; no preset or substitution.
**Canonical source:** app Module 18, Build 7. **Target:** 3–4 minutes. Do not supply the complete function implementations.

## Scene 1 — When code grows
**Visual:** Show a crowded block of repeated analysis steps, then separate it into two labelled jobs: average_score(scores), top_scorer(records).
**Narration:** “As a project grows, a large block of code becomes harder to understand and change. You don't need to turn every line into a function. Look for a clear job that deserves a name and might be reused.”

## Scene 2 — Two different questions
**Visual:** For `average_score(scores)`, show a list of numbers. For `top_scorer(records)`, show name-score pairs. Do not reveal function bodies.
**Narration:** “The first function answers, ‘What is the average of these scores?’ The second answers, ‘Whose score is highest?’ They have different inputs and different jobs. A good function makes that contract clear.”

## Scene 3 — Return values and empty cases
**Visual:** Show the words **input → one clear job → return value**. Then show an empty list and empty records as test cases, with no prescribed output.
**Narration:** “Each function needs a useful return value and a deliberate rule for empty input, as the project brief requires. Don't guess at edge cases. Follow the task's specified behavior and test it.”

## Scene 4 — Make the design decision
**Visual:** Ask: “Would naming this behavior make the program easier to understand or reuse?”
**Narration:** “Pause and choose one piece of logic from a project that could be useful somewhere else. Would giving it a function name make the program clearer?”
**Hold:** 5 seconds of silence.

## Scene 5 — Build in PyLearn
**Visual:** App/project card: **Build 7 — Reusable analysis toolkit**. Two empty function stubs labelled with their required signatures.
**Narration:** “Open Build 7 in PyLearn and implement average_score and top_scorer yourself. Test normal input and the required empty cases. The goal is not to create the most functions; it is to give reusable behavior a clear name.”

## Final call to action — required for YouTube and in-app versions

**Visual:** Show the PyLearn app's Practice section and the matching project card: **Build 7 — Toolkit**. Do not show the completed solution.

**Narration:**

Now it's your turn to build it yourself.

Open the PyLearn app and go to the Practice section for this project. If you're watching on YouTube, open PyLearn and find Build 7 — Toolkit in the app.

Write the code yourself, run it, and use the app's feedback to check your work. Try the required cases before moving on. Mistakes are part of learning, so read the feedback and try again.

Watching the example is only the first step. Now open PyLearn and build it yourself!

**End card:** “Open PyLearn → Practice → Build 7 — Toolkit”

## Production checklist

- [ ] The video demonstrates the problem and reasoning without giving away the complete app solution.
- [ ] The final card explicitly points to Practice in PyLearn.
- [ ] YouTube viewers are told to open PyLearn and find the matching project.
- [ ] Review the full rendered video at normal speed before marking it complete.
