# PyLearn Video Studio — Mandatory Agent Instructions

These instructions apply to **every AI agent, coding agent, or assistant** working in this repository. Read this file before changing files, creating a lesson, generating audio, or rendering a video. The purpose is to prevent the user from having to repeat the workflow and constraints.

## Mission

Create accurate, polished PyLearn teaching videos from the **canonical lesson content** in the PyLearn app repository. Work end-to-end where tools and required assets are available, preserve progress in GitHub, and report honestly what is and is not complete.

## Non-negotiable rules

1. **Canonical source first.** Read the full relevant lesson from `mohamedalnazeer262-coder/Pylearn-build260`, branch `ccr-c7f6fdd7-xpzi3g`. Do not invent lesson objectives or silently omit core teaching content. The source lesson is authoritative for concepts, code, outputs, and exercises.
2. **Follow the production order below.** Do not skip ahead to renderer changes or claim a lesson is ready before its prerequisites exist.
3. **Use the exact approved voice.** Narration must use the user's specified ElevenLabs v3 voice ID (Kendrick). Never substitute a different voice or a generic preset. If the exact voice ID or authorized voice-generation access is unavailable, stop at that gate and clearly identify what is missing; do not pretend audio was generated.
4. **Narration drives timing.** Transcribe the actual generated narration audio with Whisper (or the configured transcription tool). Derive scene boundaries and synchronization from that transcript, actual timestamps, and exact spoken phrases. Never invent timestamps, estimate timings from the script alone, or use another lesson's audio as a stand-in.
5. **Preserve working production methods.** Keep the existing/old alignment algorithm as a fallback. Use a new algorithm only if a rendered comparison demonstrates better visual quality and narration alignment. Do not replace a known-good path on theory alone.
6. **Teach with the visuals.** Code, output, captions, and visual emphasis must match the narration and canonical lesson. Show code as it is explained; display correct outputs; preserve readable sizing, clear transitions, and continuity. Never show misleading code or output.
7. **Validate before declaring done.** Check lesson coverage, Python correctness, expected outputs, conversion/errors, transcript alignment, scene timing, audio sync, visual continuity, and the complete rendered MP4. A successful build alone does not prove the video is correct.
8. **Keep lessons isolated.** Use lesson-specific narration/assets and a clear lesson selector/configuration. Do not accidentally reuse Lesson 1 audio, captions, or title for another lesson.
9. **Preserve existing work.** Do not break or overwrite the known-good Lesson 1 pipeline while building another lesson. Make focused changes, keep the working fallback, and commit meaningful progress.
10. **Be honest and concrete.** Never say a file was created, a commit pushed, a build passed, or an MP4 reviewed unless that action actually succeeded. Include links/commit IDs and list blockers plainly. Do not make the user repeat instructions already written here.

## Required production sequence for every lesson

### Gate 1 — Source and lesson plan
- Identify the requested lesson and fetch its complete canonical source file from the app repository/branch above.
- Extract its learning objectives, all essential examples, exact code, expected outputs, learner tasks, common mistakes, and next-lesson bridge.
- Compare the planned video coverage to the source. Do not change the source lesson itself unless explicitly requested.
- Inspect the existing video template and previous lessons before modifying the pipeline.

### Gate 2 — Narration script
- Write a natural, teachable narration script grounded in the source lesson.
- Include all essential concepts and examples; speak code clearly; add pauses for predictions and practice where useful.
- Mark stage directions separately from words to be spoken.
- Check every spoken claim, code sample, and expected output against the canonical lesson.
- Commit the script and provide its GitHub link. Do not generate visuals based on an unapproved or incomplete script.

### Gate 3 — Narration audio
- Generate narration with the exact approved ElevenLabs v3 voice ID only.
- If the user must run voice generation, provide the exact committed script and concise next action; do not imply the audio exists yet.
- Store audio in a lesson-specific path such as `public/audio/lesson-02/`, with predictable part names and a short README if needed.
- Check audio files exist, play, and cover the full script. Never point Lesson 2 at Lesson 1 assets.

### Gate 4 — Actual transcript and alignment
- Transcribe the actual audio with Whisper/the configured transcription tool.
- Preserve transcript text and word/segment timestamps as production artifacts.
- Compare transcript against the intended script; identify omissions, pronunciation problems, or unexpected wording.
- Derive scene boundaries from actual timestamps and exact phrases. Keep source transcript, alignment data, and generated artifacts traceable.
- Do not make up timestamps or treat planned script timings as measured audio timings.

