# PyLearn Video 04 — Strings and f-Strings

> **MANDATORY VOICE SETTINGS — DO NOT CHANGE**
> - Voice: Kendrick
> - Model: ElevenLabs v3
> - Voice ID: the exact approved custom Kendrick voice ID is not present in the repository files reviewed so far. Insert the verified ID from the original Runway setup before generating audio.
> - Do not guess, substitute another voice, or use a preset. Keep the same approved voice across every part.
> - Speak narration only. Do not read headings, code labels, or bracketed visual directions aloud.

**Canonical source:** `Pylearn-build260/content/python-basics/modules/04-strings.md`, branch `ccr-c7f6fdd7-xpzi3g`.  
**Target runtime:** Approximately 7–8 minutes.  
**Purpose:** Full teaching video. Keep the required app exercise solution hidden.

## Scene 1 — Text is data

**Visual:** Continue the same editor and output panel as earlier lessons. Show a single string with spaces around a list of topics.

**Narration:**

Welcome back.

Today we're going to work with strings. A string is text: a sequence of characters that Python can store, inspect, and transform.

Real programs rarely receive perfectly formatted text. A person might type extra spaces, use different capitalization, or enter several topics in one line. Our job is to learn a few simple tools for working with that text.

Let's start with a string.

**Code**
```python
topic = "Python"
print(topic)
```

**Expected output**
```text
Python
```

**Narration:**

The variable topic stores the text Python. We can work with the whole string, or we can select part of it.

## Scene 2 — Indexing starts at zero

**Visual:** Reveal `topic[0]`, then `topic[1]`. Show the characters P y t h o n with index labels 0 through 5 beneath them.

**Code**
```python
topic = "Python"
print(topic[0])
print(topic[1])
```

**Expected output**
```text
P
y
```

**Narration:**

Python lets us access one character using its index, which is its position in the string.

Notice something important: Python starts counting at zero, not one. The character P is at index zero, and y is at index one.

That is called zero-based indexing. It may feel unusual at first, so keep the index labels visible while you practice.

## Scene 3 — Slicing selects a section

**Visual:** Highlight the characters selected by each slice. Keep the start-included, end-excluded rule on screen as a short visual note.

**Code**
```python
topic = "Python"
print(topic[0:2])
print(topic[:2])
print(topic[2:])
```

**Expected output**
```text
Py
Py
thon
```

**Narration:**

A slice selects part of a string. In the first line, we start at index zero and stop before index two. That gives us Py.

The starting position is included, but the ending position is not. That's the rule to remember: start here, stop before there.

If we leave out the starting position, Python starts at the beginning. If we leave out the ending position, Python continues to the end.

So the second line also gives Py, and the third line gives thon.

Take a moment to look at the indexes again. Predict which characters a slice will select before running it. That small habit will help you avoid off-by-one mistakes.

## Scene 4 — Clean extra spaces

**Visual:** Show a value with leading and trailing spaces. Make the spaces visible with a subtle highlight, not with additional characters in the actual code.

**Code**
```python
name = "  ada  "
print(name.strip())
print(name.upper())
print(name.lower())
print(name.title())
```

**Expected output**
```text
ada
  ADA  
  ada  
  Ada  
```

**Narration:**

String methods help us transform text.

The strip method removes whitespace from the beginning and end. Upper changes the letters to uppercase. Lower changes them to lowercase. Title changes the text to title-style capitalization.

Notice that upper, lower, and title do not remove the extra spaces. Strip is the method that handles the outer whitespace.

We can combine methods too.

**Code**
```python
name = "  ada  "
clean_name = name.strip().title()
print(clean_name)
```

**Expected output**
```text
Ada
```

**Narration:**

First, strip removes the outer spaces. Then title formats the cleaned name. The result is Ada.

This is a useful pattern: take messy input, transform it, and keep the useful result.

## Scene 5 — Split one string into pieces

**Visual:** Reveal the raw string, then the split call. Show the output as a list with three items.

**Code**
```python
raw = "python, pandas, machine learning"
topics = raw.split(",")
print(topics)
```

**Expected output**
```text
['python', ' pandas', ' machine learning']
```

**Narration:**

Sometimes several values arrive in one string, separated by commas. The split method can break the string into pieces.

Here, we split at each comma. Python gives us a list of three strings.

Look closely at the second and third items. They still have spaces at the beginning. Splitting the string doesn't automatically clean each piece.

For now, focus on the sequence: one string goes in, and a list of smaller strings comes out. Later, loops will help us apply the same cleanup to every item.

