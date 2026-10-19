# PyLearn Video 03 — Numbers and Operators

> **MANDATORY VOICE SETTINGS — DO NOT CHANGE**
> - Voice name: Kendrick
> - Model: ElevenLabs v3
> - Voice ID: the exact approved custom Kendrick ID is not present in the repository files reviewed so far. Insert the verified ID from the original Runway setup before generating audio.
> - Do not guess, select a similar voice, or use a preset. Use the same approved voice for every part.
> - Speak narration only; do not read headings, code labels, or bracketed production notes.
**Source:** `Pylearn-build260/content/python-basics/modules/03-numbers-operators.md`
**Target:** 6–8 minutes. Video complements the app lesson; do not change app content.

## Learning outcome
Use arithmetic, division, floor division, remainder, powers, rounding, precedence, and units to reason about numerical results. This is the full lesson video, not the separate guided-practice video.

## Narration and visual plan

### Scene 1 — A useful question
**Visual:** Dark editor. Type `minutes = 360`, then `hours = minutes / 60`, then `print(hours)`. Run only after the narration asks for a prediction.
**Narration:** “Imagine you studied for 360 minutes this week. How many hours is that? We could calculate it ourselves, but Python can do the arithmetic reliably. First, we store the minutes in a variable. Then we divide by 60, because an hour contains 60 minutes. Before we run it, predict the result.”
**Output:** `6.0`.
**Narration:** “Python gives us 6.0. Normal division keeps a fractional result, even when this answer is a whole number.”

### Scene 2 — The familiar operators
**Visual:** Reveal `10 + 3`, `10 - 3`, `10 * 3`, `10 / 3` one at a time; run as a compact block.
**Narration:** “Addition, subtraction, multiplication, and division use the operators you already know: plus, minus, star, and slash. Let's focus on two operators that answer different questions.”

### Scene 3 — Whole groups and what remains
**Visual:** `print(10 // 3)` then `print(10 % 3)`; show output 3 and 1 separately.
**Narration:** “Floor division, written with two slashes, tells us how many complete groups fit. Ten divided into groups of three gives three complete groups. The remainder operator, percent, tells us what is left over: one. These work together for time.”
**Visual:** Type `minutes = 187`, `hours = minutes // 60`, `remaining_minutes = minutes % 60`; reveal outputs 3 and 7.
**Narration:** “187 minutes is three complete hours and seven minutes remaining. Notice that the operators were chosen because of what we wanted to know.”

### Scene 4 — Powers, rounding, and order
**Visual:** Show `print(2 ** 3)` → `8`; then `print(round(79.8333333333, 2))` → `79.83`.
**Narration:** “Two stars mean a power. Two to the power of three is two multiplied by itself three times, which gives eight. When a decimal has too many digits, round can keep the number of decimal places you choose. Here, two means two decimal places.”
**Visual:** Show `10 + 2 * 3` → 16, then `(10 + 2) * 3` → 36.
**Narration:** “Python follows mathematical precedence: multiplication happens before addition. Parentheses change the order. Without parentheses, this result is sixteen. With parentheses around ten plus two, the result is thirty-six. Use parentheses whenever they make your intention clearer.”

### Scene 5 — Track the units
**Visual:** Build `weekly_minutes = 425`, `weekly_hours = weekly_minutes / 60`, `monthly_hours = weekly_minutes * 4 / 60`.
**Narration:** “A calculation can be syntactically correct and still answer the wrong question. Here, the variable contains minutes. Dividing by sixty converts minutes to hours. Multiplying by four estimates four weeks. Always ask: what does this number represent—minutes, hours, money, items, or scores?”
**Visual:** Add readable print lines with f-strings; run and show actual output.

### Scene 6 — Prediction and practice
**Narration:** “Pause and predict: if weekly minutes changes from 425 to 500, which results change? Take a few seconds.”
**Visual:** Hold only the relevant code for 4 seconds; then run and reveal.
**Narration:** “Now build your own report. Show decimal hours, complete hours, remaining minutes, and estimated monthly hours rounded to one decimal place. Change the input and check your prediction.”

### Recap
**Narration:** “Today you used arithmetic, floor division for complete groups, remainder for what is left, powers, rounding, and parentheses. Most importantly, you learned to check the meaning and units of a result. Next, we'll work with text using strings and f-strings.”

## Final call to action — required for YouTube and in-app versions

**Visual:** Show the PyLearn app and clearly highlight the Practice section for Lesson 3. Do not show completed exercise answers.

**Narration:**

Now it's your turn to write code yourself.

Open the PyLearn app and go to the Practice section for Lesson 3. If you're watching this on YouTube, open PyLearn and find the practice for this lesson there.

Try the exercises yourself. Write the code, run it, and use the app's feedback to check your work. It's okay to make mistakes — that's how you learn.

The lesson showed you the concepts. Now practise them yourself in PyLearn. Stop watching, open the app, and start coding!

## Production checklist

- [ ] Keep the lesson rich and complete; do not shorten teaching content to make room for practice.
- [ ] The final card explicitly names the PyLearn app's Practice section.
- [ ] YouTube viewers are explicitly told to open PyLearn and find the matching lesson practice.
- [ ] The ending does not reveal exercise solutions.
- [ ] Verify all exercise references against the current app before recording.
- [ ] Review the full rendered video at normal speed before marking it complete.


