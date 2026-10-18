# PyLearn Video Studio

A reusable Remotion + React + TypeScript production template for narrated Python lessons.

## First lesson: Your First Python Program

The workflow transcribes the actual recorded narration with Whisper word timestamps. Scene boundaries are generated from transcript sentence boundaries and matched in order to the approved lesson storyboard's own titles, code, outputs, and captions. It does not use the legacy hand-authored `sync-cues.json` as the timing source, and never scales a storyboard timeline proportionally to fit the audio.

### Add the narration files

Upload the Runway-generated MP3 files to the lesson-specific folder using these exact paths:

- `public/audio/lesson-01/part-01.mp3` — first narration segment
- `public/audio/lesson-01/part-02.mp3` — second narration segment

For more segments, continue `part-03.mp3`, `part-04.mp3`, etc. in playback order. Keep only the approved narration for Lesson 1 in this folder.

They are played consecutively at their measured durations. Do not speed up or stretch the narration. Keep each part's original audio quality.

> GitHub Actions runs Whisper (`faster-whisper`) on these files during the workflow. Transcription and timing must happen in GitHub, not as a separate manual/local step.

## Run locally

Requirements: Node.js 20+, npm, Python 3.10+, and pip.

Install dependencies and generate narration timings before opening the preview or rendering:

```bash
npm install
python -m pip install -r scripts/requirements-alignment.txt
npm run align
npm run check
npm run studio
```

Render the lesson after alignment succeeds:

```bash
npm run render
```

Output: `out/pylearn-first-program.mp4`.

## Lesson editing

- `scripts/sync-cues.json`: spoken anchor phrases for scene changes and output reveals.
- `scripts/align_narration.py`: timestamped transcription, fuzzy anchor matching, and timing validation. A missing/low-confidence anchor fails the build rather than using guessed timing.
- `src/generated-alignment.json`: generated timing data consumed by the video. It is regenerated on each workflow run.
- `src/lesson.ts`: scene content plus generated timing data, code, output, prompt, and on-screen teaching captions.
- `src/Video.tsx`: reusable animation and visual layout.
- `src/styles.css`: visual theme.
- `public/audio/`: narration assets.

The scene captions are instructional summaries, not word-for-word subtitles. Scene changes and output reveals are aligned to speech anchors, but code still appears as a complete scene example rather than being typed character-by-character. Review the full render before publishing; the output panel currently illustrates expected results, and the intentional syntax-error demonstration should be checked carefully.

## GitHub Actions

Use Actions → Render PyLearn lesson video → Run workflow. The approved Runway MP3s must exist at `public/audio/lesson-01/part-01.mp3` and `public/audio/lesson-01/part-02.mp3`. GitHub Actions runs Whisper transcription during the workflow. The workflow always uploads the timestamped Whisper transcript and generated scene manifest as the `pylearn-lesson-01-transcript` diagnostic artifact. It uploads the MP4 and scene manifest as `pylearn-lesson-01-render` only after a successful render.

This repository is separate from the PyLearn Android app.

## First render checklist

1. Upload the MP3s to `public/audio/lesson-01/part-01.mp3` and `public/audio/lesson-01/part-02.mp3`.
2. Open **Actions → Render PyLearn lesson video → Run workflow** and start the workflow from the default branch.
3. Review the **Align visuals to spoken narration** log. It must find every scene anchor and output anchor with acceptable confidence.
4. If alignment fails, update the phrase in `scripts/sync-cues.json` to match the actual recording. Do not add guessed timestamps.
5. When the run finishes, download the `pylearn-lesson-01-render` artifact.
6. Review the rendered video at each printed anchor timestamp, especially code changes and output reveals, before publishing.

### If the render fails

- If the narration check fails, one or both MP3 files are missing or their names/paths do not match exactly.
- If the type-check fails, open the failed workflow log and fix the reported TypeScript error before trying again.
- If rendering succeeds but a scene feels early or late, adjust that scene's `start` / `end` values in `src/lesson.ts`. Scene boundaries are generated from the transcript's measured word timestamps; do not edit guessed times or change audio playback speed.
- The MP4 has not been considered verified until the downloaded artifact has been watched from beginning to end.


## Required pre-frame production gate

Follow `docs/VIDEO_PRODUCTION_STANDARD.md` for every lesson. Before the frame-making tool runs, prepare and approve a timestamped transcript from the approved narration and a frame-production manifest specifying ordered beats, spoken anchors, code/output states, actions, captions, and transitions. Review the generated frames before rendering the MP4.

The canonical lesson source is in the separate PyLearn Android app repository. Example: `content/python-basics/modules/01-first-program.md`; verify and record the exact source repository, branch/commit, and path for each lesson rather than assuming this path is universal.

Keep one approved visual style consistent within a course. A new course such as Data Analysis may have a different style approved at course level, then reuse it consistently. Run #25 is the approved technical baseline for the current course.
