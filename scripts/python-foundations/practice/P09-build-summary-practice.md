# PyLearn Guided Practice — Summary Practice

**Voice lock:** Use the approved Kendrick voice with ElevenLabs v3; do not substitute another voice.
**Canonical source:** Pylearn-build260/content/python-foundations/modules/09-build-summary.md, branch ccr-c7f6fdd7-xpzi3g.
**Purpose:** Separate practice companion; do not reveal the required exercise implementation or hidden evaluation answers.

## Scene 1 — Calculate a compact summary

**Narration:** Use a new set of validated scores. The summary reports the count, average, and highest score. Predict the result before running it.

**Code**

    scores = [61, 78, 91, 70]
    print("Count:", len(scores))
    print("Average:", sum(scores) / len(scores))
    print("Top:", max(scores))

**Expected output**

    Count: 4
    Average: 75.0
    Top: 91

Each number answers a different question. The average summarizes the group; the top score identifies the highest individual value.

## Scene 2 — Handle no scores

**Code**

    scores = []
    if not scores:
        print("No valid scores")

**Expected output**

    No valid scores

**Narration:** There is no meaningful average or top score when no valid records remain. Your function should return a clear empty result rather than crash.

## Production checklist
- [ ] Use approved Kendrick / ElevenLabs v3 voice.
- [ ] Verify code and output before rendering.
- [ ] Keep the examples separate from the required app exercise.
- [ ] Keep narration and visual directions separate.
- [ ] Watch the full render before approval.
