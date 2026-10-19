# PyLearn Video 20 — Mini Gradebook Capstone

**Voice lock — mandatory:** Kendrick voice; ElevenLabs v3; use the exact approved Kendrick voice ID; no substitution or preset; same voice throughout.
**Source:** `Pylearn-build260/content/python-basics/projects/capstone-gradebook.md` and capstone milestones in `content/python-basics/exercises/pb-capstone-m1.yaml` through `pb-capstone-m5.yaml`.
**Target:** 8–10 minutes. This is the capstone project, separate from the 19 track modules. Verify all milestone requirements against the canonical capstone before recording.

## Learning outcome
Combine records, loops, dictionaries, functions, conditionals, summaries, and explicit empty/invalid-data rules into a small gradebook.

### Scene 1 — The project goal
**Visual:** Title “Mini Gradebook”; show the input records as name/score pairs, not the final solution.
**Narration:** “You've learned Python one tool at a time. Now the goal is to combine those tools into one useful program. Our Mini Gradebook will accept learner records and produce a clear summary. We'll build it in small steps, testing after each step instead of writing everything at once.”

### Scene 2 — Represent the records
**Visual:** Show sample tuples such as Ada 88, Lin 72, Sam 95, Omar 64. Highlight each name/score pair.
**Narration:** “Each record groups a learner's name with a score. This structure makes it clear which score belongs to which learner. We'll loop through the records and give each field a meaningful name.”

### Scene 3 — Process and summarize
**Visual:** Build the loop and accumulator; calculate count and average, then identify top scorer. Reveal each field only when narrated.
**Narration:** “First, count the records and total the valid scores. Then calculate the average and identify the highest scorer. Each step answers one question. Keep the code readable, and test each new part before adding the next.”

### Scene 4 — Apply rules
**Visual:** Show grade boundaries and a passed threshold as configured by the capstone source. Demonstrate one boundary case at a time.
**Narration:** “Next, apply the grading rules. Translate each rule into a condition, and test the boundaries where one grade changes to another. A program can run without errors and still assign the wrong grade, so expected results matter.”

### Scene 5 — Make the report readable
**Visual:** Display a dictionary-style summary, then format a report with labels. Do not show fields that are not required by the source capstone.
**Narration:** “A summary should be easy for a person to understand. Give each result a clear label, and separate the calculation from the display where that improves reuse. The goal isn't the shortest code; it's a report whose meaning is obvious.”

### Scene 6 — Edge cases and evaluation
**Visual:** Show empty records and the source-defined invalid/missing data behavior. Show one small test at a time.
**Narration:** “Before trusting the result, test edge cases. What if there are no records? What if a score is exactly on a boundary? Follow the capstone's specified rules for empty or invalid input; don't silently invent a result.”

### Scene 7 — Recap and next stage
**Narration:** “You've combined records, loops, conditions, functions, and summaries into one program. The important skill is not memorizing every line. It's breaking a larger problem into smaller questions, testing each rule, and making the result clear. These are the same habits you'll use in data analysis.”

**Production note:** Before sending this script to Runway, reconcile each milestone and evaluation requirement with the canonical capstone file. Do not invent omitted capstone requirements or final outputs.
