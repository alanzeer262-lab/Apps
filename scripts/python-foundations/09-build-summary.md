# PyLearn Video — Build: Summary Report

**Voice lock:** Use the user-approved Kendrick voice with ElevenLabs v3. Do not substitute another voice.
**Canonical source:** Pylearn-build260/content/python-foundations/modules/09-build-summary.md, branch ccr-c7f6fdd7-xpzi3g.
**Production rule:** Narrate only spoken text. Do not show the required app exercise solution or invent app screens.

## Scene 1 — Turn rows into answers

**Narration:**

A pile of records is not yet an answer. A useful summary tells us how many valid scores we have, what their average is, and who has the highest score. The summary function should receive validated records, not raw CSV text.

**Code**

    scores = [88, 72, 95]
    print("Count:", len(scores))
    print("Average:", sum(scores) / len(scores))
    print("Top score:", max(scores))

**Expected output**

    Count: 3
    Average: 85.0
    Top score: 95

Each statistic answers a different question. The count describes the size of the group, the average describes its central value, and the top score identifies its highest value.

## Scene 2 — Protect the empty case

**Narration:**

What happens when there are no valid scores? There is no average and no top scorer. Dividing by zero or calling max on an empty list raises an error, so the function must handle the empty case explicitly.

**Code**

    scores = []
    if not scores:
        print("No valid scores")
    else:
        print(sum(scores) / len(scores))
        print(max(scores))

**Expected output**

    No valid scores

A clear empty result is better than a crash. It tells the person reading the report why no statistic was produced.

## Scene 3 — Return structured results

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

Returning a dictionary gives the rest of the program a structured result to format or save. The summary function calculates; the report layer decides how to present it.

## Recap and handoff

You've learned to summarize validated data and protect the empty case. Next, watch the practice video, then complete the exercise to unlock the next lesson. You can also practise in the PyLearn app for extra hands-on work.

## Final production checklist

- [ ] Verify each code sample and stated output in Python.
- [ ] Reveal code before running it and output only after the run.
- [ ] Keep narration separate from visual directions.
- [ ] Watch the complete rendered video at normal speed before approval.
