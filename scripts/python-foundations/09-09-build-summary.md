# PyLearn Video — 09 — Build: Summary Report

**Voice lock — mandatory:** Use the user-approved Kendrick voice with ElevenLabs v3. Do not substitute another voice or preset.
**Canonical source:** Pylearn-build260/content/python-foundations/modules/09-build-summary.md, branch ccr-c7f6fdd7-xpzi3g.
**Use:** Full teaching video, not a short outline. Narrate only spoken text; keep scene headings, code labels, and visual directions out of text-to-speech. Do not show the app's required exercise solution.

## Scene 1 — Turn rows into answers

**Visual:** Reveal the code gradually. Ask for a prediction before running it. Show the output only after the run.

**Narration:**

A pile of records is not yet a useful answer. A summary should tell us how many valid scores we have, what their average is, and who has the highest score. The function should receive validated records, not raw CSV text.

**Code**
    
    scores = [88, 72, 95]
        print("Count:", len(scores))
        print("Average:", sum(scores) / len(scores))
        print("Top score:", max(scores))

**Expected output**
    
    Count: 3
        Average: 85.0
        Top score: 95

**Narration:**

The count, average, and top score answer different questions. Keep the output clear and avoid rounding until you know how the report should display the result.

## Scene 2 — Protect the empty case

**Visual:** Reveal the code gradually. Ask for a prediction before running it. Show the output only after the run.

**Narration:**

If there are no valid scores, there is no average and no top scorer. Calling max on an empty list raises an error, and dividing by zero does too. The summary should handle the empty case explicitly.

**Code**
    
    scores = []
        if not scores:
            print("No valid scores")
        else:
            print(sum(scores) / len(scores))
            print(max(scores))

**Expected output**
    
    No valid scores

**Narration:**

A good empty result is more useful than a crash. It also tells the person reading the report why no statistic was produced.

## Scene 3 — Make the output interpretable

**Visual:** Reveal the code gradually. Ask for a prediction before running it. Show the output only after the run.

**Narration:**

A summary can report a count, average, and top score. For a real toolkit, it should also preserve the row counts and validation warnings from earlier stages.

**Code**
    
    scores = [88, 72, 95]
        summary = {
            "count": len(scores),
            "average": sum(scores) / len(scores),
            "top_score": max(scores),
        }
        print(summary)

**Expected output**
    
    {'count': 3, 'average': 85.0, 'top_score': 95}

**Narration:**

Returning a dictionary gives the rest of the program a structured result to format or write to a file. The function calculates; the report layer decides how to present it.

## Your turn — predict, run, explain

**Visual:** Keep the editor uncluttered. Show a fresh, related prompt without using the app's required exercise code.

**Narration:**

Pause the video and try a small variation of the example. Predict the output before you run it. Then run the code, compare the result with your prediction, and explain why it happened. If the result surprises you, inspect the values and change one thing at a time.

This is extra guided practice, not the required PyLearn exercise solution.

## Recap

**Narration:**

Today, you learned the core idea behind summary and empty cases. Keep the stages clear, test your assumptions, and make the program's behavior visible. In the next lesson, we'll build on this skill.

## Final call to action — watch the practice video

**Visual:** Neutral end card reading “Next: Practice Video”. Do not show unfinished app screens or invent navigation.

**Narration:**

Great work! You've finished Build: Summary Report. Next, watch the practice video. I recommend watching it because we'll use a fresh example to reinforce the skill from this lesson.

After the practice video, complete the exercise to unlock the next lesson. If you'd like extra hands-on practice, you can also try it in the PyLearn app.

**Visual:** Hold the end card long enough to read.

## Production checklist

- [ ] Use the approved Kendrick voice with ElevenLabs v3.
- [ ] Verify every example and expected output in Python before rendering.
- [ ] Reveal code before running it; reveal output only after the run.
- [ ] Keep narration separate from production directions.
- [ ] Do not show the required app exercise solution or hidden tests.
- [ ] Watch the complete rendered video at normal speed before approval.
