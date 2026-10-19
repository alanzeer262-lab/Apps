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
**Review status:** Lesson and companion script content reviewed; runnable examples executed successfully and the intentionally broken quote was confirmed to raise a SyntaxError. Not approved for video production yet: real app navigation footage and the exact approved voice ID remain unverified, and the rendered video watch-through must happen after production.

### Findings and actions

- **Coverage gap — corrected in the first revision:** the script now includes a source-aligned illustrative profile using name, learning goal, and weekly study hours, with readable f-string output. The learner's turn also asks them to create their own profile. This is a separate example, not the required in-app exercise answer.
- **Pacing / cognitive load — improved, not fully signed off:** scene transitions and visual staging are clearer. The extra completed `double(7)` example was removed so the `pass` section stays focused on recognizing a placeholder rather than adding another function-writing demonstration.
- **Prerequisite framing — corrected:** the script explicitly says learners do not need to design whole functions from scratch yet; they need to recognize a provided starter and understand `return` because the app checks returned values.
- **Repetition — reduced:** the final debugging scene now applies the missing-quote example instead of re-teaching the full routine.
- **Code staging — improved:** scenes 1–6 now include explicit code/output examples and instructions for when to run them. Function definitions, return calls, and the print-only call remain separate so the output sequence is understandable.
- **Source alignment:** the script covers `print`, numeric output, quoted text/strings, matching quotes and a deliberately broken quote example, comments, f-strings, print-versus-return, `None`, `pass`, debugging, and the learner profile task.
- **Navigation remains unverified:** the ending states the required-exercise unlock rule and that Practice Drills are optional. The exact real PyLearn screen/path still needs capture from the app; do not invent or approximate UI in final footage.
- **Voice blocker:** the approved Kendrick voice ID is not recorded in the reviewed repository. Do not generate narration until the exact ID is recovered.

### Code/output QA — executed

The runnable Lesson 1 and P01 companion examples were executed in Python during this review.

- Lesson Scene 1: displays `Hello, I'm Python.`.
- Lesson Scene 2: displays `Hello, I'm Python.` then `5`.
- Lesson Scene 3: both lines display `10`; the values remain different types.
- Lesson Scene 4: the single- and double-quoted examples each display `Hello`. The intentionally malformed `print("Hello)` example raises a `SyntaxError` as expected.
- Lesson Scene 5: displays only `The code still runs.`; the comment is not displayed.
- Lesson Scene 6: displays exactly:
  ```text
  My name is Ada.
  My goal is to learn data analysis.
  I plan to study 6 hours each week.
  ```
- Lesson Scene 7: `add_tip(40)` returns `50`; output is `You pay: 50` and `For a table of two: 100`. The print-only function displays `50`, and the assigned result is `None`.
- P01 Scene 1 displays `Welcome to my study desk!`; Scene 2 displays `10`; Scene 3 displays `Ready to learn`.
- P01 Scene 4 was clarified to show both the broken code and the corrected `print("Hello")` with expected output `Hello`. The broken and corrected versions must be run separately.
- These checks confirm code behavior and expected output for the listed examples. They do not substitute for checking every scene in the final rendered video.

### Remaining production gates

1. Capture and verify the real PyLearn navigation path and required exercise screen; do not invent the UI.
2. Recover and verify the exact approved Kendrick voice ID; use ElevenLabs v3 and do not substitute a voice.
3. Once production is possible, review the complete rendered video at normal speed and check code/output synchronization before marking the video approved.

The source comparison, teaching-flow review, and listed runnable-code QA are complete for this content pass. Video-production approval remains separate from script readiness.

## Guided Practice 01 — First Program

**Script:** `scripts/python-basics/practice/P01-first-program-practice.md`
**Review status:** Content reviewed against the Lesson 1 goals; runnable examples executed; corrected quote example now includes its exact expected output. Not production-approved while the voice ID and real app navigation remain unverified. The companion ending correctly states that it does not complete the required app exercise or unlock the next lesson.

## Lesson 02 — Variables and Data Types

**Canonical source:** `content/python-basics/modules/02-variables-types.md`
**Scripts:** `docs/LESSON_02_NARRATION_SCRIPT.md` and `scripts/python-basics/practice/P02-variables-types-practice.md`
**Review status:** Source comparison and content review completed for both scripts. Runnable examples executed in Python. Two script clarifications committed: the full `type()` output is shown in the lesson script, string repetition is explicitly described as output `2121`, and invalid conversions are labeled as expected `ValueError` examples that must be run separately. The companion now states the expected invalid-input error.

### Findings and code/output QA

- Coverage matches the canonical module: assignment and reassignment, `str`, `int`, `float`, `bool`, `type()`, behavior differences between numbers and strings, conversions, invalid conversion, clear names/snake_case, and prediction before running.
- Executed reassignment examples: `print(name)` outputs `Ada` or `Sam` as shown; assigning `Sam` after `Ada` leaves `Sam` as the final value.
- Executed type example output:
  ```text
  <class 'str'>
  <class 'int'>
  <class 'float'>
  <class 'bool'>
  ```
- Executed `print(21 * 2)` and `print("21" * 2)`: outputs `42` and `2121`.
- Executed `int("21")` followed by adding one: output `22`.
- Executed the prediction example: `25`, `<class 'str'>`, `25`, `<class 'int'>`, `50`, each on its own line.
- Executed the companion's type and conversion examples: output is the expected four type names and `30`.
- Confirmed `int("hello")` and `int("twenty-five")` raise `ValueError`; these are deliberately failing demonstrations and must be run separately from valid examples.
- The learner task does not show a completed solution. The video ending still requires verified real PyLearn navigation footage and the correct required exercise screen.

### Remaining production gates

1. Recover and verify the exact approved Kendrick voice ID; use ElevenLabs v3 and do not substitute a voice.
2. Capture and verify the real PyLearn navigation path and required exercise screen.
3. After production is possible, review the complete rendered video at normal speed and check code/output synchronization before marking it approved.

## Lessons 03–20

Not yet reviewed in this pass. Each lesson and its companion will receive an individual source comparison and findings before its scripts are approved. File existence or a link in the index is not evidence of QA completion.
