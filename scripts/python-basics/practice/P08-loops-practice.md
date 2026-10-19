# PyLearn Guided Practice 08 — Loops

> **MANDATORY VOICE SETTINGS — DO NOT CHANGE**
> - Voice: Kendrick
> - Model: ElevenLabs v3
> - Voice ID: exact approved Kendrick voice ID is not recorded in the reviewed repository files; insert the verified ID from the original Runway setup before generation.
> - No guessed ID, substitution, or preset; use the same approved voice identity throughout.
> - Speak narration only; do not read scene headings or bracketed production notes aloud.

**Canonical source:** `Pylearn-build260/content/python-basics/modules/08-loops.md`, branch `ccr-c7f6fdd7-xpzi3g`.
**Target runtime:** Approximately 2–4 minutes.
**Purpose:** Separate guided-practice companion using fresh examples; do not reveal the required app exercise solution.

## Scene 1 — Process task durations

**Code**
```python
durations = [15, 20, 10]
for duration in durations:
    print(duration)
```

**Expected output**
```text
15
20
10
```

**Narration:** The for loop visits each duration in order and prints the current item once.

## Scene 2 — Add an accumulator

**Code**
```python
durations = [15, 20, 10]
total = 0
for duration in durations:
    total += duration
print(total)
```

**Expected output:** `45`

**Narration:** Total starts at zero. Each iteration adds the current duration to it. After the loop, total contains the sum.

## Scene 3 — Filter longer tasks

**Code**
```python
durations = [15, 20, 10, 35]
long_tasks = []
for duration in durations:
    if duration >= 20:
        long_tasks.append(duration)
print(long_tasks)
```

**Expected output:** `[20, 35]`

**Narration:** The loop checks each duration and keeps only those that meet the condition. This is the visit, test, keep pattern.

## Close — Navigate to the real task

**Narration:** Open PyLearn and find the required coding exercise for Lesson 8. This practice video is separate from the graded task. Complete and pass the required exercise to unlock the next lesson.

## Production checklist
- [ ] Verify the exact approved Kendrick voice ID before generation.
- [ ] Use ElevenLabs v3 with the same approved voice identity.
- [ ] Verify code and expected outputs in Python.
- [ ] Keep output synchronized with narration.
- [ ] Do not reveal the required app exercise solution.
- [ ] End by directing the learner to the required PyLearn exercise.
