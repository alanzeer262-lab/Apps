# PyLearn Video 09 — Dictionaries, Tuples, and Sets

**Voice lock — mandatory:** Kendrick; ElevenLabs v3; exact approved Kendrick voice ID; no substitution/preset; same voice throughout.
**Source:** `Pylearn-build260/content/python-basics/modules/09-dict-tuple-set.md`
**Target:** 7–8 minutes.

### Scene 1 — Different shapes for different questions
**Narration:** “A list is useful when order matters. But sometimes you need a learner's score by name, a fixed record, or a collection of unique topics. Python offers dictionaries, tuples, and sets. We'll choose each structure based on the question we need to answer.”
**Visual:** Show the three structures as separate small code examples, no premature results.

### Scene 2 — Dictionaries map keys to values
**Visual:** Type a learner dictionary with name Ada, score 88, goal Data Analyst. Show `learner["name"]`, `learner["score"]`, update score to 91, then add level.
**Narration:** “A dictionary connects keys to values. The key is the label, and the value is the information attached to it. Read the score using its key. You can update an existing value or add a new key. Dictionaries answer: what value belongs to this label?”

### Scene 3 — Tuples represent records
**Visual:** `record = ("Ada", 88)`, then `name, score = record`; reveal variables and output.
**Narration:** “A tuple groups related values into one record. Unpacking gives each part a meaningful name. When a record represents a name and score together, this can be clearer than keeping the fields separate.”

### Scene 4 — Sets keep unique values
**Visual:** `topics = {"python", "pandas", "python"}`; show the resulting unique values without promising order; check `"python" in topics`.
**Narration:** “A set represents unique values. Repeating Python doesn't create a second distinct member. Sets are useful when uniqueness or membership matters more than order.”

### Scene 5 — Count categories
**Visual:** `grades = ["A", "B", "A", "C", "B", "A"]`; gradually build `counts = {}` and loop using `counts[grade] = counts.get(grade, 0) + 1`.
**Narration:** “A dictionary can count how often each category appears. Get looks up the current count, using zero if the key is not present, and then we add one. The final frequency table is A: three, B: two, C: one. This turns repeated raw values into a useful summary.”

### Scene 6 — Practice and recap
**Visual:** Records for Ada, Lin, Sam, Omar; task prompts: unpack a record, map names to scores, make unique scores, count grades.
**Narration:** “Your turn. Build a dictionary from the records, create a set of unique scores, and count the grades. Add a duplicate record and observe which structures keep duplicates and which remove them.”
**Hold:** 4 seconds.
**Narration:** “Use lists for ordered collections, tuples for grouped records, dictionaries for key-value lookup, and sets for uniqueness. Next, we'll give reusable pieces of logic a name with functions.”
