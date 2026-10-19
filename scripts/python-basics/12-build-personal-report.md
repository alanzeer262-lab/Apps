# PyLearn Video 12 — Build: My Learning Report

**Voice lock — mandatory:** Kendrick; ElevenLabs v3; exact approved Kendrick voice ID; no substitution/preset; same voice throughout.
**Source:** `Pylearn-build260/content/python-basics/modules/12-build-personal-report.md`
**Target:** 5–7 minutes. Project lesson after Modules 1–2.

### Scene 1 — From concepts to a useful program
**Visual:** Start with an empty editor; title “My learning report”.
**Narration:** “You've learned to give values names and display useful output. Now let's combine those skills into a small program: a learner report. It will include a name, a goal, weekly study hours, and whether the learner is active.”

### Scene 2 — Build the data
**Visual:** Reveal `name = "Ada"`, `goal = "Data Analyst"`, `weekly_hours = 6`, `active = True` one at a time.
**Narration:** “Each variable has a clear purpose. The name and goal are text, weekly hours is numeric, and active is a Boolean. The variable names tell another programmer what each value means.”

### Scene 3 — Create the report function
**Visual:** Reveal `def build_learning_report(name, goal, weekly_hours, active):` and a return value with four lines using an f-string.
**Narration:** “We'll put the formatting into a function called build_learning_report. It receives four inputs and returns a four-line report. Notice the word return: the function gives the text back to the caller. It does not print it by itself.”
**Visual:** Call the function, save its result, then print the result. Show exact output:
Learner: Ada
Goal: Data Analyst
Weekly study hours: 6
Status: Active

### Scene 4 — Test different cases
**Visual:** Test a normal learner, zero weekly hours, and an inactive learner. Change one input at a time.
**Narration:** “A useful function should work for more than one example. Test a learner who studies six hours, one who studies zero hours, and one whose status is inactive. The output should reflect the inputs without rewriting the function.”

### Scene 5 — Practice and recap
**Narration:** “Pause and build your own report. Change the name, goal, hours, and status. Then answer this: which values are measurements, and which values are descriptions?”
**Hold:** 4 seconds.
**Narration:** “You combined variables, readable names, f-strings, and a function that returns a formatted report. Next, we'll calculate study time from minutes and sessions.”
