# PyLearn Video Production Workflow

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

### 3. Validate audio and render
1. Confirm the uploaded audio file, filename, duration, and that it belongs to the correct lesson.
2. Transcribe/align the actual audio and derive timestamps from the recording. Never invent timings or reuse another lesson's audio.
3. Build the storyboard and visual sequence around the actual narration and canonical lesson examples.
4. Render using a lesson-specific configuration/workflow. Preserve the known-good Lesson 1 workflow as a fallback; do not run a Lesson 1 workflow with another lesson's audio.
5. Inspect the rendered video and audio before publishing it to `public/videos/final/`.
6. Update the production status and only then move to the next lesson.

## Lesson completion checklist

- [ ] Canonical lesson source checked
- [ ] Narration script verified
- [ ] Mandatory voice header included; exact approved voice used
- [ ] Correct lesson audio uploaded and validated
- [ ] Timing/transcription based on the actual audio
- [ ] Lesson-specific storyboard and rendering configuration used
- [ ] Final MP4 rendered successfully
- [ ] Video and audio playback inspected
- [ ] Final MP4 stored at `public/videos/final/` with the agreed filename
- [ ] Direct link and status recorded
- [ ] Lesson marked **Complete**

## Current status at time of documenting

### Lesson 1 — First Python Program
Previously reported as rendered successfully. The final MP4 still needs to be located and verified in the permanent final-output folder before this workflow can claim that the output is secured there.

### Lesson 2 — Variables and Data Types
A narration audio file has been uploaded to `public/audio/lesson-02/`. Its contents and duration have not yet been validated, and the final video has not yet been verified. The existing render workflow is Lesson 1-specific; Lesson 2 must use a separate or explicitly parameterized path so it cannot accidentally render with Lesson 1 assets.

## Status reporting rules
Report only verified outcomes. Clearly distinguish **audio uploaded**, **render started**, **render succeeded**, **video inspected**, and **final output published**. Never claim a video is complete until the final MP4 is verified and its final path/link is recorded.
