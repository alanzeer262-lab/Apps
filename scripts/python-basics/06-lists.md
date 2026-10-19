# PyLearn Video 06 — Lists

> **MANDATORY VOICE SETTINGS — DO NOT CHANGE**
> - Voice: Kendrick
> - Model: ElevenLabs v3
> - Voice ID: exact approved Kendrick voice ID not found in the reviewed repository records; insert the verified ID from the original Runway setup before generating narration.
> - No voice substitution, guessed ID, or preset. Use the same approved voice for every part.
> - Read narration only; scene titles and bracketed production notes are not spoken.

**Canonical source:** `Pylearn-build260/content/python-basics/modules/06-lists.md`, branch `ccr-c7f6fdd7-xpzi3g`.  
**Target runtime:** Approximately 7–8 minutes.

## Scene 1 — Store a collection

**Visual:** Continue the established editor layout. Show a short list and highlight the square brackets.

**Narration:**

Welcome back to PyLearn.

So far, many of our variables have stored one value at a time. But what if we need to keep several related values together, such as a group of scores?

Python has a tool for that: a list.

**Code**
```python
scores = [70, 95, 88, 60]
print(scores)
```

**Expected output**
```text
[70, 95, 88, 60]
```

**Narration:**

The square brackets mark the list, and commas separate the items. This list stores four numbers in a particular order.

Lists are useful whenever we need a collection of values, such as scores, names, topics, or measurements. The list keeps those values together under one variable name.

## Scene 2 — Access an item by index

**Visual:** Label the positions 0, 1, 2, and 3 beneath the four values. Highlight one requested item at a time.

**Code**
```python
scores = [70, 95, 88, 60]
print(scores[0])
print(scores[2])
```

**Expected output**
```text
70
88
```

**Narration:**

Lists use zero-based indexing, just like strings. The first item is at index zero. The second item is at index one. The third is at index two.

So scores at index zero gives seventy, and scores at index two gives eighty-eight.

You can also count from the end using negative indexes.

**Code**
```python
scores = [70, 95, 88, 60]
print(scores[-1])
```

**Expected output**
```text
60
```

**Narration:**

Index negative one means the last item. That's useful when you want the end of a list and don't want to calculate its final index yourself.

Before you run an index expression, point to the item you expect it to select. This is a good way to avoid choosing the wrong position.

## Scene 3 — Select part of a list

**Visual:** Highlight items at index 1 and 2 while showing the slice boundary. Keep the rule “start included, end excluded” visible.

**Code**
```python
scores = [70, 95, 88, 60]
print(scores[1:3])
```

**Expected output**
```text
[95, 88]
```

**Narration:**

A slice gives us part of a list. We start at index one and stop before index three. That means we include the items at indexes one and two, but not the item at index three.

The result is a smaller list containing ninety-five and eighty-eight.

Remember the same slicing rule we used for strings: the start position is included, and the end position is excluded. Slicing gives us a selection without removing items from the original list.

## Scene 4 — Add and replace items

**Visual:** Start with three values. Reveal append, then show the list after running. Next, change the first item.

**Code**
```python
scores = [70, 95, 88]
scores.append(60)
print(scores)
```

**Expected output**
```text
[70, 95, 88, 60]
```

**Narration:**

Lists can change after we create them. The append method adds one item to the end of the list. Here, sixty is added after the original three scores.

We can also replace an item using its index.

**Code**
```python
scores = [70, 95, 88]
scores[0] = 75
print(scores)
```

**Expected output**
```text
[75, 95, 88]
```

**Narration:**

This time, we replace the value at index zero. The first score changes from seventy to seventy-five, while the other values stay the same.

Because list contents can be changed, we say lists are mutable. You don't need to memorize the term immediately, but remember that you can append items and replace existing items.

## Scene 5 — Ask questions about a list

**Visual:** Reveal each built-in one at a time. Keep the output panel empty until each run.

**Code**
```python
scores = [70, 95, 88, 60]
print(len(scores))
print(sum(scores))
print(min(scores))
print(max(scores))
```

**Expected output**
```text
4
313
60
95
```

**Narration:**