## Scene 7 — Rounding and order of operations

**Visual:** Reveal the average first, then add the round call. Keep the code large enough to read on a phone.

**Code**
```python
average = 79.8333333333
print(round(average, 2))
```

**Expected output**
```text
79.83
```

**Narration:** “Sometimes a calculation produces more decimal places than we want to show. Python has a built-in function called round. Here, we're asking it to round the value in average to two decimal places. The number two tells round how many decimal places to keep. The result is seventy-nine point eight three. Rounding can make a report easier to read, but remember that a rounded display is not the same as keeping every digit of the original value.”

**Visual:** Replace the code with the first expression. Highlight multiplication before addition. Run only after asking for a prediction.

**Code**
```python
result = 10 + 2 * 3
print(result)
```

**Expected output**
```text
16
```

**Narration:** “What do you expect: ten plus two multiplied by three? Pause and make a prediction. Python follows the usual order of operations, so multiplication happens before addition. Two times three is six, then ten plus six gives sixteen.”

**Visual:** Add parentheses and rerun.

**Code**
```python
result = (10 + 2) * 3
print(result)
```

**Expected output**
```text
36
```

**Narration:** “This time, the parentheses tell Python to add ten and two first. That gives twelve. Then twelve multiplied by three gives thirty-six. Parentheses are useful when you need a different order, and they can make your intention clearer to someone reading your code.”

## Scene 8 — A number needs meaning

**Visual:** Show the variables first, then the formula and output.

**Code**
```python
weekly_minutes = 360
monthly_hours = weekly_minutes * 4 / 60
print(monthly_hours)
```

**Expected output**
```text
24.0
```

**Narration:** “This calculation estimates monthly study hours from a weekly total. We multiply the weekly minutes by four to estimate four weeks, then divide by sixty to convert minutes into hours. The arithmetic is straightforward, but always ask what a number represents. Is it minutes or hours? Items or prices? Points or percentages? Python can calculate a result even when we accidentally mix up the meaning of two values. Clear variable names and attention to units help prevent that kind of mistake.”

## Scene 9 — Predict, run, and inspect

**Visual:** Use this separate example. Do not use the required app exercise's starting value of 425 minutes or display its completed solution.

**Code**
```python
study_minutes = 245
complete_hours = study_minutes // 60
leftover_minutes = study_minutes % 60
print(complete_hours)
print(leftover_minutes)
print(round(study_minutes / 60, 1))
```

**Narration:** “Let's combine several ideas using a different example. Imagine the total is two hundred and forty-five minutes. Before running the program, predict the number of complete hours, the minutes left over, and the final value rounded to one decimal place. Take a few seconds to work it out.”

[Leave a silent prediction pause of about four seconds.]

**Expected output**
```text
4
5
4.1
```

**Narration:** “Two hundred and forty-five minutes contains four complete hours, with five minutes remaining. As a decimal number of hours rounded to one decimal place, it is four point one. Each line answers a different question about the same duration. That's why we choose operators based on the information we want. If your prediction was different, trace the calculation one step at a time. Check the operator, check the units, and run it again.”

## Scene 10 — Recap

**Visual:** Reveal each label one at a time: arithmetic, floor division, remainder, powers, rounding, parentheses, units.

**Narration:** “Let's review. Plus adds, minus subtracts, the asterisk multiplies, and the forward slash divides. Two slashes give the number of complete groups. The percent sign gives the remainder. Two asterisks calculate a power. The round function helps you round a number to a chosen number of decimal places. Parentheses can change the order of a calculation and make your intention clearer. And finally, think about what a number means. Track its units and use variable names that explain the value. You don't need to memorize every example. Practice making a prediction, running the code, and checking whether the result makes sense.”

## Final call to action — required for in-app and YouTube versions

**Visual:** Show the real PyLearn navigation path to Lesson 3 and highlight its required coding exercise. Do not show the completed exercise, its answer, or unverified app screens. Hold the final navigation screen long enough to read.

**Narration:**

Now it's your turn to write code yourself.

Open PyLearn and go to Lesson 3, then complete its required coding exercise. If you're watching this on YouTube, open PyLearn and find this lesson there.

Run your code, read the feedback, and fix mistakes as needed. Practice Drills are optional. Passing the required exercise is what unlocks the next lesson.

Pause this video and start coding.

## Production and QA checklist

- [ ] Verify the exact approved Kendrick voice ID from the original Runway setup before generating audio.
- [ ] Use ElevenLabs v3 and the same approved voice identity for every part; no substitution.
- [ ] Speak narration only; do not send headings or bracketed directions to text-to-speech.
- [ ] Verify every code sample and expected output in Python.
- [ ] Reveal output only after the matching narrated Run action.
- [ ] Keep code readable on a phone and maintain continuity with Lessons 1 and 2.
- [ ] Do not show the Lesson 3 required-exercise solution.
- [ ] Keep the navigation ending: required coding exercise unlocks the next lesson; Practice Drills are optional.
