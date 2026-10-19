# PyLearn Video 11 — Comprehensions, Imports, and Safe Conversion

> **MANDATORY VOICE SETTINGS — DO NOT CHANGE**
> - Voice: Kendrick
> - Model: ElevenLabs v3
> - Voice ID: exact approved Kendrick voice ID is not recorded in the reviewed repository files; insert the verified ID from the original Runway setup before generating narration.
> - No guessed ID, voice substitution, or preset. Use the same approved voice identity throughout.
> - Speak narration only; do not read headings or bracketed directions aloud.

**Canonical source:** `Pylearn-build260/content/python-basics/modules/11-comprehensions-imports.md`, branch `ccr-c7f6fdd7-xpzi3g`.  
**Target runtime:** Approximately 7–8 minutes. Keep the required app exercise solution hidden.

## Scene 1 — Real data can be imperfect

**Visual:** Show a list of text values, including one invalid item. Do not convert or analyze the full required app exercise data.

**Narration:**

Welcome back to PyLearn.

In real programs, values don't always arrive in the format we expect. A score might arrive as text. Some values may be valid numbers, while others contain words or are missing entirely.

Today, we'll learn three useful tools: list comprehensions, imports, and safe conversion. We'll also discuss a special value called None, which helps us represent the absence of a value.

Let's start with a small list.

**Code**
```python
raw_scores = ["88", "72", "oops", "95"]
print(raw_scores)
```

**Expected output**
```text
['88', '72', 'oops', '95']
```

**Narration:**

Every item here is text, even though some items look like numbers. The word oops is not a valid integer. We'll need a deliberate rule for handling that instead of assuming every value is clean.

## Scene 2 — Transform a list with a comprehension

**Visual:** First show the longer loop, then replace it with the equivalent comprehension. Keep both versions readable and explain that they produce the same result.

**Code — loop version**
```python
scores = [70, 80, 90]
doubled = []

for score in scores:
    doubled.append(score * 2)

print(doubled)
```

**Expected output**
```text
[140, 160, 180]
```

**Narration:**

Suppose we have a list of scores and want a new list with each score doubled. A loop can do that: start with an empty list, visit each score, multiply it by two, and append the result.

Python also has a compact way to express this transformation.

**Code — comprehension version**
```python
scores = [70, 80, 90]
doubled = [score * 2 for score in scores]
print(doubled)
```

**Expected output**
```text
[140, 160, 180]
```

**Narration:**

The result is the same. Read the comprehension as: build a list by taking each score and multiplying it by two.

A comprehension is useful when the transformation is simple enough to remain clear. Don't use one just to make code shorter. Readability is more important than compactness.

## Scene 3 — Filter while building a list

**Visual:** Reveal the condition at the end of the comprehension, then show the output.

**Code**
```python
scores = [55, 70, 84, 92]
passing = [score for score in scores if score >= 70]
print(passing)
```

**Expected output**
```text
[70, 84, 92]
```

**Narration:**

A comprehension can also filter items. Here, Python takes each score, checks whether it is at least seventy, and includes only the scores that pass the condition.

The value fifty-five is skipped. The other three values meet the rule and appear in the new list.

The idea is still visit, test, and keep. A comprehension is simply a compact way to express a transformation or filter when it remains easy to understand.

## Scene 4 — Reuse code with imports

**Visual:** Reveal the import line first, then the function call. Explain the module name before running.

**Code**
```python
import math
print(math.sqrt(25))
```

**Expected output**
```text
5.0
```

**Narration:**

Python includes a standard library: a collection of useful tools that you can reuse instead of writing everything from scratch.

The import statement makes a module available. Here, we import math and use its square-root function. Writing math dot sqrt makes it clear which module the function comes from.

We can also import a specific tool.

**Code**
```python
from statistics import mean
print(mean([70, 80, 90]))
```

**Expected output**
```text
80
```

**Narration:**

This line imports mean from the statistics module. Then we call mean with a list of three values, and Python calculates their average.

Imports are a way to reuse tested code. When you need a common capability, check whether Python already provides a suitable tool.

## Scene 5 — None represents the absence of a value