Python provides useful built-in functions for lists.

Len tells us how many items are in the list. There are four scores.

Sum adds the values, giving three hundred and thirteen.

Min finds the smallest value, which is sixty. Max finds the largest, which is ninety-five.

These functions answer common questions without requiring us to write a loop ourselves.

We can calculate an average by dividing the total by the number of items.

**Code**
```python
scores = [70, 95, 88, 60]
average = sum(scores) / len(scores)
print(average)
```

**Expected output**
```text
78.25
```

**Narration:**

The average is seventy-eight point two five. Notice that we use the sum and length of the list, rather than typing the total and count manually. If the list changes, the calculation can use the updated values.

But we must think about edge cases. What if the list is empty? Its length is zero, and dividing by zero causes an error. Later, when you build real programs, decide what the program should do when there are no values to calculate.

## Scene 6 — Sort and check membership

**Visual:** Show the original list, then the sorted result. Visually distinguish the original variable from the new variable.

**Code**
```python
scores = [70, 95, 88, 60]
ordered = sorted(scores)
print(ordered)
print(scores)
```

**Expected output**
```text
[60, 70, 88, 95]
[70, 95, 88, 60]
```

**Narration:**

Sorted returns a new list with the values in order. Here, the new variable ordered contains the scores from lowest to highest. The original scores list remains in its original order.

If all you need is the highest score, max is simpler than sorting the whole list. Choose the smallest tool that answers your question.

We can also ask whether a value appears in a list.

**Code**
```python
scores = [70, 95, 88, 60]
print(95 in scores)
print(100 in scores)
```

**Expected output**
```text
True
False
```

**Narration:**

The in operator returns True if the value appears in the list, and False if it doesn't. Here, ninety-five is present, but one hundred is not.

## Scene 7 — Predict, then run

**Visual:** Use a separate example that does not reproduce the app exercise list. Ask the learner to predict length, total, and highest value.

**Code**
```python
pages = [12, 18, 15]
print(len(pages))
print(sum(pages))
print(max(pages))
print(18 in pages)
```

**Narration:**

Let's test the same ideas with pages read across three sessions.

Before running the code, predict how many values are in the list, their total, the highest value, and whether eighteen appears.

Take a few seconds to think.

[Leave a silent prediction pause of about four seconds.]

**Expected output**
```text
3
45
18
True
```

**Narration:**

There are three values. Their total is forty-five. The highest value is eighteen, and eighteen is in the list, so the final result is True.

If one of your predictions was different, look at the list and check one operation at a time.

## Scene 8 — Recap

**Visual:** Reveal: create, index, slice, append, replace, len/sum/min/max, sorted, membership, empty-list edge case.

**Narration:**

Let's recap.

A list stores multiple values in order. Use an index to access one item, and a slice to select part of the list. Append adds an item, and assigning to an index replaces an item.

Len counts items. Sum adds numeric values. Min and max find the smallest and largest values. Sorted returns a new ordered list, and in checks membership.

Finally, remember edge cases. An empty list has no values to average, so a real program needs to handle that situation deliberately.

## Final call to action — watch the practice video

**Visual:** Use a neutral end card reading “Next: Practice Video”. Do not show or describe unfinished PyLearn app screens.

**Narration:**

Great work! You've finished this lesson. The next step is to watch the practice video. I recommend watching it because it will help you apply what you've learned with a fresh example.

After the practice video, complete the exercise to unlock the next lesson. If you'd like extra hands-on practice, you can also try it in the PyLearn app.

**Visual:** Hold the “Next: Practice Video” end card long enough to read.

## Production and QA checklist

- [x] Approved Kendrick / ElevenLabs v3 voice setup confirmed by the user; use the existing configuration without substitution.
- [ ] Use ElevenLabs v3 and the same voice identity throughout; no substitution.
- [ ] Verify every code sample and expected output in Python.
- [ ] Keep indexes and slices legible; visually emphasize zero-based indexing and the excluded end index.
- [ ] Do not reveal the required Lesson 6 exercise solution.
- [x] Use the agreed lesson-to-practice handoff; no app UI footage is required.
