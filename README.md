# PyLearn Video Studio

A reusable Remotion + React + TypeScript workspace for producing narrated, animated Python lessons.

## What this starter includes

- 1920×1080 educational video composition
- Animated title, Python code panel, output panel, narration-ready audio track, and timed captions
- One lesson definition file to edit for each new video
- Remotion Studio preview and MP4 rendering commands
- GitHub Actions workflow for rendering a video artifact

## Requirements

- Node.js 20 or newer
- npm

## Run locally

```bash
npm install
npm run studio
```

Render the sample lesson:

```bash
npm run render
```

The rendered file is written to `out/pylearn-first-program.mp4`.

## Customize a lesson

Edit `src/lesson.ts`. Set the title, subtitle, code lines, output lines, narration file path, and caption timings. Put narration audio files in `public/audio/` and set `audioSrc` to a path such as `/audio/lesson-01.mp3`. If no audio is supplied, the composition still renders as a silent visual preview.

Caption times are measured in seconds from the beginning of the video. The default sample is a short visual demonstration; replace the sample narration/captions with the approved lesson script before publishing.

## Project structure

- `src/lesson.ts` — lesson content and timings
- `src/Video.tsx` — reusable animated composition
- `src/Root.tsx` — composition registration
- `public/audio/` — narration audio files
- `.github/workflows/render-video.yml` — manual GitHub Actions render

## Important

This repository is the video-production project and is separate from the PyLearn Android app. Rendering is not considered verified until the workflow completes and the MP4 artifact is reviewed.