**Visual:** Show None beside 0, an empty string, and False. Keep the comparison simple and do not imply these values are interchangeable.

**Code**
```python
result = None
print(result)
print(result is None)
```

**Expected output**
```text
None
True
```

**Narration:**

Sometimes a value is absent. Python uses None to represent that absence.

None is not the same as zero, an empty string, or False. Those values can have their own meanings. For example, if a score was not supplied, replacing it with zero might incorrectly suggest that the learner earned zero points.

A missing score is not automatically a zero. Choose a rule that matches what the data means.

## Scene 6 — Handle expected conversion errors

**Visual:** Show a valid conversion first. Then show the invalid conversion in a separate run to demonstrate the error. Finally introduce try and except as a safe handling approach.

**Code — valid value**
```python
value = "88"
score = int(value)
print(score)
```

**Expected output**
```text
88
```

**Narration:**

The text eighty-eight can be converted to an integer because its contents are digits that form a valid integer.

But a value such as oops cannot be converted this way.

**Code — invalid value**
```python
value = "oops"
score = int(value)
```

**Visual direction:** Run this separate example and show the ValueError. Do not leave the editor stuck on the error; transition to the safe version.

**Narration:**

Python raises a ValueError because the text isn't a valid integer. If invalid input is something our program expects to encounter, we can handle that error with try and except.

**Code — safe conversion**
```python
value = "oops"

try:
    score = int(value)
except ValueError:
    score = None

print(score)
print(score is None)
```

**Expected output**
```text
None
True
```

**Narration:**

Python attempts the conversion inside the try block. If the conversion raises ValueError, the except block runs and assigns None.

The program continues instead of stopping at the expected conversion error. It has also made a decision: invalid numeric input will be represented as None.

In a real program, the correct decision depends on the task. You might skip a record, report it, or ask the user to correct it. The important point is not to hide bad data accidentally.

## Scene 7 — Build a safe data pipeline

**Visual:** Show a simple four-step flow: raw input, attempt conversion, separate valid and invalid values, analyze and report. Do not build a full solution to the app exercise.

**Narration:**

A useful processing pipeline starts with raw input. We attempt to convert values, separate the valid ones from the invalid ones, analyze the values that meet our rules, and report what was rejected.

That is already the beginning of data engineering and data analysis thinking.

Before you process data, ask what should happen when a value is missing or invalid. Should it be skipped, reported, or represented as None? There's no universal answer. The important thing is to choose deliberately and make the rule clear.

## Scene 8 — Recap

**Visual:** Reveal list comprehension, imports, None, try/except, and explicit validation rules.

**Narration:**

Let's recap.

A list comprehension can transform or filter a collection in a compact way. Imports let us reuse tools from Python's standard library. None represents the absence of a value and is not interchangeable with zero, an empty string, or False.

Try and except let us handle expected errors, such as converting invalid text to an integer. But catching an error is only one part of safe data handling. We also need a clear decision about what to do with the invalid value.

This is the final Python Basics concept lesson. Next, you'll start combining these ideas in projects, and then bring them together in the Mini Gradebook capstone.

## Final call to action — required for in-app and YouTube versions

**Visual:** Show the real PyLearn navigation path to Lesson 11 and highlight its required coding exercise. Do not show the completed app exercise or capstone solution.

**Narration:**

Now it's your turn to write code yourself.

Open PyLearn and go to Lesson 11, then complete its required coding exercise. If you're watching this on YouTube, open PyLearn and find this lesson there.

Run your code, read the feedback, and fix mistakes as needed. Practice Drills are optional. Passing the required exercise is what unlocks the next lesson.

Pause this video and start coding.

## Production and QA checklist

- [ ] Verify the exact approved Kendrick voice ID before generating audio.
- [ ] Use ElevenLabs v3 and the same approved voice identity throughout.
- [ ] Keep scene directions out of the spoken text.
- [ ] Verify every code sample and output in Python.
- [ ] Make the ValueError demonstration and safe version distinct.
- [ ] Do not reveal the required Lesson 11 exercise solution.
- [ ] Preserve the required PyLearn navigation ending and progression rule.
