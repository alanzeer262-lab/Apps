# Lesson 01 Narration Voice Lock

Status: candidate voice preset for the revised pilot. Do not generate full narration until the user approves a short audition.

## Original recording provenance
The original narration was generated in Runway on 2026-10-16. Available task records do not expose the original voice ID, speech model, speed, or prosody configuration. Do not invent or imply those settings were recovered.
- Part 1 task ID: `db3f7d61-135b-41cd-88a5-ad1ba8ae3349`; duration 173.82458 s.
- Part 2 task ID: `89671605-058b-4369-a1af-02ed10dcf0c5`; duration 237.865215 s.
- Existing short clip task IDs: `011c67de-1a5e-4f85-8e8f-7509bc3d82a6` (`print_1`), `cb10cf49-3d1c-4b99-9278-ea9fdf6a496c` (`print_7`), `95f3c280-bfea-4e65-b398-75f8f2034d39` (`numbers_4`).

## Voice direction
Target: an INTJ-like teaching style, interpreted as composed, analytical, precise, restrained, and thoughtful — not a literal personality diagnosis. Avoid exaggerated friendliness, hype, theatrical emotion, and an excessively deep voice.
- Elias audition v1 was rejected by the user as too deep.
- Brodie audition v2 was submitted after that, but the user said it had too much energy.
- Current candidate is Noah with a calm preset, a steadier speech model, and measured pacing. It remains a candidate until the user listens.

## Non-negotiable persistence rules
1. Keep this file and all task IDs in GitHub.
2. After each generation, record task ID, voice, model, speed, language, exact spoken text, and asset URL/status.
3. Commit a copy of approved audio into `public/audio/` before depending on it in a render.
4. Never generate the full narration until the user approves the pilot voice.
5. Never overwrite the original narration MP3s; use distinct `revised_*` filenames.
6. If a preset doesn't fit the requested style, stop and compare rather than silently replacing it.

## Audition v1 — Elias — REJECTED
- Task ID: `5a102e5f-b0e9-4650-91f2-a31f71446024`
- Voice: `Elias`; model: `eleven_v3`; speed: `0.92`; language: `en`.
- Feedback: user said the voice was too deep. Do not use it.

## Audition v2 — Brodie — NOT APPROVED
- Task ID: `3b51cfe5-591c-4f7a-99a7-f6893bc59ab8`
- Voice: `Brodie`; model: `eleven_v3`; speed: `0.98`; language: `en`.
- Feedback: user said it had too much energy. Do not treat as approved.

## Audition v3 — Noah — AWAITING REVIEW
- Task ID: `1ca0a7be-d3cd-4c9e-898c-54fbccdaebf5`
- Asset name: `PyLearn Lesson 01 — Calm Analytical Voice Audition Noah v1`
- Voice: `Noah` (young masculine American, calm/meditation preset).
- Model: `eleven_multilingual_v2` (steadier, more predictable narration).
- Speed: `0.90`.
- Language: `en`.
- Exact spoken text:
  > [calm, measured] Welcome to PyLearn. [pause] In this lesson, we'll take our first steps with Python, one idea at a time. We'll write a little code, run it, and examine the result. [pause] The goal is to understand what each line does.
- Credits reported remaining after submission: 41; Runway indicated low credits.
- Asset URL: pending completion in Runway.
- Do not generate the full lesson until the user approves this voice.
