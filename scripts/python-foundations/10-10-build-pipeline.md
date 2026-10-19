# PyLearn Video — 10 — Build: Run the Pipeline

**Voice lock — mandatory:** Use the user-approved Kendrick voice with ElevenLabs v3. Do not substitute another voice or preset.
**Canonical source:** Pylearn-build260/content/python-foundations/modules/10-build-pipeline.md, branch ccr-c7f6fdd7-xpzi3g.
**Use:** Full teaching video, not a short outline. Narrate only spoken text; keep scene headings, code labels, and visual directions out of text-to-speech. Do not show the app's required exercise solution.

## Scene 1 — Connect the parts

**Visual:** Reveal the code gradually. Ask for a prediction before running it. Show the output only after the run.

**Narration:**

A user of your toolkit should not need to remember every internal step. One public function can take raw CSV text and coordinate loading, validation, and aggregation. Internally, each stage still has one job.

**Code**
    
    raw_text = "name,score\nAda,88\nLin,72\n"
        print("Pipeline input received")
        print("Characters:", len(raw_text))

**Expected output**
    
    Pipeline input received
        Characters: 31

**Narration:**

We begin with the raw input. The full pipeline parses it, checks the values, and calculates the summary. The order matters because aggregation should use validated records.

## Scene 2 — Preserve the stages

**Visual:** Reveal the code gradually. Ask for a prediction before running it. Show the output only after the run.

**Narration:**

The pipeline should load first, validate second, and summarize last. This keeps the code understandable and makes each part testable on its own.

**Code**
    
    stages = ["load", "validate", "summarize"]
        for stage in stages:
            print("Running:", stage)

**Expected output**
    
    Running: load
        Running: validate
        Running: summarize

**Narration:**

This short example illustrates the order without pretending to be the complete toolkit. Each stage should receive a clearly defined input and return a predictable result.

## Scene 3 — One call, useful result

**Visual:** Reveal the code gradually. Ask for a prediction before running it. Show the output only after the run.

**Narration:**

A single entry point can hide the plumbing while still returning a structured summary. The caller can then display the result, save it, or test it.

**Code**
    
    result = {
            "rows_read": 2,
            "valid_rows": 2,
            "invalid_rows": 0,
            "average": 80.0,
        }
        print("Average:", result["average"])
        print("Invalid rows:", result["invalid_rows"])

**Expected output**
    
    Average: 80.0
        Invalid rows: 0

**Narration:**

The numbers here are an illustrative report structure, not the output of the app's required exercise. Your toolkit must derive its own report from the supplied input and apply its validation rules.

## Scene 4 — Ready for the final build

**Visual:** Reveal the code gradually. Ask for a prediction before running it. Show the output only after the run.

**Narration:**

You now have the building blocks: load, validate, summarize, and connect. In the capstone, you will run the toolkit on a deliberately imperfect CSV and explain the cleaning decisions. Do not aim only for code that runs; aim for a report a person can trust.

**Code**
    
    required_sections = [
            "rows read", "valid rows", "invalid rows",
            "cleaning decisions", "average", "top performer",
            "grade distribution", "warning or limitation",
        ]
        print("Report sections:", len(required_sections))

**Expected output**
    
    Report sections: 8

**Narration:**

Use this list as a planning checklist. The capstone practice video will guide you through milestones without giving away the completed implementation.

## Your turn — predict, run, explain

**Visual:** Keep the editor uncluttered. Show a fresh, related prompt without using the app's required exercise code.

**Narration:**

Pause the video and try a small variation of the example. Predict the output before you run it. Then run the code, compare the result with your prediction, and explain why it happened. If the result surprises you, inspect the values and change one thing at a time.

This is extra guided practice, not the required PyLearn exercise solution.

## Recap

**Narration:**

Today, you learned the core idea behind one entry point. Keep the stages clear, test your assumptions, and make the program's behavior visible. In the next lesson, we'll build on this skill.

## Final call to action — watch the practice video

**Visual:** Neutral end card reading “Next: Practice Video”. Do not show unfinished app screens or invent navigation.

**Narration:**

Great work! You've finished Build: Run the Pipeline. Next, watch the practice video. I recommend watching it because we'll use a fresh example to reinforce the skill from this lesson.

After the practice video, complete the exercise to unlock the next lesson. If you'd like extra hands-on practice, you can also try it in the PyLearn app.

**Visual:** Hold the end card long enough to read.

## Production checklist

- [ ] Use the approved Kendrick voice with ElevenLabs v3.
- [ ] Verify every example and expected output in Python before rendering.
- [ ] Reveal code before running it; reveal output only after the run.
- [ ] Keep narration separate from production directions.
- [ ] Do not show the required app exercise solution or hidden tests.
- [ ] Watch the complete rendered video at normal speed before approval.
