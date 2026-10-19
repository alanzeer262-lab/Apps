# Python Basics Video Script Audit — Source Check

**Status:** First source audit pass completed against the canonical Python Basics track on branch `ccr-c7f6fdd7-xpzi3g` in `Pylearn-build260`. This is a content audit, not approval to generate narration or publish videos.

## Canonical scope
- 19 track modules, in the order listed in `content/python-basics/track.yaml`.
- One separate Mini Gradebook capstone with exactly five graded milestones.
- The app lesson/module remains the source of truth. Video scripts must not add requirements or replace the app lesson.

## Findings and corrections required before Runway

1. **Lesson 1 — missing source coverage.** The app module explicitly teaches the difference between `print()` and `return`, demonstrates why a print-only function returns `None`, and explains `pass` in starter functions. The current narration draft covered print, comments, strings, f-strings, and debugging, but omitted those required concepts. The script is updated to include concise, runnable examples of both.
2. **Lesson 2 — topic scope drift.** The canonical module includes assignment/reassignment, `str`, `int`, `float`, `bool`, `type()`, conversion, invalid conversion, and `snake_case`. Keep these in the lesson rather than omitting conversion or clear naming. Avoid unrelated values or invented examples that complicate the screen.
3. **Modules 3–11 — preserve the canonical progression.** Verify operator semantics and outputs; string indexing/slicing and text cleaning; Boolean comparisons and boundaries; list empty cases; conditional ordering; loop accumulation/filtering; dictionary counting and tuple unpacking; function return/edge cases; comprehensions, imports, `None`, and `try/except`. Do not show output until narration reaches the corresponding step.
4. **Build modules 12–19 — source-defined contracts only.** Keep exact function names, parameters, return shape, thresholds, empty-case requirements, and invalid-input behavior from each module. Never imply that a function prints if the source requires it to return a value.
5. **Capstone — source mismatch corrected.** The capstone is not a generic gradebook build. It consists of exactly five milestone functions: `average_score(records)` (mean rounded to two decimal places), `top_scorer(records)` (return the name; ties keep first), `passed(records, cutoff=70)` (names in original order), `grade_map(records)` (A at 90+, B at 80–89, C at 70–79, F below 70), and `grade_counts(records)` (frequency dictionary). The source capstone does not specify invalid-score handling; do not invent it as a capstone requirement. Empty-input behavior should only be mentioned where the source/milestone actually defines it.
6. **Voice lock.** Keep Kendrick, ElevenLabs v3, exact user-approved voice ID; no guessed ID, preset, or voice substitution. Send only narration to Runway's TTS field; visual instructions stay separate.
7. **Lesson 1/2 production learning.** Correct audio timing alone is not enough: every named learner/value introduced by narration must visibly appear at the right time. Never reveal a future code line or output early. Review the whole render from first frame to last at normal speed and fix missing visual states before asking the user to review.

## Pre-Runway release gate
- Script compared against the exact canonical module/project.
- Code examples and outputs independently checked.
- Every source concept included at the intended level; no unsupported concepts or requirements.
- Narration separated from visual direction and contains only words to be spoken.
- Each scene says what must be on screen and when it appears; prediction pauses do not reveal answers early.
- Exact voice lock copied to the Runway instructions.
- User approval is still required before publishing any new video.

## Current disposition
The pack has 20 scripts (19 modules plus the separate capstone). The Lesson 1 script was revised for a confirmed source-coverage gap. The remaining scripts still require a final script-by-script release check before they should be sent for narration; this document must not be interpreted as a claim that all 20 are production-approved.
