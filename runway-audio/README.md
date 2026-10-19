# PyLearn Track 2 — Runway audio masters

These files are the **spoken narration only**, one Markdown file per video. Upload the matching `.md` file when generating that video's narration/audio.

## Required voice configuration

- **Voice:** Kendrick — the exact user-approved voice ID already selected in the connected production setup.
- **Model:** ElevenLabs v3.
- Do not substitute a voice, voice ID, or model.
- Preserve the full narration verbatim. Do not summarize, rewrite, add an intro/outro, or omit any paragraph.
- Generate one complete audio track from the entire file. Do not stop after the first section or split it into partial audio unless the user specifically asks.
- Read the text naturally as an educational teacher: clear, warm, measured, and consistent. Use natural pauses at paragraph breaks. Do not add sound effects, music, or extra spoken words.
- The narration masters intentionally contain no scene titles, visual directions, code listings, expected-output blocks, or production checklists. Those belong to the separate storyboard files under `scripts/python-foundations/` and must not be read aloud.
- Acronyms and technical terms should be spoken naturally. In the audio masters, “C S V” is spaced for clear speech.
- Do not invent pronunciation for unfamiliar names or replace the approved voice. If the voice selector is not showing the approved Kendrick voice, stop rather than silently substituting another voice.

## Endings

- Lessons 1–10 hand off to the matching practice video.
- Practice videos P01–P10 tell learners to complete the exercise to unlock the next lesson and mention optional extra practice in the PyLearn app.
- Lesson 11 hands off to final capstone practice.
- Practice P11 ends with congratulations for completing Python Foundations and does **not** mention unlocking another lesson.

## Important limitation

The Markdown controls the narration text and states the intended voice/model, but the Runway voice selector must still be configured to the approved Kendrick voice ID and ElevenLabs v3. Uploading a file alone cannot force a different or unavailable voice setting.

## Files

### Lesson narration masters
- [Lesson 01 — Debugging](python-foundations/lesson-01-debugging.md)
- [Lesson 02 — Files and CSV](python-foundations/lesson-02-files-csv.md)
- [Lesson 03 — Modules](python-foundations/lesson-03-modules-organization.md)
- [Lesson 04 — Validation and Testing](python-foundations/lesson-04-validation-testing.md)
- [Lesson 05 — Table-Shaped Data](python-foundations/lesson-05-data-shaped-python.md)
- [Lesson 06 — Reliable Report Pipeline](python-foundations/lesson-06-analysis-ready-pipeline.md)
- [Lesson 07 — Build Loader](python-foundations/lesson-07-build-loader.md)
- [Lesson 08 — Build Validation](python-foundations/lesson-08-build-validate.md)
- [Lesson 09 — Build Summary](python-foundations/lesson-09-build-summary.md)
- [Lesson 10 — Build Pipeline](python-foundations/lesson-10-build-pipeline.md)
- [Lesson 11 — Final Capstone](python-foundations/lesson-11-final-capstone.md)

### Practice narration masters
- [P01 — Debugging](python-foundations/practice-P01-debugging.md)
- [P02 — Files and CSV](python-foundations/practice-P02-files-csv.md)
- [P03 — Modules](python-foundations/practice-P03-modules.md)
- [P04 — Validation and Testing](python-foundations/practice-P04-validation-testing.md)
- [P05 — Table-Shaped Data](python-foundations/practice-P05-table-data.md)
- [P06 — Pipeline](python-foundations/practice-P06-pipeline.md)
- [P07 — Loader](python-foundations/practice-P07-loader.md)
- [P08 — Validation](python-foundations/practice-P08-validation.md)
- [P09 — Summary](python-foundations/practice-P09-summary.md)
- [P10 — Pipeline](python-foundations/practice-P10-pipeline.md)
- [P11 — Final Capstone](python-foundations/practice-P11-final-capstone.md)
