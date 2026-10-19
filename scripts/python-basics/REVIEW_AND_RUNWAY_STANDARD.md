# Python Basics Script Review and Runway Standard

Status: working production standard for the 20-script Python Basics pack.
Canonical source branch: `Pylearn-build260` / `ccr-c7f6fdd7-xpzi3g`.
Script directory: `scripts/python-basics/`.

## Mandatory voice lock
- Voice: Kendrick.
- Model: ElevenLabs v3.
- Use the exact Kendrick voice ID previously approved by the user.
- No substitute, preset, or alternate voice.
- Do not guess or invent the voice ID.
- Keep one consistent voice across a lesson and across the series.

## Lessons learned from video production
1. A video can be temporally aligned and still be wrong if the required visual state is missing. Every scene transition must change the actual code, output, diagram, or highlighted entity to what the narration is discussing.
2. A named entity introduced in narration must visibly appear when it is introduced. If narration moves from Ada to Sam, the screen must visibly change from Ada to Sam; do not leave Ada's record on screen.
3. A new code line must appear before or as it is explained, not several lines early. Avoid displaying a future answer while the learner is still being asked to predict it.
4. Do not create timing from estimated script duration. Final visual timing comes from the generated audio transcript and word/phrase timestamps.
5. Check the entire video, not only the opening, a few sampled frames, or the render status. Review scene coverage, code correctness, visual continuity, audio continuity, and end-of-video behavior.
6. A successful render is not proof of a correct lesson. Render success, media integrity, transcript/visual coverage, and pedagogical correctness are separate checks.
7. Preserve the reading lesson's scope and sequence. Video supplements it; do not quietly replace or edit the app lesson.
8. Narration must sound natural aloud. Speak symbols in plain English at first introduction, explain code before asking the learner to predict, leave a real silent pause for predictions, then run the code and explain the result.
9. Use short connected examples. Avoid jumping between unrelated examples or introducing a person/value in speech that does not appear on screen.
10. Never invent a code output, rule, capstone requirement, or feature. Verify every stated output with the Python semantics and canonical source.

## Script quality gate — before Runway
For each lesson:
- [ ] Confirm the exact canonical source module and learning outcomes.
- [ ] Compare every concept in the source with the script; no required concept silently omitted.
- [ ] Ensure no concepts are pulled forward from later modules unless the source explicitly requires them.
- [ ] Run through every code example mentally or in Python; verify output, indentation, variable names, types, and boundary behavior.
- [ ] Make narration conversational, concise, and speakable; remove repetitive filler and awkward transitions.
- [ ] Explain new terms before relying on them.
- [ ] Include a useful prediction moment and a genuine silent hold; do not speak during the hold.
- [ ] Specify exactly what is visible at every point: code lines, active line, output, labels, and changes in the screen.
- [ ] Ensure the spoken entity/value and visible entity/value match at every scene.
- [ ] End with a concise recap and a transition that matches the next canonical module.
- [ ] Keep production directions outside the text sent to text-to-speech. The user should send only narration text to Runway, while using the visual plan separately.
- [ ] Recheck voice lock: Kendrick / ElevenLabs v3 / exact approved ID / no substitution.

## Full video quality gate — after render
- [ ] Validate file duration, resolution, frame rate, audio stream, and playable MP4.
- [ ] Review from first frame to last frame, not only sampled frames.
- [ ] Compare narration transcript/timestamps against the screen content throughout.
- [ ] Confirm every spoken name, value, code line, and output appears at the right time.
- [ ] Check that no required frame/state is missing, held over from the previous scene, or revealed too early.
- [ ] Verify code is legible on mobile and does not clip.
- [ ] Check silent prediction holds and no narration is cut off.
- [ ] Confirm final recap, next-lesson bridge, and end card.
- [ ] Fix all defects and rerender before asking the user to review.
- [ ] Do not publish or move an unapproved new video to a permanent final location without the user's approval.

## Source accuracy notes
- The canonical lesson files are the authority. If a draft disagrees, revise the draft, not the lesson.
- The current module sequence is Modules 1–19; the Mini Gradebook is a separate capstone.
- The existing Lesson 1/2 video-production defects should be used as regression tests, not repeated.
- The script pack is not ready to send to Runway until each lesson's individual source audit is complete.
