# P02 — Guided Practice: Variables and types

**Purpose:** Companion practice video for Python Basics lesson 2.
**Target length:** 2–4 minutes.
**Voice:** ElevenLabs v3, Kendrick, exact approved voice ID only. Use approved audio as timing master; do not substitute voices.
**Learning goal:** Store simple study details.

## Runway visual direction
Use the shared visual style from `docs/RUNWAY_PYTHON_BASICS_MASTER_PACKAGE.md`: 16:9, 1920×1080, restrained motion, large high-contrast code, accurate captions, no fake PyLearn UI. Exact code must be typeset or captured from a real editor; do not ask the model to generate code text. Use the supplied narration audio; do not generate replacement speech.

## Scene plan
1. **Hook (0:00–0:15):** Introduce the everyday problem in one sentence. Show only a simple visual relevant to the example.
2. **Predict (0:15–0:35):** Display the code in short readable chunks. Ask the learner to pause and predict the result.
3. **Run and explain (0:35–1:40):** Reveal the result, highlight one line at a time, and explain why it behaves that way.
4. **Try a variation (1:40–2:20):** Invite the learner to change one value or condition mentally, then reveal the changed behavior.
5. **Transfer to PyLearn (final 15–25 seconds):** Use the exact CTA below. Never imply watching this video completes the app task.

## Original illustrative example
```python
course = "Python"
minutes = 25
rating = 4.5
is_ready = True
print(type(course))
print(type(minutes))
print(type(rating))
print(type(is_ready))
```

## Direction for the presenter/editor
Explain assignment as a label attached to a value. Convert numeric text such as int("25") and show why int("twenty") is invalid. Use fresh values unrelated to app tasks.

## Closing narration
“Open PyLearn Lesson 2 and complete its required coding exercise. Practice Drills are optional; passing the required exercise unlocks the next lesson.”

## Safety and quality checks
- This is a fresh illustrative example, not the required app exercise answer.
- Run the code in plain Python and verify every output before export.
- Keep each code screen visible long enough to read on a phone.
- Do not show hidden tests, app solutions, or a complete project solution.
- Captions must preserve Python punctuation, underscores, quotes, operators, and indentation.
