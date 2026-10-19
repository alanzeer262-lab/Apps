# PyLearn Video 10 — Functions

**Voice lock — mandatory:** Kendrick; ElevenLabs v3; exact approved Kendrick voice ID; no substitution/preset; same voice throughout.
**Source:** `Pylearn-build260/content/python-basics/modules/10-functions.md`
**Target:** 7–8 minutes.

### Scene 1 — Give reusable logic a name
**Visual:** Show the same average calculation repeated twice, then replace it with a function definition.
**Narration:** “If the same calculation appears in several places, changing it becomes difficult. A function gives a piece of logic a name so you can reuse it. There are two separate actions: defining a function and calling it. Defining it doesn't run the body immediately.”

### Scene 2 — Parameters and arguments
**Visual:** Type `def greet(name):` with `return f"Hello, {name}!"`; call `greet("Ada")` and print returned message.
**Narration:** “The name inside the function definition is a parameter. When we call greet with Ada, Ada is the argument passed into that parameter. Think input, function, result.”

### Scene 3 — print versus return
**Visual:** Compare `show_double(number)` that prints with `double(number)` that returns number * 2. Call `result = double(7)` then print result.
**Narration:** “Print displays a result to the screen. Return gives a result back to the part of the program that called the function. The returned value can be saved, combined with another calculation, or passed to another function. For reusable logic, returning a value is often more useful than printing it.”

### Scene 4 — One clear job
**Visual:** Build `average_score(scores)` returning `sum(scores) / len(scores)`; show a call on [10, 20, 30] → 20.0.
**Narration:** “A good function has one clear job, and its name helps explain that job. Small functions are easier to test, understand, and change. Also think about edge cases: what should average_score do when the list is empty? Decide a rule instead of letting an unexpected crash define the behavior.”

### Scene 5 — Defaults and local variables
**Visual:** `def passed(score, cutoff=70): return score >= cutoff`; show calls passed(80) and passed(80, 90). Then highlight local total inside average_score.
**Narration:** “A default parameter provides a common value but lets the caller choose another. Here, the cutoff is seventy unless we supply a different one. Variables created inside a function normally belong to that function, so the caller only needs the returned result.”

### Scene 6 — Practice
**Visual:** Prompt: write study_hours(minutes), return minutes / 60 rounded to two decimals; then passed(score, cutoff=70). Do not reveal complete solution until after pause.
**Narration:** “Your turn. Write a function that converts minutes to hours and returns the result rounded to two decimal places. Then write a passed function with a default cutoff. Test normal values and the edge cases you think matter.”
**Hold:** 4 seconds.

### Recap
**Narration:** “Functions organize programs into reusable pieces. You define and call them, pass inputs through parameters, and return useful results. Defaults make common choices convenient, and small functions make larger problems manageable. Next, we'll use comprehensions, imports, and safe conversion.”

## Final call to action — required for YouTube and in-app versions

**Visual:** Show the PyLearn app and clearly highlight the Practice section for Lesson 10. Do not show completed exercise answers. Leave the call to action on screen long enough to read.

**Narration:**

Now it's your turn to write code yourself.

Open the PyLearn app and go to the Practice section for Lesson 10. If you're watching this on YouTube, open PyLearn and find the practice for this lesson there.

Try the exercises yourself. Write the code, run it, and use the app's feedback to check your work. It's okay to make mistakes — that's how you learn.

The lesson showed you the concepts. Now practise them yourself in PyLearn. Stop watching, open the app, and start coding!

## Production checklist

- [ ] Keep the lesson rich and complete; do not shorten teaching content to make room for practice.
- [ ] The final card explicitly names the PyLearn app's Practice section.
- [ ] YouTube viewers are explicitly told to open PyLearn and find the matching lesson practice.
- [ ] The ending does not reveal exercise solutions.
- [ ] Verify all exercise references against the current app before recording.
- [ ] Review the full rendered video at normal speed before marking it complete.
