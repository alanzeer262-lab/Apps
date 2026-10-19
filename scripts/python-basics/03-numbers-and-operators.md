# PyLearn Video 03 — Numbers and Operators

> **MANDATORY VOICE SETTINGS — DO NOT CHANGE**
> - Voice name: Kendrick
> - Model: ElevenLabs v3
> - Voice ID: the exact approved custom Kendrick ID is not present in the repository files reviewed so far. Insert the verified ID from the original Runway setup before generating audio.
> - Do not guess, select a similar voice, or use a preset. Use the same approved voice for every part.
> - Speak narration only; do not read headings, code labels, or bracketed production notes.

**Canonical source:** `Pylearn-build260/content/python-basics/modules/03-numbers-operators.md`, branch `ccr-c7f6fdd7-xpzi3g`.
**Target runtime:** Approximately 6–8 minutes.
**Purpose:** Full teaching video. Keep it separate from the guided-practice companion.

## Scene 1 — Turn minutes into hours

**Visual:** Start with an empty editor. Reveal each line only when mentioned. Ask for a prediction before running.

**Narration:**

Imagine you studied for 360 minutes this week. How many hours is that?

We know an hour has 60 minutes, so we can divide the total minutes by 60. Let's ask Python to do the calculation.

**Code**
```python
minutes = 360
hours = minutes / 60
print(hours)
```

**Expected output**
```text
6.0
```

**Narration:**

Python gives us 6.0. Notice the decimal point. Normal division uses a slash and keeps a fractional result, even when the answer is a whole number. We will use this same example to explore other operators.

## Scene 2 — The four familiar operations

**Visual:** Reveal one expression at a time. Ask learners to predict, then run the complete block.

**Code**
```python
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
```

**Expected output**
```text
13
7
30
3.3333333333333335
```

**Narration:**

Plus adds, minus subtracts, the asterisk multiplies, and the forward slash divides. The first three results are whole numbers in this example. Division gives a decimal result. Python is showing the value it calculates, not automatically formatting it for a report.

Now let's look at two operators that answer more specific questions.

## Scene 3 — Complete groups and leftovers

**Visual:** Show ten objects grouped into threes if an animation is available; otherwise use a simple number line. Then reveal each expression.

**Code**
```python
print(10 // 3)
print(10 % 3)
```

**Expected output**
```text
3
1
```

**Narration:**

Two slashes mean floor division. They tell us how many complete groups fit. Ten divided into groups of three gives three complete groups.

The percent sign gives the remainder: one is left over.

Let's use those operators with time.

**Code**
```python
minutes = 187
hours = minutes // 60
remaining_minutes = minutes % 60
print(hours)
print(remaining_minutes)
```

**Expected output**
```text
3
7
```

**Narration:**

187 minutes contains three complete hours and seven minutes remaining. We chose each operator based on the question we wanted to answer.

## Scene 4 — Division versus floor division

**Visual:** Put the two expressions side by side, highlight the extra slash in the second one, and reveal output after the run.

**Code**
```python
print(10 / 3)
print(10 // 3)
```

**Expected output**
```text
3.3333333333333335
3
```

**Narration:**

These operators are not interchangeable. A single slash gives the division result, including its fractional part. Two slashes give the number of complete groups. Choose the one that matches the question you're asking.

## Scene 5 — Powers

**Visual:** Reveal the expression, then show three small multiplication steps before displaying the result.

**Code**
```python
print(2 ** 3)
```

**Expected output**
```text
8
```

**Narration:**

Two asterisks calculate a power. Two to the power of three means two multiplied by itself three times: two times two times two. The result is eight. You will see powers again in mathematics, statistics, and machine learning.

## Scene 6 — Rounding a result

**Visual:** Show the long decimal first, then add the `round` call. Keep the second argument highlighted.

**Code**
```python
average = 79.8333333333
print(round(average, 2))
```

**Expected output**
```text
79.83
```

**Narration:**

Calculations can produce more decimal places than we want to show. Python has a built-in function called round. Here, the second argument tells Python to round to two decimal places. The displayed result is easier to read.

Remember that rounding the result for display is not the same as changing the original value stored in average.

## Scene 7 — Order of operations

**Visual:** Show the first expression and ask for a prediction. Highlight multiplication before running. Then add parentheses and run again.

**Code**
```python
result = 10 + 2 * 3
print(result)
```

**Expected output**
```text
16
```

