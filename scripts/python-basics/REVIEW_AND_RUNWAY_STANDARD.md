# Python Basics Script Review and Runway Standard

Status: active production standard for the 20-script Python Basics pack.
Canonical source branch: `Pylearn-build260` / `ccr-c7f6fdd7-xpzi3g`.
Script directory: `scripts/python-basics/`.

## Learning design: video teaches; PyLearn assesses

**The learner must do the practice in the app. Watching the video is not completion.**

- **Concept modules 1–11:** teach the concept with a small connected example; ask a prediction question; hold silence long enough to think; then reveal and explain the result. End by directing the learner to the corresponding PyLearn lesson/exercise. Do not replace the app exercise with a video-only quiz.
- **Project modules 12–19:** state the project goal and exact contract; teach the key ideas and demonstrate only a small, representative step; leave meaningful implementation to the learner. Do not reveal the full function body, complete project output, or every step needed to copy the answer. End with the exact PyLearn project title and an instruction to implement and test it in the app.
- **Capstone:** orient the learner to the data and the five milestone goals. Do not reveal completed solutions or final answers for all five milestones. Learners solve, submit, and receive app feedback for each milestone.
- The app owns code entry, tests, hints, grading, submissions, and completion state. Video cannot verify that the learner practiced.
- Use only requirements and behavior defined by the canonical app lesson. Do not invent edge-case contracts, duplicate policies, outputs, or grading rules.

## Mandatory voice lock
- Voice: Kendrick.
- Model: ElevenLabs v3.
- Use the exact Kendrick voice ID previously approved by the user.
- No substitute, preset, or alternate voice.
- Do not guess or invent the voice ID.
- Keep one consistent voice across a lesson and across the series.

## Lessons learned from video production
1. Correct audio timing does not fix a missing visual state. Every scene must show the code, output, diagram, or entity being discussed.
2. Every named entity introduced in narration must visibly appear at the right time.
3. Do not reveal future code or answers before the narration reaches them.
4. Final visual timing comes from generated audio transcript timestamps, not estimates from a draft.
5. Review the whole video from first frame to last at normal speed.
6. Render success is not proof of correctness. Media integrity, visual coverage, and pedagogical correctness are separate checks.
7. Preserve the app lesson's scope and sequence.
8. Narration should be conversational, speak symbols plainly, and include real silent prediction holds.
9. Use connected examples; keep spoken and visible values aligned.
10. Independently verify code semantics and outputs against the canonical source.
11. Make code legible on a phone; avoid showing more code than the learner can follow.
12. The video must direct learners back to the app for actual practice and submission.

## Script quality gate — before Runway
- [ ] Confirm exact canonical source module and outcomes.
- [ ] Compare concepts and exact function contracts against source.
- [ ] Keep the example small and do not give away the app exercise's full solution.
- [ ] Verify every code example and output independently.
- [ ] Narration is separated from visual directions.
- [ ] Each scene defines the visible state and when it changes.
- [ ] Include a genuine silent prediction hold.
- [ ] End with the corresponding PyLearn task and explicit practice CTA.
- [ ] Copy the exact voice lock; do not guess the approved voice ID.
- [ ] User generates narration; assistant owns scene design, render setup, render review, and fixes.

## Full video quality gate — after render
- [ ] Validate duration, resolution, frame rate, audio stream, and MP4 playability.
- [ ] Review every scene end-to-end, not only sampled frames.
- [ ] Compare transcript timestamps with visual states.
- [ ] Confirm every spoken name, value, line, and output appears at the correct time.
- [ ] Check no required state is missing, stale, clipped, or revealed early.
- [ ] Confirm silent holds and complete narration.
- [ ] Confirm end card sends learner into the correct app task.
- [ ] Fix defects and rerender before asking user to review.
- [ ] Do not publish or move a new video to permanent final storage without explicit user approval.
