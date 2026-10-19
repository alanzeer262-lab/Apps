# PyLearn Video 14 — Build: Clean My Learning Topics

**Voice lock — mandatory:** Kendrick; ElevenLabs v3; exact approved Kendrick voice ID; no substitution/preset; same voice throughout.
**Source:** `Pylearn-build260/content/python-basics/modules/14-build-topic-cleaner.md`
**Target:** 5–7 minutes.

### Scene 1 — Messy input
**Visual:** Show exact input `" python, pandas, pandas, machine learning "`.
**Narration:** “Text from real people is rarely perfectly consistent. This input has extra spaces, mixed capitalization, and a repeated topic. We'll build clean_topics so the rest of our program can work with normalized values.”

### Scene 2 — Split the input
**Visual:** Function `clean_topics(raw_text)`; reveal `parts = raw_text.split(",")`. Show list with whitespace preserved.
**Narration:** “First, split the string at each comma. Now each topic is a separate piece, but some pieces still have spaces around them. Splitting separates the data; it does not automatically clean each piece.”

### Scene 3 — Clean each piece
**Visual:** Walk through each part, applying strip and title normalization; show empty pieces being ignored. Avoid revealing later code before narration.
**Narration:** “For every piece, remove surrounding whitespace and normalize its capitalization. Ignore empty pieces so an extra comma doesn't create an empty topic. The output should be consistent even when the input has extra spaces.”
**Visual:** Show final cleaned topics and case-insensitive search.

### Scene 4 — Verify the behavior
**Visual:** Run original input; then a second input with different capitalization and an extra comma.
**Narration:** “Test the original text, then change capitalization and add an empty piece. Check that the result still follows the rules. Normalization matters because Python and python can otherwise be treated as different strings.”

### Scene 5 — Practice and recap
**Narration:** “Pause and try a new list of topics. Decide how to handle duplicates, then test whether Python is present without being affected by capitalization.”
**Hold:** 4 seconds.
**Narration:** “You split text, cleaned each piece, ignored empty entries, and normalized categories. This is a small example of preparing raw data before analyzing it. Next, we'll summarize a list of scores.”
