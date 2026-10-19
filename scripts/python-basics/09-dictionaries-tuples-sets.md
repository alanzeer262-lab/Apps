# PyLearn Video 09 — Dictionaries, Tuples, and Sets

> **MANDATORY VOICE SETTINGS — DO NOT CHANGE**
> - Voice: Kendrick
> - Model: ElevenLabs v3
> - Voice ID: exact approved Kendrick voice ID is not recorded in the reviewed repository files; insert the verified ID from the original Runway setup before generating audio.
> - No guessed ID, voice substitution, or preset. Use the same approved voice throughout.
> - Speak narration only. Do not read scene headings or bracketed directions aloud.

**Canonical source:** `Pylearn-build260/content/python-basics/modules/09-dict-tuple-set.md`, branch `ccr-c7f6fdd7-xpzi3g`.  
**Target runtime:** Approximately 7–8 minutes. Do not reveal the required app exercise solution.

## Scene 1 — Different data needs different structures

**Visual:** Show a list briefly, then transition to a learner record with labeled fields. Keep the same editor style as previous lessons.

**Narration:**

Welcome back to PyLearn.

A list is useful when you need an ordered collection. But sometimes our data has more structure. A learner has a name, a score, and a goal. A report may connect categories to counts. A group of repeated labels may need to be reduced to unique values.

Python gives us different structures for these jobs. Today we'll look at dictionaries, tuples, and sets, and learn when each one makes sense.

## Scene 2 — Dictionaries connect keys and values

**Visual:** Reveal the dictionary one key-value pair at a time. Highlight the key, colon, and value.

**Code**
```python
learner = {
    "name": "Ada",
    "score": 88,
    "goal": "Data Analyst"
}
print(learner["name"])
print(learner["score"])
```

**Expected output**
```text
Ada
88
```

**Narration:**

A dictionary stores key-value pairs. Each key is a label, and each value is the information associated with that label.

Here, the key name points to Ada, score points to eighty-eight, and goal points to Data Analyst.

We look up a value by writing the key inside square brackets after the dictionary name. So learner, open bracket, name, close bracket gives us Ada.

Think of a dictionary as a way to answer this question: what value belongs to this label?

## Scene 3 — Update and add dictionary entries

**Visual:** Start with the same learner dictionary. Change the score, then add a new key. Show the updated structure after each operation.

**Code**
```python
learner = {"name": "Ada", "score": 88}
learner["score"] = 91
learner["level"] = "beginner"
print(learner["score"])
print(learner["level"])
```

**Expected output**
```text
91
beginner
```

**Narration:**

A dictionary can be updated. Assigning a new value to an existing key changes that entry. Here, the score changes from eighty-eight to ninety-one.

We can also assign a value to a new key. The key level didn't exist before, so this adds a new entry.

Use a dictionary when the label matters more than the position. We don't have to remember that a score was stored in the second slot, because we can ask for the value using its key.

## Scene 4 — Tuples group related values

**Visual:** Show a two-value tuple. Highlight each item and then the matching unpacked variable.

**Code**
```python
record = ("Ada", 88)
name, score = record
print(name)
print(score)
```

**Expected output**
```text
Ada
88
```

**Narration:**

A tuple groups related values into one record. Here, the tuple contains a name and a score.

We can unpack the tuple into two variables. The first item goes into name, and the second item goes into score.

This can make code easier to read than repeatedly selecting items by numeric position. A tuple is a useful choice when several values belong together as one fixed record.

## Scene 5 — Process records with unpacking

**Visual:** Show three records and then the loop. Highlight the current name and score as each output line appears.

**Code**
```python
records = [
    ("Ada", 88),
    ("Lin", 72),
    ("Sam", 95)
]

for name, score in records:
    print(f"{name}: {score}")
```

**Expected output**
```text
Ada: 88
Lin: 72
Sam: 95
```

**Narration:**

Here, we have a list of tuples. Each tuple represents one record, and the list contains several records.

The loop unpacks each tuple into name and score. Then the f-string creates a readable line for that learner.

Notice how each structure has a role. The list keeps the records in order. Each tuple groups the fields for one record. The loop visits each record, and the variables name and score make the fields easy to understand.

## Scene 6 — Sets keep unique values

**Visual:** Show a short list of topic labels with a duplicate, then a set. Emphasize uniqueness, not order.

**Code**
```python
topics = {"python", "pandas", "python"}
print(len(topics))
print("python" in topics)
```

**Expected output**
```text
2
True
```

**Narration:**

A set stores unique values. In this example, python appears twice in the written set, but a set keeps only one copy of that value.

The length is two because the unique topics are python and pandas. The membership check is true because python is present.

Sets are useful when uniqueness or membership is what matters most. Don't depend on a set to preserve the order in which values were written. If order matters, consider a list instead.

## Scene 7 — Count categories with a dictionary

**Visual:** Reveal the list of grade labels, then an empty dictionary. Step through the loop, showing how each count is updated.

**Code**
```python
grades = ["A", "B", "A", "C", "B", "A"]
counts = {}

for grade in grades:
    counts[grade] = counts.get(grade, 0) + 1

print(counts)
```

**Expected output**
```text
{'A': 3, 'B': 2, 'C': 1}
```

**Narration:**

A dictionary can also help us count how often each category appears.

We start with an empty dictionary called counts. For each grade, the get method looks up the current count. If that key hasn't appeared yet, get gives us zero. Then we add one and store the updated count.

The first A gets a count of one. When another A appears, its count becomes two. When the third A appears, the count becomes three. The same process counts B twice and C once.

This is called a frequency count. It turns repeated raw values into a summary. Later, data-analysis tools will make grouping and counting more powerful, but this basic idea remains important.

## Scene 8 — Choose the structure that fits

**Visual:** Show four simple labels: list = ordered collection; tuple = grouped record; dictionary = key/value lookup; set = unique values. Keep each explanation short.

**Narration:**

How do you choose between these structures?

Use a list when you need an ordered collection of items. Use a tuple to group related values into one record. Use a dictionary when you need to look up a value by a key. Use a set when uniqueness or membership is the main concern.

Don't choose a structure only because it's the newest one you've learned. Choose it because it matches the question your program needs to answer.

## Scene 9 — Recap

**Visual:** Bring back a small example of each structure without showing the app exercise's full required data or solution.

**Narration:**

Let's recap.

Dictionaries connect keys to values and let us update entries. Tuples group related values and can be unpacked into named variables. Sets keep unique values and are useful for membership checks. A dictionary can also count categories by updating the count for each key.

Together, these structures help us move from a few separate values to data with shape and meaning.

## Final call to action — watch the practice video

**Visual:** Use a neutral end card reading “Next: Practice Video”. Do not show or describe unfinished PyLearn app screens.

**Narration:**

Great work! You've finished this lesson. The next step is to watch the practice video. I recommend watching it because it will help you apply what you've learned with a fresh example.

After the practice video, complete the exercise to unlock the next lesson. If you'd like extra hands-on practice, you can also try it in the PyLearn app.

**Visual:** Hold the “Next: Practice Video” end card long enough to read.

## Production and QA checklist

- [ ] Verify the exact approved Kendrick voice ID before generating audio.
- [ ] Use ElevenLabs v3 and the same approved voice throughout.
- [ ] Keep production directions out of spoken narration.
- [ ] Verify every code sample and expected output in Python.
- [ ] Make dictionary keys, tuple fields, and set uniqueness visually clear.
- [ ] Do not reveal the required Lesson 9 exercise solution.
- [ ] Preserve the required PyLearn navigation ending and progression rule.
