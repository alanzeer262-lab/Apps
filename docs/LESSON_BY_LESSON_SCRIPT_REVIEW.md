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
**Review status:** First revision committed; still not approved for production. Remaining gates: execute all code examples, verify real app navigation footage, and recover the exact approved voice ID.

### Findings and actions

- **Coverage gap — corrected in the first revision:** the script now includes a source-aligned illustrative profile using name, learning goal, and weekly study hours, with readable f-string output. The learner's turn also asks them to create their own profile. This is a separate example, not the required in-app exercise answer.
- **Pacing / cognitive load — improved, not fully signed off:** scene transitions and visual staging are clearer. The extra completed `double(7)` example was removed so the `pass` section stays focused on recognizing a placeholder rather than adding another function-writing demonstration.
- **Prerequisite framing — corrected:** the script explicitly says learners do not need to design whole functions from scratch yet; they need to recognize a provided starter and understand `return` because the app checks returned values.
- **Repetition — reduced:** the final debugging scene now applies the missing-quote example instead of re-teaching the full routine.
- **Code staging — improved:** scenes 1–6 now include explicit code/output examples and instructions for when to run them. Function definitions, return calls, and the print-only call remain separate so the output sequence is understandable.
- **Source alignment:** the script covers `print`, numeric output, quoted text/strings, matching quotes and a deliberately broken quote example, comments, f-strings, print-versus-return, `None`, `pass`, debugging, and the learner profile task.
- **Navigation remains unverified:** the ending states the required-exercise unlock rule and that Practice Drills are optional. The exact real PyLearn screen/path still needs capture from the app; do not invent or approximate UI in final footage.
- **Voice blocker:** the approved Kendrick voice ID is not recorded in the reviewed repository. Do not generate narration until the exact ID is recovered.

### Code/output observations

- `print("Hello, I'm Python.")` displays `Hello, I'm Python.`.
- `print(2 + 3)` displays `5`.
- `print(10)` and `print("10")` both display `10`, while Python treats the values differently.
- The profile example should display exactly:
  ```text
  My name is Ada.
  My goal is to learn data analysis.
  I plan to study 6 hours each week.
  ```
- The return example is logically correct: `add_tip(40)` returns `50`; the following prints show `You pay: 50` and `For a table of two: 100`. The print-only function displays `50`, and its assigned result is `None`.
- The comments example displays only `The code still runs.`; the comment is not displayed.
- These outputs have been checked by inspection but **have not yet been executed as a complete QA pass**. Run every runnable code sample before production approval. The intentionally malformed quote must be tested separately as an expected SyntaxError.

### Remaining approval gates

1. Execute every runnable code sample and confirm exact output; separately verify the expected syntax error.
2. Confirm that the full narration does not imply learners must design functions from scratch.
3. Capture and verify the real PyLearn navigation path and required exercise screen.
4. Recover and verify the exact approved Kendrick voice ID; do not substitute a voice.
5. Review the complete rendered video at normal speed before marking Lesson 1 approved.

## Lessons 02–20

Not yet reviewed in this pass. Each will receive its own source comparison and findings before its script is approved. File existence or a link in the index is not evidence of QA completion.
