# Python Basics Video Script Audit — Source Check

**Status:** Source audit is ongoing. The first pass found gaps; revised project scripts now follow an app-first practice design. This is not blanket approval to generate narration or publish all 20 videos.

## Canonical scope
- 19 Python Basics modules in `content/python-basics/track.yaml`.
- One separate Mini Gradebook capstone with five graded milestones.
- Canonical app content on `Pylearn-build260`, branch `ccr-c7f6fdd7-xpzi3g`, is the source of truth.

## Learning design decision
The video explains and demonstrates a concept; the learner does the actual practice in PyLearn. Concept videos use short examples and prediction pauses. Project videos explain the goal and contract, demonstrate selected techniques, and leave meaningful implementation to the learner. The capstone video introduces the dataset and milestone goals without revealing the five solutions. The app remains responsible for code entry, tests, hints, grading, and completion.

## Findings and controls
1. **Lesson 1:** the app explicitly teaches `print()` versus `return`, why a print-only function returns `None`, and `pass` in starter functions. The script was updated for these omissions; verify the final scene order before narration.
2. **Lesson 2:** preserve assignment/reassignment, `str`, `int`, `float`, `bool`, `type()`, conversion, invalid conversion, and `snake_case`. Verify final scene order before narration.
3. **Modules 3–11:** still require individual source-by-source final checks for operator semantics/outputs, strings, Booleans, lists, conditionals, loops, dictionaries/tuples/sets, functions, comprehensions/imports, `None`, and safe conversion.
4. **Project modules 12–19:** rewritten to explain the mission, teach selected concepts, ask a prediction question, and direct learners to implement and test in PyLearn. Their exact function signatures, output contracts, thresholds, and edge-case behavior must remain aligned with source.
5. **Capstone:** revised to orientation-only. It names the five milestone goals in order but intentionally withholds completed code and final answers. The canonical app tasks are `average_score(records)`, `top_scorer(records)`, `passed(records, cutoff=70)`, `grade_map(records)`, and `grade_counts(records)`. Tie behavior, threshold, order, and grade rules are defined by the app; do not invent invalid-input requirements.
6. **Voice lock:** Kendrick, ElevenLabs v3, exact user-approved voice ID. Never guess an ID or substitute another voice. Only narration text belongs in the TTS field.
7. **Production regression checks:** correct timing cannot compensate for a missing visual state; named learners/values must appear when spoken; future code/results must not be revealed early; use actual transcript timestamps; inspect the full render.

## Release gate
A script is ready for narration only after its own canonical-source comparison, code/output verification, scene-by-scene visual plan review, app-practice CTA check, and voice-lock check. A rendered video must be watched end-to-end and corrected before user review. Publishing still requires explicit user approval.

## Current disposition
- Modules 12–19: rewritten to make the app the place where learners implement the projects; they still need a final individual source and production-readiness review.
- Capstone: rewritten as orientation only; does not reveal milestone solutions.
- Modules 1–11: remain in the audit queue; do not describe the full 20-script pack as approved.
