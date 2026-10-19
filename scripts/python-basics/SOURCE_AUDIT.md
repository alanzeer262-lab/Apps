# Python Basics Video Script Audit — Source Check

**Status:** The pedagogical handoff is implemented across the current 20-script pack. This is not blanket approval to generate narration or publish all videos; individual technical and production checks remain.

## Canonical scope
- 19 Python Basics modules in `content/python-basics/track.yaml`.
- One separate Mini Gradebook capstone with five graded milestones.
- Canonical app content on `Pylearn-build260`, branch `ccr-c7f6fdd7-xpzi3g`, is the source of truth.

## Learning design implemented
The video explains and demonstrates a concept; the learner does actual practice in PyLearn.
- **Modules 1–11:** app-practice handoff added to each concept script. Videos use small examples and prediction pauses; the app is where learners complete the corresponding exercises.
- **Modules 12–19:** rewritten to explain the project goal and contract, teach selected concepts, ask a prediction question, and direct learners to implement and test in PyLearn. They intentionally do not provide a copyable full project solution.
- **Capstone:** rewritten as orientation only. It introduces the sample records and five milestone goals in order, but withholds completed code and final milestone answers. Learners solve and submit each milestone in the app.
- The app owns code entry, tests, hints, grading, submissions, and completion state. Video cannot verify that the learner practiced.

## Source accuracy and production controls
1. **Lesson 1:** added coverage of `print()` versus `return`, why a print-only function returns `None`, and `pass` in starter functions. Verify final scene order and visual timing before narration.
2. **Lesson 2:** preserve assignment/reassignment, `str`, `int`, `float`, `bool`, `type()`, conversion, invalid conversion, and `snake_case`. Verify final scene order and visual timing before narration.
3. **Modules 3–11:** scripts were compared with the canonical sources in this audit pass. Before audio, still independently verify every code example/output and ensure the final visual plan shows the right state at the right time. Pay special attention to operator semantics and units, string slices, threshold boundaries, empty lists, condition ordering, loop behavior, dictionary counting, return values, and safe conversion.
4. **Project modules 12–19:** preserve exact function signatures, return contracts, thresholds, and source-defined edge-case behavior. Do not invent extra behavior, including duplicate policy or unspecified empty-case outputs.
5. **Capstone:** exact milestones are `average_score(records)`, `top_scorer(records)`, `passed(records, cutoff=70)`, `grade_map(records)`, and `grade_counts(records)`. Tie behavior, threshold, order, and grade rules are defined by the app. Do not add invalid-input requirements.
6. **Voice lock:** Kendrick, ElevenLabs v3, exact user-approved voice ID. Never guess an ID or substitute another voice. Only narration text belongs in the TTS field.
7. **Production regression checks:** correct timing cannot compensate for a missing visual state; named learners/values must appear when spoken; future code/results must not be revealed early; use actual transcript timestamps; inspect the full render end-to-end.

## Release gate
A script is ready for narration only after its own canonical-source comparison, code/output verification, scene-by-scene visual plan review, app-practice handoff check, and voice-lock check. A rendered video must be watched end-to-end and corrected before user review. Publishing still requires explicit user approval.

## Current disposition
- **20 scripts updated for the app-first learning design.**
- **Project scripts 12–19 and capstone:** revised substantially; final line-by-line contract check and production review remain.
- **Concept scripts 1–11:** app-practice handoff added; full technical/visual QA remains before narration.
- **Not yet production-approved:** the pack must not be described as fully audited or ready to send to Runway until the release gate is completed.
