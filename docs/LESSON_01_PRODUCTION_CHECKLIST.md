# Lesson 01 — Production Checklist

## Locked decisions
- Target length: 6–8 minutes.
- Teacher voice: Noah.
- Speech model: `eleven_multilingual_v2`.
- Speed: `0.90`.
- Language: English.
- Delivery: composed, analytical, patient; neither overly deep nor high-energy.
- Do not include literal `[pause]`, voice direction, headings, or scene labels in the text sent to speech generation.
- Add deliberate silence in the edit when the learner needs time to think.
- Keep the original narration MP3s unchanged.

## Current preparation (no new speech credits spent)
- `docs/LESSON_01_FINAL_NARRATION_TEXT.md`: clean spoken text, about 909 words / 5,081 characters.
- `docs/LESSON_01_REVISED_STORYBOARD.json`: prepared nine-scene visual storyboard.
- `scripts/sync-cues.revised-draft.json`: nine-scene cue draft; scene 8's correction/output cue is matched to the spoken phrase “Now it works.”
- `scripts/align_narration.py`: supports optional `PYLEARN_AUDIO_FILES`, `PYLEARN_SYNC_CUES`, and `PYLEARN_ALIGNMENT_OUTPUT` environment variables. Defaults preserve the original two audio tracks, original cue file, and original alignment output.
- Current production workflow and active 14-scene lesson have not been switched to the revised materials.

## Credit gate
Last known Runway balance: 41 credits. Estimated full narration cost: about 102 credits, depending on how requests are chunked and billed. Wait until the available balance can cover the complete narration; do not generate a partial lesson that cannot be finished.

## When credits are sufficient
1. Split the clean narration into two sequential chunks at a natural scene boundary, each within the speech tool's text limit. Do not duplicate or omit words at the join.
2. Generate each chunk with the locked Noah voice, `eleven_multilingual_v2`, speed `0.90`, English. Send only spoken words; use ordinary punctuation, not stage directions.
3. Record both Runway task IDs, asset URLs, exact text, settings, and durations in the voice-lock doc and handover.
4. Download the audio and commit it as `public/audio/revised_narration_part_1.mp3` and `public/audio/revised_narration_part_2.mp3`; never overwrite original files.
5. Run alignment in isolation with:
   ```sh
   PYLEARN_AUDIO_FILES=public/audio/revised_narration_part_1.mp3,public/audio/revised_narration_part_2.mp3 \
   PYLEARN_SYNC_CUES=scripts/sync-cues.revised-draft.json \
   PYLEARN_ALIGNMENT_OUTPUT=src/generated-alignment.revised.json \
   python scripts/align_narration.py
   ```
6. Inspect all anchor matches and timing. If an anchor fails, correct the cue to the actual spoken phrase; never invent timestamps.
7. Implement the nine-scene revised lesson as a separate Remotion composition first. Do not break the known active composition.
8. Type-check and render a separate revised MP4 artifact.
9. Watch the entire revised video from start to finish. Verify every scene change, code/output reveal, quote error and correction, learner task, recap, and ending.
10. Only after approval, switch the primary workflow to the revised composition and mark the production checklist complete.

## Final quality gate
- Total duration is between 360 and 480 seconds, or any deviation is explicitly reviewed.
- No stage directions are spoken aloud.
- The narration is not rushed; each learner prompt has enough silence.
- Code shown matches the explanation and displayed output.
- Scene boundaries and events follow measured spoken anchors.
- Full playback is checked, not inferred from a successful GitHub Actions build.