**Narration:**

What do you expect from ten plus two multiplied by three? Python follows the usual order of operations, so multiplication happens before addition. Two times three is six, then ten plus six gives sixteen.

Now watch what happens when we add parentheses.

**Code**
```python
result = (10 + 2) * 3
print(result)
```

**Expected output**
```text
36
```

**Narration:**

The parentheses tell Python to add ten and two first. That gives twelve, and twelve multiplied by three gives thirty-six. Parentheses are useful when you need a different order, and they can make your intention clearer to another person reading the code.

## Scene 8 — Numbers need meaning and units

**Visual:** Reveal the variable names before the formulas. Show the output only after running the code.

**Code**
```python
weekly_minutes = 360
weekly_hours = weekly_minutes / 60
monthly_hours = weekly_minutes * 4 / 60
print(f"Weekly hours: {weekly_hours}")
print(f"Monthly estimate: {monthly_hours}")
```

**Expected output**
```text
Weekly hours: 6.0
Monthly estimate: 24.0
```

**Narration:**

The first calculation converts weekly minutes into hours. The second multiplies the weekly total by four to estimate four weeks, then converts minutes to hours.

A calculation can be valid Python and still answer the wrong question if we mix up what the numbers represent. Before trusting a result, ask: is this minutes or hours? Items or prices? Points or percentages? Python does not know the meaning of our units unless we keep track of them.

## Scene 9 — Predict, run, and inspect

**Visual:** Use this separate example, not the required app exercise's starting value. Show the code, pause for a prediction, then run and reveal output one line at a time.

**Code**
```python
study_minutes = 245
complete_hours = study_minutes // 60
leftover_minutes = study_minutes % 60
print(study_minutes / 60)
print(complete_hours)
print(leftover_minutes)
print(round(study_minutes * 4 / 60, 1))
```

**Expected output**
```text
4.083333333333333
4
5
16.3
```

**Narration:**

Before running this program, predict four things: the decimal number of hours, the number of complete hours, the minutes left over, and the estimated monthly hours rounded to one decimal place. Take a few seconds.

Now let's check. The decimal result is about four point zero eight hours. That contains four complete hours and five minutes remaining. The four-week estimate, rounded to one decimal place, is sixteen point three hours.

Each line answers a different question about the same duration. If your prediction was different, trace the calculation one step at a time. Check the operator, check the units, and run it again.

## Scene 10 — Recap

**Visual:** Reveal each label one at a time: arithmetic, floor division, remainder, powers, rounding, parentheses, units.

**Narration:**

Let's review.

Plus adds, minus subtracts, the asterisk multiplies, and the forward slash divides. Two slashes give the number of complete groups. The percent sign gives the remainder. Two asterisks calculate a power. The round function helps you round a number to a chosen number of decimal places. Parentheses can change the order of a calculation and make your intention clearer.

Most importantly, think about what a number means. Track its units and use variable names that explain the value. You don't need to memorize every example. Practice making a prediction, running the code, and checking whether the result makes sense.

Next, we'll work with text using strings and f-strings.

## Final call to action — watch the practice video

**Visual:** Use a neutral end card reading “Next: Practice Video”. Do not show or describe unfinished PyLearn app screens.

**Narration:**

Great work! You've finished this lesson. The next step is to watch the practice video. I recommend watching it because it will help you apply what you've learned with a fresh example.

After the practice video, complete the exercise to unlock the next lesson. If you'd like extra hands-on practice, you can also try it in the PyLearn app.

**Visual:** Hold the “Next: Practice Video” end card long enough to read.

## Production and QA checklist

- [ ] Verify the exact approved Kendrick voice ID from the original Runway setup before generating audio.
- [ ] Use ElevenLabs v3 and the same approved voice identity for every part; no substitution.
- [ ] Speak narration only; do not send headings or bracketed directions to text-to-speech.
- [ ] Verify every code sample and expected output in Python.
- [ ] Reveal output only after the matching narrated Run action.
- [ ] Keep code readable on a phone and maintain continuity with Lessons 1 and 2.
- [ ] Do not show the Lesson 3 required-exercise solution or its starting value and completed report.
- [ ] Keep one final call to action only; Practice Drills are optional and passing the required exercise unlocks the next lesson.
- [ ] Verify the real PyLearn navigation path before recording.
- [ ] Review the full rendered video at normal speed before marking it approved.
