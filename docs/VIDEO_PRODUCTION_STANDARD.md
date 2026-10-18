# PyLearn Video Production Standard

**Purpose:** Produce accurate, synchronized educational videos without requiring the user to repeat the workflow or quality requirements for every lesson.

## Non-negotiable rule

The approved narration audio is the source of truth. Never force old scene cues, an old storyboard, or guessed timestamps onto a new recording. Do not call a video complete until the rendered MP4 has been checked.


## The agreed teacher standard — preserve these details

This section is intentional and must not be reduced to generic words such as “clear” or “engaging.” Apply it to every PyLearn video script, narration, scene, and review.

### Teacher persona and voice
- Keep the currently approved voice. Do not change the voice identity unless the user explicitly requests it.
- Voice profile: male voice, neutral accent, warm teaching style, natural and human-like delivery, with clear pronunciation of Python terms and deliberate pauses.
- Teacher personality: confident, energetic, experienced, composed, and reassuring. Never sound weak, shy, robotic, bored, or uncertain; never shout or rush.
- Overall pacing is slightly faster and natural, but speed must follow meaning. Slow down for a new or difficult concept; use a natural pace for familiar details. Do not apply one fixed speed to every sentence.
- Emphasize important words and ideas naturally. Use purposeful pauses after questions, code, execution, output, and mistakes so the learner can think and observe.
- Tune pauses and pace to sentence meaning and punctuation. Do not cut off the beginning or end of spoken lines, or trim meaningful silence that supports learning.

### Teaching method
- Teach like a patient personal tutor speaking directly to one learner—not like a narrator reading documentation and not like an information dump.
- Teach one idea at a time. Explain what the code means, why it is used, and what the learner should notice.
- Preserve the source lesson’s technical meaning, examples, learning sequence, and all essential information. Do not silently omit, replace, or invent lesson content.
- The video complements the Android app lesson; it does not replace or rewrite the app lesson. Video-production work must not change the app, repository's app code, or existing reading lessons.
- Start by establishing the lesson's real learning objective and connect the opening to the first concept. Do not begin midway through an explanation, code example, or narration.
- Use prediction pauses where appropriate: invite the learner to think about what the code will do before revealing the result. Then run the code and explain the actual output.
- Treat mistakes as normal and teachable. When the lesson includes an error, show the relevant error, explain why it happened, and demonstrate the correction in sequence. Do not invent an error merely to make a scene dramatic.
- End with a concise recap of the ideas actually taught and an encouraging next step that fits the lesson. Do not introduce new technical content in the recap.

### Script construction requirements
For each lesson, read the exact Android lesson content before writing the script. Extract the learning objective, prerequisites, concepts, code, expected output, explanations, and sequence.
Then write a production-ready script with:
1. Learning objective and a complete opening.
2. Teacher narration in spoken, natural language.
3. Scene-by-scene visual directions that correspond to the narration.
4. Code displayed and typed progressively at the moment it is discussed.
5. Execution action and the correct output at the moment the teacher refers to them.
6. Prediction pauses and purposeful observation time where useful.
7. Transitions that connect ideas instead of jumping between unrelated scenes.
8. A recap that reinforces the lesson without changing its meaning.

Narration and visuals must describe the same thing at the same time. Do not show the final code or output before the narration's teaching sequence calls for it. Do not let visuals advance ahead of the spoken explanation or remain on unrelated material. Preserve all meaningful lesson content while removing only unnecessary repetition or filler; never shorten by deleting important explanations.

### Audio generation and approval
- The user supplies the script to Runway; Runway-generated audio is the narration asset used for video production.
- The script must be approved/usable before audio generation. Once audio exists, inspect the exact audio files and their order, transcribe them, and build scene timing from the actual recording.
- Do not assume audio filenames, file order, or a previous script describe the audio correctly. Check the first spoken words and the last spoken words of every part.
- If narration is split across files, join or sequence parts in the intended order with no missing opening, duplicated section, accidental gap, or abrupt cut. Confirm continuity across each join.
- If the audio differs materially from the approved script or does not cover the full source lesson, flag it; do not silently adapt the visuals to hide missing teaching content.

### Mandatory start-to-finish checks
Before approving a video:
- Confirm the first frame and first spoken words begin at the true beginning of the lesson.
- Confirm the opening objective/introduction is present and no initial narration is skipped.
- Confirm all audio parts are in the intended order and the final spoken section is present.
- Watch/listen to the complete rendered video, not only a preview or successful build log.
- Check synchronization of speech, code typing, pauses, Run action, output, captions, and transitions.
- Check that the technical content and output are correct and that every essential concept from the app lesson is covered.
- Check the final scene and ending for abrupt truncation.
- Record any unresolved issue explicitly. A successful workflow run alone does not mean the video is approved.

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
