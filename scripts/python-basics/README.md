# PyLearn Python Basics — Runway Script Pack

This folder contains the **pre-audio phase** for the full Python Basics track. The goal is to prepare the source-grounded narration and visual plan now, without spending Runway credits. No Android app code or reading lessons are changed by these scripts.

## Voice lock — applies to every script
- Voice: **Kendrick**
- Model: **ElevenLabs v3**
- Use the exact Kendrick voice ID already approved by the user.
- **No voice substitution, preset, or alternate voice. Keep the same voice throughout.**
- Never invent or guess the custom voice ID. If Runway cannot list it, stop and report the limitation rather than silently choosing another voice.

## Lesson order
1. [Your First Python Program](../../docs/LESSON_01_FINAL_NARRATION_TEXT.md) — existing approved source script; check its voice lock before submission.
2. [Variables and Data Types](../../docs/LESSON_02_VARIABLES_AND_DATA_TYPES_SCRIPT.md) — existing script; must be reviewed against the canonical module and the latest full-video defect log before audio generation.
3. [Numbers and Operators](03-numbers-and-operators.md)
4. [Strings and f-strings](04-strings-and-f-strings.md)
5. [Booleans and Comparisons](05-booleans-and-comparisons.md)
6. [Lists](06-lists.md)
7. [Conditionals](07-conditionals.md)
8. [Loops](08-loops.md)
9. [Dictionaries, Tuples, and Sets](09-dictionaries-tuples-sets.md)
10. [Functions](10-functions.md)
11. [Comprehensions, Imports, and Safe Conversion](11-comprehensions-imports-safe-conversion.md)
12. [Build: My Learning Report](12-build-personal-report.md)
13. [Build: Study Time Calculator](13-build-study-calculator.md)
14. [Build: Clean My Learning Topics](14-build-topic-cleaner.md)
15. [Build: Score Summary](15-build-score-summary.md)
16. [Build: Multi-Record Progress Analyzer](16-build-progress-analyzer.md)
17. [Build: Grade Distribution](17-build-grade-distribution.md)
18. [Build: Reusable Analysis Toolkit](18-build-toolkit.md)
19. [Build: Handle Imperfect Scores](19-build-messy-input.md)
20. [Mini Gradebook Capstone](20-mini-gradebook-capstone.md) — project/capstone, not a numbered module.

## Before sending any script to Runway
1. Confirm the script matches the exact source lesson and its sequence.
2. Read the whole narration out loud or silently check for missing words, awkward transitions, code pronunciation, and unsupported claims.
3. Confirm every code example and stated output is correct.
4. Keep voice lock text at the top of the Runway request.
5. Generate audio only when credits are available and the script is approved.
6. Preserve the exact generated audio files and settings. Upload the audio to the matching lesson folder.
7. The production workflow then starts from the audio: validate all files, transcribe, timestamp, align visuals to the actual recording, render, inspect the entire MP4, fix defects, rerender, and only then request the user's video review.

## Important boundaries
- These are draft narration/visual scripts, not approved final audio timings. Never use estimated script timings as final sync timestamps.
- Do not edit the Android app or its existing reading lessons.
- Do not generate audio or spend Runway credits in this phase.
- Do not publish a lesson automatically. The user must inspect and confirm the finished video before any final publication step.
- The mandatory full-video checklist in `docs/VIDEO_PRODUCTION_WORKFLOW.md` applies to every lesson.
