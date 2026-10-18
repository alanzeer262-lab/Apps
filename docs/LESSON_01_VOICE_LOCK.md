# Lesson 01 Narration Voice Lock

Status: Noah voice approved by user for the revised pilot, with one text-markup correction required before using this approach for future narration.

## Original recording provenance
The original narration was generated in Runway on 2026-10-16. Available task records do not expose the original voice ID, speech model, speed, or prosody configuration. Do not invent or imply those settings were recovered.
- Part 1 task ID: `db3f7d61-135b-41cd-88a5-ad1ba8ae3349`; duration 173.82458 s.
- Part 2 task ID: `89671605-058b-4369-a1af-02ed10dcf0c5`; duration 237.865215 s.
- Existing short clip task IDs: `011c67de-1a5e-4f85-8e8f-7509bc3d82a6` (`print_1`), `cb10cf49-3d1c-4b99-9278-ea9fdf6a496c` (`print_7`), `95f3c280-bfea-4e65-b398-75f8f2034d39` (`numbers_4`).

## Approved voice direction
Target: an INTJ-like teaching style, interpreted as composed, analytical, precise, restrained, and thoughtful — not a literal personality diagnosis. Avoid exaggerated friendliness, hype, theatrical emotion, and an excessively deep voice.
- Elias audition v1 was rejected by the user as too deep.
- Brodie audition v2 was rejected by the user as too energetic.
- Noah audition v3 was approved by the user as very good. Preserve this voice, model, and speed for the pilot unless the user requests a change.

## Delivery and pause rules
- Approved audition voice: Noah; model: `eleven_multilingual_v2`; speed: `0.90`; language: `en`.
- Do NOT put literal `[pause]` markers in spoken narration text: the model spoke the word “pause” aloud.
- Use natural sentence punctuation and paragraph breaks to guide delivery. If a longer silent pause is needed, insert silence in the video/audio edit rather than speaking a stage direction.
- Do not change the approved voice/model/speed just to solve spoken stage directions.

## Non-negotiable persistence rules
1. Keep this file and all task IDs in GitHub.
2. After each generation, record task ID, voice, model, speed, language, exact spoken text, and asset URL/status.
3. Commit a copy of approved audio into `public/audio/` before depending on it in a render.
4. Never generate the full lesson until the user approves the pilot voice.
5. Never overwrite the original narration MP3s; use distinct `revised_*` filenames.
6. If a preset doesn't fit the requested style, stop and compare rather than silently replacing it.

## Audition v1 — Elias — REJECTED
- Task ID: `5a102e5f-b0e9-4650-91f2-a31f71446024`
- Voice: `Elias`; model: `eleven_v3`; speed: `0.92`; language: `en`.
- Feedback: user said the voice was too deep. Do not use it.

## Audition v2 — Brodie — REJECTED
- Task ID: `3b51cfe5-591c-4f7a-99a7-f6893bc59ab8`
- Voice: `Brodie`; model: `eleven_v3`; speed: `0.98`; language: `en`.
- Feedback: user said it had too much energy. Do not use it.

## Audition v3 — Noah — APPROVED WITH TEXT-MARKUP FIX
- Task ID: `1ca0a7be-d3cd-4c9e-898c-54fbccdaebf5`
- Asset name: `PyLearn Lesson 01 — Calm Analytical Voice Audition Noah v1`
- Voice: `Noah` (young masculine American, calm/meditation preset).
- Model: `eleven_multilingual_v2`.
- Speed: `0.90`.
- Language: `en`.
- Spoken text submitted:
  > [calm, measured] Welcome to PyLearn. [pause] In this lesson, we'll take our first steps with Python, one idea at a time. We'll write a little code, run it, and examine the result. [pause] The goal is to understand what each line does.
- User feedback: “Done very good but I am hearing the word pause every time.” Voice approved; remove literal pause markers from future spoken text.
- Asset URL returned by Runway: https://dnznrvs05pmza.cloudfront.net/text_to_speech/36bce141-28b6-4f3d-9e60-cb960cee963a/PyLearn_Lesson_01___Calm_Analytical_Voice_Audition_Noah_v1.mp3
- Credits reported remaining at generation: 41; Runway indicated low credits.
- Do not generate the full lesson until the revised script is ready and the user confirms to proceed.


## Full revised narration generation — submitted 2026-10-18
Both chunks were submitted using the approved voice settings: Noah, `eleven_multilingual_v2`, speed `0.90`, language `en`. No pause markers or spoken stage directions were included.
- Part 1 — scenes 1–6; 3,492 characters; estimated 70 credits; task ID `5890fe18-15be-4e91-a6a5-e6583a278fcf`; last observed status RUNNING (98%); final asset URL pending.
- Part 2 — scenes 7–9; 1,579 characters; estimated 32 credits; task ID `ea274edf-db56-4c42-9ba2-d3e8ee264349`; last observed status RUNNING (72%); final asset URL pending.
- Submitted through Runway workspace `Moh` (workspace ID `70442037`). Reported remaining balance after both submissions: 398 credits.
- Do not rely on either output until both tasks succeed and the audio URLs/durations are verified. Then preserve the original MP3s, save revised files under distinct names, and continue with isolated alignment and a separate composition.


## Revised full narration — generation completed 2026-10-18
- Part 1 (scenes 1–6): task ID `5890fe18-15be-4e91-a6a5-e6583a278fcf`; Noah; `eleven_multilingual_v2`; speed 0.90; language en; duration 274.181224 s; asset name `PyLearn Lesson 01 Revised Narration Part 1 — Noah`.
  URL: https://dnznrvs05pmza.cloudfront.net/text_to_speech/da79bf60-e88d-4c18-b43a-fa80482caf84/PyLearn_Lesson_01_Revised_Narration_Part_1___Noah.mp3
- Part 2 (scenes 7–9): task ID `ea274edf-db56-4c42-9ba2-d3e8ee264349`; Noah; `eleven_multilingual_v2`; speed 0.90; language en; duration 127.663311 s; asset name `PyLearn Lesson 01 Revised Narration Part 2 — Noah`.
  URL: https://dnznrvs05pmza.cloudfront.net/text_to_speech/2c4f563f-14d0-4940-98f3-59614bed4a91/PyLearn_Lesson_01_Revised_Narration_Part_2___Noah.mp3
- Combined duration is 401.844535 s (~6:42), inside the requested 6–8 minute range.
- The generation tasks succeeded. However, local download attempts failed because the signed URLs could not be fetched from the runtime. Do not claim the MP3 files are committed. Keep the original recordings and active renderer untouched until the revised files are available locally and committed.
