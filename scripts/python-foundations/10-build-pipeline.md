# PyLearn Video — Build: Run the Pipeline

**Track 2 visual identity:** Keep the same teacher and pacing. Use an animated pipeline map with three connected stations—Load, Validate, Summarize—and show each station passing a small record bundle to the next. When introducing report requirements, use a checklist panel and report wireframe rather than a stack of input/output boxes. Highlight the active stage on the persistent toolkit rail.

**Voice lock:** Use the user-approved Kendrick voice with ElevenLabs v3. Do not substitute another voice.
**Canonical source:** Pylearn-build260/content/python-foundations/modules/10-build-pipeline.md, branch ccr-c7f6fdd7-xpzi3g.
**Production rule:** Narrate only spoken text. Do not show the required app exercise solution or invent app screens.

## Scene 1 — Connect the parts

**Narration:**

A user should not need to remember every internal step. One public function can take raw CSV text and coordinate loading, validation, and aggregation. Each internal stage still has one clear job.

**Visual:** Show the sequence load → validate → summarize.

**Code**

    stages = ["load", "validate", "summarize"]
    for stage in stages:
        print("Running:", stage)

**Expected output**

    Running: load
    Running: validate
    Running: summarize

This simple example illustrates the order. The actual toolkit must pass the output of each stage to the next.

## Scene 2 — Keep the stages testable

**Narration:**

Loading turns CSV text into records. Validation checks the rules. Aggregation calculates the summary from records that passed validation. If one stage fails, you can test it on its own instead of debugging one giant function.

**Code**

    raw_text = "name,score\nAda,88\nLin,72\n"
    print("Input received:", len(raw_text), "characters")

**Expected output**

    Input received: 25 characters

The pipeline starts with raw input. The final result should come from processing that input, not from hard-coded summary values.

## Scene 3 — Design a useful report

**Narration:**

The capstone report must include rows read, valid rows, invalid rows, cleaning decisions, average score, top performer, grade distribution, and one warning or limitation. A report should explain what happened to the data, not just show a number.

**Visual:** Reveal the eight report requirements as an empty checklist. Do not show a completed solution.

## Recap and handoff

You've connected the loading, validation, and summary stages into one pipeline concept. Next, watch the practice video, then complete the exercise to unlock the next lesson. Extra practice in the PyLearn app is optional.

## Final production checklist

- [ ] Verify each code sample and stated output in Python.
- [ ] Reveal code before running it and output only after the run.
- [ ] Keep narration separate from visual directions.
- [ ] Watch the complete rendered video at normal speed before approval.
