# Repository instructions for AI coding agents

For all PyLearn educational-video work, follow `docs/VIDEO_PRODUCTION_STANDARD.md` as the required production process.

Critical requirements:
- Treat the exact approved narration audio as the source of truth.
- Never patch old cue phrases one error at a time as a substitute for rebuilding a mismatched storyboard.
- Transcribe the current audio, derive scenes and anchors from that transcript, then generate and validate timings.
- Never guess timestamps or weaken confidence thresholds to bypass failures.
- Keep scene content, code, output, and timing tied to the current recording.
- Do not claim a video is complete until the MP4 has been rendered and its audio/visual synchronization has been checked.
- Reuse the approved visual template only after it has been verified; regenerate lesson-specific scenes for every new narration.
- Do not ask the user to repeat this standard. Ask only when an essential input or decision is genuinely missing.
