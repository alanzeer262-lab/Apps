# PyLearn Video Studio

A reusable Remotion + React + TypeScript production template for narrated Python lessons.

## First lesson: Your First Python Program

The scene plan follows the approved 10-scene lesson script, preserving its continuous editor-and-output teaching style. The video is approximately 6 minutes 52 seconds because the two supplied narration MP3s total 411.768 seconds. The script's 7:15 estimate includes pauses and holds, so timings are scaled to the recorded narration rather than stretching the audio.

### Add the narration files

Copy the two existing narration files into `public/audio/` using these exact names:

- `PyLearn_Video_01_Narration_Part_1.mp3` (173.871 seconds)
- `PyLearn_Video_01_Narration_Part_2.mp3` (237.897 seconds)

They are played consecutively at their measured durations. Do not speed up or stretch the narration. Keep each part's original audio quality.

> The audio files are not included in this repository yet. Add them before rendering; otherwise Remotion cannot resolve the audio paths.

## Run locally

Requirements: Node.js 20+ and npm.

```bash
npm install
npm run studio
```

Render the lesson:

```bash
npm run render
```

Output: `out/pylearn-first-program.mp4`.

## Lesson editing

- `src/lesson.ts`: scene timings, code, output, prompt, and on-screen teaching captions.
- `src/Video.tsx`: reusable animation and visual layout.
- `src/styles.css`: visual theme.
- `public/audio/`: narration assets.

The scene captions are instructional on-screen summaries, not word-for-word subtitles. Before publishing, review the full render for scene/audio synchronization and adjust scene timings if needed. The output panel illustrates expected results from the script; the intentional syntax-error demonstration is described in the storyboard but should show genuine interpreter output in a production capture.

## GitHub Actions

Use Actions → Render PyLearn lesson video → Run workflow. The narration files must already exist under `public/audio/`. The workflow uploads the MP4 as an artifact for seven days.

This repository is separate from the PyLearn Android app.

## First render checklist

1. Download the narration ZIP from the project conversation and extract it on your device.
2. In this repository, open the `public/audio` folder. If it does not exist in the GitHub file view, create the folder by uploading a file into that path.
3. Upload both MP3 files with these exact names (capitalization and underscores matter):
   - `PyLearn_Video_01_Narration_Part_1.mp3`
   - `PyLearn_Video_01_Narration_Part_2.mp3`
4. Confirm the files appear at `public/audio/PyLearn_Video_01_Narration_Part_1.mp3` and `public/audio/PyLearn_Video_01_Narration_Part_2.mp3` in the repository.
5. Open **Actions → Render PyLearn lesson video → Run workflow** and start the workflow from the default branch.
6. When the run finishes, open the run and download the `pylearn-first-program` artifact. It contains the rendered MP4.
7. Watch the whole video once before publishing. Check that the audio is present, scene changes follow the narration, and code/output examples are readable.

### If the render fails

- If the narration check fails, one or both MP3 files are missing or their names/paths do not match exactly.
- If the type-check fails, open the failed workflow log and fix the reported TypeScript error before trying again.
- If rendering succeeds but a scene feels early or late, adjust that scene's `start` / `end` values in `src/lesson.ts`. Scene times are scaled from the storyboard's 435-second outline to the measured 411.768-second narration; do not change audio playback speed.
- The MP4 has not been considered verified until the downloaded artifact has been watched from beginning to end.
