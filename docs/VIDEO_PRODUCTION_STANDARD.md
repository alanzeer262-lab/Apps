# PyLearn Video Production Standard

**Purpose:** Produce accurate, synchronized educational videos without requiring the user to repeat the workflow or quality requirements for every lesson.

## Non-negotiable rule

The approved narration audio is the source of truth. Never force old scene cues, an old storyboard, or guessed timestamps onto a new recording. Do not call a video complete until the rendered MP4 has been checked.

## Standard workflow for every lesson

### 1. Inspect the inputs
- Identify the exact approved audio file(s), their order, and their actual durations.
- Inspect the lesson script, code examples, expected outputs, and any supplied assets.
- Do not assume narration matches a previous script or storyboard.
- If audio is missing, corrupt, ambiguous, or multiple versions exist without an obvious approved version, stop and ask one focused question.

### 2. Transcribe the actual audio
- Generate a timestamped transcript from the exact audio files that will be rendered.
- Preserve the actual spoken wording; do not silently rewrite it to fit existing cues.
- Treat automatic transcription as a draft. Inspect low-confidence or unclear passages before using them to drive scenes.
- Keep a transcript artifact with the lesson so decisions are traceable.

### 3. Build the storyboard from the transcript
- Create scene boundaries from the actual narration's topic changes and teaching beats.
- For each scene, define: scene ID, title/topic, narration start/end, on-screen code, expected output, captions/key takeaway, and any typing/run/error/fix events.
- Use exact phrases from the transcript as anchors. Anchors must occur in the recording and be distinct enough to identify the intended moment.
- Ensure the code and output shown are technically correct and match what is being explained.
- Do not retain an old scene merely because it already exists in the codebase. Reuse only content that demonstrably matches the current narration.
- If the narration and lesson content conflict, flag the conflict and resolve it before rendering; never invent a timestamp or silently change the lesson.

### 4. Synchronize and validate
- Derive timestamps from audio/transcript word timing, not proportional scaling or guessed values.
- Validate scene order, non-overlapping boundaries, minimum scene duration, and that every code/output/error/fix event falls inside the right scene.
- Check anchors across the whole transcript, not only the first failed anchor.
- A low-confidence anchor must trigger review of the transcript/storyboard and correction of the source cue. Do not lower the confidence threshold just to make a build pass.
- Prefer a transcript-driven scene manifest as the single source of truth, so the storyboard and timing cannot drift independently.

### 5. Render and quality-check
- Run type checks and all available tests before rendering.
- Render the full MP4 with the approved audio.
- Verify the actual output exists, has a plausible duration, includes all audio tracks, and plays from beginning to end.
- Review scene transitions, code typing, outputs, captions, audio/visual synchronization, and the ending. Check both the start and the later portions; do not infer success from a successful build alone.
- If any check fails, fix the underlying source and rerun. Never report a video as finished if the render or review did not happen.
- Preserve logs, transcript, storyboard/manifest, and the final MP4 or a clear artifact link.

## Reusable template and design system

Once Lesson 1 is verified and approved, lock its reusable visual system: PyLearn branding, typography, colors, editor/output panels, typing animation, captions, transitions, and scene layouts. Future lessons should reuse the visual template, but must generate their own transcript-derived scenes and timings. Reusing the template must never mean reusing old narration cues.

## Required lesson deliverables

- Exact source audio file list and durations
- Timestamped transcript
- Transcript-derived storyboard/scene manifest
- Validated synchronization data
- Rendered MP4
- Build/render result and quality-check status

## Completion report format

Report these items clearly:
1. **Audio used:** filenames and total duration
2. **Scenes:** number created from the current recording
3. **Validation:** transcript anchors, code/output timing, and type checks
4. **Render:** success/failure and link to the actual artifact, if available
5. **Review:** what was checked and any known issues
6. **Status:** complete only after successful render and review; otherwise identify the exact blocker and next action

## User interaction defaults

- Apply this standard automatically to every PyLearn lesson/video task in this repository.
- Do not ask the user to repeat these production rules.
- Ask only for genuinely missing decisions or ambiguous source assets.
- Make the smallest safe repository changes, preserve working assets, and report what was actually changed and verified.
