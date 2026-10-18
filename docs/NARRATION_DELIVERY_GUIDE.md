# Narration Delivery Guide — Lesson 01 Pilot

Status: implementation guide for the first patient-tutor render.

## Objective

Keep the existing teacher voice if the original voice can be regenerated. The priority is not voice replacement: it is expressive, meaning-led delivery. The teacher should sound as if they are guiding one beginner, not reading a dense list of facts.

## Performance rules

1. **Vary pace by purpose.** Use a natural conversational pace for familiar transitions. Slow slightly when a new concept or code element first appears. Do not slow every sentence equally.
2. **Give questions a real question shape.** Lift the tone slightly on the question, then stop speaking so the learner can think.
3. **Use silence deliberately.** Allow 3–5 seconds after prediction prompts and learner tasks. Use shorter pauses between related sentences and a little more space before revealing an output or explaining an error.
4. **Emphasize meaning, not every keyword.** Give light emphasis to the contrast that matters (for example, number versus text, opening quote versus closing quote, value changes versus message stays the same).
5. **Reassure during errors.** Use a calm, supportive tone. Avoid dramatic alarm or a rushed explanation.
6. **Sound encouraging at success points.** Warmth should feel natural, not overexcited or like an advertisement.
7. **Do not stretch audio artificially.** Prefer natural delivery and clean pauses over uniformly slowing the whole recording. If a sentence sounds rushed, rewrite or regenerate that sentence/section.
8. **Keep visual holds aligned with speech.** Do not reveal the answer while the question is still being asked. Keep code visible while it is explained, then show output at the spoken run/reveal cue.
9. **Preserve the words and meaning.** Delivery cues guide tone and timing; they must not add spoken instructions that are absent from the script.
10. **Review the full render.** Check the first listen without pausing, then inspect each scene for pace, emphasis, silence, and code/output alignment. A successful build alone is not approval.

## Scene-level delivery map

| Scene | Delivery intention |
|---|---|
| 1 — First program | Warm welcome; unhurried code introduction; quiet satisfaction after the first output |
| 2 — Calculation | Curious setup; clear question; full thinking pause; simple explanation after reveal |
| 3 — Number and text | Invite observation; gently emphasize the quotation marks; avoid making the distinction sound more complicated than it is |
| 4 — Quotes and error | Calm explanation; clearly signal the intentional mistake; reassuring tone after the error |
| 5 — Comment | Conversational and matter-of-fact; pause to compare code with output |
| 6 — Personal message | Friendly; explain one line at a time; emphasize that only the value changes |
| 7 — Learner turn | Encouraging invitation; leave genuine silent practice time; do not talk over the learner's thinking |
| 8 — Debugging | Calm and practical; one instruction at a time; positive but restrained confirmation after the fix |
| 9 — Recap | Reflective, not rushed; let the final achievement land before the end card |

## Production sequence

1. Confirm whether the existing voice can be regenerated from its original source/settings. Do not assume a different preset is the same voice.
2. Prepare narration in manageable scene/section chunks so pace and tone can vary by purpose.
3. Generate or record the updated delivery. If the original voice cannot be reproduced, decide explicitly whether the delivery improvement justifies a replacement voice; do not silently substitute one.
4. Update `scripts/sync-cues.json` to use exact phrases from the new narration.
5. Run alignment and render. Fix cue mismatches rather than guessing timestamps.
6. Watch the complete video and evaluate teaching quality and synchronization before approval.

## Acceptance criteria

- The voice has natural pace variation tied to meaning.
- Questions are followed by genuine thinking time.
- Code and output remain readable without the narration rushing ahead.
- Errors sound safe to explore, not frightening.
- No scene feels like a compressed list of facts.
- The final video is reviewed from beginning to end.
