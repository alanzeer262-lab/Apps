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
