# PyLearn Video 08 — Loops: for and while

> **MANDATORY VOICE SETTINGS — DO NOT CHANGE**
> - Voice: Kendrick
> - Model: ElevenLabs v3
> - Voice ID: the exact approved Kendrick voice ID is not recorded in the repository files reviewed; insert the verified ID from the original Runway setup before generating narration.
> - Do not guess or substitute another voice or preset. Keep the same approved voice throughout.
> - Speak narration only; do not read scene titles or bracketed production notes.

**Canonical source:** `Pylearn-build260/content/python-basics/modules/08-loops.md`, branch `ccr-c7f6fdd7-xpzi3g`.  
**Target runtime:** Approximately 7–8 minutes. Keep the required app exercise solution hidden.

## Scene 1 — Repetition without copying code

**Visual:** Show a list of four names. Start by demonstrating repeated print lines briefly, then replace them with a loop.

**Narration:**

Welcome back to PyLearn.

Imagine you have four learner names and want to display each one. You could write a separate print statement for every name. But what if the list had hundreds of names? Copying the same line again and again would be slow and difficult to maintain.

A loop lets us repeat an action without repeating the code.

**Code**
```python
names = ["Ada", "Lin", "Sam", "Omar"]

for name in names:
    print(name)
```

**Expected output**
```text
Ada
Lin
Sam
Omar
```

**Narration:**

Read this as: for each name in names, print the name.

Python takes the first item and stores it in the loop variable name. It runs the indented print line. Then it moves to the next item and repeats. When there are no more items, the loop ends.

The variable name is the current item for that turn through the loop. The name of the variable could be different, but choosing a clear name makes the code easier to understand.

## Scene 2 — Indentation and each iteration

**Visual:** Keep the code visible. Highlight one list item and the loop variable as each output line appears. Do not rush the four iterations.

**Narration:**

Notice the indentation again. The print line is inside the loop, so it runs once for every item. The line that begins with for ends with a colon, and the indented block defines the repeated action.

The loop doesn't print the whole list four times. It visits each item and prints the current name once.

Whenever you read a loop, ask two questions: what collection is it visiting, and what work happens for each item?

## Scene 3 — Use a loop to calculate a total

**Visual:** Reveal the initial total, then the loop. Animate the accumulator value changing as each score is added, and show the final output only after the loop completes.

**Code**
```python
scores = [70, 95, 88, 60]
total = 0

for score in scores:
    total += score

print(total)
```

**Expected output**
```text
313
```

**Narration:**

Loops can do more than display values. They can calculate.

We start total at zero. Then, for each score, we add that score to total. The shorthand plus-equals means take the current total, add the value on the right, and store the new total.

This pattern is called an accumulator. It starts with an initial value and updates that value as the loop processes each item.

Let's trace it. The total begins at zero. The first score is added. Then the next score is added to the updated total, and the process continues until every score has been visited.

After the loop finishes, print displays the final total: three hundred and thirteen.

## Scene 4 — Filter values with a condition

**Visual:** Show the list and an empty passed list. Highlight the condition as each score is tested. Append only values that meet the rule.

**Code**
```python
scores = [70, 95, 88, 60]
passed = []

for score in scores:
    if score >= 70:
        passed.append(score)

print(passed)
```

**Expected output**
```text
[70, 95, 88]
```

**Narration:**

A loop can also select values that meet a rule. We begin with an empty list called passed. Then we visit each score and check whether it is at least seventy.

If the condition is true, append adds that score to the passed list. If the condition is false, the program skips the append line for that item.

The result contains seventy, ninety-five, and eighty-eight. Sixty was tested, but it did not meet the condition, so it wasn't added.

This is a common pattern: visit an item, test it, and keep it if it qualifies. The same idea appears later in data analysis when we filter rows.

## Scene 5 — Process records

**Visual:** Show the records as pairs. Highlight one pair at a time and then reveal the for loop with two variables.

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

Sometimes each record contains more than one value. Here, each tuple holds a learner's name and score.

The loop uses two variables: name and score. Python unpacks each pair into those variables on each iteration.

That lets us write a readable message without repeatedly referring to numeric indexes. The first record gives Ada and eighty-eight. The next gives Lin and seventy-two, and then Sam and ninety-five.

Use clear variable names so you can tell what each part of the record represents.

## Scene 6 — Repeat while a condition is true

**Visual:** Show count beginning at 3. Highlight the condition, print line, and decrement line in order. Display each output after the iteration.

**Code**
```python
count = 3

while count > 0:
    print(count)
    count -= 1
```

**Expected output**
```text
3
2
1
```

**Narration:**

A while loop repeats as long as its condition remains true.

Here, count begins at three. While count is greater than zero, Python prints the value and subtracts one. When count reaches zero, the condition is false, so the loop stops.

Be careful with while loops. If nothing changes in a way that eventually makes the condition false, the loop may run forever.

When you already have a collection of items to process, a for loop is usually the clearer choice. A while loop is useful when repetition depends on a condition.

## Scene 7 — break and continue

**Visual:** Use a short list. Explain break and continue separately. Do not overload the screen with both examples at once.

**Code: break**
```python
scores = [70, 88, 95, 60]

for score in scores:
    if score == 95:
        break
    print(score)
```

**Expected output**
```text
70
88
```

**Narration:**

Break stops the loop immediately. In this example, Python prints seventy and eighty-eight. When the score is ninety-five, the condition becomes true and break ends the loop, so that value and later values are not printed.

Continue has a different purpose. It skips the rest of the current iteration and moves on to the next item.

**Code: continue**
```python
scores = [70, 88, 60, 95]

for score in scores:
    if score < 70:
        continue
    print(score)
```

**Expected output**
```text
70
88
95
```

**Narration:**

This time, sixty is below seventy, so continue skips the print line for that iteration. The loop then continues with the next score.

Use break or continue when it makes the algorithm clearer. They are tools, not requirements for every loop.

## Scene 8 — Recap

**Visual:** Show the concepts one at a time: for loop, accumulator, filtering, unpacking, while, break, continue.

**Narration:**

Let's recap.

A for loop visits items in a collection and runs its indented block for each item. An accumulator updates a running value, such as a total. A loop can filter items by testing a condition and keeping only the ones that qualify.

When a record contains multiple values, a loop can unpack them into clear variable names. A while loop repeats as long as its condition remains true, so make sure the condition can eventually become false. Break stops a loop, while continue skips the rest of the current iteration.

## Final call to action — required for in-app and YouTube versions

**Visual:** Show the real PyLearn navigation path to Lesson 8 and highlight its required coding exercise. Do not display the completed app exercise or unverified UI.

**Narration:**

Now it's your turn to write code yourself.

Open PyLearn and go to Lesson 8, then complete its required coding exercise. If you're watching this on YouTube, open PyLearn and find this lesson there.

Run your code, read the feedback, and fix mistakes as needed. Practice Drills are optional. Passing the required exercise is what unlocks the next lesson.

Pause this video and start coding.

## Production and QA checklist

- [ ] Verify the exact approved Kendrick voice ID before generating audio.
- [ ] Use ElevenLabs v3 and the same approved voice throughout.
- [ ] Keep production notes out of spoken narration.
- [ ] Verify all code samples and outputs in Python.
- [ ] Synchronize highlights with each loop iteration and output line.
- [ ] Do not reveal the required Lesson 8 exercise solution.
- [ ] Preserve the required PyLearn navigation ending and progression rule.
