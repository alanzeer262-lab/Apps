# PyLearn Video Studio

A reusable Remotion + React + TypeScript production template for narrated Python lessons.

## First lesson: Your First Python Program

The visuals are aligned to the actual recorded narration. Before rendering, the workflow transcribes both MP3s with word timestamps, matches scene boundaries, code appearances, output reveals, and intentional error/correction states to spoken phrases. The narration is never sped up, stretched, or proportionally scaled to storyboard timestamps.

### Add the narration files

Copy the two existing narration files into `public/audio/` using these exact names:

- `PyLearn_Video_01_Narration_Part_1.mp3` (173.871 seconds)
- `PyLearn_Video_01_Narration_Part_2.mp3` (237.897 seconds)

They are played consecutively at their measured durations. Do not speed up or stretch the narration. Keep each part's original audio quality.

> The narration files are committed under `public/audio/`. The workflow verifies both files before running alignment.

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

Use Actions → Render PyLearn lesson video → Run workflow. The narration files must already exist under `public/audio/`. The workflow uploads the MP4 as an artifact for seven days.

This repository is separate from the PyLearn Android app.

## First render checklist

1. Confirm both MP3 files are present under `public/audio/`.
2. Open **Actions → Render PyLearn lesson video → Run workflow** and start the workflow from the default branch.
3. Review the **Align visuals to spoken narration** log. It must find every scene anchor and output anchor with acceptable confidence.
4. If alignment fails, update the phrase in `scripts/sync-cues.json` to match the actual recording. Do not add guessed timestamps.
5. When the run finishes, download the `pylearn-first-program` artifact.
6. Review the rendered video at each printed anchor timestamp, especially code changes and output reveals, before publishing.

### If the render fails

- If the narration check fails, one or both MP3 files are missing or their names/paths do not match exactly.
- If the type-check fails, open the failed workflow log and fix the reported TypeScript error before trying again.
- If rendering succeeds but a scene feels early or late, adjust that scene's `start` / `end` values in `src/lesson.ts`. Scene times are scaled from the storyboard's 435-second outline to the measured 411.768-second narration; do not change audio playback speed.
- The MP4 has not been considered verified until the downloaded artifact has been watched from beginning to end.
