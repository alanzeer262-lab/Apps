# PyLearn Video 14 — Build: Clean My Learning Topics

**Voice lock:** Kendrick · ElevenLabs v3 · exact user-approved Kendrick voice ID only; no preset or substitution.
**Canonical source:** app Module 14, Build 3. **Target:** 3–4 minutes. Do not reveal a complete function or decide duplicate policy beyond the source brief.

## Scene 1 — The mission
**Visual:** Show the exact raw input: `" python, pandas, pandas, machine learning "`. Highlight extra spaces and inconsistent capitalization.
**Narration:** “Text people type is not always consistent. Our example has extra spaces, and the capitalization isn't standardized. Your task is to build clean_topics so the topic names are easier to use consistently.”

## Scene 2 — Split is not clean
**Visual:** Animate the string splitting at commas into separate pieces. Keep the spaces visible around each piece.
**Narration:** “First, split the text at commas. Now each topic is a separate piece. But splitting does not remove the spaces around each piece, so the data still needs cleaning.”

## Scene 3 — The cleaning sequence
**Visual:** Show three separate labels, in order: **split on commas → strip surrounding whitespace → normalize capitalization**. Then show an empty piece caused by an extra comma, crossed out.
**Narration:** “Follow the project rules in order: split on commas, remove surrounding whitespace, normalize capitalization, and ignore empty pieces. These steps make the output consistent. The project also asks you to search the cleaned topics without case affecting the search.”

## Scene 4 — Predict and test
**Visual:** Show the search question: “Should searching for PYTHON find the cleaned topic Python?” Do not show code.
**Narration:** “Pause and predict whether a search for PYTHON should find the topic after normalization. Then consider why Python and python could otherwise become separate categories.”
**Hold:** 5 seconds of silence. Reveal: “The search should not depend on capitalization.”

## Scene 5 — Build in PyLearn
**Visual:** App/project card: **Build 3 — Clean my learning topics**. Checklist mirrors the four source rules; no completed function.
**Narration:** “Open Build 3 in PyLearn and implement clean_topics yourself. Test the supplied input, then try different capitalization and an empty piece. Use the app's feedback, and explain why normalization matters before data analysis.”

## Final call to action — required for YouTube and in-app versions

**Visual:** Show the PyLearn app's Practice section and the matching project card: **Build 3 — Clean my learning topics**. Do not show the completed solution.

**Narration:**

Now it's your turn to build it yourself.

Open the PyLearn app and go to the Practice section for this project. If you're watching on YouTube, open PyLearn and find Build 3 — Clean my learning topics in the app.

Write the code yourself, run it, and use the app's feedback to check your work. Try the required cases before moving on. Mistakes are part of learning, so read the feedback and try again.

Watching the example is only the first step. Now open PyLearn and build it yourself!

**End card:** “Open PyLearn → Practice → Build 3 — Clean my learning topics”

## Production checklist

- [ ] The video demonstrates the problem and reasoning without giving away the complete app solution.
- [ ] The final card explicitly points to Practice in PyLearn.
- [ ] YouTube viewers are told to open PyLearn and find the matching project.
- [ ] Review the full rendered video at normal speed before marking it complete.