### Gate 5 — Storyboard and scene design
- Build a connected storyboard from the canonical lesson plus the actual transcript.
- For every scene, specify purpose, narration anchor/phrase, actual time range, visible code or output, animation/action, caption, and transition.
- Keep code and output in sync with what is being said. Include prediction pauses, worked examples, practice, and recap where the source calls for them.
- Avoid unrelated stock visuals or decorative scenes that do not help teach the concept.
- Keep the design consistent with the established PyLearn video style while improving clarity.

### Gate 6 — Implementation and lesson isolation
- Adapt the Remotion/React/TypeScript implementation only as needed for the new lesson.
- Add a clear lesson-specific configuration/selector for title, source, audio, transcript, scenes, and output name.
- Preserve Lesson 1 and its current known-good rendering/alignment path.
- Run type checks and available automated checks before rendering.
- Prefer small, reviewable commits over risky broad rewrites.

### Gate 7 — Render and inspect
- Render the full MP4 with the actual lesson-specific audio.
- Review the **entire video**, not only a still frame or successful CI status.
- Verify opening, every scene transition, code/output correctness, caption legibility, narration sync, pauses, ending, and total audio/video duration.
- Fix discovered issues and rerender. If the full output cannot be inspected, state that limitation instead of claiming final approval.
- Compare a new alignment method with the old fallback if alignment logic changed; retain the old algorithm unless the rendered result is demonstrably better.

### Gate 8 — Closeout
- Commit scripts, audio metadata, transcript, alignment, storyboard, and code changes that are ready to preserve.
- Report: source used, script link, audio status, transcript/alignment status, build result, MP4 link/artifact, what was actually reviewed, known issues, and the single next action if blocked.
- Clearly distinguish **complete**, **in progress**, and **blocked**. A committed script is not a completed video; a successful render is not a reviewed video.

## Repository-specific context

- Video repository: `mohamedalnazeer262-coder/pylearn-video-studio.`, branch `main`.
- Canonical app repository: `mohamedalnazeer262-coder/Pylearn-build260`, branch `ccr-c7f6fdd7-xpzi3g`.
- Canonical Lesson 2 source: `content/python-basics/modules/02-variables-types.md`.
- Lesson 2 narration draft: `docs/LESSON_02_NARRATION_SCRIPT.md`.
- Lesson 2 supporting files include `docs/LESSON_02_VARIABLES_AND_DATA_TYPES_SCRIPT.md`, `docs/LESSON_02_STORYBOARD.json`, and `docs/LESSON_02_PRODUCTION_STATUS.md`.
- Lesson 1 known-good Actions run: [Run #38](https://github.com/mohamedalnazeer262-coder/pylearn-video-studio./actions/runs/39146694927).
- Lesson 1 lesson-specific audio paths: `public/audio/lesson-01/part-01.mp3` and `public/audio/lesson-01/part-02.mp3`.
- The existing workflow is called **Render PyLearn lesson video**.
- Existing implementation uses Remotion, React, and TypeScript. Inspect the current repository before assuming file paths or behavior; this list is orientation, not a substitute for reading the code.

## Reusable task prompt for any lesson

> Create the PyLearn video for **[LESSON NUMBER AND TITLE]**. First read these mandatory instructions in `AGENTS.md`. Read the full canonical lesson from `mohamedalnazeer262-coder/Pylearn-build260` on branch `ccr-c7f6fdd7-xpzi3g`. Follow every production gate in order: source verification, source-aligned narration script, exact approved ElevenLabs v3 Kendrick voice, lesson-specific audio, Whisper transcription of the actual audio, timestamp/phrase-driven alignment, connected storyboard, lesson-isolated Remotion implementation, checks, complete MP4 render, and full-video review. Never invent timestamps, substitute voices, reuse another lesson's audio, skip prerequisites, or claim unverified work is done. Preserve the known-good Lesson 1 path and old alignment algorithm as fallback; adopt a new alignment method only if rendered results are demonstrably better. Commit progress, link the artifacts, state blockers honestly, and give the user only the next action that is actually needed.

## If blocked

Do not quietly skip a gate. State the exact missing input/access, preserve completed work, and stop at that gate. Do not ask the user to repeat requirements already documented here.
