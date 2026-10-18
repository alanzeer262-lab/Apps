# PyLearn Video Teaching Rules — Pilot Standard

Status: PILOT — validate against Lesson 01 before treating these rules as final.

## Teaching promise
Teach like a patient personal tutor sitting beside a beginner. The learner should feel guided, not flooded with information. Understanding matters more than covering the maximum number of facts per minute.

## Rules for every lesson
1. **One learning goal per video.** Do not add an advanced concept merely because it fits in the runtime. Move it to the lesson where it is needed.
2. **One new idea at a time.** Introduce it in plain language, show the smallest useful example, explain the example, then let the learner observe the result.
3. **Use the tutor rhythm:** introduce → demonstrate → explain → predict → run → observe → practice → recap.
4. **Explain the why.** For every new code element, answer: What is it? What does it do here? What should I notice?
5. **Keep sentences short and conversational.** Avoid long strings of definitions, lists, or repeated facts. Speak to the learner as “you”.
6. **Do not rush code.** Reveal only the relevant line or small chunk. Keep code and its real output visible together long enough to read both.
7. **Pause with purpose.** Give about 3–5 seconds for a genuine prediction or learner task. Do not use long empty holds to hide a fast script.
8. **Reveal answers after thinking time.** Ask a clear question, pause, run the code, then explain what happened.
9. **Prefer a small number of meaningful examples.** Change one value at a time so the learner can see cause and effect.
10. **Normalize mistakes.** Demonstrate at most one small, relevant error at a time. Explain what the error tells us, fix one thing, and run again.
11. **Protect lesson scope.** If a concept needs a long explanation, move it to a separate video. In particular, do not teach `print()` versus `return` in the first program video; reserve functions and return values for a dedicated lesson.
12. **End with learner success.** The learner should complete one small task and be able to say what they learned in their own words.
13. **Never sacrifice clarity to hit a target duration.** Prefer a clear 6–8 minute lesson over a dense lesson with more topics. If a script is too long, remove lower-priority concepts before speeding up delivery.
14. **Narration and visuals must agree exactly.** The spoken code, editor code, output, and cue anchors must refer to the same example.
15. **Do not fake validation.** A successful render proves the build completed, not that the lesson is pedagogically good or fully synchronized. Review the rendered video from beginning to end.

## Review checklist
- Can a beginner explain the main idea after watching?
- Is every new term explained when first introduced?
- Does each code example have a clear purpose?
- Is there time to read code before it runs?
- Are prediction pauses real and answers revealed afterward?
- Does any section feel like a list of facts? If yes, cut or split it.
- Is the learner asked to do one manageable task?
- Is the whole video checked, not only the first half?

## Pilot decision
After reviewing Lesson 01, mark each rule as:
- **Keep** — clearly improves learning.
- **Change** — needs adjustment based on playback.
- **Unproven** — needs another lesson or learner test.

Only after the pilot review should these become the standard for the remaining videos.
