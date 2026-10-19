# PyLearn Python Basics — Lesson-by-Lesson Script Review

**Status:** Review in progress. Scripts are not approved for narration or rendering merely because files exist.
**Source of truth:** `mohamedalnazeer262-coder/Pylearn-build260`, branch `ccr-c7f6fdd7-xpzi3g`.
**Review rule:** Finish the source comparison, teaching-flow review, code/output checks, and navigation check for one lesson before treating that lesson as ready. Do not bulk-mark lessons complete.

## Review checklist applied to every lesson

1. **Source fidelity:** every required concept is represented; no source requirement is silently dropped; examples stay aligned with the canonical app lesson.
2. **Teaching sequence:** one main idea at a time, appropriate prerequisites, explanations before terminology, prediction pauses before runs, recap matches what was taught.
3. **Code/output correctness:** execute every example; verify exact output, whitespace, types, rounding, and error claims.
4. **Example safety:** examples teach the concept without revealing required exercise answers, hidden tests, or a complete project/capstone solution.
5. **Video usability:** readable phone-sized code, explicit reveal/run/output timing, no duplicate scenes or conflicting versions, narration separated from production notes.
6. **Navigation:** exact lesson/task name and real app path verified; required exercise completion unlocks the next lesson; Practice Drills are optional; project and capstone endings follow their own rules.
7. **Voice and delivery:** Kendrick, ElevenLabs v3, exact approved voice ID verified before narration generation; no guessed ID or substitute voice.
8. **Final watch-through:** inspect the full rendered video at normal speed before approval.

## Lesson 01 — Your First Python Program

**Canonical source:** `content/python-basics/modules/01-first-program.md`
**Script:** `scripts/python-basics/01-your-first-python-program.md`
**Review status:** Needs revision before production.

### Findings

- **Coverage gap — learner profile:** the source asks the learner to store a name, a learning goal, and weekly study hours, then print all three as readable sentences. The script demonstrates a name greeting but does not teach the goal and weekly-hours parts of that source example. Add a small complete illustrative profile while keeping it separate from the required app exercise.
- **Pacing / cognitive load:** the script contains 11 teaching scenes and introduces strings, comments, f-strings, functions, print-versus-return, `None`, `pass`, and debugging in one video. These concepts exist in the source, but the current video needs stronger signposting and shorter, clearly separated steps so the first lesson does not feel like several lessons combined.
- **Prerequisite framing:** the source says learners do not need to design functions yet, while also introducing `return` because the first exercises check returned values. The script should make that distinction explicit: recognize and understand the provided function starter; do not imply that learners must already design functions from scratch.
- **Repetition:** debugging is explained in the matching-quotes scene, again in “Your turn,” and again in a separate debugging scene. Keep the first explanation, then use the later moment as a short application rather than repeating the same lesson.
- **Visual/code staging:** the script includes code/output for the function examples, but the editor instructions need to make each execution boundary explicit: defining functions alone produces no output; each call should be run separately; output must appear only after its call is explained.
- **Navigation remains unverified:** the ending correctly states that the required exercise unlocks the next lesson and that Practice Drills are optional. The exact real PyLearn screen/path still needs a capture from the app; do not invent or approximate the UI in the final footage.
- **Voice blocker:** the approved Kendrick voice ID is not recorded in the reviewed repository. Do not generate narration until the exact ID is recovered.

### Code/output observations

- `print("Hello, I'm Python.")` should display `Hello, I'm Python.`.
- `print(2 + 3)` displays `5`.
- `print(10)` and `print("10")` look alike in output, but are different types; this lesson should state that type is explored in Lesson 2.
- The return example is logically correct: `add_tip(40)` returns `50`, the two subsequent prints show `You pay: 50` and `For a table of two: 100`; `show_total(40)` displays `50` and its assigned result is `None`. These outputs still need execution in the final QA pass.
- The script's `double(7)` example outputs `14`; consider whether this extra function example is worth the additional load in Lesson 1.

### Required revision before approval

1. Add the source-aligned name/goal/study-hours example.
2. Rework the lesson flow to distinguish “understand a provided return-based starter” from “learn to design functions later.”
3. Reduce repeated debugging explanation and tighten scene transitions without removing required source concepts.
4. Make the run/output sequence explicit for each function example.
5. Keep the existing required-exercise unlock rule and optional-drills wording.
6. Verify the actual Lesson 1 navigation footage and execute every code sample before marking the lesson approved.

## Lessons 02–20

Not yet reviewed in this pass. Each will receive its own source comparison and findings before its script is approved. File existence or a link in the index is not evidence of QA completion.
