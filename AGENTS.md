# PyLearn Video Studio — Mandatory Agent Instructions

These instructions apply to **every AI agent, coding agent, or assistant** working in this repository. Read this file before changing files, creating a lesson, generating audio, or rendering a video. The purpose is to prevent the user from having to repeat the workflow and constraints.

## Mission

Create accurate, polished PyLearn teaching videos from the **canonical lesson content** in the PyLearn app repository. Work end-to-end where tools and required assets are available, preserve progress in GitHub, and report honestly what is and is not complete.

## Explicit production ownership — mandatory

Use this ownership table for every lesson. **“Me” means the AI assistant; “You” means the user.** This division is intentional and overrides any vague wording elsewhere in these instructions.

| Stage | Owner |
|---|---|
| Validate audio and generate transcript with timestamps | Automated workflow |
| Create scene splits, code screens, and visual timing | AI assistant |
| Prepare the lesson-specific video render setup | AI assistant |
| Render and inspect the complete MP4 | AI assistant |
| Review the finished video and provide feedback/approval | User |

After the automated audio-validation workflow succeeds, the assistant must retrieve and inspect its transcript artifact, build the scene plan, implement the lesson-specific render setup, render the complete MP4, inspect it, fix defects, and publish the verified output before asking the user to review. Do not ask the user to build scenes, implement rendering code, or run the render. The user's final responsibility is reviewing the finished video. Keep this ownership table consistent in the production workflow and each lesson status document.

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



## Mandatory voice header in every narration script

Every lesson narration script Markdown file must begin with a clearly visible voice-settings block before the lesson title or narration. This is mandatory, not optional, and must be included in every script part/chunk if the script is split across multiple files. Use this exact standard:

> **MANDATORY VOICE SETTINGS — DO NOT CHANGE**
> - **Voice name:** Kendrick
> - **Model:** ElevenLabs v3
> - **Voice ID:** Use the exact approved custom Kendrick voice ID supplied/confirmed by the user. Never invent, guess, or silently omit it from a Runway handoff when the ID is available in the project context.
> - **Voice substitution:** Not allowed. Do not replace Kendrick with another voice or a preset.
> - **Consistency:** Keep the same voice identity throughout every part of the lesson.
> - **Read-aloud rule:** Speak only narration text. Do not read production notes or instructions in square brackets aloud.

The script author must verify this header before committing or sharing any script. If the exact voice ID is not available in repository/context, keep the required name and model explicit and flag the missing ID for confirmation; do not fabricate an ID. The production status and handoff README must repeat the same voice requirement where relevant. Update existing script files to include this header when touching them, and include it automatically in all newly created narration scripts and script chunks.

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


## Standard behavior when the user says “start production”

This phrase starts a standard, repeatable **script-preparation phase**. Do not jump to audio generation, rendering, or blockers before delivering the script.

1. Read this file and the complete canonical lesson source.
2. Check the existing script if one exists. Verify it against the source and revise only if needed; do not make a duplicate script unnecessarily.
3. Prepare/verify the exact lesson audio folder in the video repo. For Lesson 02, use `public/audio/lesson-02/`. Include a README that tells the user exactly where to place the Runway-generated MP3 part files and what filenames the pipeline expects.
4. Produce or verify the final narration script. Keep stage directions separate from spoken words. Ensure the script is suitable to paste into Runway, splitting it into clearly ordered chunks only if required by the tool's character limit. Never replace the approved voice with a preset voice.
5. Commit any needed script/folder README changes.
6. Give the user the script and direct GitHub link, state the exact audio filenames/folder, and stop for the user's Runway audio. **Do not ask the user to regenerate the process instructions or repeat the voice/workflow requirements.**
7. When the user later places or uploads the audio, resume at audio validation/transcription. Transcribe the actual audio, align to real timestamps, then storyboard, implement, render, and inspect.

The intended handoff is: **Assistant prepares source-verified script and folder → user sends script to Runway using the exact approved voice → user places returned audio in the documented lesson folder → assistant resumes production from the audio gate.** This handoff is normal workflow, not a production failure or an unexpected blocker.

## If blocked

Do not quietly skip a gate. State the exact missing input/access, preserve completed work, and stop at that gate. Do not ask the user to repeat requirements already documented here.


## Mandatory full-video quality review checklist

This checklist is part of the production process for **every lesson**. It is required before any MP4 is marked ready or handed to the user. A successful render/build or valid MP4 file is not evidence that the lesson is pedagogically correct.

### A. Transcript and coverage
- [ ] Compare the actual audio transcript and word/segment timestamps against the canonical lesson and approved narration script.
- [ ] Confirm every intended spoken section is present; identify omissions, duplicated narration, cut-off sentences, and unexplained gaps.
- [ ] Verify scene boundaries against the actual phrase being spoken, not estimated script timings.

### B. Scene-by-scene teaching accuracy
- [ ] For every scene, record its narration anchor, start/end time, visible code, output, caption, and transition.
- [ ] Check each example change explicitly: when the narrator changes a value/name/example, the corresponding visual state must also change.
- [ ] Verify code is syntactically valid and matches the explanation; execute or independently calculate expected outputs where practical.
- [ ] Confirm type labels, conversions, errors, predictions, practice tasks, and answers are shown at the right point and are accurate.
- [ ] Preserve intentional prediction/practice pauses; do not reveal an answer before the narration does.

### C. Full rendered video inspection
- [ ] Inspect the entire rendered MP4 from beginning to end, not just a contact sheet or selected screenshots.
- [ ] Inspect every scene boundary and each meaningful code/output state; use denser frame sampling around transitions or suspected defects.
- [ ] Check for missing visual states, stale/repeated examples, blank frames, dropped/held frames, flicker, unexpected layout changes, clipping, and unreadable text.
- [ ] Check narration/audio is audible and continuous, and visuals are aligned to the spoken words throughout.
- [ ] Confirm opening, recap, ending/end card, and total audio/video duration are correct.

### D. Fix, rerender, and prove the fix
- [ ] Log each defect with timestamp, expected visual/audio state, actual state, and root cause.
- [ ] Fix the underlying storyboard/configuration/renderer problem; do not patch timings randomly or only correct the first reported example.
- [ ] Rerender after any content/timing change and repeat the relevant checks. Recheck the whole lesson after broad changes.
- [ ] Record the exact render run/commit and evidence of the inspected output. If any section cannot be inspected, state the limitation and do not mark the video review as passed.

### E. Release gate
- [ ] All checklist items pass or any exception is explicitly documented and approved.
- [ ] Publish the verified MP4 to `public/videos/final/` and update the production status.
- [ ] Only then hand the video to the user for their final review. Keep assistant inspection and user approval as separate statuses.
