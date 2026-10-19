# PyLearn Video 14 — Project 3: Clean My Learning Topics

> **MANDATORY VOICE SETTINGS — DO NOT CHANGE**
> - Voice: Kendrick
> - Model: ElevenLabs v3
> - Voice ID: exact approved Kendrick voice ID is not recorded in the reviewed repository files; insert the verified ID from the original Runway setup before generating audio.
> - No guessed ID, substitution, or preset. Keep the same approved voice throughout.
> - Speak narration only; do not read headings or bracketed directions aloud.

**Canonical source:** `Pylearn-build260/content/python-basics/modules/14-build-topic-cleaner.md`, branch `ccr-c7f6fdd7-xpzi3g`.  
**Target runtime:** Approximately 5–7 minutes. Do not show the complete required function or solution.

## Scene 1 — Messy text is normal

**Visual:** Show a string with extra spaces, inconsistent capitalization, and a repeated topic. Keep the actual code unchanged; use highlights to reveal the whitespace.

**Narration:**

Welcome back.

In real programs, text rarely arrives perfectly formatted. Someone might type extra spaces, use different capitalization, repeat a topic, or leave an empty entry between commas.

In this project, you'll build a topic cleaner. Before coding, let's understand the sequence of transformations we need.

**Code**
```python
raw = "  data, Python, data  "
print(repr(raw))
```

**Expected output**
```text
'  data, Python, data  '
```

Using `repr` makes the leading and trailing spaces visible in the editor output.

**Narration:**

This is the raw input. We should not assume it's already ready to use. We need to split it into individual topics, remove surrounding whitespace, normalize capitalization, and ignore empty pieces.

## Scene 2 — Split a string

**Visual:** Reveal split first and show the resulting list. Highlight that the separator is a comma.

**Code**
```python
raw = "data, Python, data"
parts = raw.split(",")
print(parts)
```

**Expected output**
```text
['data', ' Python', ' data']
```

**Narration:**

Split breaks one string into pieces wherever it finds the separator. Here, the separator is a comma, so we get three strings in a list.

Notice that the spaces after the commas remain. Splitting and cleaning are separate operations. Keeping those steps separate makes the process easier to understand and test.

## Scene 3 — Strip and normalize

**Visual:** Show one string being cleaned. Reveal strip and title separately, then show the resulting text.

**Code**
```python
topic = "  pYtHoN  "
clean_topic = topic.strip().lower()
print(clean_topic)
```

**Expected output**
```text
python
```

**Narration:**

Strip removes whitespace from the beginning and end. Lower converts the text to lowercase. We can combine the methods because the result of strip can be passed to lower.

Normalizing capitalization matters. Without it, Python and python may be treated as different strings even if we intend them to represent the same topic.

The project asks you to choose a consistent capitalization rule and apply it to every topic.

## Scene 4 — Ignore empty pieces

**Visual:** Show a simple input with two commas next to each other. Show the split result containing an empty string, then visually mark that empty piece as something the cleaner should skip. Do not show the full required function.

**Code**
```python
raw = "python,,pandas"
parts = raw.split(",")
print(parts)
```

**Expected output**
```text
['python', '', 'pandas']
```

**Narration:**

If two separators appear next to each other, split creates an empty string between them. The project requires you to ignore empty pieces.

Think about the order of operations. Split the raw string. Clean each piece. Then check whether the cleaned piece is empty before keeping it. That order handles both extra spaces and empty entries.

## Scene 5 — Search without capitalization surprises

**Visual:** Show a cleaned topic and a search phrase with different capitalization. Demonstrate the idea using an independent example.

**Code**
```python
topic = "python"
search_text = "PYTHON"
print(search_text.lower() == topic.lower())
```

**Expected output**
```text
True
```

**Narration:**

When searching should ignore capitalization, normalize both sides of the comparison. Here, both strings are converted to lowercase before we compare them, so the result is true.

The important point is consistency. If we normalize stored topics one way but search using a different rule, a valid match may be missed.

## Scene 6 — Plan the transformation pipeline

**Visual:** Show a four-step flow: raw text → split → clean each piece → ignore empty pieces. Avoid showing a completed list for the required input.

**Narration:**

Let's put the steps together conceptually.

Start with raw text. Split it on commas to get individual pieces. Remove surrounding whitespace and normalize capitalization for each piece. Ignore any pieces that become empty. Then use a consistent search rule to check whether a topic is present.

Build and test one step at a time. First inspect the result of split. Then test cleaning on one topic. Then add the rule for empty pieces. Finally, test a search with different capitalization.

This is easier to debug than writing the whole function in one attempt.

## Scene 7 — Reflection

**Visual:** Show the words “Python” and “python” side by side, then show the normalized forms.

**Narration:**

Before you finish, consider this question: why could Python and python become two different categories if you don't normalize them?

Strings are compared by their characters, including capitalization. A consistent normalization rule makes the data more reliable and prevents accidental duplicate categories.

## Final call to action — watch the practice video

**Visual:** Use a neutral end card reading “Next: Practice Video”. Do not show or describe unfinished PyLearn app screens or reveal a completed project solution.

**Narration:**

Great work! You've finished this lesson. The next step is to watch the practice video. I recommend watching it because it will help you apply what you've learned with a fresh example.

After the practice video, complete the exercise to unlock the next lesson. If you'd like extra hands-on practice, you can also try it in the PyLearn app.

**Visual:** Hold the “Next: Practice Video” end card long enough to read.

## Production and QA checklist

- [ ] Verify the exact approved Kendrick voice ID before generating audio.
- [ ] Use ElevenLabs v3 and the same approved voice throughout.
- [ ] Keep production notes out of spoken narration.
- [ ] Verify all demonstration code and outputs in Python, including whitespace.
- [ ] Do not reveal the full `clean_topics` implementation or required input's completed output.
- [ ] Preserve the project navigation ending and progression rule.
