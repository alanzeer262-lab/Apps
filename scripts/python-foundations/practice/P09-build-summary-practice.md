# PyLearn Guided Practice — Summary Practice

**Voice lock:** Use the approved Kendrick voice with ElevenLabs v3; do not substitute another voice.
**Canonical source:** Pylearn-build260/content/python-foundations/modules/09-build-summary.md, branch ccr-c7f6fdd7-xpzi3g.
**Purpose:** Separate practice companion; do not reveal the required exercise implementation or hidden evaluation answers.
**Track 2 practice visuals:** Use a compact analytics dashboard with count, average, and maximum tiles plus a small distribution graphic. Pause before the figures appear. Demonstrate the empty case with an intentional empty-state panel. Keep “Summarize” active on the toolkit progress rail.

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


## Production-critical rule — traceable transformation and truthful results
- Show the sequence explicitly: **source/input → each meaningful transformation → final output**. Use the actual data and code from this script; keep transitions readable and in causal order. Do not jump-cut from input to a result without showing or explaining the operation that produced it.
- Whenever a result is shown, it must be the exact output produced by running the displayed code against the displayed sample data. Verify it in Python before rendering. If it has not been run and verified, do not present it as a real result; mark it as a schematic illustration or omit the value.
- For the toolkit-build and capstone scenes, show the real end-to-end result learners can reproduce by building the tool themselves. No fabricated dashboard metrics, invented report rows, decorative “success” values, or output inconsistent with the code/data. Keep the sample dataset, code, and displayed result synchronized.
- For practice videos, use the script's own independent example and verify that example. Do not reveal the required PyLearn exercise solution.
