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

**Trigger:** The workflow begins the moment the user says, “We need to generate a video for Lesson X.” Start with Step 1 below. Do not assume narration already exists, and do not start from the rendering stage.

### Phase A — Source lesson to approved script

1. **Identify the exact lesson in the Android app**
   - Use the app repository and the specified lesson number/title to locate the actual lesson content.
   - Read the entire lesson, including its explanations, code examples, expected output, exercises, prerequisites, and lesson-specific learning objectives.
   - Check related lesson files or track metadata only as needed to understand context and the intended sequence.
   - Record the exact source paths and lesson title so the script can be traced back to its source.
   - Never substitute a similarly named lesson, an old video script, or an existing storyboard for the actual app lesson. If the correct source lesson cannot be identified or accessed, stop and ask for the missing source instead of guessing.

2. **Analyze the lesson before writing**
   - Extract the learning objective, learner starting point, key concepts, teaching order, code, expected output, and all essential explanations.
   - Identify what the learner should understand at the end and which ideas need a demonstration.
   - Preserve the app lesson's meaning and essential coverage. Do not add unsupported technical claims, skip important details, or change the lesson sequence just to make a shorter video.
   - Keep video production separate from app editing: do not modify Android app content or app code as part of making the video.

3. **Apply the agreed teacher standard**
   - Use the teacher persona, voice, delivery, pacing, and teaching method defined in “The agreed teacher standard” above.
   - Speak to one learner as a confident, experienced, patient tutor. Explain what the code does, why it works, and what the learner should notice.
   - Teach one concept at a time. Use natural transitions, appropriate pauses, prediction prompts where useful, and step-by-step demonstrations.
   - Keep all essential information from the source lesson. Remove only unnecessary repetition or filler—not teaching explanations.
   - Include a complete opening that introduces the actual lesson and leads into its first concept; do not start with a middle section or assume the learner has heard another video.
   - End with a concise recap of what was taught and a suitable next step, without introducing new concepts.

4. **Create the production-ready script**
   - Write natural spoken narration and a scene-by-scene visual plan together, so each visual action is motivated by the words being spoken.
   - For each scene, specify its purpose, narration, on-screen text, code state, typing action, expected output, captions/key takeaway, and any run/prediction/error/fix action.
   - Show code progressively as it is taught; do not reveal the final code or output before the teacher reaches that point.
   - Check all code and outputs against the app lesson and Python behavior.
   - Preserve the complete instructional sequence and ensure the script covers the whole lesson.
   - Save the script and source references as lesson-specific artifacts in the video repository. Clearly distinguish the approved script from drafts.

5. **Present the script for Runway narration**
   - Give the user the final script in a format that can be copied into Runway, preserving the agreed voice and delivery instructions where supported.
   - If the user's established workflow requires them to generate the audio in Runway, do not pretend to generate that audio yourself or move to video rendering before the audio is available.
   - If a necessary choice is genuinely missing (for example, two conflicting lesson sources or two possible approved scripts), ask one focused question. Otherwise proceed without asking the user to repeat established requirements.

### Phase B — Runway audio to synchronized video

6. **Receive and verify the generated narration**
   - Locate the audio files for the specified lesson in the supplied files or agreed repository.
   - Confirm which files are approved, their order, their actual durations, and their technical readability.
   - Listen to or transcribe the opening and ending of every part; verify that the first spoken words contain the true lesson opening and that the final part contains the complete ending.
   - Check for missing sections, duplicated narration, abrupt cuts, accidental silence, or parts in the wrong order.
   - If there are multiple plausible versions, corrupted files, or a material mismatch with the approved script, stop and ask one focused question or report the specific mismatch. Do not guess which audio is approved.

7. **Transcribe the exact approved audio**
   - Produce a timestamped transcript from the exact audio that will be used in the video.
   - Preserve what was actually spoken. Review uncertain automatic-transcription passages against the audio.
   - Compare the transcript with the approved script and full Android lesson. Flag omitted or altered essential content; do not hide the omission by adjusting visuals.
   - Save the transcript as a lesson-specific artifact.

8. **Build the storyboard and scene manifest from that audio**
   - Derive scene boundaries from actual spoken words, concept changes, demonstrations, and teaching pauses.
   - For every scene, record its ID, topic, narration start/end, transcript anchor, code state, typing events, run action, expected output, captions, and transition.
   - Use exact, distinctive phrases that actually occur in the transcript as anchors. Check all anchors across the full recording.
   - Generate timings from timestamped audio words. Never use guessed timestamps or proportional timing as a substitute.
   - Do not reuse stale cues or an old storyboard just because they already exist. Reuse the visual design template only when appropriate; rebuild the lesson-specific content and timings.

9. **Validate before rendering**
   - Check that the scene sequence starts at the true beginning, follows the full narration, and ends at the actual conclusion.
   - Check scene order, boundaries, overlaps, minimum duration, and anchor confidence.
   - Confirm that typing, code completion, Run action, output, captions, pauses, and transitions occur at the correct narrated moments.
   - Check Python syntax, behavior, and expected output. Ensure every essential concept from the app lesson is represented.
   - If an anchor is low-confidence, inspect the transcript, audio, and cue. Correct the underlying source; never lower a threshold merely to force a successful build.
   - Run type checks and available tests. Do not render until blocking validation errors are resolved.

10. **Render the complete video**
    - Render the full MP4 with the exact approved audio files in the verified order.
    - Confirm the actual MP4 exists, can be opened, has a plausible duration, and includes all intended narration.
    - Keep logs, transcript, scene manifest, synchronization data, and render output traceable to this lesson.

11. **Review the entire rendered video**
    - Watch/listen from the first frame and first spoken word through the final frame and final spoken word.
    - Explicitly verify that the video does not begin partway through the audio, omit the opening, skip a scene, repeat a section, or cut off the ending.
    - Check audio/visual sync, voice continuity, code typing, output timing, captions, transitions, readability, technical correctness, and full lesson coverage.
    - A successful build log or a short preview is not sufficient. If a defect is found, fix its source and render/review again.

12. **Deliver and report honestly**
    - Provide the actual rendered MP4 or a verified link to it, plus the script, transcript, and storyboard/manifest where available.
    - Report source lesson and paths; script status; audio filenames/order/durations; scene count; validation/test result; render result; what was reviewed; and any unresolved issues.
    - Mark the video **complete and approved** only after the actual full render has been reviewed successfully. Otherwise state the exact blocker and the next action.

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