## Scene 6 — Check whether text is present

**Visual:** Show the two membership expressions, then reveal each Boolean result only after running.

**Code**
```python
topic = "machine learning"
print("learning" in topic)
print("python" in topic)
```

**Expected output**
```text
True
False
```

**Narration:**

The word in lets us check whether one piece of text appears inside another string.

The first question is true because learning appears in machine learning. The second is false because python does not appear in that text.

This check is case-sensitive. Python and python are not the same sequence of characters. If we want a simple case-insensitive check, we can convert the text to lowercase before searching.

**Code**
```python
topic = "Machine Learning"
print("learning" in topic.lower())
```

**Expected output**
```text
True
```

**Narration:**

The lower method makes the stored text lowercase for this check, so learning is found. We haven't changed the original variable; we're using the transformed result for the comparison.

## Scene 7 — Replace text and build readable messages

**Visual:** Reveal the original message, then the replace call. Afterward show an f-string using variables.

**Code**
```python
message = "I like Java"
message = message.replace("Java", "Python")
print(message)
```

**Expected output**
```text
I like Python
```

**Narration:**

The replace method substitutes one piece of text for another. Here, Java is replaced with Python, and the updated message is printed.

Be precise about what you're replacing. Basic string replacement looks for the literal text you specify.

Now let's use an f-string to combine text with values.

**Code**
```python
name = "Ada"
score = 92
print(f"{name} scored {score}.")
print(f"Next target: {score + 3}")
```

**Expected output**
```text
Ada scored 92.
Next target: 95
```

**Narration:**

The f before the quotation mark tells Python to evaluate expressions inside curly braces. The first message inserts the name and score. The second performs a small calculation inside the braces and inserts the result.

Readable output matters. A useful program should make its result understandable to the person reading it.

## Scene 8 — Predict and inspect a transformation

**Visual:** Use a fresh example that does not reproduce the required app exercise. Reveal the code gradually, ask for a prediction, and hold the editor still during the pause.

**Code**
```python
raw = "  DATA, Python  "
clean = raw.strip()
print(clean)
print(clean.lower())
print(clean.replace("Python", "coding"))
```

**Narration:**

Let's combine a few of today's tools.

Before running the code, predict what strip will remove, what lower will change, and what replace will do to the final line.

Take a few seconds to think.

[Leave a silent prediction pause of about four seconds.]

Now let's run it.

**Expected output**
```text
DATA, Python
data, python
  DATA, coding  
```

**Narration:**

The first output has no outer spaces because strip removed them. The second output is lowercase. The last output replaces Python with coding in the original raw string, so the original outer spaces remain.

That's a useful detail: each line starts with the value named in that line. We didn't assign the stripped value back to raw, so raw still contains the original text.

## Scene 9 — Recap

**Visual:** Reveal the recap terms one by one: indexing, slicing, strip, upper/lower/title, split, in, replace, f-strings.

**Narration:**

Let's recap.

A string is a sequence of characters. Indexing selects one character, and Python starts counting at zero. Slicing selects a section; the start is included and the end is excluded.

Strip removes outer whitespace. Upper, lower, and title change capitalization. Split breaks one string into pieces. The in operator checks whether text appears inside another string. Replace substitutes one piece of text for another, and f-strings help us build readable messages with values.

Most importantly, think of text as data you can transform step by step.

## Final call to action — required for in-app and YouTube versions

**Visual:** Show the real PyLearn navigation path to Lesson 4 and highlight its required coding exercise. Do not show a completed solution or unverified app UI. Hold the screen long enough to read.

**Narration:**

Now it's your turn to write code yourself.

Open PyLearn and go to Lesson 4, then complete its required coding exercise. If you're watching this on YouTube, open PyLearn and find this lesson there.

Run your code, read the feedback, and fix mistakes as needed. Practice Drills are optional. Passing the required exercise is what unlocks the next lesson.

Pause this video and start coding.

## Production and QA checklist

- [ ] Verify the approved Kendrick voice ID before generating audio; it is not recorded in the reviewed repository files.
- [ ] Use ElevenLabs v3 and the same approved voice identity throughout; no substitution.
- [ ] Keep spoken narration separate from production notes.
- [ ] Verify every code block and output in Python; confirm whitespace in displayed outputs.
- [ ] Do not reveal the Lesson 4 required-exercise solution.
- [ ] Keep code and index labels legible on a phone.
- [ ] Preserve the required PyLearn navigation ending and progression rule.
