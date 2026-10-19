# File and Production Workflow

1. Upload new, unclassified audio to `incoming/audio/` with its original filename.
2. Inspect/transcribe each recording and identify whether it is a lesson or practice and which track/unit it belongs to. Do not infer from duration alone.
3. Move/copy each verified recording to its permanent destination:
   - `tracks/track-01-python-basics/<unit>/lesson/audio/lesson.mp3`
   - `tracks/track-01-python-basics/<unit>/practice/audio/practice.mp3`
   - or the corresponding `tracks/track-02-python-foundations/` path.
4. Put narration source in the same lesson/practice folder as `script.md`; put verified transcript/timestamps in `transcript/`; put supporting visual assets in `assets/`.
5. Before rendering, read `AGENTS.md`, the canonical lesson source, and the existing scripts/workflow. Follow the current validated production order; actual audio transcript and word timestamps drive timing.
6. Preserve original audio quality. Never invent transcript text, timestamps, cue matches, or claim a render was verified unless it was inspected.
7. Update `docs/project-status.md` and `FILE_MAP.md` whenever a production milestone or path convention changes.
8. Keep approved final videos in `public/videos/final/` and temporary renders in `public/videos/previews/`.
9. Do not change the current Lesson 1 paths or rendering pipeline until a deliberate migration is implemented and tested.
