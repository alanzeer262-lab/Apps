# PyLearn Video 15 — Build: Score Summary

**Voice lock — mandatory:** Kendrick; ElevenLabs v3; exact approved Kendrick voice ID; no substitution/preset; same voice throughout.
**Source:** `Pylearn-build260/content/python-basics/modules/15-build-score-summary.md`
**Target:** 6–7 minutes.

### Scene 1 — Ask useful questions
**Visual:** `scores = [70, 95, 88, 60]`.
**Narration:** “A list of scores is useful, but a summary makes it easier to understand. We'll build summarize_scores, which returns the count, average, highest score, lowest score, and how many scores meet a threshold.”

### Scene 2 — Build the summary
**Visual:** Function signature `def summarize_scores(scores, threshold=70):`; reveal count, average, max, min, passed count, and return dictionary one line at a time.
**Narration:** “The threshold defaults to seventy, but the caller can change it. Count comes from the length of the list, average is total divided by count, and max and min find the extremes. The passed field counts scores at or above the threshold.”
**Visual:** Run normal example; show returned dictionary.

### Scene 3 — Empty list and boundary
**Visual:** Show empty list check before average; return a deliberate empty result. Then test scores 69, 70, 71 against threshold 70.
**Narration:** “An empty list has no average, maximum, or minimum. Handle it deliberately instead of letting the program crash. Now test sixty-nine, seventy, and seventy-one. If seventy or higher passes, exactly seventy must count.”

### Scene 4 — Practice
**Narration:** “Your turn. Change the scores and run the summary again. Then pass a different threshold and predict how the passed count changes. Explain why a dictionary is a useful shape for the result: each summary value has a clear label.”
**Hold:** 4 seconds.
**Narration:** “You combined lists, functions, conditions, and a dictionary result into a reusable summary. Next, we'll analyze several learners rather than a single list of scores.”
