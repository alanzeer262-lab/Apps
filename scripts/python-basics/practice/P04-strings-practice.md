# PyLearn Guided Practice 04 — Strings

> **MANDATORY VOICE SETTINGS — DO NOT CHANGE**
> - Voice: Kendrick
> - Model: ElevenLabs v3
> - Voice ID: exact approved Kendrick voice ID is not recorded in the reviewed repository files; insert the verified ID from the original Runway setup before generation.
> - No guessed ID, substitution, or preset; use the same approved voice identity throughout.
> - Speak narration only; do not read scene headings or bracketed production notes aloud.

**Canonical source:** `Pylearn-build260/content/python-basics/modules/04-strings.md`, branch `ccr-c7f6fdd7-xpzi3g`.
**Target runtime:** Approximately 2–4 minutes.
**Purpose:** Separate guided-practice companion using fresh examples; never reveal the required app exercise solution.

## Scene 1 — Clean a topic string

**Visual:** Highlight the leading and trailing spaces without changing the actual code text.

**Code**
```python
raw = "  data science, python  "
clean = raw.strip()
print(clean)
```

**Expected output:** `data science, python`

**Narration:** Strip removes whitespace from the beginning and end. It doesn't change the spaces between the words.

## Scene 2 — Split into pieces

**Code**
```python
topics = clean.split(",")
print(topics)
```

**Expected output**
```text
['data science', ' python']
```

**Narration:** Split uses the comma as a separator. Notice that the second item still has a leading space, so splitting alone does not clean every piece.

## Scene 3 — Normalize and search

**Code**
```python
topic = " Python "
print(topic.strip().lower())
print("python" in topic.lower())
```

**Expected output**
```text
python
True
```

**Narration:** We strip outer spaces and normalize capitalization. For a case-insensitive search, normalize the text before checking whether the search term appears.

## Close — Navigate to the real task

**Narration:** Now open PyLearn and find the required coding exercise for Lesson 4. This video is extra practice; the actual app exercise is still required to unlock the next lesson.

## Production checklist
- [ ] Verify the exact approved Kendrick voice ID before generating audio.
- [ ] Use ElevenLabs v3 with the same approved voice identity.
- [ ] Verify all code and outputs in Python.
- [ ] Keep code and output synchronized with narration.
- [ ] Do not reveal the required app exercise solution.
- [ ] End by directing the learner to the required PyLearn exercise.
