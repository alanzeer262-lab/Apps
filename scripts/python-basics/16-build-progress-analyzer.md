# PyLearn Video 16 — Build: Multi-Record Progress Analyzer

**Voice lock — mandatory:** Kendrick; ElevenLabs v3; exact approved Kendrick voice ID; no substitution/preset; same voice throughout.
**Source:** `Pylearn-build260/content/python-basics/modules/16-build-progress-analyzer.md`
**Target:** 6–8 minutes.

### Scene 1 — Move from one list to many records
**Visual:** Show records Ada 88, Lin 72, Sam 95, Omar 64 as tuples.
**Narration:** “A score summary handles one list. Now we have multiple learners, each represented by a name and score. We'll build analyze_records to produce one summary across the records.”

### Scene 2 — Read records clearly
**Visual:** Type the function signature with threshold 70; loop `for name, score in records:`; initialize totals and lists.
**Narration:** “Each tuple contains two related fields. Unpacking gives us name and score directly. We'll loop over each record, updating the total, tracking the highest scorer, and placing each learner in the passed or needs-support list.”

### Scene 3 — Return a summary
**Visual:** Show count, average, top_scorer, passed, needs_support. Preserve input order in the lists.
**Narration:** “The result includes the number of records, average score, top scorer, learners who passed, and learners who need support. We preserve the original order in the learner lists so the report stays predictable.”
**Visual:** Run records; verify average 79.75 and top scorer Sam with 95; passed Ada, Lin, Sam; needs support Omar.

### Scene 4 — Empty records
**Visual:** Run with empty records and show the deliberate empty result.
**Narration:** “Now consider no records at all. There is no average and no top scorer. The function should return the empty-case result we chose rather than dividing by zero or inventing a learner.”

### Scene 5 — Practice and recap
**Narration:** “Add one record and predict how the count, average, and learner groups change. Why is a tuple like name and score easier to process than two unrelated lists?”
**Hold:** 4 seconds.
**Narration:** “The pattern is records, loop, rule, summary. Later, pandas can perform similar operations on tables, but the reasoning remains familiar. Next, we'll count grade categories.”
