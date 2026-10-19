# PyLearn Video — Build: Summary Report

**Track 2 visual identity:** Keep the same teacher and pacing. Shift from code demonstration to a compact analytics dashboard: count, average, and top score become three metric tiles supported by a small bar or distribution graphic. Show the empty-data case as a clear empty state, not an error explosion. Keep the toolkit stage rail with “Summarize” highlighted.

**Voice lock:** Use the user-approved Kendrick voice with ElevenLabs v3. Do not substitute another voice.
**Canonical source:** Pylearn-build260/content/python-foundations/modules/09-build-summary.md, branch ccr-c7f6fdd7-xpzi3g.
**Production rule:** Narrate only spoken text. Do not show the required app exercise solution or invent app screens.

## Visual execution notes — keep the result traceable

For Scene 1, show the actual input list `[88, 72, 95]` before revealing any metric. Animate the three values into the count calculation (3), the sum (255), and then the average calculation (255 ÷ 3 = 85.0). Highlight 95 as the maximum only after the `max(scores)` operation runs. The dashboard tiles must read **Count: 3**, **Average: 85.0**, and **Top score: 95** because these are the exact results of the displayed code.

For Scene 2, start with an empty list and show the branch taken by `if not scores`; reveal “No valid scores” only after that branch runs. Do not display an average or top-score tile for an empty list.

For Scene 3, reveal the dictionary only after the code runs. Keep its keys and values identical to the printed output. Never use placeholder dashboard values or animate numbers that do not come from the displayed variables.

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


## Production-critical rule — traceable transformation and truthful results
- Show the sequence explicitly: **source/input → each meaningful transformation → final output**. Use the actual data and code from this script; keep transitions readable and in causal order. Do not jump-cut from input to a result without showing or explaining the operation that produced it.
- Whenever a result is shown, it must be the exact output produced by running the displayed code against the displayed sample data. Verify it in Python before rendering. If it has not been run and verified, do not present it as a real result; mark it as a schematic illustration or omit the value.
- For the toolkit-build and capstone scenes, show the real end-to-end result learners can reproduce by building the tool themselves. No fabricated dashboard metrics, invented report rows, decorative “success” values, or output inconsistent with the code/data. Keep the sample dataset, code, and displayed result synchronized.
- For practice videos, use the script's own independent example and verify that example. Do not reveal the required PyLearn exercise solution.
