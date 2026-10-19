# PyLearn Video 07 — Conditionals: if, elif, else

**Voice lock — mandatory:** Kendrick; ElevenLabs v3; exact approved Kendrick voice ID; no substitution/preset; same voice throughout.
**Source:** `Pylearn-build260/content/python-basics/modules/07-conditionals.md`
**Target:** 6–8 minutes.

### Scene 1 — A program makes a decision
**Visual:** Type `score = 82`, then `if score >= 70:` and indented `print("Passed")`.
**Narration:** “A score is eighty-two. Should the learner pass? A program can use a condition to choose what happens next. Read this as: if the score is at least seventy, print Passed. Notice that the print line is indented. In Python, indentation is part of the program's structure.”
**Run:** Output `Passed`.

### Scene 2 — Add an alternative
**Visual:** Add `else:` and `print("Needs more practice")`; change score to 64, run, then restore 82.
**Narration:** “The else branch gives Python another path when the condition is false. Only one of these branches runs. Change the score to sixty-four and predict the message before we run it.”
**Pause 4 seconds, run:** `Needs more practice`.

### Scene 3 — Multiple possibilities
**Visual:** Build the grade classifier incrementally: score >= 90 A; elif >= 80 B; elif >= 70 C; else F.
**Narration:** “When there are more than two possibilities, use elif. Python checks from top to bottom and stops at the first true condition. That's why the order matters. If a broad condition comes first, it can catch values that should have matched a more specific rule.”
**Visual:** Show plain-language rules beside code, then test 95, 84, 72, 55.

### Scene 4 — Boundary tests
**Visual:** Table of test scores 69, 70, 79, 80, 89, 90 and the expected grade. Reveal one row at a time with code execution.
**Narration:** “Don't test only middle values. Test where each rule changes: sixty-nine and seventy, seventy-nine and eighty, eighty-nine and ninety. This catches mistakes in greater-than versus greater-than-or-equal.”

### Scene 5 — Combine rules and practice
**Visual:** Show `if score >= 70 and attempts <= 3:`; highlight each condition.
**Narration:** “Conditions can combine Boolean expressions. This says the score must be at least seventy and the number of attempts must be no more than three. Your turn: build the score classifier and test every boundary. Then print a readable message with the score and grade.”
**Hold:** 4 seconds.

### Recap
**Narration:** “Use if, elif, and else to express decisions. Indentation defines each block, order matters, and boundary tests help verify the rules. Next, we'll repeat work efficiently with loops.”

## Final call to action — required for YouTube and in-app versions

**Visual:** Show the PyLearn app and clearly highlight the Practice section for Lesson 7. Do not show completed exercise answers. Leave the call to action on screen long enough to read.

**Narration:**

Now it's your turn to write code yourself.

Open the PyLearn app and go to the Practice section for Lesson 7. If you're watching this on YouTube, open PyLearn and find the practice for this lesson there.

Try the exercises yourself. Write the code, run it, and use the app's feedback to check your work. It's okay to make mistakes — that's how you learn.

The lesson showed you the concepts. Now practise them yourself in PyLearn. Stop watching, open the app, and start coding!

## Production checklist

- [ ] Keep the lesson rich and complete; do not shorten teaching content to make room for practice.
- [ ] The final card explicitly names the PyLearn app's Practice section.
- [ ] YouTube viewers are explicitly told to open PyLearn and find the matching lesson practice.
- [ ] The ending does not reveal exercise solutions.
- [ ] Verify all exercise references against the current app before recording.
- [ ] Review the full rendered video at normal speed before marking it complete.
