# PyLearn Video Production Workflow

## Explicit stage ownership — source of truth

The word **Me** below means the AI assistant working in this repository. **You** means the user. Do not swap these responsibilities or ask the user to do the assistant's implementation work.

| Stage | Who does it | Deliverable / handoff |
|---|---|---|
| Validate audio and generate transcript with timestamps | Automated workflow | Verified audio duration, transcript text, and word/segment timestamps as a downloadable artifact |
| Create the scene splits, code screens, and visual timing | Me (assistant) | Lesson-specific scene timeline/storyboard grounded in the real transcript and canonical lesson |
| Prepare the Lesson 2 video render setup | Me (assistant) | Lesson-isolated Remotion composition/configuration and render workflow, preserving Lesson 1 |
| Render and inspect the complete MP4 | Me (assistant) | Full rendered MP4; technical and visual/audio checks; fix defects and rerender as needed |
| Review the finished video | You (user) | Final human review and feedback/approval |

**Important handoff:** The automated transcript is an input, not the finished storyboard. Once the validation workflow succeeds, I must retrieve and inspect its artifact, create the scene splits/code screens/timing, implement the Lesson 2 render setup, render the full MP4, and inspect it before asking you to review the finished video. You should not need to design scenes, write rendering code, or run the render yourself.

## Purpose
Produce the PyLearn course videos in lesson order. Each lesson must be finished, rendered, checked, and placed in the final-output folder before the next lesson is treated as complete.

## Permanent final-output folder
All approved final MP4 files belong in:

`public/videos/final/`

Use stable, descriptive filenames:

- `lesson-01-first-python-program.mp4`
- `lesson-02-variables-and-data-types.mp4`
- `lesson-03-<lesson-title>.mp4`
- Continue the same naming pattern for later lessons.

Keep final MP4s separate from narration audio, scripts, storyboards, intermediate renders, and other production assets. Do not treat an audio upload or a successful workflow start as a finished video.

## Required sequential workflow

### 1. Complete and secure the current lesson
1. Locate the actual rendered MP4 for the lesson.
2. Confirm the file exists and can be opened/played; inspect the output for obvious rendering, audio, timing, and visual problems.
3. Place or publish the verified MP4 in `public/videos/final/` using the agreed filename.
4. Record its repository path and a direct link in the production status document.
5. Mark the lesson **Complete** only after these checks pass.

### 2. Prepare the next lesson
1. Read the canonical lesson source and current production instructions.
2. Prepare or verify the narration script against the source.
3. Put the mandatory approved voice header at the top of every narration script. Use the exact approved Kendrick voice, ElevenLabs v3, and the user's exact voice ID; never invent an ID or substitute a voice. Production notes in brackets must not be read aloud.
4. Prepare that lesson's audio folder and document exact expected filenames.
5. Give the user the script and exact audio paths so they can generate the narration in Runway and upload it.

### 3. Validate, design, implement, render, inspect
1. The automated workflow validates the uploaded audio and generates the transcript with timestamps.
2. I retrieve and inspect the artifact, compare the transcript with the canonical script, and note recognition errors without changing the recorded audio.
3. I create the scene splits, code screens, visual sequence, and timing based on the real recording and canonical examples.
4. I implement a lesson-specific rendering setup. Preserve the known-good Lesson 1 workflow; never run a Lesson 1 workflow with another lesson's audio.
5. I render the full MP4, inspect the complete output for code correctness, timing, text clipping, audio sync, and ending, and fix/rerender any defects.
6. I publish the verified MP4 under `public/videos/final/`, update the status, and then hand the finished video to you for human review.
7. You review the finished video and provide feedback or approval. Do not transfer implementation or rendering tasks to the user.

## Lesson completion checklist

- [ ] Canonical lesson source checked
- [ ] Narration script verified
- [ ] Mandatory voice header included; exact approved voice used
- [ ] Correct lesson audio uploaded and validated
- [ ] Automated transcript and actual timestamps generated
- [ ] Assistant created lesson-specific scene splits, code screens, and visual timing
- [ ] Assistant prepared lesson-specific rendering configuration
- [ ] Full MP4 rendered successfully by assistant
- [ ] Assistant inspected full video and audio; defects fixed and rerendered if needed
- [ ] Final MP4 stored at `public/videos/final/` with the agreed filename
- [ ] Direct link and status recorded
- [ ] Finished video handed to user for review
- [ ] User review/approval recorded before calling the lesson approved

## Status reporting rules
Report only verified outcomes. Clearly distinguish **audio uploaded**, **transcript generated**, **storyboard prepared**, **render setup prepared**, **render succeeded**, **assistant inspection passed**, **final output published**, and **user review/approval**. Never claim a video is complete until the final MP4 is verified and its final path/link is recorded.

## Mandatory full-video quality review gate (every lesson)

This release gate is required for every lesson. A successful render or valid MP4 does not prove the lesson is correct.

### Transcript and coverage
- [ ] Compare the actual audio transcript and word/segment timestamps against the canonical source and narration script.
- [ ] Confirm no missing or duplicated spoken sections, cut-off sentences, or unexplained audio gaps.
- [ ] Anchor scene boundaries to actual spoken phrases and timestamps.

### Scene-by-scene accuracy
- [ ] Track each scene's narration anchor, time range, code, output, caption, and transition.
- [ ] Whenever narration changes a variable, value, example, or program state, verify the matching visual state appears at the right time.
- [ ] Verify Python syntax and expected outputs, including types, conversions, errors, predictions, and practice exercises.
- [ ] Preserve learner pauses and do not reveal answers before the narration does.

### Inspect the complete rendered MP4
- [ ] Inspect the entire video from beginning to end; a contact sheet or sparse screenshots alone are insufficient.
- [ ] Inspect every scene transition and meaningful code/output state, with denser checks around suspected defects.
- [ ] Check missing states, stale examples, blank or repeated frames, flicker, clipping, readability, and layout continuity.
- [ ] Verify audio continuity, narration/visual alignment, opening, recap, ending, and total duration.

### Defect log and rerender
- [ ] Log each defect with timestamp, expected state, actual state, and root cause.
- [ ] Fix the underlying storyboard/configuration/renderer issue; do not shift timestamps randomly or patch only the first reported example.
- [ ] Rerender after any content or timing change and repeat relevant checks. After broad changes, recheck the entire lesson.
- [ ] Record the render run/commit and what was actually inspected. If full inspection is not possible, disclose the limitation and do not mark review as passed.

### Release gate
- [ ] All checks pass, or any exception is explicitly documented and approved.
- [ ] Publish the verified MP4 to `public/videos/final/` and update the production status.
- [ ] Record assistant inspection separately from user review/approval. Do not hand off until assistant inspection passes.
