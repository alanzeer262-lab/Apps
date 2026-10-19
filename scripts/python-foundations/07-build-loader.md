# PyLearn Video — 07 — Build: Load a Scores CSV

**Voice lock — mandatory:** Use the user-approved Kendrick voice with ElevenLabs v3. Do not substitute another voice or preset.
**Canonical source:** Pylearn-build260/content/python-foundations/modules/07-build-loader.md, branch ccr-c7f6fdd7-xpzi3g.
**Use:** Full teaching video, not a short outline. Narrate only spoken text; keep scene headings, code labels, and visual directions out of text-to-speech. Do not show the app's required exercise solution.

**Track 2 visual identity:** Keep the same teacher and pacing. Make this feel like the first build bench: a CSV file card opens into a row inspector, with headers and raw values highlighted. Use a persistent small progress rail for the toolkit stages, with “Load” highlighted and later stages muted. Avoid making the screen a generic input/output demonstration.

## Scene 1 — The loader's responsibility

**Visual:** Reveal the code gradually. Ask for a prediction before running it. Show the output only after the run.

**Narration:**

Now we move from individual skills to a small toolkit. The loader's job is narrow: take raw CSV text and turn it into a consistent list of records. It should not calculate averages or decide which scores are valid.

**Code**
    
    csv_text = "name,score\nAda,88\nLin,72\n"
        print(csv_text.splitlines())

**Expected output**
    
    ['name,score', 'Ada,88', 'Lin,72']

**Narration:**

The input is plain text. A loader parses the rows and trims stray spaces so later functions receive predictable values.

## Scene 2 — Separate parsing from analysis

**Visual:** Reveal the code gradually. Ask for a prediction before running it. Show the output only after the run.

**Narration:**

For this demonstration, we'll use Python's CSV reader with an in-memory text stream. That lets us show the parsing idea without needing a real file on screen.

**Code**
    
    import csv
        from io import StringIO
    
        text = "name,score\nAda,88\nLin,72\n"
        reader = csv.DictReader(StringIO(text))
        rows = list(reader)
        print(rows[0]["name"], rows[0]["score"])

**Expected output**
    
    Ada 88

**Narration:**

The CSV reader recognizes the header fields. At this stage, the score is still text. Loading should preserve the parsed value and leave validation to the next step.

## Scene 3 — Handle ordinary mess

**Visual:** Reveal the code gradually. Ask for a prediction before running it. Show the output only after the run.

**Narration:**

Real inputs may have extra spaces or a final blank line. A good loader trims fields and skips rows that contain no meaningful data. That makes its output more consistent without hiding invalid scores.

**Code**
    
    raw_name = "  Ada  "
        raw_score = " 88 "
        print(raw_name.strip())
        print(raw_score.strip())

**Expected output**
    
    Ada
        88

**Narration:**

Trimming whitespace is not the same as deciding whether a score is valid. Keep the loader's job focused, then test its behavior on clean rows and awkward formatting.

## Your turn — predict, run, explain

**Visual:** Keep the editor uncluttered. Show a fresh, related prompt without using the app's required exercise code.

**Narration:**

Pause the video and try a small variation of the example. Predict the output before you run it. Then run the code, compare the result with your prediction, and explain why it happened. If the result surprises you, inspect the values and change one thing at a time.

This is extra guided practice, not the required PyLearn exercise solution.

## Recap

**Narration:**

Today, you learned the core idea behind loader. Keep the stages clear, test your assumptions, and make the program's behavior visible. In the next lesson, we'll build on this skill.

## Final call to action — watch the practice video

**Visual:** Neutral end card reading “Next: Practice Video”. Do not show unfinished app screens or invent navigation.

**Narration:**

Great work! You've finished Build: Load a Scores CSV. Next, watch the practice video. I recommend watching it because we'll use a fresh example to reinforce the skill from this lesson.

After the practice video, complete the exercise to unlock the next lesson. If you'd like extra hands-on practice, you can also try it in the PyLearn app.

**Visual:** Hold the end card long enough to read.

## Production checklist

- [ ] Use the approved Kendrick voice with ElevenLabs v3.
- [ ] Verify every example and expected output in Python before rendering.
- [ ] Reveal code before running it; reveal output only after the run.
- [ ] Keep narration separate from production directions.
- [ ] Do not show the required app exercise solution or hidden tests.
- [ ] Watch the complete rendered video at normal speed before approval.
