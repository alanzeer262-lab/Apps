# Lesson 01 Narration Voice Lock

Status: candidate voice preset for the revised pilot. This is a durable record; do not generate full narration until the pilot voice has been reviewed.

## Original recording provenance
The original narration was generated in Runway on 2026-10-16. The available task records do not expose the original voice ID, speech model, speed, or prosody configuration. Do not invent or imply that those settings have been recovered.
- Part 1 task ID: `db3f7d61-135b-41cd-88a5-ad1ba8ae3349`; duration 173.82458 s.
- Part 2 task ID: `89671605-058b-4369-a1af-02ed10dcf0c5`; duration 237.865215 s.
- Existing short clip task IDs: `011c67de-1a5e-4f85-8e8f-7509bc3d82a6` (`print_1`), `cb10cf49-3d1c-4b99-9278-ea9fdf6a496c` (`print_7`), `95f3c280-bfea-4e65-b398-75f8f2034d39` (`numbers_4`).

## Candidate settings for voice audition
- Voice preset: `Elias` — masculine, older, American accent, calm narrator.
- Speech model: `eleven_v3` — expressive model supporting inline delivery tags.
- Speed: `0.92`.
- Language: English (`en`).
- Delivery: conversational welcome; small pause after the welcome; gentle emphasis on “one idea at a time”; reassuring, never rushed.
- Purpose: short audition only, not approved as the final voice until compared with the original.
- This is a new candidate selection, **not** a recovered original setting.

## Non-negotiable persistence rules
1. Keep this file and the task IDs in GitHub.
2. After each generation, immediately record task ID, chosen voice, model, speed, language, exact spoken text, and asset URL in this file.
3. Keep the generated MP3 in the Runway workspace and commit a copy into `public/audio/` before depending on it in a render.
4. Do not regenerate the full narration until the user approves the pilot voice.
5. Never overwrite the original narration MP3s; use distinct `revised_*` filenames.
6. If the preset cannot reproduce the original sufficiently, stop and present the comparison rather than silently replacing the voice.

## Audition generation v1
- Status: submitted to Runway; the inline viewer is handling completion.
- Task ID: `5a102e5f-b0e9-4650-91f2-a31f71446024`
- Asset name: `PyLearn Lesson 01 — Voice Lock Audition Elias v1`
- Voice preset: `Elias`
- Model: `eleven_v3`
- Speed: `0.92`
- Language: `en`
- Exact spoken text (including delivery tags):
  > [warm, conversational] Welcome to PyLearn. I'm glad you're here. [pause] In this lesson, we're going to take our first steps with Python, one idea at a time. There's no need to rush. We'll write a little code, run it, and look carefully at what happens. [gentle emphasis] The goal isn't to memorize everything. It's to understand what each line is doing.
- Credits reported remaining after submission: 54 (Runway indicated low credits).
- Asset URL: pending task completion; append the final URL here before depending on the audio.
- Important: this is a candidate audition, not confirmed to match the original teacher voice. Do not generate the full lesson until the user has listened and approved the voice.
